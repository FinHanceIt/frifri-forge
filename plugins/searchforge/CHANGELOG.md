# Changelog

All notable changes to SearchForge are documented here. Format follows Keep a Changelog; versioning is semantic.

## [1.0.0] — 2026-06-17

Initial release.

### Added
- **Orchestrator** — the `searchforge` Director skill: mission classification, parallel-vs-sequential dispatch maps, three human gates (scope · strategy · pre-publish QA), shared SEO Brief, and the core operating rules.
- **17 specialist agents** across the search value chain:
  - Discover — search-strategist, international-seo-strategist
  - Build — technical-seo-engineer, structured-data-specialist, ecommerce-seo-specialist, local-seo-specialist
  - Content — content-architect, seo-copywriter, content-editor
  - Amplify — link-building-strategist, digital-pr-strategist, video-seo-specialist, sem-strategist, geo-aeo-strategist
  - Convert & Measure — cro-specialist, analytics-reporter
  - Gate — audit-qa-director
- **8 reference playbooks** — operating rules, free-tool stack, audit checklists, GEO/AEO playbook, schema library, international SEO, reporting templates, handoff contracts.
- **Golden test set** — regression scenarios covering routing, data-honesty refusals, white-hat refusals, GEO scoping (incl. the honest llms.txt verdict), international nuance, and the QA gate.

### Principles baked in
- Data honesty: no fabricated metrics; source, `[ESTIMATE]`, or `[VERIFY]`.
- White-hat only: Google Search Essentials + spam policies; compliant alternatives over shortcuts.
- Chat-first on Google Search Console + free tools (no paid suite assumed).
- Bilingual RO/EN deliverables (transcreated, not machine-translated).
- Built for blue links AND AI answers.

### Knowledge baseline (June 2026)
- Core Web Vitals: LCP <2.5s, INP <200ms, CLS <0.1.
- AI Overviews on a large and growing share of searches; informational CTR down — content shaped to be cited, not just ranked.
- GEO/AEO: retrieval vs training mechanisms; Bing index path for ChatGPT; ~30-day freshness advantage for AI citations.
- llms.txt scoped honestly as optional/non-adopted.
- SEM: Google Ads AI Max for Search out of beta and central.
- FAQ/HowTo rich results narrowed — markup kept for entity clarity, eligibility marked `[VERIFY]`.
