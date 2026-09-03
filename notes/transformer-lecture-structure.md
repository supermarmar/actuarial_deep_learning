# Credit lectures 10 and 11: overlap map, notation bridge, measured facts and citation register

Working note for `credit_lectures/10-11_credit-transformer.qmd`, the companion to
`lectures/10-11_transformers.html`. It records what the earlier lectures already own and must
not be redefined, which numbers were measured before any prose was written, and which
citations survived verification.

Read this before editing the lecture. Everything settled here is settled.

## Why the lecture exists, and what it discharges

Course lectures 10 and 11 introduce attention layers, the Transformer layer, feature
tokenisation for tabular data, and the Credibility Transformer of Richman, Scognamiglio and
Wüthrich (2025). Three debts in the credit series point here.

- `06:1205-1215` builds the entity embedding into a common $\mathbb{R}^b$ and then says
  outright that this construction is what an attention layer needs: "Hence the Credibility
  Transformer of Richman, Scognamiglio and Wüthrich (2025), which the tenth and eleventh
  lectures build, starts from the construction in this section." The lecture therefore
  starts from lecture 6's tokens rather than re-deriving them.
- `03:837-843` promises attention "in full" and names the dataset: "the Amex panel is the
  dataset in this series it was made for." That promise is discharged literally, in the
  sequential act.
- `03:798-804` closes the recurrence section with "Both are superseded for most purposes by
  attention, which the transformer lectures take up."

## The two-act structure, decided 3 September 2026

Mario chose a tabular spine plus a bounded sequential act.

**Act one, sections 1 to 2, sequential, on the Amex panel.** This is the act that has no
insurance counterpart. Course section 2.5 introduces time-causal masking and then never
applies it, because tabular tokenisation is explicitly permutation invariant. A monthly
behavioural panel makes the mask a leakage control instead of a technicality.

**Act two, sections 3 to 5, tabular, on the Bondora book.** This is the course's own
centrepiece and it carries the series' deviance comparison, so it uses
`bondora_pd.parquet` with the filters, the seed-1 80/20 split and the
$100 \times 2 \times$ mean-Bernoulli scale of lectures 2 and 4 to 9 unchanged.

### Why not Home Credit for the sequential act

The first plan used `home_credit_cards.parquet`, on the ground that it carries a
month-stamped days-past-due field and is 53 MB against the Amex panel's 2.97 GB. It was
rejected on 3 September 2026 for a decisive reason: **the converted table carries no
response variable.** Home Credit's target lives in `application_train.csv`, which
`convert_credit_data.py` never converts, so a supervised sequential model there would have
to invent a target out of `SK_DPD`. That is D1's territory, not this lecture's. The Amex
panel carries `target` already, and it is the dataset lecture 3 named.

The Amex file's size turned out not to matter. A column-projected `scan_parquet` over
`customer_ID`, `S_2`, `target` and eight behavioural channels collects in under a second.

## What the earlier lectures already own

**Do not redefine any of the following.** Cite backwards.

| Already owned | Where |
|---|---|
| Entity embedding, its dimension, and the common $\mathbb{R}^b$ token space | `06:810-1215` |
| Bühlmann credibility, its shrinkage parameter and the borrow-strength argument | `06:576-600` |
| Weight of evidence as target encoding on the log-odds scale | `06:536-575`, applied in `F1` |
| Standardisation, and censoring a tail before standardising | `06:1131-1159` |
| The FNN, its widths, the training routine and early stopping | `04-05:118-160`, `04-05:405-470` |
| Nagging, and why $\sqrt{M}$ needs the split held fixed | `06:130-166` |
| The balance property and canonical-link exactness | `07`, and `08:1266-1374` |
| Bernoulli deviance on the series scale | `04-05` onwards |
| Drop-out as a regulariser | `08` |
| The attention-weight decomposition and reason codes | `09` |
| The outcome window, and that a target is a claim about a sequence of states | `D1` |
| Sample design, the four samples and clustered splitting | `R3` |
| Recurrence, convolution and where each suits credit | `03:783-804` |

## Boundaries

