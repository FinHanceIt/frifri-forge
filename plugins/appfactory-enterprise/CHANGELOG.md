# Changelog — appfactory-enterprise

## 1.0.0 (2026-06-07)

### All 80 agents rewritten to a research-backed template

Patterns distilled from the two leading public subagent collections — wshobson/agents (35.7k★) and VoltAgent/awesome-claude-code-subagents (20.2k★, both MIT) — plus the official Claude Code subagent docs:

- `<done_when>`: 4–6 quantified completion gates per agent (numbers, not adjectives).
- `<workflow_position>`: After / Hands off to / Gate / Distinct from — explicit sibling boundaries so an 80-role roster routes cleanly.
- `<knowledge>`: June-2026 ground truth per domain (React 19.2 + Compiler GA, Next.js 16.2 LTS, TS 6/7-beta, Node 24 LTS, Vue 3.5/3.6-beta Vapor, Nuxt 4.4, Angular 22, Python 3.14, Spring Boot 4/Java 25 LTS, PHP 8.5/Laravel 13, .NET 10 LTS, Unity 6.4, Unreal 5.7/UE6 announced, Godot 4.6.3 Jolt, Tailwind 4.3, Playwright 1.60, Vitest 4.1) with a verify-volatile-facts rule.
- Descriptions: sharpened, second `<example>` added, "Use PROACTIVELY when …" auto-delegation trigger added.
- Professional-services roles (legal ×4, finance ×4, chro, org-psychologist): disclaimers, jurisdiction-first intake (≤3 questions), most-protective-standard default, refusal-with-lawful-alternative, escalation triggers.
- Auditors (×7): independence rules, evidence per finding, Critical→Positive findings ladder, remediation ladder, PASS/FIX verdicts.
- skills.sh hooks: agents reference installable rule-source skills (see `skills/appfactory/references/skills-sh-picks.md`).
- Tools: least-privilege kept; WebSearch/WebFetch added only where live-fact verification is part of the job.

### Fixed

- 3 truncated agent files reconstructed in full: `angular-engineer`, `audit-director`, `financial-auditor`.
- Truncated `SKILL.md` and `references/org-chart.md` rebuilt completely (org chart previously ended mid-row at agent 69/80; W6 workflow cut mid-sentence).
- Stale "48 specialist agents across 10 departments" in `ceo.md` → 80/14 everywhere.
- Stray `</output>` artifact tag removed from the end of every agent file.

### Added

- `CHANGELOG.md` (this file).
- Workflows W7 (web platform deep work) and W8 (independent audit) fully documented in SKILL.md and org-chart.md.
- Cost-tiering guidance (when to pin opus/haiku vs keep `inherit`) in org-chart.md.
- Refreshed skills-sh-picks.md with June-2026 registry additions (mattpocock/skills, microsoft/playwright-cli, firebase, sentry, posthog, remotion, taste-skill, superpowers orchestration skills, marketing-psychology/ai-seo).

### Credits

Structural patterns adapted (not copied) from MIT-licensed collections wshobson/agents and VoltAgent/awesome-claude-code-subagents, and from the skills.sh registry. Version facts verified against official release channels, June 2026.

## 0.3.0

- 80 agents, 14 departments, orchestration skill, skills.sh picks reference.
