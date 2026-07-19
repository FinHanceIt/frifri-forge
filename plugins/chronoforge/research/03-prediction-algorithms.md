# Research Brief 03 — Prediction Algorithms Scan (2023–2025)

> Concrete, implementable forecasting methods for a solo builder's event-prediction system. Star counts are point-in-time, order-of-magnitude. Nothing fabricated.

**Governing finding:** blind competitions and 2025 leakage audits keep reaching one verdict — *simple + combined beats fancy*, a naive/seasonal baseline is hard to beat, and much "AI dominance" is inflated by benchmark contamination. Build the naive floor first; add sophistication only where it earns its place out-of-sample.

---

## 1. Time-series foundation models (pretrained zero-shot)
| Model | What | Repo | ~Stars | License |
|---|---|---|---|---|
| **Amazon Chronos / Bolt** | Tokenizes series, runs a T5 LM; Bolt emits quantiles, much faster | `amazon-science/chronos-forecasting` | ~5.3k | Apache-2.0 |
| **Google TimesFM** | Decoder-only patched model, small but strong | `google-research/timesfm` | ~26k | Apache-2.0 |
| **Nixtla TimeGPT** | First TSFM; API-only **closed model** | `Nixtla/nixtla` (SDK) | ~3.9k | Closed/API |
| **Salesforce Moirai / MoE** | Masked-encoder any-variate universal forecaster | `SalesforceAIResearch/uni2ts` | ~1.5k | Apache-2.0 |
| **IBM Tiny Time Mixers** | MLP-Mixer, ~1M params, CPU inference | `ibm-granite/granite-tsfm` | ~870 | Apache-2.0 |
| **Datadog Toto** | Decoder-only, specialized for observability metrics | `DataDog/toto` | ~470 | Apache-2.0 |

