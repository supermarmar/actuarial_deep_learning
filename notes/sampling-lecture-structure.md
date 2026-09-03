# Lecture R3: citation register and notation bridge

Working note for `credit_lectures/R3_credit-sampling-and-representativeness.qmd`. It records
which claims were verified by direct read, which were corrected during verification, and which
symbols the lecture may and may not use.

Read this before editing `R3`. Everything settled here is settled, and re-deriving it costs
more than reading it. The lecture was built on 3 September 2026 and the results it produced are
recorded at the foot of this note.

## Confidentiality, applied

The A-IRB material in the guides repo derives from a real engagement, so this note inherits the
bar `notes/irb-lecture-structure.md` sets: **structure, regulatory references and transferable
method travel, and no portfolio specific does.**

Left behind entirely, and deliberately not itemised further: the source portfolio's COVID
exclusion dates, its master reference data start date, its snapshot calendar, its acquisition
and strategy-change history, its segment volumes, its stratification scheme and its observed
diagnostic values. Bondora carries every worked example.

One consequence bites this lecture specifically. The guides' representativeness variable
battery (utilisation bands, credit limit bands, revolver against transactor, bureau score
bands) describes the source portfolio, so it does not travel. Section 8 uses Bondora's own
columns: `Rating`, `Country`, banded `Age`, banded `DebtToIncome`, banded `IncomeTotal`,
`NewCreditCustomer`, `UseOfLoan` and `VerificationType`.

## Verified by direct read, 3 September 2026

Every row below was read from the primary file named, not from a subagent summary.

| Claim | Source | Verdict |
|---|---|---|
| Training data must be representative of the actual obligor population | CRR Art. 174(c) | VERIFIED verbatim |
| Model documentation must establish out-of-time **and** out-of-sample tests | CRR Art. 175(4)(b) | VERIFIED verbatim |
| Retail observation period floor of five years | CRR Art. 180(2)(e) | VERIFIED verbatim |
| Institutions must identify and analyse seasoning effects | CRR Art. 180(2)(f) | VERIFIED verbatim |
| Overlapping one-year windows require a documented over-weighting bias analysis | PRA SS4/24 ¶11.10(c) | VERIFIED verbatim |
| SS4/24 section 8 is titled "Data representativeness" | `vault/wiki/regulation/pra-ss4-24-irb-approach-2026.md:50` | VERIFIED |
| Simple random clustered sampling, grouped by loan ID, with `s_f` = 70% | Botha and Verster (2025) tutorial, p. 15 | VERIFIED verbatim |
| Weighted logistic regression at a default weight of ten, tuned on the empirical rate | same, p. 23 | VERIFIED verbatim |
| Imbalance correction harms calibration without improving AUC | van den Goorbergh et al. (2022) abstract | VERIFIED verbatim |
| ROC misleads under imbalance through "an intuitive but wrong interpretation of specificity", whereas the precision-recall plot measures the fraction of true positives among positive predictions | Saito and Rehmsmeier (2015) abstract | VERIFIED verbatim |

CRR text is `vault/raw/eba/CRR_2013_EN_TXT.pdf`, extracted with `pdftotext -layout`. Note that
the two-column layout interleaves columns under plain `pdftotext`, which is how Art. 175(4)(b)
first looked like a limb of Art. 174. Use `-layout` and cut the column.

## Four corrections that verification forced

1. **The representativeness anchor is not Article 179.** The brief paired representativeness
   with CRR Art. 179. The guides material never makes that pairing, and the black-letter text
   settles it: Art. 174(c) carries the development-against-application comparison, whereas
   Art. 179(1)(b) requires estimates representative of *long-run experience*, which is the
   cycle-coverage argument the R2 lecture already owns.

2. **Article 180(2)(e) does not require good and bad years.** It sets a bare five-year floor
   and says nothing about an economic cycle. The guides material attributes the cycle-breadth
   requirement to it, and that attribution is wrong; the requirement sits in EBA/GL/2017/16.
   Cite Art. 180(2)(e) for the floor alone. Its final sentence is worth quoting for a different
   reason: "An institution need not give equal importance to historic data if more recent data
   is a better predictor of loss rates." That is explicit permission to down-weight old
   vintages, and the series has never mentioned it. It earns a place in section 6 rather than
   only in this list, because it is the regulation's own answer to the tension that section
   sets up: excluding a distorted window costs cycle coverage, and weighting is the
   alternative to a binary keep-or-drop.

