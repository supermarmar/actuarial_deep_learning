# Research verdict: what epidemiology has built for the interaction problem

Written 2 September 2026 for `credit_lectures/C1_credit-interaction-and-causation.qmd`,
executing task 1 of `notes/plans/03-causal-inference-lecture.md`. The plan answers review
comment 3 of round 3 on credit lecture 1, which asked for deep research into how the medical
statistics field handles interactions, covariates and causation, for the results to enter the
vault, and for a separate lecture to come out of it.

Every citation below was resolved against PubMed's own MEDLINE record or, where the journal
is not MEDLINE-indexed, against the Crossref metadata and then the article PDF itself. The
plan warned that the candidate list came from recall and had to be treated as hypothesis, and
that warning earned its keep: one item's title was wrong in the plan, one candidate turned out
to have an open-access technical companion that is better suited to our purposes than the
paper the plan named, and one item was found only under a title nobody would guess.

## Step 1: what the vault already covers, so the ingest adds rather than repeats

`~/Documents/Repos/vault/wiki/methods/causal-inference.md` is a 61-line article drawing on
Hernán and Robins alone, registered as `hernan-robins-2025-causal-inference-what-if` at T5
(`doc_type: textbook`). It already carries four things the new lecture needs and must not
re-derive.

Firstly, it states the three identification conditions and gives each a credit reading:
exchangeability, positivity (with the observation that a model driver violates it silently
when a segment has no variation in it), and consistency. Secondly, it separates the three
threats by causal structure, so confounding is a common cause, selection bias is conditioning
on a common effect, and measurement bias is error in the recorded variables. Thirdly, it
notes that chapter 18 treats variable selection as a causal question rather than a predictive
one, because a variable chosen for predictive lift can be the collider that introduces bias.
Fourthly, it covers target trial emulation and the treatment-confounder feedback problem.

Consequently the ingest gap is specific rather than general. The vault has the framework and
none of the operational machinery. It has no article on interaction against effect
modification, nothing on the scale-dependence of an interaction claim, nothing on the backdoor
criterion as a derivation rather than a taste, nothing on how large a collider bias actually
is next to a classical confounding bias, nothing on what a regression coefficient table may be
read as, and nothing on sensitivity analysis for unmeasured confounding. Those six gaps are
what the core set below fills, and each is admissible under the vault's inclusion criteria
because none is a near-duplicate of the existing article.

One correction to the plan. Task 2 step 4 predicted `reputation_tier: T4` "matching the Botha
journal-article registrations", which is the right answer reached by the wrong route, since
those Botha entries are arXiv preprints. Reading `wiki/_meta/schemas/reputation-tiers.md`
directly, the tier table assigns `journal-article` and peer-reviewed `working-paper` to T4,
and a `textbook` to T5. Every item below is a peer-reviewed journal article except the
encyclopedia entry, so T4 is correct on the schema's own terms.

## Step 2: verification, item by item

Author lists, years, journals, volumes, pages and DOIs are as printed in the MEDLINE record.
PMIDs are given so any of these can be re-checked in one call.

