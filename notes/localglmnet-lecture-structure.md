# Credit lecture 9: overlap map, notation bridge, measured facts and citation register

Working note for `credit_lectures/09_credit-localglmnet.qmd`, the companion to
`lectures/09_localglmnet.html`. It records what the earlier lectures already own and must not
be redefined, which numbers were measured before any prose was written, and which regulatory
claims survived verification against primary text.

Read this before editing the lecture. Everything settled here is settled.

## Why the lecture exists, and what it discharges

Lecture 9 of the course presents the LocalGLMnet of Richman and Wüthrich (2023b), a GLM whose
coefficient vector is replaced by the outputs of a multi-output network, so the model is
locally a GLM everywhere and every individual prediction decomposes into per-covariate
contributions. Three debts in the credit series point here.

- `03:845-856` calls LocalGLMnet "arguably the most important idea in the course" for credit,
  on the ground that a lender declining an application needs a per-decision decomposition, and
  that getting one from a fitted structure beats a post hoc attribution method in front of a
  supervisor. The lecture discharges that with a measurement rather than a restatement.
- `06:1125-1128` defers the question of what a fitted model has learned about levels to "the
  interpretability tools the ninth lecture introduces, which work on the fitted regression
  function rather than on internal weights".
- `08:1424-1428` names the ninth lecture as where LocalGLMnet is taken up.

## The C2 boundary, decided 3 September 2026

`C1:74-75` defers SHAP, LocalGLMnet and ICE marginal effects **read causally** to `C2`. Mario
confirmed on 3 September 2026 that lecture 9 stops short of that line.

- **09 owns** the architecture, the attention weights, the noise-calibrated variable importance
  test, interactions read off the attention gradient, and the reason-code decomposition with
  its stability.
- **09 does not own** whether an attention weight may be read as an effect. Every place the
  temptation arises, the lecture states what the weight is and cites `C2` forward.

The precedent is `F1`, which stops at the fitted feature set and cites `R3` forward for
stability.

## What the earlier lectures already own

**Do not redefine any of the following.** Cite backwards.

| Already owned | Where |
|---|---|
| Entity embedding, its dimension, and whether proximity tracks risk | `06:810-1128` |
| Standardisation, censoring a tail before standardising | `06:1131-1159` |
| The FNN, its widths, the training routine and early stopping | `04-05:118-160`, `04-05:405-470` |
| Nagging, and why $\sqrt{M}$ needs the split held fixed | `06:130-166` |
| The balance property and canonical-link exactness | `07`, and `08:1266-1374` |
| Bernoulli deviance on the series scale, $100 \times 2 \times$ the mean contribution | `04-05` onwards |
| Information value and weight of evidence | `06:536-575`, applied in `F1` |
| Group LASSO as a scorecard's variable-reduction step | `08:499-584` |
| Individual conditional expectation and the partial dependence plot | `08:804-855` |
| Population stability and the two-sample classifier | `R3:553-737` |

The lecture reuses lecture 6's `EmbedFNN` idiom rather than restating the case for embeddings.

## Notation bridge

The course writes the LocalGLMnet in Poisson form with an exposure offset. The credit series
has no offset, since `default_12m` is a zero-one flag over a fixed twelve-month window, so the
case weights are all one. Three symbols therefore need pinning.

| Symbol | Course | Here |
|---|---|---|
| $g$ | log link, Poisson | logit link, Bernoulli |
| $\mu_\vartheta(\boldsymbol{X})$ | expected claim count per unit exposure | probability of default within twelve months |
| $v_i$ | exposure in policy-years | absent; all case weights are one |
| $z_j^{(d:1)}(\boldsymbol{X})$ | attention weight | unchanged |
| $\operatorname{VI}_j$ | $\frac1n\sum_i |z_j(\boldsymbol{X}_i)|$ | unchanged, on the test sample |

One clash to avoid. The course's $q$ is the covariate count and `R2` uses $q$ for a risk-grade
index. Lecture 9 uses $q$ in the course's sense only, and mentions no risk grade.

A second clash, introduced here. The attention weight $z_j$ collides with the $z$-statistic
printed in every `statsmodels` GLM summary the series quotes. The lecture prints that summary
once and labels the column explicitly when it does.

## Design decisions

**Categoricals enter as two-dimensional entity embeddings, PCA-rotated within each
characteristic.** This follows the course, which uses the previous lecture's embeddings for
exactly this reason: the variable importance measure compares magnitudes of $z_j$ across
components, which requires every component standardised and continuous, and the course states
outright that one-hot encoding makes the testing harder and would want group LASSO instead.
The design has $q = 14$ columns against the 38 of the one-hot design used from lecture 4
onwards, so the two are not interchangeable and the lecture says so.

