# Grading report: R3, sample design, representativeness and class imbalance

Input: `credit_lectures/R3_credit-sampling-and-representativeness.html`
Graded: 3 September 2026, against `01 Guidelines/_rubrics/writing-guidelines-global.md`.

| Document | Verdict | Mechanical fails | Judgement fails | Notes |
|---|---|---|---|---|
| `R3_credit-sampling-and-representativeness.html` | pass | 0 | 0 | Four breaches found on the first pass and all four fixed before this report. |

## Findings, all resolved before publication

**J17, negated counterpart clause. Banned outright, fixed.**
The section 4 heading read "Split loans, not rows". The construction carries no budget, so the
heading was rewritten to "The unit of a split is the loan", which keeps the claim and drops the
negation. The rendered HTML and the table of contents were both checked afterwards.

**J23, a claim shadowed by its own negative, combined with J18, an unpacking colon.**
Section 7.1 read "The cleaned out-of-time test sample is empty. Not small: empty." Deleting the
negative half left a passage that survives intact, which is the rubric's own test, so the beat
was cut. It now reads "empty, and the count is exactly zero rather than merely small".

**J23 budget, one instance retained deliberately.**
Section 2 opens "A rating system is not built on a training set and a test set. It is built on
four samples with four different jobs." The construction is doing real work there, since it
corrects the assumption the reader arrives with, and the rubric allows roughly one per piece.
It is the only one left in the document.

**J25, connective density.**
Four sections fell below the floor on the first pass, namely 6.2, 7.2, 8.2 and the opening of
section 9. Each gained a fronted connective carrying real content rather than a filler word.
The document now runs 64 connectives across 6,152 words of prose, or 1.04 per 100.

## Mechanical criteria

No em or en dashes anywhere in the prose. No American spellings outside code identifiers
(`color=`, `normalize=`, both matplotlib and scikit-learn arguments) and one verbatim paper
title, "Rethinking Representativeness Analysis in IRB Modeling", which is quoted as published.
None of the banned vocabulary appears. No competitor is cited, and the reference list carries
regulation, peer-reviewed papers and two industry sources, none of them an advisory firm.

## What this run tells us

Density was measured against the published series rather than against an absolute, because the
rubric grades a floor and the series has its own register. R3 at 1.04 per 100 sits between R2 at
0.88 and lecture 2 at 1.26, so it reads as house prose rather than as an outlier.

The two substantive breaches were both in the same family, namely a contrast stated by negating
its counterpart, and both arrived in places where the writing was trying to be emphatic. That
is the pattern worth watching in this series: the machine-cadence constructions turn up at the
points where a finding is being landed, which is exactly where they are most tempting and most
recognisable.
