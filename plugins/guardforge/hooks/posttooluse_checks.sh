#!/usr/bin/env bash
# GuardForge PostToolUse advisory for Write|Edit|MultiEdit. Never blocks — it just suggests
# running the project's own format/lint/test if a known config is present. Reads event JSON
# on stdin and emits additionalContext.
payload="$(cat)"
cwd="$(printf '%s' "$payload" | python3 -c 'import sys,json
try:
    print(json.load(sys.stdin).get("cwd",""))
except Exception:
    print("")' 2>/dev/null)"
[ -z "$cwd" ] && cwd="${PWD}"

sugg=""
add() { sugg="${sugg}${sugg:+ · }$1"; }
[ -f "$cwd/package.json" ] && add "npm run lint && npm test"
{ [ -f "$cwd/pyproject.toml" ] || [ -f "$cwd/setup.cfg" ]; } && add "ruff check . && pytest -q"
[ -f "$cwd/Cargo.toml" ] && add "cargo fmt && cargo clippy && cargo test"
[ -f "$cwd/go.mod" ] && add "gofmt -l . && go vet ./... && go test ./..."
[ -f "$cwd/.pre-commit-config.yaml" ] && add "pre-commit run --files <changed>"

if [ -n "$sugg" ]; then
  printf '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"GuardForge advisory — after this edit, consider: %s"}}\n' "$sugg"
fi
exit 0
