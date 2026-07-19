# Model Landscape — snapshot 2026-06-13

> A dated map, not a source of truth. Prices and names below were verified on the
> snapshot date; this file's half-life is weeks. **Re-verify by search anything you
> quote in MODELFIT.** When this file and reality disagree, reality wins — and this
> file should be updated.

## Claude family (Anthropic) — primary platform

| Model | API string | $/MTok in/out | Context | Max out | Assign to |
|---|---|---|---|---|---|
| Claude Fable 5 | `claude-fable-5` | 10 / 50 | 1M | 128k | frontier work: long-horizon agentic loops, orchestrators of large crews, judgment where a wrong call is expensive, single-agent designs that absorb a former multi-agent context split |
| Claude Opus 4.8 | `claude-opus-4-8` | 5 / 25 | 1M | — | heavy judgment workhorse: review, strategy, critique, complex code |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | 3 / 15 | 1M | — | default for workers: structured generation, code, most pipeline stages |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` | 1 / 5 | 200k | — | deterministic transforms: extract, classify, reformat, route |

Notes:
- **Fable 5** (released 2026-06-09) is the first Mythos-class model — a tier above
  Opus. Its sibling **Mythos 5** is the same model restricted to approved
  organizations; never assign Mythos in a general build.
- Fable 5 is not the default anything. It is the escalation target when Opus-tier
  evals fail, and the first choice only for genuinely frontier workloads. "Cheapest
  model that clears the bar" survives every release.
- 1M context on Fable/Opus/Sonnet tiers weakens "split agents because the window is
  too small" as an architecture argument — route that observation to the Director.

## Cost levers (apply before downgrading quality)

- **Batch API:** −50% on input and output, all tiers — default for anything
  non-interactive (overnight pipelines, bulk evals, golden-set runs).
- **Prompt caching:** cache hits ~−90% vs base input (Fable: $1/MTok hit; writes
  $12.50–$20/MTok depending on TTL). Layout prompts cache-first: stable system prompt
  and schemas as prefix, volatile input last.
- **Effort/thinking budgets:** on reasoning tiers, output cost scales with thinking —
  cap budgets per workload class instead of paying frontier-depth thinking on
  reformatting jobs.

## The tier ladder (workload class → starting tier)

| Workload class | Start at | Escalate to (on eval failure) |
|---|---|---|
| deterministic transform | Haiku-tier | Sonnet-tier |
| structured generation | Sonnet-tier | Opus-tier |
| judgment | Opus-tier (Sonnet if checkable downstream) | Fable-tier |
| open creative | Sonnet/Opus-tier | Fable-tier |
| frontier (long-horizon agentic, large-crew orchestration) | Fable-tier | — (redesign, don't pray) |

## Other families — as of snapshot; verify at engagement time

- **OpenAI:** GPT-5.5 flagship (2026-04); GPT-5.6 reported launching as of the snapshot
  date — exactly why you re-verify. Strong creative writing; chatty by default.
- **Google:** Gemini 3.1 Pro — price-to-performance leader at the frontier; newer 3.x
  releases rumored. Long context; mind-the-middle placement issues persist.
- **xAI:** Grok 4.3 in the frontier conversation.
- **Open weights (Llama, Qwen, Mistral, DeepSeek):** the fastest-moving shelf; never
  quote a name or size without a same-day search. Porting idioms in the SKILL apply
  regardless of version.
