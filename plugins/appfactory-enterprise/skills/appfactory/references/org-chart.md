# AppFactory Enterprise — Organization Blueprint (v1.0)

Mission: operate as a full-scale app development company. Any mission enters through the CEO (or goes straight to a single specialist), flows through the right departments, and exits as a finished, verified deliverable.

## Org chart (80 agents, 14 departments)

| # | Agent | Department | Purpose |
|---|-------|-----------|---------|
| 1 | `ceo` | Executive | Chief orchestrator. Decomposes any mission, routes to departments, assembles the final deliverable. |
| 2 | `coo` | Executive | Operations. Project plans, timelines, RACI, cross-department coordination, status reports, incident command. |
| 3 | `cpo` | Product | Product vision, portfolio decisions, build/kill/pivot calls, scope arbitration. |
| 4 | `product-manager` | Product | PRDs, user stories with Given/When/Then acceptance criteria, prioritization (RICE/MoSCoW). |
| 5 | `ux-researcher` | Product | Personas, JTBD, interview/survey design, usability findings. |
| 6 | `product-designer` | Product | UX flows, wireframes, UI specs, design tokens, all-states screens, a11y AA. |
| 7 | `product-analyst` | Product | KPI trees, funnels, A/B test design (95% significance, MDE), tracking plans. |
| 8 | `cto` | Engineering | Tech strategy, stack decisions, build-vs-buy, tech radar, risk calls. |
| 9 | `solutions-architect` | Engineering | System design, C4/Mermaid diagrams, ADRs, API contracts, resilience trio (circuit breakers, retries+jitter, timeouts). |
| 10 | `frontend-engineer` | Engineering | Cross-framework web UI delivery, accessibility, Core Web Vitals budgets. |
| 11 | `backend-engineer` | Engineering | APIs, services, business logic, integrations; production-readiness checklist; defers schema to database-engineer. |
| 12 | `mobile-engineer` | Engineering | iOS/Android (Swift/Kotlin/React Native/Flutter), offline-first, store-readiness, crash-free >99.9%. |
| 13 | `devops-engineer` | Engineering | CI/CD, IaC, environments, releases, observability, DORA four keys. |
| 14 | `qa-engineer` | Engineering | Test plans, formal test design, automation, go/no-go gate during builds. |
| 15 | `security-engineer` | Engineering | STRIDE threat models, secure code review and fixes, OWASP, scanner stack, incident response plans. |
| 16 | `data-engineer` | Engineering | ELT pipelines, warehouse modeling, data contracts, quality SLOs. |
| 17 | `ml-engineer` | Engineering | LLM/RAG features, eval harnesses, deployment ladder (shadow→canary), drift monitoring. |
| 18 | `tech-writer` | Engineering | Developer docs, API references, quickstart-first guides, changelogs, runbooks. |
| 19 | `tech-lead` | Web Platform | Staff-level review GATE, cross-architecture standards, refactor strategy, dispute arbitration. |
| 20 | `fullstack-engineer` | Web Platform | End-to-end features on any web architecture; architecture pattern selection (SPA/SSR/islands/edge). |
| 21 | `distributed-systems-engineer` | Web Platform | Microservices, event-driven, sagas, outbox, idempotency, consistency trade-offs, scale. |
| 22 | `database-engineer` | Web Platform | Engine selection, schema at scale, index strategy, query tuning SLOs, replication/sharding, zero-downtime migrations. |
| 23 | `realtime-engineer` | Web Platform | SSE/WebSocket/WebRTC decisions, live collaboration, presence, CRDT/OT, connection scale. |
| 24 | `performance-engineer` | Web Platform | Profile-first optimization, load test taxonomy, CWV + latency budgets as CI gates, capacity. |
| 25 | `react-engineer` | Stack Guild | React 19 + Compiler-era idioms: waterfalls→bundle→re-renders, state taxonomy, concurrent features. |
| 26 | `nextjs-engineer` | Stack Guild | Next.js App Router: rendering strategy per route, explicit caching (use cache/cacheTag/PPR), server actions. |
| 27 | `typescript-engineer` | Stack Guild | Advanced types, runtime-validated boundaries (zod), branded types, tsconfig, monorepos, JS→TS. |
| 28 | `node-engineer` | Stack Guild | Node 24 LTS backends: event-loop discipline, streams+backpressure, workers, graceful shutdown. |
| 29 | `vue-nuxt-engineer` | Stack Guild | Vue 3 Composition API, Pinia, Vapor-mode awareness, Nuxt rendering modes, Nitro routes. |
| 30 | `angular-engineer` | Stack Guild | Angular 22: signals-first (Signal Forms, Resource API), OnPush/zoneless, standalone, RxJS discipline, migrations. |
| 31 | `python-engineer` | Stack Guild | FastAPI/Django services, async discipline, uv+ruff toolchain, typed Python. |
| 32 | `java-spring-engineer` | Stack Guild | Spring Boot 4 / Java 25 LTS, virtual threads, JPA discipline, Testcontainers, enterprise integration. |
| 33 | `php-laravel-engineer` | Stack Guild | Laravel 13, Eloquent N+1 vigilance, queues, Livewire/Inertia, legacy PHP modernization. |
| 34 | `dotnet-engineer` | Stack Guild | .NET 10 LTS, ASP.NET Core minimal APIs, EF Core discipline, Blazor, Azure-leaning backends. |
| 35 | `audit-director` | Audit Office | Audit orchestrator: scopes, dispatches specialist auditors in parallel, consolidates into one verdict. |
| 36 | `code-auditor` | Audit Office | Independent code quality audit: dimensions scored 1–10, hotspots (churn×complexity), dependency health. |
| 37 | `security-auditor` | Audit Office | Independent security audit: ASVS-style, severity = likelihood×impact, coverage map, no fixes. |
| 38 | `accessibility-auditor` | Audit Office | WCAG 2.2 AA conformance, screen-reader flows, keyboard pass, contrast, prioritized remediation. |
| 39 | `ux-auditor` | Audit Office | Nielsen heuristics scored, task-flow friction, copy clarity, conversion blockers. |
| 40 | `compliance-auditor` | Audit Office | Policy-vs-practice gaps, GDPR essentials, OSS license scan, SOC2-readiness. |
| 41 | `financial-auditor` | Audit Office | Books reconciliation, controls assessment, model assumption audit, due-diligence readiness. |
| 42 | `game-producer` | Game Studio | Milestone pipeline (prototype→fun gate→vertical slice→alpha→beta→gold) with entry/exit criteria; scope by fun-per-cost. |
| 43 | `game-designer` | Game Studio | Core loop, GDD, systems and balancing math, economy sources/sinks, playtest protocol. |
| 44 | `gameplay-engineer` | Game Studio | Gameplay code on Unity/Unreal/Godot/web: controllers, combat, AI, game feel (coyote time, buffering). |
| 45 | `game-engine-engineer` | Game Studio | Frame budgets (16.6ms), rendering, shaders, batching/LOD/occlusion, memory per platform tier, porting. |
| 46 | `game-server-engineer` | Game Studio | Server-authority netcode, prediction/reconciliation, rollback, matchmaking, anti-cheat layers. |
| 47 | `technical-artist` | Game Studio | DCC→engine pipelines with validation gates, asset budgets, shader/VFX cost specs, artist tooling. |
| 48 | `level-designer` | Game Studio | Layout grammar (intro→teach→test→twist→payoff), pacing maps, tutorial choreography, per-level metrics. |
| 49 | `narrative-designer` | Game Studio | Story structure, world bibles, dialogue-as-data (IDs, conditions, localization-ready), barks. |
| 50 | `liveops-monetization` | Game Studio | Monetization with mandatory ethics review, battle-pass math, events calendar, retention mechanics. |
| 51 | `creative-director` | Creative | Creative GATE: scored rubric (on-brief, on-brand, craft, originality, legal-safe); campaign concepts. |
| 52 | `brand-designer` | Creative | Identity systems: logo rules, color tokens with contrast checks, type scale, brand guidelines. |
| 53 | `copywriter` | Creative | Naming, taglines, UX microcopy states, landing pages, ad copy; AIDA/PAS/JTBD-language. |
| 54 | `motion-designer` | Creative | Storyboards, 30s promo structure (hook 0–3s), animation specs, platform aspect/caption specs. |
| 55 | `cmo` | Marketing | Budget by funnel stage, CAC ceilings per channel, brand-vs-performance split, quarterly plans. |
| 56 | `marketing-strategist` | Marketing | GTM: positioning → messaging house → channel plan → launch tiers; competitive analysis. |
| 57 | `content-marketer` | Marketing | E-E-A-T content, pillar→cluster calendars, repurposing matrix, case studies, newsletters. |
| 58 | `social-media-manager` | Marketing | Platform matrix (LinkedIn/X/IG/TikTok), hook-first posts, cadences, community SLAs. |
| 59 | `seo-aso-specialist` | Marketing | Technical SEO, keyword maps (intent×difficulty×volume), ASO, AI-search answer-shaped content. |
| 60 | `performance-marketer` | Marketing | Paid campaign structures per channel, creative testing cadence with kill rules, CAC/ROAS math, CRO. |
| 61 | `pr-manager` | Marketing | Inverted-pyramid releases, media tiers, embargoes, crisis comms (<1h holding statement). |
| 62 | `cro-sales` | Sales | Pricing/packaging (value metric, good-better-best), pipeline stages with exit criteria, weighted forecasts. |
| 63 | `sdr` | Sales | ICP + trigger events, 5–8 touch sequences, ≤90-word emails, personalization with sourcing. |
| 64 | `account-executive` | Sales | MEDDICC/SPICED discovery, problem-led demos, mutual action plans, trade-don't-cave negotiation. |
| 65 | `customer-success-manager` | Sales | Weighted health scores, time-to-first-value onboarding, QBRs, churn playbooks by signal. |
| 66 | `partnerships-manager` | Sales | Partner-fit scorecards, program economics (referral/reseller/tech), co-marketing plans. |
| 67 | `chro` | People | Org design (spans 5–8), comp philosophy (percentiles, bands), calibrated performance, values. |
| 68 | `recruiter` | People | Structured interviews with anchored scorecards, bias-free JDs, sourcing, offer frameworks. |
| 69 | `org-psychologist` | People | Psychological safety, SCARF, mediation protocol, WHO burnout dimensions; not therapy — escalates crises. |
| 70 | `learning-development` | People | 70-20-10 programs, skill matrices, 30/60/90 onboarding, workshop design. |
| 71 | `general-counsel` | Legal | Legal TRIAGE: risk matrix, regulatory maps, decide-vs-escalate, routes to specialists. |
| 72 | `contracts-counsel` | Legal | Clause-by-clause review tables, redlines, ToS/EULA essentials, MSAs/NDAs/SOWs/DPAs. |
| 73 | `privacy-dpo` | Legal | Data mapping, lawful bases, DPIAs, consent UX, 72h breach clock, DSR workflows. |
| 74 | `ip-counsel` | Legal | Trademark clearance ladder, OSS license compatibility, IP assignment hygiene, prior-art sanity. |
| 75 | `cfo` | Finance | Runway with scenario bands, raise timing, gross-margin floors, financial risk register. |
| 76 | `accountant` | Finance | SaaS chart of accounts, revenue recognition (deferral), month-end close, expense policies. |
| 77 | `fpa-analyst` | Finance | Unit economics (LTV:CAC >3, payback <12mo), driver-based models, scenarios, variance narratives, Rule of 40. |
| 78 | `tax-advisor` | Finance | Obligation maps, EU VAT OSS, US nexus, R&D credits, transfer pricing flags, tax calendar. |
| 79 | `support-lead` | Operations | Help center, macros, severity-based SLA matrix, deflection, CSAT/CES programs. |
| 80 | `procurement-ops` | Operations | Weighted vendor scorecards, SaaS stack audits, renewal discipline, cost optimization. |

