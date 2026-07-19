# Guardian checklists (defensive signatures)

What each guardian sweeps for. These are **detection signatures and review questions** — the
job is to flag the bug class and prescribe the fix, never to write the exploit. Lists are
starting points, not exhaustive; use judgement and the project's own context.

## security-sentinel
**Secrets & keys** — committed API keys/tokens (AWS `AKIA…`, Google, Stripe `sk_live_…`,
GitHub `ghp_…`), private keys (`BEGIN … PRIVATE KEY`), `.env`/credentials written into VCS,
hardcoded passwords/connection strings. → report **masked**, never the live value.
**Injection** — untrusted input concatenated into SQL, shell, OS commands, file paths, or
LLM/system prompts; templating without escaping (XSS); SSRF from user-controlled URLs.
**Unsafe execution** — `eval`/`exec`/`Function()` on input; `pickle`/`yaml.load`/native
deserialization of untrusted data; `subprocess(..., shell=True)` with interpolation.
**AuthZ/AuthN** — missing access check, broken object-level authorization (IDOR), tokens
without expiry/verification, weak crypto (MD5/SHA1 for passwords, ECB, static IV/salt).
**Dependencies** — known-vulnerable/abandoned packages, install-time scripts, typosquats,
lockfile drift.
**Exfiltration / shell** — outbound calls sending secrets/PII; `curl … | bash`; network
calls added to a build step. *(For dangerous shell at tool-time, the Bash hook catches it.)*

## quality-warden
**Build & tests** — does it compile/build? tests present for new logic? any removed or now-
failing tests? assertions meaningful (not `assert true`)?
**Correctness** — off-by-one, null/None handling, race conditions, unhandled async
rejections, resource leaks (unclosed files/conns), wrong error type swallowed.
**Hallucinated APIs** — calls to functions/params/imports that don't exist in the declared
deps or stdlib; invented config keys; signatures that don't match the library version.
**Error handling** — bare `except: pass`, swallowed errors, logging secrets, missing timeouts
/ retries on I/O.
**Maintainability & perf** — dead code, copy-paste, N+1 queries, O(n²) on large input,
unbounded memory, missing pagination. *(Style/lint = LOW unless it hides a bug.)*

## integrity-keeper
**Licenses** — new dependency licenses vs the project's license; copyleft (GPL/AGPL) pulled
into proprietary/MIT; missing NOTICE/attribution; license incompatibility in bundling.
**Provenance** — code that looks copied from a specific source without attribution; large
verbatim blocks; "borrowed" snippets that carry a license.
**Data protection** — PII collected/logged/transmitted without basis; missing consent/
retention/anonymization; secrets or PII in fixtures, seeds, or test data; cross-border data
flows.
**Honesty of claims** — code/docs/marketing strings that assert "undetectable", "100%
secure/private", "guaranteed", "military-grade", or fake compliance badges → flag as
deceptive.
**VCS hygiene** — secrets in history, `.env`/keys not git-ignored, large binaries, generated
artifacts committed.

## ethics-safety-guard (holds the veto)
**Harmful capability** — is the change building malware, surveillance/stalkerware, credential
harvesters, weapons tech, fraud/scam tooling, or means to attack third-party systems?
**Minors** — anything that collects from, profiles, targets, or could endanger children;
age-inappropriate flows in a product aimed at or used by minors.
**Manipulation / dark patterns** — coercive defaults, deceptive consent, addictive loops
engineered to exploit, mass-persuasion/disinfo tooling.
**Dual-use** — legitimate security/automation that could be misused: allow with a note and
the safeguard, unless intent/targeting makes it a red line.
A red line → **veto / BLOCK**, name the line in one sentence. Ambiguous → flag HIGH and ask
the human for intent, don't accuse.
