# Plan 3: an interaction and causation lecture, plus the vault ingest behind it

> **For a fresh session.** This plan is self-contained and assumes no memory of the
> conversation that produced it. Read it top to bottom before touching a file. Steps
> carry checkboxes so progress survives an interruption. Repo root is
> `/Users/mervedosa/Documents/Repos/actuarial_deep_learning`; every path below is
> relative to it unless it starts with `~` or `/`. Note that this plan writes to **two
> repos**, since the vault is a separate git repository with its own conventions.

**Answers:** review comment 3 of round 3, recorded verbatim in
`notes/lecture-1-review-comments-2026-09-01.md`. The comment reads:

> The interactions and covariates and causation stuff I would like to do some deep
> research into the medical stats field to see how they deal with this - add to vault
> and plan this out as your 3rd plan this will be a seperate lecture or more

**Goal:** take lecture 1 section 3.1, which currently demonstrates Simpson's paradox on
the Bondora book and then moves on, and give it the machinery epidemiology has built for
exactly this problem. The lecture answers three questions a credit modeller asks and
usually answers by habit: which covariates belong in the model, what an interaction means
and on which scale, and what a fitted coefficient may be read as.

**Approach:** three workstreams in order. First research, because the vault holds one
article on causal inference and one source behind it, so the material genuinely has to be
found. Secondly the vault ingest the comment asks for, run through the vault's own
pipeline so every source yields either a wiki article or an audit entry. Thirdly the
lecture, whose empirical spine is the Bondora country-income confounding that lecture 1
already puts on screen, extended to a standardised marginal effect and a worked
demonstration of the Table 2 fallacy on lecture 1's own GLM3 coefficients.

**Stack:** Quarto plus the pinned `.venv` for the lecture. The vault work needs the
`doc-to-markdown` and `kb-ingest` skills and nothing from this repo.

---

## Global constraints

- Never call a system `python3`. Use `.venv/bin/python` or activate the venv first.
- Never edit a rendered `credit_lectures/*.html` by hand.
- British English throughout. No em or en dashes as punctuation. No negated counterpart
  clauses, which are banned outright. Prose carries the reasoning.
- **Verify every citation against the primary source before it enters the vault or the
  lecture.** The candidate reading list below was assembled from recall, so treat every
  author, year, journal and title in it as a hypothesis to check rather than a fact.
  Where a check fails, correct it or drop the item; never carry an unverified citation.
- The vault is a separate repo with its own commit conventions. Commit there separately
  and follow `~/Documents/Repos/vault/.claude/rules/curation-workflow.md`, which requires
  that every file entering `raw/` yields either a wiki article or an audit entry in
  `audit/`. Never silently skip a document.
- Small logical commits under Conventional Commits in both repos.

## Decisions taken, 2 September 2026

1. **File name.** `credit_lectures/C1_credit-interaction-and-causation.qmd`, on a causal
   track of its own, alongside the regulatory `R1` and `R2` from plans 1 and 2.

## Decisions taken, 2 September 2026, continued

Mario settled all four on the day the plan was written, so nothing here blocks.

2. **One lecture or two.** `C1` now, covering interaction, confounding, the adjustment
   decision and marginal against conditional effects. A follow-on `C2` is named and
   deferred, covering attribution read causally, i.e. SHAP, LocalGLMnet and ICE marginal
   effects against the Table 2 fallacy. `C2` belongs beside the course's LocalGLMnet
   lectures rather than here, so it gets its own plan when that part of the syllabus
   comes up. Task 8 records whether it was created or deferred.
3. **How far the empirical work goes.** Standardisation only. Compute the marginal income
   effect by averaging the country-conditional model over the observed country
   distribution, which is precisely the operation lecture 1 says cannot be done by
   combining marginal rates. Propensity scores and instrumental variables get named and
   defined, and are not demonstrated, because Bondora carries no treatment variable and a
   staged demonstration would teach the mechanics of a method nobody should apply here.
