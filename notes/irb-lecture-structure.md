# Lecture R2: structure, notation bridge and citation register

Working note for `credit_lectures/R2_credit-irb-capital.qmd`, produced by tasks 1 to 3 of
`notes/plans/02-irb-capital-lecture.md` on 2 September 2026. It records the section-by-section
outline, the source of each section, the notation decisions, and the regulatory citations that
survived verification.

Read this before writing any prose into `R2`. Everything settled here is settled, and
re-deriving it costs more than reading it.

## Confidentiality, applied

The A-IRB material in the guides repo derives from a real engagement. This note is committed to
a git repository, so it inherits the same bar as the lecture: **structure, regulatory
references and transferable method travel, and no portfolio specific does.** Where an omission
has to be recorded, it is recorded by category rather than by content.

Left behind entirely, and deliberately not itemised further: the source portfolio's asset class
and jurisdiction, its segmentation scheme and segment volumes, its cohort and snapshot dates,
its selected macroeconomic variables, its exclusion and downturn windows, its benchmark
discrimination levels, and its acquisition history. None of that is needed to teach the
mechanics, and Bondora carries every worked example.

## Source register

| Tag | Where it lives |
|---|---|
| `CR/` | `~/Documents/Repos/guides/docs/wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/` |
| `AIRB/` | `CR/a-irb_capital/` |
| vault | `~/Documents/Repos/vault/wiki/` |
| series | `credit_lectures/` in this repo |

---

# Task 1: the outline

Nine sections. Against each, one sentence of intent and the source of the material. The arc is
the guides' own ordering, which is the ordering a model document carries, and the lecture
inherits it rather than inventing one.

## 1. What lecture 1 left unpaid

**Intent.** Open on the debt: lecture 1's hybrid callout derived Vasicek's conditional default
probability, noted in one sentence that the IRB capital formula is the same expression with the
factor stressed instead of averaged, and stopped. This lecture follows that sentence to a
capital number, through the production sequence a bank actually runs.

**Source.** Fresh, built from `credit_lectures/01_credit-use-case.qmd` lines 723 to 785 and
from `R1`'s section "What stays with the IRB lecture", which already names the three things
that come here: the hybrid PD and its dial, the long-run average, and the capital formula.

Carries the "where this sits in the series" callout in the pattern `R1` uses, and the notation
bridge from task 2.

## 2. Why the capital exists at all

**Intent.** Establish that a risk weight is a rule about the denominator of a capital ratio,
then walk Pillar 1 from Basel I's four buckets through the standardised approach to the IRB
approach, so the reader sees what the internal model is competing against.

**Source.** `AIRB/01_introduction/01-context.md` for the arc and for $K \ge 8\% \times
\mathrm{RWA}$, $\mathrm{RWA} = K \times 12.5$ and the F-IRB against A-IRB split. Vault
`regulation/irb-approach.md` for verification of every number quoted. Rewritten throughout; the
guides' South African supervisory detail and its worked rand examples do not travel.

Keep this section short. It is context for the formula rather than the subject of the lecture,
and the temptation is to let a history of Basel eat the first quarter of the document.

## 3. Expected loss, unexpected loss and the gap capital covers

**Intent.** The spine of the lecture's first half. Build the loss distribution, place the mean
and the 99.9th percentile on it, and state which of the two provisions covers and which capital
covers. Then split the accounting expected credit loss from the regulatory expected loss and
show where they meet on a balance sheet.

**Source.** `AIRB/01_introduction/02-credit_losses.md` for the whole progression, which is
already ordered the way this section wants. Vault `methods/asrf-capital-foundation.md` for the
conditional expected loss and the asymptotic single risk factor argument. The EL shortfall
treatment, i.e. a CET1 deduction where regulatory EL exceeds provisions and Tier 2 eligibility
up to 0.6 per cent of RWA where provisions exceed it, needs a vault citation before it goes in
(task 3).

Cross-reference `R1`: the accounting side of this comparison is that lecture's subject, and the
IFRS 9 against IRB table lives there per decision 4.

## 4. Rating philosophy, and what the regulation forces

**Intent.** Define through-the-cycle, point-in-time and dynamic point-in-time by what happens
to two observable quantities across the cycle, namely grade migration and the observed default
rate within a grade. That contrast is the one a reader remembers, and it is more useful than
any definition by intent.

