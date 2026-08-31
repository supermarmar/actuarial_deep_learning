# The credit risk datasets

Profiled 31 August 2026, when the two datasets were added to `data/` for the
credit lecture series. Conversion and cleaning live in
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
