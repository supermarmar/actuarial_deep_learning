# Lecture D1: structure, measured facts and notation bridge

Working note for `credit_lectures/D1_credit-default-definition.qmd`. It records what was
measured rather than assumed, which symbols the lecture may spend, and where its boundary with
the neighbouring lectures runs.

Read this before writing prose into `D1`. Everything settled here is settled, and re-deriving it
costs more than reading it. The citation register lives beside this file in
`notes/default-definition-citations.md`, because regulatory verification and empirical
measurement have different failure modes and mixing them hides both.

## Confidentiality, applied

**This repository became public on 3 September 2026.** Assume anything committed here is
published on landing. That raises the bar this note inherits from
`notes/irb-lecture-structure.md` rather than merely restating it: **structure, public regulatory
references and transferable method travel, and no portfolio specific does.**

The A-IRB definitions material in the guides repo derives from a real engagement. Left behind
entirely, and deliberately not itemised further than this: that firm's chosen materiality
threshold, its pulling-effect percentage, its statement about historical technical defaults, its
maximum recovery period, its data-control sampling volumes, and the conclusion of its own
probation-period study. What travels is that a materiality threshold exists under the CRR and is
a firm's choice, and that probation length trades cure rate against re-default rate. Bondora and
the public Home Credit panel carry every worked example, and both are public downloads.

## Source register

| Tag | Path | Role |
|---|---|---|
| `BOND` | `data/bondora_raw.parquet` | Bondora public loan book, extract 2021-07-20 |
| `HC` | `data/home_credit_cards.parquet` | Kaggle Home Credit `credit_card_balance`, converted |
| `HCDICT` | `data/home-credit-default-risk/HomeCredit_columns_description.csv` | The competition's own column dictionary |
| `CR/` | `~/Documents/Repos/guides/docs/wiki/.../credit_risk/` | Pointer to primary sources only |
| `vault` | `~/Documents/Repos/vault` | Regulatory primary text |

## Where D1 sits, and what it does not own

D1 owns the **target-variable layer**, meaning what the response column is and how a definitional
dial changes it. Four neighbours own the rest, and D1 cross-references each rather than
re-deriving it.

Lecture 1 fixes the outcome window and coins the worst-ever aggregation. `R1` owns the estimation
layer and already derives the marginal PD, so D1 defines the three targets and hands their
estimation over. `R2` owns the capital formula and the worst-case default rate. The S track owns
the hazard machinery.

`R3_credit-sampling-and-representativeness` is being written concurrently and sits closest, so
the boundary is stated here to stop both lectures writing the same material. **D1 builds the
outcome variable, and R3 picks the rows.** D1 covers the delinquency chain, the dials, cure,
probation, write-off, and the construction of the response column. R3 covers which observations
enter the sample, meaning sampling windows, exclusions, representativeness and stratification.
Data quality assessment sits with D1 only where it bears on whether the outcome can be built at
all.

# Task 1: the outline

Fourteen sections. Definitions run 1 to 7, section 8 is the joint, engineering runs 9 to 10.

## 1. Where lecture 1 stopped

**Intent.** Open on the debt. Lecture 1 named default three times without finishing the job, and
one measured claim in it was wrong. State the correction, preview the four dials and three
targets.

**Source.** Lecture 1's dials table and its outcome-window section. Demonstration 1 below.

## 2. Terminology and notation

**Intent.** Fix the vocabulary and the symbol table before any formula appears. This is the
terminology section the brief asks for, and it is the densest section in the lecture.

**Source.** Synthesis across lecture 1, `R1` and `R2`, corrected against direct reads where the
planning notes disagree with the rendered lectures. Two such corrections are recorded in task 2.

## 3. The four dials and the state machine

**Intent.** Formalise the delinquency indicator completely for the first time in the series,
since lecture 1 could only state it, and add probation as the fourth dial governing the return
path. Draw the state diagram, reusing `R1`'s five-state space without redefining it.

**Source.** Botha, Oberholzer, Larney and de Jongh (2023), pending the citation register.

## 4. The three targets

**Intent.** The apex. Separate three quantities that practice, lecture 1 and the guides all call
some version of the twelve-month PD, and show that two of them are routinely conflated.

**Source.** Original synthesis. Demonstration 8 gives the empirical size of the gap.

## 5. Cure

**Intent.** Define cure as the transition back to performing, distinct from settlement. Give the
probation condition its formal content, then measure what a snapshot extract can and cannot say
about it.