**`C2` owns causal reading.** `C1:74-75` defers SHAP, LocalGLMnet and ICE marginal effects
read causally to `C2`. The same line binds here: the lecture says what a CLS-token attention
weight **is** and cites `C2` forward wherever the temptation to read it as an effect arises.

**`09` owns reason codes.** Lecture 9 built the per-decision decomposition and measured its
stability. This lecture does not re-issue reason codes; where the CLS token's attention over
covariates looks like a variable importance measure, the lecture says so and points back to
`09`'s noise-calibrated test rather than inventing a second one.

**`D1` owns the target.** The Amex `target` is default within 18 months of the customer's
**latest** statement, so it is fixed at customer level. What varies across the months of the
panel is the information set alone, not the horizon. The lecture states that explicitly,
because it is what makes the month-by-month AUC curve a clean measurement of information
accumulation rather than a confounded one, and it cites `D1` for outcome windows.

## Notation bridge

The course carries two symbol clashes of its own and this series adds two more.

| Symbol | Course | Here |
|---|---|---|
| $t$ | sequence length | unchanged; 13 monthly statements in act one |
| $q$ | number of channels in §1-2, **and** covariate count in §3-4 | covariate count **only** |
| $b$ | channels, §3-4 only | channels **throughout**, act one included |
| $\boldsymbol{q}_u$ | query vector | unchanged |
| $g$ | log link, Poisson | logit link, Bernoulli |
| $\mu(\boldsymbol{X})$ | expected claim count per unit exposure | probability of default within twelve months |
| $v_i$ | exposure in policy-years | absent; all case weights are one |
| $\alpha$ | Bernoulli gate probability, **and** the drop-out rate in the appendix | gate probability only; the appendix rate is $\alpha^{\rm drop}$ |
| $Z$ | the Bernoulli gate variable | unchanged |
| $P$, $1-P$ | implicit weights on covariate and prior values | unchanged |

Four resolutions worth stating.

**$q$ against $b$.** The course writes $\mathbb{R}^{t \times q}$ for sequential data with $q$
channels, then in section 3 writes $\mathbb{R}^{q \times b}$ for tabular data with $q$
covariates and $b$ channels. The same letter therefore means channels in one half and
covariate count in the other. This lecture uses $b$ for channels everywhere and reserves $q$
for the covariate count, so the two acts share one notation. Lecture 9 used $q$ in the
covariate-count sense too, and `R2`'s risk-grade $q$ does not appear here.

**$\alpha$ against lecture 6's $\alpha_k$.** This is the clash that matters, because it sits
inside the one concept the lecture bridges. `06:580-590` writes Bühlmann credibility as
$\overline{y}^{\rm cred}_k = \alpha_k \overline{y}_k + (1-\alpha_k)\overline{y}$ with
$\alpha_k = n_k/(n_k+\tau)$, so lecture 6's $\alpha_k$ is a **credibility weight on the
data**. The course's $\alpha$ is a **Bernoulli probability**. They are not the same kind of
object and the lecture must not let the letter suggest otherwise. Resolution: $\alpha$
unsubscripted is the gate probability, $\alpha_k$ subscripted is lecture 6's credibility
weight, and the lecture says this the first time either appears.

**The direction of the credibility weight.** The quantity that actually corresponds to
lecture 6's $\alpha_k$ is $P$, not $\alpha$. Both weight the data-driven estimate, and both
leave the complement on a prior that carries no covariate information: lecture 6's global
mean $\overline{y}$, and the CT's prior token. That correspondence is the bridge, and it is
exact in form rather than by analogy.

**$Z$.** The classical actuarial literature writes the Bühlmann credibility factor as $Z$.
The course writes the Bernoulli gate variable as $Z$. This lecture uses $Z$ for the gate
variable only and never for a credibility factor, and flags the collision once.

## Design decisions

**One attention head, not multi-head.** Course section 4.7 derives the implicit credibility
mechanism from the last row of a **single** attention head, $H_{q+1} = A_{q+1}V$, and reads
$1-P := a_{q+1,q+1}$ off it. With $n_h$ heads there are $n_h$ such weights and no single
credibility weight to report. Since the implicit mechanism is where this lecture's own
finding sits, the architecture stays single-headed and the lecture says why. Multi-head is
defined in section 1 and its consequence for the reading is stated.

