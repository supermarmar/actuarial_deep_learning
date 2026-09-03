# The F track: citation register, overlap map and notation bridge

Working note for `credit_lectures/F1_credit-classing-and-characteristic-analysis.qmd` and
`F2_credit-selection-collinearity-and-points.qmd`. It records what lecture 6 already owns and
must not be redefined, which claims were verified by direct read, which were rejected during
verification, and which symbols the two lectures may and may not use.

Read this before writing any prose into `F1` or `F2`. Everything settled here is settled. The
section outlines live in `notes/plans/04-feature-engineering-lectures.md`.

## Why the track exists

Credit lecture 3 describes the classical scorecard's feature engineering in one paragraph
(`03_credit-deep-learning-overview.qmd:76-95`) and moves on: bin into coarse classes, replace
each class by its weight of evidence, admit the variable only if the binning is monotone,
populated and stable. That single paragraph stands for the activity that consumes most of a
real PD model's development effort, and Mario asked on 3 September 2026 for it to become its
own lecture.

The track is numbered outside the course sequence for the reason the S, R and C tracks are: no
course lecture answers it.

## Confidentiality, applied

The A-IRB material in the `guides` repo derives from a real engagement, so this note inherits
the bar `notes/irb-lecture-structure.md` sets: **structure, regulatory references and
transferable method travel, and no portfolio specific does.**

Omissions are recorded by category rather than by content, which is the same note's rule for
exactly this situation. Left behind entirely, and deliberately not itemised further: the
source portfolio's segmentation scheme with its segment volumes and observed default rates,
its acquisition and strategy-change history, its risk-grade construction scheme, its variable-clustering configuration, its data-quality screening
thresholds, and its bureau vendor's special-value code list. None of that is needed to teach
the mechanics.

Bondora and the anonymised credit card table carry every worked example. The special-value
material transfers as a rule about coded exceptions, illustrated on Bondora's own `-1` and
null sentinels rather than on any vendor's code list.

## What lecture 6 already owns

This was the decisive check before the track was numbered.
`credit_lectures/06_credit-covariate-engineering.qmd` is titled *Ensembling and Entity
Embedding*, and its second half covers considerably more than that title suggests.

**Do not redefine any of the following.** Cite lecture 6 backwards.

| Already owned | Where |
|---|---|
| The WoE formula, and why the log-odds scale matches the logit link | `06:536-575` |
| Bühlmann-credibilitised target encoding, and minimum bin size as its blunter cousin | `06:578-600` |
| Ordinal, one-hot and dummy coding; five encodings compared on a 328-level cell; leakage | `06:506-535`, `06:692-809` |
| Entity embedding, and whether proximity tracks risk | `06:810-1128` |
| Standardisation, the MinMaxScaler, and censoring or log-transforming a tail first | `06:1131-1159` |
| Binning as a mapping, why scorecards bin, and what binning costs | `06:1160-1185` |

Lecture 6 asks how to encode a level once you have one. On boundaries it says only that they
"are chosen by the modeller", and stops. The F track takes the questions it leaves open: how
the boundaries are actually chosen, which characteristics earn a place, how the choice is
defended, and what the rival tradition does instead.

## The R3 boundary, checked against the landed lecture

`R3_credit-sampling-and-representativeness` landed on this branch's parent before F1 was
written, so the boundary was read from the lecture rather than assumed.

- **R3 owns** the population stability index and its two failure modes (`R3:553-674`) and the
  joint-distribution classifier two-sample test (`R3:675-737`). F1 stops at the fitted feature
  set and cites R3 forward for stability.
- **R3 does not cover the characteristic stability index**, confirmed by grep. CSI weights each
  class's population shift by its points contribution, so it needs the points scale to exist
  first. It therefore belongs in **F2 section 5**, beside Factor and Offset, and not in F1.
- R3's "What a validator asks, and what this lecture does not show" section (`R3:900`) is the
  pattern for F1's closing callout.

## Verified by direct read, 3 September 2026

Every row was read from the primary file named, not from a subagent summary.

