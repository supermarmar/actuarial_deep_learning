# Credit lecture 12: overlap map, notation bridge, measured facts and citation register

Working note for `credit_lectures/12_credit-foundation-models.qmd`, the companion to
`lectures/12_foundation-models.html`. It records what the earlier lectures already own and
must not be redefined, which numbers were measured before any prose was written, and which
citations survived verification.

Read this before editing the lecture. Everything settled here is settled.

Planned 4 September 2026 and measured the same day. The measured-facts section began life as
a contract naming what had to be measured; every entry has now been measured and the section
is a register. Two entries were killed by their own measurement and both are recorded below
under "what the measurements changed", because a claim the data refused is worth keeping as a
warning.

## Why the lecture exists, and what it discharges

Course lecture 12 covers foundation models as a model class, the GPT series, tabular
foundation models (TabTransformer, FT-Transformer, TransTab, TabPFN, TabPFN v2, TabICL) and
the in-context learning credibility transformer (ICL-CT) of Padayachy, Richman, Scognamiglio
and Wüthrich (2025). It closes the course.

Two debts in the credit series point here.

- `10-11` closes on the Credibility Transformer having competed without leading, with the
  credibility mechanism working mechanically and buying nothing. Its takeaways name this
  lecture explicitly: "Lecture 12 takes up foundation models and in-context learning, where
  the tokenisation of section 3 becomes the interface to a pretrained model rather than a
  component of a fitted one." The obvious next question is whether a mechanism that retrieves
  **other borrowers' outcomes** at prediction time does better than one that shrinks towards
  a learned prior. That question is this lecture's.
- `03` promises the deep-learning overview's forward pointers are all discharged. Foundation
  models are the last of them.

## The spine, decided 4 September 2026

Credit's version of the course's limited-data problem is a **cold start** rather than a small
portfolio: a new country, a new product, a segment with no default history of its own.
Insurance lecture 12 motivates credibility with small portfolios, new products, rare events
and new vehicle models. Credit's counterpart is sharper, because a lender genuinely opens and
closes country books, and Bondora's Slovak book is one of them.

The lecture therefore asks one question in every act: **does a prior the model did not learn
from this book, or context it retrieves at prediction time, buy what lecture 10-11's
credibility gate did not?** The yardstick is stated in the abstract and again at the first
deviance table: lecture 10-11 measured a seed standard deviation of 0.126 on this book.

**A null result was accepted as a finding before any fit was run.** Mario settled this on
4 September 2026, precisely so the lecture could not be quietly reframed around whatever the
numbers turned out to be. It was the right call, because the tabular result is null.

### Why Slovakia carries the cold-start act

After the series' filters (`Age` not null, `IncomeTotal > 0`, `Education != -1`) the modelling
frame holds 148,667 loans in four countries:

| Country | n | Twelve-month default rate | First origination | Last origination |
|:---|---:|---:|:---|:---|
| EE | 86,224 | 0.1703 | 2009-02-28 | 2020-07-19 |
| FI | 35,879 | 0.3784 | 2013-07-23 | 2020-03-24 |
| ES | 26,268 | 0.5543 | 2013-10-18 | 2020-03-24 |
| SK | 296 | 0.7061 | 2014-03-13 | 2015-01-05 |

All 296 Slovak loans survive the filters. Slovakia is a genuine closed cohort: originations
run for ten months and then stop, which is what a lender's withdrawal from a market looks
like. Its default rate of 70.6 per cent against Estonia's 17.0 makes it a hard cold start
rather than a cosmetic one, and CLAUDE.md already records it as excluded from the Eurostat
fetch on the ground that its survival risk set has a median of seventeen loans a month.

Two rejected alternatives, recorded so they are not revisited. `County` and `City` are
**entirely null** in `bondora_pd.parquet`, so the course's region remap has no direct
analogue. `OccupationArea` has 22 levels and would give a larger held-out set, and it was
rejected because a pooled set of small occupation codes is a synthetic segment where a
withdrawn country book is a real one.

## The five acts

1. **Foundation models as a model class.** Exposition. The one credit-specific subsection maps
   the adaptation ladder onto lending practice, and its load-bearing observation is that a
   **bureau score is already a pretrained prior** somebody else fitted on a population the
   lender cannot inspect. That precedent is what section 5.4 leans on.
