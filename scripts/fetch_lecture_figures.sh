#!/usr/bin/env bash
#
# Fetch the lecture figures from the summer school site into lectures/.
#
# The seven lecture documents were downloaded as bare HTML, without the image
# files they reference. This script pulls those images so the plots and diagrams
# appear. They are gitignored, for the same reason data/ is: 5.6 MB of the course
# authors' binaries have no business in git history when a script can rebuild
# them.
#
# The list of images is read out of the HTML itself rather than hardcoded, so the
# script stays correct if a lecture is re-downloaded or another is added. Adding
# a lecture means adding one line to MAP below.
#
# Usage:
#   bash scripts/fetch_lecture_figures.sh           # fetch what is missing
#   bash scripts/fetch_lecture_figures.sh --force   # re-fetch everything
#
# Needs only curl. Safe to re-run.

set -uo pipefail

BASE="https://people.math.ethz.ch/~wueth/Lecture/SummerSchool2026"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LECTURES="$REPO/lectures"

FORCE=0
[ "${1:-}" = "--force" ] && FORCE=1

# Local file :: the directory it came from on the course site. The remote
# directory names carry spaces, and the figure directories inside them are
# hyphenated, which is why the two cannot be derived from each other.
MAP=(
  "01_use-case.html::Lecture 1_Use Case"
  "02_edf-glm.html::Lecture 2_EDF - GLM"
  "04-05_fnn.html::Lecture 4_5_FNN"
  "06_covariate-engineering.html::Lecture 6_Embedding Layers"
  "07_calibration.html::Lecture 7_Calibration"
  "09_localglmnet.html::Lecture 9_LocalGLMnet"
  "10-11_transformers.html::Lecture 10_11"
)

fetched=0; skipped=0; failed=0; conflicts=0
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

# Which lecture claimed each destination, so a filename used by two lectures can
# be compared rather than silently overwritten. frMTPLNN3.png is referenced by
# both lecture 4/5 and lecture 6, and the two copies were identical when this was
# written; a future divergence should be shouted about, not absorbed.
#
# A file rather than an associative array, because macOS ships bash 3.2 and
# `declare -A` arrived in bash 4.
registry="$tmp/claimed"
: > "$registry"

claimed_by() {   # prints the lecture that claimed $1, empty if unclaimed
  awk -F'\t' -v k="$1" '$1 == k { print $2; exit }' "$registry"
}

for entry in "${MAP[@]}"; do
  local_file="${entry%%::*}"
  remote_dir="${entry##*::}"

  if [ ! -f "$LECTURES/$local_file" ]; then
    printf '!! %s is missing, skipping its figures\n' "$local_file"
    continue
  fi

  printf '== %s\n' "$local_file"

  while IFS= read -r rel; do
    [ -z "$rel" ] && continue
    dest="$LECTURES/$rel"
    url="$(printf '%s' "$BASE/$remote_dir/$rel" | sed 's/ /%20/g')"

    # A second lecture wanting the same path: fetch to a temporary file and
    # compare, so a genuine difference surfaces instead of one copy winning.
    owner="$(claimed_by "$rel")"
    if [ -n "$owner" ]; then
      probe="$tmp/probe.png"
      if curl -fsS -L --max-time 60 -o "$probe" "$url" 2>/dev/null; then
        if cmp -s "$probe" "$dest"; then
          skipped=$((skipped+1))
          printf '   same   %s (also in %s)\n' "$rel" "$owner"
        else
          conflicts=$((conflicts+1))
          printf '   CLASH  %s differs between %s and %s. Kept the first.\n' \
                 "$rel" "$owner" "$local_file"
        fi
      fi
      continue
    fi
    printf '%s\t%s\n' "$rel" "$local_file" >> "$registry"

    if [ -s "$dest" ] && [ "$FORCE" -eq 0 ]; then
      skipped=$((skipped+1))
      printf '   have   %s\n' "$rel"
      continue
    fi

    mkdir -p "$(dirname "$dest")"
    if curl -fsS -L --max-time 60 -o "$dest" "$url" 2>/dev/null && [ -s "$dest" ]; then
      fetched=$((fetched+1))
      printf '   got    %7s  %s\n' "$(wc -c < "$dest" | tr -d ' ')" "$rel"
    else
      failed=$((failed+1))
      rm -f "$dest"
      printf '   FAIL   %s\n' "$rel"
    fi
  done < <(grep -o 'src="[^"]*\.png"' "$LECTURES/$local_file" | sed 's/src="//;s/"$//' | sort -u)
done

printf '\nfetched=%d  already present=%d  failed=%d  clashes=%d\n' \
       "$fetched" "$skipped" "$failed" "$conflicts"

# Report anything an HTML still asks for and cannot find.
missing=0
for entry in "${MAP[@]}"; do
  local_file="${entry%%::*}"
  [ -f "$LECTURES/$local_file" ] || continue
  while IFS= read -r rel; do
    [ -z "$rel" ] && continue
    [ -f "$LECTURES/$rel" ] || { printf 'still missing: %s (%s)\n' "$rel" "$local_file"; missing=$((missing+1)); }
  done < <(grep -o 'src="[^"]*\.png"' "$LECTURES/$local_file" | sed 's/src="//;s/"$//' | sort -u)
done

if [ "$missing" -eq 0 ] && [ "$failed" -eq 0 ]; then
  echo "every referenced figure is present"
  exit 0
fi
exit 1
