# Examples

All examples read your key from the `ZYLA_API_KEY` environment variable. **Never commit your key.**

| Folder | File | What it does |
| :--- | :--- | :--- |
| `curl/` | `analyze.sh`, `generate.sh` | One-liners (need `curl` + `jq`) |
| `python/` | `analyze.py` | Analyze one password (`pip install requests`) |
| `python/` | `audit_list.py` | Audit a file of passwords, save a **masked** CSV (respects 60 req/min) |
| `python/` | `generate.py` | Generate a strong password |
| `node/` | `analyze.mjs` | Analyze one password (Node 18+) |
| `node/` | `signup-validation.mjs` | Backend check for sign-up / reset flows |
| `php/` | `analyze.php` | Analyze one password (PHP + cURL) |

```bash
export ZYLA_API_KEY=your_key
python examples/python/analyze.py 'Ahmed@01012345678'
node examples/node/analyze.mjs 'ضصثقفغعهخ'
```

Notes: the free trial has 50 requests, and only successful (HTTP 200) calls are counted. The remaining monthly quota is returned in the `X-Zyla-API-Calls-Monthly-Remaining` response header.