4. **Fairness is in scope, as one section.** A discrimination claim is a causal claim, so
   it inherits every identification condition above. Work the Bondora differential
   honestly, cite `concepts/ml-fairness.md` on why the candidate criteria cannot all hold
   at once, and resist a metrics tournament. Task 7 carries it.
5. **Ingest size.** Six to eight core papers, i.e. the items marked **core** below.
   Extend `methods/causal-inference.md` and add two new articles rather than one article
   per paper, since fewer and denser articles survive the vault's health check better.

## What ground is already taken

Read these first, so the lecture does not restate a neighbour. Note that plan 1 was
executed on 2 September 2026, adding `credit_lectures/R1_credit-ifrs9-pit-pd.qmd` and
trimming lecture 1's point-in-time callout, so every line number below is as of commit
`6303d4f` and should be confirmed with a grep before editing.

- `credit_lectures/01_credit-use-case.qmd`, section 3.1 at line 938, already
  demonstrates Simpson's paradox on Bondora: within Estonia, Finland and Spain default
  risk falls with income, while pooled it rises, because the high-income countries carry
  default rates of 38 and 55 per cent against Estonia's 17. Section 3 then runs GLM1,
  GLM2 and GLM3, where GLM3 "adds the confounder". So lecture 1 already makes a causal
  argument and never uses the word.
- Lecture 1 also argues that `Interest` is **endogenous**, being an output of the
  lender's previous risk assessment rather than a property of the borrower. That is a
  mediator argument in disguise and it is the lecture's best worked example of why an
  adjustment set has to be chosen rather than maximised.
- `credit_lectures/06_credit-covariate-engineering.qmd` owns encodings, target encoding
  and leakage, embeddings and continuous covariate treatment. It has no causal content,
  so the boundary is clean: lecture 6 asks how a covariate enters a model, and `C1` asks
  whether it should.
- `~/Documents/Repos/vault/wiki/methods/causal-inference.md` exists, is sourced from
  Hernán and Robins alone, and already covers the three identification conditions
  (exchangeability, positivity, consistency), threats and their methods, and target
  trial emulation. It is the article the new sources extend rather than replace.

## Candidate reading list, every item to be verified

Grouped by the question it answers. Items marked **core** are the recommended ingest set.
Author, year and venue are from recall and must be checked before use.

**What a coefficient may be read as**

- **core** Westreich and Greenland, "The Table 2 fallacy", *American Journal of
  Epidemiology*, around 2013. The single most transferable idea for credit risk: the
  coefficients in one regression table cannot all be read as effects of their own
  variable, because each is conditioned on the others and the adjustment set that
  identifies one does not identify another. A scorecard coefficient table is exactly the
  object the paper is about.

**What an interaction is, and on which scale**

- **core** VanderWeele, "On the distinction between interaction and effect
  modification", *Epidemiology*, around 2009. Interaction concerns two interventions;
  effect modification concerns how one effect varies across strata of a variable nobody
  intervenes on. Credit models routinely claim the first and mean the second.
- **core** VanderWeele and Knol, "A tutorial on interaction", *Epidemiologic Methods*,
  around 2014. Additive against multiplicative scale, and the result that matters here:
  a model with no interaction term on the logit scale still carries interaction on the
  risk-difference scale. Since every PD model in this course is fitted on a logit, the
  claim "there is no interaction" is scale-dependent and usually unstated.
- Knol and VanderWeele on presenting analyses of effect modification, around 2012, for
  the reporting conventions, which map onto what a validator should ask to see.
- Rothman on sufficient causes, around 1976, for interaction as mechanistic synergy.

**Which covariates belong in the model**

- **core** Greenland, Pearl and Robins, "Causal diagrams for epidemiologic research",
  *Epidemiology*, around 1999. Directed acyclic graphs and the backdoor criterion, i.e.
  the tool that turns "which variables do I control for" from taste into a derivation.
- **core** Greenland on classical confounding against collider-stratification bias,
  around 2003. Adjusting for the wrong variable creates bias rather than removing it,
  which is the argument against throwing every available field at a scorecard.
