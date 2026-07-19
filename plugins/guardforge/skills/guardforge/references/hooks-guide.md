# Hooks guide — the automatic guardrails

The guardian **agents** judge a change when you ask. The **hooks** are the always-on layer:
deterministic checks that fire on Claude Code tool events and can stop a dangerous action
*before* it happens. This is the "stil hooks" half of GuardForge.

## What ships
`hooks/hooks.json` wires three guards (all scripts are Python/Bash, stdlib only):

| Event · matcher | Script | What it does |
|---|---|---|
| **PreToolUse · `Write\|Edit\|MultiEdit`** | `pretooluse_secrets.py` | Scans the content being written for secrets/keys and blocks writes to protected files (`.env`, `*.pem`, `id_rsa`, credential stores). Blocks on a secret; **asks** on a protected path. |
| **PreToolUse · `Bash`** | `pretooluse_bash.py` | Scans the command for dangerous patterns (`rm -rf /`, `curl…\|sh`, force-push to `main`, `chmod 777`, fork bombs, raw `dd` to a device, `mkfs`, `:(){…}`). Blocks the clearly-destructive; **asks** on the merely-risky. |
| **PostToolUse · `Write\|Edit`** | `posttooluse_checks.sh` | Advisory only: if the project has a known formatter/linter/test config, suggests running it. Never blocks. |

## The protocol (how blocking works)
Each hook reads the event JSON on **stdin** (`tool_name`, `tool_input`, `cwd`, …) and writes a
decision to **stdout**:
```json
{ "hookSpecificOutput": { "permissionDecision": "deny",
                          "permissionDecisionReason": "GuardForge: <why> — <fix>" } }
```
`permissionDecision` is `"allow"`, `"ask"` (prompt you), or `"deny"` (block, reason shown to
Claude). Scripts exit 0. The reason always says **what** and **how to proceed** — e.g. "looks
like an AWS key — move it to an env var / secrets manager, then retry."

## Fail-open vs fail-closed
By default the hooks **fail-open**: if a script can't parse the event or crashes, it allows the
action (a guardrail must never wedge your session). Set `GUARDFORGE_STRICT=1` in the
environment to **fail-closed** — on any internal error the hook denies instead. Use STRICT in
CI or on a sensitive repo; leave it off for everyday flow.

## Install
GuardForge's hooks activate automatically when the plugin is installed and enabled — Claude
Code reads `hooks/hooks.json` and resolves `${CLAUDE_PLUGIN_ROOT}` to the plugin path. To
verify or tune:
1. Enable the plugin, then run `/hooks` in Claude Code to see GuardForge's entries registered.
2. Test the Bash guard: ask Claude to run `rm -rf /tmp/guardforge-selftest` (safe path) — you
   should see it allowed; `rm -rf /` — denied. Test the secret guard by asking it to write
   `AKIAIOSFODNN7EXAMPLE` into a file — denied with a reason.
3. To disable one guard, comment it out of a local copy of `hooks.json`, or disable the
   plugin. To make a guard stricter, edit the pattern list at the top of its script.

## How hooks and agents relate
- The hooks share their pattern logic with `scripts/scan.py`, which `triage-scanner` runs — so
  what blocks you live is the same thing the review flags in a diff. One brain, two timings.
- Hooks are deterministic and narrow (no false sense of completeness). The **agents** are where
  judgement lives. A clean hook run is **not** a PASS — run a Review/Audit for that.
- Hooks never exfiltrate: a flagged secret is reported masked, never echoed.

## Tuning notes
- Patterns live as plain lists at the top of each script — add your org's token formats there.
- Keep `timeout` generous enough (the JSON sets a few seconds); a slow hook that times out
  fails-open by default.
- These guards reduce risk; they don't replace review, code scanning, or a real secrets
  manager. Honest by design.
