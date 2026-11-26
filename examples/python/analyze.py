#!/usr/bin/env python3
"""Analyze one password.   ZYLA_API_KEY=... python analyze.py 'Ahmed@01012345678'   (pip install requests)"""
import getpass
import os
import sys

import requests

URL = os.environ.get("PA_ANALYZE_URL",
                     "https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42105/analyze+password+strength+and+vulnerabilities")
KEY = os.environ.get("ZYLA_API_KEY", "")


def analyze(password, check_cloud=False):
    """Returns (result_dict, remaining_monthly_calls_or_None)."""
    headers = {"Authorization": f"Bearer {KEY}"}
    r = requests.post(URL, headers=headers, json={"password": password, "check_cloud": check_cloud}, timeout=15)
    r.raise_for_status()
    return r.json(), r.headers.get("X-Zyla-API-Calls-Monthly-Remaining")


if __name__ == "__main__":
    if not KEY and "zylalabs.com" in URL:
        sys.exit("Set the ZYLA_API_KEY environment variable first.")
    pwd = sys.argv[1] if len(sys.argv) > 1 else getpass.getpass("Password to analyze: ")
    result, remaining = analyze(pwd, check_cloud="--cloud" in sys.argv)
    print(f"{result['status']} (score {result['score']}/100, true entropy {result['true_entropy']} bits)")
    print(f"Estimated resilience: {result['resilience']}")
    for line in result["vulnerabilities"]:
        print(" -", line)
    if result.get("recommended_alternative"):
        print("Suggested alternative:", result["recommended_alternative"])
    if remaining is not None:
        print(f"[API calls left this month: {remaining}]")
