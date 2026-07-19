# Reference — The Codex (session file template)

Every AevumForge mission opens one `codex-{slug}.md` in the project folder. It is the single
source of truth; every agent reads and appends to its own section. Copy the skeleton below.

```
# CODEX — {inquiry title}
MODE: INQUIRE | GREAT WORK | APPRAISE | DESIGN
DATE: {YYYY-MM-DD}
QUESTION: {the real question, one paragraph — framed by the director / gerontologist}
HALLMARK FOCUS: {which of the 12 hallmarks, if any}

## SCIENTIA
{mechanisms & findings from the specialists — each claim carries an evidence-status label}

## HERMETICA
{symbolic readings — each labeled INTERPRETATION / ANALOGY / SYMBOL, real sources cited}

## BRIDGE
{symbolic-hypothesis-weaver: each crossing as
 SYMBOL (ORIGIN) → HYPOTHESIS → falsification test → [TESTABLE-NOW / IN-PRINCIPLE / UNTESTABLE]}

## EVIDENCE LEDGER
{evidence-librarian: CLAIM → SOURCE (graded) / ASSUMPTION / UNVERIFIED / BLOCKED: needs {X}}

## SKEPTIC PASS
{red-team-skeptic: steelman → ranked attacks → kill-question → verdict + what would change it}

## SAFETY & ETHICS
{bioethics-safety-warden: concern → line → ruling; overall PASS / PASS-WITH-FLAGS / BLOCK}

## INTEGRITY
{epistemic-integrity-auditor: no-fabrication + firewall checklist; breaches → owner; PASS / FIX}

## SYNTHESIS
{magnum-synthesist: the narrative + ranked hypothesis cards + the single next action}
```

## Section ownership & order
1. `SCIENTIA` — the routed specialists (director/gerontologist assign)
2. `HERMETICA` — hermetic-philosopher, spagyric-alchemist, eastern-longevity-adept, harmonics-resonance-adept
   *(parallel with SCIENTIA on GREAT WORK missions)*
3. `BRIDGE` — symbolic-hypothesis-weaver
4. `EVIDENCE LEDGER` — evidence-librarian
5. `SKEPTIC PASS` — red-team-skeptic
6. `SAFETY & ETHICS` — bioethics-safety-warden *(gate)*
7. `INTEGRITY` — epistemic-integrity-auditor *(gate — last before delivery)*
8. `SYNTHESIS` — magnum-synthesist *(only after both gates PASS)*

## Mode shortcuts
- **INQUIRE** — SCIENTIA + EVIDENCE LEDGER + INTEGRITY (skip HERMETICA/BRIDGE unless asked;
  SAFETY only if content drifts to application).
- **APPRAISE** — EVIDENCE LEDGER + owning specialist + SKEPTIC PASS + SAFETY + INTEGRITY.
- **DESIGN** — owning specialist + SKEPTIC PASS + SAFETY (conceptual study only) + INTEGRITY.
- **GREAT WORK** — the full Codex.
- **FAST-PATH** — no Codex; one labeled answer.
