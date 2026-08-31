"""Convert the credit risk CSVs in data/ to typed parquet files.

Inputs (local only, never committed; see CLAUDE.md for provenance):
    data/LoanData_Bondora.csv                Bondora P2P loan book, 179,235 loans
    data/Dev_data_to_be_shared.csv           credit-card behavioural data, labelled
    data/validation_data_to_be_shared.csv    same features, no bad_flag column

Outputs (all under the gitignored data/):
    data/bondora_raw.parquet             faithful typed conversion, no rows dropped
    data/credit_card_dev.parquet         straight typed conversion
    data/credit_card_validation.parquet  straight typed conversion
    data/bondora_pd.parquet              the modelling table for the credit lecture
                                         series: seasoned loans, application-time
                                         features, and a 12-month default flag

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

Target definition: default_12m = 1 where DefaultDate (Bondora's 60+ days past
due definition) falls within 365 days of LoanDate, on loans originated at
least 365 days before the newest origination date in the file, so that every
kept loan has a complete 12-month observation window.

Run with the project environment:
    .venv/bin/python scripts/convert_credit_data.py
"""

from pathlib import Path

import polars as pl

DATA = Path(__file__).resolve().parent.parent / "data"

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


def convert_credit_card() -> None:
    for src, dst in [
        ("Dev_data_to_be_shared.csv", "credit_card_dev.parquet"),
        ("validation_data_to_be_shared.csv", "credit_card_validation.parquet"),
    ]:
        pl.read_csv(DATA / src, infer_schema_length=None).write_parquet(DATA / dst)


def main() -> None:
    raw = convert_bondora_raw()
    print(f"bondora_raw.parquet: {raw.shape}")
    pd_table = build_bondora_pd(raw)
    rate = pd_table["default_12m"].mean()
    print(f"bondora_pd.parquet: {pd_table.shape}, default_12m rate {rate:.4f}")
    convert_credit_card()
    for name in ["credit_card_dev", "credit_card_validation"]:
        shape = pl.scan_parquet(DATA / f"{name}.parquet").collect().shape
        print(f"{name}.parquet: {shape}")


if __name__ == "__main__":
    main()
