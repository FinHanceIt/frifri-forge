# LLMForge

A virtual **AI/LLM engineering studio** for Claude (Cowork / Claude Code): 1 director
skill + 8 specialist agents that design, build, evaluate, and harden LLM-powered
systems — with quality and safety gates before every ship verdict.

## What it covers

| Agent | Craft |
|---|---|
| `llmforge` (skill) | Intake, mission routing (BUILD / FIX / DECIDE / AUDIT / FAST-PATH), gates, final Build Spec |
| `llm-architect` | System design: plain prompt vs RAG vs agentic vs fine-tune, blueprints, ADRs |
| `rag-engineer` | Chunking, embeddings, vector stores, hybrid search, retrieval evals |
| `agent-engineer` | Agent loops, tool/MCP schemas, memory, orchestration, framework choice |
| `model-strategist` | Sourced model comparisons, fine-tune vs prompt vs RAG, dataset specs, params |
| `integration-engineer` | Provider SDK code: streaming, structured outputs, retries, batching (Py/TS) |
| `eval-engineer` | **Quality gate** — golden sets, LLM-as-judge rubrics, regression harnesses |
| `safety-engineer` | **Risk gate** — injection surfaces, PII/GDPR, hallucination mitigations (defensive-only) |
| `llmops-engineer` | Cost math, caching, latency budgets, deploy + minimal observability |

## Use it

Say things like:

- "Build an LLM feature that answers questions from my product docs" → full BUILD
  pipeline ending in a Claude-Code-ready Build Spec.
- "My AI feature hallucinates prices" → FIX: eval-engineer reproduces, specialists
  repair, re-eval.
- "Which model should I use for X?" / "ce model folosesc?" → DECIDE memo with a sourced
  candidate table.
- "Audit my chatbot" → AUDIT findings report.

Interaction is bilingual (RO/EN); all internal artifacts are English.

## House rules baked in

- **Zero fabricated metrics** — every price/benchmark is searched + cited or labeled
  `ASSUMPTION`; evals report only numbers from actual runs.
- **Two gates** — nothing ships without eval PASS + safety PASS (except labeled
  fast-path answers).
- **Solo-operator economics** — managed-first, fewest moving parts, costs shown with
  math.
- **Fleet boundaries** — prompt craft → PromptForge; full apps → AppFactory; repo
  guardrails → GuardForge.

## Version

1.0.0 — built 2026-07-02 with PromptForge.
