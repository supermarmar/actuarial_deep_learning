# Research verdict: estimating a point-in-time PD under IFRS 9

Written 2 September 2026 for `credit_lectures/R1_credit-ifrs9-pit-pd.qmd`, executing task 1
of `notes/plans/01-ifrs9-pit-pd-lecture.md`. The plan answers review comment 1 of round 3 on
credit lecture 1, which asked for conditional and unconditional PiT PDs, for FiT, and for the
Botha methods with pros and cons on each.

Every source here was already on disk, in `~/Documents/Repos/vault/wiki/` or in
`~/Documents/Repos/guides/`, and every claim below traces to a direct read of the file named.
Where a claim reaches me through a vault article rather than through the paper itself, the
paragraph says so, because a wiki summary is a secondary source and the lecture should not
pretend otherwise.

## The two terminology questions, both now answered

### Conditional against unconditional names the survival axis

Decision 2 of the plan is corroborated by Mario's own notation rather than by preference. The
guides' credit risk notation table, at
`docs/wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/03_notation.md`,
carries two adjacent rows. Verbatim:

> **$k$-month unconditional PiT marginal PD**
> $\text{PD}_{i,t}^\text{uPiT}(k,x_{i},x_{i,t})=P(D^*_{i,t}(k,p) = 1\mid X_i=x_i,X_{i,t}=x_{i,t})$
> $k$-month unconditional probability of default for a loan from a particular cohort group,
> regardless of prior default or prepayment

> **$k$-month conditional PiT marginal PD**
> $\text{PD}_{i,t}^\text{PiT}(k,x_{i},x_{i,t})=P(D^*_{i,t}(k,p) = 1 \mid D_{i,t}(p)=0,X_i=x_i,X_{i,t}=x_{i,t})$
> $k$-month conditional probability of default for a non-defaulted loan from a particular
> cohort group

The conditioning event is $D_{i,t}(p) = 0$, i.e. the loan sits in the performing risk set. The
axis is therefore survival, and the phrase "regardless of prior default or prepayment" on the
unconditional row states the same thing from the other side. Neither row conditions on the
macroeconomy, and both carry the PiT label, which is the decisive point: PiT against TTC is a
separate axis in this notation, exactly as the plan assumed.

Nothing in the sources uses the macro reading. Botha and Verster's tutorial reaches the same
place through survival language rather than through the words "conditional" and
"unconditional": its discrete-time hazard is a marginal PD "conditioned on survival to that
point and on the prevailing macroeconomic and loan-level inputs", which puts survival and
macro conditioning in one sentence as two different conditions. Recorded via
`vault/wiki/methods/ifrs9-lifetime-pd-term-structure.md`, sourced there to the tutorial's
section 3, "Estimating lifetime PDs using survival analysis in discrete time".

**No source uses the macro reading of conditional, so the lecture needs no defensive
paragraph.** It can state the survival reading and cite `03_notation.md` for it.

### FiT is Mario's own term, and the standard's word is "forward-looking"

IFRS 9 itself never says "forward in time". What it requires, at paragraph 5.5.17, is that an
entity measure expected credit losses in a way that reflects

> (a) an unbiased and probability-weighted amount that is determined by evaluating a range of
> possible outcomes; (b) the time value of money; and (c) reasonable and supportable
> information that is available without undue cost or effort at the reporting date about past
> events, current conditions and forecasts of future economic conditions.

Read from `vault/markdown/ifrs/ifrs9_standard.md`, lines 195 to 199. That file is a
**synthesised** markdown of the standard rather than the IASB PDF, which its own registration
at `wiki/_meta/sources/iasb-ifrs9-standard.md` states plainly, so the paragraph number is the
citation anchor and the wording was cross-checked against the standard as commonly quoted.
Two neighbouring paragraphs matter as much:

- **5.5.18** requires at least the possibility that a credit loss occurs and the possibility
  that none does, "even if the possibility of a credit loss occurring is very low". This is
  the floor under scenario weighting, and it is a much weaker requirement than the three
  scenarios the industry actually runs.
- **B5.5.52** requires that estimates of changes in expected credit losses "reflect, and be
  directionally consistent with, changes in related observable data from period to period
  (such as changes in unemployment rates, property prices, commodity prices, payment status
  ...)". The standard therefore names unemployment first, which is a gift for this lecture,
  whose Bondora demonstration conditions on the harmonised unemployment rate.

