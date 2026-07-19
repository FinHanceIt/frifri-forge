# OfertaForge

A bidding, prospecting & negotiation team — **10 AI agents** that take any sales situation (cold lead, brief, DM, referral) and run it to a won deal:
**prospect → scope → market-benchmark → price → offer (RO/EN) → negotiate → close → upsell → learn.**
Built for a solo creative selling design, copywriting, social media, video, web and AI across Romanian, EU and US markets.

## What it does
- Prices **fair-but-competitive even with no rate card** — built-in starter rate card with **floor / target / anchor** so you never quote a bare number.
- **Multi-currency** (RON / EUR / USD) and **multi-tier** (RO individual · RO SMB · EU · US).
- Agents **reason in English**, deliver offers in **Romanian and/or English**.
- **Human gates** at scope, price and send — you stay in control and you send everything.
- **Learns across runs** — a deal ledger reads past lessons at the start and logs each outcome at the end, so the win-rate and playbook compound. File-based memory, not model retraining; it never fabricates an outcome.

## Components
- **Skill: `ofertaforge`** — the orchestrator and entry point. Triggers on "fă o ofertă", "ofertare", "quote this", "new lead", "how much should I charge", "negotiate", "follow up", "turn into a retainer", etc.
- **10 agents:** `deal-lead` · `prospector` · `discovery-scoping` · `market-analyst` · `pricing-engineer` · `offer-writer` · `negotiator` · `closer-followup` · `upsell-retainer` · `ledger-keeper`.
- **Shared brain (references):** house-style · handoff-contracts · pricing-method (starter rate card) · market-bands · objection-library · learning-loop · golden-tests.

## Usage
Describe the situation in plain language:
- *"Un client vrea un site de prezentare și un logo — cât cer?"*
- *"Cold lead: [company] + [website]"*
- *"Clientul zice că e prea scump și vrea −20%."*
- *"Am trimis oferta acum 5 zile, niciun răspuns."*

The `ofertaforge` skill classifies it and runs the right agents in order. You can also call a single agent directly (e.g., the `negotiator`) for a one-off.

## The three gates (you approve)
1. **Scope** — confirm deliverables + assumptions.
2. **Price** — confirm floor + target.
3. **Send** — approve the offer text. *Agents never contact clients — you send.*

## Pricing note
The starter rate card in `pricing-method.md` is a market-informed starting point (2025–2026 freelance data) refined per deal by the `market-analyst`. Tune it as you learn your real numbers and win rates.

## Models
**Opus:** deal-lead, pricing-engineer, negotiator (the decisions that win or lose money). **Sonnet:** the other seven (including `ledger-keeper`, which does bookkeeping and honest scoring).
