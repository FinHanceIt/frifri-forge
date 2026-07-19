# Topology Catalog

Seven shapes cover virtually every agent team. Pick the simplest that fits; combine only
when the BRIEF demands it.

## 1. Pipeline (sequential relay)

```
A → B → C → D
```

- **Use when:** output of each craft is the input of the next; order is inherent
  (research → write → edit).
- **Strengths:** simple contracts, easy debugging (binary-search the stage that broke).
- **Failure modes:** error compounding downstream; latency = sum of stages.
- **Sizing:** 3–5 stages. Beyond that, group stages under sub-pipelines.
- **Contract rule:** each stage validates its input against the handoff contract and
  rejects upstream garbage instead of "fixing" it silently.

## 2. Orchestrator–workers (hub and spoke)

```
        ┌→ W1
ORCH ───┼→ W2
        └→ W3
```

- **Use when:** tasks are dynamic/heterogeneous; a router brain decides who works.
- **Strengths:** flexible, workers stay simple and stateless.
- **Failure modes:** orchestrator bottleneck; orchestrator context bloat (it sees
  everything). Mitigate: workers return summaries, not transcripts.
- **Sizing:** 1 orchestrator : 3–7 workers.

## 3. Hierarchical (managers of managers)

```
EXEC → LEAD-A → {a1, a2}
     → LEAD-B → {b1, b2}
```

- **Use when:** two genuinely different abstraction levels exist (program vs workstream).
- **Failure modes:** telephone-game distortion between layers; cost multiplication.
- **Rule:** never add a layer that only forwards messages. Each layer must add a
  decision only it can make. Most teams do NOT need this.

## 4. Blackboard / shared artifact (the bible pattern)

```
A, B, C, D ⇄ ONE SHARED DOCUMENT (sectioned, single-writer-per-section)
```

- **Use when:** the deliverable IS a document/spec assembled from specialist sections
  (PromptForge and CineForge both use this).
- **Strengths:** total transparency; any agent can read all context; trivially auditable.
- **Failure modes:** write conflicts (solve: one writer per section, enforced);
  document bloat (solve: section size budgets).

## 5. Parallel fan-out / map-reduce

```
SPLIT → {A1, A2, ... An} → MERGE
```

- **Use when:** same operation over many independent items (50 pages to review,
  20 prompts to test).
- **Failure modes:** merge-stage quality (the reducer needs a real rubric, not "combine
  these"); inconsistent style across workers (solve: shared style anchor in every
  worker's prompt).

## 6. Critic pair / debate (maker–checker)

```
MAKER → CRITIC → (fix loop ≤ N) → OUT
```

- **Use when:** correctness or safety matters more than latency; outputs are checkable.
- **Rules:** critic gets the rubric, NOT the maker's reasoning (independence); hard cap
  on loops (2–3) with escalation to human on non-convergence; critic verdicts are
  structured (PASS/FIX + routed findings), never essays.

## 7. Router / dispatcher

```
IN → ROUTER → exactly one of {A, B, C}
```

- **Use when:** inputs fall into discrete categories needing different specialists
  (support triage: billing vs tech vs refund).
- **Failure modes:** ambiguous categories (solve: explicit tie-break rules + a default
  route); router doing the work itself (solve: router outputs ONLY a route + confidence).

## Combination guidance

Real systems compose: PromptForge = pipeline spine + blackboard artifact + parallel
fan-out mid-section + critic gate before ship. Name each pattern you borrow and which
failure mode you inherit from it — the risk register should trace back to these.