## Workflows in detail

### W1 — Build an app
1. `ceo` decomposes mission → execution plan. 2. Product track: `product-manager` PRD ∥ `ux-researcher` personas/JTBD ∥ `product-designer` flows+wireframes (gate: `cpo` on scope). 3. `solutions-architect` system design + API contracts (consults `cto` on stack; `database-engineer` on schema). 4. Build in parallel: `frontend-engineer`/Stack Guild specialist per chosen framework, `backend-engineer`/stack specialist, `mobile-engineer` if mobile, `devops-engineer` pipeline from day one. 5. Gates in sequence: `qa-engineer` (functional) → `security-engineer` (defensive) → `tech-lead` if architectural risk. 6. `tech-writer` docs ∥ `devops-engineer` release. 7. `ceo` assembly: artifacts, decisions, risks.

### W2 — Launch / GTM
1. `cmo` sets budget + channel mix. 2. `marketing-strategist` GTM plan (positioning, messaging house, launch tiers). 3. Parallel: `content-marketer`, `social-media-manager`, `performance-marketer`, `seo-aso-specialist`, `copywriter` (+ `motion-designer` for video, `brand-designer` for identity refresh). 4. `pr-manager` press motion. 5. GATE: `creative-director` scored rubric on all creative. 6. `product-analyst` defines launch KPIs/tracking.

