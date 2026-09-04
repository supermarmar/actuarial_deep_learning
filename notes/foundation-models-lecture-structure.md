# Credit lecture 12: overlap map, notation bridge, measured-facts contract and citation register

Working note for `credit_lectures/12_credit-foundation-models.qmd`, the companion to
`lectures/12_foundation-models.html`. It records what the earlier lectures already own and
must not be redefined, which figures must be measured before any prose is written, and which
citations have to survive verification.

Read this before editing the lecture. Everything settled here is settled.

Written 4 September 2026, before any modelling cell existed. The measured-facts section is
therefore a **contract** rather than a register: it names what has to be measured and the
acceptance criterion for each. Convert each entry to a recorded figure as the lecture is
built, and delete any entry the measurement kills.

## Why the lecture exists, and what it discharges

Course lecture 12 covers foundation models as a model class, the GPT series, tabular
foundation models (TabTransformer, FT-Transformer, TransTab, TabPFN, TabPFN v2, TabICL) and
the in-context learning credibility transformer (ICL-CT) of Padayachy, Richman, Scognamiglio
and Wüthrich (2025). It closes the course.

Two debts in the credit series point here.

- `10-11:1505ff` closes on the Credibility Transformer having competed without leading, with
  the credibility mechanism working mechanically and buying nothing. The obvious next
  question is whether a mechanism that retrieves **other borrowers' outcomes** at prediction
  time does better than one that shrinks towards a learned prior. That question is this
  lecture's.
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
deviance table: lecture 10-11 measured a seed standard deviation of 0.126 on this book, so
any difference smaller than that is noise and the lecture says so.

**A null result is an acceptable finding and was chosen deliberately.** Mario settled this
on 4 September 2026, before any fit was run, precisely so the lecture cannot be quietly
reframed around whatever the numbers turn out to be.

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

**Act one, foundation models as a model class.** Exposition, kept short, because the course
lecture carries it and there is no credit content in the GPT series. It covers the definition,
scale, the softmax model class, pre-training by autoregressive maximum likelihood, and the
adaptation ladder (fine-tuning, PEFT and LoRA, in-context learning, retrieval-augmented
generation). One credit-specific subsection maps that ladder onto credit practice: a bureau
score is already a pre-trained prior somebody else fitted on a population you cannot inspect;
RAG has an obvious home over a credit policy manual; and in-context learning over a retrieved
neighbour set is what acts three and four build.

**Act two, tabular foundation models, empirical on TabPFN v2.** Why tabular is different, then
the families, then the measurement. The exhibit is a **learning curve**: TabPFN v2 against
lecture 2's GLM and against the base Credibility Transformer of act three, all three trained on
nested subsamples of the learning sample at roughly n = 250, 500, 1,000, 2,000, 5,000 and
10,000, and every model scored on the series' own seed-1 test set so the deviances chain. The
neural arm is the CT rather than lecture 6's embedded network because act three imports the CT
class anyway, so the curve costs no second architecture. The question the curve answers is where
the foundation model's prior stops paying, which is a credit-specific number nobody has
published for this book. A calibration panel follows, because an IRB PD must be calibrated
rather than merely discriminating, and TabPFN carries no offset or exposure notion with which
to satisfy lecture 7's balance property.

**Act three, the ICL credibility transformer, empirical in torch.** Component zero is the base
CT, refit inside this lecture from lecture 10-11's `CredibilityTransformer` class. Then context
retrieval in CLS-token space by cosine similarity, the outcome-token decorator, causal
self-attention over `[context | target]` with the mask blocking target-target interaction, and
the frozen decoder. The proposition is restated and then **checked numerically**: the attention
row must satisfy $a_{i,i} + \sum_j a_{i,j} = 1$, and the lecture asks of the own-weight
$a_{i,i}$ exactly what lecture 10-11 asked of the implicit credibility weight, namely whether
it is a property of the borrower or of the fit.

**Act four, the Slovak cold start.** Train on EE, FI and ES with Slovakia remapped to an unseen
country level, then score the 296 Slovak loans. Null model, GLM, base CT and ICL-CT, with the
ICL-CT's context drawn from the training distribution alone. Every figure carries a bootstrap
interval, because a point deviance on 296 rows is not readable. The lecture also asks where the
retrieved context comes from: if retrieval pulls Estonian neighbours for a Slovak borrower, the
prediction is a statement about Estonians, and the borrower's own book contributed nothing.

**Act five, what this costs in governance.** The closing act, and the one no insurance lecture
can write. It measures rather than asserts, per Mario's decision of 4 September 2026.

