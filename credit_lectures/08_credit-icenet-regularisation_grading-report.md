# Grading report: 08_credit-icenet-regularisation

Graded 2 September 2026 against `01 Guidelines/_rubrics/writing-guidelines-global.md`
(criteria `M1` to `M11`, `J1` to `J29`; seven withdrawn ids return `not_applicable`). The
grader is informational and blocks nothing.

Text extracted from `credit_lectures/08_credit-icenet-regularisation.qmd` rather than from the
rendered HTML, following the R1 and lecture 7 reports: the skill's `extract_text.py` returns
Quarto's inlined CSS and JavaScript alongside the prose on these documents. Code cells, display
maths and the YAML header were stripped, and inline maths was left in place since it does not
affect any criterion. Prose total is 6,763 words across twenty-four graded sections, with the
copyright note and the reference list excluded from the `J25` counts and included in every
mechanical check, for the reason lecture 7's report records.

## Headline

| Document | Verdict | Mechanical fails | Judgement fails | Notes |
|---|---|---|---|---|
| `08_credit-icenet-regularisation.qmd` | **pass with warnings** | 0 | 0 | `J25` connective density passes in eleven of twenty-four sections and warns in thirteen, with no prose section below the 2.0 fail threshold. `M10`, `J17`, `J24` and `J27` each had genuine breaches and all are fixed. |

The document closed at **2.71** combined connectives per 100 words overall, and at **2.96**
excluding the copyright note and the reference list, which carry no argument and therefore no
turns. That sits alongside lecture 7's 2.95 and inside the 2.5 to 3.3 band `_craft.md` records
for the reference corpus. The opening draft measured 1.70, so this took a deliberate connective
pass across four rounds.

One measurement caveat worth recording, because it changes how an earlier number should be read.
The first two passes ran a subordinator regex without a case-insensitive flag, so every
sentence-initial "Since", "Because", "Although" and "While" went uncounted. Corrected, the
document that appeared to sit at 2.50 was already at 2.71. Any future run of this check should
carry `(?i)` on both patterns, not the discursive one alone.

## Fixes applied before this report

Four criteria had genuine breaches. Each was fixed in the source and the document re-rendered,
so this report describes the graded state rather than a to-do list. All 19 computed output
blocks reproduced identically after the prose pass, so no edit touched a number.

### `M10` serial comma: eight lists corrected

