# ChronoForge Methodology — Esoteric-Seeded, Science-Locked Forecasting (ESL)

**The canonical spec. Every agent obeys this file. Project rules here win over general preferences.**

ChronoForge predicts future events by forward inference only. It admits esoteric and lateral frameworks as **hypothesis generators**, forces each into a **measurable present-signal proxy**, locks every proxy against physics, forecasts with a calibrated ensemble, and keeps a **rolling Brier score per lens** so that fringe framings earn weight or die. Belief is never an input; falsification is the judge.

---

## 0. The three laws (non-negotiable)

1. **Forward inference only.** No channel from the future exists (no tachyon, no entanglement signal, no precognition). Every "signal from the future" framing must be re-expressed as a *present-or-past* measurable proxy, or it is discarded. See `science-charter.md`.
2. **Nothing is believed; everything is scored.** No lens, esoteric or conventional, carries authority. A lens influences a forecast only in proportion to its rolling out-of-sample Brier skill vs baseline (the Lens Ledger, §6). A lens below baseline is demoted, then killed.
3. **No fabrication, ever.** No invented data, sources, numbers, backtests, or track records. Unknown = "unknown." Assumed is labeled assumed. A backtest is never reported as a live track record.

---

## 1. Pipeline (the DAG)

```
FRAME → DIVERGE (lenses) → OPERATIONALIZE (gate) → REALITY-LOCK (science council)
      → GATHER & TRIANGULATE → FORECAST (ensemble) → CALIBRATE & FALSIFY (gate)
      → SCORE LENSES (ledger) → SYNTHESIZE → REMEMBER
```

