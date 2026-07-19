# Ship Ledger — format

The sentinel's persistent memory of the whole pipeline. One row per artifact. State is
computed from **evidence**, never assumed. Killed items stay logged (they are learning),
never deleted.

## Columns
`artifact | state | blocking gap | next action (ONE) | days-stuck | verdict | last-touched`

- **state**: NEEDS-BUILD · READY-TO-DEPLOY · DEPLOYED-UNPROVEN · LIVE-PROVEN · FROZEN · KILLED
- **verdict**: SHIP (do the next action now) · FREEZE (parked on purpose, with a revisit date) · KILL (stopped, with the honest reason)
- **rule**: exactly one next action per row; anything **>14 days stuck** with no movement is forced to SHIP-or-KILL — no permanent limbo.

## Example row
`BrainBridge | NEEDS-BUILD | no code yet, only a build prompt | paste the build prompt into Claude Code, get a running local build | — | SHIP | 2026-07-07`

## Seed candidates — UNVERIFIED
From the fleet memo these looked stuck as of 2026-07-07. **Do not treat as fact** — run
triage on each before trusting the state. Listing them is a starting queue, not a claim.

- ChronoForge — packaged, not yet live-tested → candidate SHIP (run one real prediction end-to-end).
- MirrorChat — scaffold, not yet run → candidate SHIP or FREEZE.
- Telegram↔Claude bridge — built, not yet run → candidate SHIP (start it once).
- BrainBridge — build prompt only, no code → candidate SHIP (generate the build) or KILL.
- FleetView worker — blocked on pasting service_role → candidate SHIP (one paste unblocks live mode).
- FellaForge — validated concept (7.6), Phase-0 prototype not built → candidate SHIP (cheap prototype test) or FREEZE.

The point of the ledger is not to feel busy. It is to make sure every item is either
moving toward live or honestly dead — nothing rotting in the middle.