The embedding is fitted once, at seed 100, and held fixed across every LocalGLMnet refit. That
is a deliberate limitation and the lecture states it: the reason-code instability measured in
section 9 is therefore a lower bound, since refitting the embedding would add variance this
design holds constant. Lecture 6 found embedding proximity did not track risk across refits,
which is the reason the caveat matters here.

**Reason codes are ranked at characteristic level, never at coordinate level.** `CountryEmb1`
is a rotated coordinate of a two-dimensional embedding and no borrower could be told anything
about it. The interpretable object is the grouped contribution $\sum_{j \in k} z_j(\boldsymbol{X})X_j$
summed over the coordinates belonging to characteristic $k$.

**The declined population is the highest-PD decile of the test sample.** A reason code is
issued only where the decision is adverse, so measuring code stability over approved applicants
measures a quantity nobody computes. The lecture reports the approved figure once, for contrast,
and labels it as such.

**The noise band is centred on zero.** The null hypothesis is $z_j \equiv 0$, so the band is
$\pm 2.576 \, \widehat{\sigma}(z_{\rm RandN})$ about zero, and the fitted mean of the noise
term is reported separately as the bias. The course notes that its own interquartile shading
ignores that bias; this lecture states the convention instead of leaving it implicit.

## Measured facts

Every number below was computed before any prose was written, in
`scratchpad/lgn*.py`, and is reproduced by the lecture's own cells. Where the render disagrees
with this table, the render is right and this table is stale.

**Sample and design.** $n = 148{,}667$; learn 118,933, test 29,734; learning-sample default rate
0.28878, test 0.29209. Embedding cardinalities including the reserved unseen index: Country 5,
Education 6, HomeOwnership 13, VerificationType 5, EmploymentDuration 11. Embedding FNN early
stop 161. Design $q = 14$.

**Benchmark GLM on the standardised embedded design.** Learn 106.945, test 108.522. `RandN` is
the only term failing its Wald test, at $p = 0.4411$; `CountryEmb1` reaches $z = -100.6$. Note
that this GLM is *worse* out of sample than the banded GLM of lecture 2 at 108.20, which is
worth a sentence.

**Initialisation.** The GLM-initialised network returns 106.945 and 108.522 exactly, to three
decimals, on both samples.

**Fit.** Seed 100: early stop 67, learn 104.874, test 107.360. Over seeds 100 to 104 the test
deviance has mean 107.446 and standard deviation 0.115. Nagged over ten fits, 107.132 against
an individual-fit mean of 107.434. Series comparison: GLM 108.20, FNN 107.621 at AUC 0.7241,
ICEnet at $\lambda = 0.1$ 107.583. The LocalGLMnet therefore beats the FNN here, where in the
course it came out slightly worse.

**Noise calibration.** Seed 100: $z_{\rm RandN}$ has mean 0.01241 and standard deviation
0.04805, so the zero-centred 99 per cent band is $\pm 0.1238$. Nagged over ten fits the
standard deviation falls to 0.01394 and the band to $\pm 0.0359$.

**Variable importance, seed 100.** Smallest `RandN` 0.0408, largest `CountryEmb1` 0.8005. Over
five seeds `RandN` is 0.0335 (sd 0.0069) and `logIncome` 0.1066 (sd 0.0308).

**Grouped importance against the other two orderings.** Spearman correlation with `F1`'s
information values is 0.619 over eight characteristics. All three orderings put `Country`
first. The two disagreements are `Age` (importance rank 4, information value rank 8) and
`logIncome` (importance rank 8, information value rank 4), and the series already explains
both: `F1` reports age's information value at 0.0066 *because* forcing monotonicity reports
lecture 1's hump as noise, and `08` drops `logIncome` first under group LASSO while `C1` finds
income moves the fitted PD by under three points once country is held fixed.

**The income sign flip, and its verdict.** Seed 100 gives 37.4 per cent of borrowers a positive
income attention weight, and a clean country ordering: EE $+0.0400$, ES $-0.1235$, FI
$-0.1618$, SK $-0.2667$. Seed 104 reverses it: EE $-0.0466$, FI $+0.0130$, ES $+0.0022$. Over
ten fits the country means are EE $-0.0120$ (sd 0.0322), FI $-0.0395$ (sd 0.0545), ES $-0.0573$
(sd 0.0412), SK $-0.0630$ (sd 0.1256). The between-country spread from EE to ES is 0.045 and
the between-fit standard deviations run 0.032 to 0.055, so **the varying coefficient is
directionally consistent with `C1` and cannot establish it alone.** Report it that way.

