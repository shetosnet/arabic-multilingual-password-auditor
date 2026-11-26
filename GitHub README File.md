# Arabic & Multilingual Password Security Auditor API

A zero-knowledge, edge-deployed REST API designed to audit password strength, detect regional Arabic and Franco-Arab keyboard patterns, check against known data breaches via `k-anonymity`, and generate cryptographically secure passwords.

🔗 **Live API & 7-Day Free Trial:** [Get Your API Key on Zyla API Hub](https://zylalabs.com/api-marketplace/other/arabic+and+multilingual+password+auditor+api/15605)

---

## Why Traditional Password Checkers Fail in MENA & Multilingual Apps

Standard open-source libraries (such as `zxcvbn`) are built primarily around English dictionaries and QWERTY layouts. As a result, they often rate weak Arabic passwords as "strong" simply because they use non-Latin UTF-8 characters.

This API solves that gap by analyzing:
- **Arabic & Regional Keyboard Walks:** Detects adjacent key sequences on Arabic layouts (e.g., `ضصثقف`, `شسيبل`) alongside QWERTY/AZERTY patterns.
- **Franco-Arab, Regional Patterns & Leetspeak:** Catches localized patterns, regional phone numbers, and common substitutions (e.g., `Ahmed@01012345678`, `P@ssw0rd123`).
- **Privacy-First Breach Verification (`k-anonymity`):** Optionally checks passwords (`check_cloud: true`) against known leaked credential databases without ever transmitting or storing the full password.
- **Stateless Zero-Knowledge Architecture:** Hosted on global edge workers with zero database persistence—passwords are processed in memory and discarded immediately.

---

## Endpoints

| Method | Endpoint URL | Description |
| :--- | :--- | :--- |
| `POST` | `https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42105/analyze+password+strength+and+vulnerabilities` | Audits a password for entropy, keyboard walks, dictionary/leetspeak matches, and optional breach exposure. |
| `GET` | `https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42106/generate+cryptographically+strong+password` | Generates a verified high-entropy password (`length` query parameter: `12` to `64`, default `16`). |

---

## Quick Start Code Examples

### 1. cURL (`POST` Analyze Password)
```bash
curl --location --request POST 'https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42105/analyze+password+strength+and+vulnerabilities' \
  --header 'Authorization: Bearer YOUR_ZYLA_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"password": "Ahmed@01012345678", "check_cloud": false}'
```

### 2. Python (`requests`)
```python
import requests

url = "https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42105/analyze+password+strength+and+vulnerabilities"
headers = {
    "Authorization": "Bearer YOUR_ZYLA_API_KEY",
    "Content-Type": "application/json"
}
payload = {
    "password": "ضصثقف123",
    "check_cloud": True
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

### 3. JavaScript / Node.js (`fetch`)
```javascript
const response = await fetch(
  "https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42105/analyze+password+strength+and+vulnerabilities",
  {
    method: "POST",
    headers: {
      "Authorization": "Bearer YOUR_ZYLA_API_KEY",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      password: "ضصثقف123",
      check_cloud: false
    })
  }
);

const data = await response.json();
console.log(data);
```

### 4. Generate a Cryptographically Strong Password (`GET`)
```bash
curl --location --request GET 'https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42106/generate+cryptographically+strong+password?length=20' \
  --header 'Authorization: Bearer YOUR_ZYLA_API_KEY'
```

---

## Privacy & Free Trial
- **Zero Logging:** Input passwords are never written to disk, logs, or analytics.
- **AI Agent Ready:** Compatible with Zyla MCP Server (`mcp.zylalabs.com`) for automated agent workflows.
- **Start Free:** Includes a 7-day free trial (50 requests) on [Zyla API Hub](https://zylalabs.com/api-marketplace/other/arabic+and+multilingual+password+auditor+api/15605).