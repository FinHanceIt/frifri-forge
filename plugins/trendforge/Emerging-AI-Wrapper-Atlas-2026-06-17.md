# TrendForge — Emerging AI-Wrapper Atlas
### Live demo run · Emergence mode · 2026-06-17

**Mission:** find AI "wrapper"/product categories that **do not meaningfully exist yet** (the capability just landed; the product hasn't), and forecast which will break out.
**Scope:** AI tools, global, horizon ~6–18 months.
**What ran:** 6 leading-indicator scouts in parallel — `scout-arxiv`, `scout-github`, `scout-huggingface`, `scout-producthunt`, `scout-reddit`, `scout-ai-tool-directories` — then corroboration, a competitive-density **honesty gate**, the AI-tools lens, confidence scoring and a verification pass. ~90 web sources, all 2025–2026.

> **How to read this:** every candidate had to clear two bars — (1) the enabling capability became cheap/open/reliable in 2025–26, and (2) the packaged product is genuinely thin. Anything that turned out to already have shipping entrants got **demoted to the Kill List** (see bottom) — that's the system refusing to sell you hype.

---

## Executive brief (TL;DR)

The frontier moved from *"can the model do it?"* to **"can it do it reliably, cheaply, privately and safely — at length?"** Every base capability (computer-use, memory, voice, video understanding, image editing) crossed a usable threshold in 2025–26, but the **trust/packaging layer** lags 6–18 months behind. So the not-yet-built wrappers don't look like new chatbots — they look like **reliability, privacy/on-device, real-time voice, consistency, and agent-safety** layers wrapped around capabilities that already work in a demo.

**Top 3 calls (highest conviction):**
1. **Agent Reliability & Observability for non-engineers** — "is my agent drifting / about to fail?" + runtime guardrails + undo. The single most-corroborated unmet need.
2. **Private, on-device "watch-my-screen" copilot** — local VLM + computer-use + preview/undo, sold on privacy. The capability just went sub-1GB.
3. **Truly full-duplex, multilingual, on-device voice agent** — voice SaaS is crowded but half-duplex and English-first; genuine barge-in + 40 languages + local just went open.

---

## Ranked not-yet-built categories

Each: enabling capability → unmet need → who's already near it (honesty) → the wedge → breakout ETA & estimated probability → riskiest assumption → confidence. **P(breakout) figures are TrendForge forecasts (calibrated judgment), not measured facts.**

### 1. Agent Reliability & Observability layer (for SMBs / prosumers) — *strongest*
- **Capability that landed:** Computer-use agents crossed human *accuracy* (OSWorld ~12% in 2024 → Claude Opus 4.6 **72.7%** in 2026) but not human *reliability*; long-horizon pass-rate collapses (76% → 52% as tasks lengthen) and a 50-component agent at 99%/step still fails ~4 in 10 runs. Eval tooling matured (DeepEval, Inspect AI, Promptfoo — Promptfoo acquired by OpenAI Mar 2026).
- **Unmet need:** "agents demo great, fail catastrophically in production"; Gartner-style projections of 40%+ agentic projects cancelled. No tool tells a *non-engineer* SMB "your support agent is drifting / hallucinating more this week."
- **Already near it (honesty):** developer eval frameworks exist; "ontology layer" framings are emerging. **Prosumer/SMB packaging is absent.**
- **Wedge:** continuous eval-as-a-service translated into plain-language **agent health monitoring** + runtime guardrails + one-click rollback. Moat = the longitudinal reliability dataset you accumulate.
- **ETA:** now–9 months · **P(breakout) ≈ 0.70**
- **Riskiest assumption:** that SMBs deploy enough agents *soon* to need a monitor before the platforms bundle it.
- **Confidence: MEDIUM-HIGH** (corroborated by arXiv + GitHub + Reddit + verification).

### 2. Private, on-device "watch-my-screen" copilot
- **Capability that landed:** Video-capable VLMs shrank below 1GB (SmolVLM2 256M runs in-browser; a 500M model already powers an iPhone app analyzing video locally); open computer-use grounding (OpenCUA-7B/72B) hit usable accuracy; <3B agentic SLMs drive system APIs on ~6GB phone RAM.
- **Unmet need:** screen-aware assistants today are cloud-bound and expensive; privacy-sensitive users (health, legal, finance, journaling) can't use them.
- **Already near it (honesty):** cloud computer-use (OpenAI Operator, Claude Computer Use) exists but is brittle and not private; **local + private + with an undo/preview layer is thin-to-absent.**
- **Wedge:** "an assistant that watches your screen and acts — 100% on your machine," sold on privacy + a dry-run/undo trust layer.
- **ETA:** 6–12 months · **P(breakout) ≈ 0.55**
- **Riskiest assumption:** on-device reliability/latency is good enough for real tasks in this window.
- **Confidence: MEDIUM** (HF + arXiv + GitHub).

### 3. Full-duplex, multilingual, on-device voice agent
- **Capability that landed:** Open full-duplex speech (Moshi ~200ms on an iPhone; VibeVoice-Realtime-0.5B), 40-language streaming ASR in one 600M model (NVIDIA Nemotron/Parakeet, Jun 2026), free in-browser TTS (Kokoro-82M), and a post-training recipe (OmniFlatten) to make *any* LLM voice-native.
- **Unmet need:** voice-agent SaaS is **half-duplex** (walkie-talkie feel) and English-first; nobody has a genuinely interruptible, 40-language, low-cost receptionist/booking line.
- **Already near it (honesty):** voice agents are **crowded** (ElevenLabs, Vapi ~62M calls/mo, Retell, Synthflow). The crowd is *turn-based + cloud + English*. The specific combo — full-duplex **and** multilingual **and** on-device/cheap — is the gap.
- **Wedge:** the interaction model (true barge-in) + non-English markets + near-zero inference cost.
- **ETA:** 3–9 months · **P(breakout) ≈ 0.60**
- **Riskiest assumption:** incumbents bolt on full-duplex before a new entrant wins distribution.
- **Confidence: MEDIUM** (HF + arXiv).

### 4. Consistent serial / branded visual-content engine
- **Capability that landed:** Open, character-consistent, instruction-driven image editing with reliable in-image **text** editing (Qwen-Image-Edit-2511, FLUX.1 Kontext) — i.e., "change this, keep the character/brand the same" across many frames.
- **Unmet need:** image generators are saturated but produce **one-off** images; keeping the *same* character/brand across a whole campaign, comic, storybook or product line is still painful.
- **Already near it (honesty):** image gen is one of the **most saturated** categories on every directory; consistency primitives exist but aren't packaged as a "whole-series brand engine."
- **Wedge:** workflow + brand memory (lock a character/style, generate a coherent *series*), not another single-image generator. (Directly adjacent to your Little Wonder Press storybook work.)
- **ETA:** now–6 months · **P(breakout) ≈ 0.60**
- **Riskiest assumption:** Midjourney/Adobe/base tools add native consistency and eat the niche.
- **Confidence: MEDIUM** (HF + Product Hunt + directories).

### 5. Agent "firewall" / continuous red-team for non-experts
- **Capability & threat that landed:** automated agent red-teaming found up to **90.5% attack success** on LLM search agents (prompt injection via tools/web); a wave of dev-side agent-firewall repos appeared after 2026's first big agent-security scare.
- **Unmet need:** as people deploy agents that touch their accounts, there's no consumer-grade "permission gating + egress firewall + kill switch" they can understand.
- **Already near it (honesty):** **dev-facing** firewalls/sandboxes are emerging (e.g. Pipelock). Consumer/prosumer packaging barely exists.
- **Wedge:** a non-developer "agent safety control panel" — approvals, receipts, undo, kill switch.
- **ETA:** 6–12 months · **P(breakout) ≈ 0.50**
- **Riskiest assumption:** the OS/platform vendors own this surface and absorb it.
- **Confidence: MEDIUM** (arXiv + GitHub).

### 6. Interactive-environment-as-a-service (world-model dev primitive) — *speculative / longer horizon*
- **Capability that landed:** real-time, playable world models (Genie 3: 720p/24fps, minutes of coherent interaction; Waymo adopted it for driving sim in Feb 2026); open streaming variants (Matrix-Game 2.0) appearing.
- **Unmet need:** no general, dev-facing API to spin up controllable simulated environments (game prototyping, robot/VLA training data, edge-case sims).
- **Already near it (honesty):** Genie 3 is **gated/research**; Waymo's use is internal. No general primitive.
- **Wedge:** be the "Stripe for simulated environments."
- **ETA:** 12–24 months · **P(breakout) ≈ 0.35 (12mo), higher by 24mo**
- **Riskiest assumption:** cost/quality/control aren't dev-ready in the window, and frontier labs keep it in-house.
- **Confidence: LOW-MEDIUM** (single-domain: mostly arXiv; flagged speculative).

---

## Kill list — looks "uninvented," but is already being built (don't)

The honesty gate demoted these from "whitespace" to "contested" using the verification pass:

- **Insurance / liability for AI agents** — already forming: **Mount** (YC Spring 2026, marketed as the first AI-agent liability insurance carrier), **Klaimee** (YC, EU-AI-Act-focused), plus Munich Re, Armilla, Corgi, Embroker. Regulatory tailwind is real but **the EU AI Act high-risk deadline is in flux** (original 2 Aug 2026; a 7 May 2026 political agreement proposes pushing Annex III to Dec 2027 — not yet law). *Adjacent* whitespace: the agent **audit-log/telemetry/risk-scoring substrate** insurers need.
- **Portable "memory passport" across models** — already shipping in early form: **Anuma** (private cross-model memory), plus Anthropic and Google adding ChatGPT/Claude memory import (Mar 2026). Narrower whitespace: **user-owned/local** memory, or memory **for agents** (not just chat).
- **"Prove a human wrote this" / authorship provenance** — already here: **GPTZero Writing Replay** (keystroke playback) and **Grammarly Authorship**. Narrower whitespace: portable, cross-app provenance, or provenance for **code/design** rather than prose.
- **Generic computer-use & generic AI notetakers/voice bots** — crowded; do not enter horizontally.

---

## Convergence & timing map

- **The repeating pattern:** capability crosses a usable threshold → builders ship *infrastructure* on GitHub/HF → the *trust/packaging* product lags 6–18 months. That lag is the whole opportunity.
- **Near term (now–9mo):** reliability/observability (#1), serial-content engine (#4), full-duplex voice (#3).
- **Mid term (6–12mo):** private on-device copilot (#2), agent firewall (#5).
- **Longer (12–24mo):** world-model-as-a-service (#6).
- **Strongest convergence:** *on-device + private + agentic* (small VLMs + SLMs + local voice) — a different cost/privacy structure under every cloud wrapper today. Picks #2 and #3 sit on it.

---

## Caveats (read before betting)

1. **Some magnitudes are from secondary aggregators** (star counts, directory totals, a few launch metrics), not first-party APIs — treat them as indicative; a Phase-2 backend would harden them.
2. **"Absence" is absence-of-evidence, not proof of zero** — each whitespace is "thin," not "empty"; one verification pass already collapsed three candidates.
3. **This space moves monthly.** Re-run triggers: a base-model vendor ships any of these natively; a named entrant raises a large round; the EU AI Act timeline is finalized.

---

## Sources (selected, all 2025–2026)

**Capability / research:** OSWorld-Human (arxiv.org/abs/2506.16042); long-horizon reliability (arxiv.org/abs/2603.29231); JitRL gradient-free continual learning (arxiv.org/abs/2601.18510); SEAL (arxiv.org/abs/2506.10943); SLMs for agents (arxiv.org/abs/2510.03847); behaviorally-calibrated abstention (arxiv.org/abs/2512.19920); SafeSearch agent red-teaming (arxiv.org/abs/2509.23694); Genie 3 / world models survey (arxiv.org/abs/2510.20668); full-duplex speech survey (arxiv.org/abs/2509.14515).
**Models / infra:** Moshi (kyutai.org/Moshi.pdf); VibeVoice-Realtime-0.5B & 1.5B (huggingface.co/microsoft); Nemotron/Parakeet 40-lang ASR (huggingface.co/nvidia/parakeet-unified-en-0.6b); Kokoro-82M (huggingface.co/hexgrad/Kokoro-82M); SmolVLM2 (huggingface.co/blog/smolvlm); OpenCUA (huggingface.co/xlangai/OpenCUA-7B); mem0 (github.com/mem0ai/mem0); DeepEval (github.com/confident-ai/deepeval); Pipecat (github.com/pipecat-ai/pipecat); Agent Skills + gh CLI (github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli).
**Market / saturation / honesty:** Product Hunt AI categories (producthunt.com/categories/ai-voice-agents, /ai-agents); There's An AI For That (theresanaiforthat.com); Toolify (toolify.ai); a16z Top-100 GenAI apps (a16z.com/100-gen-ai-apps-6); computer-use failures 2026 (coasty.ai/blog); reliability-compounding (mindstudio.ai/blog/reliability-compounding-problem-ai-agent-stacks).
**Verification pass:** EU AI Act timeline (digital-strategy.ec.europa.eu; gibsondunn.com Omnibus); AI-agent insurance — Mount/Klaimee (founderland.ai; ycombinator.com); portable memory — Anuma + Gemini/Claude import (winbuzzer.com 2026-03-27; bloomberg.com 2026-03-03); authorship provenance — GPTZero/Grammarly (gptzero.me/authorship; grammarly.com/authorship); computer-use reliability — Claude Opus 4.6 72.7% OSWorld (coasty.ai).

*Generated by TrendForge v1.0 — emergence-mode demo run. P(breakout) values are calibrated forecasts, not measured metrics. This run detects trends; it does not manufacture them.*