- Hernán, Hernández-Díaz and Robins, "A structural approach to selection bias",
  *Epidemiology*, around 2004. Selection bias as a collider, which is the cleanest
  account of reject inference's real problem.

**Honesty about what is left over**

- **core** VanderWeele and Ding on the E-value, *Annals of Internal Medicine*, around
  2017. How strong an unmeasured confounder would have to be to explain away an observed
  association, which is a sensitivity analysis a credit validator can actually run.
- Hernán and Robins, "Using big data to emulate a target trial", around 2016, which
  connects to the target trial section already in the vault article.

**Books, for reference rather than ingest**

- Hernán and Robins, *Causal Inference: What If*, already registered in the vault as
  `hernan-robins-2025-causal-inference-what-if`.
- Rothman, Greenland and Lash, *Modern Epidemiology*.
- Pearl, *Causality*.

**Credit-side counterparts already in the vault**, to cross-reference rather than ingest:
`methods/causal-inference.md`, `methods/block-design-regression.md`,
`methods/risk-factor-binning.md`, `methods/weight-of-evidence-encoding.md`,
`methods/ols-assumption-violations.md`, `methods/shap-model-explainability.md`,
`methods/localglmnet.md`, `concepts/interpretability-versus-post-hoc-explanation.md`,
`concepts/model-interpretability.md`, `concepts/ml-fairness.md` and
`concepts/lending-discrimination-evidence.md`.

---

## Task 1: the research pass

**Files:** create `notes/causation-research.md`.

- [ ] **Step 1.** Read `~/Documents/Repos/vault/wiki/methods/causal-inference.md` in full,
      plus its source registration at
      `_meta/sources/hernan-robins-2025-causal-inference-what-if.md`, and record what is
      already covered so the ingest adds rather than duplicates. The vault's inclusion
      criteria exclude a near-duplicate of an existing article, so this step is what
      keeps the ingest admissible.
- [ ] **Step 2.** Verify each candidate above against the primary source. Record the
      exact author list, year, journal, volume, pages, DOI and an open-access URL where
      one exists. Mark any item that fails verification and say why.
- [ ] **Step 3.** For each verified core item, write one paragraph on what it says and
      one sentence on the credit risk translation. The translation sentence is what makes
      the source worth ingesting.
- [ ] **Step 4.** Record the three or four ideas the lecture will be built on, in
      priority order. The proposal is the Table 2 fallacy, the scale-dependence of
      interaction, the backdoor criterion against the collider trap, and standardisation
      as the correct route from conditional estimates to a marginal one.
- [ ] **Step 5.** Commit in this repo.

```bash
git add notes/causation-research.md
git commit -m "docs(notes): research verdict on causal methods from epidemiology"
```

**Done when** every core item is verified with a full citation or explicitly dropped, and
each carries a credit translation.

## Task 2: the vault ingest

**Files:** in `~/Documents/Repos/vault` only. Sources into `raw/`, markdown into
`markdown/`, articles into `wiki/`, registrations into `wiki/_meta/sources/`, and any
exclusion into `audit/`.

- [ ] **Step 1.** Take the core set as the ingest scope, per decision 5, i.e. six to
      eight papers, and drop any item that failed verification in task 1.
- [ ] **Step 2.** Download each source. Every item on the core list is a journal article,
      so check for an open-access version first. Where a paper is paywalled, record it in
      `raw/_stubs` following the pattern of the existing
      `_ingest-*_manual-downloads-outstanding.md` files rather than working around the
      paywall.
- [ ] **Step 3.** Run the `doc-to-markdown` skill to convert `raw/` into `markdown/`.
- [ ] **Step 4.** Run the `kb-ingest` skill. Expect the articles to be registered with
      `issuer: academic` and `reputation_tier: T4`, matching the Botha journal-article
      registrations at `wiki/_meta/sources/botha-2025-*.md`, which are the closest
      precedent on disk.
