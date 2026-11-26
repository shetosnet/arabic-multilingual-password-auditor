# Arabic & Multilingual Password Security Auditor API

A stateless REST API that audits password strength with Arabic-aware detection: keyboard walks on **Arabic, QWERTY and AZERTY** layouts, common Arabic/Egyptian names and words, **Arabizi** digits (`7`=ح, `3`=ع, `5`=خ), Egyptian mobile numbers, dates, leetspeak, and an optional **k-anonymity breach check**.

🔗 **API & 7-day free trial (50 requests):** [Zyla API Hub](https://zylalabs.com/api-marketplace/other/arabic+and+multilingual+password+auditor+api/15605)


---

## Promo Videos

**Arabic (0:52)**

https://github.com/user-attachments/assets/94fb3d90-c095-4476-a19f-a7b3f8337e1e

**English (0:48)**

https://github.com/user-attachments/assets/2cba0a9b-f079-421a-b25e-b0c92f286bbe

---

## Why generic checkers miss Arabic patterns

Generic estimators know English dictionaries and QWERTY. Tested with `zxcvbn` 4.4.2 (npm):

| Password | zxcvbn 4.4.2 (0-4) | This API |
| :--- | :---: | :---: |
| `ضصثقف123` | 2 | WEAK (0) |
| `شسيبل` | 1 | WEAK (7) |
| `ضصثقفغعهخ` | **3** | WEAK (7) |
| `Ahmed@01012345678` | **3** | WEAK (37) |
| `a7med.3ali` | **3** | WEAK (38) |
| `azertyuiop` | 1 | WEAK (0) |
| `k9#Xv!2mQ@7zLp$w` | 4 | STRONG (100) |

`zxcvbn` gives a full Arabic keyboard row, a name + phone number, and an Arabizi name a **3 ("safely unguessable")**. This API marks all of them WEAK.

## What it detects
- **Keyboard walks** on Arabic, QWERTY and AZERTY layouts. A walk costs almost all the entropy of the characters it covers.
- **Dictionary words + substitutions:** about 10,000 common passwords, 240+ Arabic/Egyptian names and words, leetspeak (`P@ssw0rd`) and Arabizi (`mo7amed`, `a7med`).
- **Arabic typed on an English keyboard** (e.g. `lpl]` = محمد), and Arabic-Indic digits (`٠١٢٣`).
- **Personal-data patterns:** Egyptian mobile numbers (010/011/012/015), dates (DDMMYYYY / YYYYMMDD), years.
- **Optional breach check** (`check_cloud: true`) through Have I Been Pwned using k-anonymity (only the first 5 characters of the SHA-1 hash are sent).

## Endpoints

| Method | URL | Description |
| :--- | :--- | :--- |
| `POST` | `https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42105/analyze+password+strength+and+vulnerabilities` | Analyze a password. Body: `{"password": "...", "check_cloud": false}` |
| `GET` | `https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42106/generate+cryptographically+strong+password` | Generate a verified strong password (`length` 12-64, default 16). |

Passwords longer than 256 characters are truncated (`"truncated": true`). Every finding has the shape `{"code": "...", "params": {...}}`, and `params` is **always an object** (`{}` when empty).

## Quick start

```bash
curl --location --request POST 'https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42105/analyze+password+strength+and+vulnerabilities' \
  --header 'Authorization: Bearer YOUR_ZYLA_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"password": "Ahmed@01012345678", "check_cloud": false}'
```

```python
import requests
r = requests.post("https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42105/analyze+password+strength+and+vulnerabilities",
    headers={"Authorization": "Bearer YOUR_ZYLA_API_KEY"},
    json={"password": "ضصثقفغعهخ", "check_cloud": False}, timeout=10)
print(r.json()["status"])   # WEAK
```

> **Call the API from your backend, never from the browser**, so your API key stays secret.

### Example response
```json
{
    "length": 17,
    "truncated": false,
    "is_passphrase": false,
    "scripts": [
        "Lowercase",
        "Uppercase",
        "Digits",
        "Symbols"
    ],
    "raw_entropy": 111.43,
    "true_entropy": 31.88,
    "score": 37,
    "status": "WEAK",
    "resilience": "Instant (< 1 second)",
    "cloud_audit": "Skipped (Offline Mode)",
    "findings": [
        {
            "code": "name_found",
            "params": {
                "word": "ahmed"
            }
        },
        {
            "code": "phone",
            "params": {}
        }
    ],
    "vulnerabilities": [
        "Contains a common name or local word: 'ahmed'",
        "Looks like a phone number"
    ],
    "compliance": {
        "Standard_Policy": {
            "passed": false,
            "reasons": [
                "True Entropy < 50.0 bits"
            ]
        },
        "Enterprise_Strict": {
            "passed": false,
            "reasons": [
                "True Entropy < 65.0 bits"
            ]
        }
    },
    "recommended_alternative": "L!3+5s_sK@+QNDpH"
}
```

## Privacy and limits
- This service does **not store or log** the passwords it receives, and keeps them in memory only while analyzing.
- Requests pass through **Zyla API Hub's gateway**; see their [privacy policy](https://zylalabs.com/terms#privacy). Avoid sending real production passwords you cannot afford to expose; for sign-up forms, prefer analyzing in your own backend over HTTPS.
- Scoring is an **estimate** (entropy + patterns), not a cracking tool. A password built from words that are not in the dictionaries can score higher than it deserves, and passphrases of uncommon words are scored by characters, not words.
- The policies `Standard_Policy` and `Enterprise_Strict` are this API's own baselines, **not** NIST SP 800-63B.
- Common-password list: [SecLists](https://github.com/danielmiessler/SecLists) (MIT).

## Examples

Ready-to-run code in [`examples/`](examples/): **cURL, Python (single + batch audit), Node.js (including a sign-up validation helper), PHP**. See [`examples/README.md`](examples/README.md).

```bash
export ZYLA_API_KEY=your_key
python examples/python/analyze.py 'Ahmed@01012345678'
```

## License
MIT (examples). See [LICENSE](LICENSE).