| Claim | Source read | Verdict |
|---|---|---|
| The `71+` class held 13 loans and zero defaults, drove its coefficient towards $-\infty$ by quasi-complete separation, and the two oldest bands were merged into `61+` | `credit_lectures/02_credit-edf-glm.qmd:815-829` | VERIFIED verbatim |
| Lecture 2 assigned explicit `missing` levels to `HomeOwnershipType` (1,604 loans) and `EmploymentDurationCurrentEmployer` (820) | same, `:815-819` | VERIFIED verbatim |
| Lecture 2's eight-covariate `FORMULA` is reused verbatim by lecture 4-5 | `02:846-848`, `04-05:411-415` | VERIFIED |
| Out of time, that GLM scores AUC 0.716 against the network's 0.715 | `04-05:653-656` | VERIFIED, and see the benchmark note below |
| WoE $= \ln(\mathrm{DistGood}/\mathrm{DistBad})$; intercept-implied default rate spanned 29.64 to 30.39 per cent across 7,007 model combinations against an observed 30 | `vault/wiki/methods/weight-of-evidence-encoding.md:36,40` | VERIFIED |
| MAPA and isotonic regression as the two monotonicity algorithms; U-shape handled by splitting at a spline-located turning point; algorithm choice changes the final grade count materially | `vault/wiki/methods/risk-factor-binning.md:29-39` | VERIFIED |
| Partition variables and the wrong-hypothesis problem; Harrell's stepwise critique; the white-noise simulation (100 candidates, 100 bads, ten or more noise variables in the median model); MIV > 0.02; the triple test | `vault/wiki/methods/scallan-2011-classic-scorecard-development.md:33-47` | VERIFIED |
| WoE encoding is not self-replicating, whereas dummy encoding is exactly so | `vault/wiki/methods/encoding-instability.md:28-30` | VERIFIED |
| Factor $=$ PDO$/\ln 2$; the Offset; equal intercept distribution; score-share importance shifting across three Factor and Offset configurations; Hoadley's quadratic program | `vault/wiki/methods/scorecard-scaling.md:31-51` | VERIFIED |
| The condition index with variance-proportion one-drop, and iterated correlation clustering at progressively looser thresholds, as the method | guides `a-irb_capital/04_feature_engineering/pd/04-variable-reduction.md:53-94,141-170` | VERIFIED as method; the build's own threshold values stay behind |
| The 1 per cent special-value materiality rule; MAR, MNAR and structural missingness; capping at the 1st and 99th percentiles; Tukey's ladder and the bulging rule | guides `.../pd/05-variable-transformation.md:22-195` | VERIFIED |
| Discretisation arose in the 1960s because hand calculation made addition more reliable than multiplication | `vault/wiki/methods/scorecard-scaling.md:27` | VERIFIED |

**The benchmark, stated precisely.** The 0.716 figure is lecture 4-5's own fit, on lecture
4-5's splits. F1 must not quote it. F1 refits the same eight-covariate formula in its own
chunk, on its own splits, so that the only difference between the classed fit and the benchmark
is the classing.

## Four claims rejected during verification

All four came from `guides/docs/raw/compass_artifact_wf-415a19b4-*.md`, which is a generated
research dump rather than a source, or from guides wiki files that are visibly ChatGPT
transcripts (they close with "Do you want me to expand it in that formal style?"). Mario framed
the guides as an indicator rather than a source of truth, and this is what that caution buys.

1. **"Monotonicity is required by EBA Article 174 and US fair-lending review."** Treated as
   false. This repository's own register pins Art. 174(c) to *representativeness*
   (`notes/sampling-lecture-structure.md:50-54`), and no regulation mandates a monotone WoE
   profile. F1 presents monotonicity as practitioner discipline and gives the out-of-time
   stability rationale from `risk-factor-binning.md` instead.
2. **Siddiqi's IV bands** (0.02, 0.10, 0.30, 0.50). The vault carries no Siddiqi article. F1
   states the bands as unattributed common practice and notes that they depend on the class
   count, which is the qualification that makes them usable.
