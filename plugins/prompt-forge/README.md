# PromptForge

**A virtual prompt-engineering studio.** A crew of 12 specialist agents that takes a one-line idea ("I want a team of agents that does X") and ships a production-grade, red-teamed, fully documented agent team — for any AI model and any framework.

PromptForge is the meta-team: the team that builds other teams.

**v2.0.0 — the Fable rebuild.** Re-engineered with Claude Fable 5: current model
knowledge (Claude 5 family + tier ladder), modern attack classes (indirect injection,
memory poisoning, crescendo), compaction-era context engineering, and agentic loop
patterns (stop conditions, tool budgets).

## How it works

Everything flows through one shared document, the **Team Bible**. Each specialist owns one section. The Director runs the pipeline, holds approval gates, and ships the result in your target format.

```
BRIEF → ARCHITECTURE → ROSTER → ┬ TOOLING   ┬ → PROMPTS → MODELFIT → EVAL ⇄ DEBUG → SHIP
                                ├ CONTEXT   ┤
                                └ WORKFLOW  ┘
        Gate A ▲                              Gate B ▲              Gate C ▲
```

## The crew

| # | Skill | Owns | What it does |
|---|-------|------|--------------|
| 1 | `promptforge-director` | the whole pipeline | Orchestrates the crew, holds gates, ships |
| 2 | `intake-strategist` | BRIEF | Closes the information gap; turns vague asks into a contract |
| 3 | `team-architect` | ARCHITECTURE | Picks topology; decides how many agents (fewest that ship) |
| 4 | `role-designer` | ROSTER | Writes role cards: mandate, boundaries, success criteria |
| 5 | `tool-integration-designer` | TOOLING | Tool schemas, MCP design, error contracts |
| 6 | `context-curator` | CONTEXT | Context budgets, few-shot anchors, memory design |
| 7 | `workflow-choreographer` | WORKFLOW | Handoff contracts, gates, escalation — the seams |
| 8 | `system-prompt-engineer` | PROMPTS | Writes every system prompt; the master craftsman |
| 9 | `model-optimizer` | MODELFIT | Model/params per role, cost budget, cross-model porting |
| 10 | `red-team-evaluator` | EVAL | Attacks the prompts; scorecard; PASS/FIX verdict |
| 11 | `prompt-debugger` | DEBUG | Symptom→cause→single-variable fix; regression via golden set |
| 12 | `ship-packager` | SHIP | Packages as plugin/GPT/LangGraph/CrewAI/n8n + docs + changelog |

## Modes

- **team** — full pipeline; build a new agent team from scratch
- **solo** — one perfect prompt or single agent (compressed spine)
- **audit** — review/score an existing prompt or team, then fix it
- **port** — convert an existing team to another model or framework

## Usage

Say things like:

- "Build me an agent team that does [X]"
- "Write a system prompt for [Y]"
- "Audit this prompt" / "Why does my agent keep doing [Z]?"
- "Port my CrewAI team to Claude skills"

The Director triggers on any of these and offers the full pipeline. Every specialist also works standalone.

## Output

Each engagement produces:

1. **The Team Bible** (`bible.md`) — the complete project record
2. **The deliverable** — ready-to-install prompts/skills/plugin/code in your target format
3. **A golden test set** — so future edits never silently regress

## Changelog

- **2.0.0** (2026-06-13) — Fable-era rebuild. `model-optimizer`: dated model-landscape
  reference (Fable 5 / Opus 4.8 / Sonnet 4.6 / Haiku 4.5, tier ladder, cost levers,
  1M-context architecture feedback). `red-team-evaluator`: 4 new attack classes —
  indirect injection via tool results, crescendo, memory poisoning, privilege probe.
  `context-curator`: compaction protocol, JIT retrieval, tool-result pruning, sub-agent
  isolation. `prompt-patterns`: agentic loop rules, instruction budget, long-context
  placement. `ship-packager`: subagent packaging (`agents/` + pinned `model:`). Surgical
  upgrades to architect, intake, roles, tooling, workflow, debugger. Director, pipeline,
  and topologies unchanged — they were already right.
- **1.0.0** — initial 12-skill release.

## Setup

No environment variables, no MCP servers required. Install the `.plugin` file and go.