**Source.** CRR Article 178(5), pending the register. Demonstrations 2, 3 and 7.

## 6. Write-off

**Intent.** Define derecognition as an absorbing state distinct from both default and cure.
Extend lecture 1's life table with a write-off decrement.

**Source.** IFRS 9's write-off paragraph, pending the register. Demonstration 4.

## 7. SICR, bounded from above by default

**Intent.** Place SICR as the upstream trigger, bounded above by the default definition, since a
defaulted exposure is already Stage 3. Hand the staging-horizon consequence to `R1`.

**Source.** `R1`'s staging paragraph. No demonstration, deliberately: the honest way to bound a
section is to spend no code on it.

## 8. From definition to data shape

**Intent.** The joint. One paragraph restating four dials as claims about what a table must
contain. Short enough to quote back in one breath.

**Craft warning.** A short section carrying a turn in the argument is where machine cadence bites
hardest. No one-line paragraph for gravitas, and no colon doing a full stop's work.

## 9. Bondora: what a snapshot extract cannot show

**Intent.** Ground section 8 in one real extract's columns. Demonstration 5.

## 10. Home Credit: what a monthly panel adds

**Intent.** The data engineering proper. Panel shape, the join key, the cleaning the outcome
build actually requires, and the three sweeps. Demonstrations 6, 7 and 8.

## What the lecture omits, and why

Severity, meaning LGD and EAD, belongs to the guides and is named once. Hazard estimation of any
of the three targets belongs to the S track and `R1`. A fitted multistate transition matrix
belongs to `R1`, so D1's state machine stays a picture. SICR beyond section 7 is a lecture in its
own right. Sampling, exclusions and representativeness belong to `R3` under the boundary above.
Rebuilding lecture 1's GLMs under a ninety-day flag changes no conclusion and is not attempted.
Nine of the Home Credit archive's ten tables are never read.

# Task 2: measured facts

Every figure below was computed directly from the file named, and the lecture recomputes each one
in its own chunks rather than quoting this note.

## The Bondora declaration lag, and what settles it

The load-bearing question was what `DebtOccuredOn` measures, because the whole correction turns on
it. On the 68,480 late loans carrying both fields,
`ReportAsOfEOD - DebtOccuredOn - CurrentDebtDaysPrimary` equals exactly 1 from the tenth to the
ninetieth percentile. `DebtOccuredOn` therefore starts the days-past-due counter, and
`DefaultDate - DebtOccuredOn` is genuinely days past due at declaration.

Of 67,712 loans carrying both dates, 7,917 show a lag of exactly zero and 101 show a negative one,
both of which are named in the lecture as anomalies rather than dropped in silence. On the 59,694
with a strictly positive lag the percentiles run 1, 21, 48, 74, 79, 92, 122 and 126 days at the
1st, 5th, 10th, 25th, 50th, 75th, 90th and 99th. Some 15.4 per cent are declared under sixty days,
57 per cent fall between sixty and ninety, and 28 per cent reach ninety or beyond.

**The finding is that no single threshold exists.** Lecture 1's error was quoting sixty as though
Bondora ran a rule, when the flag is an operational collection decision with a median of 79 days.

Months on book at default: the minimum is 1.61, no default precedes month one, exactly one
precedes month two, 259 precede month three, and 7,499 precede month four. Lecture 1's
outcome-window argument and S1's zero first-month hazard both survive on these numbers.

## Bondora cure and write-off

Cure splits two ways and the English word hides it. 19,287 loans reach a late bucket, carry no
`DefaultDate`, and end `Repaid`, of which 460 reached the 180-plus bucket without ever being
flagged. Separately 10,743 loans carry a `DefaultDate` and end `Repaid`. Only the second is cure
in the regulatory sense, since only there was a default declared.

Write-off: 7,745 loans carry a positive `PrincipalWriteOffs` while `RecoveryStage` is populated for
111,940, so entering recovery and being written off are separate transitions whose base rates
differ by more than an order of magnitude.

## The Home Credit panel

3,840,312 monthly statements, 104,307 card facilities, 103,558 customers, `MONTHS_BALANCE` from
-96 to -1. History length per facility runs 6, 10, 21, 74 and 95 months at the 10th, 25th, 50th,
75th and 90th percentiles, with a maximum of 96.

