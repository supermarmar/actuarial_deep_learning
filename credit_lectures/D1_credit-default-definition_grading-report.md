# Grading report: D1_credit-default-definition

Graded 3 September 2026 against `01 Guidelines/_rubrics/writing-guidelines-global.md`
(criteria `M1` to `M11`, `J1` to `J29`; seven withdrawn ids return `not_applicable`).
Input: `credit_lectures/D1_credit-default-definition.html`.

Graded on **prose only**. The rendered HTML carries Python chunks, matplotlib keyword
arguments and pandoc's default CSS, and grading those produced three false positives on the
first pass (`color=` sixteen times, an en dash inside an axis-label string, and LaTeX
`\mathcal`). The text under grade is the `.qmd` with its YAML header and code chunks stripped:
7,663 words of flowing prose.

| Document | Overall | Mechanical fails | Judgement fails | Notes |
|---|---|---|---|---|
| D1_credit-default-definition | **warn** | 0 | 1 (`J25`) | One en dash found and fixed during the run; `J25` under-connection improved from 0.80 to 1.36 per 100 words and remains below the floor |

## Mechanical criteria

All eleven pass. Three candidates were raised by the regex pre-pass and all three were
discounted on confirmation.

| Id | Verdict | Note |
|---|---|---|
| `M1` no em or en dashes | **pass** (after fix) | One en dash found, inside `b.replace("-", "–")`, which rewrote the chart's bucket labels. Removed rather than argued about, since a numeric-range en dash is defensible typography and the house rule is cheaper to obey than to litigate. Source now contains zero. |
| `M2` British spelling | **pass** | `Modeling` appears once, inside the course's own title "Deep Learning for Actuarial Modeling". A proper noun, and it matches every other lecture in the series. |
| `M3` banned phrases | **pass** | None of the five present. |
| `M4` percentages | **pass** | The document writes "per cent" throughout, the British two-word form. The criterion's regex targets the American "percent" and does not fire. |
| `M5` decimal places | **warn**, see below | |
| `M6` currency | **not_applicable** | No currency amounts. |
| `M7` dates | **pass** | Prose dates in full form; no abbreviated months. |
| `M8` underline | **pass** | None. |
| `M9` | **not_applicable** | Withdrawn 22 August 2026. |
| `M10` serial comma | **pass** | 44 regex candidates, which the rubric says over-fires by design. Every one inspected is a compound predicate, a non-restrictive clause, or a two-item list. Genuine three-item lists all carry the comma: "were never declared in default, and repaid in full"; "No metric, no threshold, and no method". |
| `M11` competitor citation | **pass** | No banned firm appears. |

### `M5`: decimal places, and why this is referred rather than fixed

The rubric asks for two decimal places on percentages. The lecture reports one: 61.8, 37.8,
9.8, 1.4, 15.4, 20.8, 43.7, 91.9.

This is referred to the author rather than corrected, for two reasons. The series is already
inconsistent, since lecture 1 writes "28.95 per cent" and `R1` writes "9.1 percentage points",
so changing D1 alone would make it agree with one neighbour and disagree with the other.
Separately, a cure rate computed on 1,613 facilities carries a standard error near 1.2
percentage points, so a second decimal place would assert precision the sample does not have.
The fix, if wanted, is a series-wide convention rather than an edit to this file.

## Judgement criteria

Twenty-two pass, seven are withdrawn, and one fails.

The machine-cadence family is clean. `J17`, the banned negated counterpart clause, returns
zero on every form tested, including "not only ... but also", "it's not just X, it's Y" and
"less about X than about Y". `J20` finds no rhetorical-question hinge. `J22` finds no
three-adjective series. `J21`'s candidates are a bolded lead-in to a display equation and two
reference-list fragments, none of them a gravitas fragment. `J18` raises six colons; all six
introduce a genuine list, a datum or a definition, and none stands in for a full stop.

### `J25`: connective density, **fail**

The document ran at **0.80** connectives per 100 words on the first pass, against a floor of
2.0 and a measured house voice of 1.78. This is the documented failure mode of the house
voice, and it was the only real finding of the grading run.

Fifty connectives were added at genuine logical turns across two passes, taking the rate to
**1.36**. Discursive connectives rose from 15 to 44 and, more usefully, from one distinct form
to sixteen: "However" and "Moreover" and "Hence" and "Indeed" and "In particular" appeared
zero times before the pass and appear throughout now.

| Section | Words | Connectives | Rate | Verdict |
|---|---|---|---|---|
| Where lecture 1 stopped | 838 | 13 | 1.55 | warn |
| Terminology | 805 | 13 | 1.61 | warn |
| The four dials | 620 | 8 | 1.29 | warn |
| Three targets wearing one name | 509 | 11 | 2.16 | **pass** |
| Cure | 737 | 11 | 1.49 | warn |
| Write-off | 331 | 6 | 1.81 | warn |
| SICR, bounded above by default | 363 | 5 | 1.38 | warn |
| From a definition to a data shape | 129 | 1 | 0.78 | fail |
| What a snapshot extract cannot answer | 230 | 4 | 1.74 | warn |
| What a monthly panel adds | 2,137 | 30 | 1.40 | warn |
| What this lecture omits, and why | 265 | 0 | n/a | apparatus |
| Takeaways | 396 | 2 | 0.51 | apparatus |
| Copyright and attribution | 236 | 0 | n/a | apparatus |
| References | 67 | 0 | n/a | apparatus |
| **Document** | **7,663** | **104** | **1.36** | **warn** |

Three of the four remaining zeros are apparatus the rubric excludes: a numbered takeaways
list, a copyright note and a reference list. The fourth, "From a definition to a data shape",
is a deliberate one-paragraph section whose entire job is compression, and stuffing a
connective into it would work against the only thing it is for.

The honest verdict is that the flowing sections now run between 1.29 and 2.16 and average
close to the house 1.78, while the document as a whole sits below the floor. The rubric states
that `warn` is the expected verdict on competent house prose, so this is the diagnosis the
rule exists to make rather than a defect left in place.

## What this run tells us

The lecture was mechanically clean on arrival and its one real weakness was the house's own
documented one. Under-connection is invisible to the writer, because each sentence is
individually well formed and only the joins between them are missing, which is exactly why the
criterion grades a rate rather than a span. Worth noting for future runs in this repo: grading
a rendered Quarto lecture without stripping its code chunks produces three false positives and
hides the real finding, so strip the `.qmd` rather than extract the HTML.
