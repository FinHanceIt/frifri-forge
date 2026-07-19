# SearchForge — KPIs & Reporting Templates

Owned by `analytics-reporter`. Every figure obeys the data-honesty rule: sourced, `[ESTIMATE: method]`, or `[VERIFY]`. Reports are delivered in the client's language (RO/EN).

## KPI definitions (and their free source)
| KPI | Definition | Source |
|---|---|---|
| Organic clicks / impressions / CTR / avg position | Performance on Google organic | **GSC** Performance |
| Indexed pages / coverage | Pages eligible to rank | GSC Page Indexing |
| Core Web Vitals | % of URLs "Good" for LCP/INP/CLS | GSC CWV / CrUX / PageSpeed |
| Organic sessions / engaged sessions | On-site organic traffic & quality | GA4 |
| Conversions / conversion rate | Goal completions from organic/paid | GA4 (with tracking caveats) |
| Keyword movements | Position changes for tracked terms | GSC (own) + manual checks `[label]` |
| Backlinks / referring domains | Links to the site | GSC Links + Bing WMT (sampled) |
| AI-visibility / share of voice | % of target questions where the brand is cited by AI engines | Manual protocol (geo-aeo-playbook) |
| Local actions | Calls, directions, profile views | GBP Performance |
| ROAS / CPA (paid) | Return / cost per acquisition | Google & Microsoft Ads + GA4 |

## North-Star → drivers (build per client)
Pick one North-Star (e.g. organic-driven leads or revenue). Decompose into drivers: impressions (demand captured) → CTR (snippet/title) → sessions → conversion rate → value. Each driver gets an owner and a lever. This makes every report tie back to a number Fri can move.

## Monthly report template (EN)
1. **Executive summary** — 3–5 decisions/outcomes in plain language, decision-first.
2. **Results vs. last period** — KPI table with **sourced** deltas (GSC/GA4); call out what's `[ESTIMATE]`.
3. **What we did** — work shipped this month, mapped to the approved roadmap.
4. **Wins & learnings** — what moved, what didn't, why.
5. **AI-search visibility** — citations/share-of-voice across ChatGPT/Perplexity/Gemini/AI Overviews (manual read).
6. **Next month** — prioritized plan (impact × effort · owner · KPI).
7. **Appendix** — raw numbers + their source.

## Șablon raport lunar (RO)
1. **Rezumat executiv** — 3–5 decizii/rezultate, pe scurt, orientat pe decizie.
2. **Rezultate față de perioada anterioară** — tabel KPI cu variații **din surse** (GSC/GA4); marchează ce e `[ESTIMARE]`.
3. **Ce am făcut** — activitățile lunii, corelate cu roadmap-ul aprobat.
4. **Reușite & învățăminte** — ce a funcționat, ce nu, de ce.
5. **Vizibilitate în căutarea AI** — citări/share-of-voice în ChatGPT/Perplexity/Gemini/AI Overviews (verificare manuală).
6. **Luna viitoare** — plan prioritizat (impact × efort · responsabil · KPI).
7. **Anexă** — cifre brute + sursa lor.

## Reporting rules
- **No number without a source.** If GSC/GA4 weren't shared, list what to export and pause the metric.
- Compare like-for-like periods; note seasonality (Trends) and algorithm updates that affect the read.
- Attribution is imperfect — state the model and its caveats; never imply false precision.
- Tie every result back to the approved strategy and the next decision.
