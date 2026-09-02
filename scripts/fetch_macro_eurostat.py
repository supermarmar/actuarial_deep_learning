"""Fetch the three Eurostat macro series credit lecture R1 conditions on.

Writes `credit_lectures/data/macro_eurostat.csv`, one row per country and calendar
month, so the lecture renders on a fresh clone without a network call. That CSV is
the one data file in this repository that is committed rather than gitignored: it is
around 30 kB, and a lecture nobody can render is worse than a small text file in git
history.

Three series, all public and free from Eurostat's dissemination API:

  unemployment  une_rt_m       harmonised unemployment rate, per cent of the active
                               population, seasonally adjusted, total sex and age
  inflation     prc_hicp_manr  HICP annual rate of change, all-items (CP00), per cent
  gdp_growth    namq_10_gdp    real GDP (B1GQ, chain-linked volumes), percentage
                               change on the same quarter of the previous year,
                               seasonally and calendar adjusted

The GDP series is **quarterly**, and this script holds each quarterly growth rate
constant across the three months of its quarter rather than interpolating. Holding
it constant states what was published; interpolating would invent monthly variation
that Eurostat never measured.

Countries are EE, FI and ES, the three Bondora markets with a usable at-risk panel.
SK is excluded: its median risk set is 17 loans a month, which no macro coefficient
can be identified from.

Usage:

    .venv/bin/python scripts/fetch_macro_eurostat.py
    .venv/bin/python scripts/fetch_macro_eurostat.py --start 2009-01
"""

from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request
from pathlib import Path

import polars as pl

API = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"
COUNTRIES = ["EE", "FI", "ES"]
OUT = Path(__file__).resolve().parent.parent / "credit_lectures" / "data" / "macro_eurostat.csv"

SERIES = {
    "unemployment": {
        "dataset": "une_rt_m",
        "params": {"s_adj": "SA", "age": "TOTAL", "sex": "T", "unit": "PC_ACT"},
        "freq": "monthly",
    },
    "inflation": {
        "dataset": "prc_hicp_manr",
        "params": {"coicop": "CP00", "unit": "RCH_A"},
        "freq": "monthly",
    },
    "gdp_growth": {
        "dataset": "namq_10_gdp",
        "params": {"s_adj": "SCA", "na_item": "B1GQ", "unit": "CLV_PCH_SM"},
        "freq": "quarterly",
    },
}


def fetch(dataset: str, params: dict[str, str], geo: str, start: str) -> dict[str, float]:
    """Return {period label: value} for one country and one Eurostat dataset."""
    query = {"format": "JSON", "lang": "en", "geo": geo, "sinceTimePeriod": start, **params}
    url = f"{API}/{dataset}?{urllib.parse.urlencode(query)}"
    with urllib.request.urlopen(url, timeout=120) as response:
        payload = json.load(response)

    # JSON-stat 2.0: `value` is keyed by flat index, `dimension.time.category.index`
    # maps the period label onto that index. Missing periods are simply absent.
    time_index = payload["dimension"]["time"]["category"]["index"]
    values = payload["value"]
    return {
        period: values[str(position)]
        for period, position in time_index.items()
        if str(position) in values
    }


def month_rows(series: dict[str, float]) -> list[tuple[str, float]]:
    """Monthly Eurostat labels are already `YYYY-MM`."""
    return sorted(series.items())


def quarter_rows(series: dict[str, float]) -> list[tuple[str, float]]:
    """Expand `YYYY-Qn` onto its three months, holding the published rate constant."""
    rows: list[tuple[str, float]] = []
    for label, value in sorted(series.items()):
        year, quarter = label.split("-Q")
        first = (int(quarter) - 1) * 3 + 1
        rows.extend((f"{year}-{first + offset:02d}", value) for offset in range(3))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", default="2009-01", help="earliest period, YYYY-MM")
    args = parser.parse_args()

    frames = []
    for name, spec in SERIES.items():
        expand = quarter_rows if spec["freq"] == "quarterly" else month_rows
        for geo in COUNTRIES:
            raw = fetch(spec["dataset"], spec["params"], geo, args.start)
            rows = expand(raw)
            print(f"{name:13s} {geo}  {len(raw):4d} {spec['freq']} periods "
                  f"-> {len(rows):4d} months  ({rows[0][0]} to {rows[-1][0]})")
            frames.append(pl.DataFrame(
                {"country": [geo] * len(rows),
                 "month": [period for period, _ in rows],
                 name: [value for _, value in rows]},
            ))

    merged: pl.DataFrame | None = None
    for name in SERIES:
        stacked = pl.concat([f for f in frames if name in f.columns])
        merged = stacked if merged is None else merged.join(
            stacked, on=["country", "month"], how="full", coalesce=True,
        )

    assert merged is not None
    merged = merged.sort(["country", "month"]).select(
        ["country", "month", "unemployment", "inflation", "gdp_growth"],
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "# Eurostat macro series for credit lecture R1. Public and free; no client data.\n"
        "# Committed deliberately, unlike everything else under data/, so the lecture\n"
        "# renders on a fresh clone. Rebuild with scripts/fetch_macro_eurostat.py.\n"
        "# unemployment  une_rt_m       harmonised rate, % of active population, SA\n"
        "# inflation     prc_hicp_manr  HICP all-items annual rate of change, %\n"
        "# gdp_growth    namq_10_gdp    real GDP, % change on same quarter a year\n"
        "#                              earlier, SCA, held constant across the quarter\n"
        f"# Downloaded {__import__('datetime').date.today().isoformat()} "
        f"from {API}\n"
    )
    with OUT.open("w") as handle:
        handle.write(header)
        merged.write_csv(handle)

    print(f"\nwrote {OUT.relative_to(OUT.parent.parent.parent)}: "
          f"{merged.height:,} rows, {OUT.stat().st_size / 1024:.1f} kB")
    print(merged.group_by("country").agg(
        months=pl.len(),
        first=pl.col("month").min(),
        last=pl.col("month").max(),
        missing=pl.sum_horizontal(
            pl.col("unemployment").is_null().sum(),
            pl.col("inflation").is_null().sum(),
            pl.col("gdp_growth").is_null().sum(),
        ),
    ).sort("country"))


if __name__ == "__main__":
    main()
