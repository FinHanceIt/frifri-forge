# TEAM BIBLE — {project-name}

> Single source of truth for this engagement. Every specialist reads the whole bible and
> writes ONLY its own section. The Director keeps it consistent.

## META

- **Project:**
- **Mode:** team | solo | audit | port
- **Date / Version:** {date} / v0.1
- **Target platform(s):** (Claude skills/plugin, Claude Project, OpenAI Assistant/GPT,
  LangGraph, CrewAI, AutoGen, n8n/Make, raw prompt pack)
- **Status:** DRAFT | GATE-A-APPROVED | GATE-B-APPROVED | PASS | SHIPPED

---

## BRIEF — owner: intake-strategist

- **Job to be done (one sentence):**
- **Who operates the team / who consumes its output:**
- **Environment:** (where it runs, what it can touch, interface: chat / API / pipeline)
- **Success criteria (verifiable):**
  1.
- **Hard constraints:** (language, compliance, budget, latency, models allowed)
- **Out of scope (the team will NOT):**
- **Inputs available:** (data, docs, APIs, examples of good/bad output)
- **Risks / unknowns:**
- **Smart defaults taken:** (decision — one-line reasoning)

---

## ARCHITECTURE — owner: team-architect

- **Verdict: single agent or team? Why (2 sentences max):**
- **Topology:** pipeline | orchestrator-workers | hierarchical | blackboard | parallel
  fan-out | critic pair | router (+ justification)
- **Diagram:**

```
(ascii or mermaid)
```

- **Agent list (name + one-line mandate each):**
- **Data flow (what artifact moves between whom):**
- **Rejected alternatives (what + why rejected):**
- **Risk register (top 3 failure risks of this architecture):**

---

## ROSTER — owner: role-designer

One role card per agent:

### {agent-name}

- **Mandate (one sentence):**
- **Persona anchor:** (seniority + domain, e.g. "senior data engineer, ETL focus")
- **Owns:** (artifact/section this agent is sole writer of)
- **Inputs:** / **Outputs (contract):**
- **Tools needed:** (names only — schemas live in TOOLING)
- **Success criteria (verifiable):**
- **Failure modes → recovery:**
- **Boundaries:** NEVER / ALWAYS / DEFER-TO-HUMAN-WHEN
- **Escalation trigger:**

---

## TOOLING — owner: tool-integration-designer

- **Tool table:** | tool | owner agent(s) | when to use | side-effect class | constraints |
- **Schemas:** (JSON Schema or TypeScript per tool, with model-facing descriptions)
- **Error contract:** (what the agent sees on failure; retry/backoff/give-up rules)
- **Confirmation gates:** (which irreversible actions require human approval)
- **MCP/integration notes:** (transport, auth, env vars)

---

## CONTEXT — owner: context-curator

- **Per-agent context map:** | agent | static (in prompt) | per-task (injected) |
  retrieved (RAG) | accumulated (memory) | token budget |
- **Few-shot anchors:** (2–5 per agent where format/style is non-obvious; include one
  labeled near-miss with why it's wrong)
- **Memory design:** (what persists, schema, when written, when pruned)
- **Context-rot defenses:** (compaction protocol with survives/dies lists, tool-result
  pruning, fresh-context boundaries, anchor refresh)

---

## WORKFLOW — owner: workflow-choreographer

- **Flow diagram (runtime):**
- **Handoff contracts:** | edge (A→B) | artifact schema | acceptance criteria B validates |
  on-reject path |
- **Parallel vs gated:** (what runs concurrently; what blocks on what)
- **Human-in-the-loop gates:** (where, what the human approves, default on no-response)
- **Escalation matrix:** (stuck agent → orchestrator → human; triggers and timeouts)
- **State & idempotency:** (single-artifact vs message-passing; retry safety)

---

## PROMPTS — owner: system-prompt-engineer

One fenced, copy-ready system prompt per agent. Each must embed: identity, context,
objective, constraints, output format, tool-use rules (matching TOOLING exactly), handoff
contracts (matching WORKFLOW exactly), few-shot anchors (from CONTEXT), and a
self-verification block.

### {agent-name}

```
(full system prompt)
```

---

## MODELFIT — owner: model-optimizer

- **Assignment table:** | agent | model | fallback | temperature | top-p / reasoning
  effort | max tokens | rationale |
- **Cost estimate:** (tokens/run × runs/period → cost/period; worst case)
- **Porting notes:** (per target model family: what to change and why)
- **Compression report:** (what was cut from prompts with zero signal loss)

---

## EVAL — owner: red-team-evaluator

- **Scorecard (per agent + whole team):** clarity / specificity / completeness /
  efficiency / model-fit / robustness / format-precision / testability — 1–5 each
- **Attacks run & findings:** | attack class | input | expected | observed | severity |
- **Golden set:** (5–10 test cases with expected outputs — the regression suite)
- **Verdict:** PASS | FIX (routed list: finding → owner skill)

---

## DEBUG LOG — owner: prompt-debugger

| # | Symptom | Root cause (layer) | Single-variable fix | Golden-set result | Status |
|---|---------|--------------------|---------------------|-------------------|--------|

---

## SHIP — owner: ship-packager

- **Target format(s) & files produced:**
- **Install/run instructions:**
- **Docs delivered:** (README, quickstart, per-agent usage)
- **Version & changelog:**
- **Acceptance checklist:** (every BRIEF success criterion → where it's proven)
