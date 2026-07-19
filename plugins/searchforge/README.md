# SearchForge

**A full-spectrum search-visibility studio as an agent team** — SEO + SEM + GEO/AEO. One orchestrator routes 17 specialists to audit, create, optimize, and report across classic search (Google, Bing), paid search (Google Ads, Microsoft Ads), and AI answer engines (ChatGPT, Perplexity, Gemini, Google AI Overviews). Chat-first on Google Search Console + free tools, bilingual RO/EN, white-hat only, with a hard **no-fabricated-metrics** rule.

> RO: O echipă de 18 (un orchestrator + 17 specialiști) care îți acoperă toată vizibilitatea în căutare — SEO tehnic și de conținut, internațional, local, e-commerce, link building, digital PR, video/YouTube, date structurate, SEM/plătit și optimizare pentru motoarele AI (ChatGPT, Perplexity, Gemini, AI Overviews). Lucrează din Google Search Console + unelte gratuite, livrează în RO/EN, doar tehnici white-hat și **niciodată cifre inventate**.

## Why it exists

Search in 2026 spans three surfaces at once: blue links, paid results, and AI answers that increasingly replace the click. Most "SEO help" covers one slice. SearchForge covers all three with one coherent team, and refuses the two things that get sites burned — black-hat shortcuts and made-up numbers.

## The team

**Director** (`searchforge` skill) — classifies the request, routes the specialists (parallel for audits, sequential for content), holds the gates, assembles the deliverable.

| Stage | Specialists |
|---|---|
| **Discover** | search-strategist · international-seo-strategist |
| **Build** | technical-seo-engineer · structured-data-specialist · ecommerce-seo-specialist · local-seo-specialist |
| **Content** | content-architect · seo-copywriter · content-editor |
| **Amplify** | link-building-strategist · digital-pr-strategist · video-seo-specialist · sem-strategist · geo-aeo-strategist |
| **Convert & Measure** | cro-specialist · analytics-reporter |
| **Gate** | audit-qa-director (audit synthesis + final QA gate) |

## Install

It's a Claude Code / Cowork plugin. Either:
- Add the `SearchForge` folder to a plugin marketplace you control, or
- Drop it where your Claude plugins live and enable it.

The plugin manifest is `.claude-plugin/plugin.json`. Once enabled, the `searchforge` skill triggers on search/SEO/SEM/GEO requests, and the 17 agents become dispatchable.

## Use it

Just describe the situation — in Romanian or English. Examples:

- "Fă-mi un audit SEO complet pentru [site]." → full audit (parallel fan-out → one prioritized roadmap)
- "I want to rank for [topic] — build the content." → content engine (strategy → brief → write → edit → GEO polish → QA)
- "De ce nu apar în ChatGPT și Perplexity?" → GEO/AEO visibility plan + manual AI-visibility test
- "Set up Google Ads for [product] with a [budget]." → paid search plan (+ landing-page CRO)
- "Optimize my Google Business Profile." → local SEO plan
- "Raport SEO pe luna trecută." → monthly report (RO/EN) from your GSC/GA4 data

The Director will stop at the **three gates** — scope, strategy, and pre-publish QA — so you stay in control.

## How it works (the rules that make it trustworthy)

- **Data honesty.** No invented volumes, rankings, or backlinks. Numbers are sourced from your GSC/GA4 + free tools, or labelled `[ESTIMATE]` / `[VERIFY]` with exactly how to get the real figure. Fabricated metrics fail the QA gate.
- **White-hat only.** Google Search Essentials + spam policies. Black-hat requests get the compliant alternative, not the shortcut.
- **Free-tool first.** Built to run on Google Search Console, GA4, Keyword Planner, Trends, PageSpeed, Bing Webmaster Tools, Microsoft Clarity, Screaming Frog (free), and more — see `references/free-tools.md`.
- **Blue links AND AI answers.** Every page is shaped to be ranked and to be cited.
- **You ship.** Agents draft and recommend; you publish, change the site, launch ads, and contact clients.

## Structure

```
SearchForge/
├── .claude-plugin/plugin.json     # manifest
├── skills/searchforge/
│   ├── SKILL.md                   # the Director (orchestrator)
│   └── references/                # shared brain (8 playbooks)
│       ├── operating-rules.md     # language, data-honesty, white-hat, gates, glossary
│       ├── free-tools.md          # the GSC-first free stack
│       ├── audit-checklists.md    # master audit checklists (8 pillars)
│       ├── geo-aeo-playbook.md    # AI-search citation playbook (2026)
│       ├── schema-library.md      # copy-paste JSON-LD recipes
│       ├── international-seo.md    # RO/EU/US + hreflang
│       ├── reporting-templates.md # KPIs + monthly report (RO/EN)
│       └── handoff-contracts.md   # the artifact each agent produces/consumes
├── agents/                        # 17 specialist agents
├── bible.md                       # team record (brief, architecture, decisions)
├── golden-tests.md                # regression test scenarios
├── CHANGELOG.md
└── README.md
```

## Notes

- Built for **Fri** (Romanian solo creator) — own brands + clients in RO/EU/US.
- Knowledge is current to **June 2026**; volatile specifics (tool limits, character counts, coverage stats) are marked `[VERIFY]` so the team re-checks them live rather than trusting a stale number.
- License: MIT.
