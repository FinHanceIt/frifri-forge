# OfertaForge — Learning Loop (memory & self-improvement)
*Shared by Deal Lead and Ledger Keeper. This is how OfertaForge gets better every run instead of starting from zero.*

## What this is (and isn't)
The loop is **file-based memory**, not model retraining. Each run reads the curated lessons from past deals and writes back what it learned. Over time the *promoted playbook* compounds. It does **not** change any model's weights — it changes what the team knows going in. Honest framing: the "improvement" is better context, not a smarter model.

## Where memory lives
One ledger per install, **outside** the read-only plugin, at:

`~/.forge/ofertaforge/LEDGER.md`

Create it from `memory/LEDGER.template.md` on first run. Fallback if home isn't writable: `./.forge-memory/ofertaforge/LEDGER.md`. (This path is a convention; if you change it, update it everywhere it appears — this file, `SKILL.md`, `deal-lead.md`, `ledger-keeper.md`, `handoff-contracts.md`, and the template.)

**Privacy:** first name + tier + service only. No emails, phones, full company dossiers, and never the internal floor/margin.

## The loop
**Read at start — Deal Lead, Step 0.** Open the ledger's `## PROMOTED PLAYBOOK`. Pull the ≤5 lessons whose tags match this run (client tier · service · situation type). Carry them in the Deal File as `prior_lessons[]`. Empty or missing ledger → say so in one line and proceed. Never invent past deals.

**Write at end — Ledger Keeper, Step 5.** After Gate 3 (or whenever an outcome is known), append one `Ledger Entry`, then update the playbook and the calibration tally.

## Ledger Entry schema
```
## <YYYY-MM-DD> · <deal-slug> · <situation_type>
tags: <tier: Individual-RO|SMB-RO|EU|US> · <service> · <complexity>
did: <the 2–4 moves that mattered — anchor level, tier chosen, concessions traded, cadence>
predicted_win: <X%>          # Deal Lead's honest win-likelihood at the Send gate
outcome: WON | LOST | GHOSTED | PENDING    # PENDING until Fri confirms — never guess
value: <final signed amount + currency, only if WON>
worked: <one concrete signal>
friction: <one concrete signal>
lesson: <one reusable, falsifiable rule>
promote: yes | no
```

## Promotion rules (keep context small)
- Only `promote: yes` lessons rise into `## PROMOTED PLAYBOOK`.
- A promoted lesson is **one tagged, actionable line** ("EU · web: opening anchor at 1.4× target held in 4/5 deals").
- **Dedupe:** a new lesson that repeats an existing one doesn't get a second line — increment its evidence count instead ("(seen 5×)").
- **Decay:** a promoted lesson contradicted by 2 later outcomes is demoted back to the LOG with a struck note. No lesson is permanent.
- **Cap** the playbook at ~25 lines. When full, drop the lowest-evidence lesson.

## Calibration (this team has a real truth: won / lost)
- Every entry logs `predicted_win` vs the real `outcome`.
- Ledger Keeper keeps a `## CALIBRATION` block: rolling win-rate by tier + a blunt honesty note ("said 70%+ on 8 deals, won 5 → mild overconfidence").
- This is the **only** place OfertaForge scores itself. Use it to correct anchor aggressiveness and win/walk calls — never to inflate confidence.

## Honesty guards (non-negotiable — inherits house-style)
- Never fabricate an outcome, a signed value, or a lesson. Unknown = PENDING.
- A lesson must be earned from a real logged outcome, not a hunch.
- Never write client PII or the internal floor/margin into the ledger.
