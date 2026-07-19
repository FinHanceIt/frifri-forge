# frifri-forge

**FriFri Creatives' forge fleet as a Claude Code plugin marketplace** — 18 multi-agent studios and verification harnesses, installable natively or copied into any repo with `npx`.

## Install

**Native (recommended) — inside Claude Code:**
```
/plugin marketplace add FinHanceIt/frifri-forge
/plugin install <name>@frifri-forge
```
Update later with `/plugin marketplace update frifri-forge`.

**As an `npx` installer — copy a plugin's prompts into any repo / terminal:**
```sh
npx github:FinHanceIt/frifri-forge list
npx github:FinHanceIt/frifri-forge add <name> [--dir <path>] [--force]
npx github:FinHanceIt/frifri-forge add --all
```
`add` copies a plugin's `agents/`, `skills/`, and `commands/` into `./.claude`. Plugins that ship `scripts/` or `hooks/` (e.g. waveforge, guardforge, cairn-harness) rely on the plugin root — use the **native** install for those.

## Plugins

| Plugin | What it is |
|---|---|
| `aevumforge` | Virtual longevity & regeneration research institute: 31 agents in two hemispheres (molecular science + alchemical hypothesis-generation), behind bioethics + never-fabricate gates. |
| `chronoforge` | Esoteric-seeded, science-locked event-prediction studio: turns fringe framings into measurable proxies, forecasts with a calibrated ensemble, keeps a Brier ledger. |
| `council-of-the-scythe` | Portfolio governance / anti-forge: forces SHIP/KILL/FREEZE/IGNORE on the whole fleet with a 100-point attention allocation. |
| `guardforge` | Guardian-agent team + real Claude Code hooks that gate code/build changes PASS / PASS-WITH-FIXES / BLOCK. Defensive only. |
| `ideaforge` | Domain-agnostic 11-agent think-tank: frame → generate → ground in evidence → premortem → verdict + next action. |
| `inkforge` | 7-agent human-voice writing studio: drafts in a bespoke voice, then de-AIs against an 8-point tell list + textstats. |
| `llmforge` | AI/LLM engineering studio: architecture, RAG, agents, model choice, integration code, evals, safety, cost — with gates. |
| `ofertaforge` | 10-agent bidding/prospecting/negotiation team for solo creatives; multi-currency, human gates, learning ledger. |
| `originforge` | 9-agent originality & authenticity studio: AI/plagiarism detection the way market engines see it, then honest human rewrite. |
| `psycheforge` | 15-unit self-transformation studio for reprogramming your own patterns; evidence-labeled, safety gates, measurable protocols. |
| `searchforge` | SEO/SEM/GEO studio: orchestrator + 17 specialists; Search-Console-first, white-hat, no fabricated metrics. |
| `shipforge` | Anti-build studio that drives built-but-not-live things to LIVE behind a reality gate (URL + smoke + one real event). |
| `statecraft` | Virtual state: 24 agents across all branches + central bank + oversight; configurable regime, checks & balances by default. |
| `theoforge` | The Eternal Council: 134 voices across 27 chambers of the world's traditions; full-council plenary per question. |
| `trendforge` | Trend-prediction megastructure: 168 agents harvest signals, grade momentum, forecast what's next with intervals. |
| `waveforge` | 7-agent binaural/brainwave audio studio: designs the protocol, renders a real .wav, FFT-verifies the beat, safety-gates. |
| `appfactory-enterprise` | Enterprise app-dev company: 80 agents across 14 departments (any web stack + game pipeline + independent audit office). |
| `cairn-harness` | Verification harness for AI coding agents: a 5-agent crew + a mutation-testing gate that catches a weakened/deleted test. |

## Notes
- The agents + skills activate in a Claude Code-compatible runtime. The marketplace catalog is `.claude-plugin/marketplace.json`.
- Each plugin under `plugins/` keeps its own `plugin.json` and any third-party attributions (see `LICENSE`).
- Marketplace wrapper is MIT. Not affiliated with Anthropic.
