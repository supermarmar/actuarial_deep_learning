# The credit risk datasets

Profiled 31 August 2026, when the first two datasets were added to `data/` for
the credit lecture series; the Amex panel below was added and profiled the
same day once it arrived. Conversion and cleaning live in
`scripts/convert_credit_data.py`; this note records what the files are and the
decisions taken on them. The lecture built on top is
`credit_lectures/01_credit-use-case.qmd`.

## Bondora loan book (`LoanData_Bondora.csv`, 150 MB)

The full origination history of Bondora, an Estonian peer-to-peer consumer
lender, as published in the platform's public reports
(<https://www.bondora.com/en/public-reports>). The extract is dated
2021-07-20 and holds 179,235 loans originated between February 2009 and July
2021 across Estonia (110,714), Finland (41,955), Spain (26,270) and Slovakia
(296). There are 112 columns spanning the application (demographics, income
decomposition, liabilities, platform history), the contract (amount,
interest, duration), and the loan's subsequent life (payments, arrears,
recoveries, write-offs) together with Bondora's own model outputs (Rating,
ProbabilityOfDefault, ExpectedLoss, LossGivenDefault, EAD1/EAD2).

The CSV is raw. Missing values arrive as empty strings, decimals are written
like `.6800`, and 53 seasoned loans carry an age below Bondora's contractual
minimum of 18. Whole-file schema inference therefore leaves 81 columns as
strings; the conversion script nulls the empties and adopts a Date, Datetime,
Int64 or Float64 cast per column only where it parses every non-null value.

### Files produced

- `bondora_raw.parquet`: all 179,235 rows, all 112 columns, typed.
- `bondora_pd.parquet`: the modelling table for the lecture series. 148,733
  loans with a complete 12-month observation window, 45 application-time
  columns, identifiers, `LoanDate` as vintage, and the target `default_12m`
  (DefaultDate within 365 days of origination). The 12-month default rate is
  28.95 per cent.

### The leakage census

Everything Bondora records after origination is excluded from the modelling
table by construction. The excluded groups are the outcome fields (Status,
DefaultDate, ActiveLateCategory, WorseLateCategory, CurrentDebtDays and
DebtOccuredOn variants), the payment and balance columns (balances, payments
made, write-offs, overdue amounts, post-default schedules, servicing costs),
the recovery columns (EAD1, EAD2, recoveries, RecoveryStage, grace periods,
rescheduling), and the platform's own lifetime model outputs (ExpectedLoss,
LossGivenDefault, ExpectedReturn, ProbabilityOfDefault, EL and Rating
versions, ModelVersion). `Rating` itself is kept because it is assigned at
listing time; the lectures use it to discuss modelling on another model's
output. The full list sits in the conversion script's docstring.

### Points worth remembering

- `DefaultDate` is Bondora's own default event (entry into collection), so
  the target is a platform definition rather than an Article 178 flag. A
  regulatory model would rebuild the flag from arrears at more than 90 days
  past due.
- The book is violently non-stationary: vintage default rates run from 7 per
  cent (2012) to 37 per cent (2017), and volume grows by two orders of
  magnitude. Out-of-time splits must respect `LoanDate`.