**Interactions.** Noise ceiling: the largest mean absolute gradient of $z_{\rm RandN}$ with
respect to any covariate is 0.0331. Pairs clearing it include $\partial z_{\rm HomeOwnershipEmb2}
/ \partial x_{\rm EducationEmb1}$ at 0.1354, $\partial z_{\rm CountryEmb2} / \partial
x_{\rm logIncome}$ at 0.0992 and $\partial z_{\rm logIncome} / \partial x_{\rm NewCredit}$ at
0.0958. Own-component $\partial z_{\rm Age} / \partial x_{\rm Age}$ is 0.1368.

**Reason codes.** The logit reconstruction $\vartheta_0 + \sum_j z_j X_j$ matches the fitted
logit to a maximum absolute error of $1.67 \times 10^{-6}$. In the highest-PD decile, 2,974
applicants, ranked at characteristic level over ten fits:

| Rank | Identical across all ten fits | Mean distinct codes |
|---|---|---|
| 1 | 92.0 % | 1.15 |
| 2 | 1.6 % | 3.06 |
| 3 | 0.1 % | 4.13 |

Mechanism, fit 1 of the decile: mean contribution by rank 1.3305, 0.2873, 0.1692, 0.1015, so
the rank 1 to rank 2 gap is 1.0432 while rank 2 to rank 3 is 0.1181 and rank 3 to rank 4 is
0.0677. `Country` is the rank 1 code for 2,770 of the 2,974, that is 93.1 per cent, and the
rank 2 code splits across `HomeOwnership` 772, `NewCreditCustomer` 727, `Age` 601 and
`Education` 313. Tightening to the highest-PD 5 per cent gives rank 1 at 96.3 per cent and rank
2 at 0.7 per cent. For contrast only, over the 90 per cent outside the decline region rank 1
agrees for 21.1 per cent.

**Final model, noise column dropped.** Early stop 38, learn 105.203, test 107.358, AUC 0.7254,
balance $-1.40$ per cent against the observed test rate.

## Citation register

Every regulatory claim was checked against primary text on 3 September 2026. The lecture makes
no regulatory claim beyond the two verified below.

| Claim | Source | Verdict |
|---|---|---|
| On declining a prospective regulated agreement on the basis of credit reference information, the creditor must inform the debtor that the decision was reached on that basis and give the agency's name, address and telephone number | Consumer Credit Act 1974 s.157(A1), inserted by the Consumer Credit (EU Directive) Regulations 2010 with effect from 1 February 2011 | **Verified** against legislation.gov.uk |
| Where a significant decision is taken with no meaningful human involvement, the controller must secure safeguards that provide the data subject with information about the decision, and enable them to make representations, obtain human intervention and contest it | UK GDPR Article 22C, substituted for the former Article 22 by the Data (Use and Access) Act 2025 s.80, fully in force 5 February 2026 | **Verified** against legislation.gov.uk |

Two consequences the lecture draws, and neither goes further than the text supports. First,
neither provision prescribes a ranked list of reasons, so reason codes are industry practice
discharging a duty stated more generally. Second, quoting the pre-2025 Article 22 would now be
wrong, and a good deal of the secondary literature still does.

**Not cited, and why.** Directive (EU) 2023/2225, the recast Consumer Credit Directive, almost
certainly carries the closer EU analogue for an Estonian book. EUR-Lex returned no body text on
two attempts on 3 September 2026, so the claim could not be verified and the lecture cites
around it, following the precedent `notes/irb-lecture-structure.md` set for four unverifiable
citations in `R2`. The lecture states plainly that it takes the UK duty as its worked example
and that Bondora's own jurisdiction differs. Anyone with EUR-Lex access should verify Article
18 and add it.

## What the lecture deliberately leaves out

- **LASSO-regularised attention weights** (Richman and Wüthrich, 2023a). Named as the
  smoothing and selection route, and left to the reference, since `08` has already run five
  penalties on this book.
- **A demonstration of the identifiability failure.** The trap $z_j(\boldsymbol{X})X_j =
  X_{j'}$ is stated and the GLM initialisation is given as the practical guard, which is the
  course's own treatment. Staging a failure would need an adversarial initialisation that
  teaches the mechanics of something nobody should do.
- **SHAP.** It belongs beside LocalGLMnet in a comparison, and that comparison is `C2`'s.
- **The characteristic stability index** on the attention weights, which is `F2`'s.
