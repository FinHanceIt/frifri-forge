# SearchForge — Handoff Contracts

The named artifact each specialist **produces** and **consumes**, so handoffs never lose information. The Director keeps the live **SEO Brief** (site, markets, goals, target map, decisions, roadmap, KPIs) as the running record that threads these together.

| Specialist | Produces (named artifact) | Consumes | Hands to |
|---|---|---|---|
| **search-strategist** | **Target Map** (cluster · intent · difficulty · demand[source] · target URL · opportunity) + SERP Notes + Competitor Gap | site, market(s), goal | content-architect, international-seo-strategist, geo-aeo-strategist, ecommerce/local, sem-strategist |
| **international-seo-strategist** | **Locale Strategy** (market priority · hreflang map · URL-structure choice · transcreation brief · per-locale terms) | Target Map, markets | technical-seo-engineer (hreflang impl), content-architect + seo-copywriter (locale briefs), local-seo-specialist |
| **technical-seo-engineer** | **Technical Audit & Fix List** (finding · severity · evidence · fix · owner) + architecture/internal-link recs + CWV diagnosis | live URLs, GSC/PSI exports | structured-data-specialist, content-architect, international (hreflang), cro-specialist (CWV) |
| **structured-data-specialist** | **Schema Pack** (validated JSON-LD per template) + entity/sameAs map | page types, content, business data | geo-aeo-strategist, ecommerce, local, video, content-architect |
| **ecommerce-seo-specialist** | **E-com SEO Plan** (category/PDP recs · faceted-nav rules · lifecycle keep/301/410 · feed notes) | store structure, product data | technical-seo-engineer, structured-data-specialist, content-architect, sem-strategist |
| **local-seo-specialist** | **Local SEO Plan** (GBP optimization · citation list · review plan · local pages · schema need) | business info, locations | structured-data-specialist, content-architect, digital-pr-strategist, analytics-reporter |
| **content-architect** | **Content Brief** (per page) + cluster/content strategy + on-page spec + refresh plan | Target Map, GEO reqs, schema needs, locale brief | seo-copywriter |
| **seo-copywriter** | **Draft** (content + title/meta + FAQs, RO/EN) | Content Brief, locale brief | content-editor |
| **content-editor** | **Edited Content + Fix List** (pass / line-level fixes) | Draft + Brief | seo-copywriter (fixes) → geo-aeo-strategist (polish) → audit-qa-director |
| **link-building-strategist** | **Link Plan** (backlink audit · link-gap · target list · outreach templates · disavow if any) | GSC Links, niche, assets | digital-pr-strategist, content-architect (assets), analytics-reporter |
| **digital-pr-strategist** | **Digital PR Plan** (campaign ideas · media list · pitches/releases · mention reclamation) | brand, data assets | link-building-strategist, geo-aeo-strategist, content-architect, analytics-reporter |
| **video-seo-specialist** | **Video SEO Plan** (YouTube optimization · VideoObject need · transcript/caption plan · SERP/AI strategy) | video assets/topics | structured-data-specialist, content-architect, geo-aeo-strategist |
| **sem-strategist** | **Paid Search Plan** (campaign architecture · keywords/negatives · ad copy · bidding/budget · tracking · landing reqs) | goals, budget (Fri), conversion data | cro-specialist, analytics-reporter, ecommerce (Shopping) |
| **cro-specialist** | **CRO Plan** (LP structure · hypotheses · test design · friction fixes) | GA4/Clarity data, traffic | seo-copywriter, sem-strategist, technical-seo-engineer, analytics-reporter |
| **geo-aeo-strategist** | **GEO Requirements + AI-Visibility Report** (answer-shape rules · entity/freshness reqs · Bing-index actions · manual visibility results) | content, entities, target questions | content-architect, seo-copywriter, structured-data-specialist, video, analytics-reporter |
| **analytics-reporter** | **Performance Report / KPI Read** (RO/EN, baselined, sourced) | GSC/GA4 exports (pasted) | Director, content-architect (decay/refresh), all (KPIs) |
| **audit-qa-director** | **Consolidated Roadmap** and/or **QA Verdict + Routed Fix List** | all auditor outputs / any deliverable | Director (cleared), specialists (fixes) |

**Rule:** if an input artifact is missing, request it by name rather than inventing its contents. Every artifact that contains a metric obeys the data-honesty rule.