"Forward-looking information", abbreviated FLI, is the phrase the standard and the EBA
guidelines use, and the guides FLI methodology file uses it too.

**"Forward in time" and "FiT" appear nowhere in the vault corpus and nowhere in the
literature I can reach.** A case-sensitive search over `vault/markdown/` and `vault/wiki/`
returns two hits and neither is the term: one is base64 noise inside a scanned textbook, the
other is ordinary prose in `wiki/methods/boe-credit-losses-cyclicality.md` about losses being
"pulled forward in time". The single definition of FiT as a PD label is Mario's own
`03_notation.md`. Decision 3 of the plan therefore stands as written: introduce the standard's
own wording first, then name FiT as this course's label, so a reader can find the material in
a bank's documentation under either name.

### The FiT definition needs a second half, and the plan's recommendation is adopted

`03_notation.md` defines FiT twice, and the two are different objects.

| Row | Formula | What FLI is |
|---|---|---|
| $k$-month conditional FiT PD | $\text{PD}_{i,t,t'}^\text{FiT}(k) = \text{PD}_{i,t}^\text{PiT}(k) \times \text{FLI}_{t'}$ | a multiplicative scalar on a probability |
| $k$-month systemically conditional PiT PD | $\text{PD}_{i}^\text{SysPiT}(k \mid \text{FLI}_{t'}) = N\!\left(\frac{N^{-1}(\text{PD}_{i}^\text{TTC}(k)) + \text{FLI}_{t'}\sqrt{\rho}}{\sqrt{1-\rho}}\right)$ | a standard normal factor realisation inside a probit |

