# Launch-Readiness Ladder

The rungs from "built" to "traction." Rule: **find the lowest failing rung and fix only
that.** Everything above a failing rung is noise. Mark each rung PASS (with evidence) or GAP.

| # | Rung | PASS means (evidence) |
|---|---|---|
| 0 | Actually built | the core feature works locally — a real run, not a plan. GAP here → state **NEEDS-BUILD** and hand off; ShipForge does not build. |
| 1 | Runs from clean state | a fresh clone/env with a documented command starts it; no "works on my machine" magic. |
| 2 | Deploy target chosen | host picked (Vercel / Netlify / Supabase / managed) and the account exists. |
| 3 | Env & secrets resolved | every variable mapped to where it lives; **NO secret in the repo** (.env, service_role kept out). |
| 4 | Data ready | schema/migrations applied on the target; seed data if the app needs it to work. |
| 5 | Public URL live | a stranger (not localhost, not just Fri) can load it. |
| 6 | Critical path passes live | the one core action works on the live URL — smoke-tester PASS with captured output. |
| 7 | Telemetry live | one real activation event received + one alert (cost / downtime / errors) set. **← Definition of DONE.** |
| 8 | First real user/euro | an activation event from someone who is not Fri. **← Traction.** |

## How to use
- Triage walks 0→8 and stops at the first GAP = the single blocking gap.
- The next action clears that one rung (target: under a day of work).
- "Shipped" is claimed only at rung 7 (live + proven + instrumented). Rung 8 is the
  sentinel's traction check.
- If rung 0 fails, it is not a shipping job — it is a build job. Hand off; do not let
  ShipForge quietly turn into a builder.
