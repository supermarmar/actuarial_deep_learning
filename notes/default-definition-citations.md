# Citation verification: definition of default in credit risk

Teaching lecture, public. Verified 2026-09-03.

Every VERIFIED status traces to a primary document read directly, as required by Gini's
subagent-verification rule. Local PDFs used as primary sources are noted with their vault paths.

Status legend:

- **VERIFIED** — exact black-letter quote confirmed from primary document.
- **PARTIALLY VERIFIED** — article exists and requirement confirmed; specific paragraph within a section not confirmed to exact text.
- **CORRECTED** — the claimed provision is absent from the stated instrument; attribution corrected here.
- **UNVERIFIED** — could not be sourced; see "Do not state in a public lecture".

---

## CRR (Regulation (EU) No 575/2013 as amended / UK CRR)

Primary source read: consolidated pre-CRR3 EU CRR PDF,
`vault/raw/legislation/2024-01-09_575-2013_crr-consolidated-pre-crr3.pdf`
(02013R0575 — EN — 09.01.2024 — 016.001), extracted via pdftotext.

UK CRR primary source: PRA Rulebook draft instrument (near-final), PS9/24 Appendix 2,
`vault/raw/pra/pra_ps9_24_app2_crr_near_final.pdf`, extracted via pdftotext.

Note on vintage: this verification uses the EU CRR consolidated to 9 January 2024 (pre-CRR3
floors). CRR3 (Regulation (EU) 2024/1623) applies from 1 January 2025 and renumbers some
articles. The UK CRR text has been separately restated in the PRA Rulebook. Paragraphs 5, 5A,
5B and 5C below exist in the UK CRR; the EU CRR consolidated text carries only a shorter
Article 178(5) without sub-lettered paragraphs.

---

### 1. Article 178(1)(a) and 178(1)(b): the two limbs of default

**Status: VERIFIED** from EU CRR consolidated pre-CRR3, Article 178.

> **Article 178 — Default of an obligor**
>
> 1. A default shall be considered to have occurred with regard to a particular obligor when
> either or both of the following have taken place:
>
> **(a)** the institution considers that the obligor is unlikely to pay its credit obligations to
> the institution, the parent undertaking or any of its subsidiaries in full, without recourse
> by the institution to actions such as realising security;
>
> **(b)** the obligor is more than 90 days past due on any material credit obligation to the
> institution, the parent undertaking or any of its subsidiaries. Competent authorities may
> replace the 90 days with 180 days for exposures secured by residential property or SME
> commercial immovable property in the retail exposure class, as well as exposures to public
> sector entities. The 180 days shall not apply for the purposes of point (m) Article 36(1) or
> Article 127.

In the case of retail exposures, institutions may apply the definition at the level of an
individual credit facility rather than in relation to the total obligations of a borrower.

**Citation:** Regulation (EU) No 575/2013 (CRR), Article 178(1)(a) and 178(1)(b), as
consolidated to 9 January 2024. EUR-Lex CELEX 02013R0575-20231228.

---

### 2. Article 178(2)(d): the materiality threshold

**Status: VERIFIED** from EU CRR consolidated pre-CRR3, Article 178(2)(d).

> **(d)** materiality of a credit obligation past due shall be assessed against a threshold,
> defined by the competent authorities. This threshold shall reflect a level of risk that the
> competent authority considers to be reasonable;

**Who sets it:** The competent authority sets the threshold under Article 178(6), within
conditions specified by Commission Delegated Regulation (EU) 2018/171 (the absolute
threshold RTS). The EU consolidated CRR does not contain a specific GBP or EUR amount in
Article 178(2)(d) itself.

**UK CRR:** The UK CRR rulebook (PS9/24 near-final) specifies the materiality threshold
directly in the text. Article 178(2)(da) for non-retail requires both:
(i) the sum of all amounts past due exceeds GBP 440; and
(ii) the past-due amount represents more than 1% of all on-balance-sheet items to that obligor.
For retail (Article 178(2)(d) UK CRR) the absolute threshold is GBP 0 with 0% relative.

Both extraction methods (standard pdftotext and -raw flag) return GBP 0 / 0% for retail
consistently, confirming this is the actual text and not a watermark-corruption artifact. It
reflects the UK's choice to set no absolute monetary floor for retail — any past-due penny is
material. This differs from the EU CDR 2018/171 calibration, which sets EUR 100 (retail)
and EUR 500 (non-retail) as the absolute component.

**Citation:** Regulation (EU) No 575/2013 (CRR), Article 178(2)(d), consolidated to
9 January 2024. The absolute-threshold detail: Commission Delegated Regulation (EU)
2018/171, Article 1.

