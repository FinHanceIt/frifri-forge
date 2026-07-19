# SearchForge — GEO/AEO Playbook (getting cited by AI answer engines)

Owned by `geo-aeo-strategist`; touches `content-architect`, `seo-copywriter`, `structured-data-specialist`, `digital-pr-strategist`. Built for blue links **and** AI answers. No paid AI trackers assumed — the visibility protocol below is free and manual. Never invent citation counts or share-of-voice; log what you actually observe.

---

## 1. What GEO/AEO is, and why now
**GEO** (Generative Engine Optimization) / **AEO** (Answer Engine Optimization) = earning your brand a **citation or mention inside an AI-generated answer**, not just a blue link. Used interchangeably here.

Why it matters in 2026:
- AI Overviews appear on **~25–26% of US searches** `[VERIFY — 2026 studies vary, some report higher]`, ~39% of *informational* queries, and ~66% of 7+-word queries.
- Informational-query CTR is down **double digits** where an AI answer shows; clicks concentrate on the few **cited** sources.
- Assistant reach is large: **ChatGPT ~800M WAU · Gemini ~750M MAU · Perplexity ~45M · Claude ~30M** `[VERIFY — moving fast]`.

**Google's official line:** there is **no special "AI ranking."** Strong classic SEO + structured data + entity authority is what earns AI inclusion. There is no separate lever to pull — GEO is SEO done well, shaped to be *extractable*.

---