- [ ] **Step 5.** Decide the article shape. The recommendation is to extend
      `methods/causal-inference.md` rather than create one article per paper, and to add
      two new articles where the subject genuinely stands alone: one on interaction and
      effect modification, and one on choosing an adjustment set with causal diagrams.
      Fewer, denser articles survive the vault's own health check better, and decision 5
      settles this shape.
- [ ] **Step 6.** Record an audit entry for anything downloaded and not used, per the
      curation workflow rule. Never silently skip a document.
- [ ] **Step 7.** Run `kb-lint` and fix what it reports on the new articles.
- [ ] **Step 8.** Commit in the vault repo, one commit for the ingest.

**Done when** every file that entered `raw/` has either a wiki article or an audit entry,
and `kb-lint` reports no broken wikilink or citation in the new material.

## Task 3: the notation and boundary note

**Files:** append to `notes/causation-research.md`.

- [ ] **Step 1.** Decide the causal notation. The proposal is Hernán and Robins' style,
      i.e. $Y^{a}$ for the counterfactual outcome under intervention $a$, since the vault
      article already uses that vocabulary, mapped onto lecture 1's $D^{(k)}_i$ outcome
      and $\boldsymbol{X}_i$ covariates. Check `do`-notation is not introduced as well,
      because two notations for one idea is worse than either.
- [ ] **Step 2.** Write the boundary paragraph, i.e. what `C1` owns against lecture 1,
      lecture 6 and the proposed `C2`.
- [ ] **Step 3.** Commit.

## Task 4: the lecture skeleton

**Files:** create `credit_lectures/C1_credit-interaction-and-causation.qmd`.

- [ ] **Step 1.** Copy the YAML header and provenance comment pattern from
      `credit_lectures/S2_survival-insurance-to-credit.qmd` and adjust it.
- [ ] **Step 2.** Write the abstract, three or four sentences, opening on the fact that
      lecture 1 already made a causal argument without naming it.
- [ ] **Step 3.** Lay out the headings with one sentence of intent each. The proposed
      spine is: what lecture 1's Simpson's paradox actually was; the three identification
      conditions; interaction against effect modification and the scale problem; choosing
      an adjustment set, with confounders, mediators and colliders separated; the Table 2
      fallacy on a scorecard; marginal against conditional effects and standardisation;
      how much unmeasured confounding would be needed to explain the result away; and
      what this means for a model built to predict rather than to explain.
- [ ] **Step 4.** Render, confirm, commit.

```bash
bash scripts/render_lecture.sh credit_lectures/C1_credit-interaction-and-causation.qmd
```

## Task 5: the conceptual core

**Files:** modify `credit_lectures/C1_credit-interaction-and-causation.qmd`.

- [ ] **Step 1.** Re-read lecture 1's country-income figure as a confounding structure,
      and draw the diagram, i.e. country pointing at both income and default. Use an
      inline SVG per `~/.claude/rules/html-design.md`, with the literal `#B18559` for any
      stroke, since SVG attributes cannot resolve custom properties.
- [ ] **Step 2.** State the three identification conditions on the credit problem, and
      give each a concrete failure from a credit portfolio. Positivity is the easy one,
      i.e. a segment with no variation in a driver, and consistency is the hard one,
      i.e. "reduce the interest rate" is not one intervention.
- [ ] **Step 3.** Separate interaction from effect modification with a credit example
      each, then demonstrate the scale problem numerically: take a fitted logit with no
      interaction term and show the risk differences by stratum are unequal anyway. One
      short table settles it, and it is the kind of thing a reader disbelieves until they
      see the arithmetic.
