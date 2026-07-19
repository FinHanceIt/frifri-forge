---
name: harden
description: Make a repo ready for the Cairn crew — install the mutation gate + baseline, wire test/typecheck, and optionally add a pre-commit hook and git guardrails. Use once per repo, or when "make this repo agent-ready", "set up the gate", "harden this repo", "add the mutation gate". Refuses to claim readiness a repo doesn't have.
---

# harden — make a repo Cairn-ready

Idempotent setup. Inspect first; never overwrite a customized file without saying so.

## Steps

1. **Refuse if there is no test runner.** If the repo has no way to run tests (no vitest/jest/pytest/go test, no `test` script), say so plainly and offer to scaffold one. A gate with nothing to measure is worse than none. Do not proceed silently.
2. **Install the gate.** Copy this plugin's `scripts/mutation-gate.mjs` into the repo's `scripts/`. Add dev deps for the repo's stack — for a JS/TS + vitest repo: `@stryker-mutator/core`, `@stryker-mutator/vitest-runner`. Add scripts: `"gate": "node scripts/mutation-gate.mjs"`, `"gate:baseline": "node scripts/mutation-gate.mjs --all --set-baseline"`.
3. **Baseline.** Run `npm run gate:baseline` to record the current mutation score into `.cairn/mutation-baseline.json`. Report it honestly — a low score is a finding, not a failure.
4. **(Optional) Pre-commit — from mattpocock/setup-pre-commit.** Offer Husky + lint-staged running typecheck + tests on staged files, so nothing merges red. Ask before adding.
5. **(Optional) Git guardrails — from mattpocock/git-guardrails.** Offer PreToolUse hooks that block dangerous git (`push --force`, `reset --hard`, `clean -fd`) and writes to sealed test paths. Ask before adding.

## Hard rules

- Never fake readiness. `gate:baseline` reports the real number; a repo with weak tests gets told, not flattered.
- Every dev dep you add must resolve at a real version — check, don't guess.
- Secrets never enter the repo. The gate's config carries no keys.

## Output

A short readiness report: test runner (found/missing), gate installed (y/n), baseline mutation score, pre-commit + guardrails (added/declined), and the one next step.
