# Actuarial Deep Learning

## Project overview

This repo holds Mario's working files for the actuarial summer school **Deep Learning for
Actuarial Modeling**, run at Università Cattolica del Sacro Cuore, Milan, from 31 August to
4 September 2026 by Salvatore Scognamiglio, Marco Maggi, Mario V. Wüthrich and Ronald Richman.
The course site is
`https://people.math.ethz.ch/~wueth/Lecture/SummerSchool2026/SummerSchoolMilano.html`, and the
lecture notes are the SSRN technical document at `abstract_id=5162304`.

Treat this as a **learning repo**, not a Gini deliverable. The work here is exercise solutions,
scratch experiments and notes taken during twelve lectures. Consequently several Gini
engineering conventions are relaxed, and the relaxations are stated below rather than left to
inference.

The syllabus runs from Poisson GLMs on French motor third-party liability data through
feed-forward networks, entity embeddings, the balance property and auto-calibration, ICE
networks, LocalGLMnet, attention layers and the Credibility Transformer, ending on foundation
models and in-context learning.

## Key directories

| Path | Purpose |
|---|---|
| `lectures/` | Ten lecture documents (`.html`) plus `lecture.css`, the shared presentation layer. Seven were Quarto-rendered by the course authors and downloaded from the course site; lectures 3, 8 and 12 are reconstructions from the PDF decks, and carry a `.qmd` source beside them. The authors' figures live in `lectures/figures/`, gitignored; the reconstructed ones live in `lectures/figures-reconstructed/` and are committed, see below |
| `scripts/` | Repo utilities: the lecture figure fetcher, the PDF figure extractor, the Quarto render wrapper, the HTML-to-PDF printer, the credit data converter and the Eurostat macro fetcher |
| `credit_lectures/` | Mario's credit risk companion lectures: Quarto `.qmd` sources and their rendered HTML, one per course lecture and **numbered to match the course**, so `03_credit-deep-learning-overview` answers `lectures/03_deep-learning-overview` and `04-05_credit-fnn` answers `lectures/04-05_fnn`. Most adapt their course lecture to the Bondora PD problem; lecture 3 uses the wide credit card portfolio instead, because Bondora's 45 interpretable columns make no case for automated feature extraction. Render with `bash scripts/render_lecture.sh credit_lectures/*.qmd`, never bare `quarto render`: the script strips Quarto's Bootstrap/JS assets so `lecture.css` gets the bare structure it lays out, and it moves the figures out of Quarto's `<stem>_files/figure-html/` into `credit_lectures/figures/<stem>/`, rewriting the `src` paths to match. That move, made on 3 September 2026, is why the directory holds one `figures/` tree rather than sixteen `_files` directories, and it is also why `quarto render` on its own is a regression: Quarto recreates `<stem>_files` every time, so the sixteen come straight back. Lecture 1 reads `bondora_raw.parquet` for its censoring and outcome-window illustrations, which need `DefaultDate`, `Status` and `ReportAsOfEOD`; the modelling table `bondora_pd.parquet` stays leak-free and is never the source for those. `09_credit-localglmnet` discharges the promise lecture 3 made for LocalGLMnet, namely per-decision reason codes out of a fitted decomposition, and it is the one credit lecture whose design matrix is **not** the 38-column one-hot one: the variable importance measure compares attention-weight magnitudes across components, so it needs every covariate continuous and standardised, and the five categoricals therefore enter as two-dimensional entity embeddings rotated by a within-characteristic PCA, giving 14 columns. Four results are worth knowing before editing it. Initialised at the fitted GLM the network reproduces that GLM's deviance exactly, which is the check to run before reading any attention weight. Nagged over ten fits it reaches a test deviance of 107.132, beating everything else in the series and reversing the course's own finding that the LocalGLMnet trails the plain network. Income's attention weight is negative for 62.6 per cent of borrowers and positive for the rest, which looks like lecture 1's Simpson paradox recovered per borrower, and yet the country ordering supporting that reading reverses between seeds, so the lecture grades it directionally consistent with `C1` and unable to establish the paradox alone. Above all, among the highest-PD decile the leading adverse characteristic is identical across all ten fits for 92.0 per cent of applicants while the second-ranked one agrees for 1.6 per cent, because the leading contribution exceeds the second by 1.043 on the log-odds scale and the second exceeds the third by 0.118; hence one reason code is defensible on this book and three are not, and that figure is a lower bound, since the entity embedding was fitted once and held fixed across the refits. Its overlap map, notation bridge, measured-facts register and citation register are in `notes/localglmnet-lecture-structure.md`, where the two regulatory duties it cites were verified against primary text and one point matters: UK GDPR Article 22 was substituted by Articles 22A to 22D under the Data (Use and Access) Act 2025 and has been in force in that form since 5 February 2026, so the older wording much of the secondary literature still quotes no longer states the law. `10-11_credit-transformer` answers `lectures/10-11_transformers` and is the only credit lecture reading **two** datasets for two different problems, because credit has a sequential problem where insurance has none. Its first act runs attention over `amex_panel.parquet`, discharging lecture 3's explicit promise that "the Amex panel is the dataset in this series it was made for", and its second act builds the Credibility Transformer on `bondora_pd.parquet` with the filters and seed-1 split of lectures 4 to 9 so the deviance still chains. Note that `home_credit_cards.parquet` was considered for the first act and rejected: the converted table carries no response variable, since Home Credit's target lives in `application_train.csv`, which the converter never touches. Six results are worth knowing before editing it. A causally masked layer gives the profile a behavioural scorecard should have, 0.8828 of AUC on one statement rising to 0.9468 on thirteen, and it beats the unmasked layer at month 13 on deviance, 49.370 against 52.385, so respecting time order costs nothing where both models are entitled to the same data. Dropping the mask buys 0.0481 of AUC at month 1, which is the leak priced. A panel sorted the wrong way round and then fitted reports 0.9435 of AUC from a single statement against an honest 0.8828 and understates the deviance by 19.7 points, and it passes a hold-out test because the hold-out shares the bug; the only surviving tell is that the profile goes flat where a genuine one rises, which is now the recommended diagnostic for any sequential credit model. On the tabular side the architecture competes without leading: 107.342 at seed 100 and 107.327 with the credibility mechanism switched off lead the single fits the series has published, the ten-seed mean of 107.381 sits between lecture 9's 107.434 and lecture 6's 107.313 with neither difference significant, and nagging reaches 107.097 against lecture 6's nagged embedded network at 106.921. Do not attach a bare "best single fit" to 107.342, since this lecture's own alpha = 1 fit is lower. The explicit credibility gate works mechanically, in that below alpha = 1 the prior token learns the global mean to floating-point constancy while at alpha = 1 it never trains at all, and yet it buys no accuracy here: the sweep spans 0.213 against a seed standard deviation of 0.126 and is won by switching the mechanism off, so the course's French motor gain does not reproduce. Above all, the implicit credibility weight is a property of the fit rather than of the borrower. Reseeding moves its mean from 0.0295 to 0.1683, a between-fit dispersion 9.4 times the spread across borrowers inside one fit, it separates borrowers with no prior loan from those with three or more by 0.0012 in the wrong direction, and it correlates with the fitted probability at -0.67; hence no threshold on it survives a refit and the lecture says so. Two smaller decisions carry weight: the architecture is deliberately **single-headed**, because the implicit mechanism is read off one entry of one attention matrix and multi-head attention gives n_h of them with no single credibility weight to report, and the lecture **declines** to turn the CLS token's attention over characteristics into a variable importance measure, since nine of ten fits put `Country` first while the primary fit puts `NewCreditCustomer` first and no noise covariate calibrates the weights, so it points at lecture 9's tested measure instead. Its overlap map, notation bridge, measured-facts register and citation register are in `notes/transformer-lecture-structure.md`, which also records that the course miscites feature tokenisation to TabM when it belongs to the FT-Transformer of Gorishniy, Rubachev, Khrulkov and Babenko (2021), and that the lecture carries no regulatory citation by decision rather than by omission. It renders in roughly twenty minutes, and the note explains which fits are reused and must not be tidied apart. `12_credit-foundation-models` answers `lectures/12_foundation-models` and closes the course sequence. It is the only credit lecture that runs a **third-party pretrained model**, namely TabPFN v2 through the `tabpfn` package installed into `.venv` under the render-only precedent, and two install traps are worth knowing before touching it: the package's default checkpoint is gated on HuggingFace and fails without an accepted licence, so the lecture passes `model_path="tabpfn-v2-classifier.ckpt"` to select the ungated v2 weights the course actually cites, and pinning `tabpfn` 2.x instead downgrades `scikit-learn` to 1.6.1 and then breaks outright when the 1.8.0 pin is restored. Its spine is a **cold start** rather than a small portfolio, on the ground that lenders open and close whole books, and it holds out Bondora's Slovak book of 296 seasoned loans, originated over ten months in 2014 and then closed, defaulting at 70.6 per cent against Estonia's 17.0. Sections 2.6 to 2.8 score on a fixed 3,000-row subsample of the test set rather than all 29,734, because TabPFN's cost is quadratic in its context; sections 3 onward return to the full test set, so only the learning-curve figures sit off the series' scale. Seven results are worth knowing before editing it. TabPFN leads the learning curve at every size to 10,000 rows, reaching 113.312 at 250 rows where the Credibility Transformer manages 119.638 against a null of 122.114, and the maximum-likelihood GLM separates below 5,000 rows, averaging 1901.015 at 250. TabPFN handed 10,000 rows reaches 110.877 and a GLM fitted on all 118,933 reaches 110.873, so a cross-table prior on 8 per cent of the data reproduces the classical model without bettering it. TabPFN also lands 1.9 percentage points below the observed default rate, about 2.3 sampling standard errors, and has no parameter through which a balance correction could be applied, so lecture 7's recalibration has to sit outside the model. On the tabular side in-context learning does nothing: five paired fits put the ICL-CT 0.0116 behind its own base model with a paired standard deviation of 0.0320, and in two of the five seeds no epoch of either phase beat the identity initialisation, so the best-epoch column has to be reported or a difference of 0.000 is indistinguishable from a tie. Three measurements say why, and the first is the lecture's most novel finding: the paper's batch retrieval unions 200 targets' 64 nearest neighbours and caps the union at 1,000 by retrieval frequency, and since 94.6 per cent of retrieved rows are retrieved by exactly one target the cap discards 92 per cent of the union and hands the median borrower **three of its own sixty-four neighbours**, so the context is close to a random thousand-row sample of the book. That is a scale mismatch in the paper's own batching rather than an implementation error, since a union of 200 neighbourhoods fits inside 1,000 slots only where neighbourhoods overlap heavily. Sharpening it does not help: scoring one borrower at a time against its own 64 neighbours makes the attention row flatter, a coefficient of variation of 0.023 against 0.099, and moves the prediction somewhere slightly worse. And the neighbourhood mean that survives the averaging correlates +0.6535 with what the base model already predicts, because retrieval searches the space the decoder reads. On the Slovak cold start both networks are decisively **worse than the null model**, 236.626 and 234.636 against 195.781 with non-overlapping intervals, only the GLM beats it at 185.720, and every model under-predicts by around forty percentage points. Above all, retrieval imports the wrong country's experience, drawing 71.0 per cent of its context from Estonia against 58.1 per cent of the pool while pricing the segment whose default rate is four times Estonia's, because similarity is measured in the CLS token space of the very model that is wrong about the segment. Two further points must not be lost in editing. The governance finding **reverses** the intuitive one: re-drawing half the retrieval pool moves a borrower's fitted log-odds by 0.0023 in range against the 1.043 separating lecture 9's leading reason code from its second, so the explanation survives, and it survives because the attention is flat and the retrieved set was barely the borrower's own to begin with, which are the same properties that denied the mechanism any accuracy. And the seed-100 re-draw of exactly zero is an **artefact** of the selection rule returning the identity initialisation, whose ICL layers ignore their context entirely, so section 5.2 measures the actively trained state and reports the selected state beside it only as a wiring check; keep both rows. One methodological finding travels further than the rest: on the 296-row Slovak sample a paired bootstrap reports a confident -1.990 gain under a 20-by-50 training budget and a confident +4.172 loss under a 30-by-100 one, with no resample dissenting either way, so an interval computed on a small test sample measures sampling variation and not the model-selection variation that dominates it. Its overlap map, notation bridge, measured-facts register and citation register are in `notes/foundation-models-lecture-structure.md`, which also records the two planned claims the measurements killed, the three fit reuses that must not be tidied apart, and why section 5.2 recomputes its CLS tokens rather than reusing section 3.7's. It renders in roughly thirty minutes. Lectures prefixed `S` are a **survival analysis track numbered outside the course sequence**, because no course lecture answers them: `S1_credit-survival-bridge` picks up the discrete-hazard exposure convention lecture 1 defines but does not use, and `S2_survival-insurance-to-credit` supplies the actuarial-to-statistical translation and the Fine-Gray correction S1 defers. `S3_deep-survival-credit` replaces S1's logistic regression with a network, so the whole term structure comes out of one forward pass with a mask instead of the 2.7 million-row expansion, and asks lecture 7's balance and auto-calibration questions of a survival head. All three read `bondora_survival.parquet`. Lectures prefixed `R` are a **regulatory track, also numbered outside the course sequence**, and they grow out of review comments on lecture 1 asking for two of its callouts to become lectures: `R1_credit-ifrs9-pit-pd` separates the survival conditioning axis from the macro one, reviews eleven ways to estimate a point-in-time PD term structure, and demonstrates one on Bondora expanded to person-periods with real Eurostat series attached, so it reads `bondora_survival.parquet` **and** `credit_lectures/data/macro_eurostat.csv`. `R2_credit-irb-capital` takes lecture 1's hybrid PD callout into the IRB world, running the five-step production sequence from a point-in-time scorecard through risk grades, a long-run average and a margin of conservatism to the regulatory PD, then through the single-factor model to the worst-case default rate and the risk weight. It reads `bondora_pd.parquet` **and** `credit_lectures/data/macro_eurostat.csv`, reuses lecture 1's GLM3 unchanged as its scorecard, and takes its structure, regulatory references and transferable method from Mario's A-IRB guides material with no portfolio specifics carried over. Its outline, the notation bridge resolving the three symbol clashes against the guides, and the register of which regulatory citations survived verification are in `notes/irb-lecture-structure.md`; four citations could not be verified locally and the lecture cites around them. `R3_credit-sampling-and-representativeness` audits the partition every other lecture inherited, and grew out of a request for a lecture on sampling, the time axis, class imbalance and the exclusion of distorted periods. It owns sample design: the four samples, clustered splitting, snapshot eligibility, representativeness and imbalance. It reads **four** sources, namely `bondora_pd.parquet`, `bondora_raw.parquet` for the `ReScheduledOn` relief exhibit, `bondora_survival.parquet` for R1's calendar-indexed expansion, and `credit_card_dev.parquet` for the 1.42 per cent bad rate lecture 1 promised and lecture 3 only named. Four results are worth knowing before editing it: the pandemic relief distortion is a two-month notch in the hazard, April and May 2020, rather than a multi-year window; the fixed-horizon table cannot express a calendar exclusion at all, since overlap-based exclusion empties the out-of-time test sample exactly; `DebtToIncome` and `UseOfLoan` stop being populated in July 2017, which no lecture had noticed and which no fitted model happens to use; and a classifier separates the development and out-of-time samples at an AUC of 0.96 while most marginal stability indices call the covariates stable. Its citation register and notation bridge are in `notes/sampling-lecture-structure.md`, which also records four corrections that verification forced, including that representativeness anchors on CRR Article 174(c) rather than 179 and that Article 180(2)(e) carries no economic-cycle requirement. Lecture 2 carries a callout pointing forward to it and its own numbers are deliberately left unchanged.  Lectures prefixed `C` are a **causal track, numbered outside the course sequence for the same reason**, and answer the third of those review comments, which asked for research into how medical statistics handles interactions, covariates and causation: `C1_credit-interaction-and-causation` separates interaction from effect modification and shows the scale-dependence numerically, derives an adjustment set from a causal diagram rather than from predictive lift, walks every row of lecture 1's own GLM3 table asking what it may be read as, standardises that model over the observed country and age distribution to recover the marginal income curve lecture 1 could not assemble, and prices the result's exposure to unmeasured confounding at an E-value of 1.34. It reads `bondora_pd.parquet` alone. `C2` is named and deferred, covering attribution read causally, i.e. SHAP, LocalGLMnet and ICE marginal effects against the Table 2 fallacy, and it belongs beside the course's LocalGLMnet lectures rather than here. The eleven epidemiology sources behind `C1` were ingested into the vault on 2 September 2026 and the verification contract is `notes/causation-research.md` Lectures prefixed `D` are a **definitional track, outside the sequence for the same reason**, and answer the part of lecture 1 that named default three times without finishing it: `D1_credit-default-definition` owns the response variable the whole series is built on. It separates the three targets that all answer to the name twelve-month PD, namely the worst-ever window maximum, the point-at-horizon state and the marginal PD, and shows that the first two are provably the same column whenever the probation period is at least as long as the outcome window, which is why documents routinely define one and describe the other. It corrects lecture 1's claim that Bondora flags at 60 days past due, measuring the declaration lag at a median 79 with quartiles 74 and 92; that correction also touches `S1` and the converter docstring, and it changes no target column, since `default_12m` was always Bondora's own flag within 365 days. It then defines cure, probation and write-off and sweeps them, which needs a monthly delinquency series that neither Bondora nor the Amex extract carries, so it reads `bondora_raw.parquet` **and** `home_credit_cards.parquet`. Its planning note, measured-facts register and notation bridge are in `notes/default-definition-lecture-structure.md`, and every regulatory quotation was verified against primary text in `notes/default-definition-citations.md`, which records four claims that had to be corrected, the largest being that EU CRR Article 178(5) states no minimum probation period at all. The boundary against `R3` is that D1 builds the outcome variable and `R3` picks the rows. Lectures prefixed `F` are a **feature engineering track, outside the sequence for the same reason**, and grow out of the single paragraph in lecture 3 that described the classical scorecard's hand-crafted features and moved on. Their organising finding is that the industry runs two incompatible traditions: one discretises every characteristic and weight-of-evidence encodes it, the other never bins and instead straightens covariates with Tukey's ladder and screens on a condition index. `F1_credit-classing-and-characteristic-analysis` runs the first tradition end to end on `bondora_pd.parquet`, hand-rolling monotone adjacent pooling, weight of evidence, information value and the IV-driven categorical merge, and using the pinned `sklearn.isotonic` for isotonic regression only. Four results are worth knowing before editing it: borrower age scores an information value of 0.0066 and would be screened out by any threshold in use, because forcing monotonicity reports lecture 1's hump as noise, and a two-arm classing at age 41 recovers only 1.64 times that and still misses the 0.02 floor; holding lecture 2's eight covariates fixed, the classed fit loses about four tenths of an AUC point on both splits, which is the cost of the step function as a number; income's weight-of-evidence coefficient is +1.0001 alone and -0.1459 with country, so lecture 1's Simpson paradox surfaces as the sign flip the procedure's own red flag is designed to catch; and a WoE model retrained on its own predictions moves a fitted PD by 6.7 percentage points where a dummy-coded one reproduces itself to 1e-13. It deliberately does **not** redefine weight of evidence, Bühlmann credibility or one-hot encoding, all of which lecture 6 already owns, and it stops at the fitted feature set, citing `R3` forward for stability. `F2` is outlined and deferred, covering stepwise's failure on noise, partition variables, marginal information value, correlation clustering and the condition index on `credit_card_dev.parquet`, the Tukey-ladder tradition in full, and the points scale with the characteristic stability index that needs it. The overlap map, notation bridge and citation register are in `notes/feature-engineering-lecture-structure.md`, which records four claims that verification rejected, the largest being that no regulation requires a monotone weight-of-evidence profile: CRR Article 174(c) is the representativeness anchor, as `R3` already established. |
| `exercises/` | The three 2026 exercise notebooks, exactly as issued |
| `exercises/solutions/` | Mario's worked solutions. Never edit an issued exercise in place |
| `reference/` | Four Python notebooks from the `wueth/AITools4Actuaries` GitHub repo |
| `data/` | Course data, unpacked from `Data.zip`. Gitignored, see below |
| `notes/` | Notes per lecture, in markdown |
| `dashboard/` | Builder for the self-contained portfolio explorer. Output is gitignored, see below |
| `index.html` | Landing page for the published lecture site, linking the nineteen credit lectures. See below |

