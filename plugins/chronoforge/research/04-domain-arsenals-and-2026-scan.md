# Research Brief 04 — Domain Method-Arsenals + 2026 / Fringe Scan

> Extends `03-prediction-algorithms.md`. Arms the three new reality-lock seats (chemistry-criticality, economics-reflexivity, social-network) with cited domain machinery, and adds the current (2026) + fringe sweep Fri asked for. Star counts / dates are point-in-time and order-of-magnitude. Nothing fabricated; where a tool is R-only or a result is a single study, it says so.

---

## 1. Chemistry & criticality → `chemistry-criticality-scientist`

The honest core: a "tipping point" is real only if there is an **order parameter** and a **control parameter**, with the system near a bifurcation. Then generic early-warning signals appear.

- **Early-warning signals (EWS) / critical slowing down** — near a fold bifurcation, recovery from perturbation slows, so **variance and lag-1 autocorrelation rise** (also skewness, flickering). Canonical review: **Scheffer et al., *Nature* 2009**. Tooling: **`ThomasMBury/ewstools`** (Python — variance, AR1, DFA, plus ML detectors). Honest caveat: EWS have real **false-positive / false-negative rates**, are confounded by changing noise, and warn *that*, not *when*.
- **Percolation / nucleation** — change propagates once a connected cluster crosses the **percolation threshold p_c**; the proxy is connectivity/coverage vs p_c, not raw counts. Nucleation: a metastable state flips once a critical nucleus forms.
- **Self-organized criticality (SOC)** — Bak–Tang–Wiesenfeld (1987): systems that self-tune to criticality emit **power-law avalanche sizes** → magnitude is intrinsically unpredictable; size with power-law/EVT, never Gaussian, never a dated event.
- **Autocatalysis / reaction kinetics** — self-reinforcing processes show super-linear kinetics (gain > 1); the chemistry analogue of reflexive/viral feedback. Separate true positive feedback from mere exponential fashion.
- **Catastrophe theory (cusp)** — Thom/Zeeman: discontinuous jumps from smooth control changes; a useful *qualitative* map (hysteresis, bimodality), abused when fit to noisy data — treat as a lens, not a fitter.

## 2. Economics, markets & reflexivity → `economics-reflexivity-scientist`

- **Efficient-market null** — in a liquid market a "signal" must name a surviving **edge** (informational, structural, behavioral) or it is already priced. This gate kills most mystical market claims.
- **Reflexivity (Soros)** — expectations → actions → outcomes → new expectations. The operationalizable kernel behind Transurfing's "expectation" claim: build an **expectation index** (survey, positioning, implied volatility, search interest), predict the action, measure the loop.
- **Market-implied probabilities** — odds and prediction markets as calibrated priors: **Metaculus ≈ 0.11 Brier**, Manifold play-money close behind; **Polymarket/Kalshi** carry favorite-longshot bias + whale / thin-market risk. Option-implied densities where available.
- **Explosive-root bubble econometrics** — **GSADF / PSY** (Phillips–Shi–Yu) right-tailed recursive unit-root tests **date-stamp** explosive price regimes in real time. Review: **Hu, *J. Economic Surveys* 2023**. Tooling: **`exuber`** (R, CRAN), **`psymonitor`** (R — Caspi, real-time monitoring), **`deanfantazzini/bubble`** (R); Python **BSADF** implementations exist but are less mature. Pair with **LPPL** (brief 03) as a *risk window*, never a crash date.
- **Agent-based markets** — Mesa; LMSR (Hanson) is the market-maker behind prediction markets.

Honest caveat: educational, **not financial advice**; a backtested edge is not a live one; ChronoForge never places trades.

## 3. Social dynamics & networks → `social-network-scientist`

The rigorous home for the "attention cascade" the esoteric lenses gesture at.

