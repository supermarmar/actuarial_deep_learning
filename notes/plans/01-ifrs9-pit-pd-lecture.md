# Plan 1: an IFRS 9 point-in-time PD lecture

> **For a fresh session.** This plan is self-contained and assumes no memory of the
> conversation that produced it. Read it top to bottom before touching a file. Steps
> carry checkboxes so progress survives an interruption. Repo root is
> `/Users/mervedosa/Documents/Repos/actuarial_deep_learning`; every path below is
> relative to it unless it starts with `~` or `/`.

**Answers:** review comment 1 of round 3, recorded verbatim in
`notes/lecture-1-review-comments-2026-09-01.md`. The comment reads:

> This section is getting quite large I think it might need it as its own lecture given
> the complexity expands in a IFRS 9 space. Lets plan out a lecture where we look to
> build that up from this lecture and the notation is aligned to what you have, what I
> want you to touch on is concepts like conditional PiT PDs, unconditional PiT PDs, FiT
> (Forward in Time) which is when you incorporating macro economic information. Do some
> deep research perhaps to find papers that speak about this and refernce many of the
> Botha papers that go into different methods of estimating such PiT PDs (markov
> chains, regressions, survival models etc) and the pros and cons of eahc

**Goal:** grow lecture 1's point-in-time callout into a lecture of its own that defines
the PD conditioning axes properly, introduces macro conditioning and its IFRS 9 use,
and reviews the competing estimation methods with an honest verdict on each.

**Approach:** the lecture inherits lecture 1's notation unchanged and adds only what the
term structure forces, i.e. a discrete hazard, a survival function and the marginal and
cumulative PDs built from them. It argues from the Bondora person-period expansion that
`S1_credit-survival-bridge` already establishes, with real macroeconomic series attached
by calendar month, so the point-in-time claim is demonstrated rather than asserted. The
methods review is a comparison table plus prose, sourced from the vault's existing Botha
registrations rather than from a fresh literature trawl.

**Stack:** Quarto plus the pinned `.venv` (polars 1.40.1, statsmodels 0.14.6,
scikit-learn 1.8.0, torch 2.11.0). Render with
`bash scripts/render_lecture.sh credit_lectures/<file>.qmd`, never bare `quarto render`.

---

## Global constraints

These bind every task. They come from `CLAUDE.md` at the repo root and from the house
writing rules, and they are the constraints most easily lost in a fresh session.

- Never call a system `python3`. Use `.venv/bin/python` or activate the venv first.
- Never edit a rendered `credit_lectures/*.html` by hand. The `.qmd` is the source, and
  a render overwrites the HTML. Comments left in HTML are destroyed on render.
- Never add a dependency without flagging it first. `requirements.txt` is the course's
  own file byte for byte.
- British English throughout. No em or en dashes as punctuation. No negated counterpart
  clauses ("X, not Y", "not only ... but also"), which are banned outright. Prose
  carries the reasoning; bullets are for genuine enumerations.
- Every claim taken from a paper gets an inline citation in the lecture's reference
  list, matching the pattern already used in `credit_lectures/S2_survival-insurance-to-credit.qmd`.
- Small logical commits under Conventional Commits, scope `credit_lectures`.

## Decisions taken, 2 September 2026

Mario settled all four on the day the plan was written, so nothing here blocks.

1. **File prefix.** A regulatory track shared with plan 2, giving
   `R1_credit-ifrs9-pit-pd.qmd` here and `R2_credit-irb-capital.qmd` there. Plan 3's
   causal inference lecture takes `C1`.
2. **What "conditional" and "unconditional" name.** The survival axis. A conditional PD
   is the hazard given survival to the start of the period; an unconditional PD is the
   marginal probability that mixes in the chance of surviving that far. PiT against TTC
   stays the macro axis, and the lecture opens by separating the two axes explicitly in
   a two-by-two table, since confusing them is what a reader arrives with.