| Item as the plan named it | Verdict | Verified citation |
|---|---|---|
| Westreich and Greenland, "The Table 2 fallacy", *AJE*, ~2013 | **Verified** | Westreich D, Greenland S. "The table 2 fallacy: presenting and interpreting confounder and modifier coefficients." *Am J Epidemiol.* 2013 Feb 15;177(4):292-8. doi:10.1093/aje/kws412. PMID 23371353. PMC3626058 |
| VanderWeele, "On the distinction between interaction and effect modification", *Epidemiology*, ~2009 | **Verified** | VanderWeele TJ. "On the distinction between interaction and effect modification." *Epidemiology.* 2009 Nov;20(6):863-71. doi:10.1097/EDE.0b013e3181ba333c. PMID 19806059. Two published errata, 2010 and 2011 |
| VanderWeele and Knol, "A tutorial on interaction", *Epidemiologic Methods*, ~2014 | **Verified** | VanderWeele TJ, Knol MJ. "A Tutorial on Interaction." *Epidemiol Methods.* 2014;3(1):33-72. doi:10.1515/em-2013-0005. Not MEDLINE-indexed, so verified via Crossref and then against the PDF's own title page |
| Knol and VanderWeele on presenting analyses of effect modification, ~2012 | **Verified** | Knol MJ, VanderWeele TJ. "Recommendations for presenting analyses of effect modification and interaction." *Int J Epidemiol.* 2012 Apr;41(2):514-20. doi:10.1093/ije/dyr218. PMID 22253321. PMC3324457 |
| Rothman on sufficient causes, ~1976 | **Verified, title corrected** | Rothman KJ. "Causes." *Am J Epidemiol.* 1976 Dec;104(6):587-92. doi:10.1093/oxfordjournals.aje.a112335. PMID 998606. The plan's description was right and its implied title was not; the sufficient-cause paper is called simply "Causes". The adjacent synergy paper is Rothman 1974, *AJE* 99(6):385-8, doi:10.1093/oxfordjournals.aje.a121626 |
| Greenland, Pearl and Robins, "Causal diagrams for epidemiologic research", *Epidemiology*, ~1999 | **Verified** | Greenland S, Pearl J, Robins JM. "Causal diagrams for epidemiologic research." *Epidemiology.* 1999 Jan;10(1):37-48. PMID 9888278. The MEDLINE record carries no DOI, so the PMID and the UCLA technical report number R-251 are the durable identifiers |
| Greenland on classical confounding against collider-stratification bias, ~2003 | **Verified** | Greenland S. "Quantifying biases in causal models: classical confounding vs collider-stratification bias." *Epidemiology.* 2003 May;14(3):300-6. PMID 12859030. No DOI in the MEDLINE record |
| Hernán, Hernández-Díaz and Robins, "A structural approach to selection bias", *Epidemiology*, ~2004 | **Verified** | Hernán MA, Hernández-Díaz S, Robins JM. "A structural approach to selection bias." *Epidemiology.* 2004 Sep;15(5):615-25. doi:10.1097/01.ede.0000135174.63482.43. PMID 15308962 |
| VanderWeele and Ding on the E-value, *Annals of Internal Medicine*, ~2017 | **Verified** | VanderWeele TJ, Ding P. "Sensitivity Analysis in Observational Research: Introducing the E-Value." *Ann Intern Med.* 2017 Aug 15;167(4):268-274. doi:10.7326/M16-2607. PMID 28693043 |
| Hernán and Robins, "Using big data to emulate a target trial", ~2016 | **Verified** | Hernán MA, Robins JM. "Using Big Data to Emulate a Target Trial When a Randomized Trial Is Not Available." *Am J Epidemiol.* 2016 Apr 15;183(8):758-64. doi:10.1093/aje/kwv254. PMID 26994063. PMC4832051 |

Nothing failed verification, so nothing is dropped on citation grounds. Two items were added
during the search and both earn a place.

- **Ding P, VanderWeele TJ. "Sensitivity Analysis Without Assumptions." *Epidemiology.* 2016
  May;27(3):368-77. doi:10.1097/EDE.0000000000000457. PMID 26841057. PMC4820664.** This is the
  technical paper behind the E-value, it derives the bounding factor the 2017 article
  packages, and it is the only item on the whole list that is genuinely open access
  (CC BY-NC-ND). Since the 2017 *Annals* paper is paywalled, this is the source the vault can
  actually hold for the sensitivity-analysis material.
- **Greenland S, Pearl J. "Causal Diagrams." In: Boslaugh S, ed. *Encyclopedia of
  Epidemiology.* Thousand Oaks, CA: Sage; 2007:149-156. UCLA technical report R-332.** Eight
  pages by two of the three authors of the 1999 paper, covering paths, colliders, blocking and
  d-separation, hosted by Pearl on his own technical report series with a full text layer.
  Verified from the reprint's own header line.

### Availability, which decides what task 2 can hold

The plan told task 2 to prefer an open-access version and to record a stub rather than work
around a paywall. Applying that rule splits the list cleanly, and the split matters enough to
record here rather than leave to the ingest.