- **Simple vs complex contagion** — information spreads on a single contact (**simple → SIR/branching, Hawkes**); norms/behaviors often need **reinforcement from multiple sources** (**complex → threshold models**), where **wide bridges** beat long weak ties. Misclassifying the two is the top modeling error.
- **Thresholds & critical mass** — Granovetter threshold model; **committed-minority tipping ≈ 25%** in **Centola et al., *Science* 2018** — real and striking, but **context-dependent; never quote 25% as a universal constant**.
- **Cascade dynamics & final size** — **Hawkes / SEISMIC** for retweet/adoption cascades (final-size estimate without training); epidemic **reproduction number R** for attention.
- **Network structure** — hubs, brokers/bridges (weak ties, Granovetter), **k-core**, community boundaries; *who* is seeded usually beats *how many*.
- Tooling: **NDlib** (Rossetti et al.; 11 epidemic + 5 opinion-dynamics + dynamic-network models; arXiv:1801.05854), **networkx**, **`tick` / `EasyTPP`** (point processes).

Honest caveat: coordinate with `osint-triangulator` to discount **bots / astroturf**; the famous constants (25%, R) are context-dependent, not laws.

## 4. Current & fringe scan — the 2026 LLM-forecasting frontier

Fri asked for GitHub + obscure/current. The live edge in event forecasting is **LLM agents scored against humans**:

- **Metaculus `forecasting-tools`** (`github.com/Metaculus/forecasting-tools`) — framework to build an AI forecasting bot; `metac-bot-template` for tournaments. The **Metaculus AI Benchmark (AIB)** runs bots against pro humans (seasonal + MiniBench, prize-backed).
- **MIRAI** (arXiv:2407.01231; `mirai-llm.github.io`) — benchmark for LLM agents as temporal forecasters of international events, with tool use over a structured event database.
- **PolyBench** (arXiv:2604.14199) — a **Feb 2026** live prediction-market benchmark; across 7 LLMs and ~36k timestamp-locked predictions, only 2 posted positive returns — i.e. **most LLMs still don't beat the market**. Single recent study; treat as directional.
- **Open forecasting LLMs** — OpenForecaster-8B and successors approach superforecaster level on some 2025 benchmarks, **but the Metaculus AIB still shows top human Pros ahead**, and every result is shadowed by **temporal leakage** — trust prospective, distrust backtests (echoing brief 03 §6).

Design implication for ChronoForge: an **LLM-research + calibrated-prior + human/market-anchor hybrid** is the honest state of the art. It slots into the FORECAST stage as one ensemble member — never as an oracle.

## 5. What did NOT survive the honest scan (the fringe Fri named)

Explicitly checked, explicitly failed as prediction *channels* (full physics in `research/02-physics-reality-gate.md` + `science-charter.md §1`): **tachyonic/FTL signaling** (tachyons = vacuum instability, not messengers), **quantum-jumping / intention-based branch selection**, **precognition**, **entanglement-as-comms**. None provides a usable signal from the future.

They may enter ChronoForge **only** as lens hypotheses — reframed to a present-signal proxy, physics-locked, and scored by the Lens Ledger like anything else. No exceptions, no back door.

---

## Sources

- Scheffer et al., *Early-warning signals for critical transitions*, Nature 2009 — https://pdodds.w3.uvm.edu/files/papers/others/2009/scheffer2009a.pdf
- ewstools (Bury) — https://github.com/ThomasMBury/ewstools
- Bury et al., *ewstools* / critical-transition detection — https://arxiv.org/pdf/2406.05195
- Hu, *A review of Phillips-type right-tailed unit root bubble detection tests*, J. Economic Surveys 2023 — https://onlinelibrary.wiley.com/doi/10.1111/joes.12524
- psymonitor (Phillips, Shi & Caspi) — https://itamarcaspi.github.io/psymonitor/articles/illustrationSNP.html
- exuber (R) — https://cran.r-project.org/web/packages/exuber/exuber.pdf
- deanfantazzini/bubble (R) — https://rdrr.io/github/deanfantazzini/bubble/man/GSADF_Y.html
- Centola et al., *Experimental evidence for tipping points in social convention*, Science 2018 — https://www.science.org/doi/10.1126/science.aas8827
- NDlib (Rossetti et al.) — https://arxiv.org/pdf/1801.05854 · https://link.springer.com/article/10.1007/s41060-017-0086-6
- MIRAI: Evaluating LLM Agents for Event Forecasting — https://arxiv.org/abs/2407.01231 · https://mirai-llm.github.io/
- Metaculus forecasting-tools — https://github.com/Metaculus/forecasting-tools
- Metaculus AI Benchmark — https://www.metaculus.com/aib/
- PolyBench (live prediction-market LLM benchmark, 2026) — https://arxiv.org/abs/2604.14199