2. **Tabular foundation models, empirical on TabPFN v2.** A nested learning curve at six
   sample sizes and three draws, against lecture 2's GLM and the base Credibility
   Transformer, plus a calibration check against lecture 7's balance property.
3. **The ICL-CT in torch**, built in five components on lecture 10-11's model, with the
   proposition's arithmetic checked and five paired seeds.
4. **The Slovak cold start**, with bootstrap intervals and the retrieved context's country
   composition.
5. **Governance**, measured rather than asserted.

## Boundaries

**`10-11` owns the Credibility Transformer.** Its architecture, the feature tokeniser, the CLS
token, the explicit Bernoulli gate and the implicit credibility weight are all built there.
This lecture imports the class in a folded cell and cites backwards. It does **not** re-derive
attention, layer normalisation or the time-distributed layer.

**`06` owns entity embeddings, one-hot encoding, weight of evidence and Bühlmann credibility.**

**`09` owns reason codes and variable importance.** Lecture 9 built the per-decision
decomposition, calibrated it against noise, and established that one reason code is defensible
on this book while three are not. Section 5.2 measures the **stability of an ICL prediction
under a re-draw of its retrieval pool**, which is a different quantity, and it uses lecture 9's
1.043 and 0.118 log-odds gaps as its yardstick rather than inventing a second measure.

**`07` owns the balance property and auto-calibration.** Section 2.8 applies that machinery
and does not restate it.

**`R3` owns representativeness and sample design.** Its verification record already
established that representativeness anchors on **CRR Article 174(c)** rather than 179, and
that Article 180(2)(e) carries no economic-cycle requirement. Section 5.4 cites `R3` and does
not re-import the 179 anchoring `R3` rejected.

**`D1` owns the target and the exposure convention.** `default_12m` is Bondora's own flag
within 365 days and every loan in the fixed-horizon table carries the same twelve-month
window by construction. Section 3.2's decorator problem turns on that, so it cites `D1`.

**`R2` owns IRB capital.** Section 5.4 names the documentation problem; it does not re-run the
five-step production sequence.

**`S` track owns the survival estimand.** Section 3.2 names observed duration as the honest
exposure analogue and declines to use it, because it changes the estimand.

## The exposure problem, and how the decorator resolves it

The insurance decorator injects the observed response into a context instance's CLS token in a
credibility-weighted way:

$$\boldsymbol{c}^{\rm decor}(\boldsymbol{x}_j) = \widehat{\boldsymbol{c}}^{\,\rm cred}(\boldsymbol{x}_j) + \frac{v_j}{v_j + \kappa}\, \boldsymbol{z}^{\rm FNN1}(Y_j),$$

where $v_j$ is exposure in policy-years. The weight $v/(v+\kappa)$ is what makes this a
credibility construction.

**Bondora's fixed-horizon table has no exposure.** Setting $v \equiv 1$ collapses the weight
to the constant $1/(1+\kappa)$, so $\kappa$ stops being a credibility coefficient and becomes
a plain shrinkage hyper-parameter applied identically to every context instance.

**Resolution, as built.** $v \equiv 1$, with the demotion stated in the lecture at first use.
Two alternatives are named and not run: observed duration from `bondora_survival.parquet`,
which belongs to the `S` track's estimand, and `Amount` as an EAD-style weight, which would
make the decorator loss-weighted rather than credibility-weighted. Do **not** manufacture an
exposure column to make the formula look transferable.

## Notation bridge

| Symbol | Course | Here |
|---|---|---|
| $\mathcal{C}$ | prompt demonstration set | the retrieved context batch |
| $\mathcal{D}$, $S$ | ICL context / support set | "support set" in prose; a bare $S$ is never used, since `S` prefixes this repo's survival track |
| $v_j$ | exposure in policy-years | absent by construction; $v \equiv 1$, see above |
| $\kappa$ | credibility coefficient in the decorator | a shrinkage hyper-parameter, and the lecture says so at first use |
| $\mu(\boldsymbol{x})$ | expected claim count per unit exposure | probability of default within twelve months |
| $a_{i,j}$, $a_{i,i}$ | causal attention weights, own-weight | unchanged |
| $\alpha$ | Bernoulli gate probability in the base CT | unchanged from `10-11`; lecture 6's credibility weight stays $\alpha_k$ |
| $q$, $b$ | covariate count, channels | unchanged, per `10-11`'s resolution |
| $K$ | retrieved neighbours per target | neighbours only; the softmax class count is written $K^{\rm cls}$ and equals 2 throughout |
| $c$, $m$ | context batch size, target batch size | unchanged: $c = 1000$, $m = 200$, $K = 64$ |
| $n$ | sample size | unchanged; section 2.6's learning curve indexes on it |