### W3 — Sales motion
1. `cro-sales` pricing/process. 2. `sdr` ICP + outbound. 3. `account-executive` discovery→close (support: `contracts-counsel` redlines, `fpa-analyst` deal economics). 4. `customer-success-manager` onboarding/renewals. 5. `partnerships-manager` for channel/BD plays.

### W4 — Back office
`coo` coordinates three parallel tracks: People (`chro` → `recruiter`/`org-psychologist`/`learning-development`) ∥ Finance (`cfo` → `accountant`/`fpa-analyst`/`tax-advisor`) ∥ Legal (`general-counsel` → specialists). Each track's lead gates its outputs.

### W5 — Incident / crisis
1. `coo` takes command (severity, comms cadence). 2. Technical: relevant engineers + `security-engineer` (+ `devops-engineer` rollback). 3. External: `pr-manager` holding statement <1h ∥ `support-lead` customer comms. 4. `general-counsel` exposure review. 5. Post-mortem: blameless, action items with owners (`coo`).

### W6 — Game production
1. `game-producer` pipeline + milestone gates. 2. `game-designer` core loop + GDD. 3. PROTOTYPE → fun gate (producer + designer; kill/iterate if not fun). 4. VERTICAL SLICE: `level-designer` + `gameplay-engineer` + `technical-artist` + `narrative-designer` in parallel; `game-engine-engineer` perf budgets. 5. ALPHA (content complete) → BETA: `game-server-engineer` netcode/scale + `liveops-monetization` (ethics review mandatory). 6. GOLD: producer ship-gate (budgets: 60 FPS, load <3s, crash <0.1%).