## Tech stack

Python 3.14.7, managed with `uv`, in an in-repo `.venv`. The pinned stack is `torch` 2.11.0,
`polars` 1.40.1, `pandas` 3.0.2, `scikit-learn` 1.8.0, `statsmodels` 0.14.6 and
`model-diagnostics` 1.5.0, with `ipykernel` for notebooks.

To set the environment up from scratch, or to rebuild it:

```bash
uv venv --python 3.14.7 .venv
uv pip install --python .venv -r requirements.txt
source .venv/bin/activate          # then select .venv as the notebook kernel in VS Code
```

`requirements.txt` is the course's own file, byte for byte, and it is the source of truth for
the environment. Do not curate it into `pyproject.toml` dependencies and do not bump a pin: the
demonstrators say "pip install -r requirements.txt" out loud, and any divergence becomes a
debugging job during a lecture.

Two deliberate deviations from the course IT instructions:

- The instructions ask for **miniconda**. This repo uses `uv` instead, because `uv` is already
  installed and every pin resolves to a binary wheel on `cp314` macOS arm64. When a demonstrator
  says `conda activate summer_school_2026`, read it as `source .venv/bin/activate`.
- The instructions ask for **Python 3.14.4 exactly**. That patch has no `uv` build, so the repo
  pins 3.14.7 in `.python-version`. Both are `cp314`, so every wheel above matches either way.

