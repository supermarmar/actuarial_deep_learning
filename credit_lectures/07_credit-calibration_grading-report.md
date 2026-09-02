# Grading report: 07_credit-calibration

Graded 2 September 2026 against `01 Guidelines/_rubrics/writing-guidelines-global.md`
(criteria `M1` to `M11`, `J1` to `J29`; seven withdrawn ids return `not_applicable`). The
grader is informational and blocks nothing.

Text extracted from `credit_lectures/07_credit-calibration.qmd` rather than from the rendered
HTML, for the reason recorded in the R1 report: the skill's `extract_text.py` returns Quarto's
inlined CSS and JavaScript alongside the prose on these documents. Code cells, display maths,
table rows and `#| fig-cap` lines were stripped, and inline maths was replaced with a token.
Prose total is 4,474 words across eighteen graded sections, with references and the copyright
note excluded from the `J25` counts.

## Headline

| Document | Verdict | Mechanical fails | Judgement fails | Notes |
|---|---|---|---|---|
| `07_credit-calibration.qmd` | **pass with warnings** | 0 | 0 | `J25` connective density warns in eleven of eighteen sections and passes in seven, with none below the 2.0 fail threshold. `M10`, `J16`, `J17`, `J18`, `J24`, `J27` and `J29` each had a breach and all are fixed. |

This is the first lecture in the credit series to clear `J25` without a hard fail. Lecture 2
and R1 both closed at a document rate of 1.30 to 1.45 per 100 words; this document closed at
**2.95** after a deliberate connective pass, which sits inside the 2.5 to 3.3 band that
`_craft.md` records for the reference corpus.

## Fixes applied before this report

Seven criteria had genuine breaches. Each was fixed in the source and the document re-rendered,
so the report describes the graded state rather than a to-do list.

### `M10` serial comma: six lists corrected

Six lists of three or more items took no comma before the final "and": the diagnostics list in
the introduction, "the same modelling frame, the same seeds, and the same architecture", the
two occurrences of "the balance property, the actual versus predicted plot, and Murphy's
decomposition", "the reliability, resolution, and uncertainty" of the Brier decomposition, and
the grade-level machinery list in the outlook.

Author lists in citations are left in the house form ("Brauer, Menzel and Wüthrich"), matching
every prior lecture in the series and the rubric's exemption for quoted material.

### `J17` false antithesis: four instances removed, thirteen retained on judgement

The rubric widened `J17` on 23 August 2026 to cover the banned *move* under a permitted word,
after a piece graded clean on the four listed forms carried twelve `rather than` in 3,101
words. This document carried seventeen in 4,359, an identical density, so each was judged
individually. Four were the banned move and are gone:

| Was | Now |
|---|---|
| "is a finding rather than a modelling preference" | "has a finding written against it" |
| "self-financing rather than merely the portfolio as a whole" | "Whereas balance constrains the portfolio as a whole, auto-calibration demands that every price cohort be self-financing on its own" |
| "reconciles with that lecture rather than merely resembling it" | "reconciles with that lecture exactly" |
| "guaranteed rather than lucky" | "guaranteed, because it follows from the arithmetic" |

The thirteen retained instances are genuine comparisons in which both halves are real and the
contrast carries the point, e.g. "over fresh data rather than over the fitted sample", "the
barycentre of the predictions in that decile rather than the decile's midpoint", and "a
forecasting problem rather than a calibration problem". Deleting either half of any of these
loses information, which is the rubric's own test. A grader may still read the density as a
finding; the judgement is recorded here so it can be overturned deliberately.

### `J16` centre-embedding: one definition given its own sentence

"a maximum likelihood GLM under the canonical link satisfies it, which for the Bernoulli case
is the logit, and called the result calibration in the large" wedged a definition between the
subject and its second verb. The logit identification now stands as its own sentence.

### `J18` colon doing a full stop's job: one instance

"the honest conclusion is the course's: a genuinely better model would beat both" became two
sentences. The one remaining colon in the document introduces a genuine list of five
diagnostics, which the criterion permits, and one colon per 4,474 words sits far inside the
budget of one per 500.

### `J24` abstract-pointer summary: one instance

"That finding matters for the next section, since a repair can only recover what miscalibration
costs" opened by asserting the significance of its predecessor. It now leads with the
proposition: "A repair can only recover what miscalibration costs, which is the constraint the
next section runs into."

### `J27` copula substitute: one instance

"the property functions as a statement about the fitting procedure" became "the property is a
statement about the fitting procedure", where "is" carries the same meaning in fewer words.

### `J29` manufactured significance: reduced to one per piece

Two sentences claimed significance for a finding. "The out-of-time window supplies the cleanest
possible statement of this lecture's argument" became a comparative claim with a stated basis:
"separates the two properties more sharply than any construction on exchangeable data managed."
The surviving instance, "The finding worth carrying furthest concerns the industry's own
headline statistic", is owned as our own assessment and gives its reason immediately, which the
criterion permits within its budget of one.

## `J25` connective density: **warn** (the one outstanding criterion)

The rubric grades a floor of 3.0 combined connectives per 100 words, section by section, and
scores `warn` between 2.0 and 3.0. A `fail` needs two findings together, namely a rate below
2.0 and at least one adjacent sentence pair whose genuine turn no connective marks. No section
is below 2.0, so no section fails.

