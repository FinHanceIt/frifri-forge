# Changelog

## v1.0.0 — 2026-06-24
- Initial release. 7-agent human-voice writing studio: `inkforge` (director) +
  `commission-desk`, `voice-caster`, `story-architect`, `the-pen`, `voice-editor`,
  `authenticity-qc`.
- Bespoke voice-per-assignment engine (`references/voice-spec-schema.md`).
- 8-point AI-tell spec (`references/ai-tells-checklist.md`) wired into `voice-editor` + `authenticity-qc`.
- Format playbooks for fiction, scripts, essays, long-form, marketing, academic-style.
- Integrity boundary (original/own work only; no "undetectable" claims).
- Real metrics via `scripts/textstats.py` (burstiness, TTR, transition density) + a
  two-text voice-distinctiveness check.
- Bilingual RO/EN (Romanian via the `romanian-grammar` skill).
