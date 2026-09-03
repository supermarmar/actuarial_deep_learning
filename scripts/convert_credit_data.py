"""Convert the credit risk CSVs in data/ to typed parquet files.

Inputs (local only, never committed; see CLAUDE.md for provenance):
    data/LoanData_Bondora.csv                        Bondora P2P loan book, 179,235 loans
    data/Dev_data_to_be_shared.csv                   credit-card behavioural data, labelled
    data/validation_data_to_be_shared.csv            same features, no bad_flag column
    data/amex-default-prediction/train_data.csv      Amex monthly statement panel, 15 GB
    data/amex-default-prediction/train_labels.csv    one target per customer

Outputs (all under the gitignored data/):
    data/bondora_raw.parquet             faithful typed conversion, no rows dropped
    data/credit_card_dev.parquet         straight typed conversion
    data/credit_card_validation.parquet  straight typed conversion
    data/bondora_pd.parquet              the modelling table for the credit lecture
                                         series: seasoned loans, application-time
                                         features, and a 12-month default flag
    data/bondora_survival.parquet        the survival table for the S-series
                                         lectures: every loan, its observed
                                         duration, and how it left the risk set
    data/amex_panel.parquet              faithful typed conversion of the customer-month
                                         panel, no rows dropped, target joined on
    data/amex_cross_section.parquet      one row per customer at their earliest
                                         statement, the Bondora-style analogue of
                                         amex_panel.parquet: application-time features
                                         plus a matured outcome, restricted to customers
                                         with a full 13-month history

Typing strategy for the Bondora file: the CSV encodes missing values as empty
strings and writes decimals like ".6800", so whole-file schema inference leaves
81 of 112 columns as strings. After replacing empty strings with nulls, each
remaining string column is cast to Date, Datetime, Int64 or Float64 in that
order of preference, and a cast is adopted only when it parses every non-null
value. Genuine label columns (Rating, Status, WorkExperience, ...) survive as
strings because no cast wins losslessly.

The modelling table keeps application-time information only. Everything Bondora
records after origination is excluded by construction, because those columns
leak the outcome into the covariates: Status, DefaultDate, ActiveLateCategory,
WorseLateCategory, CurrentDebtDays*, DebtOccuredOn*, the payment and balance
columns (PrincipalBalance, *PaymentsMade, *WriteOffs, *Overdue*, *PostDefault,
*TillDate, *DebtServicingCost), the recovery columns (EAD1, EAD2,
*Recovery, RecoveryStage, StageActiveSince, GracePeriod*, ReScheduledOn,
Restructured, NextPayment*, NrOfScheduledPayments, LastPaymentOn,
ContractEndDate, MaturityDate_Last), and Bondora's own model outputs computed
over the life of the loan (ExpectedLoss, LossGivenDefault, ExpectedReturn,
ProbabilityOfDefault, EL_V0/V1, Rating_V0/V1/V2, ModelVersion). Rating itself
is kept: it is assigned at listing time, and the lectures use it to discuss
modelling on top of another model's output.

Target definition: default_12m = 1 where DefaultDate (Bondora's own platform
flag, declared at a median 79 days past due rather than on a fixed threshold;
see credit lecture D1) falls within 365 days of LoanDate, on loans originated at
least 365 days before the newest origination date in the file, so that every
kept loan has a complete 12-month observation window.

Survival table: bondora_survival.parquet answers a different question and so
takes a different shape. It keeps all 179,235 loans rather than the seasoned
148,733, because a survival likelihood wants a short-seasoned loan as a
censored observation rather than as a dropped one, and it records when each
loan left the risk set rather than whether it defaulted inside a fixed window.
Exits are encoded three ways. A loan exits as `default` on its DefaultDate,
which takes precedence over Status: 10,743 loans are Repaid yet carry a
DefaultDate, having defaulted and later recovered, and default is absorbing,
so scoring them as settlements would discard them. A loan exits as `settled`
where Status is Repaid and no DefaultDate exists, on its ContractEndDate.
Everything else is `censored` at ReportAsOfEOD, which covers the 57,611
Current loans and the 8,064 Late loans carrying no DefaultDate. That gives
71,416 defaults, 42,144 settlements and 65,675 censored observations.
Settlement is a competing risk rather than censoring, which is why the exit
kind travels in the file: a table carrying only the binary event indicator
would have baked prepayment-as-censoring into the data irreversibly.

ContractEndDate is on the leakage exclusion list above and is nonetheless read
here, deliberately. The exclusion protects a fixed-horizon target, where
knowing when the loan ended leaks the outcome into the covariates. A survival
model's response IS the exit time, so the same column is the response rather
than a covariate. It never enters the survival table as a feature; only the
derived duration and exit kind do.

Typing strategy for the Amex file: unlike Bondora's CSV, train_data.csv is
already numeric everywhere except five columns (customer_ID, the S_2 statement
date, the two categorical columns D_63 and D_64, and the binary flag B_31), so
there is no need for the Bondora file's per-column cast search. The 185
anonymised feature columns go straight to Float32, which quarters the file's
memory footprint against Float64 with no loss Amex's own anonymisation would
have destroyed anyway. At 15 GB the file does not fit the read-then-write
pattern used above, so the conversion runs through polars' lazy scan_csv and
sink_parquet instead of read_csv and write_parquet.

Amex cross-section: bondora_pd.parquet is a snapshot at origination with a
matured outcome. amex_panel.parquet has no equivalent single snapshot, since
every customer contributes one row per monthly statement, so
amex_cross_section.parquet manufactures one: each customer's earliest
statement stands in for "at origination", restricted to the 386,034 customers
(84 per cent) who hold the full 13-month history, so every kept customer
shares the same observation window. The target is unaffected by which
statement is kept, since Amex defines it 120 days after each customer's last
statement regardless.

Home Credit revolving cards: home_credit_cards.parquet is the one table taken
from the Kaggle "Home Credit Default Risk" competition
(https://www.kaggle.com/competitions/home-credit-default-risk), namely
credit_card_balance.csv, 3,840,312 monthly statements across 104,307 card
facilities held by 103,558 customers. It is here because it is the only public
panel in this repo that carries a month-stamped days-past-due field, which is
what a definition of default needs: a delinquency threshold and a persistence
requirement are claims about a sequence of monthly states, and neither Bondora
nor the Amex extract records one. Two columns carry the clock. SK_DPD is days
past due in the month and SK_DPD_DEF is the same figure after a materiality
tolerance, so the pair puts Article 178's materiality limb in two columns
rather than in prose; 48,377 statements reach 90 days on the first and 1,078 on
the second. MONTHS_BALANCE counts backwards from the application, so ordering
ascending gives chronological order. The archive ships ten tables and nine are
left alone, bureau_balance included: it keys on SK_ID_BUREAU and bridges to the
rest only through the bureau table, and its STATUS field collapses 120+ days
past due, sale and write-off into one bucket, which is the opposite of what a
lecture separating those events wants. Only credit_card_balance.csv and the
column dictionary are copied into data/home-credit-default-risk/.

Run with the project environment:
    .venv/bin/python scripts/convert_credit_data.py                    # bondora + credit card
    .venv/bin/python scripts/convert_credit_data.py --datasets amex    # amex only
    .venv/bin/python scripts/convert_credit_data.py --datasets home_credit
    .venv/bin/python scripts/convert_credit_data.py --datasets bondora credit_card amex
"""