**Hand-rolled in torch.** The reference implementation of the Credibility Transformer is
R and Keras, and every credit lecture in this series is Python and torch, so layer
normalisation, the time-distributed FNN, scaled dot-product attention, the feature
tokeniser, the CLS token, the prior token and the Bernoulli gate are all built here. Only
`torch.nn.LayerNorm` is taken off the shelf, and it is the course's mapping exactly: it
normalises over the channel dimension within each time slice, which is what
$\boldsymbol{z}^{\rm norm}$ does.

**The tabular design is the tokenised one, so it is a third design matrix.** Lectures 4 to 8
use a 38-column one-hot design; lecture 9 used a 14-column PCA-rotated embedded design; this
lecture tokenises 5 categoricals and 3 continuous covariates into 8 tokens of $b$ channels.
The three are not interchangeable. What is held fixed is the modelling frame, the filters,
the sample and the split, which is what makes the deviances comparable.

**Continuous covariates get depth-2 FNNs per covariate**, following course section 3.3, and
the lecture notes the GAM parallel the course draws. Piecewise linear encoding is named and
not implemented, with `F1`'s classing cited as the credit tradition's answer to the same
problem.

## Citation register

Every citation was checked before the lecture quoted it. Three findings changed what the
lecture says.

| Claim | Verdict | Note |
|---|---|---|
| Vaswani et al. (2017), *Attention is all you need*, NeurIPS 30 | verified | The attention mechanism and positional encoding |
| Ba, Kiros and Hinton (2016), *Layer normalization*, arXiv:1607.06450 | verified | |
| Ioffe and Szegedy (2015), *Batch normalization*, ICML, PMLR 37, 448-456 | verified | Cited for the contrast only |
| Devlin et al. (2019), *BERT*, NAACL-HLT, 4171-4186 | verified | The CLS token |
| Feature tokenisation is **Gorishniy, Rubachev, Khrulkov and Babenko (2021)**, *Revisiting deep learning models for tabular data*, NeurIPS 34, arXiv:2106.11959 | **corrected** | See below |
| Gorishniy, Rubachev and Babenko (2022), *On embeddings for numerical features in tabular deep learning*, NeurIPS 35, arXiv:2203.05556 | verified | Piecewise linear encoding, named and not implemented |
| Gorishniy, Kotelnikov and Babenko (2024), *TabM*, arXiv:2410.24210, ICLR 2025 | verified, and **not** about tokenisation | See below |
| Bühlmann (1967), *Experience rating and credibility*, ASTIN Bulletin 4(3), 199-207 | verified | Already cited by lecture 6 |
| Bühlmann and Straub (1970), Mitteilungen SVVM 1970, 111-131 | verified | |
| Richman, Scognamiglio and Wüthrich (2025), *The credibility transformer*, European Actuarial Journal | verified | The architecture |
| Srivastava et al. (2014), *Dropout*, JMLR 15(1), 1929-1958 | verified | Appendix |
| Wager, Wang and Liang (2013), *Dropout training as adaptive regularization*, NeurIPS 26 | verified | Appendix |
| The course's roughly 7 per cent prior credibility weight | attributed to the course | The figure is stated in course section 4.7 on the French motor data, so the lecture attributes it there rather than to the paper |

### The tokenisation citation, corrected

Course section 3 introduces feature tokenisation and attributes it to "the approach proposed
by Gorishniy, Kotelnikov and Babenko (2024)", which is TabM. Both halves of that were
checked on 3 September 2026 and the attribution does not hold.

- **TabM** (arXiv:2410.24210, ICLR 2025) is about parameter-efficient ensembling: an
  ensemble of MLPs implemented as one model sharing most parameters, built on
  BatchEnsemble. It proposes no tokeniser.