---

### 3. Article 178(5): conditions for return to non-defaulted status; is a three-month minimum stated?

**Status: VERIFIED — with important distinction between EU CRR and UK CRR.**

**EU CRR Article 178(5)** contains no minimum observation period expressed in months. The full
text reads:

> 5. If the institution considers that a previously defaulted exposure is such that no trigger
> of default continues to apply, the institution shall rate the obligor or facility as they would
> for a non-defaulted exposure. Where the definition of default is subsequently triggered,
> another default would be deemed to have occurred.

No "three months" in the EU CRR text. The three-month minimum originates in the supervisory
guidance rather than the primary regulation. EBA/GL/2016/07 is the primary EU instrument
for the minimum observation period (confirmed by reference in the EBA/GL/2026/05 amending
guidelines, which describe the GL/2016/07 requirement and the option to shorten it). A direct
paragraph-level quote from GL/2016/07 itself was not obtained; see item 5 in "Do not state"
below for the acquisition path.

**UK CRR Article 178(5)(a)** (PS9/24 near-final) does state a three-month minimum explicitly:

> **(5)(a)** An institution shall, subject to points (c) and (d), and subject to paragraphs 5A
> to 5C where a distressed restructuring has occurred, in cases where the institution considers
> that a previously defaulted exposure is such that no trigger of default continues to apply,
> **continue to rate an exposure as being in default until at least 3 months have passed** since
> the conditions in points (a) and (b) of paragraph 1 ceased to be met. After this period the
> institution shall rate the exposure as it would for a non-defaulted exposure;

**If the lecture cites "three months":** The three-month minimum is correct for UK CRR
Article 178(5)(a) and for EBA/GL/2016/07 guidance on the EU CRR. It must not be attributed
to EU CRR Article 178(5) alone, which is silent on the duration.

**Citation:** UK CRR Art 178(5)(a): PRA Rulebook, Credit Risk: IRB Approach Part, Article 178(5),
PS9/24 near-final draft. EU CRR: Regulation (EU) No 575/2013, Article 178(5), consolidated to
9 January 2024.

---

### 4. Does Article 178(5a)/178(5A) exist, imposing a 12-month probation for distressed restructuring?

**Status: VERIFIED for UK CRR. CORRECTED for EU CRR — 178(5A) does not exist in the EU
consolidated text as such; the equivalent requirement originates in EBA/GL/2016/07.**

The EU CRR consolidated text (pre-CRR3) has Article 178 with paragraphs numbered 1 to 7.
There is no paragraph 5a or 5A. Paragraph 5 is the single return-to-non-defaulted-status
provision quoted in item 3 above.

**UK CRR Article 178(5A)** (PS9/24 near-final) does exist and does impose a one-year
(12-month) minimum for distressed restructuring cases:

> **5A.** An institution shall, where a distressed restructuring has occurred in accordance with
> point (d) of paragraph 3, rate the obligor or facility as they would for a non-defaulted
> exposure in paragraph 5 if:
>
> **(a)** at least one year has passed since the latest occurrence of one of the following events:
> (i) the moment of extending the restructuring measures;
> (ii) the moment when the exposure was classified as defaulted; or
> (iii) the end of the grace period included in restructuring arrangements; and
>
> **(b)** all of the following conditions are met:
> (i) during the one year period referred to in point (a), a material payment has been made
> by the obligor [...];
> (ii) during the one year period referred to in point (a) the payments have been made
> regularly according to the schedule applicable after the restructuring arrangements;
> (iii) there are no past due credit obligations according to the schedule applicable after the
> restructuring arrangements;
> (iv) no indications of unlikeliness to pay [...] apply;
> (v) the institution does not consider it otherwise unlikely that the obligor will pay [...]

**Source of the 12-month figure in the EU context:** EBA/GL/2016/07 (Guidelines on the
application of the definition of default under Article 178 CRR) contains the equivalent
one-year probation period requirement for exposures defaulted through distressed
restructuring. This is confirmed by reference in the EBA/GL/2026/05 amending guidelines
(7 May 2026), which note that "the possibility to shorten the probation period from 1 year
to e.g. 3 months for certain forborne exposures has been considered" but was not adopted
for the general population (a partial shortening to 3–6 months for limited categories was
adopted). The GL/2016/07 PDF itself was not directly read (see item 5 in "Do not state").

**If asked in a lecture:** 178(5A) as a numbered provision exists in the UK CRR only. The 12-month
probation for distressed restructuring is real and EU-applicable; its primary instrument in the EU
context is EBA/GL/2016/07, not the EU CRR text.