import argparse
from pathlib import Path

import polars as pl

DATA = Path(__file__).resolve().parent.parent / "data"
AMEX = DATA / "amex-default-prediction"
HOME_CREDIT = DATA / "home-credit-default-risk"

DATE_FORMATS = ["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"]

# Application-time columns for the modelling table, grouped as in the Bondora
# data dictionary. LoanId, LoanNumber and LoanDate come along as identifiers
# and vintage, not as covariates.
APPLICATION_COLUMNS = [
    # loan terms as listed
    "AppliedAmount", "Amount", "Interest", "LoanDuration", "MonthlyPayment",
    "UseOfLoan", "Rating",
    # borrower demographics
    "Age", "Gender", "Country", "County", "City", "LanguageCode",
    "Education", "MaritalStatus", "NrOfDependants",
    # employment and income
    "EmploymentStatus", "EmploymentDurationCurrentEmployer",
    "EmploymentPosition", "WorkExperience", "OccupationArea",
    "HomeOwnershipType",
    "IncomeFromPrincipalEmployer", "IncomeFromPension",
    "IncomeFromFamilyAllowance", "IncomeFromSocialWelfare",
    "IncomeFromLeavePay", "IncomeFromChildSupport", "IncomeOther",
    "IncomeTotal",
    # liabilities and affordability
    "ExistingLiabilities", "LiabilitiesTotal", "RefinanceLiabilities",
    "DebtToIncome", "FreeCash",
    # application metadata and credit history on the platform
    "VerificationType", "NewCreditCustomer",
    "ApplicationSignedHour", "ApplicationSignedWeekday", "MonthlyPaymentDay",
    "NoOfPreviousLoansBeforeLoan", "AmountOfPreviousLoansBeforeLoan",
    "PreviousRepaymentsBeforeLoan", "PreviousEarlyRepaymentsBefoleLoan",
    "PreviousEarlyRepaymentsCountBeforeLoan",
]


