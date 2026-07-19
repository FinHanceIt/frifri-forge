# SearchForge — International SEO (RO / EU / US)

Owned by `international-seo-strategist`. Built for serving Fri's own brands and clients across **RO** (Romanian, RON), **EU/English** (multi-country, EUR, GDPR-aware), and **US/Global** (English, USD, highest competition). Reason in English; **transcreate**, never machine-translate. Mark volatile specifics `[VERIFY]`.

---

## 1. Choosing URL structure
| Structure | Example | Pros | Cons | Best when |
|---|---|---|---|---|
| **ccTLD** | `example.ro`, `example.de` | Strongest geo signal; trust in-market; clean legal/hosting split | Splits authority across domains; more cost/admin; each starts cold | A committed, distinct national market (e.g. a real RO presence) |
| **Subfolder** | `example.com/ro/`, `example.com/en/` | **Consolidates authority** on one domain; cheapest to run; easiest hreflang | Geo signal weaker than ccTLD; one platform/CMS | Default for most RO/EU/US setups, especially newer/smaller sites |
| **Subdomain** | `ro.example.com` | Some separation; flexible hosting | Authority sharing is murkier; treated as semi-separate | Tech constraints force separation |

**Default recommendation:** **subfolders** on one strong domain — best authority consolidation for a solo/lean operation, simplest hreflang. Use a ccTLD only when a market warrants its own identity and you can invest in it. Decide once; document it; don't mix structures per locale without reason. `[VERIFY per project]`

---

## 2. hreflang done right
hreflang tells Google **which language/region version** to serve — it is **not** a ranking boost; it prevents the wrong-locale page from showing and reduces cross-locale duplication.

Rules:
- **Codes:** `language` (ISO 639-1) optionally `-REGION` (ISO 3166-1 alpha-2): `ro`, `en`, `en-US`, `en-GB`, `de-DE`. Language is required; region is optional and only for region-specific variants.
- **Return/reciprocal:** every page in the set must reference **every** other version, including itself (**self-reference**).
- **x-default:** add an `x-default` for the fallback/selector page when no locale matches.
- **Delivery:** via `<link>` tags in `<head>`, **or** HTTP headers (non-HTML), **or** the **XML sitemap** (cleanest for large sites — keeps tags out of every page head). Pick one method; don't half-duplicate across two.
- **Absolute URLs**, indexable targets only (never point hreflang at a `noindex`/redirected/canonical-away URL).

**Most common mistakes:** missing self-reference · non-reciprocal (A→B but not B→A) · wrong/invented region codes (`en-EU` is **not** valid — EU isn't a country) · pointing at redirected or non-canonical URLs · mixing `<link>` and sitemap inconsistently · using hreflang to "rank" rather than to route.

---

## 3. Locale vs language targeting
- **Language targeting** = one version per language (`ro`, `en`). Enough when content is identical for all speakers of that language.
- **Locale/region targeting** = language **+** market specifics (currency, shipping, legal, examples): `en-US` vs `en-GB`, `de-DE` vs `de-AT`.
- Don't create region splits you can't differentiate — duplicate `en-US`/`en-GB` pages with nothing different just add maintenance. Split by region **only** when content genuinely differs.

---

## 4. GSC International Targeting / per-property setup
- The legacy **International Targeting** country-setting tool is deprecated/limited `[VERIFY]`; geo-targeting is now driven mainly by **ccTLD, hreflang, and on-page/server signals**.
- Verify **each locale property** (or a Domain property covering all) in GSC so you can read queries/coverage **per market** — RO demand and SERP behavior differ from US and must be analyzed separately.
- Check the hreflang/international reports for return-tag errors after launch.

---

## 5. RO ↔ EN transcreation
Translation ≠ optimization. Romanian searchers use **different real query terms** than a literal translation of the English page, and local intent differs.

- **Search the term people actually type**, then write to it — don't rank a translated phrase nobody searches. Validate against RO autocomplete + Keyword Planner ranges + Trends.
- **Currency/units:** RON (and EUR where shown) for RO, USD for US; metric for RO/EU, adapt for US; localize sizes, VAT-inclusive pricing where expected.
- **Date/number formats:** RO uses `zz.ll.aaaa` and `,` as the decimal separator; US uses `mm/dd/yyyy` and `.`.
- **Examples & references** localized (local brands, places, scenarios) — not US examples translated.
- **Diacritics:** write correct Romanian (ă, â, î, ș, ț). Note that many users **type queries without diacritics** — cover both forms in content/headings naturally so you match either (see §8).
- **Tone/idiom:** transcreate idioms; a literal calque reads foreign and underperforms.

---

## 6. Per-market keyword research nuance
- **Google Trends geo-compare:** relative interest **within** a market and across markets — never an absolute volume.
- **RO autocomplete + "People also ask" + "Related searches"** in Romanian: the real phrasing, question forms, and diacritic patterns.
- **Local competitors** (who actually ranks in the RO/EU SERP) reveal intent and gaps better than US competitors.
- **Keyword Planner** ranges per geo/language for directional sizing — label `[ESTIMATE]`.
- Never assume a keyword's US demand/intent transfers to RO. Re-research each market.

---

## 7. Avoiding cross-locale duplicate content
- Same-language locales (`en-US`/`en-GB`, or RO content reused) need **correct hreflang** so Google treats them as alternates, not duplicates.
- Keep **self-referencing canonicals** per locale (canonical points to the **same-locale** URL, not the other language).
- Don't canonicalize one locale to another — that drops it from its market.
- Differentiate same-language locales with genuine local content where you can.

---

## 8. Market prioritization
- **Don't launch all locales at once.** Start with the market with real demand + capacity to support it (content, links, reviews, local proof).
- Sequence: prove one locale → templatize → expand. A thin half-built locale dilutes authority and creates hreflang debt.
- Score markets by demand × competition × your ability to serve (language, fulfillment, support) — pair each with impact × effort like every SearchForge rec.

---

## 9. RO-specific notes
- **Diacritics in queries:** Romanians search both with and without diacritics; content should read correctly (with diacritics) yet still match diacritic-free queries. Don't strip diacritics from copy to "match" — write properly and let Google's normalization + natural coverage handle it `[VERIFY]`.
- **eMAG / marketplaces:** much RO product discovery starts on **eMAG** and marketplaces, not Google — factor marketplace presence into an e-commerce strategy (cross-ref `ecommerce-seo-specialist`).
- **Local directories:** Pagini Aurii, ListaFirme.ro, Bizoo, Afacerist for NAP/citations `[VERIFY current]` (cross-ref `local-seo-specialist`, `free-tools.md`).
- **SERP behavior:** RO SERPs show fewer/different SERP features than US; AI Overview coverage and feature mix differ by market `[VERIFY]` — confirm against the live RO SERP, don't assume US patterns.

---

## hreflang example block (RO + EN + x-default)
Subfolder setup, `<link>` delivery — each version lists **all** versions including itself:
```html
<link rel="alternate" hreflang="ro" href="https://example.com/ro/pagina/" />
<link rel="alternate" hreflang="en" href="https://example.com/en/page/" />
<link rel="alternate" hreflang="x-default" href="https://example.com/en/page/" />
```
Same three tags appear on **both** `/ro/pagina/` and `/en/page/`. For large sites, deliver the same mapping via the **XML sitemap** instead of per-page `<link>` tags.

---

## Honesty note
hreflang routes users to the right version; it doesn't rank. Volumes per market are ranges (`[ESTIMATE]`) until pulled from GSC per property. RO behavior is researched, not assumed from US. Transcreation is judged by a native speaker, never by a translation engine.
