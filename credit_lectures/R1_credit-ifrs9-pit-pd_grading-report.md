# Grading report: R1_credit-ifrs9-pit-pd

Graded 2 September 2026 against `01 Guidelines/_rubrics/writing-guidelines-global.md`
(criteria `M1` to `M11`, `J1` to `J29`; seven withdrawn ids return `not_applicable`). The
grader is informational and blocks nothing.

Text extracted from `credit_lectures/R1_credit-ifrs9-pit-pd.qmd` rather than from the rendered
HTML, because the skill's `extract_text.py` returns Quarto's inlined CSS and JavaScript
alongside the prose on this document. Code cells, display maths, table rows, table captions
and `#| fig-cap` lines were stripped; inline maths was replaced with a token. Prose total is
9,179 words across seven sections.

## Headline

| Document | Verdict | Mechanical fails | Judgement fails | Notes |
|---|---|---|---|---|
| `R1_credit-ifrs9-pit-pd.qmd` | **fail** | 0 | 1 | `J25` connective density fails in all seven prose sections. Everything else passes after the fixes below. |

## Detailed findings

### `J25` connective density: **fail** (the one outstanding issue)

The rubric grades a floor of 3.0 combined connectives per 100 words, section by section, and
`_craft.md` names under-connection as the documented failure of the house voice. This document
runs at **1.30**, below the 1.78 that `_craft.md` records as the failing house measurement and
well below the 2.0 that separates `warn` from `fail`.

| Section | Words | Connectives | Per 100 words | Verdict | To reach 3.0 |
|---|---|---|---|---|---|
| Where lecture 1 stopped | 285 | 1 | 0.35 | fail | +8 |
| The two conditioning axes | 1,342 | 18 | 1.34 | fail | +22 |
| Macro conditioning, forward-looking information and the FiT PD | 2,237 | 26 | 1.16 | fail | +41 |
| How the estimate is actually produced | 3,018 | 44 | 1.46 | fail | +47 |
| The demonstration on Bondora | 1,530 | 22 | 1.44 | fail | +24 |
| What stays with the IRB lecture | 351 | 5 | 1.42 | fail | +6 |
| Takeaways | 416 | 3 | 0.72 | fail | +9 |
| **Prose total** | **9,179** | **119** | **1.30** | **fail** | **+156** |

Counted with the rubric's own inventory: the fourteen discursive connectives from `_craft.md`,
the five further house connectives, and the subordinating and coordinating turns the
23 August 2026 raise added (`whereas`, `although`, `while`, `because`, `since`, `so`, `so
that`, `even though`, `which means`, `which is why`, `but`, `yet`). The document's actual
inventory is narrow: 30 `because`, 12 `since`, 10 `while`, 6 `consequently`, 6 `therefore`,
4 `instead`, 4 `so that`, 3 `which is why`, 2 `furthermore`, 1 `however`, 1 `hence`. One
`however` in 9,179 words is the shape of the problem.

**Fix, not applied.** Raising the rate to the floor means roughly 156 inserted connectives
across every paragraph of the lecture. That is a single stylistic decision about the whole
document rather than seven local repairs, so it is left for the author. The suggested target
is the 2.5 to 3.0 band, fronting each connective at its clause, and concentrating first on the
opening section and the takeaways, which are the most-read and the two worst measured.

## Findings raised and fixed during grading

These were breaches when the grader first ran and are corrected in the committed `.qmd`.

### `J17` false antithesis: was **fail**, now **pass**

The construction is banned outright, and the 23 August 2026 widening extends the ban to
`rather than` wherever the second half names a counterpart the reader would otherwise have
believed. The document carried **48** instances in 10,452 words, one every 218 words, denser
than the 258-word density that prompted the widening. Nineteen were the banned move and are
rewritten. Representative spans:

| Was | Now |
|---|---|
| "the notation is inherited rather than invented" | "the series inherits the notation" |
| "a modelling choice rather than a formatting one" | "a modelling choice with a measurable cost" |
| "the point-in-time claim is demonstrated rather than asserted" | "the point-in-time claim now rests on evidence" |
| "makes the size of the error concrete rather than abstract" | "puts a number on the error" |
| "which the method intends rather than tolerates" | "which the method intends" |
| "deserves scrutiny rather than applause" | "invites scrutiny" |
| "the division between the two is by purpose rather than by mathematics" | "purpose divides the two lectures while the mathematics stays common" |

Twenty-nine instances remain, one every 358 words, and each does plain comparative work of
the kind the rubric passes ("national rather than borrower-specific", "settlement and
write-off are states rather than a censoring convention").

### `M10` serial comma: was **fail**, now **pass**

Five three-or-more-item lists took no comma before the final "and": "nowhere in IFRS 9,
nowhere in the EBA guidelines and nowhere in the literature"; "baseline, downside and upside";
"the baseline, time-fixed covariates, spell-level time-varying covariates and portfolio-level
time-varying covariates"; "economic plausibility, directional constraints, parsimony and
calibration stability"; and the comparison table's source list. All five now carry it.

### `J18` unpacking colons: was **warn**, now **pass**

Two summarising clauses unpacked by a colon into parallel phrases, in the two most visible
positions in the document. Both are now full stops.

- Abstract: "the map is what makes the rest legible: the term structure IFRS 9 needs,
  forward-looking information and the FiT PD it produces, the eleven ways..."
- Section 1: "What follows pays the debt: it separates..., builds..., reviews..."

Sixteen mid-sentence colons remain against a budget of eighteen at one per 500 words, and each
introduces a genuine datum, list or definition.

### `J23` mirrored negation: was **warn**, now **pass**

Three claims shadowed by their own negative, all rewritten: "It is over the macro state, and
it is not over anything to do with survival"; "That is a legitimate quantity and it is not the
one an expected credit loss needs"; "The variable is not uninformative in general; it is
uninformative in this window". A fourth was introduced by one of the `J17` rewrites
("purpose divides the two lectures, and the mathematics does not") and removed in the same
pass.

### `J24` abstract-pointer summaries: was **warn**, now **pass**

Two sentences pointed back with a bare noun purely to announce that the previous sentence
mattered: "That table is the map for the rest of the lecture" and "That table is the whole
answer to lecture 1's objection". Both now carry the proposition instead. One pseudo-cleft
doing the same work ("the honest note is what the comparison shows") is also reworded. The
ten remaining `is what` constructions all introduce new content and pass on function.

## Criteria passing without change

`M1` no dashes (zero). `M2` British spelling: the only American spellings are `Modeling`
inside three quoted Djurovic paper titles, which the quoted-material exemption covers, and the
158 apparent hits on `math` are the extraction token for inline maths. `M3` banned phrases
(zero). `M4` percentages: the document uses "per cent" in prose throughout, which the rule
permits, and no table or caption carries the word form. `M5` to `M8` formatting. `M11` no
competitor citation (zero; the reference list is regulators, academics and Eurostat).
`J1` to `J4`, `J6` to `J10`, `J14`, `J16`, `J20` rhetorical questions (zero), `J21` fragment
paragraphs, `J22` adjective triads, `J26` to `J29`. Withdrawn and `not_applicable`: `M9`,
`J5`, `J11`, `J12`, `J13`, `J15`, `J19`.

## What this run tells us

Every mechanical criterion and every judgement criterion except one now passes, and the one
that fails is the house's own documented weakness rather than an accident of this document.
The `J17` result is the more instructive of the two: the lecture carried no instance of the
surface form "X, not Y", so the grep used while drafting reported it clean, and the ban was
being breached forty-eight times under a permitted word. A drafting check that greps only the
literal forms will keep missing this, which is the argument for running the grader rather than
a regex.
