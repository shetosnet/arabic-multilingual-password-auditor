#!/usr/bin/env python3
"""Audit a file of passwords (one per line) and save a MASKED csv report.
   ZYLA_API_KEY=... python audit_list.py passwords.txt report.csv
Respects the 60 requests/minute limit of the Basic plan. Mind your monthly quota (the free trial has 50 requests)."""
import csv
import sys
import time

import requests

from analyze import KEY, URL  # same folder


def mask(p):
    return p[:2] + "*" * (len(p) - 2) if len(p) > 2 else "**"


def csv_safe(v):
    v = str(v)
    return "'" + v if v and v[0] in "=+-@" else v     # avoid spreadsheet formula injection


def main(src, dst):
    with open(src, encoding="utf-8") as f:
        passwords = [line.strip() for line in f if line.strip()]
    counts = {"WEAK": 0, "MODERATE": 0, "STRONG": 0}
    with open(dst, "w", newline="", encoding="utf-8-sig") as out:
        w = csv.writer(out)
        w.writerow(["id", "masked_sample", "length", "score", "status", "issues"])
        for i, pwd in enumerate(passwords, 1):
            for attempt in range(3):
                r = requests.post(URL, headers={"Authorization": f"Bearer {KEY}"},
                                  json={"password": pwd, "check_cloud": False}, timeout=15)
                if r.status_code == 429:                      # rate limited: wait and retry
                    time.sleep(5)
                    continue
                r.raise_for_status()
                break
            res = r.json()
            counts[res["status"]] += 1
            w.writerow([i, csv_safe(mask(pwd)), res["length"], res["score"], res["status"],
                        csv_safe(" | ".join(res["vulnerabilities"]))])
            time.sleep(1.1)                                    # stay under 60 requests/minute
    print(f"Done: {len(passwords)} passwords -> {dst}  {counts}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python audit_list.py passwords.txt report.csv")
    main(sys.argv[1], sys.argv[2])