Seven documents are obtainable legitimately. Four are free to read on PMC as NIH public-access
deposits (Westreich and Greenland 2013, Knol and VanderWeele 2012, Hernán and Robins 2016, and
Ding and VanderWeele 2016, the last being the only one in the bulk open-access subset). Two
are author-hosted: VanderWeele and Knol 2014 as a 40-page PDF on the Harvard Chan School's
site, and Greenland and Pearl 2007 as UCLA R-332. One, Greenland, Pearl and Robins 1999, is
author-hosted as UCLA R-251 but is a scanned reprint with no text layer, so it needs OCR;
`tesseract` is installed locally and a test page came back clean on the prose, with only the
figure labels garbled.

Four are paywalled and become stubs: VanderWeele 2009, Greenland 2003, and Hernán,
Hernández-Díaz and Robins 2004, all behind Lippincott's *Epidemiology*, plus VanderWeele and
Ding 2017 behind *Annals*. Rothman 1976 is also paywalled and stays off the core list, where
the plan already placed it as a secondary item.

The loss is smaller than the count suggests, because each paywalled item has an obtainable
substitute for the specific idea the lecture needs. VanderWeele and Knol 2014 treats the
interaction against effect modification distinction across forty pages, which covers
VanderWeele 2009. Greenland and Pearl 2007 treats colliders and blocking, and the
Hernán-Robins textbook chapter 8 treats selection bias as conditioning on a common effect,
which between them cover Greenland 2003 and Hernán et al. 2004. Ding and VanderWeele 2016
derives the bounding factor, which covers VanderWeele and Ding 2017. Hence seven obtainable
documents sit inside decision 5's six-to-eight range and no lecture section is left without a
source it can cite.

## Step 3: what each core item says, and the credit translation

**Westreich and Greenland 2013, the Table 2 fallacy.** It is common to present multiple
adjusted effect estimates from one model in one table, and the paper uses causal diagrams to
show why that invites error. Three distinct problems are identified. The reader confuses a
direct-effect estimate with a total-effect estimate for the covariates; a covariate's
coefficient can be confounded even where the main exposure's coefficient is not; and
heterogeneity of the exposure effect across covariate levels complicates every coefficient in
the table. Their remedy is to distinguish total from direct effects explicitly, and to fit
multiple models where total effects for the covariates are actually wanted.

> Credit translation: a scorecard's coefficient table is exactly the object this paper is
> about, and the adjustment set that identifies the coefficient a modeller cares about does
> not identify the others sitting beside it in the same table.

**VanderWeele and Knol 2014, a tutorial on interaction.** Forty pages covering interaction on
the additive and the multiplicative scale using risks, the relation of each to the linear,
log-linear and logistic model, and the arguments for choosing one scale over the other. It
then treats presentation, mechanistic forms of interaction, when interaction is robust to
unmeasured confounding, continuous outcomes, crossover interaction, attribution of effects to
interaction, case-only estimators, and power.

> Credit translation: every PD model in this course is fitted on a logit, so a model with no
> interaction term still carries interaction on the risk-difference scale, and the claim "there
> is no interaction in this model" is a statement about a scale the modeller has usually left
> unstated.

**VanderWeele 2009, interaction against effect modification.** Both concepts are defined
inside the counterfactual framework and then separated. Interaction concerns the effects of
two interventions. Effect modification concerns one intervention's effect varying across
strata of a second variable. Either can be present without the other, some settings permit
assessing one and not the other, and the paper characterises where the two coincide.

> Credit translation: a credit modeller who says two covariates interact almost always means
> effect modification, because nobody intervenes on a borrower's country of residence, and the
> distinction decides what the finding licenses.

**Greenland, Pearl and Robins 1999, causal diagrams, with Greenland and Pearl 2007 alongside
it.** The 1999 paper introduces directed acyclic graphs to epidemiology, with paths, colliders
and the criteria for reading confounding off a graph. The 2007 encyclopedia entry restates the
machinery compactly: a variable is a collider on a path where the path enters and leaves it
through arrowheads, paths are open at non-colliders and closed at colliders, and the
moralisation rules let a reader decide by inspection which conditioning sets block which paths.

