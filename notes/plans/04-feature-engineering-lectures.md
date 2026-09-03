# A feature engineering track for the credit lectures: F1 and F2

## Context

Credit lecture 3 names the classical scorecard's feature engineering in a single paragraph
(`credit_lectures/03_credit-deep-learning-overview.qmd:76-95`) and then moves past it:

> The classical scorecard takes each candidate variable, bins it into coarse classes,
> replaces each class by its weight of evidence, and admits the variable only if the binning
> is monotone, populated at every level and stable across time. The procedure is transparent,
> auditable and slow, and every step of it is a decision recorded in a model development
> document.

That paragraph is the whole of the series' account of an activity that occupies most of a real
PD model's development effort. Mario asked for it to become its own lecture, drawing on the
`guides` repo as an indicator and on the vault for citable sources. Reading the two together
turned up the finding that gives the material an argument rather than a technique tour: the
two source bodies describe **rival traditions that disagree about whether to discretise at
all**. The vault articles describe the classic scorecard, where every characteristic is binned
and weight-of-evidence encoded. The guides' A-IRB pipeline never bins: it keeps covariates
continuous, straightens them with Tukey's ladder and the bulging rule, and screens on a
condition index. Both are live practice. Neither is what a network does, which lands the
material exactly on lecture 3's claim about representation learning.

The outcome is a new **feature engineering track**, `F1` and `F2`, numbered outside the course
sequence for the reason the S, R and C tracks are: no course lecture answers them.

## What lecture 6 already owns, and why F1 is still a distinct lecture

This was the decisive check. `credit_lectures/06_credit-covariate-engineering.qmd` is titled
*Ensembling and Entity Embedding* and its second half already covers more than its title
suggests. **Do not redefine any of the following.** Cite lecture 6 backwards instead.

| Already owned by lecture 6 | Where |
|---|---|
| The WoE formula, and why the log-odds scale matches the logit link | `06:536-575` |
| Bühlmann-credibilitised target encoding, and minimum bin size as its blunter cousin | `06:578-600` |
| Ordinal, one-hot and dummy coding; five encodings compared; leakage | `06:506-535`, `06:692-809` |
| Entity embedding, and whether proximity tracks risk | `06:810-1128` |
| Standardisation, the MinMaxScaler, censoring and log-transforming a tail first | `06:1131-1159` |
| Binning as a mapping, why scorecards bin, and what binning costs | `06:1160-1185` |

Lecture 6 asks how to encode a level once you have one. It says the bin boundaries "are chosen
by the modeller" and stops there. The F track asks the questions it leaves open: how the
boundaries are actually chosen, which characteristics earn a place, how the choice is defended,
and what the rival tradition does instead.

## The split

Both lectures read `data/bondora_pd.parquet` for interpretable work and
`data/credit_card_dev.parquet` (1,214 features, 1.42 per cent bad rate) where a wide book is
needed. That switch has precedent and a stated justification in lecture 3.

### F1: `credit_lectures/F1_credit-classing-and-characteristic-analysis.qmd`

Roughly 6,000 words. Bondora throughout. The discretise tradition, run end to end.

1. **What lecture 2 did without naming it.** Opens on the verified continuity hook at
   `02_credit-edf-glm.qmd:815-829`: the `71+` class held 13 loans and zero defaults, drove its
   coefficient towards minus infinity through quasi-complete separation, and the two oldest
   bands were merged into `61+`; `HomeOwnershipType` and `EmploymentDurationCurrentEmployer`
   were given explicit `missing` levels. Lecture 2 called the remedy "coarser classes". This
   section names it coarse classing and says the discipline has forty years of procedure
   behind it.
2. **Two traditions, one aim.** States the frame for both F lectures. Both hand-craft the
   transformation φ that lecture 3 defines; they disagree about its functional class (step
   function against smooth monotone map). F1 runs the discretise branch and closes by showing
   the other on one covariate, per section 11 below; F2 runs the second branch in full.
3. **Fine classing.** Twenty-quantile fine classes on Bondora numerics, the observed default
   rate per fine class, and the raw jaggedness that motivates the next step.