Apple silicon note: `torch.backends.mps.is_available()` returns `True` here, so pass
`device="mps"` where a course notebook assumes CUDA.

## Data provenance

`data/` holds `freMTPL2freq.parquet` and `freMTPL2freqEmb.parquet`, unpacked from `Data.zip`
(16 MB) downloaded from the course site on 29 August 2026. Both are the **public** French motor
third-party liability dataset, 678,007 policies with 14 columns, which the actuarial literature
has used openly for years. No client data is involved.

The directory is gitignored all the same, since a 34 MB binary blob has no business in git
history and the file is one `curl` away. Redownload it from
`https://people.math.ethz.ch/~wueth/Lecture/SummerSchool2026/Data/Data.zip`.

### Credit risk data

`data/` also holds three credit risk datasets, added from 31 August 2026 for the
`credit_lectures/` series and profiled in `notes/credit-datasets.md`:

- `LoanData_Bondora.csv` (150 MB): the public Bondora P2P loan book, extract dated
  2021-07-20, from `https://www.bondora.com/en/public-reports`. It yields two derived
  modelling tables with different shapes, and mixing them up is the easy mistake.
  `bondora_pd.parquet` is the fixed-horizon table: 148,733 seasoned loans and a
  12-month flag. `bondora_survival.parquet` is the survival table: all 179,235 loans,
  the observed duration, and a three-level `exit_kind` (71,416 default, 42,144 settled,
  65,675 censored) from which the event indicator is derived rather than stored, so
  prepayment-as-censoring is never baked in. `DefaultDate` takes precedence over
  `Status` there, since 10,743 Repaid loans carry one; and `ContractEndDate` is
  deliberately admitted despite the leakage exclusion list, because a survival model's
  response **is** the exit time.
