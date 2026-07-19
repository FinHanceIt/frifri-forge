# SearchForge — Team Bible

The project record: what was decided and why. Source of truth for future edits.

## META
- **Mode:** team (build a new agent team)
- **Name:** SearchForge
- **Owner:** Fri (Romanian solo creator — own brands + clients in RO/EU/US)
- **Built:** 2026-06-17 · **Version:** 1.0.0
- **One-liner:** an 18-part team (orchestrator + 17 specialists) that audits, creates, optimizes, and reports across SEO, SEM, and GEO/AEO — chat-first on GSC + free tools, bilingual RO/EN, white-hat, no fabricated metrics.
- **How we know it works:** the golden test set (`golden-tests.md`) — routing, data-honesty refusals, white-hat refusals, GEO scoping, international nuance, and the QA gate all pass.

## BRIEF (locked at intake)
- **Audience:** both Fri's own brands and client work → client-facing reporting + onboarding are first-class.
- **Markets:** Romania (RO), EU/English, US/Global → international SEO (hreflang, locale terms, RO↔EN transcreation) is core, not an add-on.
- **Pillars (all eight):** technical, on-page/content, off-page, local, e-commerce, SEM, GEO/AI search, analytics.
- **Tooling reality:** Google Search Console + free tools, chat-first. No paid Ahrefs/Semrush seat assumed → **data-honesty rule** (no fabricated metrics) is the spine.
- **Package:** Claude Code plugin in Fri's house style (orchestrator skill + specialist agents + references + golden tests).
- **Internal prompt language:** English. **Deliverables:** RO + EN.
- **Roster size:** broadest option — off-page split into link-building + digital PR; added structured-data, international SEO, video/YouTube, CRO, and a content editor.

## ARCHITECTURE
- **Topology:** hub-and-spoke. The `searchforge` Director classifies each mission and dispatches specialists along a five-stage value chain (Discover → Build → Content → Amplify → Convert/Measure), ending at a single Gate.
- **Two motions:** **parallel fan-out** for audits (specialists audit concurrently → `audit-qa-director` consolidates into one roadmap); **sequential pipeline** for content (strategy → brief → write → edit → GEO polish → QA).
- **Why this shape:** mirrors Fri's proven patterns (AppFactory's audit fan-out, OfertaForge's routing). Each pillar has exactly one owner; no two agents overlap (enforced by each agent's "Distinct from" boundary).

## ROSTER (17 specialists + Director)
Discover: search-strategist, international-seo-strategist · Build: technical-seo-engineer, structured-data-specialist, ecommerce-seo-specialist, local-seo-specialist · Content: content-architect, seo-copywriter, content-editor · Amplify: link-building-strategist, digital-pr-strategist, video-seo-specialist, sem-strategist, geo-aeo-strategist · Convert/Measure: cro-specialist, analytics-reporter · Gate: audit-qa-director.
Full role cards: `agents/*.md`. Each follows the same contract: objective · done_when · instructions · knowledge · workflow_position · output_contract · guardrails.

## TOOLING & CONTEXT
- Agents use `Read/Write/Edit/WebSearch/WebFetch` (+ `Bash` for the few that compute on pasted numbers: technical, sem, analytics).
- Shared brain = `references/` (8 files). The data-honesty rule + free-tool stack are the load-bearing context every agent inherits.
- No live SEO-suite APIs — by design. The team runs on what Fri can paste/pull from free tools, and says so.

## WORKFLOW & GATES
- **Gate 1 — Scope & targets** (before deep work)
- **Gate 2 — Strategy & priorities** (before execution)
- **Gate 3 — Pre-publish QA** by `audit-qa-director` (before anything ships)
- Fri publishes / changes the site / launches ads / contacts clients. Agents never act on the outside world.
- Handoffs are contract-based (`references/handoff-contracts.md`); the Director keeps the running SEO Brief.

## MODELFIT
- All agents are `model: inherit` (portable). Recommended when assigning: strongest model for `audit-qa-director`, `search-strategist`, `geo-aeo-strategist`, `seo-copywriter`, and the Director; mid-tier is fine for catalog/checklist-driven roles. Temperature low for audits/analytics (precision), a touch higher for copywriting (voice).

## EVAL
- See `golden-tests.md`. Coverage: mission routing, data-honesty (refuse to invent a volume), white-hat (refuse PBN/fake reviews), GEO honesty (llms.txt scoped as non-adopted), international (RO ≠ translated EN), cannibalization, SEM (AI Max awareness), the QA gate (fabricated metric = FAIL), and gate-holding (stops for scope).

## SHIP
- Delivered as the `SearchForge/` plugin folder in `Prompt forger/`. Install via a marketplace Fri controls or by enabling the folder as a plugin.
- Known cosmetic note: subagent-written agent files carry a trailing orphan `</output>` tag (matching Fri's existing AppFactory files) — harmless prompt-body text; sweep on next edit pass if desired.

## OPEN QUESTIONS / FUTURE
- Optional: a thin `marketplace.json` if Fri wants one-click install.
- Optional later split if needed: a dedicated migrations specialist, or a YouTube-vs-TikTok short-form split.
- Re-verify `[VERIFY]`-tagged 2026 stats quarterly (AI-Overview coverage, rich-result eligibility, Ads migration dates).