A multiplier on a probability and a factor realisation inside a probit cannot both be the same
$\text{FLI}_{t'}$. Plan 1 and plan 2 both flag this and both recommend the probit reading, on
the grounds that it is the form which reproduces the IRB capital formula and the form credit
lecture 1's hybrid callout already carries.

**Settled by Mario on 2 September 2026, and it went this way.** Decision 3 of plan 1 now reads "Its **form** is the probit one, i.e. the factor enters through the Vasicek transform, and the multiplicative $\mathrm{PD}^{\rm PiT} \times \mathrm{FLI}$ version is named as the practitioner shortcut with its bias stated", which is what this note recommended independently. The lecture takes the probit form as the
definition and names the multiplicative version as the practitioner shortcut it is, with its
bias stated, which is the treatment lecture 1 already gives the Jensen trap. Two reasons
beyond the plan's: the multiplicative form is not closed on $[0,1]$, so a downside scenario
factor of 1.4 applied to a PiT PD of 80 per cent returns 112 per cent; and the guides' own FLI
methodology file derives the factor as
$\text{Factor } X = \text{FLI-adjusted PD}_X / \text{Base PD}$, which makes it an output of a
scenario regression rather than an input, so reading it as a primitive inverts the
construction. `R2_credit-irb-capital.qmd` must answer the same way, per plan 2's task 2 step 5.

## The methods, each with a verdict

Nine methods the plan names, plus two the guides' PD methodology file carries that belong in
the comparison because they are actuarial techniques answering a credit question.

### Discrete-time hazard model

One row per loan-month at risk, a binary response flagging the month of default, and a
logistic regression on it whose period indicators form the baseline hazard. Botha and Verster
(2025) specify it as
$h(t \mid \boldsymbol{E}_i, \boldsymbol{x}_i, \boldsymbol{x}_i(t), \boldsymbol{x}(t))$ with
four covariate blocks, the last being portfolio-level time-varying inputs, which is where the
macroeconomy enters (tutorial section 3). What it buys is every horizon from one fit, native
macro conditioning through $\boldsymbol{x}(t)$, and no new estimation machinery, since any
binomial likelihood fits it. What it costs is the expansion: 179,235 Bondora loans become
2,672,193 rows at a sixty-month cap, and the exposure convention inside that expansion is a
real modelling choice rather than a formatting one, worth 3.5 per cent of exposure on this
book by lecture S2's measurement. Competing risks are handled by data construction rather than
by the estimator, so treating settlement as censoring is a decision the layout hides.
**Verdict: the default choice, and the spine of this lecture.** It is the only method on this
list that gives a loan-level term structure and native macro conditioning together without a
second model.

### Non-stationary semi-Markov chain

Loans occupy delinquency states, a transition matrix governs migration, and the term structure
comes from powering the matrix, $v_t = v_1 T^t$. Botha, Verster and Breedt (2025) treat the
plain first-order chain as a baseline and reject both of its assumptions empirically:
stationarity of the matrix and homogeneity of the population (multistate section 2). The
guides' PD methodology file adds a third rejection from the same family of evidence, namely
that observed sojourn times are heavily right-skewed and visibly not exponential, which the
Markov property requires. What the chain buys is a PD at any horizon, easy implementation, and
a forecast of the whole future portfolio profile rather than of default alone, which is what a
budgeting or stress-testing exercise wants. What it costs is fit: the guides file records that
time-specific matrices are usually needed to reach acceptable multi-period fit, making the
model complex for little gain over direct estimation, and that small monthly migration errors
compound into large multi-year PD errors. **Verdict: keep it as the baseline every richer
method is measured against, and do not ship it.** Its value in the lecture is pedagogical,
since the state space is where competing risks become visible.

### Beta regression on transition cells

Each cell of the transition matrix becomes a time series of percentages over calendar months,
and each series is modelled by a beta regression with variable dispersion, with both mean and
precision parameterised. This is the repair for non-stationarity: the matrix becomes $T(t')$
and macro variables enter each cell's regression directly. What it buys is exactly that macro
conditioning, at portfolio level, in a distribution that respects the $[0,1]$ support of a
proportion. What it costs is that the unit of observation is a cell, so it cannot see a loan:
population heterogeneity remains unaddressed, and one model per transition type of interest
means a proliferation of fits with no joint constraint keeping a row of the matrix summing to
one. **Verdict: a genuine improvement on the plain chain, and a halfway house.** Botha, Verster
and Breedt place it second of three on their mortgage data (multistate section 3).

### Multinomial logistic regression on transitions

The same transition problem at loan level: $p_{ml}(t', x_i) = P(Y_t = l \mid Y_{t-1} = m, x_i)$
fitted jointly across destination states with a baseline category, so the probabilities in a
row sum to one by construction. Time-fixed, time-varying and portfolio-level covariates all
enter. What it buys is heterogeneity and joint estimation together, and Botha, Verster and
Breedt attribute its win to precisely that joint modelling rather than to cell-by-cell fits
(multistate section 3). What it costs is parameters, $(J-1)(p+1)$ of them per starting state,
and a design that needs the delinquency state observed monthly for every account, which is
more data than a hazard model on time to default needs. **Verdict: the best of the three
multistate techniques on the published evidence, and the right choice where the bank wants
stage migration rather than default alone.** It answers IFRS 9 staging and lifetime PD from
one model, which is an operational argument the hazard model cannot make.

### Cox proportional hazards with time-varying macro covariates

Bellotti and Crook (2009) is the methodological ancestor: a nonparametric baseline hazard
multiplied by the exponential of a covariate index, with each macro series entering at the
value it took in the month of default or censoring. What it buys is the case for macro
conditioning itself, made empirically. On over 100,000 UK credit card accounts opened between
1997 and 2005, adding seven macro series lifted the log-likelihood ratio statistic by 1,779 on
25 degrees of freedom, and the augmented model beat both logistic regression and a
macro-free Cox model on an independent 2002 to 2005 test set. The interest rate dominated,
with a standardised marginal effect of 0.261, nearly three times that of earnings. Those
figures reach me through `vault/wiki/methods/survival-analysis-macroeconomic-pd.md` rather
than through the paper, which the lecture should say when it quotes them. What it costs is the
proportional hazards assumption, a baseline left unparameterised and therefore awkward to
extrapolate beyond the observed follow-up, and a continuous-time apparatus imposed on data
that arrive monthly. **Verdict: cite it for the argument, fit the discrete-time version.** In
monthly data the discrete hazard is the same model with a tractable likelihood and an
interpretable baseline, which is why the Botha tutorial builds on the discrete form.

### Andersen-Gill recurrent-event Cox

A common baseline hazard across all default spells, with time measured on a single calendar
scale, so a cured loan simply continues to contribute at-risk time. Botha, Verster and
Scheepers (2025) set it out alongside PWP in section 2, "Different types of recurrent event
survival models". What it buys is redefaults, which a time-to-first-default model discards
along with all loan history after the first event, and both §36.74 of the Basel framework and
Article 178(5) of the Capital Requirements Regulation acknowledge that default is a cyclic
state rather than an absorbing one. What it costs is the assumption doing the work: one
baseline for every spell asserts that the risk of a second default behaves like the risk of a
first, which retail experience contradicts. **Verdict: dominated by PWP, and the weakest of
the three specifications the paper compares.** It underperforms on Harrell's c-statistic and
on time-dependent ROC analysis against both time-to-first-default and PWP.

### Prentice-Williams-Peterson gap-time Cox

Stratifies by spell number, so each spell gets its own baseline hazard and may get its own
covariate effects, and resets the time index to zero at the start of every new spell (same
paper, section 2). What it buys is the right shape for retail: a redefault is a different
event from a first default, and the gap-time clock matches how a cured account is actually
managed. What it costs is data, since spell-stratified baselines need enough second and third
spells to estimate, and a portfolio-level term structure now requires aggregating spell-level
marginals back to the loan. **Verdict: the theoretically right recurrent-event choice, and
worth the complexity only where redefaults are material.** The paper's own comparison is the
honest note to end on: time-to-first-default and PWP produce broadly similar discriminatory
performance, so the recurrent-event machinery buys correctness of the estimand rather than
discrimination.

### Vasicek Z-factor scaling of a TTC grade PD

Take a TTC grade PD, push it through
$\Phi\left((\Phi^{-1}(p) - \sqrt{\rho} Z)/\sqrt{1-\rho}\right)$ with a systematic factor $Z$
and a loading $\rho$, and read the output as the PiT PD for that state of the cycle. Belkin,
Suchower and Forest (1998) established that $Z$ need not stay latent: it is recoverable year
by year from observed transition matrices by inverting the conditional migration formula, and
the recovered series turns negative in downturns, which is the evidence that it is measuring
the cycle. Djurovic (2025) improves the recovery by fitting one $Z$ to the whole matrix in a
weighted least-squares problem rather than grade by grade, which removes the inconsistency of
different grades implying different values of $Z$. What it buys is a PiT PD from a TTC model
without refitting anything, closed form, and the exact averaging property that
$\mathbb{E}_Z[\text{PD}^{\text{PiT}}] = \text{PD}^{\text{TTC}}$, which no other method on this
list gives for free. What it costs is that $Z$ is not a forecast: it is recovered from realised
transitions, so projecting a PiT PD forward needs a separate model linking $Z$ to
macroeconomic variables, and $\rho$ is either prescribed by regulation or estimated with wide
uncertainty. **Verdict: the right tool for converting an existing IRB grade PD, and the wrong
tool for a term structure.** It scales a level and says nothing about how risk runs with loan
age, which is the whole content of an IFRS 9 term structure.

### Age-period-cohort decomposition

Breeden (2016) decomposes a loan-level outcome into three separable offsets, the loan's age on
book, its origination vintage, and the macroeconomic environment at the observation date, and
embeds all three in a GLM scorecard as extra predictors. The identification problem is the one
credit lecture 1 complains about, since age, vintage and calendar time are structurally
correlated in any live book, and the answer is **augmented macroeconomic history**: anchor the
environment sensitivity to an external series spanning several cycles, then back-project onto
the portfolio's vintages. What it buys is exactly the collinearity break lecture 1 says more
modelling cannot achieve, plus a named, traceable macro coefficient that a validator can
challenge, plus reported stability of rank-ordering out of time on a US auto book where a
plain scorecard decays. What it costs is the external series and the assumption that its
sensitivity transfers to this portfolio, which is an untestable extrapolation dressed as a
data step. **Verdict: the cleanest answer to lecture 1's collinearity complaint, and the one
method here whose key step cannot be validated on internal data alone.** Claims reach me
through `vault/wiki/methods/breeden-2016-lifecycle-environment-loan-level-forecasts.md`.

### Empirical term structures, added from the guides

Cumulative and marginal default curves read straight off a defaults table, with
$p^m_{k,t} = d_{k,t}/n_{k,0}$ per observation month and horizon, then averaged over the most
recent $R$ observation months. $R$ is the dial: a short reference period gives a PiT estimate
with unwanted volatility, and a period spanning a cycle gives a TTC one. What it buys is
intuitiveness, no forecasting step, and native treatment of attrition and redefaults, so a
lifetime PD may exceed 100 per cent for a high-risk account, which the method intends rather
than tolerates. What it costs is segmentation, since the whole model is the segment definition and
granular segments run out of defaults. **Verdict: worth naming in the lecture because it makes
the PiT-to-TTC axis a single tunable parameter, and because it is what many production stacks
actually run.** Source: the guides' `ifrs9_impairments/05_modelling/pd/01-model_methodology.md`,
which credits Schutte et al. (2020) and Yang (2017).

### Run-off triangles and the chain ladder, added from the guides

The reserving triangle, applied to defaults and closures instead of claims. What it buys is
ease of design and automation, and PiT estimates that predict the near future well. What it
costs is that account-level term structures then need crude linear scaling of a segment curve,
and that recent structural change in the portfolio distorts the triangle. **Verdict: include
it in the comparison table for one reason, that an actuarial audience already owns the
technique.** England and Verrall (2002) is the chain ladder reference the guides file gives.

Explicitly out of scope, though the same guides file carries them: ARIMA on the default rate
series, Lorenz curve calibration, gradient-boosted direct PD prediction, and market-implied
PDs from credit spreads. None of the four is a Botha method and none answers the review
comment.

## The empirical ordering, and how to attribute it

Two performance claims the lecture wants, with what can honestly be said about each.

**Multistate.** Each successive model outperforms the previous, with multinomial logistic
regression best, on residential mortgage data, attributed to joint rather than per-cell
modelling of transition probabilities. Anchor: Botha, Verster and Breedt (2025), section 3,
"Three models for deriving lifetime PD-estimates". The registration's section map has only
three sections, so section 3 is where both the models and their comparison sit.

**Recurrent events.** Time-to-first-default and PWP produce broadly similar discriminatory
performance while Andersen-Gill underperforms, measured by Harrell's c-statistic and
time-dependent ROC analysis. Anchor: Botha, Verster and Scheepers (2025), naming the two
diagnostics rather than a section number, for the reason in the next block.

### Flag: the vault's footnote labels drift from its own registration

Worth fixing in the vault, and worth not propagating here.
`wiki/methods/ifrs9-lifetime-pd-term-structure.md` cites the recurrent-event paper's `_s3` as
"Recurrent event Cox model subtypes (AG and PWP)" and `_s4` as "Empirical results and
portfolio-level term structure derivation". The registration at
`wiki/_meta/sources/botha-2025-recurrent-event-cox.md` maps section 2 to "Different types of
recurrent event survival models", section 3 to "Time-dependent ROC-analysis for survival
models" and section 4 to "Input space and data", and stops there.

The plan says to take section anchors from the registrations, so this note does: AG and PWP
are **section 2**, and the empirical comparison has no section anchor the registration
supports. Consequently the lecture attributes the performance ordering to the paper and to the
named diagnostics, and cites no section number for it. The tutorial registration shows the
same drift in milder form, mapping section 3 to "Estimating lifetime PDs using survival
analysis in discrete time" against the article's "Discrete-time survival analysis for lifetime
PD estimation", which is the same section under a paraphrased title and harmless.

## The FLI design problem, and the three remedies

Two or three cycles of history against dozens of candidate macro indicators is the standing
condition of this work, so the design choices matter more than the estimator. Djurovic (2025)
identifies eight principles a well-specified FLI model should satisfy, including economic
plausibility, directional constraints, parsimony and calibration stability, and names three
enhancements over naive stepwise selection: **OLS model averaging** across plausible
specifications, **blockwise design** grouping predictors by economic theme, and **constrained
regression** enforcing sign restrictions from prior economic knowledge. Two further findings
from the same series belong in the lecture as validation warnings. The AR(1) coefficient in a
dynamic-regression FLI model is heavily downward-biased at the sample sizes IFRS 9 work
actually has, 10 to 30 observations, while the predictor coefficient stays largely unbiased.
And the Augmented Dickey-Fuller test loses power precipitously at those sample sizes, so at
$n = 20$ a non-rejection is weak evidence of non-stationarity. All via
`vault/wiki/methods/forward-looking-information-modelling.md`.

Downstream of the PD, two facts frame why any of this matters. The EBA's 2023 monitoring
report found an average baseline scenario weight of about 57 per cent, downside 27 and upside
17, across 37 EU institutions, with wide dispersion and limited evidence that severity and
probability were jointly calibrated. And post-model adjustments are meant to be temporary,
specific and quantified, with the PRA pressing on completeness and on component-level rather
than aggregate application. Via `wiki/methods/ifrs9-scenario-design-and-weighting.md` and
`wiki/methods/ifrs9-post-model-adjustments.md`. Neither belongs in the body of this lecture at
length, and one sentence each earns its place, because a reader who has just built a term
structure should know it gets weighted and overlaid before it becomes a provision.

## For vault ingest

Nothing new was downloaded for this lecture, so this list is short and consists of gaps the
vault could usefully close. None is needed for R1 to be written, and none should be ingested
from here: `kb-ingest` in the vault owns that, with its audit entry per file.

- **Schutte et al. (2020)**, on segmented empirical PD term structures. The guides cite it as
  "Schutte et al. 2020" and give no fuller reference, so the author list is unverified here. The guides' PD methodology file cites it and links
  <https://mpra.ub.uni-muenchen.de/76271/1/MPRA_paper_76271.pdf>. The vault has no
  registration for it, and it is the primary source for the empirical term structure method
  above.
- **Yang, B.H. (2017)**, cited by the same file for the cumulative and marginal PD definitions
  the empirical method uses. No vault registration.
- **Djurovic, A. (2025) FLI series.** Registered and used above, but the wiki article is the
  only route to it and the article is marked `reviewed: false`, `confidence: medium`. A
  fact-check pass would raise confidence in the three remedies this lecture cites.
- **The IASB PDF of IFRS 9.** The vault's copy is a synthesised markdown by its own admission.
  Every paragraph quoted above was cross-checked, and the gap is worth closing before any
  client-facing document quotes the standard from this repository.

## Notation contract

Task 2 of the plan. A fresh session would otherwise reinvent symbols that lecture 1 and the
survival track already own, and a clash is the most expensive mistake available here.

### Inherited from credit lecture 1

| Symbol | Meaning |
|---|---|
| $y_{i,t}$ | monthly default flag for loan $i$ in month $t$ on book |
| $D^{(k)}_i$ | worst-ever default flag over the $k$-month window from origination |
| $D^{(k)}_{i,t}$ | the same flag over the window opening at $t$ months on book |
| $g_i$ | origination month of loan $i$ |
| $A_i$ | age of the borrower at origination |
| $T_i$ | time in whole months from origination to default |
| ${\cal W}_k$ | the set of loans seasoned enough to carry a $k$-month outcome |
| ${\cal P}_u$ | the set of loans on book and performing at calendar month $u$ |
| $n_u$ | $\# {\cal P}_u$, the size of that performing set |
| $\mathrm{DR}^{(k)}_u$ | portfolio $k$-month default rate at calendar month $u$ |
| $\boldsymbol{X}_i$ | time-fixed covariates of loan $i$ |
| $\boldsymbol{Z}_u$ | macroeconomic state at calendar month $u$ |
| $u = g_i + t$ | the calendar-time identity linking the two clocks |
| $\lambda$ | the hybrid PD's logit-scale interpolation weight |
| $\rho$ | the loan's loading on the systematic factor |
| $\mathrm{PD}_k$ | the $k$-month PD, i.e. the cumulative PD to horizon $k$ |
| $d$ | Botha's delinquency threshold, lecture 1 section 2.1. **Spent** |
| $\mu_k$ | the regression function $\boldsymbol{X} \mapsto \mathbb{E}[D^{(k)} \mid \boldsymbol{X}]$ |

### Inherited from the survival track

| Symbol | Meaning | Owner |
|---|---|---|
| $q_{i,t}$ | the discrete default hazard of loan $i$ in month $t$ | S1, reused in S2 and S3 |
| ${}_k p_{i,t}$ | probability loan $i$, now $t$ months on book, survives a further $k$ | S1 |
| $l_t$ | life-table count still in force and performing at $t$ | lecture 1 |
| $d^{\rm def}_t$, $d^{\rm set}_t$ | the two decrements, default and settlement | lecture 1 |
| ${}_k p_t$, ${}_k q_t$ | the life-table survival and failure probabilities | lecture 1 |
| $f(t_{(k)})$ | Botha's marginal default probability for the $k$th ordered month | S1 |
| $\tilde T_i$, $\delta_i$ | observed duration and event indicator | S1 |
| $R_i$ | Botha's four-level exit variable | S1 |
| ${\cal R}$ | the set of at-risk loan-months | S3 |
| $m$ | the number of periods in Botha's specification. **Spent** | S1, S3 |

### The plan's four proposed symbols, all revised

The plan proposed $h_{i,t}$, $S_{i,t}$, $m^{(k)}_{i,t}$ and $\mathrm{PD}^{\rm cum}_k$. The grep
it specifies returns nothing for the first three, which is how the plan expected the check to
pass. However the check the plan intended is the stronger one, i.e. whether the **object**
already has a name, and on that reading three of the four are redundant and one is a clash of a
worse kind, a second name for something already named.

| Proposed | Verdict | Adopted instead |
|---|---|---|
| $h_{i,t}$, the discrete hazard | Reject. S1, S2 and S3 all write this $q_{i,t}$, and S2's four-vocabulary table maps it to the actuarial $q_{x+t}$ | $q_{i,t}(\boldsymbol{X}_i, \boldsymbol{Z}_u)$, i.e. the inherited symbol with the conditioning made explicit |
| $S_{i,t}$, survival to $t$ | Reject. S1 owns ${}_k p_{i,t}$, and $S$ additionally collides with the guides' $S_{99.9}$ | ${}_t p_{i,0}$, and ${}_k p_{i,t}$ for the general case |
| $m^{(k)}_{i,t}$, the marginal PD | Reject the letter. $m$ is spent as Botha's period count in S1 and S3 | $f_{i,t}$, which is S1's own $f(t_{(k)})$ in loan-subscripted form |
| $\mathrm{PD}^{\rm cum}_k$ | Reject as redundant. Lecture 1's $\mathrm{PD}_k$ and S1's $\mathrm{PD}_k = 1 - {}_k p_{i,0}$ already **are** the cumulative PD | $\mathrm{PD}_k$, unchanged |

So the lecture adds exactly one symbol, $f_{i,t} = {}_{t-1}p_{i,0} \cdot q_{i,t}$, and it is
inherited rather than invented: it is Botha's third identity, $f(t_{(k)}) = S(t_{(k-1)}) \cdot
h(t_{(k)})$, written with the subscripts this track uses. Everything else the lecture needs is
already defined somewhere in the series, which is the outcome the plan wanted and a better one
than four new symbols.

Two superscripts are new as labels rather than as symbols, both taken from `03_notation.md` so
the lecture and the guides agree: $\mathrm{PD}^{\rm uPiT}$ for the unconditional PiT PD and
$\mathrm{PD}^{\rm FiT}$ for the macro-conditioned one. $\mathrm{PD}^{\rm PiT}$,
$\mathrm{PD}^{\rm TTC}$ and $\mathrm{PD}^{\rm hyb}$ are already lecture 1's.

### Two mappings to state once in the lecture

The guides use $t'$ for calendar time where this series uses $u$, and $N(\cdot)$ where this
series uses $\Phi(\cdot)$. Both are cosmetic and both need stating once so a reader can move
between the two documents.

The systematic factor's **sign convention is opposite** in the two, and that is not cosmetic.
Lecture 1 writes $-\sqrt{\rho}\, Z_u$ with high $Z_u$ benign; `03_notation.md` writes
$+\sqrt{\rho}\, \mathrm{FLI}_{t'}$. The two agree under $\mathrm{FLI}_{t'} = -Z_u$, and the
lecture should say so as a displayed equation rather than in prose, because a reader checking
one formula against the other will otherwise conclude that one of them is wrong. Plan 2's task
2 step 4 owns the same statement for R2, and the two lectures must match.
