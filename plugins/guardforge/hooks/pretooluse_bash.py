#!/usr/bin/env python3
"""GuardForge PreToolUse guard for Bash. DENY clearly-destructive commands (rm -rf /,
curl|bash, fork bombs, disk dd, force-push to main); ASK on merely-risky ones. Fail-open by
default; GUARDFORGE_STRICT=1 fails closed. Reuses scripts/scan.py when reachable."""
import sys, os, json, re

STRICT = os.environ.get("GUARDFORGE_STRICT", "").strip().lower() in ("1", "true", "yes", "on")

def emit(decision, reason=""):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": decision,
        "permissionDecisionReason": reason}}))
    sys.exit(0)

root = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
if root:
    sys.path.insert(0, os.path.join(root, "skills", "guardforge", "scripts"))
try:
    import scan as _scan
    classify = _scan.classify_command
except Exception:
    def classify(cmd):
        cmd = cmd or ""
        if (re.search(r"\brm\b[^\n;&|]*-\w*r\w*f|\brm\b[^\n;&|]*-\w*f\w*r", cmd)
                and re.search(r"(?:\s|=)(?:/|~|\$HOME|\*)(?:\s|$)", cmd)):
            return ("deny", "Recursive force-delete of a root/home path.")
        if re.search(r"(?:curl|wget)[^|]*\|\s*(?:sudo\s+)?(?:ba)?sh\b", cmd):
            return ("deny", "Piping a download into a shell.")
        if re.search(r":\s*\(\s*\)\s*\{\s*:\s*\|\s*:", cmd):
            return ("deny", "Fork bomb.")
        if re.search(r"git\s+push\b.*(?:--force\b|-f\b)", cmd) or re.search(r"chmod\s+(?:-R\s+)?777\b", cmd):
            return ("ask", "Risky command.")
        return ("allow", "")

def main():
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except Exception:
        emit("deny", "GuardForge: couldn't parse the hook input (STRICT mode).") if STRICT else emit("allow")
        return
    cmd = (data.get("tool_input", {}) or {}).get("command", "") or ""
    decision, why = classify(cmd)
    if decision == "deny":
        emit("deny", f"GuardForge blocked this: {why} If you truly intend it, run it yourself outside Claude.")
    if decision == "ask":
        emit("ask", f"GuardForge flag: {why} Confirm you want to proceed.")
    emit("allow")

main()