**Source.** `AIRB/05_modelling/pd/01-model_methodology.md` for the three-way comparison, whose
pros-and-cons table is genuinely transferable once the engagement's chosen approach and its
partner-resilience rationale are stripped out. `CR/03-definitions.md` sections "Ratings
Philosophy" and "Ratings Mobility" for the mobility framing. Vault
`methods/credit-risk-procyclicality.md` and `methods/rwa-pd-sensitivity.md` for the supervisory
preference for a stable grade PD.

The comparison table is rewritten in house voice and styled per `~/.claude/rules/html-design.md`
with a `<caption>` naming the basis. Article 180 states what each philosophy has to satisfy;
task 3 supplies the verified wording.

Close by pointing at `R1`: IFRS 9 wants the opposite philosophy out of the same data, and the
table in `R1` is the place that contrast is tabulated.

## 5. The five-step sequence

**Intent.** State the production sequence plainly, then split it into the two phases that
organise the rest of the lecture. Risk differentiation asks whether the model rank-orders.
Risk quantification asks whether the level is right.

**Source.** `AIRB/05_modelling/pd/02-model_design.md`, which states the five steps in order:
point-in-time PD estimation, risk grade assignment, long-run average PD, margin of
conservatism, regulatory PD. `AIRB/01_introduction/04-process_overview.md` for the model
document headings and for the point the lecture must not lose, namely that without the LRA
adjustment, the margin of conservatism and the downturn adjustment the same models feed IFRS 9,
so the two frameworks share a rank ordering and differ only in calibration.

This section is short and structural. Its job is to give the reader a map before section 6
walks it.

## 6. The five steps on Bondora

**Intent.** Walk the sequence end to end on a real book, and make one grade's number traceable
from scorecard output to regulatory PD in a single table. Say plainly and early that Bondora is
a peer-to-peer loan book rather than a bank's, that it carries no IRB permission, and that the
demonstration illustrates mechanics rather than producing a capital number anyone could use.

**Source.** Method from `AIRB/05_modelling/pd/03-risk-differentiation.md`,
`07-risk-quantification.md` and `08-lra.md`. Data and every figure from
`data/bondora_pd.parquet` and `credit_lectures/data/macro_eurostat.csv`. Test choices from vault
`methods/heterogeneity-testing.md`, `methods/pd-rating-scale-calibration.md` and
`methods/margin-of-conservatism-egim.md`.

Six subsections, one per step plus the traceability table.

- **6.1 The point-in-time model.** Reuse lecture 1's GLM3 specification so the two lectures
  agree, back-score the book. Written fresh against the existing lecture.
- **6.2 Risk grades.** Bin the scores, then test the bins. The design constraints are
  regulatory rather than statistical and they bind hard: at least seven non-default grades,
  each grade holding between 1 and 30 per cent of the population, monotone observed default
  rates, homogeneity within a grade and heterogeneity between adjacent grades. Chi-square for
  homogeneity, a two-proportion z-test for heterogeneity, the Herfindahl-Hirschman index for
  concentration.
- **6.3 Observed default rates.** By grade, and by grade and cohort year, so the reader sees
  the cycle move through the table.
- **6.4 The long-run average and its window.** The four-step method from `08-lra.md`, which is
  the most transferable piece of method in the whole folder: derive an economic factor from the
  Eurostat series, classify good and bad periods off it, mark the cycle peak to peak, then
  F-test observed default rate variability in the chosen window against the full window.
- **6.5 The margin of conservatism.** Category structure from vault
  `methods/margin-of-conservatism-egim.md`. Name which category each Bondora uplift falls in,
  then form the regulatory PD as the calibrated PD plus the MoC.
- **6.6 One grade, end to end.** The traceability table. This is the section's deliverable.

**Two things decided in advance, so the demonstration cannot drift.**

First, **the F-test in 6.4 is expected to reject, and rejection is the finding.** Estonia is the
only Bondora market observed through 2009, where `R1` records GDP contracting 18.6 per cent year
on year, and any sub-window compared against a window containing that contraction will show
materially different default rate variability. Report the rejection and say what it means: a
book spanning one financial crisis and one pandemic, with a lender expanding across both, cannot
support a clean long-run average period. Do not tune the window until the test passes.