4. **Coarse classing algorithms.** The Monotone Adjacent Pooling Algorithm and isotonic
   regression, both hand-rolled in numpy (see dependencies below), plus the U-shaped case split
   at a turning point before monotone binning is applied to each arm. Run all three on
   `Age`, `DebtToIncome`, `IncomeTotal` and `LoanDuration`, and show that the algorithm choice
   changes the class count materially, which is the validation point in
   `vault/wiki/methods/risk-factor-binning.md`.
5. **Information value, and what it does not tell you.** The IV formula, the common bands, and
   two honest qualifications: IV is bin-count dependent, so a comparison across characteristics
   requires comparable class counts, and a suspiciously high IV is a leakage signal. Bondora's
   `Interest` column is the worked example, since `notes/credit-datasets.md` already records
   that it rank-orders default powerfully and is endogenous.
6. **Monotonicity as discipline, not regulation.** Stated as practitioner practice with its
   rationale (out-of-time stability), explicitly **not** as a regulatory requirement. See the
   verification register below.
7. **Small cells, and where the 13 loans came from.** Bondora's 28.95 per cent default rate
   makes any minimum-defaults-per-bin rule trivial on the whole book, so the instability
   argument is made on the age tail and on a deliberately thin slice, not on the portfolio.
   Ties back to lecture 6's credibility alternative in one sentence.
8. **Missing and special values as attributes.** The three-way MAR, MNAR, structurally-missing
   classification, and the case for an own-attribute treatment over imputation, which is what
   lecture 2 chose by instinct.
9. **The characteristic-analysis table, and a fitted scorecard.** Assemble the classed
   characteristics into the standard characteristic-analysis layout, fit the WoE logistic
   regression, and report deviance and AUC on both series splits (80/20 random and the
   80th-percentile-date out-of-time).

   **Refit the benchmark inside F1 rather than quoting it.** Lecture 2's `FORMULA`
   (`02:846-848`) is reused verbatim by lecture 4-5 (`04-05:411-415`), whose out-of-time
   numbers are a GLM AUC of 0.716 against the network's 0.715. Quoting either figure across
   lectures would compare the classing and the covariate list at once. So F1 recomputes that
   same eight-covariate GLM in its own chunk, on F1's own splits, and the only difference
   between the two AUCs is then the classing, which is what the section is about.
10. **One result the procedure does not advertise.** WoE encoding is not self-replicating
    (`vault/wiki/methods/encoding-instability.md`): retrain a WoE model on its own predictions
    and it does not reproduce itself, whereas a dummy-encoded model does. Demonstrate it on
    Bondora. Also state the intercept-drift result: across 7,007 model combinations the
    intercept-implied default rate spanned 29.64 to 30.39 per cent against an observed 30
    (`vault/wiki/methods/weight-of-evidence-encoding.md:40`).
11. **The same covariate, undiscretised.** Around 400 words and one exhibit, so that F1 pays
    off the frame it sets in section 2 instead of forward-referencing it. Take
    `DebtToIncome`, run it both ways (coarse-classed WoE against a log transform chosen off
    the bulging rule), and read both on one fixed readout. F2 then generalises the comparison
    across the wide book rather than introducing it.
12. **What a validator asks to see.** Callout. Stops at the fitted feature set and cites `R3`
    forward for stability and representativeness.
13. Takeaways, copyright and attribution, references.

### F2: `credit_lectures/F2_credit-selection-collinearity-and-points.qmd`

Outlined here, written next. Roughly 6,000 words, and the wide credit card table carries
sections 3 and 4.

1. Stepwise selection and its failure, via Scallan's white-noise simulation: 100 candidate
   variables all noise, 100 bads, median model picking up ten or more of them and reporting a
   meaninglessly inflated Gini.
2. Partition (nested dummy) variables and the wrong-hypothesis problem, then marginal
   information value with the MIV > 0.02 threshold, the marginal chi-square, and the triple
   test of importance, reliability and business sense.
3. Correlation clustering on `credit_card_dev.parquet`, where 1,214 features give the method
   something to bite on, followed by the condition index with variance-proportion one-drop at
   a threshold of 30, which is the guides' actual verified method.
