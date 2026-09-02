# Grading report: 02_credit-edf-glm

Graded 2 September 2026 against `01 Guidelines/_rubrics/writing-guidelines-global.md`
(criteria `M1` to `M11`, `J1` to `J29`; seven withdrawn ids return `not_applicable`). The
grader is informational and blocks nothing.

Text extracted from `credit_lectures/02_credit-edf-glm.qmd` rather than from the rendered
HTML, for the reason recorded in the R1 report: the skill's `extract_text.py` returns Quarto's
inlined CSS and JavaScript alongside the prose on these documents. Code cells, display maths,
table rows and `#| fig-cap` lines were stripped, and inline maths was replaced with a token.
Prose total is 3,823 words across sixteen graded sections, references and the copyright note
excluded.

## Headline

| Document | Verdict | Mechanical fails | Judgement fails | Notes |
|---|---|---|---|---|
| `02_credit-edf-glm.qmd` | **fail** | 0 | 1 | `J25` connective density fails in eleven of sixteen sections. Everything else passes after the fixes below, and the section holding the new prose clears the `J25` floor. |

## Detailed findings

### `J25` connective density: **fail**

The rubric grades a floor of 3.0 combined connectives per 100 words, section by section. The
document runs at **1.63** overall, below the 2.0 that separates `warn` from `fail`. The one
section this edit rewrote now clears the floor.

| Section | Words | Connectives | Per 100 words | Verdict |
|---|---|---|---|---|
| Introduction | 300 | 1 | 0.33 | fail |
| Exponential dispersion family: a bit of theory | 679 | 21 | 3.09 | **pass** |
| The Bernoulli member | 245 | 5 | 2.04 | warn |
| Deviance loss function | 72 | 0 | 0.00 | fail |
| Examples of deviance losses | 112 | 2 | 1.79 | fail |
| Model fitting on finite samples | 117 | 1 | 0.85 | fail |
| Model validation and model selection | 418 | 6 | 1.44 | fail |
| GLM regression function | 56 | 0 | 0.00 | fail |
| Logit-link example | 127 | 1 | 0.79 | fail |
| EDF and the (special) canonical link choice | 250 | 4 | 1.60 | fail |
| GLM fitting and examples | 52 | 0 | 0.00 | fail |
| Relationship to deviance losses | 72 | 1 | 1.39 | fail |
| GLM example: Bondora data | 349 | 4 | 1.15 | fail |
| Bernoulli deviance loss: in-sample and out-of-sample | 389 | 9 | 2.31 | warn |
| Individual Bernoulli versus grouped binomial | 226 | 3 | 1.33 | fail |
| Takeaways and outlook | 163 | 1 | 0.61 | fail |

The section holding the two new callouts was brought from 1.97 to 3.09 during this edit, by
fronting `By contrast`, `Similarly`, `Consequently`, `Therefore`, `Moreover`, `In particular`
and `Hence` at turns that were previously unmarked. Raising the remaining fifteen sections is a
separate job on prose this edit did not touch.

### `J17` false antithesis: **pass after fix** (four instances cleared)

The construction is banned outright, with no budget. All four predate this edit, and all four
were cleared, following the precedent of `cd8207c` on R1 and `1ff9456` on the research note.

| Was | Now |
|---|---|
| "overdispersion is a phenomenon of aggregated default counts rather than of individual indicators" | "overdispersion arises only once default counts are aggregated; a single indicator cannot exhibit it" |
| "we assign each an explicit `missing` category rather than dropping rows or imputing values" | "we assign each an explicit `missing` category, drop no rows, impute no values" |
| "which is IRLS convergence tolerance rather than approximation" | "which is the IRLS convergence tolerance, so the two fits are the same fit" |
| "the code is Python rather than R" | "the code is Python where the original is R" |

The copyright note's instance was the weakest of the four, since a plain comparative would
pass the rubric's part-of-speech check. The other three each name a counterpart the reader
would otherwise have believed, which is the banned move.

### `J24` abstract-pointer summary: **pass after fix**, one candidate remaining

The new prose originally closed the moments callout on "That asymmetry is why a handful of
defaults carries so much weight in a small cell", which the rubric's pointer regex catches. It
now reads "Consequently a handful of defaults carries much of the weight in a small cell, which
is a recurring difficulty in low-default portfolios".

One pseudo-cleft remains at line 724, "the out-of-time split is what reveals that". It carries
a proposition of its own, so it grades `pass` on the rubric's function test.

### `J18` unpacking colon: **pass after fix**

The moments callout originally read "The name follows: $\kappa$ generates the cumulants of the
family". The colon restated the clause before it, so it became "The name follows, since
$\kappa$ generates the cumulants of the family up to that affine change of argument". No other
mid-sentence colon in the document unpacks its own clause.

### Everything else

`M1` to `M11` return `pass` with zero candidates surviving the regex pre-pass: no dashes, no
Americanisms, no banned phrases, no bare "percent" in a data context, no spaced currency, no
abbreviated months, no underline, and no competitor citation. `M10` produced 46 serial-comma
candidates and none is a real breach; each is either a two-item list, a compound predicate, or
a comma doing appositive work. `J1` to `J24` pass on the judgement read, with `J9` satisfied by
the abstract and introduction defining PD, EDF, and GLM before use, and `J8` satisfied
throughout. `M9`, `J5`, `J11`, `J12`, `J13`, `J15` and `J19` return `not_applicable`.

## What this run tells us

The lecture's mechanics are clean and its cadence is disciplined, so the two outstanding
criteria are both about connective tissue rather than about diction. `J25` reproduces the
result R1 recorded, which suggests a house pattern in the credit lectures instead of a defect
in this document: mathematical exposition leans on the formulas to carry the logical turns, and
the prose between them goes unmarked. The new callouts show the fix is cheap when applied
deliberately, at roughly one fronted connective per eighty words.