- `Dev_data_to_be_shared.csv` and `validation_data_to_be_shared.csv` (420 MB): an
  anonymised credit card portfolio distributed as a dev/validation pair; the validation
  file carries no `bad_flag`. The source is the public Kaggle dataset **Credit Card Behaviour Score** (`https://www.kaggle.com/datasets/suvroo/credit-card-behaviour-score`), confirmed by Mario on 3 September 2026; the two CSVs carry the uploader's own file names. The earlier note that the source was unconfirmed is withdrawn, which matters because the repository is public and lecture 3 and lecture R3 both publish statistics from this file.
- `amex-default-prediction/train_data.csv` and `train_labels.csv` (15 GB, 29 MB): the
  Kaggle "American Express Default Prediction" competition data
  (`https://www.kaggle.com/competitions/amex-default-prediction`), a genuine
  customer-month panel rather than a cross-section. `test_data.csv` and
  `sample_submission.csv` (32 GB, 59 MB) are also present but unconverted: the
  competition never released test labels, so the file gives 924,621 unscoreable
  customers.

Rebuild the derived parquets with:

```bash
.venv/bin/python scripts/convert_credit_data.py                    # bondora + credit card (default)
.venv/bin/python scripts/convert_credit_data.py --datasets amex    # amex_panel, amex_cross_section; streams 15 GB
.venv/bin/python scripts/convert_credit_data.py --datasets home_credit   # home_credit_cards
```