4. The rival tradition, run on the same wide table: special-value treatment, outlier capping,
   then Tukey's ladder and the bulging rule to straighten a covariate in log-odds space
   without discretising it. Compare against F1's classed fit on a fixed readout.
5. From coefficients to points: Factor = PDO / ln 2, the Offset, per-attribute points, and the
   result that score-share importance shifts under three different Factor and Offset
   configurations for the same underlying model, so it measures the scaling and not the
   discrimination. That result is cited from
   `vault/wiki/methods/weight-of-evidence-encoding.md:56`, which carries the simulation;
   `methods/scorecard-scaling.md` carries the Factor and Offset arithmetic and the intercept
   distribution conventions. Hoadley's quadratic-programming formulation closes the section as
   the historical endpoint.
6. What a network does with the same problem, closing the loop to lecture 3 §2.1 and lecture 6.

## Sequencing, and what this plan delivers

The house convention is a structure note first, then the lecture (see `notes/irb-lecture-structure.md`
and `notes/sampling-lecture-structure.md`). Accordingly:

1. Write `notes/feature-engineering-lecture-structure.md`, covering **both** F1 and F2: the
   confidentiality boundary, the lecture 6 overlap table above, the verification register
   below, the notation bridge, and the R3 boundary.
2. Write, render, print and publish **F1** in full.
3. **F2 is outlined in the note and written in a following session.** Say so at handover rather
   than half-writing it. Override this at approval if both are wanted in one go.

## Two boundaries that must be written into the structure note

**Confidentiality.** The A-IRB material in `guides` derives from a real engagement, so this
inherits the bar `notes/irb-lecture-structure.md` sets: structure, regulatory references and
transferable method travel, and no portfolio specific does. Recorded by category rather than by content, per
`notes/irb-lecture-structure.md`. Left behind entirely and deliberately not itemised further:
the source portfolio's segmentation scheme with its volumes and observed default rates, its
acquisition history, its risk-grade construction scheme, its variable-clustering configuration,
its data-quality screening thresholds, and its bureau vendor's special-value code list. Bondora and the credit card table carry every worked example.

**R3.** The population stability index, the characteristic stability index and characteristic
stability belong to `R3_credit-sampling-and-representativeness`, whose structure note
(`notes/sampling-lecture-structure.md`) is untracked and in flight in another session. F1 stops
at the fitted feature set and cites R3 forward. Read R3's source table before claiming any
shared citation, and expect `index.html` and `CLAUDE.md` counts to move under you.

## Verification register: what may be spent, and what may not

Verified by direct read this session, and safe to use:

| Claim | Source read |
|---|---|
| `71+` held 13 loans and zero defaults; quasi-complete separation; merged to `61+` | `credit_lectures/02_credit-edf-glm.qmd:815-829` |
| Lecture 2's two explicit `missing` levels, 1,604 and 820 loans | same, `:815-819` |
| WoE = ln(DistGood/DistBad); intercept spread 29.64 to 30.39 per cent over 7,007 combinations | `vault/wiki/methods/weight-of-evidence-encoding.md:36,40` |
| MAPA and isotonic regression as the two monotonicity algorithms; U-shape split via B-splines; algorithm choice changes the grade count | `vault/wiki/methods/risk-factor-binning.md:29-39` |
| Partition variables, the wrong-hypothesis problem, Harrell's stepwise critique, the white-noise simulation, MIV > 0.02, the triple test | `vault/wiki/methods/scallan-2011-classic-scorecard-development.md:33-47` |
| WoE encoding is not self-replicating; dummy encoding is | `vault/wiki/methods/encoding-instability.md:28-30` |
| Factor = PDO / ln 2, the Offset, intercept distribution, score-share importance shifting under three scalings, Hoadley's QP | `vault/wiki/methods/scorecard-scaling.md:31-51` |
| The condition index with variance-proportion one-drop, and iterated correlation clustering at progressively looser thresholds, as the method | guides `a-irb_capital/04_feature_engineering/pd/04-variable-reduction.md:141-170,53-94` |
| Special values by the 1 per cent rule; MAR/MNAR/structural classification; 1st and 99th percentile capping; Tukey's ladder and the bulging rule | guides `.../pd/05-variable-transformation.md:22-195` |

