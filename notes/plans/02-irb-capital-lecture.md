# Plan 2: an IRB capital lecture

> **For a fresh session.** This plan is self-contained and assumes no memory of the
> conversation that produced it. Read it top to bottom before touching a file. Steps
> carry checkboxes so progress survives an interruption. Repo root is
> `/Users/mervedosa/Documents/Repos/actuarial_deep_learning`; every path below is
> relative to it unless it starts with `~` or `/`. The comment asked for a plan that
> could be run in a separate Claude session, and this is it.

**Answers:** review comment 2 of round 3, recorded verbatim in
`notes/lecture-1-review-comments-2026-09-01.md`. The comment reads:

> For this section I think this will become an IRB lecture which I think I have done
> some good work on in my guides repo in the wiki and lecture folder so read through
> that to get the structure and story and we can plan this out as well and create a
> second plan to run in another Claude session. It can be briefly mentioned here

**Goal:** grow lecture 1's hybrid PD callout into an IRB capital lecture that follows the
production sequence a bank actually runs, from a point-in-time scorecard through risk
grades, long-run average calibration and a margin of conservatism to the regulatory PD,
and then through the Vasicek conditional expectation to the worst-case default rate,
the capital requirement and the risk-weighted exposure amount.

**Approach:** the story comes from the A-IRB progression in the guides repo, which is
already ordered the way a model document is ordered, so the lecture inherits that arc
rather than inventing one. The notation comes from lecture 1, with a bridge table
reconciling it against the guides, because the two systems clash on three symbols and a
silent clash would make the lecture wrong. Bondora carries the demonstration as far as
it honestly can, i.e. grades, observed default rates by grade and a long-run average,
and the capital formula is then evaluated with the correlation the regulation prescribes
rather than one fitted here.

**Stack:** Quarto plus the pinned `.venv`. Render with
`bash scripts/render_lecture.sh credit_lectures/R2_credit-irb-capital.qmd`, never bare
`quarto render`.

**Companion:** plan 1, at `notes/plans/01-ifrs9-pit-pd-lecture.md`, builds lecture `R1`
on IFRS 9 point-in-time PDs. The two lectures share the regulatory track and the
notation bridge, so read plan 1's notation contract task before starting task 2 here.

---

## Global constraints

These bind every task, and they are the ones most easily lost in a fresh session.

- Never call a system `python3`. Use `.venv/bin/python` or activate the venv first.
- Never edit a rendered `credit_lectures/*.html` by hand. The `.qmd` is the source.
- Never add a dependency without flagging it first.
- British English throughout. No em or en dashes as punctuation. No negated counterpart
  clauses, which are banned outright. Prose carries the reasoning; bullets are for
  genuine enumerations.
- Name the standard, then name what it forces. A citation exists for the consequence it
  imposes rather than for authority alone.
- Small logical commits under Conventional Commits, scope `credit_lectures`.

## Decisions taken, 2 September 2026

1. **File name.** `credit_lectures/R2_credit-irb-capital.qmd`, sharing the regulatory
   track with plan 1's `R1`.
2. **The FiT form.** The probit form is canon; the multiplier is named as the
   practitioner shortcut with its bias stated. Shared with `R1`.
3. **Guides material.** Structure, regulatory references and transferable method only.
   No portfolio specifics travel, and Bondora carries every worked example.
4. **The IFRS 9 against IRB comparison table** lives in `R1`, cross-referenced here.
5. **Scope is PD only.** LGD and EAD get one paragraph each, naming what they are and
   pointing at the guides, because the capital formula needs them as inputs and the
   lecture would double in length if it modelled them.

## Two flags to settle before writing prose

Mario settled both on 2 September 2026. On the first, the lecture takes structure,
regulation and transferable method only, and Bondora carries every worked example. On the
second, every sentence gets rewritten in house voice.

1. **Confidentiality, settled.** The A-IRB files in the guides repo read like they derive
   from a real engagement. They name a US credit card portfolio, refer to onboarding
   partners without historical performance data, list the exact macroeconomic variables
   selected for that book, and describe COVID-19 exclusions and a chosen downturn
   period. None of that may enter this repo, which holds course material and is
   destined to stay private but is still not the right home for engagement detail. Take
   the **structure, the regulatory references and the method** from those files, and
   leave every portfolio specific behind. Where the lecture needs a worked example, it
   comes from Bondora.