3. **The PSI thresholds are contested, so do not state 0.10 and 0.25 as settled.** The vault
   records the disagreement as an open question in `methods/bureau-score-substitution.md:44`.
   Bhalla (2015) gives 0.10 and 0.20; Du Pisanie, Allison and Visagie (2022) give 0.10 and 0.25
   with simulation justification, registered at T4. The lecture states both, names the
   disagreement, and notes that the higher bound has the better statistical argument and the
   weaker claim to standard practice.

4. **Article 175(4)(b) is the anchor section 2 actually wanted, stated precisely.** The plan
   argued that out-of-sample and out-of-time test different things and neither substitutes for
   the other, sourcing it from the guides. The CRR names both in black letter, and neither the
   guides nor the series cites it. However, the article sits under *Documentation of rating
   systems* and obliges the documentation to "establish a rigorous statistical process
   including out-of-time and out-of-sample performance tests for validating the model". So the
   lecture says what the article says, i.e. that the documentation must establish both tests,
   rather than inflating it into a general testing mandate.

## Not verified, and how the lecture handles it

- **CRR3 renumbering.** Regulation (EU) 2024/1623 restructured the IRB chapter from 1 January
  2025 and I could not confirm whether Arts. 174, 175 and 180 were renumbered. The UK retained
  CRR keeps the numbering unchanged as at 2 September 2026. The lecture cites the original
  numbering, states that CRR3 amended the chapter, and points the reader at the EUR-Lex
  consolidated view rather than asserting current EU numbering.
- **SS4/24's operative date.** The January 2026 consolidated version takes effect 1 January
  2027 alongside PS1/26, so it is the PRA's published position rather than a binding rule at
  the time of writing. Say so where ¶11.10(c) is cited.

## Sources the lecture should carry

| Citation | Role | Tier or provenance |
|---|---|---|
| CRR Arts. 174(c), 175(4)(b), 180(2)(e) and (f) | Sections 2, 5, 8 | Primary regulation |
| PRA SS4/24 §8, ¶11.10(c) | Sections 5, 8 | Primary supervisory guidance |
| EBA/GL/2017/16 | The cycle-breadth requirement Art. 180 does not carry | Primary |
| Botha and Verster (2025), discrete-time survival tutorial | Sections 3, 4, 8, 9 | Journal article |
| Baesens et al. (2016, §6) | Clustered sampling, cited by Botha | Textbook |
| van den Goorbergh, van Smeden, Timmerman and Van Calster (2022), JAMIA 29(9):1525-1534 | Section 9, the central result | Peer-reviewed |
| Saito and Rehmsmeier (2015), PLOS ONE 10(3):e0118432 | Section 9, precision-recall against ROC | Peer-reviewed |
| Du Pisanie, Allison and Visagie (2022), arXiv 2206.11344 | Section 8, PSI thresholds | T4 academic |
| Bhalla (2015) | Section 8, the competing PSI threshold | Industry |
| Djurovic (2025), classifier two-sample test | Section 8, the joint-distribution test | Industry |
| Coelho and Zamil (2020), BIS FSI Brief No 8 | Section 6, payment holidays breaking the past-due signal | T3 |

Two of these were found in the vault rather than sought. The second is settled; the first is
was an open decision and was taken on 3 September 2026 in favour of including it. The deciding
argument is that the computation carries itself: the classifier separates the two samples at an
AUC of 0.9595 while most marginal indices call the covariates stable, so the finding stands on
the numbers in the lecture rather than on the authority of an industry slide deck whose vault
article is marked `reviewed: false`. Section 8.3 says exactly that in a callout, and the
classifier complements the stability index rather than replacing it.
`methods/representativeness-c2st.md` frames representativeness as a classification problem:
pool the development and out-of-time samples, label each row by its origin, and train a
classifier, whose AUC is 0.5 when the samples are indistinguishable. Permutation importance
then ranks which covariates drive the separation. That belongs in a deep learning series far
more naturally than a table of marginal PSI values, and it is directly computable on Bondora.
`_meta/sources/bis-fsi-2020-payment-holidays.md` records that mass payment holidays broke the
mapping between the past-due signal and its meaning, which is precisely the Bondora
rescheduling spike read as a measurement problem rather than a credit one.

