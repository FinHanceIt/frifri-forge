# Handoff contracts — the Manuscript File and the seams

Everything for one assignment lives in a single **Manuscript File** the director owns. Each
agent reads the whole file and writes only its own section. No artifact is skipped silently.

## The Manuscript File
```
# MANUSCRIPT — <short title>
MODE: piece | quick | voice | de-AI
OPEN GATE: <none | integrity | scope | review>
NEXT ACTION: <one line>

## COMMISSION BRIEF        (commission-desk)
## VOICE CARD              (voice-caster)
## STRUCTURE MAP           (story-architect)   [omitted in quick mode]
## DRAFT                   (the-pen)
## EDITED DRAFT + CHANGELOG (voice-editor)
## QC VERDICT              (authenticity-qc)
```

## COMMISSION BRIEF schema (commission-desk owns)
- format · topic/ask · purpose · audience · length target · language(s) · register/tone ask
- constraints (must-include, must-avoid, deadline, platform)
- success criteria (what "good" means for THIS piece)
- integrity classification (from integrity-boundary.md) + PASS / PAUSE / STOP

## Edge contracts (producer → artifact → consumer → B accepts if → on reject)
1. commission-desk → COMMISSION BRIEF → voice-caster → "format, audience, length, integrity
   PASS all present" → if STOP, director refuses+redirects; if gaps, ask the user.
2. voice-caster → VOICE CARD → story-architect/the-pen → "every dial filled + a cadence
   sample" → if generic, re-cast.
3. story-architect → STRUCTURE MAP → the-pen → "format-appropriate + has a deliberate
   asymmetry note" → if it's a tidy 3-point skeleton, rebuild.
4. the-pen → DRAFT → voice-editor → "on-brief, on-voice, complete, no fabricated facts" →
   if off-voice, the-pen redrafts (not voice-editor).
5. voice-editor → EDITED DRAFT + CHANGELOG → authenticity-qc → "tells addressed, meaning &
   voice preserved" → see FIX loop.
6. authenticity-qc → QC VERDICT → director → "PASS, or a routed FIX list" → on FIX, loop.

## The FIX loop
authenticity-qc returns PASS or FIX. FIX routes by cause:
- tells still present / rhythm flat → `voice-editor` (re-edit).
- off-voice / wrong persona → `the-pen` then `voice-editor`.
- structure too tidy / wrong format → `story-architect`, then redraft.
- voice not distinct enough (voice_distance < 0.6 vs reference) → `voice-caster` re-casts.
Max 2 FIX cycles on the same cause; then the director surfaces the trade-off to the user.

## Gates (director holds)
- Gate 0 — Integrity (before drafting): brief must be PASS. STOP → refuse+redirect.
- Gate scope — confirm format, length, language, and the cast voice with the user before a
  long piece (skip for quick jobs).
- Gate review — user approves the finished piece; meaning intact, voice right.

End every turn with the single NEXT ACTION.