2. **The guides files are drafts.** Several are raw assistant transcripts, with
   openers such as "Perfect, you're now in the..." and closing offers to write the next
   subsection, and they carry em dashes throughout. `05_modelling/pd/08-lra.md` has the
   LRA period section three times over in successive revisions. Read them for substance
   and rewrite every sentence in house voice. Copying a paragraph across would import a
   dash ban breach and a machine cadence at the same time.

## The story, taken from the guides

The arc below is the guides' own ordering, and it is what the comment means by
structure and story. Source files sit under
`~/Documents/Repos/guides/docs/wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/`,
abbreviated `CR/` from here.

1. **Why capital exists at all.** `CR/a-irb_capital/01_introduction/01-context.md` runs
   Pillar 1 from Basel I through the standardised and IRB approaches to Basel III.
2. **What the capital is for.**
   `CR/a-irb_capital/01_introduction/02-credit_losses.md` is the spine of the lecture's
   second half. It moves from expected loss, splitting the IFRS 9 ECL from the
   regulatory EL, to unexpected loss, conditional expected loss, the EL shortfall,
   value at risk, downturn LGD, the systemically conditional PiT PD, the Vasicek model,
   the worst-case default rate, systemic risk, asset correlations and time to default,
   and finishes on defaulted assets and the expected loss best estimate.
3. **Definitions and the process.** `01_introduction/03-definitions.md`,
   `04-process_overview.md` and `05-use_tests.md`. The process overview gives the
   purpose, scope, data, modelling, performance, assumptions, limitations, validation,
   materiality and compliance headings that a model document carries, and it states the
   point the lecture should not lose: without the LRA adjustment, the margin of
   conservatism and the downturn adjustment, the same models feed IFRS 9, so the two
   frameworks share a rank ordering and differ in calibration.
4. **Rating philosophy.** `05_modelling/pd/01-model_methodology.md` carries a
   three-way comparison of through-the-cycle, point-in-time and dynamic point-in-time
   with pros and cons already tabulated, plus the regulatory hooks: CRR Article
   180(2)(a) on consistency with long-run average default rates, PRA SS4/24 paragraph
   10.10 on all three philosophies being permissible, and PS9/24 paragraph 3.129 on
   dynamic recalibration with a buffer.
5. **The five-step development sequence.** `05_modelling/pd/02-model_design.md` states
   it plainly: point-in-time PD estimation, risk grade assignment, long-run average PD,
   margin of conservatism, regulatory PD. It splits into a risk differentiation phase
   and a risk quantification phase, which is the division the whole lecture should
   inherit.
6. **Risk differentiation.** `05_modelling/pd/03-risk-differentiation.md` and
   `06-pit-model.md` for segmentation, univariate and correlation analysis, variable
   transformation and segment-level logistic regression.
7. **Risk quantification.** `05_modelling/pd/07-risk-quantification.md` for grade
   construction, and `08-lra.md` for the LRA period, whose four-step determination is
   the most transferable piece of method in the whole folder: derive an economic factor
   from macroeconomic variables, classify good and bad periods, identify the cycle peak
   to peak, then test the observed default rate variability of the chosen window
   against the full cycle with an F-test.
8. **Testing.** `06_testing_results/pd/01-risk-differentiation.md` covers accuracy,
   discrimination, stability, robustness, stress analysis and benchmarking;
   `02-risk-quantification.md` covers concentration, homogeneity within grades,
   heterogeneity between grades, grade migration and calibration accuracy.

Also read `CR/02_probability_of_default.md`, which already holds the IFRS 9 against IRB
comparison table (PD type, rating philosophy, macro sensitivity, update frequency, data
period, horizon, granularity, flooring, data inputs) and the three transformations: 12
month PiT to TTC, TTC to the worst-case default rate, and systemic PiT to lifetime by
migration matrix. That table is the natural bridge between `R1` and `R2` and should
appear in `R1`, per Mario's decision of 2 September 2026, because the reader meets IFRS 9
there and the contrast lands while IRB is still the unknown half. `R2` points back to it.

## The notation clash, and it is real

`CR/03_notation.md` is a full notation table and it collides with lecture 1 in three
places. Resolving this is task 2, and getting it wrong is the most expensive mistake
available in this plan.