- **Feature tokenisation**, meaning the module that maps each categorical and each
  continuous covariate into a shared $b$-dimensional space so a Transformer can consume a
  tabular row, is the FT-Transformer of **Gorishniy, Rubachev, Khrulkov and Babenko (2021)**
  (arXiv:2106.11959, NeurIPS 34).

The lecture therefore cites the 2021 paper for the construction it actually uses and does
not cite TabM at all. The slip is worth recording rather than silently fixing, because a
reader working from the course notes will look for a tokeniser in TabM and fail to find one.

### Deliberately absent

**No regulatory citation.** Earlier lectures in this series carry verified regulatory
references, and this one carries none, which is a decision rather than an omission. The
leakage finding of section 2.4 is a modelling failure with obvious supervisory consequences,
and the temptation was to reach for a model risk management or a representativeness article.
`R3` already owns representativeness and anchored it on CRR Article 174(c) after
verification rejected three other candidates; `D1` owns the default definition and Article
178. Adding an unverified article here would put a weaker claim beside their verified ones.
Section 2.4 therefore cites `R3` forward and states the failure in modelling terms.

## Measured facts

Every number below was measured before any prose was written, and the prose quotes these.
Two independent runs of the sequential act reproduced identically after the determinism fix
recorded below, and the tabular act reproduces the values lecture 9 and lecture 6 published
for the shared split.

### Act one: the Amex behavioural panel

Panel as loaded: 5,531,451 statements over 458,913 customers, dated 2017-03-01 to
2018-03-31. History lengths run 1 to 13, and 386,034 customers (84.1 per cent) carry the
full 13. The lecture subsamples 60,000 of those, giving 780,000 statement rows, an 80/20
customer split of 48,000 and 12,000, and a default rate of 0.23298.

| Measurement | Value |
|---|---|
| Causal model, AUC at month 1 | 0.8828 |
| Causal model, AUC at month 13 | 0.9468 |
| Unmasked model, AUC at month 1 | 0.9309 |
| Unmasked model, AUC at month 13 | 0.9390 |
| Leakage gap at month 1 | +0.0481 of AUC |
| Month-13 deviance, causal against unmasked | 49.370 against 52.385 |
| Correct model scored on a reversed panel, AUC month 1 to month 13 | 0.9406 falling to 0.8927 |
| Mis-sorted throughout, AUC month 1 to month 13 | 0.9435 falling to 0.9398 |
| Mis-sorted throughout, month-1 deviance against the honest one | 50.595 against 70.324 |
| Permutation equivariance, unmasked model, largest discrepancy | 2.38e-07 |
| Permutation equivariance, causal model, largest discrepancy | 0.591 |
| No positional channel, unmasked, largest discrepancy | 2.38e-07 |
| Final month's attention row, minimum and maximum | 0.0728 and 0.0840, against uniform 0.0769 |

**The determinism fix.** `polars` `group_by` returns groups in a non-deterministic order, so
`.sample(n, seed=11)` over its output drew a different customer subsample on every run: two
runs gave default rates of 0.23048 and 0.23232 before the fix. Sorting on `customer_ID`
before sampling makes the subsample reproducible, and two runs afterwards agreed on 0.23298
and on every fitted figure, early-stopping epoch included. The lecture carries the comment
explaining it, because the failure is silent.

**Why the two mis-sort variants are both shown.** Scoring a correctly fitted model on a
reversed panel inverts the discrimination profile, which is loud. Fitting on the reversed
panel is quiet and therefore worse: it is self-consistent, so a hold-out sample carrying the
same bug validates it. The only surviving tell is the shape of the profile, and that is the
lecture's practical recommendation.

### Act two: the Bondora book

Frame as in lectures 4 to 9: $n = 148{,}667$, learn 118,933 and test 29,734, learning-sample
default rate 0.28878. Cardinalities `Country` 4, `Education` 5, `HomeOwnership` 12,
`VerificationType` 4, `EmploymentDuration` 10, so 8 covariates become 8 tokens.

