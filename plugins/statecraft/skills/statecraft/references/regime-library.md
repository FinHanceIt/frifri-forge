# Statecraft — Regime Library

`the-charter` picks or builds the regime for a run. Default is **constitutional
democracy**. Each preset defines: how power is distributed, who checks whom (the
checks-and-balances matrix), the franchise, and how the seats behave. Under every preset,
the checks still *speak* (safety-charter §2) even where their *power* is dialed down.

## The checks-and-balances matrix
For any regime, `the-charter` fills this grid — who can stop whom:

| Actor | Can be checked by | Instrument |
|---|---|---|
| Head of government (`the-premier`) | assembly, court, press, citizenry | no-confidence, review, scrutiny, vote |
| Legislature (`the-assembly`) | court, head of state, referendum | judicial review, veto/assent, ballot |
| Court (`the-bench`) | constitution, appointments, amendment | charter text, who seats judges |
| Money: `the-treasury` | `the-mint` (independent), auditor | monetary independence, audit |
| Executive generally | `the-auditor`, `the-opposition`, `the-citizenry` | anti-corruption, opposition, protest/elections |

A regime is largely *defined* by which of these instruments are strong, weak, or absent.

## Presets

**Constitutional democracy (default).** Full separation of powers; free elections; strong
court; independent central bank and press; rights entrenched. All checks strong.

**Parliamentary vs presidential.** Parliamentary: `the-premier` sits in and answers to
`the-assembly`; `the-sovereign` is ceremonial. Presidential: an elected executive separate
from the legislature; stronger veto, fixed term, harder gridlock.

**Federal vs unitary.** Federal: power shared with sub-units (states/Länder); add a
territorial check and inter-governmental bargaining. Unitary: central government dominant;
local government delegated, not sovereign.

**Constitutional monarchy.** `the-sovereign` reigns with ceremonial/reserve powers; real
power with `the-premier` + `the-assembly`.

**Technocracy.** Ministries staffed by experts; `the-mandarin` weight is high; legitimacy
rests on performance, not the ballot — model the legitimacy risk when performance dips.

**Council / direct democracy.** Frequent referenda; `the-citizenry` has direct
instruments; slower, more volatile, high-participation dynamics.

**One-party / authoritarian (analysis-only).** Executive dominance; weak or captured
court, opposition, press. Per safety-charter, this is modeled as **dynamics and
trade-offs** — how legitimacy, information, and unrest behave when checks are suppressed —
never as a real repression playbook. The suppressed checks are still *voiced* so their
cost is visible.

**Custom.** Fri sets each matrix cell; `the-charter` flags any incoherence (e.g., "strong
court but the executive appoints and removes judges at will" → the court's independence is
nominal, say so).

## Anchoring
A preset can be anchored to a real country (RO+EU, US, etc.). Then `the-charter` maps the
preset onto that country's real institutions, and facts about them are labeled
`verified/assumed` per never-fabricate.
