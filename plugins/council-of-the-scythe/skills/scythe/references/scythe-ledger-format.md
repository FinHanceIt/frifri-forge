# Scythe-Ledger.md — canonical format

One file in the working folder. Only the-reckoner writes it. Append/edit rows; history is
never rewritten — corrections get a new row referencing the old one.

```markdown
# SCYTHE LEDGER
last-updated: {YYYY-MM-DD} · councils held: {n} · predictions: {n} ({n} resolved)

## ROSTER — current standing of every item
| item | class | verdict | ruled | attention | thaw condition (FREEZE) | next review | notes |
|---|---|---|---|---|---|---|---|
| WaveForge | plugin | IGNORE | 2026-07-07 | 0 | — | on evidence | self-running |

## PREDICTIONS — every verdict is a bet
| id | made | item | falsifiable claim | deadline | P(Fri) | P(council) | outcome | Brier(Fri) | Brier(council) |
|---|---|---|---|---|---|---|---|---|---|
| P-001 | 2026-07-07 | X | "≥1 paying user by 2026-10-01" | 2026-10-01 | 0.7 | 0.4 | — | — | — |

outcome ∈ TRUE / FALSE / UNRESOLVED-STALE (past deadline, no evidence — not scored)
Brier = (P − outcome)² with outcome TRUE=1, FALSE=0. Lower is better.

## OVERRIDES — where Fri and the council split
| id | date | item | council said (why) | Fri ruled (why) | linked prediction | resolved: who was right |
|---|---|---|---|---|---|---|

## CALIBRATION — computed only from resolved rows
- resolved: {n} · mean Brier(Fri): {x} · mean Brier(council): {x}
- by domain: {builder-track n, agency-track n — who wins where}
- pattern: {one honest sentence, or "insufficient data (n<5)"}

## GRAVEYARD — killed items (kills are wins: freed attention)
| item | killed | reason | what it taught |
|---|---|---|---|
```

Rules:
- A verdict without a prediction row is incomplete — the reckoner refuses to close.
- GATE entries log the trade in notes: "entered; victim: {item} (−{points})".
- Deferred items: verdict FREEZE, thaw = "next council", note `deferred-by-owner`.
