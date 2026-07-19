# Changelog

## v1.0.0 — 2026-06-26
- Initial release. 6-part guardrail studio: `guardforge` (the Warden) + `triage-scanner`,
  `security-sentinel`, `quality-warden`, `integrity-keeper`, `ethics-safety-guard`.
- Verdict gate: **PASS / PASS-WITH-FIXES / BLOCK** on a 5-level severity rubric with an
  ethics red-line veto (`references/severity-rubric.md`).
- Real Claude Code hooks (`hooks/hooks.json`): PreToolUse secret / protected-file guard,
  PreToolUse dangerous-command guard, PostToolUse advisory checks. Fail-open with the
  `GUARDFORGE_STRICT` toggle.
- Deterministic scanner `scripts/scan.py` (secrets, risky patterns, protected files,
  license flags) shared by the triage agent and the hooks.
- Guardian checklists + handoff contracts + hooks guide (`references/`).
- Defensive-only integrity boundary: no exploit / malware authoring, no bypass help, no
  "fully secure" guarantees.
- Bilingual RO/EN (Romanian via the `romanian-grammar` skill).
