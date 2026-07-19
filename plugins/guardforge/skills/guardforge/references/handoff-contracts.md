# Handoff contracts — the Review File

How the Warden and guardians pass work without losing state. Keep it lightweight; the point
is one coherent verdict, not paperwork.

## The Review File (the Warden holds it)
```
mode:        REVIEW | QUICK | AUDIT | HOOKS | EXPLAIN
scope:       what's under review (paths / diff / repo / command) + what's explicitly out
language:    RO | EN | both
triage:      manifest from triage-scanner (deterministic findings)
findings:    accumulated, on the rubric schema, tagged by guardian
verdict:     PASS | PASS-WITH-FIXES | BLOCK  (+ residual-risk note)
gate:        which gate is open, if any
```

## Finding schema
Use the block from `severity-rubric.md` verbatim. Stable `ID`s (`SEC-1`, `QLT-2`, `INT-1`,
`ETH-1`) so the FIX loop and the user can refer to them.

## Routing
- Default order: **triage-scanner first** (cheap, deterministic, routes the rest), then the
  guardians the change touches, in parallel when independent.
- triage flags drive routing: secrets/injection/shell → `security-sentinel`; license/PII →
  `integrity-keeper`; failing build/tests → `quality-warden`; harmful-capability keywords →
  `ethics-safety-guard`. Always run security + quality on a code diff; add integrity when deps
  /data/licenses move; add ethics when the change's *purpose* (not just code) warrants it.

## The FIX loop
A BLOCK or PASS-WITH-FIXES returns required fixes by `ID`. When the user revises:
- re-run only the guardian(s) that owned the open findings + triage on the changed files;
- close fixed `ID`s, keep open ones, add any new ones the fix introduced;
- **max 2 cycles per cause** — then surface the trade-off to the user rather than looping.

## Gates (human-in-the-loop)
- **Gate scope** (AUDIT / large diffs): confirm what's in and out before a big sweep.
- **Gate verdict**: present the verdict + fixes; the user decides to fix, override (their
  call, logged in the note), or proceed. GuardForge never auto-applies fixes or overrules.

## Escalation
Disagreement between guardians on severity → take the higher, note the dissent in one line.
Anything touching the integrity boundary → `ethics-safety-guard` / boundary doc wins, full stop.
