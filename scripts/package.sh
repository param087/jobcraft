#!/usr/bin/env bash
# Validate and build the submission ZIP for the plugin directory.
set -euo pipefail

cd "$(dirname "$0")/.."

python3 scripts/validate.py

VERSION="$(python3 -c 'import json;print(json.load(open("plugin.json"))["version"])')"
OUT_DIR="dist"
OUT="$OUT_DIR/career-copilot-$VERSION.zip"

mkdir -p "$OUT_DIR"
rm -f "$OUT"

zip -r -q "$OUT" plugin.json skills assets README.md LICENSE \
  -x '*.DS_Store' -x '*/__pycache__/*'

echo "Built $OUT"
unzip -l "$OUT"