## Measured facts

Every figure below was measured before the prose around it was written. Deviances are on the
series' scale, $100 \times 2 \times$ the mean Bernoulli contribution.

### The two test samples, and why there are two

TabPFN's cost grows quadratically in its context, so scoring all 29,734 test rows at every
point on the learning curve would have dominated the render. Sections 2.6 to 2.8 therefore
score on a **fixed random 3,000-row subsample** of the test set, and sections 3 onward return
to the full test set.

| Sample | n | Observed default rate | Null deviance |
|:---|---:|---:|---:|
| learning | 118,933 | 0.28878 | |
| test, full | 29,734 | | 120.808 |
| test, 3,000-row subsample | 3,000 | 0.29933 | 122.114 |

The subsample's observed rate carries a sampling standard error of 0.00836, which is why
section 2.8's calibration table reports gaps in standard errors rather than in percentage
points alone.

### Act two: the learning curve

Mean over three draws, scored on the 3,000-row subsample.

| n | GLM | CT | TabPFN v2 | GLM AUC | CT AUC | TabPFN AUC |
|---:|---:|---:|---:|---:|---:|---:|
| 250 | 1901.015 | 119.638 | 113.312 | 0.5685 | 0.5949 | 0.6857 |
| 500 | 2017.065 | 117.694 | 112.100 | 0.5720 | 0.6547 | 0.6957 |
| 1,000 | 1370.436 | 116.481 | 111.973 | 0.5860 | 0.6727 | 0.6997 |
| 2,000 | 1299.679 | 112.951 | 111.575 | 0.6143 | 0.6877 | 0.7031 |
| 5,000 | 111.568 | 112.170 | 111.367 | 0.7000 | 0.6937 | 0.7071 |
| 10,000 | 111.150 | 111.093 | 110.988 | 0.7020 | 0.7032 | 0.7069 |

Four facts worth keeping.

- **TabPFN leads at every size up to 10,000** and by 10,000 the three arms span 0.16 in total,
  which is inside the 0.126 seed spread and therefore not a difference.
- **The GLM separates below 5,000 rows.** Maximum likelihood on roughly thirty parameters and
  a few hundred observations drives coefficients to infinity whenever a covariate pattern is
  perfectly classified. The behaviour is erratic as well as bad, since whether a pattern
  separates depends on the draw: 1,901 at 250 rows, 2,017 at 500, 1,370 at 1,000.
- **TabPFN handed 10,000 rows reaches 110.877 and the GLM fitted on all 118,933 reaches
  110.873.** Those two figures agreeing to 0.004 is the act's headline. The Credibility
  Transformer on all 118,933 takes 110.363 on the same subsample and 107.342 on the full test
  set, so twelve times TabPFN's context is worth about half a point.
- **Cost.** TabPFN is roughly quadratic in context: 7.4 seconds at 1,000 rows, 23.9 at 5,000,
  75 to 87 at 10,000, and 236.4 at 20,000. The curve stops at 10,000 for that reason and
  because the v2 pretraining regime does not extend much beyond it.

### Act two: calibration

Mean predicted PD on the 3,000-row subsample, whose observed rate is 0.29933 with a standard
error of 0.00836.

| Model | Mean predicted PD | Gap | Gap / standard error |
|:---|---:|---:|---:|
| TabPFN v2, 10,000 context rows | 0.28024 | −0.01909 | −2.28 |
| CT, 118,933 rows | 0.29116 | −0.00818 | −0.98 |
| GLM, 118,933 rows | 0.28972 | −0.00962 | −1.15 |

TabPFN's shortfall is real but modest, and the lecture says so in those terms rather than
calling 1.9 percentage points a bias without its standard error. The point that does not
depend on the arithmetic: **TabPFN has no parameter through which a balance correction could
be applied**, so lecture 7's recalibration has to sit outside the model.