| Model | In-sample | Out-of-sample | Source |
|---|---|---|---|
| Null model | | 120.80 | `07:971` |
| GLM3 | 106.641 | 108.197 | `02:903` |
| FNN, one-hot, single fit | | 107.621 | `04-05:524` |
| FNN, one-hot, mean over 10 seeds | | 107.710, sd 0.124 | `06:961-962` |
| FNN, embedding, mean over 10 seeds | | 107.313, sd 0.072 | `06:961-962` |
| ICEnet, $\lambda = 0.1$ | | 107.583 | `08:1208` |
| LocalGLMnet, seed 100 | 104.874 | 107.360 | `09` |
| LocalGLMnet, mean over 10 seeds | | 107.434, sd 0.086 | `09` |
| **Credibility Transformer, seed 100** | **105.502** | **107.342** | measured here |
| **Credibility Transformer, mean over 10 seeds** | | **107.381, sd 0.126** | measured here |
| FNN, one-hot, nagged $M = 10$ | | 107.120 | `06:965` |
| LocalGLMnet, nagged $M = 10$ | | 107.132 | `09` |
| **Credibility Transformer, nagged $M = 10$** | | **107.097** | measured here |
| FNN, embedding, nagged $M = 10$ | | 106.921 | `06:965` |

**The comparison the lecture must make honestly.** The seed-100 fit at 107.342 is the best
single fit in the series, and that is largely seed luck. On means over ten seeds the CT's
107.381 sits between the LocalGLMnet's 107.434 and the embedded network's 107.313, and
neither difference is significant: the unpaired standard error of the CT-against-LocalGLMnet
difference is 0.048 against a difference of 0.053, and of the CT-against-embedding
difference 0.046 against 0.068. Nagged over ten fits the CT reaches 107.097, second in the
series behind lecture 6's nagged embedding network at 106.921.

Consequently the lecture claims that the Credibility Transformer competes and does not lead,
and it must not repeat the framing that lecture 9 used for the LocalGLMnet. Any future edit
tempted to promote the 107.342 figure should read this paragraph first.

**Balance.** The CT misses the balance property by $-0.98$ per cent at seed 100 and $-1.41$
per cent nagged over ten fits, so it behaves as lecture 7 predicts for a non-canonical
readout and balance still has to be imposed. Lecture 6 measured a shared systematic miss of
$-0.42$ per cent for the ensembled network, so the CT's miss is the larger of the two.

**The prior token learns the null model, exactly as the course says.** Forcing $Z = 0$ at
prediction gives a constant fitted probability of 0.28701 with a standard deviation of
0.000000 across the 29,734 test loans, and a deviance of 120.815 against the null model's
120.808. The tiny gap is the difference between the prior token's learned constant and the
learning-sample default rate of 0.28878, and the constancy is exact because
$\boldsymbol{c}^{\rm prior}$ has no covariate input.

### The explicit credibility mechanism

Single fit at seed 100 for each $\alpha$, so the accuracy column separates nothing.

| $\alpha$ | Early stop | Out-of-sample | Prior token alone | sd of the prior prediction |
|---|---|---|---|---|
| 0.50 | 131 | 107.456 | 120.811 | 3.0e-08 |
| 0.80 | 82 | 107.540 | 120.802 | 0.0 |
| 0.95 | 149 | 107.342 | 120.815 | 6.0e-08 |
| 1.00 | 139 | **107.327** | 185.956 | 0.0 |

Two readings, and the second is the one the lecture leads on.

The mechanism works mechanically. At every $\alpha < 1$ the prior token is constant to
floating point and its deviance lands within 0.01 of the null model's 120.808. At
$\alpha = 1$ the gate never selects it, so no gradient reaches it and its deviance is
185.956, an untrained constant. Hence the gate is the only thing that trains the prior.

The mechanism buys no accuracy here. The four fits span 0.213, against the seed standard
deviation of 0.126 measured over ten fits, so the sweep is 1.7 standard deviations wide and
resolves nothing; and the best point estimate is $\alpha = 1.00$, meaning the mechanism
switched off. The course selected $\alpha = 0.95$ by cross-validation on the French motor
data and reported a gain. That gain does not reproduce on Bondora. The lecture keeps
$\alpha = 0.95$ downstream only because the implicit mechanism needs a trained prior token
to be interpretable.

