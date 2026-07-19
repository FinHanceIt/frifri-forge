#!/usr/bin/env python3
"""GuardForge PreToolUse guard for Write|Edit|MultiEdit.
DENY when a secret is being written into a file; ASK on writes to a protected/credential file.
Fail-open by default (a guardrail must never wedge the session); set GUARDFORGE_STRICT=1 to
fail-closed. Reuses scripts/scan.py when reachable, with a self-contained fallback."""
import sys, os, json, re

STRICT = os.environ.get("GUARDFORGE_STRICT", "").strip().lower() in ("1", "true", "yes", "on")

def emit(decision, reason=""):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": decision,
        "permissionDecisionReason": reason}}))
    sys.exit(0)

# --- load the shared brain if we can ---------------------------------------
root = os.environ.get("CLAUDE_PLUGIN_ROOT", "")
if root:
    sys.path.insert(0, os.path.join(root, "skills", "guardforge", "scripts"))
try:
    import scan as _scan
    find_secrets = _scan.find_secrets_in_text
    mask = _scan.mask
    is_protected = _scan.is_protected_file
except Exception:
    _SP = [re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
           re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b"),
           re.compile(r"\b(?:ghp|gho|ghs)_[A-Za-z0-9]{36}\b"),
           re.compile(r"\b(?:sk|rk)_live_[A-Za-z0-9]{16,}\b"),
           re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----")]
    def find_secrets(t):
        return [("secret", "CRITICAL", m.group(0)) for rx in _SP for m in rx.finditer(t)]
    def mask(s):
        s = s.strip().strip("'\"")
        return (s[:4] + "…" + s[-4:]) if len(s) > 8 else (s[:2] + "…")
    def is_protected(p):
        b = os.path.basename((p or "").lower())
        if re.match(r"\.env\.(example|sample|template|dist)$", b):
            return False
        return (b == ".env" or b.startswith(".env.")
                or b in ("id_rsa", "credentials", ".npmrc", ".pypirc", ".netrc")
                or (b.rsplit(".", 1)[-1] if "." in b else "") in ("pem", "key", "p12", "pfx", "jks", "keystore"))

def main():
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except Exception:
        emit("deny", "GuardForge: couldn't parse the hook input (STRICT mode).") if STRICT else emit("allow")
        return
    ti = data.get("tool_input", {}) or {}
    path = ti.get("file_path", "") or ""
    chunks = []
    if ti.get("content"):
        chunks.append(ti["content"])
    if ti.get("new_string"):
        chunks.append(ti["new_string"])
    for e in (ti.get("edits") or []):
        if isinstance(e, dict) and e.get("new_string"):
            chunks.append(e["new_string"])
    text = "\n".join(chunks)

    hits = find_secrets(text) if text else []
    if hits:
        kinds = ", ".join(sorted({h[0] for h in hits}))
        emit("deny", f"GuardForge: this looks like a secret being written into "
                     f"{os.path.basename(path) or 'a file'} ({kinds}, e.g. {mask(hits[0][2])}). "
                     f"Move it to an environment variable or a secrets manager and reference it, then retry.")
    if path and is_protected(path):
        emit("ask", f"GuardForge: {os.path.basename(path)} is a sensitive/credential file. "
                    f"Make sure it's git-ignored and holds no real secret before writing. Proceed?")
    emit("allow")

main()
