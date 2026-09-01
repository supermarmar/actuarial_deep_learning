#!/usr/bin/env bash
# Render a Quarto lecture and strip Quarto's theme assets from the output.
#
# lectures/lecture.css was written for the course authors' pages, which carry
# full Quarto markup (#quarto-content, #quarto-margin-sidebar, main.content)
# while their _files/libs/ assets were never downloaded, so Bootstrap and
# quarto.js are effectively absent. This script reproduces that structure for
# our own lectures: render with the default theme so the markup matches, then
# remove every <link> and <script> that points into _files/libs/ and delete
# the libs directory. MathJax loads from its CDN and is untouched.
#
# `theme: none` is not an alternative: it drops the wrapper markup itself, so
# the stylesheet's two-column rail never engages.
#
# Two kinds of .qmd go through here, and the only difference is the directory:
# credit_lectures/ holds Mario's credit risk companion lectures, and lectures/
# holds the three course lectures reconstructed from their PDF decks.
#
# Paths are required. A no-argument default that swept both directories would
# render the credit lectures too, and those execute Python against the Bondora
# parquet, which is gitignored, so a fresh clone would fail partway through on
# missing data rather than on anything to do with the lecture asked for.
#
# Usage:
#   bash scripts/render_lecture.sh lectures/08_icenet-regularization.qmd
#   bash scripts/render_lecture.sh lectures/*.qmd
#   bash scripts/render_lecture.sh credit_lectures/*.qmd

set -euo pipefail
cd "$(dirname "$0")/.."

QUARTO="${QUARTO:-$HOME/.local/bin/quarto}"
export QUARTO_PYTHON="$PWD/.venv/bin/python"

if [[ $# -eq 0 ]]; then
  echo "usage: bash scripts/render_lecture.sh <lecture.qmd> [...]" >&2
  echo "  e.g. bash scripts/render_lecture.sh lectures/*.qmd" >&2
  exit 2
fi
qmds=("$@")

for qmd in "${qmds[@]}"; do
  [[ -f "$qmd" ]] || { echo "no such file: $qmd" >&2; exit 1; }
  "$QUARTO" render "$qmd"
  html="${qmd%.qmd}.html"
  libs="${qmd%.qmd}_files/libs"
  .venv/bin/python - "$html" <<'EOF'
import re, sys

path = sys.argv[1]
raw = open(path).read()
# Drop every asset tag that points into the _files/libs/ directory: the
# Bootstrap and quarto-html stylesheets, and the bundled scripts (quarto.js,
# bootstrap.min.js, popper, tippy, anchor, clipboard, tabsets).
stripped = re.sub(
    r'[ \t]*<(?:link|script)[^>]*_files/libs/[^>]*>(?:</script>)?\n?', '', raw)
# quarto.js is gone, so its inline bootstrap call would throw on load.
stripped = re.sub(
    r'<script id="quarto-html-after-body".*?</script>\n?', '', stripped, flags=re.S)
open(path, "w").write(stripped)
removed = len(raw) - len(stripped)
print(f"stripped {removed:,} bytes of theme assets from {path}")
EOF
  rm -rf "$libs"
done