- `home-credit-default-risk/credit_card_balance.csv` (425 MB): one table from the Kaggle
  "Home Credit Default Risk" competition
  (`https://www.kaggle.com/competitions/home-credit-default-risk`), added 3 September
  2026 for lecture D1 and converted to `home_credit_cards.parquet` (3,840,312 monthly
  statements, 104,307 card facilities). It is here because it is the only public panel in
  the repo carrying a **month-stamped days-past-due field**, which a definition of default
  needs: a delinquency threshold and a persistence requirement are claims about a sequence
  of monthly states, and neither Bondora nor the Amex extract records one. `SK_DPD` is days
  past due in the month and `SK_DPD_DEF` the same after a materiality tolerance, so the pair
  puts Article 178's materiality limb in two columns; 48,377 statements reach 90 days on the
  first and 1,078 on the second. `MONTHS_BALANCE` counts backwards from the application, so
  ordering it ascending gives chronological order and reversing it silently reverses every
  sequence while leaving every marginal distribution intact. Nine of the archive's ten tables
  are deliberately left alone, `bureau_balance` included, since it keys on `SK_ID_BUREAU` and
  its `STATUS` field collapses 120+ days past due, sale, and write-off into one bucket.
  The competition's own column dictionary is copied alongside it and is quoted in the lecture.

