#!/usr/bin/env bash
# Print a rendered lecture to PDF beside its HTML, using headless Chrome.
#
# Chrome rather than weasyprint or wkhtmltopdf, because every lecture pulls
# MathJax from a CDN and typesets its mathematics in JavaScript. A print engine
# with no script runtime emits the raw \frac{}{} instead, which looks like a
# successful conversion until somebody reads page four.
#
# Page size, margins and the print-colour treatment live in the @page and
# @media print blocks of lectures/lecture.css, not in the flags below, so that
# Cmd-P from the browser produces the same page this script does.
#
# --virtual-time-budget is what waits for MathJax. Chrome fast-forwards its
# timers, so the budget is not wall-clock, but the CDN fetch underneath it is
# real, which is why the value is generous. Each run gets its own throwaway
# profile directory: concurrent Chrome instances sharing one profile fight over
# its lock and one of them silently produces nothing.
#
# Chrome 152 writes the PDF and then declines to exit, so the loop below is a
# watchdog rather than a plain call: it waits for the file to appear and stop
# growing, then terminates the browser itself. macOS ships no timeout(1), which
# rules out the one-line version of this.
#
# Paths are required, matching render_lecture.sh. A no-argument default that
# swept both lecture directories would be a fifteen-minute job started by
# accident.
#
# Usage:
#   bash scripts/html_to_pdf.sh credit_lectures/01_credit-use-case.html
#   bash scripts/html_to_pdf.sh lectures/*.html
#   bash scripts/html_to_pdf.sh lectures/*.html credit_lectures/*.html

set -euo pipefail
cd "$(dirname "$0")/.."

CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
BUDGET="${BUDGET:-30000}"
WATCHDOG="${WATCHDOG:-180}"   # seconds to wait for the PDF to settle

if [[ $# -eq 0 ]]; then
  echo "usage: bash scripts/html_to_pdf.sh <lecture.html> [...]" >&2
  echo "  e.g. bash scripts/html_to_pdf.sh credit_lectures/*.html" >&2
  exit 2
fi
[[ -x "$CHROME" ]] || { echo "no Chrome at: $CHROME" >&2; exit 1; }

for html in "$@"; do
  [[ -f "$html" ]] || { echo "no such file: $html" >&2; exit 1; }
  pdf="${html%.html}.pdf"
  profile="$(mktemp -d)"
  # lecture.css is reached by a relative href, so the URL has to be absolute
  # and the spaces in the authors' _files directory names encoded.
  url="file://$(cd "$(dirname "$html")" && pwd)/$(basename "$html")"
  rm -f "$pdf"
  "$CHROME" \
    --headless=new \
    --disable-gpu \
    --user-data-dir="$profile" \
    --no-pdf-header-footer \
    --run-all-compositor-stages-before-draw \
    --virtual-time-budget="$BUDGET" \
    --print-to-pdf="$pdf" \
    "$url" >/dev/null 2>&1 &
  pid=$!

  size=0; steady=0
  for _ in $(seq "$WATCHDOG"); do
    sleep 1
    kill -0 "$pid" 2>/dev/null || break
    now=$(stat -f %z "$pdf" 2>/dev/null || echo 0)
    if [[ "$now" -gt 0 && "$now" -eq "$size" ]]; then
      steady=$((steady + 1))
      [[ "$steady" -ge 2 ]] && break
    else
      steady=0
    fi
    size="$now"
  done
  kill "$pid" 2>/dev/null || true
  wait "$pid" 2>/dev/null || true
  rm -rf "$profile"
  [[ -s "$pdf" ]] || { echo "produced nothing: $pdf" >&2; exit 1; }
  # The watchdog stops on a settled file size, so check the trailer rather than
  # trusting that a file which stopped growing had finished being written.
  tail -c 64 "$pdf" | grep -q '%%EOF' \
    || { echo "truncated, raise WATCHDOG: $pdf" >&2; exit 1; }
  echo "$(du -h "$pdf" | cut -f1)	$pdf"
done
