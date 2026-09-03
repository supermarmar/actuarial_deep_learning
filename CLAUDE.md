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
| `credit_lectures/` | Mario's credit risk companion lectures: Quarto `.qmd` sources and their rendered HTML, one per course lecture and **numbered to match the course**, so `03_credit-deep-learning-overview` answers `lectures/03_deep-learning-overview` and `04-05_credit-fnn` answers `lectures/04-05_fnn`. Most adapt their course lecture to the Bondora PD problem; lecture 3 uses the wide credit card portfolio instead, because Bondora's 45 interpretable columns make no case for automated feature extraction. Render with `bash scripts/render_lecture.sh credit_lectures/*.qmd`, never bare `quarto render`: the script strips Quarto's Bootstrap/JS assets so `lecture.css` gets the bare structure it lays out. Lecture 1 reads `bondora_raw.parquet` for its censoring and outcome-window illustrations, which need `DefaultDate`, `Status` and `ReportAsOfEOD`; the modelling table `bondora_pd.parquet` stays leak-free and is never the source for those. Lectures prefixed `S` are a **survival analysis track numbered outside the course sequence**, because no course lecture answers them: `S1_credit-survival-bridge` picks up the discrete-hazard exposure convention lecture 1 defines but does not use, and `S2_survival-insurance-to-credit` supplies the actuarial-to-statistical translation and the Fine-Gray correction S1 defers. `S3_deep-survival-credit` replaces S1's logistic regression with a network, so the whole term structure comes out of one forward pass with a mask instead of the 2.7 million-row expansion, and asks lecture 7's balance and auto-calibration questions of a survival head. All three read `bondora_survival.parquet`. Lectures prefixed `R` are a **regulatory track, also numbered outside the course sequence**, and they grow out of review comments on lecture 1 asking for two of its callouts to become lectures: `R1_credit-ifrs9-pit-pd` separates the survival conditioning axis from the macro one, reviews eleven ways to estimate a point-in-time PD term structure, and demonstrates one on Bondora expanded to person-periods with real Eurostat series attached, so it reads `bondora_survival.parquet` **and** `credit_lectures/data/macro_eurostat.csv`. `R2_credit-irb-capital` takes lecture 1's hybrid PD callout into the IRB world, running the five-step production sequence from a point-in-time scorecard through risk grades, a long-run average and a margin of conservatism to the regulatory PD, then through the single-factor model to the worst-case default rate and the risk weight. It reads `bondora_pd.parquet` **and** `credit_lectures/data/macro_eurostat.csv`, reuses lecture 1's GLM3 unchanged as its scorecard, and takes its structure, regulatory references and transferable method from Mario's A-IRB guides material with no portfolio specifics carried over. Its outline, the notation bridge resolving the three symbol clashes against the guides, and the register of which regulatory citations survived verification are in `notes/irb-lecture-structure.md`; four citations could not be verified locally and the lecture cites around them. Lectures prefixed `C` are a **causal track, numbered outside the course sequence for the same reason**, and answer the third of those review comments, which asked for research into how medical statistics handles interactions, covariates and causation: `C1_credit-interaction-and-causation` separates interaction from effect modification and shows the scale-dependence numerically, derives an adjustment set from a causal diagram rather than from predictive lift, walks every row of lecture 1's own GLM3 table asking what it may be read as, standardises that model over the observed country and age distribution to recover the marginal income curve lecture 1 could not assemble, and prices the result's exposure to unmeasured confounding at an E-value of 1.34. It reads `bondora_pd.parquet` alone. `C2` is named and deferred, covering attribution read causally, i.e. SHAP, LocalGLMnet and ICE marginal effects against the Table 2 fallacy, and it belongs beside the course's LocalGLMnet lectures rather than here. The eleven epidemiology sources behind `C1` were ingested into the vault on 2 September 2026 and the verification contract is `notes/causation-research.md` |
| `exercises/` | The three 2026 exercise notebooks, exactly as issued |
| `exercises/solutions/` | Mario's worked solutions. Never edit an issued exercise in place |
| `reference/` | Four Python notebooks from the `wueth/AITools4Actuaries` GitHub repo |
| `data/` | Course data, unpacked from `Data.zip`. Gitignored, see below |
| `notes/` | Notes per lecture, in markdown |
| `dashboard/` | Builder for the self-contained portfolio explorer. Output is gitignored, see below |
| `index.html` | Landing page for the published lecture site, linking the thirteen credit lectures. See below |

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
  file carries no `bad_flag`. Local files only; source to be confirmed.
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
```

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

`index.html` at the repository root lists the thirteen credit lectures, each with a one-line
description and links to its HTML and its PDF. It links `lectures/lecture.css` rather than the
Gini documents layer, so the index and the lectures share one register; that sheet states the
deviation at its own head, and every value in the index comes from its token block.

`.github/workflows/pages.yml` publishes it to GitHub Pages on a push to `main`, and the site is
live at <https://supermarmar.github.io/actuarial_deep_learning/>. Its `Assemble the site` step
is an allow-list, and everything it does not name stays off the site:

- **Published:** `index.html`, `credit_lectures/*.html`, `credit_lectures/*.pdf`, the
  `credit_lectures/*_files/` figure directories, and `lectures/lecture.css`.
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
bash scripts/html_to_pdf.sh lectures/*.html credit_lectures/*.html   # all 22, roughly 20 minutes
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