3. **"VIF < 5, tightened to 4 in some IRB submissions."** Unsourced. F2 uses the condition
   index with variance-proportion one-drop, which was read directly and is the better
   diagnostic anyway, since it names which variables are collinear with which.
4. **Navas-Palencia (2020) optimal binning as a mixed-integer program**, and the
   **Haldane-Anscombe $+\tfrac12$** correction. Both are real; neither was verified here. F1
   presents the half-count adjustment as arithmetic, without the attribution.

## Notation bridge

Series notation wins. Nothing here is renamed.

**Spent, and not to be reused.** Lecture 1 owns the snapshot $\tau$, the origination month
$g_i$, the calendar identity $u$, the loan age $t$, the window flag $D^{(k)}_{i,t}$, the
availability $A_i$ and the default time $T_i$. S1 owns the exit kind, the discrete hazard $h$
and $m$, $d$, $S$. R3 owns $\mathcal{D}$ and its partitions, $s_f$, $N_p$, the spell key
$(i,j)$, the event type $\psi$, the resolution rate $r_\psi$ and the weight $w_i$. Lecture 6
owns the level label $a_k$, the interval $I_k$, the level mean $\overline{y}_k$, the credibility
weight $\alpha_k$ and the embedding $\boldsymbol{e}^{\rm EE}$.

**One clash already live in the series, which F1 must not deepen.** Lecture 6 writes the
Bühlmann shrinkage parameter as $\tau \ge 0$ (`06:590`), while lecture 1 fixed $\tau$ as the
snapshot date. F1 needs neither, so it uses $\tau$ for nothing at all and refers to lecture 6's
shrinkage parameter by name where it comes up.

**Free, and adopted by F1.** The class index $k$ within a characteristic, matching lecture 6's
$a_k$ and $I_k$; the class counts $n_k$, $n^G_k$ and $n^B_k$; the class default rate $p_k$; the
characteristic index $\ell$, since $j$ is spent as R3's spell number; ${\rm IV}$ and ${\rm MIV}$
spelled out rather than lettered.

**Free, and adopted by F2.** The condition index $\kappa$, the variance proportion $\pi_{\ell
h}$, and Factor and Offset written as words, following the vault article and every scorecard
document in practice.

**The sign convention, which is the one thing easy to get wrong.** Lecture 6 defines
$$\mathrm{WoE}_k = \log\frac{\overline{y}_k/(1-\overline{y}_k)}{\overline{y}/(1-\overline{y})}$$
i.e. risk-positive, and says openly that the industry's good-to-bad form carries the opposite
sign. F1 keeps lecture 6's convention throughout, states the flip once, and notes that
information value is unaffected, because both factors in its summand change sign together.

## Dependencies: nothing new

`requirements.txt` stays byte-for-byte the course file. Do not add `optbinning`, `monobinpy` or
`scorecardpy`.

Two algorithms are treated differently on purpose. **MAPA is hand-rolled** in numpy, because it
is a short adjacent-merge loop whose merge order is the whole teaching point and a library call
would hide it. **Isotonic regression uses the pinned library**, since
`sklearn.isotonic.IsotonicRegression` ships in the pinned `scikit-learn` 1.8.0 (verified by
import on 3 September 2026) and reimplementing pool-adjacent-violators teaches nothing that
MAPA has not already taught. WoE, IV, MIV and the condition index are hand-rolled for the same
reason MAPA is.

## Handover

F1 is written first and in full. F2 is outlined in the plan and written next; its sections 3
and 4 need `data/credit_card_dev.parquet` rather than Bondora, because 45 interpretable columns
give correlation clustering and a condition index almost nothing to bite on, and lecture 3 has
already set the precedent for that switch and justified it.

Two counts move when F1 lands. `index.html` says "the fourteen lectures" at line 6, and
`CLAUDE.md` still says "thirteen credit lectures" at lines 35 and 201, which was already stale
by one when R3 landed. Both become fifteen.
