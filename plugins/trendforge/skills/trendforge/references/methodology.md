# TrendForge — Prediction Methodology

How raw internet noise becomes a calibrated forecast. Every agent serves one of these steps; this is the logic that ties them together.

## 1. Signal → Trend → Forecast (the spine)

1. **Acquire** (D1–D10): scouts pull dated, sourced items, APIs-first.
2. **Engineer** (D11): normalize to one canonical signal schema, resolve entities, embed.
3. **Clean** (D12): strip spam/bots, grade source reliability, correct sampling/survivorship bias, validate spikes.
4. **Extract** (D13): atomize signals, cluster into candidate trends, extract jobs-to-be-done.
5. **Corroborate** (GATE): a candidate **graduates to a trend only if it appears across ≥2 independent source-types** (configurable), weighted by reliability and discounted for manipulation. This single rule kills most hype.
6. **Measure time** (D14): momentum (1st derivative), acceleration (2nd derivative / inflection), seasonality removal, lifecycle staging, saturation, **lead-lag mapping**.
7. **Measure structure** (D15): convergence, virality/R, propagation, geographic diffusion, capital+attention alignment, competitive density.
8. **Forecast** (D16): an **ensemble** of methods produces point paths WITH 80%/95% intervals.
9. **Validate** (GATE, D17): backtest, calibrate, check leakage, correct biases, score confidence — ACCEPT/RE-RUN/REJECT.
10. **Interpret** (D18): domain lenses adjust for how each domain actually diffuses and monetizes.
11. **Synthesize** (D19): rank, map opportunities/whitespace, write the Atlas + dossiers + brief.

## 2. The leading-indicator chain (why prediction is possible)

Trends rarely appear everywhere at once; they propagate along a fairly stable chain, each step leading the next by a measurable lag:

```
research (arXiv, Scholar, patents)
   → dev ecosystem (GitHub, HF, package downloads, Stack Overflow)
      → early adopters / fringe (HN, niche Reddit, Discord, emerging social, regional leaders e.g. CN/KR/IN)
         → builders (Product Hunt, YC, Indie Hackers, accelerators, funding)
            → prosumer/consumer (App stores, TikTok/Reels, search demand, commerce)
               → mainstream (mass search, news, hiring at scale)
```

`lead-lag-correlator` learns the real lags empirically (out-of-sample validated); `leading-indicator-chain-forecaster` then predicts a later stage from an earlier one. `geographic-diffusion-tracker` does the same across regions. `emergence-predictor` looks at the **earliest** links to call trends before they reach the consumer layer — the highest-value, highest-uncertainty output.

## 3. Why an ensemble (D16)

No single model is right across regimes. Each trend gets ≥2 complementary methods (ARIMA/SARIMAX, Prophet, XGBoost-quantile, Bayesian structural, historical-analogy, diffusion/Bass, leading-indicator-chain). `ensemble-blender` weights them by **validated** accuracy and widens intervals when they disagree. Disagreement is information, not a bug.

## 4. Uncertainty is mandatory

Every forecast ships with 80% and 95% prediction intervals and a 0–100 confidence. `calibration-auditor` checks that 80% intervals actually contain the truth ~80% of the time and recalibrates if not. A point estimate with no interval never ships.

## 5. The bias controls (why we are not just measuring hype)

| Bias / failure | Guard agent | Correction |
|---|---|---|
| Manufactured virality | `bot-astroturf-detector` | manipulation discount |
| Echo counted as confirmation | `independence-correlation-auditor` | one botnet/PR = one effective source |
| Over-indexing English/US/Twitter | `sampling-bias-auditor` | reweight / collect more |
| Only seeing winners | `survivorship-bias-auditor` | failure base rates from the graveyard |
| Naive hype extrapolation | `hype-cycle-corrector` | anticipate the trough |
| Latest spike dominates | `recency-bias-corrector` | re-anchor to base rates |
| Future data in features | `lookahead-leakage-auditor` | block leaked forecasts |
| Seasonal mistaken for trend | `seasonality-decomposer` | deseasonalize first |
| Spike is an artifact | `outlier-validator` | confirm before propagating |

## 6. Confidence score inputs (`confidence-scorer`)

source reliability × independent corroboration × (1 − manipulation discount) × model agreement × backtested accuracy × calibration quality × (− fragility from premortem). Output is comparable across trends and runs.

## 7. The learning loop

`memory-ledger-keeper` records every call (trend, date, confidence). `run-retrospective` later scores matured calls against reality (hit-rate, calibration), diagnoses systematic misses, and feeds concrete fixes (reweight models, adjust thresholds, add/drop sources) back into the next run. The system is supposed to get more accurate over time.

## 8. Re-run triggers

A prediction is revisited when: a leading indicator moves outside its forecast interval, corroboration drops, a scenario trigger fires, manipulation is detected after the fact, or the retrospective flags the method as unreliable for that regime.
