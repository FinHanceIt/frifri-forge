# Changelog

## 1.0.0 — 2026-06-23
Initial release.

- 9-agent studio: `forge-director`, `ai-forensics`, `plagiarism-scanner`, `engine-mirror`, `humanizer`, `originality-transformer`, `voice-keeper`, `integrity-gate`, `qc-rescan`.
- Orchestrator skill `originforge` with 4 modes (detect, defend, revise, full) and 3 human gates (integrity, scope, revision).
- Shared brain: `ai-tells` (EN+RO), `detector-landscape` (2025-26 market map), `humanization-playbook`, `citation-originality`, `integrity-policy`, `handoff-contracts`, `report-templates`.
- Real metrics: `scripts/textstats.py` (burstiness, type-token ratio, transition density, AI-phrase hits; EN+RO; stdlib only).
- Integrity boundary baked in as a first-class gate: refuses laundering of copied/third-party content and academic-fraud use; bans "undetectable / guaranteed-to-pass" claims.
- Honesty spine: bands not fake precision; residual risk always reported; false-positive reality (Stanford 2023 ESL ~61%) cited.
- Bilingual RO/EN; Romanian output uses the `romanian-grammar` skill.