> Credit translation: the backdoor criterion turns "which variables do I control for" from a
> matter of taste into a derivation, which is what a validator needs when a model owner
> defends an adjustment set by saying it improved the Gini.

**Greenland 2003, confounding against collider-stratification bias.** Stratifying on a
variable affected by the exposure has long been known to create selection bias, and the paper
adds the quantitative comparison: under simple causal models it examines how large a
collider-stratification bias is next to a classical confounding bias. Its finding is that
stratifying on a variable affected by both exposure and disease produces a bias often
comparable in size with the bias from failing to stratify on a common cause, while other
collider-stratification biases tend to be much smaller.

> Credit translation: this is the quantitative argument against throwing every available field
> at a scorecard, and its magnitude result is what stops the argument being dismissed as a
> theoretical curiosity.

**Hernán, Hernández-Díaz and Robins 2004, a structural approach to selection bias.** The paper
argues that the many things epidemiology calls selection bias share one causal structure,
namely conditioning on a common effect of two variables, one being the exposure or a cause of
it and the other being the outcome or a cause of it. Inappropriate control selection and
informative censoring both reduce to that structure, as does adjustment for variables affected
by prior exposure. The classification then separates biases from conditioning on common
effects from biases arising from common causes.

> Credit translation: this is the cleanest available account of what is actually wrong with
> fitting a scorecard on accepted applicants only, because acceptance is a common effect of
> the application characteristics and the lender's own risk view.

**Ding and VanderWeele 2016 and VanderWeele and Ding 2017, the E-value.** The E-value is the
minimum strength of association, **on the risk ratio scale**, that an unmeasured confounder
would need with both the treatment and the outcome to explain away an observed
treatment-outcome association, conditional on the measured covariates. The 2016 paper derives
the bounding factor behind it without assuming the confounder is binary, without assuming no
exposure-confounder interaction, and without assuming a single confounder, and shows the bound
is no more conservative than earlier methods that do make those assumptions. The 2017 paper
proposes that the E-value be reported for the observed estimate and for the confidence limit
nearest the null.

> Credit translation: this is a sensitivity analysis a credit validator can actually run and
> report, and it converts "there might be an omitted variable" from an unanswerable objection
> into a number.

**Hernán and Robins 2016, target trial emulation.** A causal analysis of observational data is
framed as an attempt to emulate the randomised trial that would have answered the question,
and observational studies are then criticised by how well they emulate that trial. The
framework fixes eligibility, the strategies compared, the start of follow-up, and the outcome.

> Credit translation: already covered in the vault article, so it enters the lecture as the
> discipline that makes a causal question about a model change answerable, and it stays short.

### One trap the plan does not carry, recorded before it bites

The E-value is defined on the risk ratio scale, which the 2017 abstract states in those words.
Lecture 1's GLM3 is a logit fit and yields odds ratios, and on a book whose country default
rates run from 17 to 55 per cent an odds ratio is nowhere near the corresponding risk ratio.
Therefore task 6 must feed the E-value a risk ratio computed from the standardisation in step
4, or state the odds-ratio approximation explicitly where it uses one. Passing an odds ratio
in silently would produce a number that looks like an E-value and is not one.

## Step 4: the ideas the lecture is built on, in priority order

1. **The Table 2 fallacy, on lecture 1's own GLM3 table.** This is the section with the best
   chance of changing how a reader looks at their own model documentation, and Bondora supplies
   the table for free. Westreich and Greenland 2013 carries it.
2. **Interaction is scale-dependent, and the scale is usually unstated.** A logit fit with no
   interaction term still shows unequal risk differences by stratum, and one short table
   settles it arithmetically. VanderWeele and Knol 2014 carries it, with VanderWeele 2009 for
   the interaction against effect modification separation that comes first.
3. **The backdoor criterion against the collider trap.** Confounders, mediators and colliders
   are three roles rather than one category of "control variable", and lecture 1 already has a
   confounder (`Country`) and a mediator (`Interest`) on screen without naming either.
   Greenland, Pearl and Robins 1999 and Greenland and Pearl 2007 carry the machinery, Greenland
   2003 carries the magnitude, and Hernán et al. 2004 carries the reject-inference reading.
