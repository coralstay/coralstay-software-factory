#!/usr/bin/env bash
# 에이전트_레일_파이프라인.html → .pdf 재생성.
# HTML이 원본이고 PDF는 생성물이다 — HTML을 고친 뒤 이 스크립트를 다시 돌린다.
# (GitHub은 저장소 안의 .html을 렌더하지 않고 .pdf는 렌더하므로, 읽기용으로 PDF를 함께 둔다.)
set -euo pipefail
cd "$(dirname "$0")"

SRC="에이전트_레일_파이프라인.html"
OUT="에이전트_레일_파이프라인.pdf"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"

[ -x "$CHROME" ] || { echo "Chrome을 찾을 수 없다: $CHROME (CHROME=... 로 지정)" >&2; exit 1; }

# mermaid가 그려질 시간을 주기 위해 virtual-time-budget을 넉넉히 준다.
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=30000 --run-all-compositor-stages-before-draw \
  --print-to-pdf="$OUT" "file://$PWD/$SRC" 2>/dev/null

echo "생성: $OUT ($(du -h "$OUT" | cut -f1))"