### The implicit credibility weight, which is the lecture's own finding

Primary fit, seed 100, over the 29,734 test loans: mean 0.0295, sd 0.0045, range 0.0193 to
0.0438, quartiles 0.0255 and 0.0332, 1st and 99th percentiles 0.0217 and 0.0393. Course
section 4.7 reports roughly 0.07 on the French motor portfolio.

**The weight is a property of the fit.** Mean $1-P$ by seed, over ten fits differing only in
seed: 0.0295, 0.0903, 0.0658, 0.0976, 0.0577, 0.1414, 0.0465, 0.0707, 0.1683, 0.0681. The
between-fit standard deviation of the mean is 0.0427 and the within-fit standard deviation
across borrowers runs 0.0045 to 0.0206, so the ratio at seed 100 is **9.4**. The fit means
span 0.1388 where the whole book at seed 100 spans 0.0245, a factor of 5.7.

Consequently no threshold on $1-P$ survives a refit, and the lecture says so. The comparison
with `09` is deliberate: there the leading reason code reproduced for 92.0 per cent of
high-risk applicants, so one code was defensible, whereas here the quantity's own level moves
by a factor of five.

**It tracks no thin-file measure.**

| Prior experience at Bondora | Mean $1-P$ | sd | $n$ |
|---|---|---|---|
| No prior loan | 0.0293 | 0.0048 | 14,455 |
| 1 to 2 prior loans | 0.0292 | 0.0046 | 9,085 |
| 3 or more prior loans | 0.0305 | 0.0036 | 6,194 |

Every difference is smaller than the 0.0045 within-fit standard deviation, and the ordering
runs **against** the credibility direction: more lender experience of the borrower attracts
slightly more weight on the prior. `VerificationType` spans 0.0283 to 0.0315.

**What it does associate with** is the prediction, at $-0.6655$, with log income at
$-0.3666$ and censored age at $-0.1593$. Mean $1-P$ by decile of fitted PD: 0.0314, 0.0330,
0.0331, 0.0331, 0.0322, 0.0296, 0.0269, 0.0259, 0.0247, 0.0250. The lecture states this as an
association and flags two limits: `C2` owns the causal reading, and $1-P$ and the fitted
probability are both functions of the same attention row, so part of the correlation is
mechanical.

### The CLS token's attention over characteristics

Seed 100, ascending: `Education` 0.0846, `logIncome` 0.0936, `EmploymentDuration` 0.1049,
`VerificationType` 0.1105, `HomeOwnership` 0.1125, `Country` 0.1324, `AgeCens` 0.1537,
`NewCreditCustomer` 0.1783. Those eight sum to 0.9705 and with $1-P = 0.0295$ the row sums to
1.0000, which is the check that the decomposition of section 4.3 was read off correctly.

Uniform over the $q+1 = 9$ rows would be 0.1111, and the observed spread is a factor of 2.11,
so the differentiation is mild. Across-fit standard deviations run 0.0178 to 0.0385.

**The leading characteristic is unstable at the primary fit.** Nine of the ten fits put
`Country` first and seed 100 puts `NewCreditCustomer` first. Quoting seed 100's ordering as
the model's view of importance would therefore misreport it, and the lecture prints all
three columns rather than the primary fit alone.

Because of that, and because no noise covariate calibrates the weights, **the lecture
declines to call this a variable importance measure** and points at `09`'s noise-calibrated
test instead. Course section 4.7 suggests the measure; this is where the companion parts
from it.

## Render cost

Thirteen tabular fits and four sequential fits, so the render takes roughly half an hour on
this machine. The fits are: one at $\alpha = 1$ for section 3.5, three more for the sweep at
0.50, 0.80 and 0.95, and nine at seeds 101 to 109 for the nagging. The seed-100
$\alpha = 0.95$ fit from the sweep is reused as the primary model and the $\alpha = 1$ fit is
reused as the sweep's last row, which is what keeps the count at thirteen rather than
fifteen. Do not "tidy" those reuses into separate fits.
