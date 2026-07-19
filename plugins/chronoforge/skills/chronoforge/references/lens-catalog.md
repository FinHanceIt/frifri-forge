# ChronoForge Lens Catalog

The operational catalog for every lens. Each entry: the framing's **[CLAIM]** (what proponents say — never asserted as true), the **[REFRAME]** (the measurable phenomenon it points at), the **PROXY** (what to measure), the **SOURCE** (where the data lives), and the **FALSIFICATION TEST** (what result kills this signal). Lens agents emit hypotheses in this form; the `operationalizer` enforces that PROXY + SOURCE exist or the hypothesis dies.

Every proxy below has independent backing — peer-reviewed where noted, established-practitioner (e.g. funding-rate/positioning reversals) elsewhere (see `research/01-esoteric-corpus.md`). The esoteric label is only the *hypothesis source*, not the justification.

---

## LENS A — Transurfing (reflexivity / attention / positioning)

**A1 · Pendulums → attention cascades / herding**
- [CLAIM] A collective thought-structure feeds on attention and grows.
- [REFRAME] Information cascade / herding (Bikhchandani-Hirshleifer-Welch 1992).
- PROXY: social-volume z-score; Google-Trends / Wikipedia-pageview spike ratio; engagement-percentile virality threshold; mention-velocity.
- SOURCE: Google Trends (pytrends), Wikipedia pageviews API, Reddit/X volume, GDELT.
- FALSIFICATION: cascade-detector's continuation/reversal calls do not beat naive persistence on a labeled set → drop.

**A2 · Excess potential → crowd over-commitment at extremes**
- [CLAIM] Inflated importance summons equalizing forces that deflate it.
- [REFRAME] Positioning extremes mean-revert (contrarian).
- PROXY: perpetual **funding rates**, open interest, short interest, positioning surveys at percentile extremes.
- SOURCE: exchange funding-rate APIs (CoinGecko/Coinglass-style), COT reports, put/call feeds.
- FALSIFICATION: extreme positioning gives no elevated reversal probability vs the unconditional base rate → drop.

**A3 · Importance → reflexivity / sentiment overreaction**
- [CLAIM] Over-valuing an outcome (with fear) manifests the feared result.
- [REFRAME] Soros reflexivity; sentiment overreaction and mean-reversion.
- PROXY: put/call ratio, fear/greed index, VIX spikes, social-sentiment extremes.
- SOURCE: options data, sentiment indices, social APIs.
- FALSIFICATION: fading sentiment extremes does not beat buy-and-hold risk-adjusted out-of-sample → treat as *conditioner only*, not a timing trigger (extremes can persist).

**A4 · Space of variations → probabilistic state-space (posture, not a signal)**
- [CLAIM] Realities pre-exist; you select a "sector."
- [REFRAME] The future is a distribution over paths; forecasting = assign/update probabilities.
- PROXY: prediction intervals, scenario weights, prediction-market-implied probabilities.
- SOURCE: Metaculus/Polymarket/Manifold; the model's own ensemble.
- USE: enforces the modeling posture (never a point forecast without a distribution). Not ledger-scored as a signal.

**A5 · Outer/inner intention → forceable vs timing-only (posture + lead-lag)**
- [CLAIM] "Outer intention" makes the goal realize itself.
- [REFRAME] Separate levers you control (inner) from environmental state you can only time (outer); ride upstream signals.
- PROXY: tag every signal forceable vs timing-only; use validated **lead-lag indicators** so the downstream "arrives by itself."
- SOURCE: the lead-lag map (inherited from TrendForge `lead-lag-correlator`).
- FALSIFICATION: acting on the leader does not beat acting on the follower out-of-sample → the lead-lag link is spurious, drop.

**A6 · Slides / visualization → expectation & self-fulfilling loops**
- [CLAIM] Visualizing the outcome materializes it.
- [REFRAME] Shared expectations become self-fulfilling (expected recession/bank-run).
- PROXY: expectation indices (consumer confidence, PMI-expectations), analyst-consensus revisions, market-implied probabilities.
- SOURCE: FRED, survey indices, consensus data.
- FALSIFICATION: expectation shifts do not lead outcome shifts (Granger/CCM) and don't cut forecast error vs fundamentals-only → drop.

---

## LENS B — Quantum-shift (attention / identity / expectancy)

**Hard prior:** P(physical branch-jump / inter-universe transfer) ≈ 0. This lens models the *person*, never the physics.

**B1 · Quantum jumping / reality shifting → identity priming & expectancy**
- [CLAIM] Visualize an alternate self and "download" their reality.
- [REFRAME] Absorption, expectancy/placebo, identity-priming behavior change (Somer 2021; Tellegen absorption).
- PROXY: for human-behavior forecasts — absorption (TAS), maladaptive-daydreaming severity (MDS-16, ≥40 clinical), expectancy, pre/post self-efficacy; measurable behavior change.
- SOURCE: survey instruments, behavioral logs (only where ethically available and relevant).
- FALSIFICATION: identity priming produces no measurable behavior change vs control → drop. (Physical-jump claims are auto-killed by `physics-gate`.)

**B2 · Collective "reality shift" → coordinated behavior / expectation contagion**
- [REFRAME] Large synchronized expectation shifts in a population (a legitimate reframe of "mass reality shifting").
- PROXY: synchronized search/sentiment/behavior surges across independent communities.
- SOURCE: cross-platform social + search.
- FALSIFICATION: synchronized expectation surges don't lead the target outcome → drop.

---

## LENS C — Oracle / divination (random-constraint ideation ONLY)

**Hard rule:** zero predictive validity. Used *only* to widen the hypothesis set via forced novel framings. Its seeds go through OPERATIONALIZE like any other and are kept only if they raise coverage without hurting calibration.

**C1 · Tarot / I Ching / synchronicity / astrology → random-constraint reframes**
- [CLAIM] Symbols reveal the future.
- [REFRAME] Ambiguous random stimulus → breaks functional fixedness → novel hypotheses (Oblique Strategies, de Bono Random Input; Semetsky projective technique).
- MECHANISM: sample a random constraint / reframe-verb (invert, remove, exaggerate, cross-domain-analogize, "what if the opposite driver") to force extra hypotheses the conventional lenses missed.
- FALSIFICATION (A/B): seeded hypotheses do not raise candidate-set diversity/coverage, OR calibration (Brier) with seeds injected falls below baseline → stop using seeds. Never let a seed skip the evidence gate.

---

## LENS D — Conventional (the reliable core)

**D1 · Historical analogy** — match the target to past cases with known outcomes; report base rates. SOURCE: case libraries, domain history. FALSIFICATION: analogies don't beat the reference-class base rate.

**D2 · Contrarian / positioning** — fade crowded extremes (overlaps A2/A3 with stricter stats). FALSIFICATION: no reversal edge vs base rate.

**D3 · Leading-indicator** — act on validated upstream signals (inherited lead-lag map). FALSIFICATION: leader has no out-of-sample predictive lag over follower.

**D4 · Convergence** — where two trends merge (least-crowded, biggest opportunities). FALSIFICATION: convergence doesn't precede the target shift.

---

## How the ledger treats these

Lenses A, B, D each get a ledger row (PROBATION → EARNING → TRUSTED / DEMOTED / KILLED per `methodology.md §6`). Lens C is measured differently — by whether its seeds improve coverage without hurting Brier (an A/B metric, not a per-signal Brier). Postures A4/A5 are enforced as rules, not scored as signals. Nothing here is believed; the ledger decides what survives.