| Symbol | Lecture 1 and the S track | The guides | Verdict |
|---|---|---|---|
| $g$ | $g_i$, the origination date of loan $i$ | $g_{i,t} = \mathrm{DPD}_{i,t}/30$, the arrears measure in missed payments | Genuine clash. Both are load-bearing |
| $d$ | Botha's arrears threshold, lecture 1 section 2.1 | $d$ as the arrears threshold and $d_{i,t}$ as the instantaneous default indicator | Partial clash. $d$ agrees, $d_{i,t}$ is new |
| $s$ | one-period survival in the S track | the stickiness measure, and $s_{i,v}$ for one-period survival | Clash inside the guides themselves |
| $S$ | cumulative survival | cumulative survival $S_{i,t}$, and $S_{99.9}$ for the systemic factor quantile | Clash inside the guides themselves |
| calendar time | $u$ | $t'$ | Cosmetic, so state the mapping once |
| default outcome | $D^{(k)}_{i,t}$ | $D^*_{i,t}(k,p)$, with probation period $p$ | Reconcilable. The guides carry probation, lecture 1 does not |
| normal CDF | $\Phi(\cdot)$ | $N(\cdot)$ | Cosmetic |
| the systemic factor | $Z_u$, high values benign, entering as $-\sqrt{\rho} Z_u$ | $\mathrm{FLI}_{t'}$, entering as $+\sqrt{\rho}\,\mathrm{FLI}_{t'}$ | **Opposite sign convention.** Must be stated explicitly |

Two substantive findings fall out of that table and both belong in the lecture.

The guides' definitions of conditional and unconditional settle plan 1's question, and
they settle it the way plan 1 assumed. `PD^{uPiT}` is
$P(D^*_{i,t}(k,p) = 1 \mid X)$ regardless of prior default or prepayment, while
`PD^{PiT}` is $P(D^*_{i,t}(k,p) = 1 \mid D_{i,t}(p) = 0, X)$, conditioning on the loan
being in the performing risk set. The axis is survival, so plan 1's decision 2 is
corroborated by Mario's own notation rather than by preference. Cite `CR/03_notation.md`
for it in both lectures.