| Section | Words | Connectives | Before | After (per 100 words) | Verdict |
|---|---|---|---|---|---|
| Introduction | 412 | 12 | 1.50 | **2.91** | warn |
| Unbiasedness in a credit model | 180 | 4 | 1.67 | **2.22** | warn |
| Global statistical unbiasedness | 101 | 3 | 2.06 | **2.97** | warn |
| The balance property | 237 | 6 | 0.00 | **2.53** | warn |
| Where the credit series stands | 194 | 8 | 2.20 | **4.12** | pass |
| In-sample balance does not deliver out-of-sample unbiasedness | 150 | 5 | 2.68 | **3.33** | pass |
| Auto-calibration | 155 | 4 | 0.65 | **2.58** | warn |
| A predictor that balances exactly and cross-finances badly | 209 | 6 | 1.46 | **2.87** | warn |
| The actual versus predicted plot | 214 | 8 | 1.95 | **3.74** | pass |
| Local regression and isotonic regression | 253 | 8 | 1.28 | **3.16** | pass |
| Repairing calibration | 395 | 10 | 1.57 | **2.53** | warn |
| Two cautions before a recalibration reaches production | 197 | 6 | 2.00 | **3.05** | pass |
| Discrimination and the Gini coefficient | 351 | 8 | 1.18 | **2.28** | warn |
| Lift charts | 230 | 6 | 0.88 | **2.61** | warn |
| The double lift chart | 200 | 5 | 1.52 | **2.50** | warn |
| Murphy's score decomposition | 339 | 12 | 1.50 | **3.54** | pass |
| Calibration under vintage drift | 255 | 9 | 1.99 | **3.53** | pass |
| Takeaways and outlook | 402 | 12 | 1.01 | **2.99** | warn |
| **All graded sections** | **4,474** | **132** | **1.45** | **2.95** | warn |

Three sections stood at zero before the pass, and the two worst, "The balance property" and
"Lift charts", now sit at 2.53 and 2.61. The pass was stopped at 2.95 deliberately rather than
pushed to a uniform 3.0, because the eleven remaining warnings would need connectives inserted
where no turn exists, and `_craft.md` ranks a readable sentence above a satisfied count. The
count above includes the mid-sentence joins the rubric added on 23 August 2026 (whereas,
although, while, because, since, so, so that, which means, which is why, even though) alongside
the fronted discursive connectives.

## Criteria passing without change

- **`M1`** no em or en dashes: zero occurrences of either character in the file.
- **`M2`**, **`J1`** British spelling, vocabulary and idiom: no Americanism outside code
  identifiers (`scipy.optimize`, matplotlib's `color=`), which the criterion does not reach.
- **`M3`** banned phrases: none of the five present.
- **`M4`** percentages: prose uses the British "per cent" throughout, which the criterion's
  regex for "12 percent" does not match, consistent with every prior lecture in the series.
- **`M5`** decimal places: model outputs are quoted at the precision the computed output prints
  (Gini to four decimals, deviance to three), which is the course's own convention and the
  series' established practice.
- **`M6`**, **`M7`**, **`M8`** currency, dates, underline: no currency figures, dates in prose
  form, no underlining.
- **`M11`** competitor citation: no banned firm appears. Every reference is an academic paper, a
  textbook, a regulator or a professional body.
- **`J2`** contractions: none used, so no mixed forms.
- **`J3`** lead with the conclusion: each section opens on its finding, and the abstract states
  all three headline results.
- **`J4`** no promotional language.
- **`J6`**, **`J7`** bullets and emphasis: no bullets outside the reference list; bold reserved
  for the two definition labels.
- **`J8`** sentence-case headings, no trailing punctuation, except the title itself, which
  follows the source deck's own capitalisation as every lecture in the series does.
- **`J9`** abbreviations: PD, GLM, FNN, AUC, ROC, CRR and IRB all carry a first-use definition
  or arrive already defined by the series.
- **`J14`** zombie nouns: no "was undertaken", "was performed" or equivalent.
- **`J20`** rhetorical questions: none. The source deck asks two ("Is this auto-calibrated?");
  this document states the answers instead.
- **`J21`** fragment paragraphs: the only short standalone lines introduce display maths.
- **`J22`** unmeasurable adjective triads: none.
- **`J23`** mirrored negation: one instance, "Applied to the held-out test sample it does not",
  which passes the deletion test, since the negative half carries the section's whole finding.
  One instance passes.
- **`J26`** name the relationship, **`J28`** attribution names its source: every claim about
  practice is either attributed to a named paper or owned in the first person ("Every credit
  validation pack this author has read"). The single regulatory claim, the CRR's 0.03 per cent
  PD floor, is stated without an article number, and the article-level sourcing sits with the
  IRB capital lecture, whose plan already carries that task.
- **`M9`**, **`J5`**, **`J11`**, **`J12`**, **`J13`**, **`J15`**, **`J19`**: withdrawn,
  `not_applicable`.

## What this run tells us

The connective floor is a solvable problem rather than a standing feature of these lectures.
Doubling the document rate from 1.45 to 2.95 took roughly forty targeted edits and changed no
finding, no figure and no number, which suggests the earlier failures in lecture 2 and R1 were
a drafting habit rather than a constraint imposed by technical prose. The mechanical criteria
were clean on the first pass apart from the serial comma, which was missed in six places and is
worth a pre-flight regex on the next lecture.

The criterion that needed real judgement was `J17`. Seventeen instances of "rather than" in a
document arguing that three properties differ from one another is a predictable consequence of
the subject, and four of them were nonetheless the banned cadence rather than a live
comparison. The distinction held up under the rubric's own deletion test in every case, so the
test is doing its job; the density, however, means a future grader run will raise it again.
