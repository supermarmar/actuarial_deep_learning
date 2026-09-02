# Grading report: 02_credit-edf-glm

Graded 2 September 2026 against `01 Guidelines/_rubrics/writing-guidelines-global.md`
(criteria `M1` to `M11`, `J1` to `J29`; seven withdrawn ids return `not_applicable`). The
grader is informational and blocks nothing.

Text extracted from `credit_lectures/02_credit-edf-glm.qmd` rather than from the rendered
HTML, for the reason recorded in the R1 report: the skill's `extract_text.py` returns Quarto's
inlined CSS and JavaScript alongside the prose on these documents. Code cells, display maths,
table rows and `#| fig-cap` lines were stripped, and inline maths was replaced with a token.
Prose total is 3,834 words across sixteen graded sections, references and the copyright note
excluded from the `J25` counts.

## Headline

| Document | Verdict | Mechanical fails | Judgement fails | Notes |
|---|---|---|---|---|
| `02_credit-edf-glm.qmd` | **fail** | 0 | 1 | `J25` connective density fails in fifteen of sixteen sections. `M10`, `J9`, `J17`, `J18`, `J23` and `J24` each had a breach and all are fixed. The section holding the new prose clears the `J25` floor. |

## How each criterion was reached

The distinction matters for reading the passes below, so it is stated rather than implied.

- **Regex pre-pass, then judged:** `M1`, `M2`, `M3`, `M4`, `M5`, `M6`, `M7`, `M8`, `M10`,
  `M11`, `J2`, `J9`, `J14`, `J16`, `J17`, `J18`, `J20`, `J21`, `J22`, `J23`, `J24`, `J25`,
  `J26`, `J27`, `J28`, `J29`. Each has a detection hint in the rubric and it was run.
- **Read without a regex:** `J1` (British idiom), `J3` (conclusion first), `J4` (promotional
  register), `J6` (bullet nesting), `J7` (bold and italics), `J8` (sentence-case headings).
- **`not_applicable`:** `M9`, `J5`, `J11`, `J12`, `J13`, `J15`, `J19`, all withdrawn, plus
  `J10`, since a lecture assigns no actions with an owner and a deadline.

## Detailed findings

### `J25` connective density: **fail**

The rubric grades a floor of 3.0 combined connectives per 100 words, section by section. The
document runs at **1.65** overall, below the 2.0 that separates `warn` from `fail`. The one
section this edit rewrote clears the floor.

| Section | Words | Connectives | Per 100 words | Verdict |
|---|---|---|---|---|
| Introduction | 304 | 1 | 0.33 | fail |
| Exponential dispersion family: a bit of theory | 678 | 21 | 3.10 | **pass** |
| The Bernoulli member | 239 | 5 | 2.09 | warn |
| Deviance loss function | 72 | 0 | 0.00 | fail |
| Examples of deviance losses | 112 | 2 | 1.79 | fail |
| Model fitting on finite samples | 117 | 1 | 0.85 | fail |
| Model validation and model selection | 423 | 6 | 1.42 | fail |
| GLM regression function | 56 | 0 | 0.00 | fail |
| Logit-link example | 127 | 1 | 0.79 | fail |
| EDF and the (special) canonical link choice | 250 | 4 | 1.60 | fail |
| GLM fitting and examples | 52 | 0 | 0.00 | fail |
| Relationship to deviance losses | 72 | 1 | 1.39 | fail |
| GLM example: Bondora data | 350 | 4 | 1.14 | fail |
| Bernoulli deviance loss: in-sample and out-of-sample | 389 | 9 | 2.31 | warn |
| Individual Bernoulli versus grouped binomial | 232 | 3 | 1.29 | fail |
| Takeaways and outlook | 163 | 1 | 0.61 | fail |

The passing section's 21 hits were checked one by one, since the rubric makes a
part-of-speech check mandatory on `so` and `while` and discounts "Instead of X" as a
preposition. Ten are fronted discursive connectives (`By contrast`, `Similarly`,
`Consequently` three times, `Therefore`, `hence`, `Moreover`, `In particular`, `Hence`) and
eleven are subordinating joins carrying a real turn (`so` five times as a result join,
`since` three times as causal, `Since` twice, `which is why` once). None is an intensifier and
none is a bare simultaneity. The section stood at 1.97 before this edit.

Raising the remaining fifteen sections is a separate job on prose this edit did not touch.

### `M10` serial comma: **pass after fix** (five breaches cleared)

The regex threw 46 candidates, of which five were genuine lists of three or more coordinate
items with no comma before the final "and". Author lists inside a citation (`Gourieroux,
Monfort and Trognon`; `Scognamiglio, Maggi and Wüthrich`) were left alone under the
quoted-material exemption, since repunctuating a citation is the worse error.