3. **Whether "FiT" is adopted.** Both, in order. Introduce forward-looking information
   as IFRS 9's own wording, then state that this course calls the resulting PD forward
   in time, so PiT, TTC and FiT read as one family and a reader can still find the
   material in a bank's own documentation.
4. **Empirical spine and macro data.** Bondora expanded to person-periods, with real
   Eurostat series attached, and a small curated CSV committed at
   `credit_lectures/data/macro_eurostat.csv` so the lecture renders on a fresh clone.
   The reasoning is in the data verdict below, and it forces the lecture 1 edit in
   task 8.

## Corroboration found while planning the IRB lecture

Two findings came out of reading the guides repo for plan 2, and both land here.

Decision 2 is confirmed by Mario's own notation. `03_notation.md` in the guides' credit
risk folder defines the $k$-month **unconditional** PiT marginal PD as
$\mathrm{PD}^{\rm uPiT} = P(D^*_{i,t}(k,p) = 1 \mid X)$, "regardless of prior default or
prepayment", against the **conditional** PiT marginal PD
$\mathrm{PD}^{\rm PiT} = P(D^*_{i,t}(k,p) = 1 \mid D_{i,t}(p) = 0, X)$, which conditions
on the loan sitting in the performing risk set. The axis is therefore survival, exactly as
decision 2 assumed, so task 1 step 3 records this file as the primary source rather than
searching for one. The same table already carries one-period survival, cumulative
survival, cumulative PD, lifetime PD and the PD term structure, so task 2's new symbols
should be checked against it and adopted where they agree.

