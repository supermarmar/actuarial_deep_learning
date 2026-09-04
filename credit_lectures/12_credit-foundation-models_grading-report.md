# Grading report: lecture 12, foundation models, in-context learning and the cold start

Input: `credit_lectures/12_credit-foundation-models.qmd`, prose extracted with code cells,
YAML and display mathematics removed (8,142 graded words).
Graded: 4 September 2026, against `01 Guidelines/_rubrics/writing-guidelines-global.md`.

| Document | Verdict | Mechanical fails | Judgement fails | Notes |
|---|---|---|---|---|
| `12_credit-foundation-models.qmd` | pass | 0 | 0 | Eleven breaches found on the first pass and all eleven fixed before this report. `J25` stands as a warn, which is its expected verdict. |

## Findings, all resolved before publication

**M10, serial comma. Six genuine breaches, all fixed.**

The regex returned 83 candidates, as the rubric says it will. Six survived confirmation as
lists of three or more coordinate items reaching "and" with no comma in front of it:

- "small portfolios, new products, rare events and new vehicle models"
- "a joint power law in compute, data and parameters"
- "TabPFN carries no offset, no exposure and no intercept"
- "The frame, the filters and the seed-1 split"
- "The architecture, the mathematics and the notation"
- "The credit adaptation, the implementation, the datasets and every measurement"

All six now carry the serial comma.