## 2. The TWO mechanisms (decide tactics by which one you're chasing)
| Mechanism | How it works | What it rewards | Tactics it implies |
|---|---|---|---|
| **(a) Retrieval at query time** | Engine fetches live results, reads them, summarizes with citations (Perplexity, Google AI Overviews, ChatGPT web search via **Bing's index**) | Being crawlable, indexed, fresh, and **easy to extract** right now | Behaves like SEO: be indexed (incl. **Bing**), answer-first, clean markdown, current dates |
| **(b) Training-data answers** | Model answers from what it learned **before its training cutoff**, no live fetch | Being **authoritative and widely referenced before the cutoff** | Long-game authority: original data, citations from others, entity consistency, durable reputation |

Most engines blend both. You can't optimize the training cutoff directly — you earn it by being the source people already cite.

---

## 3. Engine map
| Engine | Primary mechanism | Index it reads | SearchForge implication |
|---|---|---|---|
| **ChatGPT** (web search) | Retrieval + training | **Bing** | Submit sitemap to **Bing Webmaster Tools**; be Bing-indexed |
| **Perplexity** | Live retrieval, always cites | Own crawl + partners | Answer-first pages with quotable claims win citations |
| **Gemini / Google AI Mode** | Retrieval + training | **Google** | Classic Google SEO + structured data + entities |
| **Google AI Overviews** | Retrieval over Google index | **Google** | Same as ranking well; cited sources skew to page-1-ish authority |
| **Copilot** | Retrieval + training | **Bing** | Same as ChatGPT — Bing matters |

Takeaway: **Google index covers Gemini/AI Overviews; Bing index covers ChatGPT/Copilot.** Cover both. `[VERIFY — engine plumbing changes]`

---

## 4. On-page citation tactics (the extractable-content checklist)
- **Answer-first / TL;DR.** Lead with a 2–4 sentence direct answer the engine can lift, then expand.
- **Claim + evidence.** State a fact, immediately back it (number, source, example). Engines quote claims that carry their own proof.
- **Q&A blocks.** Real questions as headings with tight answers underneath (works regardless of FAQ rich-result status — see §7).
- **Data & comparison tables.** Structured rows are highly quotable; put the comparison the user is asking for *in a table*.
- **Descriptive headings.** Headings that read as questions/statements, not clever labels.
- **Dense, scannable markdown.** Short paragraphs, lists, tables, bolded key terms. Walls of text don't get extracted.
- **Visible author + published + updated dates** on the page (not just in schema).
- **Original data/statistics worth quoting.** A stat only you publish is a citation magnet — it's the single strongest GEO asset.

---

## 5. Entity & authority building
- **Consistent entity naming** everywhere (brand, product, author spelled identically).
- **`sameAs`** links from `Organization`/`Person` schema to official profiles (cross-ref `structured-data-specialist`, `schema-library.md`).
- **Digital PR** earns the third-party mentions that build the entity in training data and live retrieval (cross-ref `digital-pr-strategist`).
- **Author bios + credentials** (real E-E-A-T: Experience, Expertise, Authoritativeness, Trust) on bylined content.
- **Strong topical graph** — interlinked coverage of a subject so the brand reads as an authority on it, not a one-off page.

AI citations follow **real authority + clarity + freshness**. There is no shortcut that substitutes for being genuinely worth citing.

---

## 6. Freshness cadence
Pages updated within **~30 days** earn roughly **3.2× more AI citations** `[VERIFY]`. Practical cadence:
- Review cornerstone/answer pages monthly; update facts, stats, dates.
- Make the update **substantive** (new data, revised guidance) — not a date bump. Hollow re-dating is a manipulation pattern.
- Surface the `dateModified` **on the page**, not only in schema.

## 6b. The Bing step (for ChatGPT/Copilot)
ChatGPT web search and Copilot read **Bing's index**. So:
1. Verify the site in **Bing Webmaster Tools**.
2. Submit the XML sitemap there (not just GSC).
3. Confirm key pages are Bing-indexed.

This is the most overlooked, highest-leverage GEO step. See `free-tools.md`.

---

## 7. The honest `llms.txt` verdict
`llms.txt` is **not adopted by any major AI engine.** Google has confirmed Search ignores it; ALLMO's 94k-URL study found **no citation uplift**; only ~5–15% of sites have one. Treat it as **optional dev-docs tooling only** — never a ranking or citation lever. Telling Fri (and clients) this plainly is a selling point, not a gap. Don't bill effort against it.

Likewise, FAQ rich results have been heavily narrowed/removed by Google on the 2026 timeline `[VERIFY current status]`; HowTo rich results are deprecated. Keep the markup for entity/Q&A clarity, not for a guaranteed rich result.

---

## 8. Free manual AI-visibility testing protocol
No paid tracker required. Run it on a fixed cadence (e.g. monthly) and keep the log.

1. **Define a target question set** — the 15–40 real questions your buyers ask (informational, comparison, "best X for Y", branded). Reuse them every cycle.
2. **Prompt each engine** with each question: ChatGPT (web), Perplexity, Gemini, Google AI Overviews. Use neutral phrasing; don't lead the model to you.
3. **Log per question:** cited? (yes/no), position/prominence, **which competitors** were cited, the URL cited, and notable wording.
4. **Compute share-of-voice** = your citations ÷ total brand citations across the set. Track the trend, not a single snapshot.
5. **Watch GA4 referrals** from `chatgpt.com`, `perplexity.ai`, `gemini` (and Bing/GSC) as the corroborating real-traffic signal.
6. **Cadence + diff:** re-run unchanged questions each cycle; attribute movement to the content/PR/freshness work shipped between runs.

Record everything as observed data. If a number is an approximation, label it `[ESTIMATE: manual log, n questions]`.

---

## 9. What NOT to do / myths
- **Don't spam `llms.txt`** as a ranking or citation lever — nothing reads it for that.
- **Don't fake authority** — fabricated author credentials, fake reviews, invented "studies." It's the spam target and it backfires.
- **Don't keyword-stuff "AI-friendly" prose.** Clarity and structure win; stuffing doesn't.
- **There is no secret AI-ranking dial.** Citations track authority + extractable clarity + freshness — earn those.
- **Don't claim citation gains you didn't measure.** If you didn't log it in the protocol, it didn't happen.