Secondly, **any macro work here inherits `R1`'s restriction to Estonia.** The pooled fit across
markets returns economically backwards signs, which `R1` diagnoses as the lender's own expansion
running against the cycle in Finland and Spain. That is a known failure and rediscovering it
would waste a section.

## 7. The capital formula

**Intent.** The section lecture 1's callout was pointing at. Set up the single-factor model,
derive the conditional default probability, show that lecture 1's hybrid expression and the
regulation's risk weight are the same formula evaluated at different points of the factor
distribution, then produce a capital requirement and a risk-weighted exposure amount.

**Source.** Vault `methods/vasicek-loan-portfolio-value.md`,
`methods/single-factor-credit-risk-model-vasicek-and-belkin.md` and
`methods/asrf-capital-foundation.md` for the derivation.
`AIRB/01_introduction/02-credit_losses.md` for the guides' own statement of it, which the
lecture reconciles rather than repeats. Vault `regulation/irb-approach.md` and
`regulation/eu-crr-2013-credit-risk.md` for the prescribed correlations and the PD floor. Vault
`methods/asset-correlation-empirical-evidence.md` and
`methods/vasicek-asset-correlation-estimation.md` for whether the prescribed values hold up.
Vault `methods/granularity-adjustment-gordy-lutkebohmert.md` for the honest caveat.

Seven subsections following the plan's task 8. The figure is a plot of risk weight against PD at
the prescribed retail correlations, which makes the concavity and the effect of the PD floor
visible at once.

**Verify rather than recall, in this section above all.** The prescribed retail correlations by
sub-class and the PD floor are constants quoted from regulation, and a wrong constant discredits
the section whatever else it gets right. Read them out of the vault and quote the article. Note
also that retail exposures carry no maturity adjustment, so $\mathrm{MA}$ appears in the general
derivation and drops out of the Bondora evaluation; say so rather than letting it vanish.

## 8. What a validator asks

**Intent.** Close the loop. A model that produces a capital number still has to survive
independent challenge, and the tests divide along the same two phases as the development.

**Source.** `AIRB/06_testing_results/pd/01-risk-differentiation.md` for accuracy,
discrimination, stability, robustness, stress analysis and benchmarking.
`02-risk-quantification.md` for concentration, homogeneity, heterogeneity, migration and
calibration accuracy. `AIRB/01_introduction/05-use_tests.md` for the use test. Vault
`methods/irb-model-validation-and-rating-system-quality.md`, `methods/binomial-backtest-pd.md`,
`methods/eba-pd-backtesting-methodology.md`, `methods/multi-period-average-pd-backtesting.md`
and the `methods/somers-d-*` family.

One sentence per test on what it measures and what failing it means. The use test gets its own
paragraph, because a model built only for capital fails it and that is a governance point rather
than a statistical one.

## 9. Takeaways, copyright and references

**Intent.** The pattern `R1` and the S track already use. Numbered takeaways, an attribution
paragraph naming Mario's own methodology material as the source of the structure, and a
reference list.

**Source.** Fresh, in the series' established form.

---

## What the lecture omits, and why

Recorded by category, per the confidentiality note above.

**LGD and EAD modelling.** One paragraph each, naming what the parameter is and pointing at the
guides. The capital formula needs both as inputs and the lecture would double in length if it
modelled either. Decision 5 of the plan.

**Downturn LGD.** Named where the capital formula consumes it, and not derived. It is the LGD
track's subject.

**Defaulted assets.** The expected loss best estimate, the $\max(0, \mathrm{LGD}_{\rm DT} -
\mathrm{ELBE})$ capital treatment and the cure decomposition are named in one sentence inside
section 3, because the EL shortfall comparison needs them to make sense, and are otherwise out
of scope.

**Economic capital, Pillar 2 and stress testing.** Named once as what sits beyond the Pillar 1
number. Concentration risk, the granularity adjustment aside, belongs there.

**Counterparty credit risk, securitisation and equity exposures.** Out of scope. The lecture is
a retail loan book seen through the IRB lens.

**The standardised approach in any detail.** Present in section 2 as the thing IRB is measured
against, and not developed.

**Data engineering, data quality and governance.** The guides carry four files on it. None of it
travels, because the lecture's demonstration runs on one public parquet.

**Every portfolio specific from the source material**, per the confidentiality note.
