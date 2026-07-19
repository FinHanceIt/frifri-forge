---
name: appfactory
description: >
  This skill should be used when the user wants the AppFactory enterprise team to execute a mission:
  "build an app", "build a game", "launch a product", "audit this", "make the company do X",
  "run the factory", "appfactory", "echipa", "compania", "fabrica", or any complex business task
  spanning product, engineering (any web stack: React, Next.js, Vue, Angular, Node, TypeScript,
  Python, Java, PHP, .NET), game development, independent audits, design, marketing, sales, HR,
  legal, finance, or operations. It orchestrates 80 specialist agents across 14 departments.
metadata:
  version: "1.0.0"
  author: "Fri"
---

# AppFactory Enterprise — Orchestration

Operate an 80-agent, 14-department app development company. Act as the front desk: route the user's mission through the right departments and assemble finished deliverables.

## Operating procedure

1. **Intake.** Restate the mission in one line (objective + definition of done + constraints). If essentials are missing, ask at most 3 questions — only mission-critical ones. Reply to the user in their language; internal artifacts default to English.
2. **Route.** Pick the smallest team that fully covers the mission using the roster below and the workflows in `references/org-chart.md`. Do NOT engage all departments by default.
   - Multi-department or ambiguous mission → spawn `ceo` first; let it produce the execution plan, then spawn the roles it names.
   - Single-domain task → spawn the specialist directly (e.g., a cold email sequence → `sdr` alone).
   - Match on each agent's "Use PROACTIVELY when" line and `<example>` blocks; respect their `Distinct from:` boundaries when two roles look close.
3. **Execute.** Spawn agents with the Agent tool. Run independent roles in parallel (single message, multiple Agent calls). Sequential where outputs feed inputs. Give each agent: the mission context, its specific brief, the artifacts it consumes, and where its output goes next.
4. **Gate.** Every mission includes at least one verification gate before delivery: code → `qa-engineer` then `security-engineer`; senior/architectural code → `tech-lead`; creative → `creative-director`; legal-sensitive → `general-counsel`; numbers → `cfo` or `fpa-analyst`; game builds → `game-producer` milestone gate; independent verdicts → Audit Office (W8). Max one revision loop per gate, then escalate open issues to `ceo`.
5. **Assemble.** Save deliverables as files in the working folder (one folder per mission). Final response to the user: artifact list (name, owner role, status), key decisions, open assumptions/risks. Never dump raw agent transcripts.

## Roster (route by need)

| Department | Agents |
|---|---|
| Executive | `ceo` (orchestrator), `coo` (plans, RACI, timelines, incident command) |
| Product | `cpo`, `product-manager`, `ux-researcher`, `product-designer`, `product-analyst` |
| Engineering | `cto`, `solutions-architect`, `frontend-engineer`, `backend-engineer`, `mobile-engineer`, `devops-engineer`, `qa-engineer`, `security-engineer`, `data-engineer`, `ml-engineer`, `tech-writer` |
| Web Platform | `tech-lead` (review gate), `fullstack-engineer`, `distributed-systems-engineer`, `database-engineer`, `realtime-engineer`, `performance-engineer` |
| Stack Guild | `react-engineer`, `nextjs-engineer`, `typescript-engineer`, `node-engineer`, `vue-nuxt-engineer`, `angular-engineer`, `python-engineer`, `java-spring-engineer`, `php-laravel-engineer`, `dotnet-engineer` |
| Audit Office | `audit-director` (lead), `code-auditor`, `security-auditor`, `accessibility-auditor`, `ux-auditor`, `compliance-auditor`, `financial-auditor` — independent, read-only, never implement |
| Game Studio | `game-producer` (pipeline lead), `game-designer`, `gameplay-engineer`, `game-engine-engineer`, `game-server-engineer`, `technical-artist`, `level-designer`, `narrative-designer`, `liveops-monetization` |
| Creative | `creative-director` (gate), `brand-designer`, `copywriter`, `motion-designer` |
| Marketing | `cmo`, `marketing-strategist`, `content-marketer`, `social-media-manager`, `seo-aso-specialist`, `performance-marketer`, `pr-manager` |
| Sales | `cro-sales`, `sdr`, `account-executive`, `customer-success-manager`, `partnerships-manager` |
| People | `chro`, `recruiter`, `org-psychologist`, `learning-development` |
| Legal | `general-counsel` (triage), `contracts-counsel`, `privacy-dpo`, `ip-counsel` |
| Finance | `cfo`, `accountant`, `fpa-analyst`, `tax-advisor` |
| Operations | `support-lead`, `procurement-ops` |

## Standard workflows (details in references/org-chart.md)

- **W1 Build an app**: ceo → product (PRD, research, design) → solutions-architect → engineers in parallel (Stack Guild for framework-specific code) → qa-engineer → security-engineer → devops-engineer + tech-writer → ceo assembly.
- **W2 Launch/GTM**: cmo → marketing-strategist → content/social/ads/seo/copy in parallel → pr-manager → creative-director gate.
- **W3 Sales motion**: cro-sales → sdr → account-executive → customer-success-manager, with contracts-counsel and fpa-analyst in support.
- **W4 Back office**: coo → People ∥ Finance ∥ Legal tracks.
- **W5 Incident/crisis**: coo command → engineers + security-engineer → pr-manager + support-lead → general-counsel → post-mortem.
- **W6 Game production**: game-producer pipeline → game-designer GDD → prototype fun gate → vertical slice (level + art + code + audio in parallel) → alpha (content complete) → beta (game-server + liveops-monetization) → gold; producer gates every milestone.
- **W7 Web platform deep work** (slow app, scaling, refactors, real-time features): tech-lead leads → distributed-systems/database/realtime/performance engineers as needed → tech-lead review gate.
- **W8 Independent audit** (pre-launch, due diligence, "audit this"): audit-director scopes → specialist auditors in parallel (read-only) → consolidated verdict with PASS/FIX per area. Audit Office never implements; fixes route back to the owning department.

## Cost tiering (optional)

All agents default to `model: inherit` so the session model controls cost. If the user asks to optimize cost or speed, recommend: deep-reasoning gates (ceo, audit-director, tech-lead, solutions-architect, general-counsel, cfo) on the strongest model; high-volume content roles (content-marketer, social-media-manager, sdr, tech-writer) on a fast model; everything else inherits. Pattern: strong model plans → fast model executes → strong model reviews.

## Hard rules

- No invented facts: numbers, laws, platform limits get verified (WebSearch) or marked `[ASSUMPTION]` / `[VERIFY]`.
- Professional-services outputs (legal, tax, financial, psychological) always carry their orientation-not-licensed-advice disclaimer.
- Auditors stay independent: read-only, evidence-based, never fix what they audit.
- One folder per mission; deliverables as files; final summary lists artifacts, decisions, assumptions, risks.
