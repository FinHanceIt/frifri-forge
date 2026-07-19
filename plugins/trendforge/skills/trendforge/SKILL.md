---
name: trendforge
description: >
  Operate TrendForge, a standalone 168-agent trend-prediction megastructure. Use when the user wants
  to scan startup directories, app stores, social, search, dev, funding, research, commerce and global
  markets, detect trends, and forecast what is next — "find trends", "predict app trends", "what is
  about to blow up", "scan everything", "fa-mi un scan de trenduri", "ce trenduri vin". Routes
  acquisition to analysis to forecasting to synthesis with compliance and validation gates.
metadata:
  version: "1.0.0"
  author: "Fri"
---

# TrendForge — Trend-Prediction Megastructure (orchestration)

Operate a **standalone 168-agent system across 20 divisions** that harvests signals from across the internet, turns them into trends, forecasts what is next (with calibrated uncertainty), and surfaces concrete product/app opportunities. Act as the front desk: scope the mission, route it through the pipeline, hold the gates, and assemble one validated, sourced deliverable. Reply to the user in their language; internal artifacts default to English.

## Operating procedure

1. **Intake.** Restate the mission in one line — scope = domains, regions, time-horizon, depth (quick scan vs deep), and the deliverable. If essentials are missing, ask at most 3 questions. For most requests spawn `trendforge-director` first and let it own the run.
2. **Plan.** `run-planner` selects which divisions/scouts/lenses to activate. Do **not** fire all 168 agents by default — pick the smallest set that covers the mission. (A focused "AI consumer apps, US, next 2 quarters" run touches a fraction of the fleet.)
3. **Execute the pipeline (in order).** Acquisition → Data engineering → Data quality → Signal extraction → Temporal/momentum → Network → Forecasting → Validation → Domain lenses → Synthesis, with Governance crosscutting throughout. Run independent scouts/analysts in parallel (single message, multiple Agent calls); sequence where outputs feed inputs. `mission-router` manages the DAG.
4. **Gate.** Enforce four hard gates: **compliance** (compliance-officer) and **ethics** (ethics-manipulation-guard) over all collection; **corroboration** (cross-source-corroborator) before any trend is forecast; **validation** (forecast-validator-gate) before any prediction ships. Max one re-run loop per gate, then escalate to the director.
5. **Assemble.** `report-assembler` produces the package: **Executive Brief** → **Trend Atlas** (ranked trends) → **Prediction Dossiers** (top trends) → **Opportunity & Whitespace map** → **Emerging Watchlist** → **Sources appendix**. Save as files in the working folder. Never dump raw agent transcripts; every claim carries provenance and confidence.

## Run modes

- **Full sweep** — broad scan across all domains; the flagship Trend Atlas. (Heavy: activate widely.)
- **Domain deep-dive** — one domain/region/horizon; activate that domain's scouts + lens + forecasting only.
- **Emerging-only** — bias to early sources (research, dev, fringe, regional) + `emerging-predictor`; the pre-breakout watchlist.
- **Single-trend** — validate/forecast one named trend end to end (corroboration → forecast → dossier).
- **Monitor** — schedule a recurring sweep; `predictive-sentinel`-style watch via the anomaly + memory agents (pair with the schedule tool).

## The 20 divisions (pipeline order)

D0 Command · D1–D10 Acquisition scouts (78) · D11 Data Engineering · D12 Data Quality & Integrity · D13 Signal Extraction & Clustering · D14 Temporal & Momentum · D15 Cross-Signal & Network · D16 Forecasting Ensemble · D17 Validation, Calibration & Bias-control · D18 Domain Lenses · D19 Application & Synthesis · D20 Governance, Compliance & Memory.

Full roster, division-by-division, with each agent's purpose: **`references/org-chart.md`**.

## Method, scoring, sources, compliance (read before a run)

- **`references/methodology.md`** — how signals become trends become forecasts: the cross-source graduation rule, leading-indicator chains, the forecasting ensemble, calibration and the bias controls that keep predictions honest.
- **`references/scorecard.md`** — the composite trend-ranking rubric and the confidence-scoring inputs.
- **`references/source-registry.md`** — the master catalog of source families (the "thousands of sites" backbone) and the columns every source is logged against.
- **`references/compliance.md`** — APIs-first, robots.txt/ToS/GDPR rules, rate-limit policy, RED sources, and the no-fabricated-metrics rule.

## Non-negotiables

APIs first; respect robots.txt, ToS, rate limits and GDPR (compliance-officer can mark any source RED). Never fabricate a metric — if a number is unavailable, it is null. A trend is only forecast if it is corroborated across independent sources. Every forecast ships with prediction intervals and a calibrated confidence, or it does not ship. This system **detects** trends; it must never be used to **manufacture** them.

## Real-data note

The agents are the brain; they drive real tools — WebSearch/WebFetch and the Python sandbox (requests, BeautifulSoup, Playwright, pandas, pytrends, etc.). For always-on collection across tens of thousands of sources, deploy the backend in **`INFRASTRUCTURE-PHASE2.md`** (at the plugin root) and point the scouts at it.
