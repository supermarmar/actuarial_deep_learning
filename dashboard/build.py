"""Build a self-contained interactive dashboard for the freMTPL2freq portfolio.

Reads ``data/freMTPL2freq.parquet``, encodes all 678,007 policies into
column-major ``uint8`` arrays, gzips them, and injects the result into
``dashboard/template.html`` as a single base64 string. The output is one
HTML file that opens straight from disk with no server and no runtime
dependency.

Rows are sorted on a composite key before encoding. Row order carries no
meaning once ``IDpol`` is dropped, and sorting turns the low-cardinality
columns into long runs, which takes the gzipped payload from 3.6 MB to
1.6 MB.

Run it with::

    .venv/bin/python dashboard/build.py
"""

from __future__ import annotations

import base64
import gzip
import json
from pathlib import Path

import numpy as np
import polars as pl

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "data" / "freMTPL2freq.parquet"
TEMPLATE = ROOT / "dashboard" / "template.html"
OUTPUT = ROOT / "dashboard" / "dashboard.html"

# Sorting on this key maximises run lengths in the encoded columns. The order
# runs from lowest to highest cardinality so the cheapest columns compress best.
SORT_KEY = [
    "Region", "Area", "VehBrand", "VehGas", "VehPower",
    "DrivAge", "VehAge", "BonusMalus", "Density", "Exposure", "ClaimNb",
]

# Density spans 1 to 27,000 inhabitants per km2, so it is held as
# floor(log10(density) * 50) in a single byte, giving 50 codes per decade.
# Flooring rather than rounding is deliberate: the panel buckets by
# half-decade, whose edges fall on exact multiples of 25 codes, and
# floor(floor(x)/25) == floor(x/25). Rounding put 11,752 policies sitting on
# a bucket edge into the neighbouring bucket.
DENSITY_LOG_SCALE = 50.0

CATEGORICAL = ["Area", "VehBrand", "VehGas", "Region", "LearnTest"]

# Google Sans Flex, base64 woff2 under the SIL Open Font License, per the house
# design system. It lives on OneDrive, which is not always mounted, so the build
# falls back to the system stack rather than failing.
FONT_FACE = Path(
    "/Users/mervedosa/Library/CloudStorage/OneDrive-Gini/Gini - Documents"
    "/01 Guidelines/design-system/tokens/font-face.css"
)


def encode(df: pl.DataFrame) -> tuple[dict, bytes]:
    """Encode a sorted frame into a JSON header and one binary blob."""
    n = df.height
    columns: dict[str, np.ndarray] = {}
    levels: dict[str, list[str]] = {}

    # Exposure takes only 106 distinct values, so a byte code into a lookup
    # table holds it exactly rather than approximately.
    exposure_levels = sorted(df["Exposure"].unique().to_list())
    exposure_index = {v: i for i, v in enumerate(exposure_levels)}
    columns["Exposure"] = np.array(
        [exposure_index[v] for v in df["Exposure"].to_list()], dtype=np.uint8
    )

    columns["ClaimNb"] = df["ClaimNb"].to_numpy().astype(np.uint8)

    for name in CATEGORICAL:
        values = df[name].cast(pl.Utf8).to_list()
        levels[name] = sorted(set(values))
        lookup = {v: i for i, v in enumerate(levels[name])}
        columns[name] = np.array([lookup[v] for v in values], dtype=np.uint8)

    for name in ["VehPower", "VehAge", "DrivAge", "BonusMalus"]:
        columns[name] = df[name].to_numpy().astype(np.uint8)

    columns["DensityLog"] = np.floor(
        np.log10(df["Density"].to_numpy()) * DENSITY_LOG_SCALE
    ).astype(np.uint8)

    # Severity is sparse: 24,938 of 678,007 policies carry a claim amount, so
    # a dense float column would cost 2.7 MB to say nothing 96 per cent of the
    # time. Hold it as paired index and amount arrays instead.
    claim_total = df["ClaimTotal"].to_numpy()
    severity_rows = np.flatnonzero(claim_total > 0).astype(np.uint32)
    severity_amounts = claim_total[severity_rows].astype(np.float32)

    order = list(columns)
    blob = b"".join(columns[name].tobytes() for name in order)
    offsets = {name: i * n for i, name in enumerate(order)}

    severity_offset = len(blob)
    blob += severity_rows.tobytes() + severity_amounts.tobytes()

    header = {
        "n": n,
        "columns": order,
        "offsets": offsets,
        "levels": levels,
        "exposureLevels": exposure_levels,
        "densityLogScale": DENSITY_LOG_SCALE,
        "severity": {
            "count": int(severity_rows.size),
            "indexOffset": severity_offset,
            "amountOffset": severity_offset + severity_rows.nbytes,
        },
    }
    return header, blob


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(
            f"{SOURCE} is missing. data/ is gitignored, so redownload Data.zip "
            "from the course site. See CLAUDE.md."
        )

    df = pl.read_parquet(SOURCE).sort(SORT_KEY)
    header, blob = encode(df)

    payload = base64.b64encode(gzip.compress(blob, 9)).decode("ascii")

    # Totals for the unfiltered book, so the page can draw its reference lines
    # before the first pass finishes and can assert its own arithmetic.
    header["totals"] = {
        "policies": df.height,
        "exposure": float(df["Exposure"].sum()),
        "claims": float(df["ClaimNb"].sum()),
        "claimTotal": float(df["ClaimTotal"].sum()),
    }

    if FONT_FACE.exists():
        font_css = FONT_FACE.read_text(encoding="utf-8")
    else:
        font_css = "/* Google Sans Flex unavailable; falling back to the system stack. */"
        print("note: OneDrive font-face.css not found, using system fonts")

    html = TEMPLATE.read_text(encoding="utf-8")
    for placeholder, value in [
        ("__FONTFACE__", font_css),
        ("__HEADER__", json.dumps(header, separators=(",", ":"))),
        ("__PAYLOAD__", payload),
    ]:
        if placeholder not in html:
            raise SystemExit(f"template.html is missing the {placeholder} placeholder")
        html = html.replace(placeholder, value)

    OUTPUT.write_text(html, encoding="utf-8")

    print(f"rows         {header['n']:,}")
    print(f"claim rows   {header['severity']['count']:,}")
    print(f"blob         {len(blob) / 1e6:.2f} MB raw")
    print(f"payload      {len(payload) / 1e6:.2f} MB base64 gzip")
    print(f"written      {OUTPUT.relative_to(ROOT)}  ({OUTPUT.stat().st_size / 1e6:.2f} MB)")


if __name__ == "__main__":
    main()