def _lossless_cast(s: pl.Series) -> pl.Series:
    """Return s cast to the strictest type that parses every non-null value."""
    non_null = s.drop_nulls()
    if non_null.is_empty():
        return s
    for fmt in DATE_FORMATS:
        parsed = non_null.str.to_datetime(fmt, strict=False)
        if parsed.null_count() == 0:
            if fmt == "%Y-%m-%d":
                return s.str.to_date(fmt, strict=False)
            return s.str.to_datetime(fmt, strict=False)
    as_float = non_null.cast(pl.Float64, strict=False)
    if as_float.null_count() == 0:
        cast = s.cast(pl.Float64, strict=False)
        if (as_float == as_float.round(0)).all() and (as_float.abs() < 2**62).all():
            return cast.cast(pl.Int64)
        return cast
    return s


def convert_bondora_raw() -> pl.DataFrame:
    df = pl.read_csv(DATA / "LoanData_Bondora.csv", infer_schema_length=None)
    empties_to_null = [
        pl.col(c).replace("", None) for c, t in df.schema.items() if t == pl.String
    ]
    df = df.with_columns(empties_to_null)
    df = df.with_columns(
        [_lossless_cast(df[c]) for c, t in df.schema.items() if t == pl.String]
    )
    df.write_parquet(DATA / "bondora_raw.parquet")
    return df


def build_bondora_pd(raw: pl.DataFrame) -> pl.DataFrame:
    horizon_end = raw["LoanDate"].max()
    df = (
        raw.filter(pl.col("LoanDate") + pl.duration(days=365) <= horizon_end)
        .with_columns(
            default_12m=(
                (pl.col("DefaultDate") - pl.col("LoanDate")).dt.total_days() <= 365
            )
            .fill_null(False)
            .cast(pl.Int8),
            # data cleaning: 53 seasoned loans carry Age below Bondora's minimum of 18
            Age=pl.when(pl.col("Age") >= 18).then(pl.col("Age")),
        )
        .select(["LoanId", "LoanNumber", "LoanDate", *APPLICATION_COLUMNS, "default_12m"])
    )
    df.write_parquet(DATA / "bondora_pd.parquet")
    return df


# Mean Gregorian month in days, matching the convention lecture 1 uses to turn
# date differences into months on book.
MONTH = 30.4375