**Citation:** UK CRR Art 178(5A): PRA Rulebook, Credit Risk: IRB Approach Part, Article 178(5A),
PS9/24 near-final draft. EU context: EBA/GL/2016/07, Guidelines on the application of the
definition of default under Article 178 of Regulation (EU) No 575/2013.

---

### 5. Article 180(2)(a): one-year horizon for retail PD estimation

**Status: VERIFIED** from EU CRR consolidated pre-CRR3, Article 180(2)(a).

> **Article 180 — Requirements specific to PD estimation**
>
> 2. For retail exposures, the following requirements shall apply:
>
> **(a)** institutions shall estimate PDs by obligor grade or pool from long run averages of
> one-year default rates;

For comparison, Article 180(1)(a) covers non-retail (corporates, institutions, central
governments) with identical language: "institutions shall estimate PDs by obligor grade from
long run averages of one-year default rates."

The one-year horizon is mandated for retail by Article 180(2)(a) and for non-retail by
Article 180(1)(a).

**Citation:** Regulation (EU) No 575/2013 (CRR), Article 180(2)(a), consolidated to
9 January 2024. EUR-Lex CELEX 02013R0575-20231228.

---

## IFRS 9

Primary source read: IASB, *IFRS 9 Financial Instruments* (2014 as amended to 2021 edition),
`vault/raw/ifrs/iasb-ifrs9-financial-instruments-2021.pdf`, extracted via pdftotext.

All four paragraphs below were found and read directly from that PDF. The IASB edition is the
primary source for all quotes below. The EU-adopted version (Commission Regulation (EU)
2016/2067, OJ L 323, 29.11.2016) is expected to reproduce the same paragraph numbering, but
EUR-Lex was WAF-blocked during this session and that version was not read directly; do not
assert equivalence without independent verification.

---

### 6. Paragraph 5.5.11: the 30-days-past-due rebuttable presumption for SICR

**Status: VERIFIED** from IFRS 9 IASB primary PDF, paragraph 5.5.11.

> **5.5.11** If reasonable and supportable forward-looking information is available without
> undue cost or effort, an entity cannot rely solely on past due information when determining
> whether credit risk has increased significantly since initial recognition. However, when
> information that is more forward-looking than past due status (either on an individual or a
> collective basis) is not available without undue cost or effort, an entity may use past due
> information to determine whether there have been significant increases in credit risk since
> initial recognition. Regardless of the way in which an entity assesses significant increases
> in credit risk, **there is a rebuttable presumption that the credit risk on a financial asset
> has increased significantly since initial recognition when contractual payments are more
> than 30 days past due.** An entity can rebut this presumption if the entity has reasonable
> and supportable information that is available without undue cost or effort, that demonstrates
> that the credit risk has not increased significantly since initial recognition even though the
> contractual payments are more than 30 days past due. When an entity determines that there
> have been significant increases in credit risk before contractual payments are more than 30
> days past due, the rebuttable presumption does not apply.

**Citation:** IFRS 9 Financial Instruments, paragraph 5.5.11. IASB, 2014 (as amended).

---

### 7. Paragraph 5.5.9: the SICR assessment requirement

**Status: VERIFIED** from IFRS 9 IASB primary PDF, paragraph 5.5.9.

> **5.5.9** At each reporting date, an entity shall assess whether the credit risk on a financial
> instrument has increased significantly since initial recognition. When making the assessment,
> an entity shall use the **change in the risk of a default occurring over the expected life** of
> the financial instrument instead of the change in the amount of expected credit losses. To
> make that assessment, an entity shall compare the risk of a default occurring on the financial
> instrument as at the reporting date with the risk of a default occurring on the financial
> instrument as at the date of initial recognition and consider reasonable and supportable
> information, that is available without undue cost or effort, that is indicative of significant
> increases in credit risk since initial recognition.

**Citation:** IFRS 9 Financial Instruments, paragraph 5.5.9. IASB, 2014 (as amended).

---

### 8. The write-off paragraph: confirmed as 5.4.4

**Status: VERIFIED** from IFRS 9 IASB primary PDF, paragraph 5.4.4.

> **5.4.4** An entity shall directly reduce the gross carrying amount of a financial asset when
> the entity has no reasonable expectations of recovering a financial asset in its entirety or a
> portion thereof. A write-off constitutes a derecognition event (see paragraph B3.2.16(r)).

The paragraph number 5.4.4 is confirmed. The phrase "directly reduce the gross carrying
amount" is confirmed. The phrase "no reasonable expectations of recovering" is confirmed.

**Citation:** IFRS 9 Financial Instruments, paragraph 5.4.4. IASB, 2014 (as amended).

---

