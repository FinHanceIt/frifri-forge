# ChronoForge Science Charter & Method-Selection Guide

The reality-lock. The science council — `physics-gate`, `math-complexity-scientist`, `bio-cognition-scientist`, `chemistry-criticality-scientist`, `economics-reflexivity-scientist`, `social-network-scientist` — enforces §1 and assigns §2. Full backing in `research/02-physics-reality-gate.md` and `research/04-domain-arsenals-and-2026-scan.md`.

---

## 1. The physics-honest charter (8 laws)

1. **Forward inference only.** No channel from the future — no tachyon, no entanglement signal, no precognition. Any prediction is present-and-past evidence propagated forward through a model.
2. **Operationalize every "backward-in-time" framing as a present-signal proxy.** Weak values, "the future constrains the present," retrocausal talk → must become *what measurable current/past feature stands in for this?* If it can't, it's not usable — KILL.
3. **Respect the predictability horizon.** For chaotic systems estimate the largest Lyapunov exponent; point forecasts are void beyond a few Lyapunov times. Past the wall, forecast only distributions/attractor statistics. Never pretend to see through it.
4. **Tails need EVT, not Gaussians.** Model extremes with Extreme Value Theory (GPD/POT) and power laws. Fat tails by default; a normal distribution for rare events is a bug.
5. **Self-exciting events need point processes** (Hawkes/ETAS conditional intensity), not smooth trend-fitting.
6. **Causation, not correlation, feeds the model.** CCM / delay-embedding (Granger where linear) to select drivers; flag correlational drivers as fragile (they break at regime change).
7. **Carry an explicit generative model + prediction-error loop.** Predict → measure surprise → update. Surprise is the learning signal and the anomaly alarm.
8. **Ship calibrated uncertainty and backtested, honest track records — never certainty.** EWS, LPPL, cliodynamics are probabilistic alarms over horizons; label them so. Distrust any track record that lives only in a backtest (temporal leakage).

**Auto-kill list** (the council rejects on sight): usable tachyonic/FTL signaling · intention-based branch selection · precognition channels · entanglement as a comms line · any point forecast past the Lyapunov horizon · any Gaussian tail model for a fat-tailed process.

**Cite-for-honesty-but-no-channel** (real but interpretational): Two-State Vector Formalism, weak values, Wheeler-Feynman absorber, Transactional Interpretation, Price/Wharton retrocausal, Leggett-Garg tests. Weak values are a lab tool, not an oracle.

---

## 2. Method-selection guide (signal shape → formal tool)

The council assigns the right machinery to each surviving proxy. Pick by the data's shape, not by fashion.

| Signal / target shape | Correct method | Library | Note |
|---|---|---|---|
| Stationary series, autocorrelation/seasonality | ARIMA/SARIMAX, ETS, Theta | StatsForecast | The baseline that must be beaten |
| Many related series + rich features | Gradient boosting on lag features | mlforecast + LightGBM | Won M5; detrend first (trees don't extrapolate) |
| Cold-start / no time to model | TSFM zero-shot | TimesFM, Chronos-Bolt | Fallback only; benchmark vs baseline |
| Long horizon, strong seasonality | N-HiTS, TFT | neuralforecast | Bake off vs DLinear first |
| Discrete "will X happen by T?" | Bayesian event model | Oracle `event_model` | Prior from reference class; capped per-source updates |
| Any point forecast | Wrap in conformal / quantile intervals | MAPIE, LightGBM pinball | Mandatory 80% & 95% coverage |
| Tail / black-swan / "how bad can it get" | Extreme Value Theory (GPD/POT) | pyextremes | Never a Gaussian |
| Self-exciting (virality, cascades, defaults, quakes) | Hawkes / ETAS / neural TPP | tick, EasyTPP | Conditional intensity, not a curve |
| "When will X happen" with censoring | Survival analysis | lifelines, scikit-survival | Time distribution, not yes/no |
| Chaotic deterministic system | Reservoir computing / NG-RC | reservoirpy | Bounded by Lyapunov time |
| Nonlinear causality between series | Convergent Cross Mapping | pyEDM | Convergence check; not bare correlation |
| Approaching a tipping point | Early-warning signals (variance + AR1 trend) | ewstools | Probabilistic alarm, report false-alarm rate |
| Multivariate causal discovery (autocorrelated) | PCMCI / PCMCI+ / LPCMCI | tigramite | Outputs = hypotheses to validate |
| "What did this event do" (counterfactual) | Bayesian structural TS | CausalImpact | Needs clean control series |
| Combine several forecasters | Simple/skill-weighted average, FFORMA | — | Combination beats sophistication |
| Bubble / super-exponential regime | LPPL diagnostic | lppls | Risk *window*, never a dated crash |
| Explosive asset-price regime (bubble date-stamp) | GSADF / PSY explosive-root test | exuber, psymonitor (R) | Alarm window, never a crash date |
| Market-implied event probability | Odds / prediction-market / option-implied prior | Metaculus, Manifold | State favorite-longshot bias |
| Simple contagion (information spread) | SIR / branching / Hawkes | NDlib, tick | One contact suffices |
| Complex contagion (norms, behavior) | Threshold model (Granovetter / linear-threshold) | NDlib, networkx | Needs reinforcement; wide bridges beat weak ties |
| Committed-minority / social tipping | Critical-mass threshold (~25%, context-dependent) | NDlib | Centola 2018; never a universal constant |
| Self-organized criticality / avalanche sizes | Power-law sizing + EVT | pyextremes | Scale-free size = unpredictable magnitude |

---

## 3. Council review output

For each proxy the council returns: **VERDICT** (PASS / KILL-with-reason), **assigned method** (from §2), **predictability horizon** (with Lyapunov/entropy note if relevant), and **fragility flags** (correlational driver? thin-tail assumption? leakage risk?). KILLED proxies are logged with the charter law they violated. Nothing reaches forecasting without a PASS + an assigned method.
