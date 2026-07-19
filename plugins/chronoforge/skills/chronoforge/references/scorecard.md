# ChronoForge Scorecard — Confidence, Tiers, and the Lens Ledger

Canonical scoring for the whole system. No number here may be fabricated; every factor must trace to real evidence or a real backtest.

---

## 1. Evidence tiers (shared with Project Oracle & TrendForge)

After triangulation, each signal is one of:
- **CONFIRMED** — score ≥ 0.65, ≥2 independent A/B sources, no A/B contradiction. Feeds forecasting.
- **PROBABLE** — score ≥ 0.35. Feeds forecasting with wider intervals.
- **SINGLE-SOURCE** — quarantined; cannot drive a forecast alone.
- **CONTESTED** — A/B-grade contradiction; escalates to human.

Triangulation score (from Oracle's method): `raw = sqrt(n_distinct_supporting_families) × Σ(independent_group_weights) − Σ(contradiction_weights)`, squashed via `tanh` to [0,1], recency-decayed (half-life ~7 days). Independence clustering by `(source, origin)` collapses echoed wires to one vote (defeats correlation-laundering). Manipulation-family evidence discounts narrative weight.

---

## 2. Confidence formula

Final confidence is a product of independently-degradable factors, each in [0,1]. Any weak factor drags the whole call down — by design.

```
confidence = source_reliability
           × independent_corroboration
           × (1 − manipulation)
           × model_agreement          (ensemble members agree?)
           × backtested_skill          (Brier improvement vs baseline, normalized)
           × calibration_quality       (do 80% intervals cover ~80%?)
           × (1 − premortem_fragility)  (how easily the adversary broke it)
           × lens_ledger_trust          (weighted ledger skill of the decisive lenses)
```

Report confidence as a band, never a false-precise number, and always name the **weakest factor** (it's the thing to fix). A forecast leaning on a PROBATION lens is low-confidence *because* the lens is unproven — state that plainly.

---

## 3. The Lens Ledger schema

Persistent, one row per lens (and per recurring signal type). This is the learning loop and the honesty engine.

```
lens_id            e.g. "lens-transurfing:A1-attention-cascade"
n_predictions      resolved, pre-registered predictions this lens contributed to
rolling_Brier      EW Brier over resolved predictions (half-life ≈ last 20)
baseline_Brier     the naive/base-rate baseline's Brier on the same items
skill              baseline_Brier − rolling_Brier      (>0 = beats baseline)
last_updated       ISO date
status             PROBATION | EARNING | TRUSTED | DEMOTED | KILLED
```

**Brier score** = mean((p − outcome)²), outcome ∈ {0,1}, lower is better. Log score also tracked (punishes confident errors harder — Metaculus's rule).

**Weighting rule:** future forecast weight = `max(0, skill)` normalized across contributing lenses. `skill ≤ 0` → **zero weight** (hypotheses still generated for coverage, but they don't move the number).

**Status machine:**
- New esoteric lens → **PROBATION** (weight 0; log hypotheses + outcomes).
- `skill > 0` over ≥ ~20 resolved, pre-registered predictions → **EARNING** → sustained → **TRUSTED**.
- `skill ≤ 0` over a rolling window → **DEMOTED**; sustained → **KILLED** (archived; the null result is kept as data).

**Anti-gaming (the parapsychology steal):** credit counts only for predictions the lens **stamped at DIVERGE time, before resolution** (pre-registration). No retrospective attribution. No lens may claim a signal it didn't originate.

---

## 4. Forecast acceptance gate (before anything ships)

ALL must hold (from `calibration-validator`):
- Beats the naive/seasonal baseline on the primary metric (MASE < 1 for trajectories; Brier < base-rate for events).
- 80% interval coverage ∈ [75%, 85%]; 95% ∈ [90%, 97%].
- No leakage (every lag strictly past; scaler fit on train only; backtest not suspiciously perfect).
- Recent-window performance not > 2× worse than overall (regime stability).
Verdict: **ACCEPT / ACCEPT-WITH-CAVEATS / RE-RUN / REJECT**. Overconfident intervals → widen (conformal/quantile recalibration) and re-run.

---

## 5. Deliverable contract (what SYNTHESIZE must contain)

1. **The call** — probability (for events) or trajectory + **80% & 95% intervals**.
2. **Timing window** — entry / expected peak / decline, or event date range.
3. **Predictability horizon** — with Lyapunov/entropy caveat if chaotic.
4. **Evidence chain** — the decisive signals, their tiers, their sources.
5. **Contributing lenses** — each with its current ledger status/weight (so Fri sees whether an esoteric lens actually earned its place).
6. **Confidence band** + the weakest factor.
7. **Top-3 caveats** + **re-run triggers** (what new data would change the call).
8. **Honesty line** — what the system is *not* claiming.