The guides define FiT twice and the two definitions are different objects. The notation
table has
$\mathrm{PD}^{\rm FiT} = \mathrm{PD}^{\rm PiT} \times \mathrm{FLI}_{t'}$,
a multiplicative scalar, while the systemically conditional PD has $\mathrm{FLI}_{t'}$
entering a probit as $N\!\left((N^{-1}(\mathrm{PD}^{\rm TTC}) + \sqrt{\rho}\,\mathrm{FLI}_{t'})/\sqrt{1-\rho}\right)$,
where it plays the part of a standard normal factor realisation. A multiplier on a
probability and a factor realisation inside a probit cannot both be the same $\mathrm{FLI}$.
Mario settled this on 2 September 2026: the probit form is canon, since it is the form
that reproduces the capital formula and the form lecture 1 already carries. The
multiplicative version is named as the practitioner shortcut it is, with its bias
stated, exactly as lecture 1 already does for the Jensen trap. Both lectures answer it
that way.

## Vault sources, all already on disk

At `~/Documents/Repos/vault/wiki/`. The regulatory citations must be verified against
these rather than taken from the guides, because a paragraph number copied from working
notes is the classic way a wrong citation enters a document.

- `regulation/irb-pd-estimation.md`, `regulation/irb-approach.md`,
  `regulation/irb-model-validation.md` and `regulation/irb-definition-of-default.md`.
- `regulation/eu-crr-2013-credit-risk.md` and `regulation/crr.md` for Article 180.
- `regulation/pra-ss4-24-irb-approach-2026.md` plus the two source registrations at
  `_meta/sources/pra-ss4-24-irb-approach.md` and `pra-ss4-24-irb-approach-jan2026.md`,
  for the paragraph numbers the guides cite as 10.10, 11.13 and 11.20.
- `regulation/eba-pd-lgd-estimation-guidelines.md` and `eba-pd-lgd-estimation-framework.md`.
- `methods/asrf-capital-foundation.md`, `methods/vasicek-loan-portfolio-value.md` and
  `methods/single-factor-credit-risk-model-vasicek-and-belkin.md` for the capital
  formula's derivation.
- `methods/asset-correlation-empirical-evidence.md` and
  `methods/vasicek-asset-correlation-estimation.md` for whether the prescribed
  correlations hold up.
- `methods/margin-of-conservatism-egim.md` and `methods/pd-moc-c-r-package.md` for MoC.
- `methods/pd-rating-scale-calibration.md`, `methods/pluto-tasche-pd-estimator.md` and
  `methods/multi-period-average-pd-backtesting.md` for grade calibration.
- `methods/irb-model-validation-and-rating-system-quality.md`,
  `methods/binomial-backtest-pd.md`, `methods/eba-pd-backtesting-methodology.md`,
  `methods/heterogeneity-testing.md` and the `methods/somers-d-*` family for testing.
- `methods/credit-risk-procyclicality.md` and `methods/rwa-pd-sensitivity.md` for the
  procyclicality argument the rating philosophy section needs.
- `methods/granularity-adjustment-gordy-lutkebohmert.md` for what the single-factor
  model assumes away, which is the honest caveat on the whole formula.

---

## Task 1: read the arc and write the structure note

**Files:** create `notes/irb-lecture-structure.md`.

- [ ] **Step 1.** Read every guides file listed in "The story, taken from the guides",
      in that order. Take notes on the arc rather than the content.
- [ ] **Step 2.** Write the note as a section-by-section outline for the lecture, one
      sentence of intent per section, and mark against each whether the material comes
      from the guides, from the vault, or has to be written fresh.
- [ ] **Step 3.** Record explicitly what the lecture omits and why, i.e. LGD and EAD
      modelling, defaulted-asset ELBE, economic capital beyond Pillar 1, and every
      portfolio specific from the flag above.
- [ ] **Step 4.** Commit.

```bash
git add notes/irb-lecture-structure.md
git commit -m "docs(notes): outline the IRB capital lecture from the A-IRB arc"
```

**Done when** the outline covers the five-step sequence and the capital formula, and
every section names its source.

## Task 2: the notation bridge

**Files:** append to `notes/irb-lecture-structure.md`.

- [ ] **Step 1.** Reproduce the clash table above from a direct read of
      `CR/03_notation.md` rather than trusting it, since the table was compiled by hand.
- [ ] **Step 2.** Decide each row and record the decision with a reason. The
      recommendation is that this lecture keeps lecture 1's symbols as canon, introduces
      the guides' symbol in parentheses on first use so a reader can move between the
      two, and never redefines a lecture 1 symbol.
- [ ] **Step 3.** Resolve the arrears measure explicitly. Lecture 1 owns $g_i$ for the
      origination date, so the arrears measure needs a different letter here. The
      proposal is $a_{i,t} = \mathrm{DPD}_{i,t}/30$, with the guides' $g_{i,t}$ named
      once beside it.
- [ ] **Step 4.** Resolve the sign convention on the systemic factor. State the mapping
      as one displayed equation so a reader can check lecture 1's hybrid formula against
      the guides' WCDR formula and see they agree.
- [ ] **Step 5.** Record the settled FiT reading, i.e. the probit form as canon and the
      multiplier as the named shortcut, and check that `R1` states it identically.
- [ ] **Step 6.** Commit.

**Done when** every row of the clash table carries a decision, and the sign mapping is
written as an equation rather than described.

## Task 3: verify every regulatory citation

**Files:** append to `notes/irb-lecture-structure.md`.

The guides cite CRR Article 180(2)(a) and 180(2)(e), PRA SS4/24 paragraphs 10.10, 11.13
and 11.20, PS9/24 paragraph 3.129, and CRR Articles 174, 179 and 180 for segmentation,
representativeness and calibration. Note that `08-lra.md` cites 180(2)(a) in one place
and 180(1)(a) in another for the same requirement, so at least one of the two is wrong.

- [ ] **Step 1.** For each citation, read the vault regulation article that covers it
      and confirm the article or paragraph number and what it requires. Where the vault
      does not settle it, mark the citation unverified rather than repeating it.
- [ ] **Step 2.** Resolve the 180(1)(a) against 180(2)(a) discrepancy and record which
      is right.
- [ ] **Step 3.** Record each verified citation with the consequence it imposes, in one
      sentence, ready to drop into the lecture. A citation that cannot state a
      consequence does not go in.
- [ ] **Step 4.** Commit.

**Done when** every citation is either verified with a consequence or explicitly marked
unverified.

## Task 4: the lecture skeleton

**Files:** create `credit_lectures/R2_credit-irb-capital.qmd`.

- [ ] **Step 1.** Copy the YAML header and provenance comment pattern from
      `credit_lectures/S2_survival-insurance-to-credit.qmd` and adjust it.
- [ ] **Step 2.** Write the abstract, three or four sentences, saying that the lecture
      picks up lecture 1's hybrid callout and follows it to a capital number.
- [ ] **Step 3.** Lay out the headings from task 1's outline with one sentence of intent
      each and no content.
- [ ] **Step 4.** Render and confirm the skeleton comes out with `lecture.css` applied.
- [ ] **Step 5.** Commit.

## Task 5: from expected loss to unexpected loss

**Files:** modify `credit_lectures/R2_credit-irb-capital.qmd`.

- [ ] **Step 1.** Write the expected loss identity and split the IFRS 9 ECL from the
      regulatory EL, using the two definitions in `01_introduction/02-credit_losses.md`
      and citing the vault for each.
- [ ] **Step 2.** Define unexpected loss as the distance from the mean to the chosen
      quantile of the loss distribution, and state which one capital covers and which
      one provisions cover. This is the sentence the whole lecture rests on.
- [ ] **Step 3.** Add the EL shortfall, i.e. what happens when regulatory EL exceeds
      accounting provisions, since it is where the two frameworks meet on a balance
      sheet.
- [ ] **Step 4.** Render, commit.

## Task 6: rating philosophy and what the regulation forces

**Files:** modify `credit_lectures/R2_credit-irb-capital.qmd`.

- [ ] **Step 1.** Write the three philosophies as prose, i.e. through the cycle, point
      in time, and dynamic point in time, defining each by what happens to grade
      migration and to the observed default rate per grade across the cycle. That
      contrast is the one a reader remembers.
- [ ] **Step 2.** Add the comparison table with pros and cons per philosophy, rewritten
      from `05_modelling/pd/01-model_methodology.md` in house voice, styled per
      `~/.claude/rules/html-design.md` with a `<caption>` naming the basis.
- [ ] **Step 3.** State what CRR Article 180(2)(a) forces on each, using the verified
      wording from task 3, and why a pure TTC grade assignment struggles against it.
- [ ] **Step 4.** Add the procyclicality argument from
      `methods/credit-risk-procyclicality.md` and `methods/rwa-pd-sensitivity.md`,
      which is the reason a supervisor prefers a stable grade PD.
- [ ] **Step 5.** Cross-reference `R1`, since IFRS 9 wants the opposite philosophy from
      the same data, and reuse the IFRS 9 against IRB comparison table from
      `CR/02_probability_of_default.md`, which lives in `R1` per decision 4.
- [ ] **Step 6.** Render, commit.

## Task 7: the five-step sequence, demonstrated on Bondora

**Files:** modify `credit_lectures/R2_credit-irb-capital.qmd`.

Bondora is a P2P book rather than a bank's, so the demonstration is an illustration of
the mechanics and says so plainly.

- [ ] **Step 1.** Fit a point-in-time twelve-month PD on `data/bondora_pd.parquet`,
      reusing lecture 1's GLM3 specification so the two lectures agree, and back-score.
- [ ] **Step 2.** Bin the scores into risk grades. Show the grade construction tests the
      guides list, i.e. concentration, homogeneity within grades and heterogeneity
      between grades, using `methods/heterogeneity-testing.md` for the test choice.
- [ ] **Step 3.** Compute observed twelve-month default rates by grade and by cohort
      year, then the long-run average per grade over the available window.
- [ ] **Step 4.** Work the LRA period four-step method on the Bondora window, i.e. build
      an economic factor from the Eurostat series that plan 1 curates at
      `credit_lectures/data/macro_eurostat.csv`, classify good and bad years, mark the
      cycle, then run the F-test comparing observed default rate variability in the
      chosen window against the full window. State honestly that a 2009 to 2021 window
      containing the pandemic is not a clean cycle.
- [ ] **Step 5.** Add a margin of conservatism, following the category structure in
      `methods/margin-of-conservatism-egim.md`, and show the regulatory PD as the
      calibrated PD plus the MoC. Name which category each Bondora uplift falls in.
- [ ] **Step 6.** Tabulate the five steps for one grade end to end, so a reader can
      follow one number from scorecard output to regulatory PD.
- [ ] **Step 7.** Render clean, commit.

**Done when** one grade's number is traceable through all five steps in a single table.

## Task 8: the capital formula

**Files:** modify `credit_lectures/R2_credit-irb-capital.qmd`.

This is the section lecture 1's hybrid callout was pointing at.

- [ ] **Step 1.** Set up the single-factor model, i.e. a latent asset return, a
      systematic factor and an idiosyncratic term, and derive the conditional default
      probability. Cite `methods/vasicek-loan-portfolio-value.md` and
      `methods/asrf-capital-foundation.md`.
- [ ] **Step 2.** Show that lecture 1's hybrid expression and the guides' systemically
      conditional PD are the same formula under the sign mapping from task 2, and that
      the worst-case default rate is that expression at the 99.9th percentile of the
      factor.
- [ ] **Step 3.** Write the capital requirement per unit of exposure, i.e. the
      conditional expected loss less the expected loss, with the maturity adjustment
      named, then the risk-weighted exposure amount. State that the correlation is
      prescribed by exposure class rather than fitted, and give the retail values.
- [ ] **Step 4.** Plot the risk weight against PD for the prescribed retail
      correlations, which makes the concavity and the effect of the 0.03 per cent floor
      visible in one figure.
- [ ] **Step 5.** Run the formula on the Bondora grades from task 7 and report the
      capital requirement, flagging that a P2P book has no IRB permission and the number
      is illustrative.
- [ ] **Step 6.** State what the single-factor model assumes away, i.e. one factor,
      infinite granularity and no concentration, and cite
      `methods/granularity-adjustment-gordy-lutkebohmert.md` for the correction.
- [ ] **Step 7.** Render, commit.

## Task 9: what a validator asks

**Files:** modify `credit_lectures/R2_credit-irb-capital.qmd`.

- [ ] **Step 1.** Write the differentiation tests, i.e. accuracy, discrimination,
      stability, robustness, stress analysis and benchmarking, one sentence each on what
      the test is and what failing it means.
- [ ] **Step 2.** Write the quantification tests, i.e. concentration, homogeneity within
      grades, heterogeneity between grades, grade migration and calibration accuracy,
      the same way, citing `methods/binomial-backtest-pd.md` and
      `methods/eba-pd-backtesting-methodology.md` for the calibration test.
- [ ] **Step 3.** Add one paragraph on the use test, from `01_introduction/05-use_tests.md`,
      because a model used only for capital fails it.
- [ ] **Step 4.** Render, commit.

## Task 10: trim lecture 1 to a brief mention

**Files:** modify `credit_lectures/01_credit-use-case.qmd`, the hybrid callout at
lines 778 to 830.

The comment says this can be briefly mentioned in lecture 1, so lecture 1 keeps a
mention and loses the derivation.

- [ ] **Step 1.** Keep the logit-scale interpolation with $\lambda$, since it is the
      shortest honest statement of what a hybrid PD is, and keep one sentence naming the
      one-factor version.
- [ ] **Step 2.** Move the averaging identity, its algebra, the worked shortfall figure
      and the IRB capital paragraph into `R2`, leaving a forward reference.
- [ ] **Step 3.** Re-render lecture 1 and diff the computed outputs. A re-render is known
      safe: on 1 September 2026 all 58 computed output lines reproduced identically,
      the only diff being two statsmodels summary timestamps.
- [ ] **Step 4.** Commit lecture 1 separately from `R2`.

**Done when** the callout is under half its current length and still defines every symbol
lecture 1 goes on to use.

## Task 11: record the lecture

**Files:** modify `CLAUDE.md`; modify `notes/lecture-1-review-comments-2026-09-01.md`.

- [ ] **Step 1.** Add `R2` to the `credit_lectures/` row of the key directories table,
      naming the regulatory track and what each lecture reads.
- [ ] **Step 2.** Mark round 3 comment 2 as answered, one paragraph on how.
- [ ] **Step 3.** Commit.