4. **Standardisation as the route from conditional estimates to a marginal one.** Averaging the
   country-conditional model over the observed country distribution is precisely the operation
   lecture 1 says cannot be done by combining marginal rates, so it is the arithmetic that obeys
   lecture 1's warning instead of repeating it. The Hernán-Robins textbook chapter 13 carries
   it, and it is already in the vault article.

The E-value sits fifth, as the closing honesty section rather than a pillar, and fairness sits
sixth as one section per decision 4.

## Step 1 of task 3: notation, and the boundary

**Notation.** The lecture uses Hernán and Robins' counterfactual notation, so $Y^{a}$ is the
outcome under intervention $a$, and it maps onto lecture 1's symbols directly. Lecture 1's
response is $D^{(k)}_i$, the $k$-month default indicator for loan $i$, and its covariate vector
is $\boldsymbol{X}_i$. Hence the counterfactual default indicator is written
$D^{(k),\,a}_i$, meaning the $k$-month default indicator loan $i$ would have shown under
intervention $a$ on the covariate under discussion. `do`-notation is deliberately excluded,
even though Greenland and Pearl 2007 uses graph vocabulary throughout, because the vault
article already speaks Hernán and Robins and two notations for one idea costs more than either
one saves. Where the lecture needs to say "intervene", it says so in words and reserves the
superscript for the outcome.

**Boundary.** `C1` owns whether a covariate belongs in the model and what its coefficient may
be read as. Lecture 1 owns the demonstration that composition can flip a marginal gradient,
and it keeps its section 3.1 intact, gaining only a forward reference. Lecture 6 owns how a
covariate enters a model once the decision to include it has been taken, meaning encodings,
target encoding, leakage and embeddings, so the two lectures meet without overlapping: lecture
6 asks how, and `C1` asks whether. The deferred `C2` will own attribution read causally,
covering SHAP, LocalGLMnet and ICE marginal effects against the Table 2 fallacy, and it belongs
beside the course's LocalGLMnet lectures rather than here.

## What the ingest actually produced, recorded 2 September 2026

Task 2 is done, committed in the vault as `cb5d289` on `feat/ingest-causal-inference-epi`.
Eleven sources are registered at T4 and `kb-lint` reports zero broken citations and zero broken
wikilinks across 477 articles.

Three articles rather than the two decision 5 anticipated. The reason is the length envelope
rather than a change of mind: loading `methods/causal-inference.md` with both the
coefficient-reading material and the sensitivity material took it to 1,127 prose words against
the profile's 800-word envelope, so the sensitivity analysis was split out under the profile's
own decomposition rule. The result is `methods/interaction-and-effect-modification` at 802
words, `methods/adjustment-set-selection` at 824, `methods/unmeasured-confounding-sensitivity`
at 656, and the hub at 886. Three of the four carry the soft long-article warning, and none was
cut further, since shaving cited prose to clear a soft threshold costs more than the warning
does. The Table 2 fallacy went into the adjustment-set article rather than the hub, because its
mechanism is a claim about adjustment sets and the paper itself argues it with causal diagrams.

Two things the ingest turned up that change what the lecture can say.

**The scale result is stronger than the plan assumed.** Section 1.5 of VanderWeele and Knol was
read directly rather than taken from the abstract, and it states that provided both exposures
affect the outcome there will always be interaction on at least one scale, so the only way to
have none on any scale is for one exposure to have no effect at all. Hence "this model carries
no interaction" is always a claim about one scale, and a model whose covariates all matter
carries interaction somewhere by construction. The same section reports that in a random sample
of 25 cohort and 50 case-control studies from the five highest-ranked epidemiology journals,
61 per cent assessed interaction and exactly one reported an additive measure. That is a
better opening for section 3 of the lecture than the scale-dependence claim alone.