def build_bondora_survival(raw: pl.DataFrame) -> pl.DataFrame:
    """Build the survival table: one row per loan, with its exit time and kind.

    Unlike bondora_pd.parquet this keeps every loan, because a survival
    likelihood wants the short-seasoned loans as censored observations rather
    than dropped ones. See the module docstring for the exit encoding and for
    why ContractEndDate is admitted here after being excluded there.

    Args:
        raw: the faithful conversion written by convert_bondora_raw.

    Returns:
        One row per loan: identifiers, vintage, the observed duration in months
        and in whole months, the exit kind, the event indicator, the available
        observation window, and the application covariates.
    """
    tau = raw["ReportAsOfEOD"][0]
    defaulted = pl.col("DefaultDate").is_not_null()
    repaid = pl.col("Status") == "Repaid"

    df = (
        raw.with_columns(
            exit_kind=pl.when(defaulted)
            .then(pl.lit("default"))
            .when(repaid)
            .then(pl.lit("settled"))
            .otherwise(pl.lit("censored")),
            # Defaults exit on DefaultDate whatever Status says afterwards.
            # Settlements exit on the contract end, falling back to the
            # original maturity for the 809 repaid loans that carry no end
            # date. Everything else is still at risk and is censored at tau.
            exit_date=pl.when(defaulted)
            .then(pl.col("DefaultDate"))
            .when(repaid)
            .then(pl.coalesce(["ContractEndDate", "MaturityDate_Original"]))
            .otherwise(pl.lit(tau)),
            # data cleaning: 53 loans carry Age below Bondora's minimum of 18
            Age=pl.when(pl.col("Age") >= 18).then(pl.col("Age")),
        )
        # 855 settled loans carry an end date after the snapshot, i.e. a
        # scheduled date rather than the actual early repayment. Capping at tau
        # is the longest exposure consistent with the loan having ended by then.
        .with_columns(exit_date=pl.min_horizontal("exit_date", pl.lit(tau)))
        .with_columns(
            t_obs=(pl.col("exit_date") - pl.col("LoanDate")).dt.total_days() / MONTH,
            A=(pl.lit(tau) - pl.col("LoanDate")).dt.total_days() / MONTH,
            delta=(pl.col("exit_kind") == "default").cast(pl.Int8),
        )
        # Whole months at risk, floored at 1: a loan exiting inside its first
        # month still contributes that month to the discrete-time risk set.
        .with_columns(t_obs_m=pl.col("t_obs").ceil().clip(lower_bound=1).cast(pl.Int32))
        .select(
            [
                "LoanId", "LoanNumber", "LoanDate",
                "t_obs", "t_obs_m", "exit_kind", "delta", "A", "Status",
                *APPLICATION_COLUMNS,
            ]
        )
    )
    df.write_parquet(DATA / "bondora_survival.parquet")
    return df

def convert_credit_card() -> None:
    for src, dst in [
        ("Dev_data_to_be_shared.csv", "credit_card_dev.parquet"),
        ("validation_data_to_be_shared.csv", "credit_card_validation.parquet"),
    ]:
        pl.read_csv(DATA / src, infer_schema_length=None).write_parquet(DATA / dst)


# The one Home Credit table the definition-of-default lecture needs. Its
# columns are documented in HomeCredit_columns_description.csv, shipped in the
# same archive: SK_DPD is "DPD (Days past due) during the month on the previous
# credit" and SK_DPD_DEF the same "with tolerance (debts with low loan amounts
# are ignored)", which is a materiality threshold in a column rather than in
# prose. MONTHS_BALANCE counts backwards from the application, so -1 is the
# month before it and -96 the earliest observed.
def convert_home_credit_cards() -> None:
    """Convert the Home Credit revolving-card panel to a typed parquet.

    Faithful conversion in the shape of convert_bondora_raw: every row, every
    column, no derivation. The delinquency indicators the lecture builds on top
    (arrears in payments, an instant-default flag, probation and cure) are
    derived inside the lecture, so that changing a dial there does not mean
    rebuilding the file.
    """
    src = HOME_CREDIT / "credit_card_balance.csv"
    df = pl.read_csv(src, infer_schema_length=None).sort(
        ["SK_ID_PREV", "MONTHS_BALANCE"]
    )
    df.write_parquet(DATA / "home_credit_cards.parquet")


# Columns whose true type is not "one of the 185 anonymised Float32 features":
# the identifier, the statement date, the two string-coded categoricals, and
# the one binary flag. Verified against the full file: D_63 and B_31 carry no
# nulls, D_64 carries empty strings that convert_amex_panel nulls out.
AMEX_NON_FLOAT_OVERRIDES: dict[str, type[pl.DataType]] = {
    "customer_ID": pl.Utf8,
    "S_2": pl.Utf8,
    "D_63": pl.Utf8,
    "D_64": pl.Utf8,
    "B_31": pl.Int8,
}


def _amex_schema_overrides(path: Path) -> dict[str, type[pl.DataType]]:
    """Build the scan_csv schema_overrides dict for an Amex statement file.

    Args:
        path: CSV to read the header row from.

    Returns:
        One entry per column: the true type for the five non-float columns,
        Float32 for every other (anonymised feature) column.
    """
    columns = pl.read_csv(path, n_rows=0).columns
    return {c: AMEX_NON_FLOAT_OVERRIDES.get(c, pl.Float32) for c in columns}


