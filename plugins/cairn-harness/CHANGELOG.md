# Changelog

## 0.2.0 — 2026-07-19
- npx installer: `npx cairn-harness init` scaffolds the crew + gate into any repo's `.claude/` and `scripts/`, and adds `gate` / `gate:baseline` npm scripts (non-destructive — leaves existing scripts alone). `npx cairn-harness gate` runs the mutation gate with flags passed through. Zero runtime deps (Node builtins only). Also runnable pre-publish via `npx github:FinHanceIt/cairn-harness`.
- Repo is now dual-purpose: a Claude Code plugin AND an npm package (`bin/cli.mjs` + `package.json`). Plugin and package versions kept in sync at 0.2.0.

## 0.1.0 — 2026-07-19
- First release. Five-agent crew (auditor, planner, roaster, implementer, reviewer).
- L2 assertion-integrity mutation gate (diff-scoped, shadow-first). Proven on a real repo:
  caught deleting a uniquely-covering test (mutation score 58.6% -> 50.6%, BLOCK).
- `/cairn` orchestrator skill (ceremony-dial + gate ladder) and `/harden` setup skill.
- Human Gate Protocol for plain-language / non-technical review.
- Composes with mattpocock/skills (MIT) for the TDD/diagnose/review discipline layer.
