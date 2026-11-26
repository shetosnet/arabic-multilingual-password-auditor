#!/usr/bin/env bash
# Usage: ZYLA_API_KEY=your_key ./generate.sh [length 12-64]
set -euo pipefail
: "${ZYLA_API_KEY:?Set ZYLA_API_KEY first}"
LENGTH="${1:-16}"
curl --silent --show-error --location --request GET \
  "https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42106/generate+cryptographically+strong+password?length=$LENGTH" \
  --header "Authorization: Bearer $ZYLA_API_KEY"
echo
