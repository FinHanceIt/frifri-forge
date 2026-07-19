# ShipForge
**The anti-build studio. It ships what you already built.** · FriFri Creatives · v1.0.0

ShipForge is the missing last mile: it takes things that are *built but not live* and drives them to **deployed → proven → instrumented → first real user**. It is deliberately small — a shipping team should not be a 30-agent monster.

## Why it exists
The most expensive pattern in the fleet is not bad ideas — it is built things that never went live. ShipForge is the cure. The accountability sentinel is modeled on the 5/5 Santinela pattern from NEPSIS, pointed at the product pipeline instead of impulses.

## The one rule
Fix the **lowest failing rung** of the Launch-Readiness Ladder. Everything above it is noise. **Done = live + proven + instrumented** (ladder rung 7); traction = rung 8.

## Reality gate (never-fabricate)
Nothing is "shipped" without three artifacts: a public URL that loads, a passing smoke test, and one real telemetry event. No screenshots-of-hope.

## The team
- **shipforge** (director) — Harbor Master: classifies, routes, holds gates, keeps the ledger.
- **the-triage-officer** — finds the ONE gap blocking go-live.
- **the-deployer** — ready build → public URL, managed-first.
- **the-smoke-tester** — runs the real proof-of-life check (gate).
- **the-instrumentarius** — minimal telemetry + one alert (gate).
- **the-first-user** — the smallest act to get the first real user/euro.
- **the-sentinel** — Ship Ledger + ship/kill/freeze authority.

## Modes
SHIP (one artifact → live) · SWEEP (accountability pass over the stuck pile) · UNSTICK (one stuck project) · CHECK-IN (did the promised action happen) · FAST-PATH.

## Install
Install the `shipforge.plugin` file in Claude (Cowork / Claude Code). Then: "ShipForge, ship {X}" or "ShipForge, sweep my fleet."

## Boundaries
Ships what exists; never builds features (→ AppFactory / Claude Code / LLMForge). Not a launch campaign (→ launch-architect). Never fabricates a URL, a metric, or a "deployed successfully." RO/EN.