The materiality pair is the sharpest single fact in the lecture. Reaching ninety days, `SK_DPD`
fires on 48,377 statements and `SK_DPD_DEF` on 1,078. The two disagree on 64,439 statements, and
47,299 cross ninety days on the raw count while staying below it once the tolerance applies.
`HCDICT` documents `SK_DPD_DEF` as the same figure "with tolerance (debts with low loan amounts
are ignored)", so this is a materiality threshold expressed in a column.

## The three sweeps

The dial sweep, counting facilities ever meeting the delinquency indicator:

| d | s=1 | s=2 | s=3 |
|---|---|---|---|
| 30 | 3,162 | 2,221 | 1,841 |
| 60 | 2,192 | 1,807 | 1,647 |
| 90 | 1,806 | 1,647 | 1,536 |

One book, and the defaulted population moves by a factor of 2.06 between the loosest and tightest
setting. Neither dial is usually written down.

The probation sweep, at a ninety-day threshold and one-month persistence, on facilities with room
after the first default to observe probation plus a twelve-month re-default window:

| p | risk set | cured | cure rate | re-defaulted | re-default rate |
|---|---|---|---|---|---|
| 3 | 1,615 | 997 | 61.7% | 98 | 9.8% |
| 6 | 1,583 | 906 | 57.2% | 42 | 4.6% |
| 9 | 1,559 | 839 | 53.8% | 21 | 2.5% |
| 12 | 1,520 | 778 | 51.2% | 14 | 1.8% |
| 18 | 1,423 | 631 | 44.3% | 9 | 1.4% |
| 24 | 1,321 | 498 | 37.7% | 7 | 1.4% |

The trade-off is the whole argument. Lengthening probation suppresses re-default and destroys
cures at the same time, and the re-default curve flattens between eighteen and twenty-four months,
which is where the diminishing return sets in. Note where the CRR's own minimum sits on that
curve, subject to the register confirming the minimum.

The three targets, at a ninety-day threshold over a twelve-month horizon, on the 2,694,925
performing loan-months carrying a full forward window:

| Target | Definition | Count | Rate |
|---|---|---|---|
| Worst-ever | max over the window | 20,303 | 0.753% |
| Point-at-horizon | status at the horizon | 16,082 | 0.597% |
| Marginal | first default dated at the horizon | 1,612 | 0.060% |

Two readings carry the section. 20.8 per cent of worst-ever positives are point-at-horizon
negatives, having cured or lapsed before the horizon. And 90.0 per cent of point-at-horizon
positives were already in default earlier in the window, so that flag counts a stock where an
expected-loss sum needs a flow, and it is twelve times the marginal quantity it is often mistaken
for.

# Task 3: the notation bridge

Lecture 1's symbols are canon. The guides' symbol may appear in parentheses on first use, and no
lecture 1 symbol is ever redefined.

## Two errata found by direct read

`notes/ifrs9-pit-pd-research.md` and `R1`'s inherited-symbols table gloss `A_i` as the borrower's
age at origination. **That is wrong.** Lecture 1 defines `A_i = tau - g_i` as months of
observation available and never uses it for age. `R2`'s bridge declined the lowercase arrears
symbol partly on the strength of that gloss, so the stated reason does not hold and D1 takes the
letter.

`notes/irb-lecture-structure.md` records that `S` is unspent in this series. **Also wrong.** `R1`
uses a bare `S` for the absorbing settled state in its Markov section. D1 therefore adopts no `S`
and discusses settlement in prose.

## The clash table

| Symbol | Clash | Resolution |
|---|---|---|
| `g` | Lecture 1's vintage, lecture 1's own delinquency counter, the guides' arrears measure | Keep the first two, adopt neither third |
| `a` | Free, subject to the `A_i` erratum above | D1 spends it on the arrears measure in payments |
| `D` | Lecture 1's window indicator against `R1`'s Markov state label | Both kept. The indicator always carries a sub- or superscript and the state label never does |
| `S` | See the erratum | Not spent by D1 |
| `d` | The delinquency threshold against lecture 1's decrement counts | Bare `d` is the threshold, superscripted is a decrement. D1 adds a write-off decrement |
| `p` | Probation against the series' survival probability and `R1`'s transition probability | Every existing use carries a subscript. Bare unsubscripted `p` is the probation period |
| `tau` | Fixed and unsubscripted here, subscripted in the source literature | Restate the convention, introduce no subscripted form |

The arrears measure in payments and the guides' day-count-over-thirty coincide only where
instalments are monthly and equal. That holds for Bondora's instalment loans and fails for a
revolving card, so the lecture states it once and keeps the two apart.