Eight lists of three or more items took no comma before the final "and": the penalty catalogue
in the introduction ("ridge, LASSO, elastic net, group LASSO, and fused LASSO"), the
cross-lecture deviance reference ("lectures 2, 4, 5, 6, and 7"), the two correlated-group lists
("income, employment duration, and home ownership"), both age-boundary lists ("23, 26, 28, 29,
32, 34, 39, 42, and 46" and "20, 25, 30, 40, 50, and 60"), the control list ("income, country,
and the other controls"), the pseudo-input list ("country, age, employment duration, and home
ownership"), and the stack list in the copyright block ("PyTorch, statsmodels, and
scikit-learn"). Author lists inside the reference entries were left alone as bibliographic
formatting, consistent with lectures 6 and 7.

### `J17` false antithesis: four spans rewritten

Four `rather than` spans named a counterpart the reader would otherwise have believed, which the
23 August 2026 widening makes a `fail` under the permitted word.

| Was | Now |
|---|---|
| "the score equation has to be recovered rather than merely preserved" | "the score equation has to be recovered instead, because early stopping never solved it" |
| "they are controls here rather than the object of the exercise" | "they are controls here while the age boundaries are the object of the exercise" |
| "Read the boundary lists rather than the deviances." | "Read the boundary lists first, since the deviances move very little here." |
| "so they are stated rather than buried" | "so the text states each one and what it costs" |

A fifth instance was introduced during the connective pass ("it sets the level rather than any
slope") and removed in the same round. Two `rather than` spans survive and both are plain
comparatives that name no counterpart belief: "a sample of a few thousand curves rather than
20,000", which compares two magnitudes, and "the code is Python with PyTorch, statsmodels, and
scikit-learn rather than R" in the copyright block, which matches the wording lectures 6 and 7
already carry.

### `J24` abstract-pointer summary: eight pseudo-clefts rewritten

The `\b(is|are|was|were)\s+what\b` sweep returned nine hits, of which eight were the pseudo-cleft
the criterion catches and one was a genuine noun clause. The eight rewrites were "is what makes
the penalty mean the same thing" to "makes the penalty mean the same thing"; "which is what
makes the penalty non-smooth" to "so the penalty is non-smooth"; "which is what makes it a soft
constraint" to "so it constrains softly and a large enough gain in the predictive term can still
buy a violation"; "Averaging is what makes it readable and also what makes it dangerous:" split
into two sentences; "Averaging is what destroys the evidence" to "Averaging destroys the
evidence"; "the constituents are what get priced" to "the constituents get priced"; "which is
what regularisation does" to "so regularisation earns its place"; and "which is what the fourth
and fifth lecture handed the network" to "exactly as the fourth and fifth lecture handed it to
the network".

One hit remains and passes: "its subject is what happens when the fitting objective carries a
penalty alongside the loss" is a noun clause supplying the subject, and it announces no
significance for the sentence before it.

### `J27` copula: one substitute removed

"since they serve as controls" became "since they are controls here". The verb carried nothing
the copula could not. The span was introduced during the `J17` pass and caught on the following
sweep, which is an argument for re-running the mechanical checks after every editing round
rather than only at the end.

## `J25` connective density: **warn** (the one outstanding criterion)

The rubric grades a floor of 3.0 combined connectives per 100 words section by section, scores
`warn` between 2.0 and 3.0, and reserves `fail` for a rate below 2.0 accompanied by at least one
adjacent sentence pair whose genuine turn no connective marks. No prose section is below 2.0.

| Section | Words | Connectives | Before | After (per 100 words) | Verdict |
|---|---|---|---|---|---|
| Introduction | 369 | 10 | 1.91 | 2.71 | warn |
| Regularisation (overview) | 64 | 2 | 1.61 | 3.13 | pass |
| What a credit model is trying to shrink | 265 | 9 | 1.15 | 3.40 | pass |
| The penalty function | 143 | 6 | 1.53 | 4.20 | pass |
| Standardisation comes first | 218 | 5 | 2.28 | 2.29 | warn |
| A single fitter for every penalty | 136 | 3 | 2.21 | 2.21 | warn |
| Ridge regularisation | 142 | 6 | 0.87 | 4.23 | pass |
| LASSO regularisation | 237 | 8 | 1.76 | 3.38 | pass |
| Best-subset selection and elastic net | 137 | 5 | 3.65 | 3.65 | pass |
| The intercept exclusion is the balance property | 377 | 10 | 1.62 | 2.65 | warn |
| Grouped covariates and group LASSO | 319 | 9 | 1.58 | 2.82 | warn |
| Fused LASSO is automated coarse classing | 633 | 21 | 1.77 | 3.32 | pass |
| Positivity and monotonicity on the parameters | 164 | 5 | 1.91 | 3.05 | pass |
| ICEnet (overview) | 73 | 4 | 1.61 | 5.48 | pass |
| Why a credit model wants a monotone curve | 218 | 5 | 1.39 | 2.29 | warn |
| ICE and PDP | 272 | 7 | 1.56 | 2.57 | warn |
| The idea and the compound loss | 132 | 3 | 0.00 | 2.27 | warn |
| Smoothness penalty | 89 | 3 | 3.37 | 3.37 | pass |
| Choosing what to constrain on the Bondora book | 387 | 8 | 2.08 | 2.07 | warn |
| ICEnet on the Bondora PD book | 75 | 2 | 1.67 | 2.67 | warn |
| The PDP hides what the ICE curves show | 342 | 13 | 3.47 | 3.80 | pass |
| Fitting the ICEnet | 269 | 7 | 2.60 | 2.60 | warn |
| Imposing the balance property during the fit | 532 | 13 | 1.71 | 2.44 | warn |
| Takeaways and outlook | 548 | 19 | 0.94 | 3.47 | pass |
| Copyright and attribution | 282 | 0 | 0.00 | 0.00 | excluded |
| References | 340 | 0 | 0.00 | 0.00 | excluded |

The four sections left closest to the floor are the ones carrying the most mathematics. A
definition sequence has genuinely few logical turns to mark, and forcing connectives into it
produces signposting over an argument that is running on notation rather than on prose. Both
"Standardisation comes first" and "A single fitter for every penalty" were left at roughly 2.2
for that reason.

## Criteria returning `pass` with candidates examined

- **`M2` British spelling.** One hit, "nonconcave penalized likelihood", inside the title of Fan
  and Li (2001) in the reference list. Quoted material, so it stays as published.
- **`J22` unmeasurable adjective triad.** Six regex hits, all false positives. Every one is a
  series of numerals or proper nouns ("23, 26, 28, 29, 32, 34, 39, 42, and 46"; "Scognamiglio,
  Maggi and Wüthrich"), and the criterion is scoped to adjectives.
- **`J21` fragment paragraphs.** None. The document carries no standalone paragraph of eight
  words or fewer.
- **`M1`, `M3`, `M4`, `M7`, `M8`, `M11`, `J20`, `J26`, `J28`, `J29`.** No candidates at all. In
  particular `J29` is worth noting on a lecture that could easily have claimed significance for
  its own findings; the strongest claim made is "Fused LASSO is the result to carry furthest",
  which states a reason immediately afterwards.
- **`J16` centre-embedding, `J18` unpacking colons, `J3` conclusion first.** Read manually rather
  than by regex. The colons in this document introduce genuine lists, definitions, or a
  displayed equation, and none does a full stop's job.

## What this run tells us

The two failure modes here are the ones the credit series keeps producing, and they are opposite
in kind. Serial commas and pseudo-clefts are mechanical and cheap to fix once swept for.
Connective density is not, because it costs a genuine editing pass over every paragraph, and a
document opening at 1.70 needed four rounds to reach the band. Lecture 7 recorded the same
sequence and closed at almost the same place, so the honest conclusion is that the house voice's
documented under-connection reproduces on every first draft in this series and should be planned
for rather than discovered.

The `J27` finding carries the most transferable lesson. That breach did not exist in the first
draft; it was introduced while fixing a `J17` breach, and it was caught only because the
mechanical sweep was re-run after the editing round. An editing pass is itself a source of new
breaches, so the sweep belongs after every round rather than once at the start.