Three hard gates stop the flow: **Operationalization** (a hypothesis without a measurable proxy dies), **Reality-lock** (a physically impossible proxy dies), **Calibrate & Falsify** (a forecast that can't beat baseline or shows leakage is REJECTED/RE-RUN).

Two human checkpoints: **after FRAME** (confirm the question + resolution criteria) and **before SYNTHESIZE ships an actionable call** (Fri sees the forecast, intervals, and confidence before acting).

---

## 2. Stage contracts

**FRAME** — `question-framer`. Turn a vague ask into a testable target: exact event statement, **resolution criteria** (how we'll know if it happened), **horizon** (with the Lyapunov/entropy caveat if chaotic), granularity, decision context, acceptable error, reference class. Output: `TargetSpec`.

**DIVERGE** — the lens agents (`lens-transurfing`, `lens-quantum-shift`, `lens-oracle-divination`, `lens-conventional`). Each reads `TargetSpec` and emits candidate **hypotheses** about drivers/signals — quantity over judgment. Every hypothesis is tagged with its originating lens. Esoteric lenses must output in the [CLAIM]→[REFRAME] form from `lens-catalog.md`; they never assert the metaphysics as true. Output: `HypothesisPool`.

**OPERATIONALIZE (gate)** — `operationalizer`. For each hypothesis: name a **measurable present-signal proxy**, a **data source**, a **direction/magnitude prediction**, and a **falsification test** (what would prove it useless). No proxy or no source → **KILL**. Output: `SignalSpec[]` (only survivors) + a kill log.

**REALITY-LOCK (gate)** — the `science-council` (`physics-gate`, `math-complexity-scientist`, `bio-cognition-scientist`, `chemistry-criticality-scientist`, `economics-reflexivity-scientist`, `social-network-scientist`). Kill any proxy that violates the charter (backward causation, past-horizon point forecasting, no-signaling) **or that has no real mechanism in its domain** (a "tipping point" with no order parameter, a market "signal" with no surviving edge, a "cascade" that misreads simple vs complex contagion). For survivors, assign the **correct formal method** by signal shape (EVT for tails, Hawkes for self-exciting, CCM for nonlinear causality, EWS for criticality, GSADF for bubbles, threshold models for complex contagion, etc. — see `science-charter.md §2`). Output: annotated `SignalSpec[]` with method assignments.

**INVENT (optional)** — the inventors' think-tank, coordinated by `invention-lead` routing `mechanism-inventor` (compose from pipeline parts), `analogy-transfer-inventor` (import a mechanism from another domain), and `combinatorial-inventor` (cross/fork surviving proxies). Every invention is specified as a full `SignalSpec` and **re-enters OPERATIONALIZE → REALITY-LOCK** like any hypothesis; it starts on PROBATION with a fresh ledger row. Output: ≤3–5 candidate predictors (or an honest empty set).

**GATHER & TRIANGULATE** — `signal-scout` (inventory + fetch, Tier A/B/C) then `osint-triangulator` (Admiralty grade × credibility, **independence clustering** to defeat correlation-laundering, manipulation discount → tier CONFIRMED / PROBABLE / SINGLE-SOURCE / CONTESTED). Only CONFIRMED/PROBABLE signals feed forecasting. Output: `Evidence[]` with tiers.

**FORECAST** — `baseline-forecaster` then `ensemble-forecaster` (+ `event-modeler` for discrete events, `specialist-forecaster` for tails/self-exciting/chaos/time-to-event). Rules:
- Always fit the **naive/seasonal baseline first**; the ensemble must beat it in **MASE** or the naive forecast ships.
- Discrete "will X happen by T?" → Bayesian `event-modeler` (prior from reference class, capped per-source log-LR updates, Monte-Carlo intervals).
- Continuous trajectory → statistical/boosting/TSFM blend; **mandatory 80% & 95% prediction intervals** (conformal or quantile).
- Combine by simple/skill-weighted averaging (combination beats sophistication).
Output: `Forecast` (point + intervals + method trail).

**CALIBRATE & FALSIFY (gate)** — `calibration-validator`. Walk-forward backtest; **Brier/log-score vs baseline**; interval **coverage check** (80% covers ~75–85%, 95% ~90–97%); **leakage audit** (no future info in features; distrust any suspiciously good backtest). Verdict **ACCEPT / ACCEPT-WITH-CAVEATS / RE-RUN / REJECT**. Nothing ships without ACCEPT (or disclosed first-run). Output: `Validation`.

**SCORE LENSES (ledger)** — `lens-ledger-keeper`. Attribute the forecast's eventual outcome back to the contributing lenses/signals and update their rolling Brier (§6). Output: updated `LensLedger`.

**SYNTHESIZE** — `synthesis-reporter`. One deliverable: probability + 80/95% intervals + timing window + evidence chain + contributing lenses (with their current ledger weight) + honest confidence + top-3 caveats + re-run triggers. Adversarial pass by `premortem-adversary` first.

**REMEMBER** — `lens-ledger-keeper` persists the prediction, its resolution date, and the lens attribution for the learning loop.

---

## 3. The lens system

A **lens** is a framing that generates hypotheses. Lenses are peers; none has authority. Two families:

- **Esoteric lenses** (Transurfing, quantum-shift, divination) — high-divergence hypothesis generators. They exist because unusual framings sometimes surface drivers conventional models miss. They are *always on probation* (§6) and contribute only their ledger-earned weight.
- **Conventional lenses** (historical analogy, contrarian/positioning, leading-indicator, convergence) — the reliable core.

Every hypothesis is stamped with its lens so the ledger can attribute credit/blame. The full operational catalog — each lens's [CLAIM]→[REFRAME]→proxy→source→falsification-test — lives in `lens-catalog.md`.

**Divination lens special rule:** it is used *only* as a random-constraint hypothesis-seed generator (Oblique-Strategies-style forced reframes), never as a signal. Its seeds enter the same OPERATIONALIZE gate as any other hypothesis and are kept only if they raise candidate coverage without hurting calibration.

---

## 4. Inheritance (do not rebuild)

Reuse, don't reinvent:
- **Project Oracle** (`predictive-agents` plugin): triangulation (Admiralty + independence), `event_model.forecast_event` (Bayesian P with capped updates + MC intervals), calibration (Brier/EV/Kelly), `validators.walk_forward`/`coverage_check`/`beats_naive`. ChronoForge's triangulator, event-modeler, and validator are thin wrappers over these.
- **TrendForge** (`trendforge` plugin): `emergence-predictor`, `lead-lag-correlator`, `leading-indicator-chain-forecaster` for the early-signal layer; shared tier vocabulary.

ChronoForge's **delta** is the front-end (lenses + operationalization + science-lock) and the **Lens Ledger**. That is the invention; the back-end is proven machinery.

---

## 5. Scoring & confidence

Final confidence is a product of independently-degradable factors (0–1 each), never inflated:

```
confidence = source_reliability × independent_corroboration × (1 − manipulation)
           × model_agreement × backtested_skill × calibration_quality
           × (1 − premortem_fragility) × lens_ledger_trust
```

`lens_ledger_trust` is the weighted average ledger skill of the lenses that contributed the decisive signals. A forecast resting mainly on an unproven esoteric lens is automatically low-confidence until that lens earns its ledger. Full schema in `scorecard.md`.

---

## 6. The Lens Ledger (the signature mechanism)

The ledger is what makes "using Transurfing for prediction" honest instead of delusional. Each lens (and each recurring signal type) has a persistent record:

```
lens_id | n_predictions | rolling_Brier | baseline_Brier | skill = baseline_Brier − rolling_Brier
        | last_updated | status ∈ {PROBATION, EARNING, TRUSTED, DEMOTED, KILLED}
```

**Update rule.** When a prediction resolves, each contributing lens's Brier is updated (exponentially-weighted, half-life ~ the last N resolved predictions). `skill > 0` means the lens beats the baseline.

**Weighting rule.** A lens's influence on future forecasts = `max(0, skill)` normalized across contributing lenses. **A lens with skill ≤ 0 contributes nothing** — its hypotheses are still generated (for coverage) but carry zero forecast weight until they resolve well.

**Status transitions.**
- New esoteric lens → **PROBATION** (weight 0, hypotheses logged, outcomes tracked).
- Beats baseline over a minimum sample (≥ ~20 resolved) → **EARNING** → **TRUSTED**.
- Falls below baseline over a rolling window → **DEMOTED**; sustained → **KILLED** (archived, not deleted — the null result is data).

**Anti-gaming.** Lens skill is measured only on **resolved, pre-registered** predictions (registered before the outcome, per the parapsychology-methodology steal). No retrospective credit. A lens cannot claim a signal it didn't stamp at DIVERGE time.

This is the closed loop: Transurfing, quantum-shift, and every conventional lens live or die by the same Brier ledger. If the Transurfing lens genuinely surfaces useful attention/reflexivity signals, it will earn weight and you'll have proven it honestly. If it doesn't, the ledger kills it and you've lost nothing but noise.

---

## 7. Honesty boundary

ChronoForge never claims to see the future, never reports a backtest as a live record, never assigns a probability it can't defend from evidence, and always states its predictability horizon. When a question is past the Lyapunov/entropy wall, it says so and forecasts only distributions. When the esoteric lenses have no ledger yet, it says the confidence is low *because* they're unproven. The system's credibility is its only asset — it is protected above all.