- Declared income is confounded by country (Simpson's paradox): the marginal
  default rate rises with income while every within-country profile falls.
  Lecture 1 builds its interaction argument on this.
- `Interest` is the platform's price of risk and near-perfectly rank-orders
  default (9 per cent below a 10 per cent coupon, 78 per cent above 100 per
  cent). It is endogenous and stays out of the covariate set.
- Later lectures can extend to LGD and EAD using the recovery columns of
  `bondora_raw.parquet`.

## Credit card behavioural pair (`Dev_data_to_be_shared.csv`, `validation_data_to_be_shared.csv`, 420 MB)

An anonymised credit card portfolio distributed as a development/validation
pair, by its naming and structure a data-science competition release; the
original source should be confirmed before anything derived from it is
shared. The development file holds 96,806 accounts with a `bad_flag` at 1.42
per cent; the validation file holds 41,792 accounts and **no** `bad_flag`,
so honest evaluation requires splitting the development file. Both carry
1,215 anonymised features in four blocks: `onus_attribute` (48),
`transaction_attribute` (664), `bureau` (452) and `bureau_enquiry` (50).

The pair converts to `credit_card_dev.parquet` and
`credit_card_validation.parquet` unchanged. Its role in the series is the
opposite of Bondora's. The features carry no meaning a modeller could
interpret, so GLM storytelling is impossible, and the 1.42 per cent bad rate
reproduces the rare-event regime of insurance claims. It is reserved for the
lectures where wide anonymised data and class imbalance are the point, e.g.
regularisation, embeddings at scale and the deep learning comparisons.

## Amex default prediction panel (`amex-default-prediction/`, 47 GB)

The Kaggle "American Express Default Prediction" competition data
(<https://www.kaggle.com/competitions/amex-default-prediction>, run 2022),
downloaded 31 August 2026. Unlike the two datasets above, this one is a
genuine panel rather than a cross-section: `train_data.csv` (15 GB) holds one
row per customer-month statement, 5,531,451 rows over 458,913 customers, with
`S_2` as the statement date. Statement counts per customer run from 1 to 13;
386,034 customers (84 per cent) hold the full 13 months, and every customer's
history ends in March 2018, so the panel is right-aligned on a common
cut-off rather than staggered by origination. The observation window runs
2017-03-01 to 2018-03-31. `train_labels.csv` (29 MB) carries one `target` per
customer, 25.89 per cent positive.

The 190 columns are anonymised and prefix-coded by risk domain: 96 `D_`
delinquency, 40 `B_` balance, 28 `R_` risk, 22 `S_` spend and 3 `P_` payment
variables, almost all Float in roughly [0, 1] though not bounded there
(`P_2` runs from -0.38 to 1.01). Three columns are not float: `D_63` and
`D_64` are string categoricals (`CL/CO/CR/XL/XM/XZ` and `-1/O/R/U`, the
latter with true empty-string nulls) and `B_31` is a 0/1 flag. Missingness is
severe and structured: in a full-file column scan, 30 columns run more than
50 per cent null and `D_87`/`D_88` are 99.9 per cent null, while 70 columns
carry no nulls at all. `test_data.csv` (32 GB) covers 924,621 customers from
2018-04-01 to 2019-10-31, an out-of-time window by construction, but the
competition never released test labels, so `sample_submission.csv` gives
nothing but customer IDs; it and `test_data.csv` are not converted. Two facts
below come from the competition documentation rather than the files
themselves, so they are flagged as such.

### Files produced

- `amex_panel.parquet` (2.97 GB): the faithful typed panel, all 5,531,451
  rows, 191 columns, `target` joined on, no rows dropped. The 185 anonymised
  feature columns are cast to Float32 rather than Float64, which quarters
  the file's memory footprint with no loss the platform's own anonymisation
  would not already have imposed.
- `amex_cross_section.parquet` (220 MB): the Bondora-style analogue. Each
  customer's **earliest** statement stands in for "at origination",
  restricted to the 386,034 customers with a full 13-month history so every
  kept customer shares the same observation window; everything in between is
  discarded by construction, the same way Bondora's post-origination columns
  are excluded from `bondora_pd.parquet`. The target rate is 23.18 per cent,
  lower than the panel's headline 25.89 per cent, because the 13-statement
  restriction skews the cohort toward customers who stayed active and in
  good standing for the full year rather than closing or defaulting early.

### Points worth remembering

- Per Kaggle's documentation (not derivable from the files): `target` is
  failure to pay the statement balance within 120 days of the customer's
  **last** statement, and Amex added random noise to the anonymised
  features. Because the outcome window anchors to the last statement
  regardless of which statement is kept as the modelling snapshot, the
  cross-section's target is identical to the panel's; only the covariates
  change between the first-statement and last-statement framings.
- The panel gives two distinct ways to imitate a cross-section, and they are
  not the same experiment. `amex_cross_section.parquet` takes the first
  statement, an application-style snapshot with the outcome maturing over the
  following twelve months plus 120 days, restricted to a fixed cohort. Taking
  the **last** statement instead would give a behavioural scorecard as at the
  March 2018 cut-off with all 458,913 customers kept and the headline 25.89
  per cent bad rate preserved; that variant was not built, since the first
  statement is the one that mirrors Bondora.
- This is the only one of the three datasets where the sequence itself is a
  modelling object rather than something flattened away before release. The
  credit card pair's 664 `transaction_attribute` and 452 `bureau` columns
  are almost certainly behavioural aggregates over lookback windows,
  computed from a panel like this one before the file was ever released;
  that reading is inference from the shape of the columns, not a documented
  fact, and should be hedged accordingly if it is used in a lecture. Amex
  hands over the raw material those aggregates would have been built from,
  which makes it the natural fit for the attention and Credibility
  Transformer lectures later in the series.
- `train_data.csv` at 15 GB does not fit a `read_csv`/`write_parquet` pass;
  `convert_amex_panel` streams it through polars' lazy `scan_csv` and
  `sink_parquet` instead. `--datasets amex` in `convert_credit_data.py` is
  opt-in for this reason and is not part of the script's default run.