The same file defines FiT, and it defines it twice in incompatible ways. The notation
table has $\mathrm{PD}^{\rm FiT} = \mathrm{PD}^{\rm PiT} \times \mathrm{FLI}_{t'}$, a
multiplicative scalar on a probability, while the systemically conditional PD has
$\mathrm{FLI}_{t'}$ entering a probit in the position of a standard normal factor
realisation. Consequently decision 3 needs a second half, i.e. which of the two the
lecture means, and the recommendation is the probit form, with the multiplicative version
named as the practitioner shortcut and its bias stated. Plan 2 carries the same open
point at `notes/plans/02-irb-capital-lecture.md`, and both lectures must answer it the
same way. Plan 2's task 2 also owns the notation bridge between lecture 1 and the guides,
including a genuine clash on $g$, so read it before starting task 2 here.

## Source material, all of it already on disk

Read these before writing. The vault holds far more on this subject than the lecture
needs, so the research task is mostly selection.

Vault wiki, at `~/Documents/Repos/vault/wiki/`:

- `methods/ifrs9-lifetime-pd-term-structure.md` is the spine. It already summarises the
  three Botha papers the comment asks for and names their methods.
- `methods/forward-looking-information-modelling.md` for the macro regression and the
  short-series design problem.
- `methods/survival-analysis-macroeconomic-pd.md` for Bellotti and Crook (2009), which
  is the original case for time-varying macro covariates in a hazard model.
- `methods/transition-matrix-z-factor.md` and
  `methods/belkin-1998-one-parameter-credit-risk-transition-matrices.md` for the Vasicek
  Z-factor route from TTC to PiT, which is the method lecture 1's hybrid callout already
  writes down.
- `methods/breeden-2016-lifecycle-environment-loan-level-forecasts.md` for the
  age-period-cohort decomposition, which is the cleanest answer to lecture 1's
  collinearity complaint.
- `methods/ifrs9-scenario-design-and-weighting.md` and
  `methods/ifrs9-post-model-adjustments.md` for what happens downstream of the PD.
- `concepts/ifrs9-expected-credit-loss.md` for the ECL identity the lecture is serving.
- `_meta/sources/botha-2025-term-structure-pd-tutorial.md`,
  `botha-2025-term-structure-multistate.md` and `botha-2025-recurrent-event-cox.md` for
  the registrations, including exact titles and section maps for citation.

Guides repo, at
`~/Documents/Repos/guides/docs/wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/`:

- `ifrs9_impairments/05_modelling/pd/01-model_methodology.md` for the production PD
  methodology, and `02-sampling.md` and `03-data_representativeness.md` beside it.
- `ifrs9_impairments/05_modelling/fli/01-model_methodology.md` for how the FLI model is
  actually built and governed.
- `ifrs9_impairments/01_introduction/02_definitons.md` for the house definitions.
- `03_notation.md` in the `credit_risk` folder, to check for a notation clash.

This repo:

- `credit_lectures/01_credit-use-case.qmd`, lines 676 to 830, is the callout being grown.
- `credit_lectures/S1_credit-survival-bridge.qmd` owns the person-period expansion and
  the discrete-hazard exposure convention. Reuse it; do not restate it.
- `credit_lectures/S3_deep-survival-credit.qmd` owns the neural survival head and the
  masking identity. The term structure from a network is its subject, so this lecture
  cross-references it rather than competing with it.

## Trap: Botha 2021 is two documents

The vault registers `botha-2021-recovery-timing-thesis` separately from the Botha et al.
paper. The $g_0$ recovery measure is the paper; the worst-ever aggregation discussion is
the dissertation. Pin which document each claim comes from before citing it.

## Data verdict, already checked

The empirical spine is Bondora, through S1's expansion, and the reasoning is worth
carrying because it contradicts a sentence in lecture 1.

`data/bondora_survival.parquet` holds 179,235 loans originated between 28 February 2009
and 19 July 2021, summing to 2,686,522 person-months across four countries (EE 110,714,
FI 41,955, ES 26,270, SK 296). Expanded to person-periods and indexed by calendar month
$u$, that gives roughly 150 calendar months per country, so vintage and calendar month
are no longer collinear and a macro coefficient is identified.

`data/amex_panel.parquet` is a genuine customer-month panel but it spans 1 March 2017 to
31 March 2018, which is thirteen months and no cycle at all, and its 191 columns are
anonymised so no macro variable can be named. It is therefore unusable for this lecture,
despite lecture 1 pointing at it.

Consequently lecture 1's sentence "This portfolio cannot yield a PiT PD" needs
qualifying rather than deleting: it is true of the twelve-month cross-section that
lecture 1 models, and it stops being true once the book is expanded to person-periods.
Task 8 handles that edit.

Macro series to attach, by calendar month, for EE, FI and ES: harmonised unemployment
rate, HICP inflation and real GDP growth from Eurostat. Per decision 4, download them
(Eurostat is public and free, so no confidentiality question arises) and commit the
curated extract at `credit_lectures/data/macro_eurostat.csv`, which is the one data file
in this repo that is committed rather than gitignored, because a lecture nobody can
render is worse than a 30 kB CSV in git. Say so in a comment at the top of the CSV.

---

## Task 1: research pass and a written source verdict

**Files:** create `notes/ifrs9-pit-pd-research.md`.

The comment asks for deep research. Most of it is already done inside the vault, so this
task selects and fills two gaps rather than starting from nothing.

- [ ] **Step 1.** Read every vault and guides file listed above. Take the exact titles,
      authors and years from the `_meta/sources/` registrations rather than from prose.
- [ ] **Step 2.** Write `notes/ifrs9-pit-pd-research.md` with one paragraph per method,
      each ending on a verdict. The methods to cover are the discrete-time hazard model,
      the non-stationary semi-Markov chain, beta regression on transition cells,
      multinomial logistic regression on transitions, the Cox proportional hazards model
      with time-varying macro covariates, its Andersen-Gill and
      Prentice-Williams-Peterson recurrent-event subtypes, Vasicek Z-factor scaling of a
      TTC grade PD, and the age-period-cohort decomposition.
- [ ] **Step 3.** Corroborate decision 2. The survival reading is settled, so this step
      records the evidence for it rather than choosing: find the primary usage in the
      Botha tutorial and in the guides' IFRS 9 PD methodology, quote it with a section
      reference, and flag loudly in the note if either source uses the macro reading
      instead, since the lecture would then have to say so explicitly.
- [ ] **Step 4.** Fill gap two, the FiT and FLI naming. Confirm against IFRS 9 itself,
      i.e. the standard's own wording on forward-looking information, and against the
      guides FLI methodology file. Record whether "forward in time" appears anywhere in
      the literature.
- [ ] **Step 5.** Where a search turns up a paper the vault does not hold, do not ingest
      it here. Record it in the note under a heading "For vault ingest", with title,
      authors, year and URL, so the vault's own `kb-ingest` workflow can take it with
      its required audit entry.
- [ ] **Step 6.** Commit.

```bash
git add notes/ifrs9-pit-pd-research.md
git commit -m "docs(notes): research verdict on PiT PD estimation methods"
```

**Done when** the note names every method above with a verdict, and both terminology
gaps carry a sourced answer or an explicit "no primary usage found".

## Task 2: the notation contract

**Files:** append a section to `notes/ifrs9-pit-pd-research.md`.

A fresh session will otherwise reinvent symbols that lecture 1 and the S track already
own, and a clash is the single most expensive mistake available here.

- [ ] **Step 1.** Extract the inherited symbols from `01_credit-use-case.qmd` and record
      each with its meaning: $y_{i,t}$, $D^{(k)}_i$, $D^{(k)}_{i,t}$, $g_i$, $A_i$,
      $T_i$, ${\cal W}_k$, ${\cal P}_u$, $n_u$, $\mathrm{DR}^{(k)}_u$, $\boldsymbol{X}_i$,
      $\boldsymbol{Z}_u$, $u = g_i + t$, $\lambda$, $\rho$, $\mathrm{PD}_k$.
- [ ] **Step 2.** Extract what `S1` and `S3` own, above all $l_t$, the decrements
      $d^{\rm def}_t$ and $d^{\rm set}_t$, and ${}_k p_t$. Record that $d$ alone is
      Botha's delinquency threshold from lecture 1 section 2.1 and is therefore spent.
- [ ] **Step 3.** Declare the new symbols this lecture needs and check each against the
      two lists above. The proposal is $h_{i,t}$ for the discrete hazard in month $t$,
      $S_{i,t}$ for survival to $t$, $m^{(k)}_{i,t}$ for the marginal PD of period $t+k$
      and $\mathrm{PD}^{\rm cum}_{k}$ for the cumulative PD to horizon $k$. Confirm none
      of the four appears in `credit_lectures/*.qmd` with another meaning.

```bash
grep -n 'h_{i,t}\|S_{i,t}\|m\^{(k)}' credit_lectures/*.qmd
```

- [ ] **Step 4.** Commit the appended section.

**Done when** the grep returns nothing, or every hit is accounted for in the note.

## Task 3: the lecture skeleton

**Files:** create `credit_lectures/R1_credit-ifrs9-pit-pd.qmd`.

- [ ] **Step 1.** Copy the YAML header and the provenance comment pattern from
      `credit_lectures/S2_survival-insurance-to-credit.qmd`, which is the closest
      structural match, and adjust the title, abstract and bibliography.
- [ ] **Step 2.** Write the abstract, three or four sentences, stating what the lecture
      adds to lecture 1 and naming the two conditioning axes.
- [ ] **Step 3.** Lay out the section headings with one sentence of intent under each,
      no content yet. The proposed spine is: the two conditioning axes; the term
      structure from a hazard; macro conditioning and FiT; the ECL identity this serves;
      how the estimate is actually produced, i.e. the methods review; the demonstration
      on Bondora; and what stays with the IRB lecture.
- [ ] **Step 4.** Render and confirm the skeleton comes out.

```bash
bash scripts/render_lecture.sh credit_lectures/R1_credit-ifrs9-pit-pd.qmd
open credit_lectures/R1_credit-ifrs9-pit-pd.html
```

- [ ] **Step 5.** Commit.

**Done when** the HTML renders with `lecture.css` applied and every heading present.

## Task 4: the two conditioning axes

**Files:** modify `credit_lectures/R1_credit-ifrs9-pit-pd.qmd`.

This is the section that earns the lecture. Get it right before writing anything else.

- [ ] **Step 1.** Define the discrete hazard on lecture 1's outcome, i.e.
      $h_{i,t} = \mathbb{P}(y_{i,t} = 1 \mid \text{performing at } t-1, \boldsymbol{X}_i, \boldsymbol{Z}_u)$
      with $u = g_i + t$, and state plainly that this is the conditional PD.
- [ ] **Step 2.** Build survival, the marginal PD and the cumulative PD from it, and
      show that lecture 1's $D^{(k)}_{i,t}$ flag has $\mathbb{P}(D^{(k)}_{i,t} = 1)$
      equal to the cumulative PD over the window, so the two lectures agree.
- [ ] **Step 3.** State the macro axis separately, i.e. conditioning on
      $\boldsymbol{Z}_u$ versus averaging over $\boldsymbol{Z}$, and reuse lecture 1's
      Jensen warning by reference rather than by restating it.
- [ ] **Step 4.** Add a two-by-two table crossing the survival axis against the macro
      axis, with the four cells named as the literature names them and the ambiguous
      cell flagged. This is the reader's map for the rest of the lecture.
- [ ] **Step 5.** Add the competing-risk caveat, since Bondora loans leave two ways and
      `S2` owns the Fine-Gray correction. One paragraph, pointing at S2.
- [ ] **Step 6.** Render, read it, commit.

**Done when** a reader can say which of the four cells any given PD in lecture 1 sits in.

## Task 5: macro conditioning and the ECL it serves

**Files:** modify `credit_lectures/R1_credit-ifrs9-pit-pd.qmd`.

- [ ] **Step 1.** Introduce forward-looking information with IFRS 9's own wording, then
      the course's FiT label, per decision 3, and define both on first use.
- [ ] **Step 2.** Write the scenario-weighted ECL as a formula, so the lecture states
      why a term structure is needed at all, and cite
      `concepts/ifrs9-expected-credit-loss.md`'s sources.
- [ ] **Step 3.** State the short-series design problem honestly, i.e. two or three
      cycles against dozens of candidate indicators, and name the three remedies the FLI
      article records: model averaging, blockwise design and sign-constrained regression.
- [ ] **Step 4.** Add the age-period-cohort identification argument, which is what
      answers lecture 1's collinearity complaint, and cite Breeden (2016).
- [ ] **Step 5.** Render, commit.

## Task 6: the methods review with a verdict on each

**Files:** modify `credit_lectures/R1_credit-ifrs9-pit-pd.qmd`.

- [ ] **Step 1.** Write one subsection per method, in the order of task 1 step 2, each
      giving the estimator in notation from the contract, then what it buys, then what it
      costs. The comment asks for pros and cons, so no method escapes without both.
- [ ] **Step 2.** Add the comparison table, one row per method, columns for the unit of
      observation, whether macro conditioning is native, whether competing risks are
      handled, whether recurrent defaults are handled, and the data the method demands.
      Design it against `~/.claude/rules/html-design.md`, i.e. numeric columns marked
      `.num` in header and body, a `<caption>` naming the basis, and no fills.
- [ ] **Step 3.** State the empirical ordering the Botha work reports, i.e. multinomial
      logistic beating beta regression beating a plain Markov chain, and that
      time-to-first-default and Prentice-Williams-Peterson perform comparably while
      Andersen-Gill underperforms. Attribute each to its paper and section.
- [ ] **Step 4.** Cross-reference `S1` and `S3` where they already own a method, rather
      than re-deriving it.
- [ ] **Step 5.** Render, commit.

**Done when** every method carries a con as well as a pro, and every performance claim
carries a paper and a section.

## Task 7: the demonstration on Bondora

**Files:** modify `credit_lectures/R1_credit-ifrs9-pit-pd.qmd`; possibly create
`credit_lectures/data/macro_eurostat.csv` per the data decision above.

- [ ] **Step 1.** Reuse S1's expansion. Read it out of
      `credit_lectures/S1_credit-survival-bridge.qmd` and keep the exposure convention
      identical, since a silent difference makes the two lectures disagree.
- [ ] **Step 2.** Add a calendar-month column $u$ to the person-period frame and
      aggregate to $\mathrm{DR}^{(12)}_u$, giving lecture 1's series from real data.
      Plot it, with the count of loans at risk beneath, since a rate on a thin risk set
      is noise.
- [ ] **Step 3.** Attach the macro series by country and month, then fit two discrete
      hazard models, one without $\boldsymbol{Z}_u$ and one with it, and report the
      coefficient, its sign and whether the sign is economically plausible.
- [ ] **Step 4.** Show the resulting term structure for two contrasting macro paths, so
      the reader sees the point-in-time behaviour rather than reading about it.
- [ ] **Step 5.** State the limitations plainly: Bondora is a P2P book with a
      concentrated country mix and its own selection story, the macro series are
      national rather than borrower-specific, and the 2020 pandemic months sit inside
      the window.
- [ ] **Step 6.** Restart and render clean, then commit.

```bash
bash scripts/render_lecture.sh credit_lectures/R1_credit-ifrs9-pit-pd.qmd
```

**Done when** the lecture renders top to bottom from a clean state with no error, and
every figure has a caption stating its basis.

## Task 8: trim lecture 1 to a brief mention

**Files:** modify `credit_lectures/01_credit-use-case.qmd` lines 676 to 830.

The comment says the section is too large for lecture 1, so lecture 1 has to get smaller.

- [ ] **Step 1.** Keep the PiT and TTC definitions, the $D^{(k)}_{i,t}$ generalisation
      and the $\mathrm{DR}^{(k)}_u$ definition, since later sections of lecture 1 use
      them.
- [ ] **Step 2.** Move the Jensen trap, the two TTC representations and the collinearity
      discussion into the new lecture, leaving one sentence and a forward reference in
      their place.
- [ ] **Step 3.** Qualify "This portfolio cannot yield a PiT PD" so it says what is
      true, i.e. that the twelve-month cross-section cannot, and point at the new
      lecture for what the expansion recovers.
- [ ] **Step 4.** Replace the `amex_panel.parquet` sentence, since the thirteen-month
      span makes it wrong.
- [ ] **Step 5.** Re-render lecture 1 and diff the computed outputs. A re-render is
      known safe: on 1 September 2026 all 58 computed output lines reproduced
      identically, the only diff being two statsmodels summary timestamps.
- [ ] **Step 6.** Commit lecture 1 separately from the new lecture, since they are two
      concerns.

**Done when** lecture 1's callout is under a third of its current length and every
symbol it still uses is still defined in it.

## Task 9: record the lecture in the repo's own documentation

**Files:** modify `CLAUDE.md`; modify `notes/lecture-1-review-comments-2026-09-01.md`.

- [ ] **Step 1.** Add the lecture to the `credit_lectures/` row of the key directories
      table in `CLAUDE.md`, following the wording already used for the S track, and say
      which data it reads.
- [ ] **Step 2.** Mark round 3 comment 1 as answered in the review note, with one
      paragraph on how, matching the "How each was answered" pattern already there.
- [ ] **Step 3.** Commit.

**Done when** a fresh session reading `CLAUDE.md` alone can tell what the lecture is and
what it reads.