## Boundaries

**`10-11` owns the Credibility Transformer.** Its architecture, the feature tokeniser, the CLS
token, the explicit Bernoulli gate and the implicit credibility weight are all built there. This
lecture imports the class and cites backwards. It does **not** re-derive attention, layer
normalisation or the time-distributed layer.

**`06` owns entity embeddings, one-hot encoding, weight of evidence and Bühlmann credibility.**
Cite forwards from there, never redefine.

**`09` owns reason codes and variable importance.** Lecture 9 built the per-decision
decomposition, calibrated it against noise, and established that one reason code is defensible
on this book while three are not. Act five measures the **stability of an ICL prediction in its
retrieved context**, which is a different quantity, and it points back to lecture 9 for the
tested measure rather than inventing a second one.

**`07` owns the balance property and auto-calibration.** Act two's calibration panel applies
that machinery and does not restate it.

**`R3` owns representativeness and sample design.** Its verification record already established
that representativeness anchors on **CRR Article 174(c)** rather than 179, and that Article
180(2)(e) carries no economic-cycle requirement. Act five cites `R3` and must not re-import the
179 anchoring that `R3` rejected.

**`D1` owns the target and the exposure convention.** `default_12m` is Bondora's own flag within
365 days, every loan in the fixed-horizon table carries the same twelve-month window by
construction, and the declaration lag runs to a median 79 days. Act three's decorator problem
below turns on that, so it cites `D1` rather than re-deriving it.

**`R2` owns IRB capital.** Act five may name the regulatory PD's documentation duty; it does not
re-run the five-step production sequence.

## The exposure problem, and how the decorator resolves it

This is the lecture's sharpest transfer finding and it is worth stating before any code.

The insurance decorator injects the observed response into a context instance's CLS token in a
credibility-weighted way:

$$\boldsymbol{c}^{\rm decor}(\boldsymbol{x}_j) = \widehat{\boldsymbol{c}}^{\,\rm cred}(\boldsymbol{x}_j) + \frac{v_j}{v_j + \kappa}\, \boldsymbol{z}^{\rm FNN1}(Y_j),$$

where $v_j$ is exposure in policy-years. The weight $v/(v+\kappa)$ is what makes this a
credibility construction: a policy observed for a long time contributes its outcome nearly in
full, and a policy observed briefly contributes a shrunk version.

**Bondora's fixed-horizon table has no exposure.** Every loan carries the same twelve-month
outcome window by construction, which `D1` owns. Setting $v \equiv 1$ therefore collapses the
weight to the constant $1/(1+\kappa)$, so $\kappa$ stops being a credibility coefficient and
becomes a plain shrinkage hyper-parameter applied identically to every context instance.

**Resolution.** Take $v \equiv 1$ as the primary specification and say plainly what it costs:
the decorator's credibility weight has no borrower-level content on this table, and the lecture
should not pretend otherwise. Name two alternatives without running them as the primary, and
say why each is a different lecture's problem:

- Observed duration from `bondora_survival.parquet`, which is the honest exposure analogue and
  belongs to the `S` track's estimand rather than this one's.
- `Amount` as an EAD-style weight, which measures financial rather than statistical exposure and
  would make the decorator a loss-weighted construction rather than a credibility one.

Do **not** manufacture an exposure column to make the formula look transferable.

## Notation bridge

| Symbol | Course | Here |
|---|---|---|
| $\mathcal{C}$ | prompt demonstration set | the retrieved context batch |
| $\mathcal{D}$, $S$ | ICL context / support set | unchanged; `S` prefix in this repo means the survival track, so write "support set" in prose and never a bare $S$ |
| $v_j$ | exposure in policy-years | absent by construction; $v \equiv 1$, see above |
| $\kappa$ | credibility coefficient in the decorator | a shrinkage hyper-parameter, and the lecture says so |
| $\mu(\boldsymbol{x})$ | expected claim count per unit exposure | probability of default within twelve months |
| $a_{i,j}$ | causal attention weights | unchanged |
| $\alpha$ | Bernoulli gate probability in the base CT | unchanged from `10-11`; the drop-out rate stays $\alpha^{\rm drop}$ and lecture 6's credibility weight stays $\alpha_k$ |
| $q$ | covariate count | unchanged, per `10-11`'s resolution |
| $b$ | channels | unchanged, per `10-11`'s resolution |
| $K$ | retrieved neighbours per target, **and** class count in the softmax | neighbours only; write the class count as $K^{\rm cls}$ if it is ever needed, which for a Bernoulli response it is not |
| $c$, $m$ | context batch size, target batch size | unchanged |
| $n$ | sample size | unchanged; act two's learning curve indexes on it |

