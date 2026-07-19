# GuardForge

A 6-part **guardrail studio** for build & code work. Point it at a change — a diff, a
file, a pull request, a whole repo — and a team of **guardian agents** reviews it and
returns one verdict: **PASS / PASS-WITH-FIXES / BLOCK**, with every finding pinned to a
line and a fix. It ships with **real Claude Code hooks** that catch the dangerous stuff
automatically, before it lands. Bilingual RO/EN.

## What it does
You bring a change; GuardForge gates it. The studio:
1. runs a fast **deterministic scan** — secrets, dangerous commands, protected files,
   license flags (`triage-scanner` + `scripts/scan.py`),
2. routes the change to the guardians that matter,
3. **judges it across four fronts** and collects findings by severity,
4. issues **one verdict** with a required-fix list and an honest residual-risk note.

## The guardians
- `security-sentinel` — secrets & keys, injection (SQL / command / prompt), unsafe
  `eval`/deserialize, risky deps, data-exfiltration & dangerous shell. *(defensive
  detection only — it names the bug class and the fix, never a weaponized exploit.)*
- `quality-warden` — broken builds, missing or newly-failing tests, lint/format,
  hallucinated or non-existent APIs, swallowed errors, obvious perf footguns.
- `integrity-keeper` — OSS license compatibility, copied / un-attributed code, PII &
  GDPR handling, secrets-in-VCS policy, provenance, and no deceptive claims.
- `ethics-safety-guard` — does the change build harmful capability, target minors, or
  enable manipulation / dark patterns? Holds the **red-line veto**.
- `triage-scanner` — the deterministic first pass that the hooks also fire.

## The hooks (the "stil hooks" part)
Real Claude Code hooks, wired in `hooks/hooks.json`:
- **PreToolUse · Write|Edit|MultiEdit** → block writing a secret, or writing to a
  protected file (`.env`, private keys, credential stores).
- **PreToolUse · Bash** → block or *ask* on dangerous commands (`rm -rf /`,
  `curl … | bash`, force-push to `main`, `chmod 777`, fork bombs, disk `dd`…).
- **PostToolUse · Write|Edit** → advisory: run the project's formatter / linter / tests
  if a known config is present.
Fail-open by default so a hook never wedges your session; set `GUARDFORGE_STRICT=1` to
fail-closed (a parse error or scanner crash then blocks instead of allowing).

## Modes
- **Review** (default) — gate a change end-to-end.
- **Quick** — single file / small diff; security + quality only.
- **Audit** — whole-repo sweep before a release.
- **Hooks** — install or explain the automatic hooks.
- **Explain** — one finding: why it's flagged and how to fix it.

## The honest part (read this)
GuardForge is a **defensive reviewer**. By design it will **not**:
- write exploits, malware, or attack tooling — not even as a "proof of concept"; it names
  the vulnerability class and the remediation instead;
- help disable, bypass, or evade someone else's security, license terms, or detectors;
- promise anything is "100% secure", "fully safe", or "guaranteed compliant" — security is
  risk reduction, not a guarantee.
It advises; **you decide and own the call**. Boundary:
`skills/guardforge/references/integrity-boundary.md`.

## The team
`guardforge` (the Warden / director) · `triage-scanner` · `security-sentinel` ·
`quality-warden` · `integrity-keeper` · `ethics-safety-guard`.

## How to use it
Say what you want gated, in RO or EN:
- "Verifică diff-ul ăsta înainte să-l comit." / "Gate this diff before I commit."
- "Audit de securitate pe repo înainte de release." / "Security audit before release."
- "E ok să trec schimbarea asta?" / "Is this change safe to ship?"
- "Instalează-mi hooks-urile de guardrail." / "Install the guardrail hooks."
- "De ce a picat finding-ul ăsta și cum îl repar?" / "Why did this flag — how do I fix it?"

The Warden runs the deterministic scan, routes the guardians, holds the veto, and hands you
one verdict + the single next action.

## Notes
- Reasoning is in English; the verdict comes back in RO/EN (Romanian via `romanian-grammar`).
- `triage-scanner` runs `scripts/scan.py` for real, repeatable findings — not vibes.
- Heavy-judgment guardians (`security-sentinel`, `ethics-safety-guard`) default to `opus`;
  `quality-warden` and `integrity-keeper` to `sonnet`; `triage-scanner` to `haiku`.

Defensive, bilingual, honest. v1.0.0 · MIT.
