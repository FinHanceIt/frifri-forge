# IdeaForge

**The think-tank that forges any idea into a tested verdict.** An 11-agent thinking team for Fri — it takes any idea, problem, or need and runs a structured session that generates, grounds, challenges, foresees, and converges on an honest recommendation with a next action.

IdeaForge is a *thinking* team, not a building team. It decides **whether** and **what**; [AppFactory](../appfactory-enterprise) builds **how**. It's fully standalone — most ideas it chews on will never be software — but a buildable software idea can exit as an AppFactory-ready brief.

## The crew (1 Facilitator + 10 thinkers)

| Agent | Lens | Owns |
|---|---|---|
| The Facilitator | frames, routes, synthesizes, fights groupthink | the session + verdict |
| The Philosopher | first principles & reframing | FRAME |
| The Explorer | divergent generation | POOL |
| The Synthesist | combine & connect | COMBINATIONS |
| The Investigator | evidence & landscape (searches + cites) | EVIDENCE |
| The Advocate | real human demand | DEMAND |
| The Realist | feasibility & systems | FEASIBILITY |
| The Skeptic | devil's advocate & premortem | CRITIQUE |
| The Steward | ethics, stakeholders & risk | STAKES |
| The Futurist | foresight & scenarios | HORIZON |
| The Strategist | scoring & recommendation | VERDICT |

## Five session modes

The Facilitator picks one automatically, or you can force it:

- **Spark** — fast divergence, "give me ideas."
- **Crucible** — pressure-test one idea (premortem + ethics + feasibility).
- **Horizon** — foresight / scenarios.
- **Verdict** — decide between options you already have.
- **Roundtable** — the full arc, for a fresh open idea (default).

## How to use

Just describe the idea or the decision. Examples:

- "Fă-mi un brainstorm pe ideea asta de newsletter."
- "Is this product idea any good? Pressure-test it."
- "Help me decide: launch now or build an audience first?"
- "Where is this market going in 3–5 years?"

The session runs through two light human gates — **framing** (is this the real question?) and **verdict** (approve the recommendation) — and ends with a single clear next action.

## What keeps it honest

- **No fabricated facts.** Only the Investigator asserts external facts, and only with sources. Every other thinker labels speculation as speculation and tags confidence (high/med/low).
- **Steelman before critique;** minority views are kept in a dissent log.
- **"Don't do this" is a valid verdict.**
- **Safety:** harmful, illegal, or exploitative ideas are flagged by the Steward and stopped — not brainstormed.

## Install

Add the marketplace, then install `ideaforge`. Bilingual RO/EN — reasons in English, delivers in your language.

## Structure
```
ideaforge/
  .claude-plugin/plugin.json
  skills/ideaforge/SKILL.md            # the Facilitator's playbook
  skills/ideaforge/references/         # house-style, handoff-contracts, thinking-methods
  agents/                              # the 11 thinker prompts
```
