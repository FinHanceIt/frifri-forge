# OriginForge

A 9-agent **originality & authenticity studio** for Fri. It tells you, honestly, whether a text reads as AI-written or plagiarized and what real detectors would flag — and it rewrites **your own** or AI-assisted drafts into genuinely human, original writing. Bilingual RO/EN.

## What it does (4 modes)
- **Detect / Verify** — "is this AI? is this plagiarized? what would get flagged, and why?" → an Originality Report with real metrics, similarity matches, and a per-engine estimate.
- **Defend** — your genuine writing got falsely flagged as AI → it explains *why* and makes light, truthful edits. (AI detectors misflag ~60% of non-native-English essays — false positives are real.)
- **Revise / Humanize** — your own / AI-assisted draft → natural, original, human-quality prose, with a residual-risk re-scan.
- **Full** — detect → revise → re-scan.

## The honest part (read this)
OriginForge improves **your own** work. By design it will **not**:
- disguise copied or third-party copyrighted text as original;
- help pass someone else's work off as yours where authorship is certified (exams, graded work that isn't genuinely yours);
- promise anything is "undetectable" or "beats every detector" — that claim is false, and detectors are unreliable both ways.

What it *does* guarantee is real quality and real originality — which is also what actually reads as human and survives the classifier-based detectors (Originality.ai, Pangram) that cheap "humanizers" fail against.

## The team
`forge-director` (orchestrator) · `ai-forensics` (AI-likelihood, with real metrics) · `plagiarism-scanner` (web similarity) · `engine-mirror` (what GPTZero/Turnitin/Originality.ai would say) · `humanizer` (de-AI editor) · `originality-transformer` (source handling + citation) · `voice-keeper` (your voice + audience) · `integrity-gate` (the boundary) · `qc-rescan` (honest final check).

## How to use it
Just say what you want, in RO or EN:
- "E scris cu AI textul ăsta?" / "Check this for AI."
- "Verifică plagiat / similaritate."
- "Ce-ar zice Turnitin/GPTZero?"
- "M-a marcat greșit ca AI — ajută-mă." / "Defend this against a false positive."
- "Humanizează draftul meu." / "Make my draft sound human and original."

The Director classifies the job, runs the right agents, stops at the integrity / scope / revision gates, and hands you one report plus a single next action.

## Notes
- Reasoning is in English; reports and rewrites come back in RO/EN (Romanian uses the `romanian-grammar` skill).
- `ai-forensics` and `qc-rescan` run a real metrics script (`scripts/textstats.py`) — burstiness, type-token ratio, transition density — so reads are measured, not vibes.
- Every number carries a caveat; every similarity match carries its source.

Honest, bilingual, no snake oil. v1.0.0 · MIT.
