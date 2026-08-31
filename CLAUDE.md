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
| `lectures/` | Seven Quarto-rendered lecture documents (`.html`), downloaded from the course site, plus `lecture.css`, the shared presentation layer. Figures are gitignored, see below |
| `scripts/` | Repo utilities. Currently the lecture figure fetcher |
| `credit_lectures/` | Mario's credit risk companion lectures: Quarto `.qmd` sources and their rendered HTML, adapting each course lecture to the Bondora PD problem. Render with `bash scripts/render_credit_lecture.sh`, never bare `quarto render`: the script strips Quarto's Bootstrap/JS assets so `lecture.css` gets the bare structure it lays out |
| `exercises/` | The three 2026 exercise notebooks, exactly as issued |
| `exercises/solutions/` | Mario's worked solutions. Never edit an issued exercise in place |
| `reference/` | Four Python notebooks from the `wueth/AITools4Actuaries` GitHub repo |
| `data/` | Course data, unpacked from `Data.zip`. Gitignored, see below |
| `notes/` | Notes per lecture, in markdown |

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
  2021-07-20, from `https://www.bondora.com/en/public-reports`.
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
Rebuild them with:

```bash
bash scripts/fetch_lecture_figures.sh          # fetch what is missing
bash scripts/fetch_lecture_figures.sh --force  # re-fetch everything
```

The script reads the image list out of the HTML rather than carrying its own, so it stays
correct if a lecture is re-downloaded. Adding a lecture means adding one line to its `MAP`.
Note two traps it handles: the remote directories carry spaces (`Lecture 1_Use Case`) while the
figure directories inside them are hyphenated (`Lecture1-Use-Case_files`), so neither name can
be derived from the other; and `frMTPLNN3.png` is referenced by both lecture 4/5 and lecture 6,
which the flat `lectures/` layout collapses onto one path. The two copies are byte-identical
today, and the script compares rather than overwrites, so a future divergence gets shouted
about.

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
- **This repo stays private.** `lectures/`, `exercises/` and `reference/` hold the course
  authors' material rather than Mario's, so pushing to a public remote would republish it.
  `origin` is `github.com/supermarmar/actuarial_deep_learning`. Confirm it is private before
  any push, e.g. `gh repo view supermarmar/actuarial_deep_learning --json isPrivate`.
  Decided 29 August 2026.
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
