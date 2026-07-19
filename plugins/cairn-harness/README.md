# cairn-harness

**A verification harness for AI coding agents.** A five-agent crew that audits → plans → roasts → implements → reviews, and a mutation-testing gate that catches an agent weakening or deleting a test. The gate produces the evidence; the agent never does.

Ships **shadow-first** — it watches and records before it ever blocks.

> Status: 0.2.0. Works as a Claude Code plugin **and** an `npx` installer (agents + gate + skills). MIT.

## Why

Coding agents cheat their test gates — measured, not assumed. ImpossibleBench ([arXiv:2510.20270](https://arxiv.org/abs/2510.20270)): GPT-5 exploited test cases 76% of the time, and Claude-family models specifically tend to *modify the tests*. Cursor (2026): reward hacking is *more* common on newer models. Every shipped defense proves the tests **ran** or that nobody **edited** them — none proves the tests still **assert anything**.

Cairn's L2 gate does. It mutation-tests the changed files and compares the score to a baseline: if the diff **reduces what is actually tested** (a gutted or deleted test), the score drops and the gate fires. It correctly stays silent when a test is merely made uglier but coverage holds — because no hole opened. It is a **coverage-loss detector**, deterministic, no LLM in the loop.

Proven on a real repo: deleting a test that uniquely covered a function dropped the mutation score 58.6% → 50.6% → **BLOCK**.

## The crew

`agents/` — five specialists Claude Code calls by name:

| Agent | Role | Writes? |
|---|---|---|
| `the-auditor` | read-only recon: what exists, what's tested, where the holes are | no |
| `the-planner` | frozen plan, machine-checkable criteria, smallest diff, risk class | plan file only |
| `the-roaster` | red-teams the plan before any code | no |
| `the-implementer` | the ONLY writer. test-first, one bounded task | source |
| `the-reviewer` | runs the gate ladder + two-axis review. advisory, never PASS | no |

**Reads fan out; writes stay single-threaded.** Only the gates say PASS. The human gates twice (after the roast, after review).

## Ceremony is a dial. Verification is not.

Don't run five agents on a typo. `/cairn` scales the crew to the planner's risk class (S → just implementer + gate; XL → full loop + roaster + dual human gate + enforce). The **gate ladder never drops** — even a one-line change runs typecheck + test.

## Install

Two ways, same source.

**As an `npx` installer** (any repo, any terminal — including a plain shell or the Antigravity terminal):

```sh
npx cairn-harness init                 # drops agents + skills into ./.claude and the gate into ./scripts,
                                       # and adds `gate` / `gate:baseline` npm scripts (non-destructive)
npx cairn-harness gate --since main    # run the mutation gate directly, diff-scoped
```

Before it's on npm, run it straight from GitHub (no publish needed):

```sh
npx github:FinHanceIt/cairn-harness init
```

**As a Claude Code plugin** — install the `.plugin`, then in any repo:

```sh
/harden          # installs the gate + baseline, optional pre-commit + git guardrails
/cairn <task>    # run the crew
```

The gate is plain Node and runs in **any** terminal. The agents + skills activate in a Claude Code-compatible runtime. The gate needs a mutation runner in the target repo (`npm i -D vitest @stryker-mutator/core @stryker-mutator/vitest-runner`) and `SRC_DIRS` in `scripts/mutation-gate.mjs` set to your source layout — `init` prints both reminders.

## Composes with mattpocock/skills

Cairn is the **measurement** layer. For the **discipline** layer, install [`mattpocock/skills`](https://github.com/mattpocock/skills) (MIT):

```sh
npx skills add mattpocock/skills
```

Its `tdd` (behavior-first, no implementation coupling), `diagnose` (reproduce → fix → regression), and `review` (two-axis) skills carry the deep reference material the Cairn implementer and reviewer already point at. **Cairn adds the one thing that stack lacks: a gate that proves the tests actually catch regressions.** Discipline + measurement = the whole loop. Full credit and attribution in `LICENSE`.

## For non-technical / vibe-coder review

`references/human-gate-protocol.md` — every time the agent needs you to verify something, it stops and gives you a plain-language **Gate Card**: what it's proving (one jargon-free sentence), the literal output, what it means, **how it could be lying to you at that gate**, and one action. You can't be the gate for something you don't understand.

## Honest limits — read before trusting it

- The L2 gate is a **coverage-loss** detector, **not** a tamper detector. It catches a diff that reduces what's tested; it does not, by itself, stop someone *touching* a test file (that's a future hash-seal step).
- **Everything is only as good as the repo's tests.** On a repo with weak tests, the gate has little to stand on — and `/harden` will tell you the real baseline rather than flatter you.
- Mutation testing costs seconds-to-minutes per run, so the gate is **diff-scoped** and runs at review boundaries, not every loop.
- No RCT proves this recovers the productivity these tools can cost (METR, [arXiv:2507.09089](https://arxiv.org/abs/2507.09089), found early-2025 tools made experienced devs 19% *slower* while they felt faster). Cairn exists to claw that back; it has no trial proving it does.

## License

MIT. Composes with and adapts ideas from mattpocock/skills (MIT) — see `LICENSE`.
