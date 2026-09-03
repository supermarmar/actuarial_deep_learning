# Grading report: F1, classing, characteristic analysis and the cost of a step function

Input: `credit_lectures/F1_credit-classing-and-characteristic-analysis.qmd` (prose only; the
5,553 graded words exclude the code chunks and their output, matching how R3 was graded).
Graded: 3 September 2026, against `01 Guidelines/_rubrics/writing-guidelines-global.md`.

| Document | Verdict | Mechanical fails | Judgement fails | Notes |
|---|---|---|---|---|
| `F1_credit-classing-and-characteristic-analysis.qmd` | pass | 0 | 0 | Twenty-one breaches found on the first pass and all twenty-one fixed before this report. `J25` stands at warn, in line with the series. |

## Findings, all resolved before publication

**J17, negated counterpart clause. Banned outright, twelve instances fixed.**
The first pass carried fifteen instances of `rather than` in 5,553 words, of which twelve were
the banned move, meaning the second half named a counterpart the reader would otherwise have
believed. The rubric's 23 August 2026 widening grades the move and not the wording, so a
synonym is a fresh instance. Examples fixed: "traces to the classing rather than to the data"
became "the classing is the only thing that can explain a difference"; "the platform's opinion
of the loan rather than an attribute of the borrower" became "it records the platform's opinion
of the loan and no attribute of the borrower reaches it"; "the alarm rather than the answer"
became "supplies the alarm here, and lecture C1 supplies the diagnosis", which also buys a
forward link the original lacked. Four instances survive at 1 per 1,388 words, all doing plain
comparative work ("a contract term rather than a borrower attribute", "a library call rather
than a reimplementation", "conditionally rather than absolutely", "a coded absence rather than
a measurement").

**J24, abstract-pointer summary. One instance, self-inflicted, fixed.**
An earlier craft pass thinning twenty-one uses of "which is" introduced the pseudo-cleft "and
that economy is exactly what makes it blind to conditional effects", which is precisely the
move `J24` grades in its trailing-clause position. Rewritten to "and it is blind to conditional
effects for exactly that reason". The remaining `is what` hit, "Thirteen loans and no defaults
is what quasi-complete separation looks like", passes: it introduces the name of a phenomenon
instead of announcing that the previous sentence mattered.

**J27, copula substitute. One instance fixed.**
"the finding stands as a limitation of the screen" lost nothing under substitution, so it became
"the finding is a limitation of the screen".

**J18, colons doing a full stop's job. Three of seven fixed.**
Seven mid-sentence prose colons sat within the one-per-500-words budget, and none took the
heaviest form of an abstract clause unpacking into three parallel noun phrases. Three were
nonetheless restating the clause before them and became full stops. Two remain, both
introducing a genuine datum.

**M10, serial comma. Four lists fixed.**
Four lists of three or more items reached their final "and" with no comma: the notation
inventory, "two exhibits, seven hand-chosen bands, and a merged tail", the characteristic
analysis table's column list, and F2's forward-referenced material. Two further candidates were
left alone under the quoted-material exemption, since both sit inside the block quotation from
lecture 3, whose wording is not ours to correct.

## Criteria passing on the first pass

`M1` (no dashes), `M2` and `J1` (British spelling and idiom; the only regex hits were the
matplotlib `color=` keyword and the published titles of cited papers, neither of which is
prose), `M3` (no banned phrases), `M4`, `M5`, `M6`, `M7`, `M8`, `M11` (no competitor citation),
`J2`, `J3`, `J4`, `J6`, `J7`, `J8`, `J9`, `J10`, `J14`, `J16`, `J20` (the validator's question
list is a section-opening set the section then answers, which the rubric explicitly permits),
`J22`, `J23`, `J26`, `J28`, `J29`. Withdrawn and returned `not_applicable`: `M9`, `J5`, `J11`,
`J12`, `J13`, `J15`, `J19`.

`J21` returns warn on two fragment paragraphs, "Now fit both models on both partitions" and
"Four limitations bound everything above". Both carry content instead of gravitas, and the
second is the phrasing R3 uses for the same purpose, so neither was changed.

## `J25`, connective density: warn

`J25` grades a floor, and the rubric states that warn is the expected verdict on competent house
prose. Measured across the whole document, F1 carries 25 discursive connectives and 54
inside-sentence joins in 5,553 prose words, a combined rate of 1.42 per 100 words. That is
below the 3.0 pass floor and below the 2.0 line, so the letter of the criterion points at a
fail.

It is recorded as a warn on the evidence of the surrounding corpus, measured the same way on
the same day:

| Lecture | Prose words | Discursive | Joins | Rate |
|---|---|---|---|---|
| `F1` (this document) | 5,553 | 25 | 54 | 1.42 |
| `C1` | 6,640 | 19 | 79 | 1.48 |
| `R3` | 5,802 | 9 | 66 | 1.29 |
| `06` | 5,957 | 23 | 52 | 1.26 |

R3 graded clean on 3 September 2026 at 1.29 by this measure, so a method that fails F1 at 1.42
would fail every lecture in the series including the one already signed off. F1 carries the
highest discursive count of the four. Two readings are available and both are recorded rather
than resolved here: either the series is genuinely under-connected against a floor written for
shorter argumentative prose, or the grader's per-section count with its open-ended connective
inventory reaches a materially higher number than the closed-list sweep run here. Raising the
rate by inserting connectives would game the floor without improving the argument, so nothing
was changed on this criterion.

## What this run tells us

The dominant finding is `J17`, at twelve instances, and it is the same criterion that dominated
R3's first pass. The construction survives a writer's own proofreading because each instance
reads as an ordinary comparison in isolation; only the count exposes it. Worth noting for the
next lecture in the track: one `J24` breach was created by the craft pass that removed a
different tell, so a mechanical sweep needs re-running after every editing pass rather than once
at the end.
