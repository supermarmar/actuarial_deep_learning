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

---

# Task 2: the notation bridge

The clash table below was rebuilt from a direct read of `CR/03_notation.md` rather than taken
from the plan, which compiled it by hand. Every row was checked against the file and against
`notes/ifrs9-pit-pd-research.md`, which holds the settled notation contract for the series.

The governing rule is the one `R1` already follows: **lecture 1's symbols are canon, the
guides' symbol appears in parentheses on first use so a reader can move between the two
documents, and no lecture 1 symbol is ever redefined.**

## The clash table, verified

| Symbol | Lecture 1 and the S track | `CR/03_notation.md` | Verdict |
|---|---|---|---|
| $g$ | $g_i$, the origination month of loan $i$ | $g_{i,t} = \mathrm{DPD}_{i,t}/30$, the arrears measure in missed payments | Genuine clash, both load-bearing. **R2 does not import the guides' delinquency notation at all.** See below |
| $d$ | Botha's delinquency threshold, lecture 1 section 2.1, marked spent in the contract | $d$ as the arrears threshold, $d_{i,t}$ as the instantaneous default indicator $[g_{i,t} \ge 3]$ | Partial. $d$ agrees on meaning. $d_{i,t}$ is not imported |
| $s$ | one-period survival in the S track, written $q_{i,t}$ and ${}_k p_{i,t}$ rather than $s$ | $s \ge 1$ the stickiness measure **and** $s_{i,v}$ one-period survival | Clash inside the guides themselves. R2 uses neither |
| $S$ | ${}_k p_{i,t}$ for cumulative survival, so $S$ is unspent in this series | $S_{i,t}$ cumulative survival, $\mathrm{S}_{t'}$ the standardised systemic factor, $\mathrm{S}_{99.9}$ its stressed value | Clash inside the guides themselves. R2 writes the factor $Z_u$, following lecture 1 |
| calendar time | $u$ | $t'$ | Cosmetic. State the mapping once, as `R1` does |
| default outcome | $D^{(k)}_{i,t}$ | $D^*_{i,t}(k,p)$, with probation period $p$ | Reconcilable. The guides carry a probation period and lecture 1 does not. R2 names probation once, in the definition-of-default aside, and does not carry $p$ into any formula |
| normal CDF | $\Phi(\cdot)$ | $N(\cdot)$; the CRR itself writes $N(\cdot)$ and $G(\cdot)$ for the inverse | Cosmetic, and worth stating because the reader will meet $G(\cdot)$ in the regulation |
| asset correlation | $\rho$, lecture 1's loading on the systematic factor | $\rho$ in the guides' prose; **the CRR writes it $R$** | New row, not in the plan. $R_i$ is spent as Botha's four-level exit variable in S1. **R2 keeps $\rho$** and states once that the regulation writes the same quantity $R$ |
| the systematic factor | $Z_u \sim {\cal N}(0,1)$, high values benign, entering as $-\sqrt{\rho}\, Z_u$ | three different conventions, see below | The dangerous row |

## The sign convention is a three-way problem, not a two-way one

The plan records one disagreement. A direct read finds three, and only one of them is a
disagreement with this series.

1. **`CR/03_notation.md`** defines the systemically conditional PD as $N\!\left(\left(N^{-1}
   (\mathrm{PD}^{\rm TTC}) + \mathrm{FLI}_{t'}\sqrt{\rho}\right)/\sqrt{1-\rho}\right)$, with a
   **plus**. This is the disagreement `R1` already records and resolves under
   $\mathrm{FLI}_u = -Z_u$.
2. **`AIRB/01_introduction/02-credit_losses.md`** derives the same quantity from
   $X_i = \mathrm{S}_{t'}\sqrt{\rho} + Z_i\sqrt{1-\rho}$ and default at $X_i < c_i$, reaching
   $N\!\left(\left(N^{-1}(p^*) - \mathrm{S}_{t'}\sqrt{\rho}\right)/\sqrt{1-\rho}\right)$, with a
   **minus**. Since the same file sets $\mathrm{S}_{t'} = (\mathrm{FLI}_{t'} - \mu)/\sigma$,
   the two guides files contradict each other unless $\mathrm{FLI}$ is read as
   stress-oriented in one and benign-oriented in the other. **The minus form is the correct
   derivation and it agrees with lecture 1.**
3. The same file then writes $\mathrm{S}_{99.9^{\rm th}} = N^{-1}(0.999)$ while using
   $+\sqrt{\rho}\,N^{-1}(0.999)$ in the worst-case default rate. Those reconcile only if the
   stressed factor is the **0.1st** percentile, $\mathrm{S} = -N^{-1}(0.999)$. The label is
   wrong and the formula is right.

So lecture 1 agrees with the guides' derivation and differs from the guides' notation table.
`R1` states the mapping for the notation table; R2 states it once more and adds the stressed
substitution, since that substitution is R2's own subject.

## The one displayed equation task 2 step 4 asks for

R2 writes this as display mathematics rather than describing it in prose, because a reader
checking lecture 1's hybrid formula against the regulation's risk weight will otherwise
conclude that one of them has a sign error.

$$
Z_u = -\Phi^{-1}(0.999)
\quad\Longrightarrow\quad
\mathrm{PD}^{\rm hyb}_{12}\left(\boldsymbol{X}_i, Z_u\right)
= \Phi\!\left(\frac{\Phi^{-1}\!\left(\mathrm{PD}^{\rm TTC}_{12}\right) + \sqrt{\rho}\,\Phi^{-1}(0.999)}{\sqrt{1-\rho}}\right)
= \mathrm{WCDR} ,
$$

which is the regulation's $N\!\left(\left(G(\mathrm{PD}) + \sqrt{R}\,G(0.999)\right)/\sqrt{1-R}\right)$
under $N = \Phi$, $G = \Phi^{-1}$ and $R = \rho$. The algebra is trivial. The labelling is what
is dangerous, so the lecture spends its words there.

## The arrears measure: non-adoption

The plan proposes $a_{i,t} = \mathrm{DPD}_{i,t}/30$ as a replacement letter for the guides'
$g_{i,t}$, and asks whether $a$ is free. It is: the single grep hit is `\hat\eta_{i,t}`, which
matches the pattern and is not a symbol $a$.

**R2 adopts no arrears symbol.** The cheapest resolution is non-adoption, on exactly the
reasoning that dropped three of plan 1's four proposed symbols. R2's scope is PD only, lecture 1
already owns the default definition through Botha's threshold $d$ and the window flag
$D^{(k)}_{i,t}$, and neither Bondora modelling table carries a days-past-due field, so nothing
in the lecture can be indexed by an arrears measure. Where the guides' delinquency machinery
needs naming, R2 names it in prose inside the definition-of-default aside and defines no symbol.

A lower-case $a$ would also have sat one case distinction away from lecture 1's $A_i$, the
borrower's age at origination, which is 13 occurrences of a live symbol. Introducing it to
carry nothing would be the worst of both outcomes.

## What R2 actually adds

Nine symbols, all of them the regulation's own, which is the point: a reader who has met the
CRR should recognise every one on sight.

| Symbol | Meaning | Scope note |
|---|---|---|
| $\mathrm{EL}$, $\mathrm{UL}$ | expected and unexpected loss, per unit of exposure | Free across the series |
| $\mathrm{LGD}$, $\mathrm{EAD}$ | loss given default and exposure at default | Free across the series. Named, not modelled |
| $K$ | the capital requirement per unit of exposure | Lecture 2 uses $K_Y(s)$ for a cumulant generating function and lectures 3 and 6 use $K$ for a count. Different documents, so no in-lecture clash, and $K$ is the regulation's own letter |
| $\mathrm{RWA}$ | risk-weighted exposure amount, $\mathrm{RWA} = 12.5 \, K \times \mathrm{EAD}$ | Free |
| $\mathrm{WCDR}$ | worst-case default rate, the conditional PD at the 99.9th percentile | Free |
| $\mathrm{MA}$, with $b$ and $M$ | the maturity adjustment, its factor $b$, and effective maturity $M$ | $b$ is free in series mathematics. $M$ is lecture 6's count of nagging networks and lecture 2's moment generating function, so state the scope. Retail carries no maturity adjustment, so all three appear in the general derivation and drop out of the Bondora evaluation |
| $\mathrm{MoC}$ | margin of conservatism, an additive uplift on the calibrated PD | Free |
| $\mathrm{PD}^{\rm Reg}$ | the regulatory PD, i.e. calibrated PD plus MoC | New superscript in the series' existing style |
| $j$ | the risk grade index, $j = 1, \dots, J$ | $j$ is a covariate index in lectures 1, 3, 4-5 and 6 and a bin index in S1. R2 has no covariate index in display mathematics, so $j$ is free here. State it once |

$\rho$, $\lambda$, $Z_u$, $\Phi$, $\mathrm{PD}^{\rm TTC}$, $\mathrm{PD}^{\rm PiT}$,
$\mathrm{PD}^{\rm hyb}$ and $\overline{\mathrm{DR}}^{(12)}$ all arrive from lecture 1 and `R1`
unchanged and are not redefined.

## The FiT reading, and `R1` agrees

Settled by Mario on 2 September 2026 and already stated in `R1` at the callout "The scaling
route is not closed on [0, 1], so the series takes the probit form". Verified by direct read on
2 September 2026: `R1` adopts the probit form as the definition of a FiT PD, names the
multiplicative factor as the practitioner shortcut, gives the reason (the guides' own FLI
methodology derives $\mathrm{FLI}_u$ as a ratio of two fitted PDs, so it is an output and cannot
also be the primitive entering a probit), and states the mapping $\mathrm{FLI}_u = -Z_u$.

R2 states the same reading in one sentence and cross-references `R1` rather than re-arguing it.
The two lectures must not drift, so any future change to one is a change to both.

---

# Task 3: the citation register

Every regulatory citation the guides make, checked against the vault and, where the vault is
silent and a primary document sits on disk, against that. A citation appears in `R2` only if it
carries a consequence, so the register states the consequence alongside the reference. A
citation that cannot state one does not go in.

Verified on 2 September 2026.

## The decision the plan did not name: which rulebook vintage

The guides cite CRR 2013 article numbers beside PRA SS4/24 (January 2026) and PS9/24. Those are
two rulebooks a decade apart, and the vault holds material on both, including
`regulation/crr-credit-risk-provisions.md` on CRR3 and
`regulation/pra-crr-rulebook-restatement-2025.md`.

**`R2` teaches the Basel framework and cites the CRR 2013 numbering the guides use, states once
in a callout that CRR3 and the PRA's 2025 rulebook restatement renumber the articles and tighten
the input floors, and attempts no article-by-article mapping.** The reason is that the mechanics
the lecture teaches are unchanged across the two vintages while the numbering is not, and an
unverified mapping would be worse than an explicit statement of vintage. UK expectations are
cited at SS4/24 **section** level throughout, for the reason in the next-but-one subsection.

The vault itself shows why the mapping is dangerous. `crr-credit-risk-provisions.md` reports
CRR3 placing PD floors in Article 170, LGD floors in Article 179 and CCF floors in Article 180,
which is irreconcilable with the 2013 numbering where 170 is rating system structure, 179 is the
overall estimation requirements and 180 is PD estimation. One of the two numberings is being
described and the vault article is the only support for it. **Treat that claim as uncertain and
do not build on it.**

## Verified against primary text on disk

Source: `~/Documents/Repos/vault/raw/bcbs/2005-07_bcbs_irb-risk-weight-functions-explanatory-note.pdf`,
which is the Basel Committee's own explanatory note on the IRB risk weight functions and the
document the guides link to as `bis.org/bcbs/irbriskweight.pdf`. Extracted with `pdftotext
-layout` and read directly.

| Claim | Consequence it imposes on the lecture |
|---|---|
| $K = \left[\mathrm{LGD}\cdot N\!\left((1-R)^{-0.5}G(\mathrm{PD}) + (R/(1-R))^{0.5}G(0.999)\right) - \mathrm{PD}\cdot\mathrm{LGD}\right](1-1.5b)^{-1}(1+(M-2.5)b)$ | This is the formula `R2` derives. Note it is algebraically identical to the guides' $N\!\left((G(\mathrm{PD})+\sqrt{R}\,G(0.999))/\sqrt{1-R}\right)$ form, and showing that equality is a one-line check worth putting in the lecture |
| $b(\mathrm{PD}) = (0.11852 - 0.05478\ln \mathrm{PD})^2$ | The maturity adjustment factor, quoted rather than recalled |
| $\mathrm{RWA} = 12.5 \times K \times \mathrm{EAD}$, where 12.5 is the reciprocal of the 8 per cent minimum ratio | Explains why the conversion factor is 12.5 rather than an arbitrary constant, which is the kind of detail a reader remembers |
| The confidence level is fixed at 99.9 per cent | Fixes $Z_u = -\Phi^{-1}(0.999)$ in the substitution from task 2 |
| Corporate: $R = 0.12\,w + 0.24(1-w)$ with $w = (1-e^{-50\,\mathrm{PD}})/(1-e^{-50})$ | The contrast that makes the retail values legible |
| **Residential mortgages: $R = 0.15$** | Prescribed, constant |
| **Qualifying revolving retail: $R = 0.04$** | Prescribed, constant |
| **Other retail: $R = 0.03\,w + 0.16(1-w)$ with $w = (1-e^{-35\,\mathrm{PD}})/(1-e^{-35})$** | **Bondora is unsecured consumer lending, so this is the curve the demonstration uses.** The $k$-factor is 35 rather than the corporate 50, so the correlation decays more slowly in PD |
| Retail risk weight functions carry **no maturity adjustment**, because the reverse-engineered correlations already contain maturity effects that were never separately controlled for | $\mathrm{MA}$, $b$ and $M$ appear in the general derivation and drop out of the Bondora evaluation, and the lecture says why rather than letting them vanish |
| The conditional expected loss is the product of a conditional PD and a downturn LGD, and capital covers the gap between it and the expected loss | The sentence section 3 rests on |
| The retail correlations were reverse-engineered from banks' economic capital figures and G10 supervisory loss data | The honest provenance of the constants. They are calibrated to observed capital, so calling them empirical estimates of an asset correlation overstates what they are |

## Verified against the vault

| Citation | What it requires | Vault source |
|---|---|---|
| CRR Article 180(1)(a) | PD must be a long-run average of one-year default rates for the grade or pool | `regulation/eu-crr-2013-credit-risk.md` |
| 0.03 per cent PD floor | Applies to non-defaulted **corporate, institution and central government** exposures under CRR 2013. **Not verified for retail** | same |
| CRR Article 181(1)(b) | LGD estimates must reflect economic downturn conditions, with the methodology left to the institution subject to supervisory review | same |
| CRR Article 178 | Defines default by the 90-days-past-due backstop and unlikeliness to pay; 178(5) sets the conditions for return to non-defaulted status | same, and `regulation/crr-credit-risk-provisions.md` |
| CRR Article 143 | IRB use requires explicit supervisory permission, granted at approach level rather than portfolio level | `regulation/crr-credit-risk-provisions.md` |
| F-IRB against A-IRB | Under F-IRB only PD is internally estimated; **retail exposures may only be treated under A-IRB** | `regulation/eu-crr-2013-credit-risk.md` |
| EBA/GL/2017/16 | PD estimates represent a long-run average of one-year default rates; the reference period must capture a representative range of economic conditions including stress; where it falls short, apply a margin of conservatism rather than merely extending the window | `regulation/irb-pd-estimation.md` |
| PRA SS4/24 section 4 | The use test is substantive. A firm holding IRB models solely for regulatory capital reporting does not satisfy it and faces revocation or partial-use restriction | `regulation/pra-ss4-24-irb-approach-2026.md` |
| PRA SS4/24 sections 7 to 11, 21 | Section 7 rating system design including the number of grades; section 8 data representativeness; section 9 margin of conservatism; section 10 PD model development; section 11 PD calibration to the long-run average default rate; section 21 independent validation covering discriminatory power, calibration accuracy and stability | same |

**One correction to carry into the lecture.** The guides state that for retail the foundation and
advanced approaches are merged and all banks using A-IRB supply their own PD, LGD and EAD. The
vault's reading of the CRR is stronger: retail exposures may **only** be treated under A-IRB.
`R2` follows the vault.

## Partially verified: section right, paragraph unverified

The vault covers SS4/24 at section level and carries no paragraph numbering. Each guides
citation below falls in a section whose subject matches, so the reference is consistent and the
paragraph itself is unconfirmed.

| Guides citation | Subject | Section check |
|---|---|---|
| SS4/24 10.10 | PiT, TTC and a blend are all permissible rating philosophies | Section 10 is PD model development. Consistent |
| SS4/24 11.13 | Considerations in choosing the LRA period, namely ODR variability, the balance of good and bad years against the relevant macro variables, and structural change | Section 11 is PD calibration. Consistent |
| SS4/24 11.10(c) | Overlapping performance windows are permitted, with an analysis of the bias from overweighting the overlap | Section 11. Consistent |
| SS4/24 11.31 | PDs must increase monotonically across grades | Section 11. Consistent |
| SS4/24 11.20 | Quantitative and qualitative validation tests during risk quantification | Section 11, though **validation is section 21**, so this one sits least comfortably. Flag if used |
| SS4/24 12.2 | Two defaults within nine months are treated as one for LGD | Section 12 is LGD general expectations. Consistent, and out of scope anyway |

**Rule for `R2`.** Cite these as "SS4/24 section 11" with the requirement stated, and give the
paragraph number only where a reader can check it. The requirement is what the lecture is
teaching, and a paragraph number nobody verified adds risk without adding meaning.

## Unverified: do not repeat

| Citation | Why it fails verification |
|---|---|
| CRR Article 180(2)(a), 180(2)(e) | The vault carries 180(1)(a) only, and does not say what paragraph 2 covers. The plan's claim that `08-lra.md` contradicts itself is **wrong**: that file is consistent on 180(2)(a) and 180(2)(e) throughout, and the 180(1)(a) citation is in `05_modelling/pd/02-model_design.md`. Most likely Article 180 splits paragraph 1 for corporate, institution and sovereign exposures from paragraph 2 for retail, in which case both guides files are right for different exposure classes and one is misapplied. The vault cannot settle it, so `R2` cites **Article 180 at article level** and states the requirement |
| CRR Articles 169(3), 170(3)(b), 170(3)(c), 171(1), 172(2), 174, 179 | No paragraph-level coverage anywhere in the vault, and the CRR3 renumbering the vault reports makes the numbers actively unsafe. The **requirements** are transferable and go in the lecture as design constraints; the article numbers stay out |
| CRR Article 144(1)(b), the use test | The vault covers the use test through SS4/24 section 4. Cite that instead |
| CRR Article 154, retail risk weights, and the retail PD floor | The correlations themselves are verified from the BCBS note above, which is the substance. The CRR article number is not, so `R2` attributes the constants to the Basel framework |
| PS9/24 paragraph 3.129, dynamic recalibration with a buffer | The vault holds `_meta/sources/pra-ps9-24-app2-crr-near-final.md` and no paragraph-level coverage. State the practice, drop the citation |
| EL shortfall: CET1 deduction, and Tier 2 eligibility up to 0.6 per cent of RWA | Nothing in the vault. The guides are the only source, and the 0.6 per cent is a number worth being wrong about. State the mechanism, mark the threshold as one to check against the CRR own funds articles before the lecture asserts it |
| Seven non-default grades and one default grade, ratings reviewed annually, three years of demonstrated use | Guides only. These are well-known Basel II minimum requirements, so state them as such rather than citing an article |

## What this leaves the lecture

The mathematics is fully sourced from primary text. The regulatory framing is sourced at
requirement level and, for the UK, at SS4/24 section level. The exposed edges are three article
numbers (180's paragraph split, the 170 and 171 grade-structure requirements, and Article 154),
and the EL shortfall threshold.

**Closing them is a vault ingest rather than a lecture task.** The CRR primary text is not in
`vault/raw/`, and EUR-Lex would not render through `WebFetch` on 2 September 2026. Registering
`Regulation (EU) No 575/2013` and PRA SS4/24 in the vault would settle all four at once and would
serve every future piece of IRB work rather than this lecture alone. Recorded here as a
follow-up, not a blocker: `R2` can be written in full without them by citing at the levels above.

---

# Handover to the writing session

Tasks 1 to 3 are done and committed. Tasks 4 to 11 write and render the lecture, and they run
on Sonnet. Five things a fresh session needs that the register above does not already carry.

## 1. Another session is committing to this branch

Commits `7b2ce01`, `9a0f7d4` and `6055734` landed on `feat/credit-survival-lectures` interleaved
with tasks 1 to 3 on 2 September 2026, from a session working on credit lecture 2 and on the
causal-inference research note. The working tree was clean afterwards and nothing was lost.

**Two tasks are collision points.** Task 10 edits `credit_lectures/01_credit-use-case.qmd` and
task 11 edits `CLAUDE.md`, both of which another session may hold. Re-read each file immediately
before editing rather than trusting a line number, `git pull` where the branch has a remote, and
keep task 10's commit separate from `R2`'s as the plan already requires.

## 2. `R1` asserts a PD floor this register marks unverified

`R1`'s IFRS 9 against IRB comparison table gives the IRB floor as 0.03 per cent. The vault
verifies 0.03 per cent for non-defaulted **corporate, institution and central government**
exposures under CRR 2013 and says nothing about retail, and the same vault reports CRR3 raising
the floor to 0.05 per cent.

So a retail-relevant floor is asserted in one committed lecture and unverified in this register.
**Do not silently inherit `R1`'s number as verified when writing task 8.** State the floor with
its exposure class and its vintage, or state it as the widely applied Basel II value and say the
CRR3 figure differs. Leave `R1` alone; this is a note for the writer, not an erratum.

## 3. Three arrangements of the same formula, so name the canon

The task 2 substitution targets the CRR's arrangement,
$N\!\left(\left(G(\mathrm{PD}) + \sqrt{R}\,G(0.999)\right)/\sqrt{1-R}\right)$. The BCBS
explanatory note writes the same quantity as
$N\!\left((1-R)^{-0.5}G(\mathrm{PD}) + \left(R/(1-R)\right)^{0.5}G(0.999)\right)$. Lecture 1
writes it a third way, as $\Phi\!\left(\left(\Phi^{-1}(\mathrm{PD}^{\rm TTC}) - \sqrt{\rho}\,
Z_u\right)/\sqrt{1-\rho}\right)$ with the factor unstressed.

All three are the same expression. **`R2` displays lecture 1's arrangement as canon**, since the
series already owns it and it is the one the reader has met, then shows the other two as
one-line rearrangements. The equality is trivial and the point of showing it is that a reader
meeting the BCBS note or the CRR will otherwise think they have found a different formula.

## 4. The other-retail correlation moves along the x-axis

Task 8 step 4 plots the risk weight against PD. For residential mortgages and qualifying
revolving retail the correlation is a constant and the curve is straightforward. For **other
retail**, which is the class Bondora falls in,
$R = 0.03\,w + 0.16(1-w)$ with $w = (1-e^{-35\,\mathrm{PD}})/(1-e^{-35})$, so $R$ has to be
recomputed at every PD on the axis.

Holding $R$ fixed at some average produces a plausible-looking curve that is not the
regulation's. Compute $R$ per point, and plot all three retail curves together so the reader
sees what the PD dependence does to the shape.

## 5. Grade construction on Bondora will bind on monotonicity, not volume

Task 7 step 2 has 148,733 seasoned loans, a floor of seven non-default grades, and a per-grade
bound of 1 to 30 per cent of the population. Volume is not the binding constraint at that sample
size: 1 per cent is 1,487 loans and seven grades is easily cleared.

**The binding constraint will be monotone observed default rates in the thin high-risk grades**,
where a few hundred defaults drive the rate and adjacent grades cross over. Size the grades
against default counts rather than against volume alone, and expect the iterative merge step the
guides describe to be doing real work rather than being a formality.