**Not verified, and not to be asserted.** Four claims a subagent surfaced from
`guides/docs/raw/compass_artifact_wf-415a19b4-*.md`, which is a generated research dump rather
than a source, and from guides wiki files that are ChatGPT transcripts:

1. **"Monotonicity is required by EBA Article 174 and US fair-lending review."** Treat as
   false. This repo's own verification records Art. 174(c) as the *representativeness* anchor
   (`notes/sampling-lecture-structure.md:50-54`). No regulation mandates a monotone WoE
   profile. Cite monotonicity as practitioner discipline with the out-of-time stability
   rationale from `risk-factor-binning.md`.
2. **Siddiqi's IV bands** (0.02 / 0.10 / 0.30 / 0.50). The vault has no Siddiqi article. State
   the bands as unattributed common practice and note the bin-count dependence, or drop them.
3. **"VIF < 5, tightened to 4 in some IRB submissions."** Unsourced. Use the condition index
   method instead, which was read directly and is the more interesting diagnostic. Cite the
   method and not the source build's threshold values.
4. **Navas-Palencia (2020) optimal binning as a mixed-integer program**, and the
   **Haldane-Anscombe +0.5** zero-cell correction. Both are real; neither was verified here.
   Either verify before citing, or present the +0.5 adjustment as arithmetic without the name.

## Dependencies: none

Nothing new is installed, so `requirements.txt` stays byte-for-byte the course file. Do not add
`optbinning`, `monobinpy` or `scorecardpy`.

Two of the algorithms are treated differently, and the note should say why. **Hand-roll MAPA**,
WoE, IV, MIV and the condition index in `numpy`, `polars` and `statsmodels`: MAPA is a
six-line adjacent-merge loop whose merge order is the whole teaching point, and a library call
would hide it. **Use the pinned library for isotonic regression**, since
`sklearn.isotonic.IsotonicRegression` is present in the pinned `scikit-learn` 1.8.0 (verified by
import this session) and reimplementing pool-adjacent-violators buys nothing pedagogically that
MAPA has not already bought.

## Files

**Create**

- `notes/plans/04-feature-engineering-lectures.md`, the durable copy of this plan. The R and C
  lecture plans are already kept there as `01-`, `02-` and `03-`, so the numbered series
  continues rather than the plan living only under `~/.claude/plans/`.
- `notes/feature-engineering-lecture-structure.md`
- `credit_lectures/F1_credit-classing-and-characteristic-analysis.qmd`
- rendered `.html`, its `_files/` figure directory, and the `.pdf`

**Modify**

- `index.html`: a fifth track section, "The feature engineering track", with its track note and
  one entry in the established shape (`.entry-num` `F1`, `.entry-title`, `.entry-note`,
  `.entry-links` with Read and PDF). Copy the entry markup from the lecture 3 entry.
- `CLAUDE.md`: the `credit_lectures/` row gains the F track description, and the "thirteen
  credit lectures" count in both `CLAUDE.md` and `index.html` moves. Reconcile against R3 if it
  has landed.

**Do not touch.** Anything under `lectures/`, `exercises/` or `reference/`, and no rendered
`credit_lectures/*.html` by hand: edit the `.qmd` and re-render.

## Verification

Done means all six of these, in order:

1. `bash scripts/render_lecture.sh credit_lectures/F1_credit-classing-and-characteristic-analysis.qmd`
   completes and every code chunk executes. Never bare `quarto render`.
2. Read the rendered HTML and confirm each computed figure quoted in prose matches the output
   the render produced. Numbers written before the render are assumptions until checked.
3. `bash scripts/html_to_pdf.sh credit_lectures/F1_credit-classing-and-characteristic-analysis.html`,
   then open a page carrying mathematics and confirm it typeset. Chrome exits zero on raw TeX,
   so this check is by eye. A lecture is not finished without its PDF.
4. Open `index.html` and confirm the new track renders in the same shape as the other four.
5. `/writing-guidelines-grader credit_lectures/F1_credit-classing-and-characteristic-analysis.qmd`,
   then fix and re-run, because an editing pass introduces its own breaches.
6. Commit under Conventional Commits, one concern per commit: the structure note, then the
   lecture, then the index and `CLAUDE.md` updates.
