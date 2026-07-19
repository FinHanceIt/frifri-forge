# SearchForge — The Free-Tool Stack (GSC-first)

The team works without a paid Ahrefs/Semrush seat. This is the stack that replaces them, mapped to each job, with a note on **what each tool is truth for vs. only directional**. When a number isn't available here, label it `[ESTIMATE]` or `[VERIFY]` (see `operating-rules.md`).

## Owned-site truth (always start here)
| Tool | Use it for | Truth level |
|---|---|---|
| **Google Search Console (GSC)** | Real queries, impressions, clicks, CTR, avg position; Coverage/Page Indexing; CWV report; URL Inspection (live render, indexability); sitemaps; Links report (own backlinks); manual actions | **Truth** for the site's own search data |
| **Google Analytics 4 (GA4)** | Sessions, channels, engagement, conversions, funnels, landing pages, referrals (incl. from chatgpt.com / perplexity.ai / gemini) | **Truth** for on-site behavior |
| **Bing Webmaster Tools** | Bing indexation + queries; backlinks; site scan. **Critical for GEO** — ChatGPT web search uses Bing's index, so submit the sitemap here | **Truth** for Bing/ChatGPT-retrieval reach |
| **Google Business Profile Insights / Performance** | Local discovery, calls, directions, searches that surfaced the listing | **Truth** for local |
| **YouTube Studio** | Impressions, CTR, watch time, retention, traffic sources, search terms | **Truth** for video |

## Keyword & demand research
| Tool | Use it for | Truth level |
|---|---|---|
| **Google Keyword Planner** (free with an Ads account) | Volume *ranges*, related terms, forecast | Directional (ranges; logged-in detail varies) |
| **Google Trends** | Relative interest, seasonality, rising/breakout queries, geo comparison | Relative only — **never** an absolute volume |
| **Google autocomplete / "People also ask" / "Related searches"** | Real phrasing, question forms, intent variants | Qualitative demand signal |
| **AlsoAsked**, **AnswerThePublic**, **Ubersuggest**, **Keyword Surfer** (free tiers) | Question maps, long-tail expansion | Directional; verify volumes against GSC/Planner |

## Technical, speed & indexation
| Tool | Use it for |
|---|---|
| **PageSpeed Insights** | CWV field (CrUX) + lab (Lighthouse); LCP/INP/CLS diagnostics |
| **Lighthouse / Chrome DevTools** | Performance traces, render-blocking, main-thread/INP work, coverage |
| **Screaming Frog SEO Spider** (free ≤ 500 URLs) | Crawl: titles/meta, status codes, redirects, canonicals, depth, broken links |
| **GSC URL Inspection + Coverage** | Indexability, rendered HTML, why a page isn't indexed |
| **Rich Results Test** + **Schema Markup Validator (schema.org)** | Validate structured data & rich-result eligibility |

## Backlinks & off-page
| Tool | Use it for | Truth level |
|---|---|---|
| **GSC Links report** | Top linking sites, linked pages, anchor text — the site's own profile | **Truth** for own backlinks (sampled) |
| **Ahrefs Webmaster Tools** (free for verified own site) | Backlink profile + site audit for a site you own | Truth for owned site |
| **Bing Webmaster Tools** | Additional backlink data | Supplementary |
| Competitor backlinks | Free tiers are limited — use SERP analysis + manual checks; label gaps `[ESTIMATE]` | Directional only |

## Local (incl. Romania)
Google Business Profile + **NAP citations**: general directories + RO-specific (**Pagini Aurii, ListaFirme.ro, Bizoo, Afacerist**) `[VERIFY current]`. Apple Business Connect, Bing Places.

## Behavior & CRO
**Microsoft Clarity** — genuinely free and unlimited heatmaps + session recordings + frustration signals. GA4 path/funnel exploration. (A/B testing needs real traffic for significance — see `cro-specialist`.)

## AI-search visibility (GEO/AEO)
Most trackers (Otterly, Profound, Semrush AI Toolkit, Ahrefs Brand Radar) are **paid**. Free/manual protocol: prompt ChatGPT / Perplexity / Gemini / Google AI Overviews with the target questions, log whether and where the brand is cited and the share-of-voice vs competitors, repeat on a fixed cadence, and watch GA4 referrals from AI domains + Bing/GSC. Detail in `geo-aeo-playbook.md`.

## Honesty note
Keyword Planner gives ranges, Trends is relative, free backlink tiers are sampled. State the source next to every number. Directional is fine — *labelled* directional. Invented precision is not.
