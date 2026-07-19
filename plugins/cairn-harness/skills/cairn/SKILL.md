---
name: cairn
description: Run the Cairn verification crew on a coding task. Use when the user wants a change made safely with real verification — "use the crew", "run cairn", "build this with the gate", "harden then build", "audit-plan-implement-review". Routes the 5 agents (auditor -> planner -> roaster -> implementer -> reviewer), scales ceremony to risk, and runs the gate ladder. Only gates say PASS; the human gates twice.
---

# cairn — the verification crew

Five specialist agents in `agents/` do audit -> plan -> roast -> implement -> review. This skill is the operating manual: **who runs, in what order, and when NOT to run all of them.** Ceremony on a one-line change is the opposite of efficiency.

## The loop

```
AUDIT -> PLAN -> ROAST -> [human: go] -> IMPLEMENT -> REVIEW -> [human: commit]
```

- **Reads fan out. Writes stay single-threaded.** auditor / roaster / reviewer are read-only and may run in parallel. There is exactly **one implementer**, ever.
- **Only the gates say PASS.** The reviewer's judgement is advisory (REVISE/ADVISE). typecheck / test / mutation-gate decide correctness by exit code.
- **The human is a real gate twice:** the *go* after the roast (freeze the criteria) and the *commit* after review.

## Ceremony is a dial. Verification is not.

Do NOT run five agents on every tiny thing. Match the crew to the planner's risk class:

| Risk | What runs |
|---|---|
| **S** — typo, copy, one-line pure fn | implementer + reviewer's gate ladder |
| **M** — a function, a new pure helper | auditor -> planner -> implementer -> reviewer (roast optional) |
| **L** — touches a flow, a schema, core behavior | full loop incl. roaster + human gate |
| **XL** — auth, money, personal data, migrations, deletion | full loop, roaster REQUIRED, dual human gate, gate in `--enforce` on the touched files |

The dial is the ceremony. The **gate ladder never drops** — even an S change runs typecheck + test before commit.

## The gate ladder (what REVIEW runs)

1. `npm run typecheck` (or the repo's equivalent) — exit 0.
2. `npm run lint` — exit 0, or `missing` (never a fake pass).
3. `npm run test` — green; read the LAST result line (anti-echo).
4. `node scripts/mutation-gate.mjs` — **L2 assertion-integrity**, diff-scoped, **shadow by default**. It fires when the diff *reduces what is actually tested* (a deleted/gutted test that loses coverage). It is a coverage-loss detector, not a tamper detector.

Promote L2 to `--enforce` per-surface only after ~a dozen shadow runs show no false alarms.

## For non-technical / vibe-coder review

When the human must verify something, follow `references/human-gate-protocol.md`: a plain-language Gate Card — what is being proved (one jargon-free sentence), the literal command output, what it means, **how the agent could be lying at this gate**, and one action. See it before shipping.

## Setup

Run `/harden` once per repo (installs the gate, a baseline, and optional pre-commit + git guardrails). Then use the crew.

## Composes with mattpocock/skills

Cairn is the *measurement* layer. For the *discipline* layer install `npx skills add mattpocock/skills` — its `tdd`, `diagnose`, and `review` skills carry deep references (behavior-first tests, the diagnose loop) the implementer and reviewer here already point at. Cairn adds the one thing that stack lacks: a mutation gate that proves the tests actually catch regressions.
