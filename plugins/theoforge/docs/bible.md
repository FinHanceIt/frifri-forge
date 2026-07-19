# Team Bible — TheoForge (Conciliul Etern)
mode: team · client: Fri · date: 2026-07-07 · deliverable: theoforge.plugin v1.0.0

## BRIEF
A chambered mega-council simulating masters, priests, monks, priestesses, mystics, ascended masters and archetypal deities from the world's religions and spiritual forms — living and dead — for multidisciplinary mystic-esoteric discussion; every voice answers from inside its own tradition.
User decisions (Gate 0): (1) ALL religions incl. dead ones + invoker + living council; (2) mythic deities speak as archetypes, monotheisms through mystics, founders never impersonated; (3) full plenary on every question.
Success: plenary = every chamber heard, distinct dictions, honest coverage (134 seats / 279-door catalog / invoker), zero fabrication (quote discipline, attestation grades A/B/C/X, closed knowledge respected), RO/EN mirroring.
Non-goals: proselytism, "true religion" verdicts, real-world authority (medical/legal/divination-as-fact), mockery.

## ARCHITECTURE (Gate A: shape approved via user's three answers; snapshot messaged 2026-07-07)
Hub-and-chambers. One orchestrator skill (Hierophant) simulates the council in-conversation; 27 agent files define chambers/functional roles.
Living Wing 17 chambers (89 seats) · Necropola 6 chambers (36 seats) · Pantheon 9 archetypal deities · Functional 3 (Invoker, Synthesist, Truth Warden) · Registry: tradition-catalog.md (279 entries) + golden-tests.md.
Plenary protocol: opening → living chambers (all; 2–4 relevant get extended turns) → necropolis (grades visible) → pantheon (2–4) → synthesis (anti-flattening) → warden seal. Commands: adâncește/deepen, duel, invocă/invoke, chamber-only, single voice, sinteză, conciliu restrâns.

## ROSTER
See agents/*.md — every seat card: name (fictional composite; titles for the dead), lens, voice, guard. Functional mandates in the-invoker.md / the-synthesist.md / the-truth-warden.md. Integrity spine = the Seven Seals (truth-warden).

## TOOLING / CONTEXT / WORKFLOW
No runtime tools required (conversational simulation); WebSearch optional for Invoker fact-checks. Context diet: SKILL.md + needed chamber files + catalog on demand. Single human (Fri); correction-by-command; Warden may interrupt any voice.

## PROMPTS
SKILL.md + 27 agent bodies written (English internals, runtime mirrors user language; RO diacritics via romanian-grammar when RO).

## MODELFIT (Gate B)
Runs on the session's Claude model; no per-agent model split (in-context voices — routing would add cost, no benefit). Plenaries are long by design (~2–4k words); compact-plenary + zoom modes keep daily use cheap. Approved by default.

## EVAL (Gate C)
Golden set: skills/theoforge/references/golden-tests.md (12 behavioral + structural QC). Programmatic QC (descriptions ≤500, JSON valid, frontmatter complete, seat math, catalog count): see docs/qc_report.txt. Verdict recorded there.

## SHIP
theoforge.plugin (zip of plugin root) + source tree at Prompt forger/TheoForge. v1.0.0, 2026-07-07.
