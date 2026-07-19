# IdeaForge — Handoff Contracts (the Idea Dossier)
*The session lives in one running document: the **Idea Dossier**. Each thinker consumes the Dossier-so-far and appends exactly its section. The Facilitator is the only router and owns the LEDGER.*

## Session Brief (Facilitator fills first)
```
idea_or_question : <the raw input, verbatim>
reframed_as      : <the real question, after the Philosopher — may update>
mode             : Spark | Crucible | Horizon | Verdict | Roundtable
domain           : business | product | content | social | research | personal | other
success_means    : <what a good outcome looks like for THIS user>
constraints      : <budget, time, skills, values, non-negotiables — or "none stated">
audience/user    : <who the idea is for, if any>
language         : RO | EN | both
depth            : quick | standard | deep
```

## Dossier sections (owner → schema)

### LEDGER — Facilitator
```
mode · phase · sections_done[] · open_gate · dissent_log[] · next_action
```

### FRAME — Philosopher
```
real_question · hidden_assumptions[] · success_definition ·
what_changes_if_solved · reframes[] (>=2 alternative framings) · constraints_surfaced[]
```

### POOL — Explorer
```
ideas[] (>=7; each = one-line concept + the angle/method it came from) ·
wildcards[] (>=1 deliberately strange) · — NOT pre-filtered
```

### COMBINATIONS — Synthesist
```
merges[] (idea A + idea B -> new) · forks[] (one idea -> variants) ·
analogies[] (this is like X in field Y) ·
precedents[] (who has done something adjacent — label "assumption" unless Investigator-verified)
```

### EVIDENCE — Investigator  *(the ONLY section that asserts external fact)*
```
known_facts[] (each with a source link) · landscape (what already exists) ·
base_rates (how often this class of thing works) · unknowns[] (what we couldn't verify) · sources[]
```

### DEMAND — Advocate
```
who_wants_this · jobs_to_be_done[] · need_intensity (vitamin <-> painkiller) ·
adoption_friction[] · "so what / who cares" verdict
```

### FEASIBILITY — Realist
```
what_must_be_true[] · resources_needed · dependencies[] ·
second_order_effects[] · hardest_part · feasibility (high/med/low + why)
```

### CRITIQUE — Skeptic
```
steelman (strongest case FOR) · failure_modes[] ·
premortem ("it's 12 months later and this failed because…") ·
bias_check[] (which biases the team is falling for) ·
kill_question (the one question that, answered wrong, ends it)
```

### STAKES — Steward
```
stakeholders[] · who_benefits · who_pays · harms/externalities[] ·
ethics_flags[] · risk (legal/reputational/social) · safety_verdict (clear | caution | stop)
```

### HORIZON — Futurist
```
trends[] (STEEP; each = direction + so-what) · scenarios (best / base / worst) ·
wildcards[] · durability (what makes this last or expire) · timing (why now / why not yet)
```

### VERDICT — Strategist
```
options_scored[] (Impact x Confidence x Effort, or Desirability/Feasibility/Viability) ·
recommendation · rationale · confidence (high/med/low) · dissent_noted ·
next_action · build_brief? (yes/no)
```

## Optional — BUILD-BRIEF (Strategist; only when a software build is the chosen next step)
*AppFactory-ready. Hand to AppFactory's CEO/COO agent.*
```
mission · problem · target_user · core_value ·
must_have_features[] · explicitly_out_of_scope[] ·
constraints (budget/time/stack if known) · success_metric · open_questions[]
```

## Routing per mode
```
Spark      : FRAME -> POOL + COMBINATIONS -> DEMAND -> VERDICT
Crucible   : EVIDENCE -> CRITIQUE + STAKES + FEASIBILITY -> VERDICT
Horizon    : EVIDENCE -> HORIZON -> STAKES -> VERDICT
Verdict    : EVIDENCE -> FEASIBILITY + DEMAND + CRITIQUE -> VERDICT
Roundtable : FRAME -> POOL -> COMBINATIONS -> EVIDENCE -> DEMAND ->
             FEASIBILITY -> CRITIQUE -> STAKES -> HORIZON -> VERDICT
```
**Gate 1** after FRAME (or right after the mode is picked, in modes without FRAME).
**Gate 2** before VERDICT is finalized (and before any build-brief hand-off).
The Facilitator may run one loop-back to POOL if CRITIQUE/STAKES finds a fatal flaw, then proceed.

**Safety screen.** The Steward's safety verdict runs in **every** mode, regardless of the arc above — Spark included. A mode may skip the full STAKES section, never the safety check.
