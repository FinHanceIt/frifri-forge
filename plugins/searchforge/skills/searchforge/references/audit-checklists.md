# SearchForge — Master Audit Checklists

The auditors run these; `audit-qa-director` consolidates findings into one scored report. Every checked item maps to a **free tool** (see `free-tools.md`) and a **severity**. Stay chat-first on GSC + free tools; never invent volumes, rankings, or backlink counts — label `[ESTIMATE: method]` or `[VERIFY]` and name the tool that pulls the real number.

**Severity scale:** `Critical` (blocks indexing/ranking or breaks the site) · `High` (clear ranking/UX drag) · `Medium` (meaningful but contained) · `Low` (polish). Always pair a finding with **impact × effort + owner + KPI**.

---

## 1. Technical — owner `technical-seo-engineer`

### Crawlability
| Check | Tool | Severity |
|---|---|---|
| `robots.txt` reachable, not accidentally blocking JS/CSS or key paths | GSC robots tester, browser | Critical if blocking |
| XML sitemap valid, submitted, only 200/indexable URLs, fresh `lastmod` | GSC Sitemaps, Screaming Frog | High |
| Crawl budget: no large blocks of duplicate/low-value/parameter URLs eating crawl | GSC Crawl Stats, Screaming Frog | High on big sites |
| Crawl traps: infinite calendars, session IDs, sort/filter loops | Screaming Frog | High |
| Orphan pages (indexable but not internally linked) | Screaming Frog + GSC + sitemap diff | Medium |

### Indexation
| Check | Tool | Severity |
|---|---|---|
| Page Indexing/Coverage: why valuable URLs are excluded | GSC Page Indexing | Critical |
| `noindex` only where intended (not on money pages) | URL Inspection, Screaming Frog | Critical if wrong |
| Canonicals self-referential or pointing to the right target; no conflicting signals | URL Inspection, Screaming Frog | High |
| Redirect chains/loops collapsed to a single 301 | Screaming Frog | Medium |
| Parameter/faceted bloat: thin filter combinations disallowed or `noindex` | Screaming Frog, GSC | High on faceted sites |

### Architecture & internal links
| Check | Tool | Severity |
|---|---|---|
| Important pages ≤ 3 clicks from home | Screaming Frog (crawl depth) | High |
| Logical hierarchy; descriptive internal anchors (not "click here") | Screaming Frog | Medium |
| No important page stranded behind JS-only nav | URL Inspection (rendered HTML) | High |

### Core Web Vitals (CrUX field data, 75th percentile)
| Metric | Target | Tool | Note |
|---|---|---|---|
| **LCP** | < 2.5s | PageSpeed Insights | Largest content paint |
| **INP** | < 200ms | PSI, DevTools | Replaced FID; **most-failed** metric; usual cause is heavy/synchronous JS — fix via less main-thread work, code-splitting, island/partial hydration |
| **CLS** | < 0.1 | PSI | Reserve space for images/ads/fonts |

Roughly 40% of sites pass all three; treat a failing pillar as `High`. Lab (Lighthouse) diagnoses; **field (CrUX) decides** — don't report a lab score as the field result.