### The one committed data file

`credit_lectures/data/macro_eurostat.csv` (15 kB) is the exception to everything above. It
holds three public Eurostat series for EE, FI and ES from 2009, namely the harmonised
unemployment rate, HICP annual inflation and real GDP growth year on year, and lecture R1
conditions its point-in-time hazard on them. It is **committed** rather than gitignored,
because a lecture nobody can render on a fresh clone is worse than a small text file in git
history, and the file says so in a comment at its own head. Rebuild it with:

```bash
.venv/bin/python scripts/fetch_macro_eurostat.py
```

Two details in that script are deliberate. Real GDP is published quarterly, so each quarterly
rate is held constant across its three months rather than interpolated, since interpolation
would invent monthly variation Eurostat never measured. And SK is excluded from the country
list, because its Bondora risk set has a median of seventeen loans a month.

Note also that the `.gitignore` rule is `/data/` rather than `data/`. The unanchored form
matched `credit_lectures/data/` as well, and a negation inside an excluded directory is inert,
since git stops the walk at the directory and never reaches an exception for a file below it.

Rendering the credit lectures needs the quarto CLI (installed user-space at
`~/.local/bin/quarto`, since the Homebrew cask wants sudo) plus three render-only
packages (`pyyaml`, `nbformat`, `nbclient`) installed into `.venv` on top of the course
requirements. They add nothing to `requirements.txt`, which stays byte-for-byte the
course's own file, and they upgrade none of its pins; a venv rebuilt from scratch needs
`uv pip install --python .venv pyyaml nbformat nbclient` before rendering.

### Lecture figures

The seven lecture documents were downloaded as bare HTML, without the images they reference, so
every plot and diagram was blank until 31 August 2026. Those 50 files, 5.6 MB in all, are the
course authors' own plots and diagrams, and they are gitignored for the same reason `data/` is.
They live in `lectures/figures/`, moved there on 31 August 2026 to keep the lecture documents
legible in a listing; the `src` paths inside the HTML were rewritten to match, and the fetch
script strips the `figures/` prefix before building each URL. Rebuild them with:

```bash
bash scripts/fetch_lecture_figures.sh          # fetch what is missing
bash scripts/fetch_lecture_figures.sh --force  # re-fetch everything
```

The script reads the image list out of the HTML rather than carrying its own, so it stays
correct if a lecture is re-downloaded. Adding a lecture means adding one line to its `MAP`.
Note two traps it handles: the remote directories carry spaces (`Lecture 1_Use Case`) while the
figure directories inside them are hyphenated (`Lecture1-Use-Case_files`), so neither name can
be derived from the other; and `frMTPLNN3.png` is referenced by both lecture 4/5 and lecture 6,
which the flat `figures/` layout collapses onto one path. The two copies are byte-identical
today, and the script compares rather than overwrites, so a future divergence gets shouted
about.

### Reconstructed lectures

Lectures 3, 8 and 12 were handed out as beamer PDFs rather than as Quarto HTML, so they were
missing from the lecture set until 1 September 2026. Each now has a `.qmd` in `lectures/` that
transcribes its deck frame by frame, rendered through the same script the credit lectures use:

```bash
bash scripts/render_lecture.sh lectures/08_icenet-regularization.qmd
bash scripts/render_lecture.sh lectures/*.qmd                        # all three
```

The script takes paths and has no no-argument default, because sweeping both
directories would execute the credit lectures against the gitignored Bondora parquet.

The text, mathematics and tables are the authors'. Ours are the abstract (joined from each
deck's own Overview boxes), the ordering into a document rather than slides, and the figure
crops. Each `.qmd` says so in a comment at the top of its header, so the provenance travels
with the file.

Their figures live in `lectures/figures-reconstructed/` and **are committed**, unlike everything
`fetch_lecture_figures.sh` pulls. The reason is rebuildability: they come out of the PDFs, which
belong in `vault/raw/` rather than here, so a fresh clone has no way to regenerate them.
Rebuild them from the decks with:

```bash
.venv/bin/python scripts/extract_lecture_figures.py        # all three lectures
.venv/bin/python scripts/extract_lecture_figures.py 8      # one lecture
```