### W7 — Web platform deep work
For: slow apps, scaling walls, desync bugs, big refactors, real-time features. 1. `tech-lead` triages and leads. 2. Specialists as needed: `performance-engineer` (profile first), `database-engineer` (queries/schema), `distributed-systems-engineer` (consistency/queues), `realtime-engineer` (live features), `fullstack-engineer` (cross-cutting implementation). 3. GATE: `tech-lead` review + regression evidence.

### W8 — Independent audit
For: pre-launch, due diligence, "audit this". 1. `audit-director` scopes (areas, depth, evidence standards). 2. Specialist auditors run in PARALLEL, read-only: code/security/accessibility/ux/compliance/financial as scoped. 3. `audit-director` consolidates: cross-cutting themes, one verdict per area (PASS/FIX with findings ladder). 4. Fixes route to owning departments — never to the Audit Office.

## Operating rules

- **Smallest team wide enough.** Single-domain → one specialist. Cross-domain → `ceo` plan.
- **Boundaries:** respect each agent's `Distinct from:` lines (builder vs auditor, strategist vs executor, cross-stack vs framework specialist).
- **Gates:** max one revision loop per gate; unresolved → `ceo` decides as tie-breaker.
- **Evidence:** numbers, laws, platform limits verified or marked `[ASSUMPTION]`/`[VERIFY]`.
- **Files:** one folder per mission; agents write artifacts, orchestrator assembles.

## Cost tiering (when the user wants cost/speed optimization)

All agents ship `model: inherit`. Recommended pinning if asked: strongest model for deep-reasoning gates (`ceo`, `audit-director`, `tech-lead`, `solutions-architect`, `general-counsel`, `cfo`, `security-auditor`); fast model for high-volume content (`content-marketer`, `social-media-manager`, `sdr`, `tech-writer`, `support-lead`); inherit for everything else. Pattern: strong plans → fast executes → strong reviews.

## Tool archetypes

Builders: Read, Write, Edit, Bash, Glob, Grep (+WebSearch where versions/platform facts are volatile). Auditors: Read, Grep, Glob, Bash + Write (report only) — never Edit. Strategists/advisors: Read, Write (+WebSearch/WebFetch for live facts: laws, prices, benchmarks). Orchestrators (`ceo`, `coo`, `cpo`, `product-manager`, `creative-director`, `game-producer`): all tools.
