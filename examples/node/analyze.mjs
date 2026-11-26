// Analyze one password (Node 18+).   ZYLA_API_KEY=... node analyze.mjs 'ضصثقفغعهخ'
const URL_ = process.env.PA_ANALYZE_URL ??
  "https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42105/analyze+password+strength+and+vulnerabilities";
const KEY = process.env.ZYLA_API_KEY ?? "";

const password = process.argv[2];
if (!password) { console.error("Usage: node analyze.mjs <password>"); process.exit(1); }
if (!KEY && URL_.includes("zylalabs.com")) { console.error("Set ZYLA_API_KEY first."); process.exit(1); }

const res = await fetch(URL_, {
  method: "POST",
  headers: { Authorization: `Bearer ${KEY}`, "Content-Type": "application/json" },
  body: JSON.stringify({ password, check_cloud: false }),
});
if (!res.ok) { console.error("Request failed:", res.status, await res.text()); process.exit(1); }

const data = await res.json();
console.log(`${data.status} (score ${data.score}/100, ${data.true_entropy} bits)`);
data.vulnerabilities.forEach((v) => console.log(" -", v));