### Mobile, JS, security
| Check | Tool | Severity |
|---|---|---|
| Mobile renders fully; content parity with desktop; tap targets/viewport OK | URL Inspection, PSI mobile | High |
| JS rendering: client-side content actually appears in rendered HTML (Googlebot doesn't click or scroll); prefer SSR/SSG/partial hydration | URL Inspection rendered HTML, DevTools | Critical if content invisible |
| HTTPS valid, no mixed content, HTTP→HTTPS 301 | Browser, Screaming Frog | High |
| Migration check: redirect map 1:1, canonicals/hreflang updated, sitemaps refreshed, traffic monitored | GSC, Screaming Frog | Critical during migration |

---

## 2. On-page — owner `seo-copywriter` + `content-editor`
| Check | Tool | Severity |
|---|---|---|
| One `<H1>`; title ≤ ~60 chars `[VERIFY]`; meta description ≤ ~155 chars `[VERIFY]` | Screaming Frog | Medium |
| Title/H1 match the dominant **search intent** for the query | GSC queries + SERP look | High |
| Heading outline logical (H2/H3 nest correctly, descriptive) | Screaming Frog | Low–Medium |
| Relevant internal links in/out with useful anchors | Screaming Frog | Medium |
| Image `alt` text present and descriptive; filenames sane | Screaming Frog | Low |
| URL short, lowercase, hyphenated, stable | Screaming Frog | Low |
| Freshness: visible published + updated dates; stale facts refreshed | Manual, GSC (decaying pages) | Medium |

---

## 3. Content — owner `content-architect` + `content-editor`
| Check | Tool | Severity |
|---|---|---|
| Topical coverage/depth vs intent and vs top results; subtopics + entities present | SERP, AlsoAsked/PAA | High |
| E-E-A-T signals: first-hand **experience**, demonstrated **expertise**, author bio, citations, **trust** (about/contact/policies) | Manual review | High |
| Originality: original data/insight/examples, not paraphrased consensus; AI-assisted text is fine **if** original/expert/valuable | Manual review | High |
| Cannibalization: one cluster = one URL; merge/redirect competitors | GSC (multiple URLs on one query) | High |
| Decay: pages losing clicks/impressions flagged for refresh | GSC (period compare) | Medium |
| Helpfulness: satisfies the searcher first (Helpful Content is folded into core; thin bulk AI content is the spam target) | Manual review | High |

---

## 4. Off-page — owner `link-building-strategist` + `digital-pr-strategist`
| Check | Tool | Severity |
|---|---|---|
| Backlink profile: top linking domains, linked pages, growth/loss (own site = truth, sampled) | GSC Links, Ahrefs Webmaster Tools (own site) | Medium |
| Anchor health: natural mix; over-optimized commercial anchors are a risk flag | GSC Links | Medium |
| Toxic/spammy links from manipulation; document (disavow is rarely needed — Google usually ignores spam) | GSC Links, manual | Medium |
| Link gap vs competitors → digital-PR earning targets (label estimates) | SERP + manual; free tiers sampled `[ESTIMATE]` | Medium |
| Unlinked brand mentions to convert to links | Manual search, Bing/Google | Low–Medium |

> Competitor backlink totals from free tiers are sampled — mark `[ESTIMATE: free-tier sample]`, never state as exact.

---

## 5. Local — owner `local-seo-specialist`
| Check | Tool | Severity |
|---|---|---|
| Google Business Profile complete: categories, hours, services, photos, attributes | GBP dashboard | High |
| NAP consistent across site + citations (RO: Pagini Aurii, ListaFirme.ro, Bizoo, Afacerist `[VERIFY current]`) | GBP, manual | High |
| Reviews: volume/recency/rating + owner responses | GBP, GBP Insights | Medium |
| Localized content (city/service pages with real local intent, not doorway dupes) | Manual | Medium |
| `LocalBusiness` schema with matching NAP + `geo` | Rich Results Test | Medium |

---

## 6. E-commerce — owner `ecommerce-seo-specialist`
| Check | Tool | Severity |
|---|---|---|
| Category pages indexable, unique intro copy, sensible internal linking | Screaming Frog | High |
| PDPs: unique titles/descriptions, no boilerplate-only duplicates | Screaming Frog | High |
| **Faceted nav rules:** index high-demand facets; prefer `robots.txt`-disallow for thin filter combinations (noindex still consumes crawl budget); use one signal per URL — never stack robots-block + noindex + canonical on the same URL | Screaming Frog, GSC | High |
| `Product` schema (+ `Offer`, price, availability, `AggregateRating` only if real) | Rich Results Test | Medium |
| Lifecycle: in-stock keep · permanently gone **410** · replaced **301** · seasonal/temp out-of-stock keep live | Screaming Frog, GSC | High |
| Duplicate variant URLs canonicalized to a primary | Screaming Frog | Medium |
| Product feed valid (Merchant Center) and consistent with on-page | Merchant Center | Medium |

---

## 7. International — owner `international-seo-strategist`
| Check | Tool | Severity |
|---|---|---|
| `hreflang` valid: correct language[-region] codes, **return/reciprocal** tags, **self-reference**, **x-default** | Screaming Frog, GSC (Intl Targeting `[VERIFY]`) | High |
| URL structure consistent with strategy (ccTLD / subfolder / subdomain) | Manual | Medium |
| Locale targeting matches market (not just language) | Manual | Medium |
| Content **transcreated**, not machine-translated; local terms, currency, units, dates, diacritics | Native review | High |
| No cross-locale duplicate content without correct hreflang/canonical pairing | Screaming Frog | Medium |

See `international-seo.md` for the full method.

---

## 8. GEO/AEO — owner `geo-aeo-strategist`
| Check | Tool | Severity |
|---|---|---|
| Answer-shape: TL;DR/answer-first, Q&A blocks, claim+evidence, data/comparison tables | Manual | High |
| Entities clear and consistent (naming, `sameAs`, topical graph) | Manual, schema | Medium |
| Freshness: key pages updated within ~30 days (≈3.2× more AI citations) `[VERIFY]` | GSC, manual | Medium |
| **Bing index:** sitemap submitted to Bing Webmaster Tools (ChatGPT web search rides Bing) | Bing Webmaster Tools | High for GEO |
| AI-visibility baseline: run the manual testing protocol; log cited/not + competitors + SoV | Manual (ChatGPT/Perplexity/Gemini/AI Overviews) | Baseline |
| GA4 referrals from chatgpt.com / perplexity.ai / gemini tracked | GA4 | Low |

> `llms.txt` is **not** a checklist item for ranking or citation — no major AI engine uses it. Optional dev-docs tooling only. See `geo-aeo-playbook.md`.

---

## Scoring rubric (how `audit-qa-director` consolidates)
- Score **each pillar 1–5** (or a health %): 5 = clean, 1 = critical failures. Roll up to an overall site-health figure.
- Every finding becomes a row: **issue · severity · pillar · impact · effort (S/M/L) · owner · KPI**.
- Sort the roadmap by **impact × effort** — fix Critical/High blockers first, then quick high-impact wins, then long-tail polish.
- A pillar with a Critical open item **cannot** score above 2 regardless of other items.

## Honesty note
These checklists tell you *what's wrong* and *which free tool proves it*. They don't manufacture traffic forecasts or competitor numbers. Where a figure is needed and not in hand, the finding says so — `[VERIFY]` with the tool, or `[ESTIMATE: method]` — and Fri decides. A confident-sounding invented metric fails the gate.
