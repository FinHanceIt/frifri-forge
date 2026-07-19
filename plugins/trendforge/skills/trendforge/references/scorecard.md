# TrendForge — Scoring Rubrics

## A. Trend ranking composite (`trend-ranker`)

Each graduated trend scores 0–100 on a transparent weighted sum. Default weights (tune per mission):

| Axis | Weight | What it rewards | Owner agent |
|---|---|---|---|
| Momentum & acceleration | 20% | fast, accelerating growth | momentum / acceleration analysts |
| Durability (not a fad) | 15% | sustained, broad adoption | fad-vs-trend-classifier |
| Corroboration & reliability | 15% | many independent, trustworthy sources | cross-source-corroborator |
| Headroom (low saturation) | 10% | room left to grow | saturation-tam-estimator |
| Capital + attention alignment | 15% | money, talent and eyeballs moving together | capital-attention-flow-mapper |
| Timing (lifecycle sweet-spot) | 10% | early enough to act | lifecycle-scurve-stager |
| Low crowdedness | 5% | not already a red ocean | competitive-density-mapper |
| Confidence | 10% | how sure we are | confidence-scorer |

Crowded, saturated, fad-like and low-confidence trends are penalized; early + durable + aligned + corroborated trends rise. Always show sub-scores, never just the total. Output: overall ranking, per-domain views, and an **emerging watchlist** (high potential, lower confidence, kept separate).

## B. Confidence score (`confidence-scorer`)

0–100 from: source reliability, independent corroboration count, manipulation discount, model agreement (ensemble), backtested accuracy for that regime, calibration quality, and a fragility penalty from the premortem. Reported with its top drivers and "what would raise it".

## C. Opportunity score (`opportunity-mapper` / `whitespace-finder`)

For converting a trend into something buildable:

| Axis | Rewards |
|---|---|
| Pain intensity × frequency | a real, recurring job-to-be-done |
| Whitespace | demand with weak/missing existing solutions |
| Timing (why now) | the trend's entry window is open |
| Monetization clarity | a believable way to get paid (domain lens) |
| Feasibility for a small team | buildable without heroics |
| Defensibility | a wedge that is not instantly copyable |

Each opportunity ships with its **riskiest assumption** named.

## D. Confidence tiers (corroboration)

`CONFIRMED` (multiple independent source-types, high reliability) · `PROBABLE` (some independent support) · `SINGLE-SOURCE` (watchlist only) · `CONTESTED` (sources disagree). Only CONFIRMED/PROBABLE trends are forecast for delivery; the rest stay on the watchlist.