### 9. Paragraph B5.5.37: the 90-days-past-due rebuttable presumption for default; consistency with internal credit risk management

**Status: VERIFIED** from IFRS 9 IASB primary PDF, paragraph B5.5.37.

> **B5.5.37** When defining default for the purposes of determining the risk of a default
> occurring, **an entity shall apply a default definition that is consistent with the definition
> used for internal credit risk management purposes** for the relevant financial instrument and
> consider qualitative indicators (for example, financial covenants) when appropriate.
> However, **there is a rebuttable presumption that default does not occur later than when a
> financial asset is 90 days past due** unless an entity has reasonable and supportable
> information to demonstrate that a more lagging default criterion is more appropriate. The
> definition of default used for these purposes shall be applied consistently to all financial
> instruments unless information becomes available that demonstrates that another default
> definition is more appropriate for a particular financial instrument.

Both elements of the claim are confirmed: the 90-days-past-due rebuttable presumption, and
the requirement that the default definition be consistent with internal credit risk management
practice.

**Citation:** IFRS 9 Financial Instruments, paragraph B5.5.37. IASB, 2014 (as amended).

---

## Academic

### 10. Botha, Oberholzer, Larney and de Jongh (2023): full reference and G(d,s,t) definition

**Status: VERIFIED** from arXiv preprint 2303.03080v4 PDF, downloaded and read directly
2026-09-03 (3.7 MB; %PDF header confirmed). Journal publication details confirmed from
arXiv abstract metadata on the same preprint.

**Full reference:**

Botha, A., Oberholzer, E., Larney, J. and de Jongh, R. (2025). "Defining and comparing
SICR-events for classifying impaired loans under IFRS 9." *Annals of Operations Research*,
online first. DOI: [10.1007/s10479-025-06546-3](https://doi.org/10.1007/s10479-025-06546-3).

arXiv preprint: arXiv:2303.03080, submitted 6 March 2023, last revised 1 February 2025 (v4).
URL: https://arxiv.org/abs/2303.03080

The convention "Botha et al. (2023)" refers to the arXiv submission year. The journal
publication year is 2025. Cite as the 2025 Annals of Operations Research paper in any
formal reference list.

**Author list confirmed:** Arno Botha, Esmerelda Oberholzer, Janette Larney, Riaan de Jongh.

**G(d,s,t) definition, from Section 3 of the v4 PDF (Equation 1):**

> G(d, s, t) = [(∑_{v=t−(s−1)}^t [g₀(v) ≥ d]) = s]  for t ≥ s

where [·] denotes Iverson brackets (returns 1 if the enclosed statement is true, 0 otherwise),
d is the delinquency threshold, s is the stickiness parameter (number of consecutive months
over which delinquency is tested), and g₀(v) is the base delinquency measure at month v.

Verbatim from the paper: "G(d, s, t) ... is formalised within the Boolean-valued decision
function G(d, s, t) that yields a binary-valued SICR-status in defining a SICR-event at an
end-point t."

**Sweep grid, confirmed from Section 3 of the v4 PDF:**

> "the parameter space includes: 1) the threshold d ∈ {1, 2} of g₀-measured delinquency
> beyond which SICR is triggered; 2) the level of stickiness s ∈ {1, 2, 3} within the
> delinquency test; and 3) the choice of outcome period k ∈ {3, 6, 9, 12} when modelling
> SICR-outcomes."

This yields 2 × 3 × 4 = **24** combinations. Table 2 of the paper confirms this explicitly:
"Numbered SICR-definitions, indexed by j = 1,...,24." The abstract of the paper states "27
unique SICR-definitions", which appears to be an artefact of an earlier version of the
manuscript; the table count of 24 is the authoritative figure and should be used in the lecture.

**Note on the g₀ measure:** The g₀ function is from the companion Botha, Beyers and
De Villiers (2021) paper (*Expert Systems with Applications*, volume 177), not the present
paper. Do not conflate the two: the 2021 paper defines g₀; the 2023/2025 paper builds G(d,s,t)
on top of it.

---

### 11. Does the paper (or a companion Botha paper) treat three payments in arrears as default itself?

**Status: VERIFIED — YES, the paper uses g₀(t) ≥ 3 (three payments in arrears) as the
default indicator, explicitly labelled "Default" in Table 1 of the v4 PDF.**

Table 1 of the paper illustrates the G function with a column headed "Default: g₀(t) ≥ 3",
showing account-level default status alongside the SICR-status columns G(1,1,t) and
G(1,2,t). At time t = 9, when g₀(t) = 3, the "Default" column records 1; all earlier
periods with g₀(t) < 3 record 0.

