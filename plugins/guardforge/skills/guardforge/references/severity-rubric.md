# Severity rubric & the verdict gate

The single source of truth for how every guardian scores a finding and how the Warden turns
findings into one verdict. Defensive framing throughout: we rate **exposure and impact**, and
we always attach the fix.

## The five levels
| Level | Means | Examples (code/build) |
|---|---|---|
| **CRITICAL** | Ships real, exploitable harm now. Gate must BLOCK. | Live secret/key committed; SQL/command injection on user input; `eval`/pickle on untrusted data; auth bypass; RCE path; a license violation that legally blocks shipping; PII leaked to logs/3rd party without basis. |
| **HIGH** | Serious, very likely to bite; fix before merge. | Missing authz check; secret in history (not current); injection reachable only internally; no error handling on a critical path; failing/removed test on core logic; GPL dep linked into a proprietary product; hardcoded credentials in non-prod. |
| **MEDIUM** | Real issue, bounded blast radius; fix soon. | Weak input validation; broad `except: pass`; missing rate-limit; outdated dep with a known low-sev CVE; license needs attribution not yet added; PII retained longer than needed. |
| **LOW** | Minor / hygiene; advisory. | Lint/format drift; naming; a TODO left in; slightly risky but guarded pattern; missing a non-critical test. |
| **INFO** | Not a defect; context worth noting. | "This file handles auth — worth a closer human look"; "dep is fine but unmaintained." |

When unsure between two levels, state both and pick the higher only if exposure is plausible
on a realistic path. Don't inflate; don't bury.

## Confidence
Tag each finding `confidence: high | medium | low`. Low-confidence + high-severity → say
"possible" and tell the human exactly what to check. Never present a guess as a fact.

## The verdict (Warden aggregates)
After de-duping (highest severity per distinct issue):
- **BLOCK** — there is ≥1 open **CRITICAL**, **or** `ethics-safety-guard` raises a
  **red-line veto** (see below). BLOCK is never a refusal to help — it lists the exact fixes
  that turn it green.
- **PASS-WITH-FIXES** — no CRITICAL/veto, but ≥1 **HIGH** (or a meaningful cluster of MEDIUMs,
  e.g. ≥4 that compound). Ship only after the listed required fixes.
- **PASS** — only MEDIUM/LOW/INFO. Ship; advisories listed for later.

Always end with an **honest residual-risk line**: what this review did *not* cover, and that a
PASS is "no blocking issues found," not "proven safe."

## The veto (absolute)
`ethics-safety-guard` can force **BLOCK** regardless of other scores when a change crosses a
red line: building malware/weapons/abuse capability, targeting or endangering minors, or
enabling manipulation/coercion at scale. `security-sentinel` may escalate any finding to
CRITICAL when it proves exploitability on a realistic path. Vetoes are rare and must name the
line crossed in one sentence.

## Finding schema (every guardian emits this)
```
[<ID>] <SEVERITY> · <guardian> · confidence:<h/m/l>
  where:   <file>:<line>  (or "dependency: <name>", "command: <text>")
  what:    one line — the issue, concretely
  why:     one line — the impact / exposure if unfixed
  fix:     one line — the smallest change that resolves it
```
No location + no fix = not a finding; downgrade to INFO or drop it.
