#!/usr/bin/env bash
# Usage: ZYLA_API_KEY=your_key ./analyze.sh 'Ahmed@01012345678' [true|false]
# Needs: curl and jq (jq builds the JSON safely, even if the password contains quotes).
set -euo pipefail
: "${ZYLA_API_KEY:?Set ZYLA_API_KEY first}"
PASSWORD="${1:?Usage: analyze.sh <password> [check_cloud: true|false]}"
CHECK_CLOUD="${2:-false}"

jq -n --arg p "$PASSWORD" --argjson c "$CHECK_CLOUD" '{password: $p, check_cloud: $c}' |
curl --silent --show-error --location --request POST \
  'https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42105/analyze+password+strength+and+vulnerabilities' \
  --header "Authorization: Bearer $ZYLA_API_KEY" \
  --header 'Content-Type: application/json' \
  --data @-
echo