### Act three: the ICL-CT, five paired seeds

| Seed | Base CT | ICL-CT | ICL − base | Phase 2 best epoch | Phase 3 best epoch | $a_{i,i}$ |
|---:|---:|---:|---:|---:|---:|---:|
| 100 | 107.342 | 107.342 | 0.000 | 0 | 0 | 0.0009 |
| 101 | 107.288 | 107.327 | +0.039 | 5 | 1 | 0.0011 |
| 102 | 107.330 | 107.313 | −0.017 | 12 | 0 | 0.0010 |
| 103 | 107.265 | 107.249 | −0.016 | 0 | 2 | 0.0010 |
| 104 | 107.499 | 107.551 | +0.052 | 6 | 0 | 0.0011 |

Base mean 107.345 (sd 0.092); ICL-CT mean 107.356 (sd 0.115); **paired difference +0.0115
with a paired standard deviation of 0.0319**, so about a third of its own standard error in
the wrong direction. Pairing is what makes the comparison readable: the unpaired seed spread
is 0.09 here and 0.126 over lecture 10-11's ten seeds.

**Phase 2 best epoch 0 at seeds 100 and 103** means no epoch beat the identity
initialisation, so the selection rule returned the base model unchanged. At the other three
seeds phase two did improve validation and the improvement did not reach the test set. Report
the best-epoch column, because without it a difference of 0.000 is indistinguishable from a
mechanism that trained and happened to tie.

### Act three: why the mechanism finds nothing, in three measurements

**This section was rewritten on 4 September 2026 after review.** The first draft attributed
the null result to attention flatness alone. A reviewer asked whether the batch retrieval was
delivering per-borrower context at all, and the measurement said it largely is not, which is
the lecture's most novel finding and was nearly missed.

**1. The batch context is barely the borrower's own.** Retrieval takes each target's top
$K = 64$ neighbours, unions them across $m = 200$ targets and caps the union at $c = 1000$ by
retrieval frequency. On this book:

| Quantity | Value |
|:---|---:|
| draws (200 × 64) | 12,800 |
| distinct rows in the union | 12,145 |
| context cap | 1,000 |
| mean retrieval frequency | 1.05 |
| maximum retrieval frequency | 2 |
| share of rows retrieved exactly once | 94.6% |
| share of a target's own top-64 surviving the cap, mean | 0.129 |
| the same, median | 0.047 |
| the same, range | 0.000 to 0.766 |

So the median borrower receives **three of its own sixty-four nearest neighbours**, the cap
discards 92 per cent of the union, and it does so on a criterion that is close to a tie-break
because almost nothing is retrieved more than once. The context a borrower actually gets is
near a random thousand-row sample of the learning book. This is the paper's own batching, so
it is a **scale mismatch** rather than an implementation error: a union of 200 neighbourhoods
fits inside 1,000 slots only when neighbourhoods overlap heavily, and on 118,933 loans with
eight covariates they do not.

**2. Per-borrower context does not sharpen the row.** Scoring one target at a time gives it
exactly its own 64 neighbours, which is the sharpest context available.

| | Batch context (200 targets) | Per-borrower context |
|:---|---:|---:|
| context instances | 1,000 | 64 |
| $a_{i,i}$ mean | $9.06 \times 10^{-4}$ | $1.50 \times 10^{-2}$ |
| uniform weight | $9.99 \times 10^{-4}$ | $1.54 \times 10^{-2}$ |
| context weight coefficient of variation | 0.099 | 0.022 |
| largest weight / mean | 1.97 | 1.02 |
| deviance on 400 test rows | 102.024 | 102.201 |
| base model on the same 400 rows | 102.052 | 102.052 |
| largest move from the base model | 0.0195 | 0.0419 |

The row is **flatter** with per-borrower context, and the prediction moves about twice as far
from the base model's without moving anywhere better. Dilution and flatness are therefore
separate facts and neither rescues the mechanism.

**3. The context restates the base model's own prediction.** Retrieved-context default rate
per 200-target batch: mean 0.2874, sd 0.0330, range 0.2080 to 0.4000, against a
learning-sample rate of 0.2888, correlating **+0.6535** with the base model's own predicted PD
for the same targets. Retrieval searches the CLS token space and the decoder reads the CLS
token, so neighbours are by construction the borrowers the base model scores alike.