def convert_amex_panel() -> None:
    """Stream train_data.csv and train_labels.csv to amex_panel.parquet.

    Writes one row per customer-month statement, target joined on, with no
    rows dropped. Runs under polars' lazy scan_csv/sink_parquet, since the
    15 GB source does not fit the read_csv/write_parquet pattern used for the
    other three files.
    """
    train_path = AMEX / "train_data.csv"
    overrides = _amex_schema_overrides(train_path)
    panel = pl.scan_csv(train_path, schema_overrides=overrides).with_columns(
        pl.col("S_2").str.to_date("%Y-%m-%d"),
        pl.col("D_64").replace("", None),
    )
    labels = pl.scan_csv(
        AMEX / "train_labels.csv",
        schema_overrides={"customer_ID": pl.Utf8, "target": pl.Int8},
    )
    panel.join(labels, on="customer_ID", how="left").sink_parquet(
        DATA / "amex_panel.parquet"
    )


def build_amex_cross_section() -> None:
    """Build amex_cross_section.parquet: the Bondora-style Amex analogue.

    Keeps each customer's earliest statement as the "at origination" snapshot,
    restricted to the 386,034 customers holding the full 13-month history, so
    every kept customer shares the same observation window. See the module
    docstring for why the target is unaffected by which statement is kept.
    """
    panel = pl.scan_parquet(DATA / "amex_panel.parquet")
    eligible = (
        panel.group_by("customer_ID")
        .agg(pl.len().alias("n_statements"))
        .filter(pl.col("n_statements") == 13)
        .select("customer_ID")
    )
    cross_section = (
        panel.join(eligible, on="customer_ID", how="inner")
        .sort(["customer_ID", "S_2"])
        .group_by("customer_ID", maintain_order=True)
        .first()
    )
    cross_section.collect().write_parquet(DATA / "amex_cross_section.parquet")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--datasets",
        nargs="+",
        choices=["bondora", "credit_card", "amex", "home_credit"],
        default=["bondora", "credit_card"],
        help="which datasets to rebuild (default: bondora credit_card; amex "
        "reads a 15 GB CSV and home_credit wants a Kaggle download, so both "
        "are opt-in)",
    )
    args = parser.parse_args()

    if "bondora" in args.datasets:
        raw = convert_bondora_raw()
        print(f"bondora_raw.parquet: {raw.shape}")
        pd_table = build_bondora_pd(raw)
        rate = pd_table["default_12m"].mean()
        print(f"bondora_pd.parquet: {pd_table.shape}, default_12m rate {rate:.4f}")
        surv = build_bondora_survival(raw)
        kinds = surv["exit_kind"].value_counts().sort("count", descending=True)
        counts = ", ".join(f"{k} {n:,}" for k, n in kinds.iter_rows())
        print(f"bondora_survival.parquet: {surv.shape}, {counts}")

    if "credit_card" in args.datasets:
        convert_credit_card()
        for name in ["credit_card_dev", "credit_card_validation"]:
            shape = pl.scan_parquet(DATA / f"{name}.parquet").collect().shape
            print(f"{name}.parquet: {shape}")

    if "amex" in args.datasets:
        convert_amex_panel()
        panel_shape = pl.scan_parquet(DATA / "amex_panel.parquet").select(
            pl.len(), pl.col("customer_ID").n_unique()
        ).collect()
        print(f"amex_panel.parquet: {panel_shape.row(0)} (rows, customers)")

        build_amex_cross_section()
        cross = pl.scan_parquet(DATA / "amex_cross_section.parquet")
        cross_shape = cross.select(pl.len()).collect().item()
        cross_rate = cross.select(pl.col("target").mean()).collect().item()
        print(f"amex_cross_section.parquet: ({cross_shape}, ...), target rate {cross_rate:.4f}")

    if "home_credit" in args.datasets:
        convert_home_credit_cards()
        panel = pl.scan_parquet(DATA / "home_credit_cards.parquet")
        shape = panel.select(
            pl.len(), pl.col("SK_ID_PREV").n_unique(), pl.col("SK_ID_CURR").n_unique()
        ).collect()
        print(f"home_credit_cards.parquet: {shape.row(0)} (rows, facilities, customers)")


if __name__ == "__main__":
    main()
