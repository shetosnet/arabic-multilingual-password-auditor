// Server-side password check for a sign-up / password-reset flow (Node 18+).
// IMPORTANT: call this from your BACKEND over HTTPS. Never put the API key in browser code,
// and never log the password.
const URL_ = process.env.PA_ANALYZE_URL ??
  "https://zylalabs.com/api/15605/arabic+and+multilingual+password+auditor+api/42105/analyze+password+strength+and+vulnerabilities";

export async function validatePassword(password, { checkCloud = true } = {}) {
  let res;
  try {
    res = await fetch(URL_, {
      method: "POST",
      headers: { Authorization: `Bearer ${process.env.ZYLA_API_KEY}`, "Content-Type": "application/json" },
      body: JSON.stringify({ password, check_cloud: checkCloud }),
      signal: AbortSignal.timeout(5000),
    });
  } catch {
    return { ok: true, reasons: [], degraded: true };   // network failure: decide your own policy (fail open here)
  }
  if (!res.ok) return { ok: true, reasons: [], degraded: true };
  const data = await res.json();
  return {
    ok: data.status !== "WEAK",
    score: data.score,
    reasons: data.vulnerabilities,                       // human-readable English; use data.findings[].code to localize
    suggestion: data.recommended_alternative,
  };
}

// Example (Express):  const r = await validatePassword(req.body.password);  if (!r.ok) return res.status(400).json(r);