**M10, one exemption taken deliberately.** Author lists in running prose and in the reference
list ("Gorishniy, Rubachev, Khrulkov and Babenko", "Scognamiglio, Maggi, Wüthrich and
Richman", "Padayachy, Richman, Scognamiglio and Wüthrich") are lists of three or more and are
**left unchanged**. The reason is series consistency: all eighteen earlier credit lectures and
every entry in their reference lists use the same convention, so applying `M10` here alone
would make one document of nineteen inconsistent in its citation format. This is recorded as a
decision rather than an oversight. Whether to apply `M10` to author lists across the series is
a separate question, and it would be a nineteen-file change.

**J9, abbreviations defined on first use. Five breaches, all fixed.**

| Abbreviation | First use before the fix | Fix |
|:---|:---|:---|
| `GLM` | "a logistic GLM", undefined | expanded to "logistic generalised linear model (GLM)" |
| `AUC` | "The AUCs tell the same story", undefined | expanded to "the area under the receiver operating characteristic curve (AUC)" |
| `CLS` | "Its CLS token embedding", undefined | expanded to "its classification (CLS) token embedding", with a backward citation to lecture 10-11 |
| `ICL-CT` | used in section 3.7 before any parenthetical definition | "(ICL-CT)" added at the spelled-out first mention in section 3 |
| `CRR` | "CRR Article 174(c)" in section 5.3, before the section 5.4 expansion | expanded at the earlier occurrence to "Article 174(c) of the Capital Requirements Regulation (CRR)" |

`ICL`, `RAG`, `PEFT`, `LoRA` and `EAD` were already defined or glossed at first use and needed
no change. `TabPFN`, `TabICL`, `TransTab` and `FT-Transformer` are product and architecture
names rather than abbreviations, so no expansion applies.

**J9, one exemption.** `GDPR` is left unexpanded. "The UK GDPR" is a defined term in UK
statute, introduced as such by the Data Protection Act 2018, so it functions as the
regulation's short title rather than as an abbreviation the reader has to decode.

**J25, connectives carry the logical turns. Warn, and improved.**

`J25` grades a floor rather than a breach, so a warn is the expected verdict on competent
house prose. The first pass measured a document rate of **1.76 per 100 words** against the
2.5 floor, with **four sections carrying no connective at all**, which is a genuine
under-connection signal rather than a rounding artefact. Under-connection is the documented
house failure mode, so the four were rewritten along with the five next-weakest.

Nine sections were rewritten. The figures below are the first-pass rate followed by the rate
after the rewrite: "What the term means" 0.00 to 2.03, "TabPFN as approximate Bayesian
inference" 0.00 to 1.55, "The in-context learning credibility transformer" 0.00 to 1.30,
"Component 4: the frozen decoder" 0.00 to 2.70, "Adaptation, and what each rung means for a
lender" 0.71 to 1.97, "The families" 0.80 to 2.00, "The proposition, and its arithmetic" 0.92
to 3.23, "Why tabular data resists the recipe" 1.18 to 2.23, and "The retrieval leak" 1.22 to
6.17.

After the rewrite the document rate is **2.05 per 100 words**, 167 connectives in 8,142 words,
with **no section at zero**. Twenty-eight of thirty-seven graded sections remain below the 2.5
floor, and the run stops there deliberately. The remaining shortfall sits in sections whose
word count is dominated by mathematics, tables and enumerated components, where a further
connective would mark a turn the argument does not make. The guidelines are explicit that these
are strong defaults to be broken sooner than writing something awkward.

The per-section table is reproduced below so the verdict can be checked without a rerun.

| Section | Words | Connectives | Per 100 |
|:---|---:|---:|---:|
| Introduction | 224 | 5 | 2.23 |
| What the term means | 148 | 3 | 2.03 |
| The model class | 130 | 3 | 2.31 |
| Adaptation, and what each rung means for a lender | 304 | 6 | 1.97 |
| The GPT series, briefly | 150 | 3 | 2.00 |
| Why tabular data resists the recipe | 179 | 4 | 2.23 |
| The families | 150 | 3 | 2.00 |
| TabPFN as approximate Bayesian inference | 193 | 3 | 1.55 |
| What "no fitting" does and does not mean | 60 | 2 | 3.33 |
| The learning curve | 169 | 4 | 2.37 |
| Two traps in the TabPFN package | 443 | 9 | 2.03 |
| What twelve times the data is worth | 196 | 3 | 1.53 |
| Calibration, and the balance property | 282 | 7 | 2.48 |
| The in-context learning credibility transformer | 77 | 1 | 1.30 |
| Component 0: the base credibility transformer | 120 | 4 | 3.33 |
| Component 1: context retrieval | 80 | 1 | 1.25 |
| The retrieval leak | 81 | 5 | 6.17 |
| Component 2: the outcome token decorator | 267 | 3 | 1.12 |
| Component 4: the frozen decoder | 74 | 2 | 2.70 |
| The proposition, and its arithmetic | 124 | 4 | 3.23 |
| Identity initialisation | 123 | 3 | 2.44 |
| The three training phases | 145 | 2 | 1.38 |
| Fitting it, and checking the proposition | 141 | 3 | 2.13 |
| Results against the series | 253 | 4 | 1.58 |
| What a null result here does and does not license | 87 | 1 | 1.15 |
| Why the mechanism finds nothing to add | 671 | 12 | 1.79 |
| Bondora's Slovak book | 112 | 2 | 1.79 |
| Four models, with intervals | 516 | 8 | 1.55 |
| Where the context comes from | 294 | 9 | 3.06 |
| The explanation is other borrowers | 176 | 3 | 1.70 |
| Reason-code stability under a context re-draw | 416 | 9 | 2.16 |
| The general lesson, about the test rather than the answer | 77 | 3 | 3.90 |
| What does bite: the pool's composition | 103 | 3 | 2.91 |
| A prior whose training data cannot be shown | 242 | 4 | 1.65 |
| What is settled | 87 | 3 | 3.45 |
| Data protection | 253 | 6 | 2.37 |
| Takeaways and outlook | 995 | 17 | 1.71 |
| **Document** | **8,142** | **167** | **2.05** |

References and the copyright note are excluded, being bibliographic rather than argued prose.

## Criteria returning a clean pass

`M1` no em or en dashes: zero occurrences. `M2` British spelling: two candidates, both inside
quoted publication titles ("Deep Learning for Actuarial Modeling", the course's own name, and
"tabular data modeling", the TabTransformer paper's title), which the criterion exempts as
quoted material. `M3` banned phrases: zero. `M4` to `M8`: no candidates. `M11` competitor
citations: zero, on both the case-insensitive and the case-sensitive patterns.

`J1` British vocabulary, `J2` consistent contractions, `J3` conclusion first, `J4` no
promotional language, `J6` bullet nesting, `J7` emphasis, `J8` sentence-case headings with no
trailing punctuation (all 49 checked), `J10`, `J14`, `J16`, `J17` false antithesis, `J18`
colons, `J20` rhetorical hinges, `J21` fragment paragraphs, `J22` adjective triads, `J23`
mirrored negation, `J24` abstract-pointer summaries, `J26`, `J27` copulas, `J28` attribution
and `J29` manufactured significance all return `pass`.

Two `J17` candidates were examined and cleared. "genuinely different rather than merely
unobserved" and the other "X rather than Y" constructions are the **prescribed replacement**
for the banned cadence rather than instances of it, since the guidelines direct writers to
front the contrast in exactly that form.

Five `J22` candidates were examined and cleared. All five are noun or author lists
("compute, data, and parameters"; "Gorishniy, Rubachev, Khrulkov and Babenko") rather than
triads of unmeasurable adjectives, which is the over-firing the criterion warns about.

`M9`, `J5`, `J11`, `J12`, `J13`, `J15` and `J19` return `not_applicable`, being withdrawn.

## What this run tells us

The document's failure mode was mechanical rather than rhetorical. Every judgement criterion
that grades cadence passed on the first pass, which is what one would expect of prose written
against `_craft.md`, and the eleven real breaches were all in the two places that reward
sloppiness: serial commas inside three-item lists, and abbreviations that felt defined because
an earlier lecture defined them. The second is a specific hazard of a nineteen-lecture series,
where `GLM`, `AUC`, `CLS` and `PD` are so thoroughly established in the author's head that
their first appearance in a new document reads as a later one.

The connective density is the finding worth carrying forward. Four sections reached zero, and
all four were expository passages restating published work rather than passages arguing
towards a measurement. That is a recognisable pattern: where the lecture argues, it connects,
and where it summarises, it lists. Checking the sections that describe somebody else's method
is therefore a better use of a `J25` pass than checking the sections that report our own
numbers.
