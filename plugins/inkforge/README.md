# InkForge

A 7-agent **human-voice writing studio** for Fri. Give it a brief — a story, a script, an
essay, a chapter, an ad, an academic-style piece — and it drafts in a **bespoke author
voice with a distinct personality**, then runs a deliberate **de-AI pass** so the prose
reads like a real person wrote it, not like a model. Bilingual RO/EN.

## What it does
You bring the assignment; InkForge casts a writer for it and hands back a finished,
human-sounding draft. The studio:
1. takes the brief and checks it's legitimate (`commission-desk`),
2. **casts a bespoke voice** — a persona with its own rhythm, lexicon, biases and tics
   (`voice-caster`) — a different personality every time,
3. structures it for the format, on purpose *not* in the tidy AI shape (`story-architect`),
4. drafts it in that voice (`the-pen`),
5. strips the AI tells (`voice-editor`),
6. reads it back as a skeptical human and measures it (`authenticity-qc`).

## The 8 tells it kills (your list)
Low-perplexity/predictable phrasing · flat burstiness · uniform style · repeated patterns ·
over-orderly structure (intro + 3 tidy points + neat conclusion) · missing concrete/lived
specificity · unnatural consistency (no digressions, even quality) · AI vocabulary
(`moreover`, `furthermore`, `crucial`, `delve`; RO: `de asemenea`, `în plus`, `merită
menționat`, `în concluzie`). Spec: `skills/inkforge/references/ai-tells-checklist.md`.

## Modes
- **Piece** (default) — full pipeline, brief → finished draft.
- **Quick** — short copy / micro-pieces; skips the structure pass.
- **Voice** — just cast a reusable voice (a Voice Card) without drafting.
- **De-AI** — you bring your own draft; it humanizes and QC-checks it.

## The honest part (read this)
InkForge writes **your own and original work**. By design it will **not**:
- produce graded/credential work to be passed off as someone's own where authorship is
  attested (academic fraud);
- launder third-party or copyrighted text to dodge a plagiarism check;
- fabricate sources or citations;
- promise anything is "undetectable" or "beats AI detectors" — that claim is false.

What it actually does is make prose **genuinely human and specific**, which is also what
survives the serious detectors. Real voice, not tricks. Boundary:
`skills/inkforge/references/integrity-boundary.md`.

## The team
`inkforge` (director) · `commission-desk` (brief + integrity) · `voice-caster` (the
personality engine) · `story-architect` (format structure) · `the-pen` (drafts in voice) ·
`voice-editor` (de-AI pass) · `authenticity-qc` (skeptical re-read + metrics).

## How to use it
Just say what you want, in RO or EN:
- "Scrie-mi o poveste pentru copii despre un far singuratic." / "Write me a short story…"
- "Fă-mi un scenariu de 60s pentru reclama asta, ton sec." / "Write a 60s script…"
- "Scrie un eseu despre X, dar să nu sune a AI, voce de jurnalist obosit."
- "Humanizează draftul ăsta al meu." / "De-AI my own draft."
- "Dă-mi doar o voce pe care s-o refolosesc." / "Just cast me a voice."

The Director casts the writer, runs the pipeline, stops at the integrity / scope / review
gates, and hands you the finished piece plus a single next action.

## Notes
- Reasoning is in English; the writing comes back in RO/EN (Romanian via `romanian-grammar`).
- `voice-editor` and `authenticity-qc` run `scripts/textstats.py` for real numbers
  (burstiness, type-token ratio, transition density) and a two-text voice-distinctiveness
  check — voice is *measured*, not asserted.
- The drafting agents (`the-pen`, `voice-caster`, `voice-editor`) default to `opus`; swap to
  a creative-tuned model (e.g. Fable) for even more natural prose.

Honest, bilingual, voice-first. v1.0.0 · MIT.