### Act three: the mechanism's arithmetic and its flatness

- Identity initialisation is exact: max $|p_{\rm ICL} - p_{\rm base}| = 1.19 \times 10^{-7}$.
- Attention rows sum to one within $3.58 \times 10^{-7}$ to $4.77 \times 10^{-7}$.
- Target-to-target attention weights are **exactly zero**, which is the mask working.
- A uniform row over $c + 1 = 1001$ entries would give $9.99 \times 10^{-4}$ to every entry.
  The measured context-weight mean is $9.99 \times 10^{-4}$.
- Own-weight $a_{i,i}$ at seed 100: mean $9.23 \times 10^{-4}$, sd $1.60 \times 10^{-4}$.
- Coefficient of variation of the context weights: **0.100 at initialisation and 0.099 after
  eight phase-two epochs**; largest weight 1.86 then 1.97 times the mean. Training does not
  sharpen the row.
- The last-epoch phase-two state, which validation rejected, scores **107.362** against the
  base model's 107.342.
- Retrieved-context default rate per 200-target batch: mean 0.2874, sd 0.033, range 0.208 to
  0.400, against a learning-sample rate of 0.2888. It correlates **+0.6535** with the base
  model's own predicted PD for the same targets.

Together with the three measurements above these give the null result a mechanism: the
decorator's weight is constant, the retrieved set is barely the borrower's own, attention
averages the injected outcomes almost uniformly either way, and the resulting neighbourhood
mean is two-thirds explained by what the base model already predicts.

### Act four: the Slovak cold start

118,702 learning rows, of which 2,929 relabelled *unseen*; 296 Slovak test loans at an
observed rate of 0.7061 against a learning-sample rate of 0.2879.

| Model | Deviance | 95% bootstrap CI | AUC | Mean predicted PD |
|:---|---:|:---|---:|---:|
| null model | 195.781 | [185.992, 204.958] | | 0.2879 |
| logistic GLM | 185.720 | [175.523, 195.438] | 0.6233 | 0.3084 |
| base CT | 236.626 | [219.568, 253.366] | 0.5497 | 0.2189 |
| ICL-CT, 20 × 50 | 234.636 | [217.776, 251.201] | 0.5529 | 0.2240 |
| ICL-CT, 30 × 100 | 240.798 | | 0.5435 | 0.2135 |

Paired against the base CT over the same 296 loans: the 20 × 50 budget gives **−1.990**
[−2.913, −1.052], improving in 100 per cent of 2,000 resamples and stopping at epoch 6; the
30 × 100 budget gives **+4.172** [3.450, 4.920], improving in 0 per cent and stopping at
epoch 11.

Retrieved context by country, pooled over target batches, against the pool it was drawn from:

| Country | Retrieved share | Pool share | Default rate |
|:---|---:|---:|---:|
| EE | 0.710 | 0.5810 | 0.1703 |
| FI | 0.141 | 0.2415 | 0.3784 |
| ES | 0.149 | 0.1776 | 0.5543 |

Four findings, and the second is the one to quote.

- **Every model under-predicts by around forty percentage points**, so no mechanism here
  repairs a level error of that size.
- **Both networks are decisively worse than the null model**, 236.6 and 234.6 against 195.8,
  with non-overlapping intervals. Predicting the portfolio average for every Slovak applicant
  would have beaten either fitted network.
- **Only the GLM beats the null**, 185.7 against 195.8, and the intervals overlap, so even
  that is not established on 296 loans.
- **Retrieval imports the wrong country's experience**, over-weighting Estonia by about
  thirteen percentage points while pricing a segment whose default rate is four times
  Estonia's. The cause is structural: similarity is measured in the CLS token space of the
  model that is wrong about the segment, so the retrieved neighbours are the applicants that
  model also scores low, and their outcomes confirm the prediction that selected them.

### Act five: reason-code stability under a context re-draw

Ten re-draws taking a random half of the learning sample, 2,000 test borrowers, measured on
the **actively trained** phase-two state, which scores 107.362 against the base model's
107.342.