| Was | Now |
|---|---|
| "a declined applicant, a validator and a supervisor" | "a declined applicant, a validator, and a supervisor" |
| "the new-customer flag, income verification and employment duration" | "the new-customer flag, income verification, and employment duration" |
| "In-sample loss minimisation, maximum likelihood and log-loss minimisation" | "In-sample loss minimisation, maximum likelihood, and log-loss minimisation" |
| "the storyline, structure and notation" | "the storyline, structure, and notation" |
| "the scorecard points aside and the grouped binomial equivalence" | "the scorecard points aside, and the grouped binomial equivalence" |

### `J17` false antithesis: **pass after fix** (four breaches cleared)

The construction is banned outright, with no budget. All four predate this edit and all four
are cleared, following the precedent of `cd8207c` on R1 and `1ff9456` on the research note.

| Was | Now |
|---|---|
| "overdispersion is a phenomenon of aggregated default counts rather than of individual indicators" | "overdispersion belongs to aggregated default counts alone" |
| "we assign each an explicit `missing` category rather than dropping rows or imputing values" | "we assign each an explicit `missing` category, drop no rows, impute no values" |
| "which is IRLS convergence tolerance rather than approximation" | "which is the IRLS convergence tolerance, so the two fits are the same fit" |
| "the code is Python rather than R" | "the code is Python where the original is R" |

The copyright note's instance was the weakest of the four, since a plain comparative passes
the rubric's part-of-speech check. The other three each named a counterpart the reader would
otherwise have believed, which is the banned move.

### `J23` mirrored negation: **pass after fix**

The first `J17` fix initially read "overdispersion arises only once default counts are
aggregated; a single indicator cannot exhibit it", which is a claim shadowed by its own
negative. Deleting the negative half left the sentence intact, so the negative was cadence and
one breach had been traded for another. The sentence now carries the exclusion positively,
through "alone". The two negations left in the document ("a PD without a standard error cannot
support a capital number", "a single binary observation carries no free variance parameter")
are single claims with no affirmed twin, so both pass.

### `J9` abbreviations defined on first use: **pass after fix**

Four abbreviations ran ahead of their expansions. `PD` appeared in the abstract and the
introduction's bullets while "probabilities of default" sat in the opening sentence without the
parenthetical, so the parenthetical was added. `GLM` appeared in the introduction and was
expanded only in section 4, `AUC` was never expanded at all, and `MTPL` was never expanded.
All three now carry their expansion at first use. `EDF`, `IRLS` and `MLE` were already
correct.

### `J18` unpacking colon: **pass after fix**, one `warn` remaining

The moments callout originally read "The name follows: $\kappa$ generates the cumulants of the
family". The colon restated the clause before it, so it became "The name follows, since
$\kappa$ generates the cumulants of the family up to that affine change of argument".

Five mid-sentence colons remain and four are clean: two introduce a datum, one introduces the
definition of "calibration in the large", and one belongs to a cited lecture title. The fifth,
"This is the simplification that credit buys: where the insurance lectures carry $v_i$ through
every formula as a time exposure, our formulas carry $v_i \equiv 1$", grades `warn`. It
introduces the content of a named thing, which the rubric permits, and it also unpacks the
clause before it, which the rubric does not. At one instance in 3,834 words it sits inside the
budget either way.

### `J24` abstract-pointer summary: **pass after fix**

The moments callout originally closed on "That asymmetry is why a handful of defaults carries
so much weight in a small cell", which the rubric's pointer regex catches. It now reads
"Consequently a handful of defaults carries much of the weight in a small cell, which is a
recurring difficulty in low-default portfolios".

One pseudo-cleft remains at line 730, "the out-of-time split is what reveals that". It carries
a proposition of its own, so it passes the rubric's function test.

### Everything else

`M1` to `M8` and `M11` return `pass` with no candidate surviving: no dashes, no Americanisms,
no banned phrases, no bare "percent" in a data context, no percentage or model metric at the
wrong decimal count, no spaced currency, no abbreviated or slash-separated date, no underline,
and no competitor citation. `J2` finds no contraction anywhere in the document, so no phrase
appears in both forms. `J14` finds no nominalisation carrying an action while the verb idles,
and `J16` no definition or aside wedged between a subject and its verb. `J21` finds one
one-line paragraph, "which is the EDF form with", which is a lead-in to a display rather than a
drumbeat. `J22`'s single triad, "the storyline, structure, and notation", is three nouns and
out of scope. `J20`, `J26`, `J27`, `J28` and `J29` return `pass` with zero candidates. On the
read-only criteria, every section opens on its finding, the register stays analytical, bullets
nest one level, bold marks defined terms, and every heading is sentence case.

## What this run tells us

The lecture's diction is clean and the fixes above were all local, so the one outstanding
criterion is about connective tissue. `J25` reproduces the result R1 recorded, which suggests
a house pattern in the credit lectures instead of a defect in this document: mathematical
exposition leans on the formulas to carry the logical turns, and the prose between them goes
unmarked. The new callouts show the fix is cheap when applied deliberately, at roughly one
fronted connective per eighty words. Worth noting separately, the `M10` and `J9` breaches were
both invisible to a reader and both caught by a regex, which is the case for running the
grader on the remaining credit lectures rather than on the ones under active edit.