Two resolutions worth stating. First, $S$ collides with this repo's own survival-track prefix,
so the support set is named in words. Second, $\kappa$ keeps the course's letter and loses the
course's meaning, which is exactly the finding above, so the lecture flags the demotion at first
use rather than letting the symbol carry an implication the data cannot support.

## Measured-facts contract

Nothing below is a number yet. Each entry names what must be measured and what would make the
claim reportable. Convert to recorded figures as the lecture is built, and delete any entry the
measurement kills.

### Act two, TabPFN v2

1. **The learning curve.** Out-of-sample deviance and AUC for TabPFN v2, lecture 2's GLM and
   the base CT at each n, all on the seed-1 test set. Reportable claim: the n
   at which TabPFN stops leading, with a repeat over at least three subsample draws so the
   crossover is not one draw's accident.
2. **Whether TabPFN leads at all on this book.** The course's claim is that these architectures
   are strong on small problems and may have deficiencies on unbalanced data. Bondora's learning
   sample runs at roughly a 29 per cent default rate, which is not the low-default case, so the
   honest expectation is a modest edge at small n. Report what happens, including no edge.
3. **Calibration.** Mean predicted probability against observed rate on the test set, and the
   balance property in lecture 7's sense. Reportable claim: whether TabPFN's output satisfies it
   without recalibration, and by how much it misses if it does not.
4. **Cost.** Wall-clock seconds to fit and score at each n, because the practical argument for a
   foundation model is partly that there is no fitting to do. A 2,000-row fit and 4,000-row score
   took 23.3 seconds on MPS in the smoke test of 4 September 2026.

### Act three, the ICL-CT

5. **The base CT, refit here.** In-sample and out-of-sample deviance and AUC. **Do not carry
   107.342 across from `10-11`.** The seed dispersion on this book is 0.126, so a copied figure
   will not match and the lecture would be quoting a number it did not measure.
6. **The attention row sums to one.** Check $a_{i,i} + \sum_{j} a_{i,j} = 1$ numerically and
   report the maximum absolute departure. This is the proposition's own arithmetic and it is the
   check to run before reading any weight.
7. **The own-weight $a_{i,i}$: borrower or fit?** Mean and spread across borrowers within one
   fit, against the spread of that mean across seeds. `10-11` found the implicit credibility
   weight's between-fit dispersion to be 9.4 times the within-fit spread. Reportable claim
   either way, and a repeat of that pathology one architecture up would be the stronger result.
8. **The deviance against the series**, with a seed spread rather than a single fit, read
   against 0.126.

### Act four, the Slovak cold start

9. **Four out-of-sample deviances on the 296 Slovak loans**, each with a bootstrap interval:
   null model, GLM, base CT, ICL-CT. Reportable claim: whether any gap exceeds its interval.
10. **Where the context comes from.** The country composition of the retrieved neighbours for
    Slovak targets. Reportable claim: the share of retrieved context drawn from each of EE, FI
    and ES, and what that means for a prediction described as using the borrower's own segment.
11. **TabPFN's version of the same experiment**, giving the Slovak rows to TabPFN as context
    directly, which is the true in-context move and has no training step at all.

### Act five, governance

12. **Reason-code stability under context re-draw.** Re-draw the retrieved context and measure
    how far a borrower's fitted probability moves. Reportable claim: the distribution of that
    movement on the log-odds scale, set against lecture 9's finding that the leading contribution
    exceeds the second by 1.043 there. If the movement is of that order, no reason code survives
    a context re-draw, and act five can say so as a measurement.

## Citation register

Every entry must be verified against primary text before it enters the lecture. Nothing here is
verified yet.

**Carried from the course lecture and to be checked against the arXiv or journal record:**
Vaswani et al. (2017); Brown et al. (2020); Kaplan et al. (2020); Hoffmann et al. (2022);
Devlin et al. (2019); Su et al. (2021); Radford et al. (2018, 2019); Ouyang et al. (2022);
OpenAI (2023); Huang et al. (2020) for TabTransformer; Gorishniy, Rubachev, Khrulkov and
Babenko (2021) for the FT-Transformer; Wang and Sun (2022) for TransTab; Müller et al. (2021)
and Hollmann et al. (2022) for the prior-data fitted network; Hollmann et al. (2025), *Nature*
637(8045) 319-326, for TabPFN v2; Qu, Holzmüller, Varoquaux and Le Morvan (2025) for TabICL;
Helli et al. (2024) for drift-resilient TabPFN; Feuer et al. (2024) for TuneTables; Bühlmann
(1967); Richman, Scognamiglio and Wüthrich (2025) for the Credibility Transformer; Padayachy,
Richman, Scognamiglio and Wüthrich (2025), arXiv 2509.08122, for the ICL-CT.

