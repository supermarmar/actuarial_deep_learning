#!/usr/bin/env bash
# Render a credit lecture and strip Quarto's theme assets from the output.
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
# Usage:
#   bash scripts/render_credit_lecture.sh                  # all credit lectures
#   bash scripts/render_credit_lecture.sh 01_credit-use-case.qmd

set -euo pipefail
cd "$(dirname "$0")/.."

QUARTO="${QUARTO:-$HOME/.local/bin/quarto}"
export QUARTO_PYTHON="$PWD/.venv/bin/python"

if [[ $# -gt 0 ]]; then
  qmds=("$@")
else
  qmds=(credit_lectures/*.qmd)
  qmds=("${qmds[@]#credit_lectures/}")
fi

for qmd in "${qmds[@]}"; do
  "$QUARTO" render "credit_lectures/$qmd"
  html="credit_lectures/${qmd%.qmd}.html"
  libs="credit_lectures/${qmd%.qmd}_files/libs"
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