The script rasterises whole pages rather than pulling embedded images, because several plots
are vector drawings that `pdfimages` never sees and every embedded raster carries a paired soft
mask. It expects the decks in `~/Downloads`; edit `PDF_DIR` if they move. Per-figure `top`,
`bottom`, `left` and `right` fractions trim the beamer furniture before the white margins are
cropped, and the page counter is masked so it does not survive as a stray "10/36" beside a plot.

### The published site

`index.html` at the repository root lists the nineteen credit lectures, each with a one-line
description and links to its HTML and its PDF. It links `lectures/lecture.css` rather than the
Gini documents layer, so the index and the lectures share one register; that sheet states the
deviation at its own head, and every value in the index comes from its token block.

`.github/workflows/pages.yml` publishes it to GitHub Pages on a push to `main`, and the site is
live at <https://supermarmar.github.io/actuarial_deep_learning/>. Its `Assemble the site` step
is an allow-list, and everything it does not name stays off the site:

- **Published:** `index.html`, `credit_lectures/*.html`, `credit_lectures/*.pdf`, the
  `credit_lectures/figures/` tree, and `lectures/lecture.css`.
- **Not published:** everything else under `lectures/`, which is the course authors' material,
  plus the `*_grading-report.md` review artefacts, the `.qmd` sources, `notes/`, `exercises/`
  and `reference/`.

The site is assembled in the workflow rather than kept in a `docs/` folder, so the 30 MB of
rendered HTML and figures lives in the repository exactly once. Adding a lecture therefore
means adding an entry to `index.html`; the copy list itself needs no change, since it globs.

Note what the allow-list does and does not buy. It keeps the authors' material off the site,
which was its purpose while the repository was private. Since 3 September 2026 the repository
is public, so that material is readable on github.com regardless, and the list now serves the
narrower job of keeping the site to Mario's own work.

Two operational notes. Re-running only the failed job of a run that both uploads and deploys
produces a second artefact named `github-pages`, and `deploy-pages` then refuses to choose
between them; dispatch a fresh run instead. And should the actions ever be bumped,
`upload-pages-artifact@v5` excludes hidden files by default, which would silently drop
`site/.nojekyll` unless `include-hidden-files: true` is set.

### Lecture PDFs

Every lecture in `lectures/` and `credit_lectures/` carries a committed `.pdf` beside its
`.html`, so the material reads offline and on a tablet. Printing the PDF is therefore part of
landing a lecture: a new one is not finished until its PDF sits beside it. Rebuild one, or all
of them, with:

```bash
bash scripts/html_to_pdf.sh credit_lectures/R2_credit-irb-capital.html
bash scripts/html_to_pdf.sh lectures/*.html credit_lectures/*.html   # all 23, roughly 20 minutes
```

Headless Chrome does the printing, because every lecture pulls MathJax from a CDN and typesets
its mathematics in JavaScript; weasyprint and wkhtmltopdf have no script runtime, so they emit
the raw `\frac{}{}` and the failure looks like a successful conversion until somebody reads
page four. Consequently the script needs a network connection, and that is the one failure the
script cannot gate on: a slow CDN response yields raw TeX in a PDF that still exits zero, still
carries its `%%EOF` trailer and is still A4. Checking it would mean a PDF text extractor, which
is a dependency this repo does not carry, so open a rebuilt file and look at a page of
mathematics before trusting it.

A4, the margins and the print-colour treatment live in the `@page` and `@media print` blocks of
`lectures/lecture.css` rather than in the script's flags, so Cmd-P from the browser produces the
same page. Note that Chrome 152 writes the PDF and then declines to exit, and macOS ships no
`timeout(1)`, so the script waits for the file to settle and then terminates the browser itself;
it checks for a `%%EOF` trailer afterwards rather than trusting a file that merely stopped
growing. Raise `WATCHDOG` if that check ever fires.

Re-render the HTML before rebuilding a PDF from it. The PDF is downstream of the `.qmd` by two
steps, so `scripts/render_lecture.sh` comes first.

### Never reformat the authors' files

`lectures/`, `exercises/` and `reference/` hold files exactly as issued, so a formatter must
never touch them. A VS Code format-on-save rewrote 1,164 lines of `lectures/01_use-case.html`
on 31 August 2026, which buries any real change in a whitespace diff. Two guards are in place:
`.prettierignore` covers `lectures/*.html`, `exercises/` and `reference/`, and
`.vscode/settings.json` turns off format-on-save for HTML in this workspace. If a thousand-line
diff ever appears on a lecture file, that is what happened; `git checkout --` the file.

The `.prettierignore` rule names `lectures/*.html` rather than `lectures/`, so that our own
`lectures/lecture.css` stays formattable. A directory exclusion would not allow it back:
Prettier reads gitignore semantics, where excluding a directory stops the walk and a later
`!lectures/lecture.css` is inert.

The three reconstructed lectures sit inside the same guard, and want it for a different reason:
their `.html` is generated. Edit the `.qmd` and re-render rather than touching the output.

The same point bites during review. Review comments left as HTML comments in a rendered
`credit_lectures/*.html` do **not** survive the next render, so copy them out before
re-rendering (see `notes/lecture-1-review-comments-2026-09-01.md` for the pattern) and
prefer commenting in the `.qmd`. Re-rendering credit lecture 1 is safe, contrary to the
earlier assumption that its forty quoted figures made a re-render costly: on 1 September
2026 all 58 computed output lines reproduced identically, the only diff being two
statsmodels summary timestamps.