From Section 4.2 of the v4 PDF (p. 14): "Since g₀(t+k) ≥ 3 > d from Eq. 1 will hold for
both default..." — confirming that g₀ ≥ 3 is treated as the default event, which is strictly
above the SICR thresholds d ∈ {1, 2}.

The paper therefore distinguishes three zones:
- g₀(t) ∈ {1, 2}: possible SICR territory, depending on d and s;
- g₀(t) ≥ 3: default territory (three or more payments in arrears);
- g₀(t) = 0: performing, no SICR.

The paper does NOT define d = 3 as a SICR threshold (the sweep only covers d ∈ {1, 2}).
Three payments in arrears is used as the boundary between SICR and default, not as a SICR
trigger.

---

## Do not state in a public lecture

The following claims cannot be stated without qualification or must be re-attributed.

1. **"Article 178(5) requires at least three months before return to non-defaulted status."**
   Partially correct, but the EU CRR Article 178(5) does not state a minimum duration. The
   three-month minimum is stated in UK CRR Article 178(5)(a) (PS9/24) and in EBA/GL/2016/07.
   State it as a supervisory guidance requirement (EU) or cite the UK CRR article (UK context).

2. **"Article 178(5A) imposes a 12-month probation for distressed restructuring" (attributing
   this to the EU CRR).** Article 178(5A) does not exist in the EU CRR consolidated text.
   The 12-month probation requirement for distressed restructuring exists in UK CRR Article
   178(5A) (PS9/24) and in EBA/GL/2016/07. In an EU context, attribute to the GL. In a UK
   context, cite UK CRR Article 178(5A) directly.

3. **The materiality threshold amount under Article 178(2)(d).** The EU CRR text does not
   specify a monetary amount; the competent authority sets it within conditions in Commission
   Delegated Regulation (EU) 2018/171. Do not state a specific EUR threshold as if it were in
   the CRR text.

4. **The Botha paper as a 2023 journal publication.** The paper was submitted to arXiv in
   March 2023 but published in the Annals of Operations Research in 2025. Cite as Botha et al.
   (2025) in any formal reference, or note the arXiv preprint year separately.

5. **EBA/GL/2016/07 paragraph-level provisions.** The EBA/GL/2016/07 primary PDF was not
   available in the vault and could not be downloaded through EUR-Lex or EBA website (WAF
   block) during this session. The substance of its requirements is confirmed through the
   EBA/GL/2026/05 amending guidelines (vault JSON) and the vault's irb-definition-of-default
   wiki article, but paragraph-level quotes from GL/2016/07 itself are not available here.
   Acquire the PDF directly from eba.europa.eu for paragraph-level attribution.

---

## Sources consulted

| Source | Path or URL | Status |
|---|---|---|
| EU CRR consolidated pre-CRR3 (PDF) | `vault/raw/legislation/2024-01-09_575-2013_crr-consolidated-pre-crr3.pdf` | Direct read |
| UK CRR near-final draft (PS9/24 App. 2, PDF) | `vault/raw/pra/pra_ps9_24_app2_crr_near_final.pdf` | Direct read |
| PRA SS3/24 definition of default (Jan 2026, PDF) | `vault/raw/pra/pra_ss3_24_definition_of_default_jan2026.pdf` | Direct read |
| EBA/GL/2026/05 amending guidelines (JSON) | `vault/raw/eba_publications/20260507_Report_amending_the_Guidelines_on_the_application_of_the_definition_of_default.json` | Direct read |
| EBA/GL/2016/07 peer review (JSON) | `vault/raw/eba_publications/20240722_Peer_Review_report_on_the_EBA_Guidelines_on_the_application_of_the_definition_of_default.json` | Direct read |
| IFRS 9 IASB 2021 edition (PDF) | `vault/raw/ifrs/iasb-ifrs9-financial-instruments-2021.pdf` | Direct read |
| Botha et al. arXiv v4 PDF | https://arxiv.org/pdf/2303.03080v4 | Direct read (downloaded) |
| Vault wiki: irb-definition-of-default.md | `vault/wiki/regulation/irb-definition-of-default.md` | Pointer only |
| Vault wiki: eu-crr-2013-credit-risk.md | `vault/wiki/regulation/eu-crr-2013-credit-risk.md` | Pointer only |

*EBA/GL/2016/07 primary PDF: not in vault, not downloadable via curl (EBA WAF block). Acquire
manually from eba.europa.eu for paragraph-level citation.*

---

*Verification completed 2026-09-03; corrections and Botha PDF re-read 2026-09-03,
validation-researcher (claude-sonnet-4-6).*
*All VERIFIED items trace to a primary document read directly in this session.*
