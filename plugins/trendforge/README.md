# TrendForge

**A standalone trend-prediction megastructure — 168 specialist agents across 20 divisions.**

TrendForge harvests signals from across the internet (startup directories, app stores, social platforms, search, dev ecosystems, funding, research, commerce and global/regional markets), turns them into trends, **forecasts what is next with calibrated confidence**, and surfaces concrete app/product opportunities — APIs-first and compliance-gated.

## What it does

1. **Acquire** — 78 acquisition scouts (D1–D10) each own a corner of the internet and emit clean, dated, deduplicated signals.
2. **Engineer & clean** — normalize, resolve entities, embed; strip bots/spam, grade reliability, correct sampling/survivorship bias (D11–D12).
3. **Extract & corroborate** — atomize, cluster into trends, and graduate only those confirmed across **independent** sources (D13).
4. **Analyze** — momentum, acceleration, lifecycle, saturation, lead-lag chains, convergence, virality, geographic diffusion, capital+attention alignment, crowdedness (D14–D15).
5. **Forecast** — an ensemble of models produces trajectories **with 80%/95% prediction intervals** (D16), then validation/calibration/bias-control gates them (D17).
6. **Interpret & synthesize** — 14 domain lenses (D18) adjust for how each market really behaves, then synthesis (D19) writes the deliverable.
7. **Govern** — compliance, ethics, provenance, cross-run memory and a learning loop run throughout (D0, D20).

## How to use

Trigger the orchestration skill with things like: *"find trends in X"*, *"predict app trends"*, *"what's about to blow up in AI tools"*, *"scan everything and give me a trend report"*, *"fă-mi un scan de trenduri"*, *"ce trenduri vin în 2026"*. The `trendforge-director` scopes the run, activates only the divisions the mission needs, runs the pipeline, holds the gates, and assembles the package.

**Run modes:** Full sweep · Domain deep-dive · Emerging-only (pre-breakout watchlist) · Single-trend validate+forecast · Monitor (scheduled).

## What you get

Executive Brief → **Trend Atlas** (ranked trends with evidence, momentum, lifecycle, forecast, confidence) → **Prediction Dossiers** (top trends, deep) → **Opportunity & Whitespace map** → **Emerging Watchlist** → Sources appendix. Every claim carries provenance and confidence; no fabricated metrics.

## Structure

```
trendforge/
├── .claude-plugin/plugin.json
├── skills/trendforge/
│   ├── SKILL.md                 # orchestration entry point
│   └── references/
│       ├── org-chart.md         # all 168 agents, by division
│       ├── methodology.md       # how signals become calibrated forecasts
│       ├── source-registry.md   # the source backbone (thousands of sites)
│       ├── scorecard.md         # ranking + confidence + opportunity rubrics
│       └── compliance.md        # APIs-first, robots/ToS/GDPR, no-fabrication
├── agents/                      # 168 specialist agents
├── INFRASTRUCTURE-PHASE2.md     # build brief for the always-on scraping backend
└── README.md
```

## Two phases

- **Phase 1 (this plugin)** — the *brain*: orchestration, source intelligence, analysis & forecasting methodology, and reporting. It drives real tools (WebSearch/WebFetch + the Python sandbox: requests, BeautifulSoup, Playwright, pandas, pytrends, …) for on-demand runs.
- **Phase 2 (`INFRASTRUCTURE-PHASE2.md`)** — the *muscle*: a deployed always-on backend (collectors, queue, warehouse, vector store, schedulers, dashboards) so the scouts can continuously cover tens of thousands of sources. Build it with Claude Code, then point the scouts at it.

## Compliance

APIs first. Respect robots.txt, ToS, rate limits and GDPR (the compliance-officer can mark any source RED). Never fabricate a metric. Detect trends — never manufacture them. See `references/compliance.md`.

*Built for Fri · v1.0.0 · MIT.*
