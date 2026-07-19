# OfertaForge — Pricing Method
*The Pricing Engineer's playbook. Fri has no rate card, so this IS the starter rate card — clearly a starting heuristic, validated per deal by the Market Analyst.*

## Principle
Fair-but-competitive = a price that (a) covers Fri's cost + a real margin (the **floor**), (b) sits within a defensible **market band** (competitive), and (c) keeps negotiation headroom: **anchor > target > floor**. Never output a single bare number.

## Step 1 — Effort
From the Scope Sheet, sum estimated hours per role and apply a complexity factor:
`Effort_hours = Σ(task hours) × complexity` where Simple = 1.0, Standard = 1.15, Complex = 1.35.

## Step 2 — Pick the hourly (starter rate card)
Base = SMB-RO tier, mid-level solo, EUR/hour. Multiply by tier (see house-style).

| Service | Base €/h (SMB-RO) | EU ×1.6 | US ×2.2 |
|---|---|---|---|
| Web / development | 30 | 48 | 66 |
| Design & branding | 35 | 56 | 77 |
| Copywriting / content | 35 | 56 | 77 |
| Social media (hourly) | 30 | 48 | 66 |
| Video / editing | 35 | 56 | 77 |
| AI consulting | 45 | 72 | 99 |

*Individual-RO = base × 0.7. RON ≈ €×5. USD ≈ €×1.08. Mid-level solo assumed; raise for senior/specialist work.*

## Step 3 — The three numbers
- **Floor** = `Effort_hours × (hourly × 0.65)`, but never below the hard per-project minimum. The walkaway.
- **Target** = `Effort_hours × hourly × (1 + risk_buffer)`. risk_buffer: low 0.05 / medium 0.15 / high 0.30 (vague client, scope-creep, rush).
- **Anchor** = `Target × 1.20` (or the "Best" tier price). Offers and negotiations open here.

## Hard per-project minimums (SMB-RO; scale by tier)
Logo €250 · brand pack €700 · brochure site €800 · social retainer €400/mo · landing copy €250 · social video clip €80 · AI workshop €500.
*Never quote below these even when hours look tiny — protects against under-pricing small jobs.*

## Step 4 — Tiered offer (good / better / best)
- **Good** — trimmed scope at ≈ Target.
- **Better (recommended)** — full scope near Anchor; visually highlighted.
- **Best** — full scope + extras or a retainer, at premium.
Present Best alongside/first so Better reads as the reasonable middle.

## Project benchmark bands (SMB-RO, EUR — multiply by tier)
- Logo €250–600 · brand identity €700–1,800 (G/B/B ≈ €600 / 1,200 / 2,200)
- Brochure website €800–2,500 · web app from €3,000
- Social media retainer: Basic €400–700 · Standard €700–1,400 · Premium €1,400–2,800 /mo
- Copy: landing €250–700 · article €80–250 (or €0.08–0.20/word) · email sequence €300–900
- Video: social clip €80–300 (or €40–120/finished min) · promo/explainer €400–2,000
- AI consulting: €45–90/h · workshop/project €500–2,500

## Currency & rounding
Quote in the client's currency. Round to clean/psychological values. Show the client ONE number per tier; keep ranges internal.

## Discount discipline
Max standard discount 10–15%, and only **traded** (longer timeline, upfront payment, scope cut, case-study/testimonial/referral rights). Every discount needs a reason the client can see. **Below floor = walk.**

## Output
A `Price Structure` artifact (see handoff-contracts.md). Floor and margin stay internal.