**Already corrected in this series, and the correction must not be lost.** The course
attributes feature tokenisation to TabM; it belongs to the FT-Transformer of Gorishniy,
Rubachev, Khrulkov and Babenko (2021). `notes/transformer-lecture-structure.md` records the
verification, so cite that correction rather than repeating the course's attribution.

**Regulatory, for act five, each to be verified against primary text:**

- **UK GDPR Articles 22A to 22D**, substituted for the former Article 22 by the Data (Use and
  Access) Act 2025 and in force in that form since 5 February 2026. The `09` note records the
  verification and warns that much of the secondary literature still quotes the superseded
  wording. Reuse that verification; do not re-source it from secondary material.
- **CRR Article 174(c)** as the representativeness anchor, per `R3`. Article 179 is **not** the
  anchor and Article 180(2)(e) carries **no** economic-cycle requirement, both of which `R3`
  established against primary text.
- Any documentation duty cited for a model whose training data cannot be shown must be quoted
  from primary text or dropped. A synthetic-prior model is a genuinely awkward case and the
  temptation to overstate the regulatory position is the risk to guard against.

**Deliberately absent.** No competitor citation, per `~/.claude/rules/no-competitor-citations.md`.
No vendor claim about a tabular foundation model's production readiness.

## Render cost

Budget: **up to roughly thirty minutes** on this machine, settled 4 September 2026.

The plan that fits it: act two's learning curve at six values of n over three subsample draws,
each TabPFN call costing seconds rather than minutes; act three's base CT plus the ICL-CT over
five seeds; act four's cold-start refits on the three-country training set; and act five reusing
act three's fitted ICL-CT rather than refitting.

Record the reuses here as they are made, the way `10-11` does, so a later tidy-up does not
silently turn one fit into three. Tune the seed counts to the budget rather than the budget to
the seed counts, and say in the lecture how many seeds each figure rests on.

## Environment note

`tabpfn` 8.5.0 was installed into `.venv` on 4 September 2026 under the render-only precedent
that CLAUDE.md already records for `pyyaml`, `nbformat` and `nbclient`. It adds nothing to
`requirements.txt` and it upgraded none of the course pins: `torch` 2.11.0, `polars` 1.40.1,
`scikit-learn` 1.8.0 and `statsmodels` 0.14.6 all survive the install. It pulls `lightgbm`,
`mlx` and `huggingface-hub` as dependencies of its own.

Two traps, both found on 4 September 2026 and both costly to rediscover.

- **The default weights are gated.** `tabpfn` 8.5.0 resolves to the `tabpfn_3` checkpoint,
  which is a gated HuggingFace repository and fails with `TabPFNHuggingFaceGatedRepoError`
  unless the user has accepted its terms and authenticated. Pass
  `model_path="tabpfn-v2-classifier.ckpt"` to select the **v2** checkpoint, which is ungated,
  downloads without credentials, and is the version the course actually cites (Hollmann et al.
  2025).
- **Do not pin `tabpfn` 2.x.** Version 2.2.1 carries the ungated weights directly, and
  installing it downgrades `scikit-learn` to 1.6.1. Restoring the 1.8.0 pin then breaks
  `tabpfn` outright with an `ImportError` on `_is_pandas_df`. The 8.5.0-with-v2-checkpoint route
  is what keeps both the course pins and the cited model version.

TabPFN also refuses to run on CPU above 1,000 samples unless `ignore_pretraining_limits=True`
is set. Use `device="mps"` on this machine, per CLAUDE.md's Apple silicon note.

## Deliverables

1. `credit_lectures/12_credit-foundation-models.qmd`.
2. Rendered HTML via `bash scripts/render_lecture.sh`, never bare `quarto render`.
3. PDF via `bash scripts/html_to_pdf.sh`, with a page of mathematics opened and eyeballed,
   because a slow MathJax CDN yields raw TeX in a PDF that still exits zero.
4. This note, converted from contract to register.
5. An `index.html` entry, and the lecture count moved from eighteen to nineteen there and in
   CLAUDE.md's directory table, with a results summary in the table entry in the house pattern.
