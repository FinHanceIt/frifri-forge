# Statecraft — National Ledger schema

`the-registrar` owns `National-Ledger.md` — the persistent state of the nation across the
whole session (and across sessions if Fri keeps the file). Everything here is `sim-canon`
unless tagged `verified`. Indices are simulation instruments, never real polling/forecasts.

## Structure
```
# NATIONAL LEDGER — {nation}
IDENTITY: name · anchor (real country / fictional) · regime (from the-charter) · era · turn #
VITALS (each 0–100 index or labeled unit, with a one-line why):
  treasury: {balance, band: surplus/balanced/deficit/crisis}
  debt: {debt/GDP band}
  economy: {growth band, unemployment band, inflation band}
  public-trust: {0–100}     legitimacy: {0–100}
  unrest: {0–100}           intl-standing: {0–100}
  cohesion: {0–100}         state-capacity: {0–100}
FACTIONS: {party/bloc · rough support % · in coalition? · top demand}
POPULATION: {size band · key cleavages: region/class/age/ethnicity/urban-rural}
ACTIVE LAWS: {short list of enacted policies still in force, with turn enacted}
PENDING EVENTS: {scheduled or brewing — from the-oracle / the-warden-of-crises}
TIMELINE: {turn → what happened, one line each}
DECISIONS LOG: {turn → decision → who dissented → effect}
```

## Update discipline (TICK and after every enactment)
- Move indices in **bands and small steps** with a stated cause; never invent false
  precision ("trust 61.3%"). Prefer "trust: 58 → 52 (fuel tax hit low-income households)".
- Every change traces to a decision or a fired event. No orphan drift.
- Trade-offs are conserved: a win somewhere usually costs something somewhere (treasury,
  trust, a faction, international standing). If nothing is spent, say why.
- Use `Edit`, never rewrite the ledger from memory. The ledger is the truth; seats read
  it before arguing.

## How seats use it
- `the-mandarin` costs options against current vitals.
- Ministries argue from their portfolio's numbers.
- `the-citizenry`/`the-press` react to trust/unrest deltas.
- `the-oracle` seeds PENDING EVENTS; `the-warden-of-crises` fires the sharp ones.
- `the-auditor` audits whether the ledger and the decisions actually match.