| Statistic | Active ICL state | Selected state |
|:---|---:|---:|
| per-borrower log-odds sd, mean | 0.0007 | 0.0000 |
| per-borrower log-odds sd, median | 0.0006 | 0.0000 |
| per-borrower log-odds sd, 90th percentile | 0.0011 | 0.0000 |
| per-borrower log-odds range, mean | 0.0023 | 0.0000 |
| per-borrower log-odds range, max | 0.0072 | 0.0000 |
| share moving more than 0.118 | 0.0% | 0.0% |
| share moving more than 1.043 | 0.0% | 0.0% |

Against lecture 9's 1.043 between the leading and second reason codes, and 0.118 between the
second and third, the re-draw moves nothing. **The stability and the null result are the same
fact**: a near-uniform average over a thousand neighbours barely moves when half the pool is
removed. A variant attending sharply to a handful of neighbours would buy accuracy and would
put the reason code back at risk, so the two properties trade against each other.

## What the measurements changed

Two planned claims did not survive, and both are recorded because the wrong version is the
intuitive one.

**The governance claim reversed.** The plan expected the re-draw to destabilise the
prediction, on the argument that an in-context prediction depends on which other borrowers
were retrieved. The measurement says the opposite by three orders of magnitude, and the
lecture now leads on why: the same flatness that denied the mechanism any accuracy also makes
it stable. The prose was rewritten after the measurement rather than around it.

**The seed-100 re-draw of zero is an artefact, not a result.** Because the selection rule
returned the identity initialisation at that seed, the model's ICL layers return the target
token untouched and the prediction cannot depend on the pool at all. Reporting that zero as
evidence of stability would have been badly misleading. Section 5.2 therefore measures the
actively trained state and reports the selected state alongside it as a wiring check. Anyone
editing that section must keep both rows.

**A third claim was incomplete and review caught it.** The first draft explained the null
result by attention flatness alone. The batch-retrieval measurement above shows the context is
also heavily diluted, and the two are independent: sharpening the context to one borrower
makes the row flatter, not sharper. Anyone editing section 3.11 must keep all three
subsections, because dropping the retrieval one restores a claim the data only half supports.

One planned claim was sharpened rather than killed. The plan said in-context learning would
"move the deviance by less than the seed spread". The measurement supports a stronger and more
precise statement, namely that in two of five seeds no epoch beat the identity initialisation,
and where epochs did beat it on validation they lost out of sample.

## Citation register

**Verified as the version the lecture cites.** TabPFN v2 is Hollmann et al. (2025), *Nature*
637(8045) 319-326, and the checkpoint the lecture loads is the v2 classifier, so the citation
and the code agree. The ICL-CT is Padayachy, Richman, Scognamiglio and Wüthrich (2025),
arXiv 2509.08122. The Credibility Transformer is Richman, Scognamiglio and Wüthrich (2025),
*European Actuarial Journal*.

**Corrected, and the correction must not be lost.** The course attributes feature tokenisation
to TabM; it belongs to the **FT-Transformer** of Gorishniy, Rubachev, Khrulkov and Babenko
(2021). `notes/transformer-lecture-structure.md` records the verification, and section 2.3
states the correction explicitly rather than repeating the course's attribution.

**Regulatory.** Two citations, both reused from verifications this series already performed
rather than re-sourced from secondary material.

- **CRR Article 174(c)** as the representativeness anchor, per `R3`. Article 179 is **not** the
  anchor and Article 180(2)(e) carries **no** economic-cycle requirement.
- **UK GDPR Articles 22A to 22D**, substituted for the former Article 22 by the Data (Use and
  Access) Act 2025 and in force in that form since 5 February 2026, per `09`. Much of the
  secondary literature still quotes the superseded Article 22 wording.

Section 5.4 deliberately **declines to resolve** whether pretrained weights are method or data
for the purposes of Article 174(c), and says so, because the question is a supervisory
judgement rather than a statistical one. That is a decision, not an omission.

**Deliberately absent.** No competitor citation, per
`~/.claude/rules/no-competitor-citations.md`. No vendor claim about a tabular foundation
model's production readiness. TabICL, TuneTables and drift-resilient TabPFN are cited as
literature and not run, since none is needed for a question the learning curve settles.

## Render cost and the reuses that must not be tidied apart

Budget: up to roughly thirty minutes, settled 4 September 2026. The fits are:

- **Act two**, 18 Credibility Transformer fits on nested subsamples (six sizes, three draws),
  18 TabPFN calls and 18 GLM fits, then one full-sample GLM, one full-sample CT and one
  TabPFN call at 10,000 rows.
- **Act three**, four further CT fits at seeds 101 to 104, each with an ICL-CT on top.
- **Act four**, one CT fit on the three-country learning sample and two ICL-CT fits on it, one
  per training budget.
- **Act three, section 3.11**, one phase-two ICL fit to a fixed epoch budget, plus the
  per-borrower scoring of 400 test rows at `chunk=1`.
- **Act five** refits nothing; it reuses section 3.11's fixed-budget state.

Three reuses keep the count down and each would silently become a second fit if somebody
"tidied" it.

1. **The seed-100 base CT is fitted once, in section 2.7, and reused as section 3.1's base
   model.** Section 3.1 says so in the prose. Do not re-fit it there.
2. **Section 3.9's seed-100 row reuses section 3.7's fit** rather than repeating it inside the
   five-seed loop.
3. **Act four's 20 × 50 ICL-CT is the model whose context composition section 4.5 reports.**
4. **Section 3.11's fixed-budget state is section 5.2's re-draw subject**, and `Z_pool5` and
   `Z_test5` are computed once in 3.11 and reused in 5.2.

One correctness note about ordering, which is easy to break. Phase three unfreezes the encoder
and `train_icl` restores the selected state into the whole module, base included, so
`base_ct` after section 3.7 is the encoder as at the selected epoch rather than as fitted.
Section 3.11 therefore **recomputes** its CLS tokens from `base_ct` instead of reusing section
3.7's, and the cell carries a comment saying why; section 5.2 then reuses 3.11's. Reusing the earlier tokens would be correct
today, because seed 100 selects epoch 0 in both phases, and would silently go stale the moment
a seed changed.

## Environment note

`tabpfn` 8.5.0 was installed into `.venv` on 4 September 2026 under the render-only precedent
CLAUDE.md already records for `pyyaml`, `nbformat` and `nbclient`. It adds nothing to
`requirements.txt` and it upgraded none of the course pins: `torch` 2.11.0, `polars` 1.40.1,
`scikit-learn` 1.8.0 and `statsmodels` 0.14.6 all survive the install. It pulls `lightgbm`,
`mlx` and `huggingface-hub` as dependencies of its own.

Two traps, both found on 4 September 2026 and both costly to rediscover.

- **The default weights are gated.** `tabpfn` 8.5.0 resolves to the `tabpfn_3` checkpoint,
  which is a gated HuggingFace repository and fails with `TabPFNHuggingFaceGatedRepoError`
  unless the user has accepted its terms and authenticated. Pass
  `model_path="tabpfn-v2-classifier.ckpt"` to select the **v2** checkpoint, which is ungated,
  downloads without credentials, and is the version the course cites.
- **Do not pin `tabpfn` 2.x.** Version 2.2.1 carries ungated weights directly and downgrades
  `scikit-learn` to 1.6.1. Restoring the 1.8.0 pin then breaks `tabpfn` outright with an
  `ImportError` on `_is_pandas_df`. The 8.5.0-with-v2-checkpoint route is what keeps both the
  course pins and the cited model version.

TabPFN also refuses to run on CPU above 1,000 samples unless `ignore_pretraining_limits=True`
is set, and it takes `device="mps"` on this machine per CLAUDE.md's Apple silicon note.

One naming trap in the lecture's own code: `patsy` exports `C()` for a categorical contrast, so
a module aliased to `C` shadows it and the design-matrix build fails with
`'module' object is not callable`. The lecture builds its design matrix in the same cell that
uses `C(Education)`, so this only bites in scratchpad scripts, where it cost a debugging cycle.

## Deliverables

1. `credit_lectures/12_credit-foundation-models.qmd`. Done.
2. Rendered HTML via `bash scripts/render_lecture.sh`, never bare `quarto render`.
3. PDF via `bash scripts/html_to_pdf.sh`, with a page of mathematics opened and eyeballed,
   because a slow MathJax CDN yields raw TeX in a PDF that still exits zero.
4. This note, converted from contract to register. Done.
5. An `index.html` entry, and the lecture count moved from eighteen to nineteen there and in
   CLAUDE.md's directory table, with a results summary in the table entry.
