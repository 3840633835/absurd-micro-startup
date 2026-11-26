#!/bin/sh
# Determinism test: main.py must produce byte-identical entry.txt on every run.
set -e
cd "$(dirname "$0")"
TMP1="$(mktemp -d)"
TMP2="$(mktemp -d)"
trap 'rm -rf "$TMP1" "$TMP2"' EXIT
OUTPUT_DIR="$TMP1" python3 main.py
OUTPUT_DIR="$TMP2" python3 main.py
cmp "$TMP1/entry.txt" "$TMP2/entry.txt"
cmp "$TMP1/entry.txt" entry.txt
# Exact byte count: 175, no trailing newline.
BYTES="$(wc -c < "$TMP1/entry.txt" | tr -d ' ')"
[ "$BYTES" = "175" ] || { echo "FAIL: entry.txt is $BYTES bytes, expected 175"; exit 1; }
# One sentence: exactly one sentence-ending period (the $0.10 decimal excluded).
ENDS="$(python3 -c "import re,sys; print(len(re.findall(r'\.(?=\s|\$)', open(sys.argv[1]).read())))" "$TMP1/entry.txt")"
[ "$ENDS" = "1" ] || { echo "FAIL: $ENDS sentence-ending periods, expected 1"; exit 1; }
echo "PASS: deterministic, 175 bytes, one sentence"