## Portfolio dashboard

`dashboard/build.py` renders `data/freMTPL2freq.parquet` into a single self-contained
`dashboard/dashboard.html`, roughly 2.4 MB, which opens straight from disk with no server and
no kernel:

```bash
.venv/bin/python dashboard/build.py && open dashboard/dashboard.html
```

All 678,007 policies travel inside the page as column-major `uint8` arrays, gzipped and
base64-encoded, so the cross-filter aggregates the whole book rather than a sample. Rows are
sorted on a composite key before encoding, which is what takes the payload from 3.6 MB to
1.6 MB. `dashboard/template.html` holds the markup, CSS and JavaScript with three
placeholders that the builder fills.

Two things to keep in mind when editing it. The page needs JavaScript, so it deliberately
departs from the "no JavaScript" line in `~/.claude/rules/html-design.md`; every other rule in
that file still applies, above all the 14px floor and the flat treatment. Separately, density
is encoded as `floor(log10(density) * 50)` rather than `round(...)`, because the panel buckets
by half-decade and those edges fall on exact multiples of 25 codes. Rounding put 11,752
policies into the neighbouring bucket.

The output is gitignored, since it is a 2.4 MB derived artefact and `data/` is gitignored
anyway. Commit the builder and the template, never the render.

## Repo versus vault

Draw the line by role, so files stop scattering across the two repos.

**Working files live here.** Exercise notebooks, solutions, scratch experiments, notes and the
data.

**Sources live in the vault**, meaning `~/Documents/Repos/vault`, which is a separate git repo
with its own conventions. The twelve PDF slide decks and the SSRN lecture notes belong in
`vault/raw/` and then in `wiki/` through `kb-ingest`. That ingest is outstanding as of
29 August 2026, and it wants its own commit and an audit entry per file, because the vault's
`curation-workflow` rule requires every file entering `raw/` to yield either a wiki article or
a recorded exclusion.

## Behavioural foundation

These apply to every task in this repo and override stylistic preference when they conflict.

1. **Don't assume. Surface tradeoffs.** Where the request is ambiguous, ask. Where a hidden
   decision sits underneath it (format, scope, fields, audience), name it and offer options
   rather than picking silently.
2. **Minimum work that solves the problem.** No speculative abstraction and no "while I'm here"
   additions.
3. **Touch only what's asked.** Above all, never edit an issued exercise notebook in place.
   Copy it first, then work on the copy, so the original stays available for comparison against
   the demonstrator's answer:

   ```bash
   cp exercises/glm_exercise_2026.ipynb exercises/solutions/glm_exercise_2026.ipynb
   ```
4. **Define done before starting. Verify before declaring finished.** For a notebook, "done"
   means the cells run top to bottom in a fresh kernel.

## What does not apply here

The Gini standards in `~/.claude/rules/` assume a production codebase. In this repo:

- **No mirrored test suite.** `~/.claude/rules/testing.md` is suspended. A learning notebook is
  verified by running it, not by a `tests/` tree.
- **No one-public-function-per-file convention.** Exploratory code lives in the notebook it
  belongs to. Where a helper genuinely gets reused across lectures, and only then, lift it into
  a small module.
- **Type annotations and docstrings are optional in notebooks**, and expected in any module
  that outlives the lecture it came from.

Everything else in `coding-standards.md`, `git-conventions.md` and the writing rules stands.

## Absolute rules

- Never commit secrets, credentials or client data. Nothing from a Gini engagement enters this
  repo, and no example here borrows a client's parameters or figures.
- Never commit `data/` or `.venv/`.
- **This repo is public, and was private until 3 September 2026.** GitHub Pages on a free
  personal account is only available for a public repository, so `supermarmar/actuarial_deep_learning`
  was made public that day to publish the credit lecture site. The consequence was accepted
  rather than overlooked: `lectures/`, `exercises/` and `reference/` hold the course authors'
  material rather than Mario's, and every one of those files is now readable by anyone, as is
  the whole git history. `lectures/figures/` is the sole exception, being gitignored.
  Consequently the earlier rule requiring a privacy check before every push is withdrawn, and
  the burden moves to what goes **in**: assume anything committed here is published the moment
  it lands. Nothing from a Gini engagement, and nothing under a licence that forbids
  redistribution.
- Never force-push `main`.

## Instructions for Claude Code

Before starting a task, activate the environment (`source .venv/bin/activate`) or invoke
`.venv/bin/python` directly. Never call a system `python3`. This machine carries 3.14.3 under
`/Library/Frameworks` and 3.14.7 under `/opt/homebrew`, and neither has the pinned packages.

While working, make small logical commits under Conventional Commits, and flag any new
dependency before installing it, since adding one breaks the match with the course file.

After finishing a notebook, restart the kernel and run it top to bottom before reporting the
task done.

## Shared team standards

| Rule file | Covers |
|---|---|
| `~/.claude/rules/coding-standards.md` | Type annotations, docstrings, architecture |
| `~/.claude/rules/git-conventions.md` | Conventional Commits, branch naming, PR rules |
| `~/.claude/rules/testing.md` | Suspended in this repo, see above |