Papers: [Chronos arXiv:2403.07815](https://arxiv.org/abs/2403.07815) · [TimesFM arXiv:2310.10688](https://arxiv.org/abs/2310.10688) · [TimeGPT arXiv:2310.03589](https://arxiv.org/abs/2310.03589) · [Moirai arXiv:2402.02592](https://arxiv.org/abs/2402.02592). Benchmarks: **GIFT-Eval** ([arXiv:2410.10393](https://arxiv.org/abs/2410.10393)), Monash ([forecastingdata.org](https://forecastingdata.org/)), **fev-bench** ([arXiv:2509.26468](https://arxiv.org/abs/2509.26468)).
**Honest maturity:** Nixtla's own arena found TimeGPT/TimesFM beat classical baselines but **Chronos/Moirai/Lag-Llama can be outperformed by classical methods**; leakage inflates reported skill ([arXiv:2510.13654](https://arxiv.org/abs/2510.13654)). Useful for many-series / cold-start; "beats everything zero-shot" is oversold.

## 2. Classical baselines that keep winning
Library: **Nixtla StatsForecast** (`Nixtla/statsforecast`, ~4.8k) — Numba-fast AutoARIMA/AutoETS/AutoTheta/AutoCES/MSTL/TBATS. Methods: ARIMA, ETS (Hyndman state-space), Theta (won M3), TBATS/MSTL (multi-seasonality).
**M-competition lessons:** M4 — winner was an ES-RNN hybrid, #2 FFORMA; **12 of top 17 were combinations; pure ML mostly lost**. M5 — **LightGBM dominated** (equal-weighted 220-model ensemble, Tweedie loss) but *required many correlated series + rich features*. On thin data, ML is dominated by classical at higher cost ([PLOS ONE 2018](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0194889)).
**Non-negotiable:** score in **MASE** — <1 = skill, ≥1 = ship the naive forecast.

## 3. Probabilistic & uncertainty
- **Conformal prediction** — distribution-free finite-sample coverage around *any* model. **MAPIE** (`scikit-learn-contrib/MAPIE`, ~1.4k); CQR ([NeurIPS 2019](https://papers.nips.cc/paper/8613-conformalized-quantile-regression)), EnbPI/ACI for time series. Best theory-to-substance ratio here. ([Angelopoulos & Bates](https://arxiv.org/abs/2107.07511))
- **Quantile regression** via LightGBM/XGBoost pinball loss → intervals directly (conformalize to guarantee coverage).
- **Bayesian structural TS / CausalImpact** — counterfactual "what would have happened" (`WillianFuks/tfcausalimpact`, ~650; `google/tfp-causalimpact`).
- **Prophet** (`facebook/prophet`, ~20k) — easy but often no better than ARIMA/ETS; maintenance-only. Baseline only. **NeuralProphet** is the more active successor.
- **The through-line:** always check calibration — "do my 80% intervals cover 80%?"

## 4. ML forecasters
**Workhorse:** gradient boosting on lag features (XGBoost `dmlc/xgboost` ~28k; LightGBM ~18k) — *won M5*. Use **`mlforecast`** to do it right. Trees can't extrapolate beyond training range → detrend/difference first; don't leak the future.
**Deep learning worth knowing:** N-BEATS ([1905.10437](https://arxiv.org/abs/1905.10437)), **N-HiTS** (long horizons, try first — [2201.12886](https://arxiv.org/abs/2201.12886)), **TFT** (covariates + quantiles — [1912.09363](https://arxiv.org/abs/1912.09363)), DeepAR (probabilistic RNN), PatchTST. **Essential caveat — DLinear** ([2205.13504](https://arxiv.org/abs/2205.13504)): a single linear layer matched a generation of transformers. Always bake off vs DLinear + boosting.
**Libraries:** Nixtla `statsforecast`/`mlforecast`/`neuralforecast`, **Darts** (~9.4k), GluonTS (~5.2k), sktime (~9.8k), PyTorch-Forecasting (~4.9k).

## 5. Discrete-event & point processes — predicting WHEN
- **Hawkes / self-exciting:** `X-DataInitiative/tick` (~550), PyHawkes (latent network), **EasyTPP** neural TPP toolkit (`ant-research/EasyTemporalPointProcess`, ~345), ETAS (`lmizrahi/etas`), SEISMIC (retweet cascade final size, no training).
- **Survival / time-to-event:** **lifelines** (`CamDavidsonPilon/lifelines`, ~2.5k), scikit-survival (~1.3k), pycox (deep survival). Ordinary classification mislabels "hasn't happened *yet*" as "won't"; survival models output a *time distribution*. A hazard function *is* a single-event intensity.

## 6. Judgmental / human + AI forecasting
- **Superforecasting (Tetlock/GJP)** — forecasting is a trainable, measurable skill; GJP beat rivals 35–72%. Portable process: **Fermi-ize → base rate first → update in small increments → aggregate → extremize → keep score (Brier)**. [Good Judgment Open](https://www.gjopen.com/).
- **Markets/Metaculus** — well-calibrated aggregates (Metaculus ~0.11 Brier; Manifold play-money within ~4 pts — *mechanism, not money, drives calibration*). Polymarket/Kalshi: favorite-longshot bias + whale risk.
- **LLMs as forecasters:** Halawi et al. ([2402.18563](https://arxiv.org/abs/2402.18563)) *neared but didn't clearly beat* the crowd (Brier ~0.179 vs ~0.149). "Silicon Crowd" ([2402.19379](https://arxiv.org/abs/2402.19379)) — a 12-LLM ensemble matched a 925-human crowd; showing the LLM the crowd median improved Brier ~17–28%. **Metaculus AI Benchmark**: top human Pros still clearly beat bots. **Critical caveat — temporal leakage**: distrust backtests, trust prospective results ([2506.00723](https://arxiv.org/abs/2506.00723)). Best design = **hybrid** (LLM research + calibrated prior, blended with human crowd).

## 7. Ensembling & meta-learning
Simple combination is the closest thing to a free lunch (Bates-Granger 1969). The **"forecast combination puzzle"**: the simple average often beats optimal weights. **FFORMA** (M4 #2) — XGBoost meta-learner on `tsfeatures` outputs weights over classical forecasters ([PDF](https://robjhyndman.com/papers/fforma.pdf)). Feature libs: `tsfeatures`, catch22. Stacking works with strict out-of-fold discipline; M5's winner used **equal weights**.

## 8. Causal & structure discovery
Causal leading indicators survive regime change; correlated ones break. **CCM** (`SugiharaLab/pyEDM`), **Granger vs Transfer Entropy** (IDTxl, `pwollstadt/IDTxl` ~294), **Tigramite/PCMCI** (`jakobrunge/tigramite`, ~1.7k — leading TS causal-discovery: PCMCI/PCMCI+/LPCMCI), causal-learn (~1.6k), **DoWhy** (~8.1k, refute/falsify step). Assumption-heavy; treat outputs as falsifiable hypotheses.

## 9. Obscure but useful
- **Reservoir computing / NG-RC** — `reservoirpy/reservoirpy` (~640); excellent on chaotic *deterministic* systems, not noisy socio-economic data.
- **Extreme Value Theory** — `georgebv/pyextremes` (~264) for tails/black-swans; data-hungry, threshold choice is an art.
- **LPPL/Sornette** — `Boulder-Investment-Technologies/lppls` (~460); highest-caveat item, unstable fit, mixed OOS record — a bubble-risk *diagnostic*, never a crash-date.
- **Symbolic regression** — **PySR** (`MilesCranmer/PySR`, ~3.6k) discovers equations; **PySINDy** (~1.9k) discovers governing ODEs — interpretable, extrapolates better.
- **ABM / market mechanisms** — Mesa; LMSR (Hanson) behind prediction markets.
- **Event datasets** — GDELT (broad, noisy machine-coded) + ACLED (curated conflict/protest gold standard).
- **Calibration technique** — proper scoring rules: **Brier** (decomposes into calibration/resolution/uncertainty) + **log score** (punishes confident errors, Metaculus's choice). **Extremizing** ([Baron et al. 2014](https://pubsonline.informs.org/doi/10.1287/deca.2014.0293)) helps *diverse* crowds, not already-calibrated superforecasters.

---

## Prioritized shortlist — 15 highest-leverage components
1. **StatsForecast baseline battery in MASE** — the non-negotiable floor.
2. **mlforecast + LightGBM (lag/rolling/calendar features)** — pragmatic default; won M5.
3. **Simple equal-weight combination** — closest thing to a free lunch.
4. **Conformal prediction (MAPIE, CQR + EnbPI)** — distribution-free coverage around any model.
5. **Quantile regression (pinball loss)** — intervals directly; pairs with conformal.
6. **A TSFM fallback (TimesFM or Chronos-Bolt)** — cold-start / many-series.
7. **Proper scoring + calibration checks (Brier, log score, coverage)** — the discipline.
8. **Extremizing the aggregate** — cheap boost for diverse/LLM crowds.
9. **Survival analysis (lifelines → scikit-survival)** — "when will X happen" with censoring.
10. **Hawkes / point processes (tick; EasyTPP)** — self-exciting events.
11. **LLM-as-forecaster hybrid (retrieval + ensemble + show crowd median)** — guard leakage.
12. **Human/crowd anchor (Metaculus/Manifold)** — calibrated aggregate to blend/sanity-check.
13. **Tigramite/PCMCI** — causal leading-indicator discovery that survives regime change.
14. **CausalImpact** — "what did this event do" counterfactuals.
15. **EVT (pyextremes) + PySINDy/PySR** — tail risk + interpretable discovered dynamics.

**Overhyped / hard to operationalize (flagged honestly):** TSFM "zero-shot beats everything" (leakage-inflated); Prophet (baseline only); LPPL crash-dates (hindsight-prone); "superhuman AI forecasting" (assume leakage until prospective proof); transformer forecasters as default (bake off vs DLinear); BMA & causal discovery (assumption-heavy → hypotheses, not answers).

**Meta-lesson:** build the naive floor, beat it with boosting-on-features + simple combination, wrap everything in conformal intervals + proper-scoring calibration, add causal discovery and human/LLM crowds as edge — and distrust anything whose track record lives only in a backtest.
