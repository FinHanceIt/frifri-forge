# PromptForge Pipeline — routing, gates, loop-backs

## Spines per mode

### mode: team (full build)

```
BRIEF → ARCHITECTURE →[GATE A]→ ROSTER → ┬ TOOLING  ┬ → PROMPTS → MODELFIT →[GATE B]→ EVAL →[GATE C]→ SHIP
                                         ├ CONTEXT  ┤                          ▲           │
                                         └ WORKFLOW ┘                          └─ DEBUG ◄──┘ (on FIX)
```

TOOLING, CONTEXT, WORKFLOW are independent after ROSTER — run them in parallel
(subagents) when possible. PROMPTS must wait for all three: a system prompt that doesn't
embed exact tool schemas and handoff contracts is fiction.

### mode: solo (one prompt / one agent)

```
BRIEF → ROSTER(1 card) → TOOLING(if tools) → PROMPTS → MODELFIT → EVAL →[GATE C]→ SHIP
```

Skip ARCHITECTURE and WORKFLOW. CONTEXT folds into PROMPTS (the engineer pulls few-shot
anchors directly). Gates A/B collapse into one confirmation before EVAL.

### mode: audit (existing prompt/team)

```
BRIEF(what exists + what hurts) → EVAL(attack first) → DEBUG(fix list) → re-EVAL → SHIP(patch + report)
```

Never rewrite before attacking: the scorecard decides whether this is a patch job
(DEBUG) or a teardown (escalate to mode: team with the findings as input).

### mode: port (model/framework conversion)

```
BRIEF(source + target) → MODELFIT(porting plan) → PROMPTS(rewrite per target) → EVAL(golden set parity) → SHIP
```

Parity rule: the ported team must pass the SAME golden set as the original. If the
original has no golden set, build one from the original's behavior first.

## Gates

| Gate | After | The user approves | If rejected |
|------|-------|-------------------|-------------|
| A | ARCHITECTURE | topology, agent count, scope, what's out of scope | team-architect revises; max 2 cycles, then escalate trade-offs explicitly |
| B | MODELFIT | model assignments, cost/latency estimate | model-optimizer re-plans within stated budget |
| C | EVAL | nothing — verdict must be PASS | FIX list routes to prompt-debugger (prompt-level) or back to the owning specialist (design-level); then re-EVAL |

Gate C routing rule: a finding is **prompt-level** if fixable by editing a prompt without
changing any contract (→ debugger). It is **design-level** if a contract, tool, role, or
topology must change (→ owning specialist, and re-run every downstream section that
depended on it).

## Loop-backs

- EVAL finds role overlap → role-designer (ROSTER), then PROMPTS regenerates affected
  agents only.
- EVAL finds handoff break → workflow-choreographer, then PROMPTS re-embeds contracts.
- DEBUG fix fails golden set twice → stop patching; return to the owning specialist —
  the design is wrong, not the wording.
- User changes the brief mid-flight → intake-strategist amends BRIEF with a changelog
  line; Director re-validates ARCHITECTURE before anything else proceeds.

## Parallelism notes

- Safe to parallelize: TOOLING / CONTEXT / WORKFLOW (post-ROSTER); per-agent prompt
  writing within PROMPTS; per-agent attacks within EVAL.
- Never parallelize: anything across a gate; DEBUG fixes touching the same prompt.