## Notation bridge

Series notation wins. Botha's symbols are adopted only where the series has no symbol.

**Spent or rejected, and not to be reused.** $\tau$ and every subscripted form of it, since
lecture 1 fixed $\tau$ as the snapshot date and `S1_credit-survival-bridge.qmd:132` already
records the clash. Also $m$, $d$, $h$ and $S$. Botha's calendar time $t'$ is the series' $u$.

**Free, and worth adopting.** The subject-spell key $(i,j)$, the spell number $j$, the dataset
family $\mathcal{D}$, $\mathcal{D}_S$, $\mathcal{D}_T$ and $\mathcal{D}_V$, the sampling
fraction $s_f$, the portfolio size $N_p$, the event type $\psi$, the resolution rate $r_\psi$
and the observation weight $w_{ijt}$.

**One trap.** Botha's $T_{ij}$ is a spell age, whereas lecture 1's $T_i$ is time from
origination to default. The two coincide only for $j = 1$ with no left-truncation, so say so
before the recurrent-event material silently redefines an inherited symbol.

**One precision the lecture must not fumble.** Lecture 7 owns the balance property, so section
9 states it exactly: a weighted fit still satisfies $\sum_i w_i y_i = \sum_i w_i \hat\mu_i$,
and what breaks is that the weighted measure is no longer the portfolio. Botha's position
follows from that reading, since he tunes the weight until the unweighted twelve-month rate
comes right instead of correcting the intercept afterwards.


## What the build found, 3 September 2026

Five results, all computed in the lecture and none typed by hand.

**The relief distortion is two months wide.** On the Estonian, Finnish and Spanish sub-book the
monthly default hazard runs 2.90 per cent on average over the twenty-six months to February
2020, then reads 3.24 in March 2020, 2.05 in April, 1.40 in May, 2.45 in June and 3.25 in July.
May sits 57 per cent below March and the book recovers within eight weeks. The notch coincides
to the month with the rescheduling spike, where `ReScheduledOn` counts go from a baseline of
1,597 a month to 3,076 in April 2020. This is the evidence R2 asserted when it declined to
exclude the pandemic year, and it argues against the multi-year exclusions the industry used.

**The fixed-horizon table cannot express a calendar exclusion.** Excluding a distortion from
March 2020 on an overlap basis drops every loan originated from March 2019, and the out-of-time
test window opens in November 2019, so exactly 0 of 29,874 test loans survive. Excluding on
origination date leaves 21,334 whose outcome windows all close inside the pandemic.

**The exclusion is worth 2.37 per cent relative.** On R1's calendar-indexed person-period table,
dropping April and May 2020 removes 5.95 per cent of loan-months and lifts the twelve-month
probability of default for the reference profile from 18.20 to 18.63 per cent. Retaining the
relief window understates risk, which is the direction a supervisor cares about.

**A data break in July 2017.** `DebtToIncome` becomes uniformly zero and `UseOfLoan` uniformly
$-1$ from July 2017, and both persist for the remaining 110,816 loans. No fitted model in the
series uses either field, so nothing downstream is wrong, and the series had never run the
sweep that would have found it.

**The joint distribution fails where the margins pass.** Four of ten covariates have a level
absent on one side, so their stability indices are artefacts of the epsilon floor. Of the six
readable, `Rating` at 0.3521 is material and three sit below 0.03. A gradient-boosted classifier
nonetheless separates development from out-of-time at a cross-validated AUC of 0.9595, and its
strongest separator is `Amount`, whose stability index of 0.1153 only reaches the investigate
band.

## Downstream, deliberately unchanged

Lectures 2, 4/5, 6, 7 and S3 keep their published numbers. Lecture 2 gained one forward-pointing
callout and was re-rendered to confirm reproducibility: all 68 computed output lines reproduce,
the only diff being a statsmodels timestamp, which matches the lecture 1 result of
1 September 2026.

No `notes/plans/04-*.md` was written. The three existing plan files were pre-build task
breakdowns and this lecture was built in one pass, so a plan file after the fact would carry
nothing this note does not.