**The E-value has an obtainable worked example with real numbers.** Ding and VanderWeele's
illustration takes the Hammond and Horn smoking study, observed relative risk 10.73 with a
95 per cent interval of 8.02 to 14.36, and grants Fisher's hypothetical genetic confounder at
the Cornfield strength of 10.73 on both arms. The joint bounding factor is then 5.63, so the
corrected estimate is 1.91 and the corrected interval 1.42 to 2.55, which still excludes one.
The lecture can show the arithmetic on a case the reader already believes before applying the
same bound to Bondora.

**Four sources are paywalled and are registered as `not-ingested` stubs**, namely VanderWeele
2009, Greenland 2003, Hernán et al. 2004 and VanderWeele and Ding 2017. Requests sit in
`vault/raw/_ingest-2026-09-02_manual-downloads-outstanding.md`. Every claim the wiki cites to
one of them traces to the published abstract, and each citing article says so in
`fact_check_notes`. The lecture inherits that limit and must attribute those claims to the
abstract in the same way, above all Greenland 2003's magnitude comparison, which has no
substitute anywhere on the list.

## The two checks run before writing, 2 September 2026

Both were run ahead of task 6 rather than inside it, because either could have changed the
lecture's shape.

### Positivity holds, with a caveat at the tails

The plan warned that standardising across EE, FI and ES might come out unstable on thin cells,
and told the lecture to report that rather than reach for a tidier number. It does not come out
unstable. All fifteen country-by-pooled-income-quintile cells are populated, and the thinnest is
Finland's bottom quintile at 630 loans against Estonia's bottom quintile at 30,218. The risk set
splits 58.1 per cent Estonia, 24.2 per cent Finland and 17.7 per cent Spain over 148,437 loans.

The caveat is at the ends rather than in the middle. Log-income runs from a first percentile of
5.72 in Estonia, 6.62 in Finland and 6.31 in Spain, so the bottom of the pooled range is
essentially Estonian and the top is essentially Finnish. Standardising over the pooled fifth to
ninety-fifth percentile therefore extrapolates each country's fitted model outside its own
support at both ends, which is positivity failing quietly rather than loudly. The lecture states
the common-support region and shows the curve both ways.

### The standardisation flips the sign, which is the whole point

Refitting lecture 1's GLM3 gives a log-income coefficient of -0.0766, an odds ratio of 0.926,
against country coefficients of +1.905 for Spain and +1.253 for Finland on the logit scale.
Averaging the country-conditional model over the observed country distribution across the
pooled fifth to ninety-fifth percentile of log-income gives a standardised default probability
falling monotonically from 29.8 to 27.2 per cent, a change of -2.6 percentage points. The raw
pooled empirical curve over the same grid rises from 20.1 to 27.9 per cent, a change of
+7.8 points. Same data, same range, opposite sign.

Two further observations worth a paragraph each in the lecture. The standardised income effect
is small next to the country effect, so the honest reading is that income matters and country
dominates. And lecture 1's claim that the rate falls with income within every country holds on
**within-country** quintiles (Estonia 18.6 to 16.6, Finland 39.5 to 31.5, Spain 59.1 to 47.4)
while on **pooled** quintiles Finland's gradient is a hump, rising from 34.3 through 40.3 before
falling to 35.7. Nothing is wrong with either computation; the banding is doing the work, which
is a useful aside on how a stratified result depends on how the strata were cut.

## Notation, settled before task 4

One rule, stated because the plan's task 3 anticipated the ambiguity and the lecture's three
graph arguments are where it would surface.

- **An estimand is written with the counterfactual superscript.** $D^{(k),\,a}_i$ is the
  $k$-month default indicator loan $i$ would have shown under intervention $a$, mapping onto
  lecture 1's $D^{(k)}_i$ and $\boldsymbol{X}_i$.
- **Identification is argued on the graph**, in the vocabulary of Greenland and Pearl: paths,
  arrowheads, colliders, blocking, and conditioning sets.
- **"Adjust for `Country`" is never written as an intervention on `Country`.** It is conditioning
  on a set that blocks a backdoor path. Keeping those two apart is the whole content of the
  interaction against effect modification distinction, so the notation has to respect it.
- **No `do`-notation**, per the plan.