- [ ] **Step 4.** Write the adjustment-set section around three named roles, with
      `Country` as the confounder to adjust for, `Interest` as the mediator to leave out
      (which is lecture 1's endogeneity argument, now with a name), and a constructed
      collider to show what adjusting for one costs. Give the collider example real
      numbers so the sign of the induced bias is visible.
- [ ] **Step 5.** Render, commit.

**Done when** the scale demonstration and the collider demonstration both carry numbers
rather than assertions.

## Task 6: the Table 2 fallacy on lecture 1's own model

**Files:** modify `credit_lectures/C1_credit-interaction-and-causation.qmd`.

This is the section that will change how a reader looks at their own model documentation.

- [ ] **Step 1.** Refit lecture 1's GLM3 on `data/bondora_pd.parquet` and print the
      coefficient table exactly as a model document would.
- [ ] **Step 2.** Go through the table coefficient by coefficient and state, for each,
      what adjustment set would be needed to read it as an effect, and whether GLM3
      supplies it. Some will and most will not, which is the point.
- [ ] **Step 3.** State the constructive version, i.e. that a predictive model needs no
      causal reading at all and stays perfectly valid without one, and that the failure
      arises only when a coefficient is quoted as a driver in a model document or a
      credit policy discussion.
- [ ] **Step 4.** Compute the standardised marginal income effect by averaging the
      country-conditional model over the observed country distribution, and compare it
      with the raw pooled curve from lecture 1's figure. This is the arithmetic that
      shows lecture 1's warning being obeyed rather than repeated.
- [ ] **Step 5.** Add the sensitivity analysis, i.e. how strong an unmeasured confounder
      would have to be to overturn the within-country income effect, using the E-value
      method from task 1 if it verified.
- [ ] **Step 6.** Render clean, commit.

## Task 7: fairness, if in scope

**Files:** modify `credit_lectures/C1_credit-interaction-and-causation.qmd`. In scope per
decision 4, as one section only.

- [ ] **Step 1.** State the position plainly: a claim that a model discriminates is a
      causal claim, so it inherits every identification condition above.
- [ ] **Step 2.** Work the Bondora example honestly. `Gender` and `Age` are in the book,
      and the point is what a raw differential does and does not license, citing
      `concepts/ml-fairness.md` on why the candidate fairness criteria cannot all hold at
      once.
- [ ] **Step 3.** Keep it to one section and resist a metrics tournament. Render, commit.

## Task 8: connect it back, and record it

**Files:** modify `credit_lectures/01_credit-use-case.qmd`; modify `CLAUDE.md`; modify
`notes/lecture-1-review-comments-2026-09-01.md`.

Confirm the anchors first, since plan 1's execution moved them:

```bash
grep -n 'Covariates interact\|is \*\*endogenous\*\*\|lecture R1' credit_lectures/01_credit-use-case.qmd
```

Lecture 1 already carries a forward reference to `R1` at line 718. Match its wording, so
the two point forward the same way. Note also the outstanding review comment at line 981,
i.e. Mario's request for a 3D version of the kernel-smoothed figure, which sits inside the
section this task edits and is a separate change.

Lecture 1 keeps its section 3.1 intact here, unlike plans 1 and 2, because the figure is
doing work where it stands. What it gains is a forward reference.

- [ ] **Step 1.** Add one sentence at the end of section 3.1 naming the mechanism as
      confounding and pointing at `C1`.
- [ ] **Step 2.** Add one sentence to the `Interest` endogeneity paragraph naming it as a
      mediator and pointing at `C1`.
- [ ] **Step 3.** Re-render lecture 1 and diff the computed outputs. A re-render is known
      safe: on 1 September 2026 all 58 computed output lines reproduced identically, the
      only diff being two statsmodels summary timestamps.
- [ ] **Step 4.** Add `C1` to the `credit_lectures/` row of the key directories table in
      `CLAUDE.md`, naming the causal track and what the lecture reads.
- [ ] **Step 5.** Mark round 3 comment 3 as answered, one paragraph on how, and record
      that `C2` was deferred per decision 2, to be planned beside the course's
      LocalGLMnet lectures.
- [ ] **Step 6.** Commit.

**Done when** a reader of lecture 1 section 3.1 is pointed at the lecture that explains
the mechanism, and `CLAUDE.md` names the causal track.
