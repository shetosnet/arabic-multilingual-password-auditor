#!/usr/bin/env python3
"""Generate a strong password.   ZYLA_API_KEY=... python generate.py 20"""
import os
import sys

import requests

URL = os.environ.get("PA_GENERATE_URL",
                     "https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42106/generate+cryptographically+strong+password")
length = int(sys.argv[1]) if len(sys.argv) > 1 else 16
r = requests.get(URL, params={"length": length}, headers={"Authorization": f"Bearer {os.environ.get('ZYLA_API_KEY', '')}"}, timeout=15)
r.raise_for_status()
print(r.json()["generated_password"])
