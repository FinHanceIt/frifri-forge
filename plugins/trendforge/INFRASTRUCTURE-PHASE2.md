# TrendForge — Phase 2: The Always-On Collection & Prediction Backend

**Goal:** give the 168-agent brain a body — a deployed system that continuously, compliantly collects from **tens of thousands of sources**, stores full time-series history, runs the analysis/forecasting pipeline on a schedule, and serves results back to the agents and to a dashboard.

This is a Claude-Code-ready build brief. Build it in phases; each milestone is independently useful.

## 1. Architecture (high level)

```
                 ┌─────────────── SCHEDULER (Airflow / Prefect / cron) ───────────────┐
                 v                                                                     v
  SOURCE REGISTRY (Postgres) ──> COLLECTOR WORKERS ──> INGEST QUEUE ──> NORMALIZER ──> DATA WAREHOUSE
        ^   (URLs, ToS, limits)     (API + scrapers)     (Redis/SQS)    (dedupe/ER)    (Postgres + Parquet/DuckDB,
        │                                │                                              ClickHouse for time-series)
        │                                v                                                     │
   COMPLIANCE SERVICE              PROXY / RATE-LIMIT GW                                        v
   (robots/ToS/GDPR gate)         (politeness, rotation*)                              ANALYSIS WORKERS
                                                                                 (momentum, clustering, lead-lag)
                                                                                              │
   VECTOR STORE (Qdrant/pgvector) <──────────── embeddings ───────────────────────────────────┤
                                                                                              v
   DASHBOARD / API (FastAPI + Next.js)  <────  FORECAST SERVICE (ensemble + calibration)  <────┘
        ^                                              │
        └────────────── agents call the API ──────────┘     MEMORY/LEDGER (Postgres) + RETROSPECTIVE job
   *rotation only where ToS/law permit; never to evade an explicit block.
```

## 2. Recommended stack

- **Language:** Python 3.11 (collectors, analysis, forecasting), TypeScript/Next.js (dashboard).
- **Orchestration:** Prefect (simplest) or Airflow. One flow per source-family, fanned out per source.
- **Queue:** Redis (RQ/Celery) or AWS SQS.
- **Collectors:** `httpx` + `tenacity` (APIs); `playwright` (JS pages) only for AMBER/GREEN scrape sources.
- **Warehouse:** Postgres for relational + registries; **Parquet on object storage queried by DuckDB** for raw/large; **ClickHouse** (or TimescaleDB) for the metric time-series panel.
- **Vector store:** Qdrant or pgvector; embeddings via a small/cheap model (e.g. `bge-small`/`e5`) or an embeddings API.
- **Forecasting:** `statsmodels` (ARIMA/SARIMAX), `prophet`, `xgboost` (quantile), `pymc`/`orbit` (Bayesian), `mlforecast`; conformal intervals via `mapie`.
- **Serving:** FastAPI (results + run triggers); Next.js dashboard (Trend Atlas, watchlist, dossiers).
- **Secrets:** environment/secret manager only. **Never commit keys.**

## 3. Data model (core tables)

- `sources` — source_id, name, family, owning_scout, url, method, api_status, robots_status, tos_verdict(GREEN/AMBER/RED), rate_limit, cadence, reliability_tier, region, language, last_pulled.
- `raw_items` — item_id, source_id, pulled_at, payload(json), raw_ref.
- `signals` — signal_id, entity_id, source_id, ts, magnitude, metric, signals(json), reliability, manipulation_score, lang, geo, provenance.
- `entities` — entity_id, canonical_name, aliases[], category, domain.
- `metric_timeseries` — entity_id, metric, ts, value (the ClickHouse panel; append-only, never overwrite).
- `trends` — trend_id, label, taxonomy_node, first_seen, status, confidence_tier.
- `forecasts` — forecast_id, trend_id, run_id, horizon, point[], lo80[], hi80[], lo95[], hi95[], method, error, created_at.
- `predictions_ledger` — trend_id, run_id, called_at, confidence, outcome (for the retrospective).

## 4. The source-scale strategy (how to reach tens of thousands)

1. **Tier the work.** A few hundred **high-value APIs** (GREEN) carry most signal — build these first and well.
2. **Mass RSS/sitemaps.** Thousands of news/blog/newsletter sources via RSS + GDELT — cheap, compliant, high coverage.
3. **Registry-driven scraping.** AMBER sources only, generated from `sources`, each with its own parser + rate budget; add in batches.
4. **Politeness at scale.** Central rate-limit gateway enforces per-domain budgets, backoff, caching; a global crawl-budget caps total QPS.
5. **Coverage loop.** `coverage-gap-monitor` continuously requests new sources; `source-registry-keeper` grades and adds them. Coverage grows weekly without re-architecting.

## 5. Scheduling cadences

- **Daily:** fast consumer signals (app charts, TikTok/Reels/Shorts, Google Trends, GitHub, crypto, news).
- **Weekly:** most directories, social long-tail, reviews, funding, regional.
- **Monthly:** research, patents, scholarly, thematic ETFs, slow regional.
- **Continuous:** anomaly sentinel watches the metric panel and trips early alerts.

## 6. Compliance & safety (build it in, not on)

- Compliance service checks robots.txt/ToS before every new source goes live; stores the verdict; RED is hard-blocked at the collector.
- No collection of personal/sensitive data; aggregate metrics only; GDPR data-minimization and retention policies enforced in the warehouse.
- Proxies/rotation only where lawful and ToS-permitted; explicit blocks escalate, never get evaded.
- Audit log of every fetch (source, time, status) for provenance.

## 7. Cost ballpark (order of magnitude, tune later)

- Small VPS fleet or a single beefy box + object storage: ~$50–300/mo to start.
- Paid data APIs (Sensor Tower, Ahrefs/Semrush, premium news) are the main variable cost — add only the ones that earn their keep.
- Embeddings/forecast compute: modest; batch nightly.

## 8. Milestones

- **M1 — Spine (1–2 wks):** registry + 20 GREEN APIs + queue + Postgres + normalizer + a basic momentum view. Proves the loop end-to-end.
- **M2 — Scale collection (2–4 wks):** mass RSS/GDELT + 100+ sources + proxy/rate gateway + ClickHouse panel + vector store + clustering/corroboration.
- **M3 — Forecasting (2–3 wks):** ensemble + calibration + backtester + validator gate + confidence scoring; nightly forecasts.
- **M4 — Serving (1–2 wks):** FastAPI + Next.js dashboard (Atlas, watchlist, dossiers); agents call the API.
- **M5 — Learning loop:** ledger + retrospective scoring + auto-reweighting; coverage-gap loop expands sources weekly.

## 9. How the agents plug in

The Phase-1 agents stop running ad-hoc Python and instead **call the backend API**: scouts read from `signals`/`metric_timeseries`, analysts query the panel, forecasters call the forecast service, and the synthesis agents read results to write the Atlas. The methodology, scoring and compliance references stay the single source of truth for *how* — the backend just makes it always-on and large.
