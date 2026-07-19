#!/usr/bin/env python3
"""
GuardForge deterministic scanner — the shared brain for the triage-scanner agent AND the
Claude Code hooks. It finds, with file:line:
  - secrets / keys           (reported MASKED, never echoed in clear)
  - risky code patterns      (eval, pickle, shell=True, SQL interpolation, verify=False, ...)
  - protected files present  (.env, private keys, credential stores)
  - copyleft license signals (GPL / AGPL / LGPL)

Usage:
  python3 scan.py <path>            scan a file or directory
  python3 scan.py --stdin           scan a unified diff piped on stdin (added lines only)
  python3 scan.py --diff <file>     scan a unified diff from a file
  python3 scan.py <path> --format text

Always exits 0 — it reports, it does not gate. Stdlib only. Functions are importable
(find_secrets_in_text, mask, is_protected_file, classify_command) for the hook scripts.
"""
import sys, os, re, json, argparse

# --------------------------------------------------------------------------- secrets
SECRET_PATTERNS = [
    ("aws_access_key",  re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"), "CRITICAL"),
    ("aws_secret_key",  re.compile(r"(?i)aws_secret_access_key\s*[:=]\s*['\"]?([A-Za-z0-9/+]{40})"), "CRITICAL"),
    ("gcp_api_key",     re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b"), "CRITICAL"),
    ("github_token",    re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36}\b"), "CRITICAL"),
    ("github_fine_pat", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{22,}\b"), "CRITICAL"),
    ("stripe_secret",   re.compile(r"\b(?:sk|rk)_live_[A-Za-z0-9]{16,}\b"), "CRITICAL"),
    ("slack_token",     re.compile(r"\bxox[baprs]-[0-9A-Za-z-]{10,}\b"), "HIGH"),
    ("ai_api_key",      re.compile(r"\bsk-(?:ant-|proj-)?[A-Za-z0-9_\-]{20,}\b"), "HIGH"),
    ("google_oauth",    re.compile(r"\bya29\.[0-9A-Za-z_\-]+\b"), "HIGH"),
    ("private_key",     re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----"), "CRITICAL"),
    ("jwt",             re.compile(r"\beyJ[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}\b"), "MEDIUM"),
    ("generic_secret",  re.compile(r"(?i)\b(?:api[_-]?key|secret|password|passwd|token|access[_-]?token)\b\s*[:=]\s*['\"][^'\"]{8,}['\"]"), "MEDIUM"),
]
PLACEHOLDER_RE = re.compile(r"(?i)(example|placeholder|your[_-]?|xxx+|changeme|dummy|sample|redacted|<[^>]+>|\.\.\.|\*{3,})")

def mask(s):
    s = s.strip().strip("'\"")
    return (s[:4] + "…" + s[-4:]) if len(s) > 8 else (s[:2] + "…")

def find_secrets_in_text(text):
    """Return [(subtype, severity_hint, matched_substring), ...]."""
    out = []
    for subtype, rx, sev in SECRET_PATTERNS:
        for m in rx.finditer(text):
            val = m.group(0)
            if subtype in ("generic_secret", "jwt") and PLACEHOLDER_RE.search(val):
                continue
            out.append((subtype, sev, val))
    return out

def redact(line):
    out = line
    for _st, _sev, val in find_secrets_in_text(line):
        out = out.replace(val, mask(val))
    return out.strip()[:200]

# --------------------------------------------------------------------------- risky code
RISKY_PATTERNS = [
    ("eval_exec",       re.compile(r"\b(?:eval|exec)\s*\("), "HIGH",   "Dynamic eval/exec — never on untrusted input."),
    ("js_function_ctor",re.compile(r"\bnew\s+Function\s*\("), "HIGH",  "new Function() executes strings — avoid on input."),
    ("pickle_load",     re.compile(r"\bpickle\.loads?\s*\("), "HIGH",  "pickle on untrusted data = code execution; use json/safe formats."),
    ("yaml_unsafe",     re.compile(r"\byaml\.load\s*\((?![^)]*Safe)"), "HIGH", "yaml.load without SafeLoader; use yaml.safe_load."),
    ("shell_true",      re.compile(r"shell\s*=\s*True"), "HIGH",       "subprocess(shell=True) invites command injection; pass a list."),
    ("os_system",       re.compile(r"\bos\.system\s*\("), "MEDIUM",    "os.system runs a shell; prefer subprocess with a list."),
    ("tls_verify_off",  re.compile(r"verify\s*=\s*False|rejectUnauthorized\s*:\s*false"), "HIGH", "TLS verification disabled — MITM risk."),
    ("sql_interpolation",re.compile(r"(?i)(?:execute|query)\s*\(\s*f?['\"][^'\"]*(?:%s|\{|\+|\$\{)"), "HIGH", "SQL built by string interpolation; use parameterized queries."),
    ("html_sink",       re.compile(r"\b(?:innerHTML|outerHTML)\s*=|dangerouslySetInnerHTML"), "MEDIUM", "Raw HTML sink — XSS risk; sanitize/escape."),
    ("weak_hash",       re.compile(r"(?i)\b(?:md5|sha1)\s*\("), "MEDIUM", "MD5/SHA1 weak for security use; use SHA-256+/bcrypt/argon2."),
    ("insecure_random", re.compile(r"\bMath\.random\s*\(\)"), "LOW",   "Math.random() is not cryptographically secure for tokens/ids."),
]
LICENSE_RE = re.compile(r"SPDX-License-Identifier:\s*(?:AGPL|GPL|LGPL)|GNU (?:Affero )?General Public License")

# --------------------------------------------------------------------------- protected files
PROTECTED_EXTS = {"pem", "key", "p12", "pfx", "keystore", "jks", "kdbx", "asc"}
PROTECTED_NAMES = {"id_rsa", "id_dsa", "id_ecdsa", "id_ed25519", "credentials", ".npmrc", ".pypirc", ".netrc"}

def is_protected_file(path):
    base = os.path.basename((path or "").strip())
    low = base.lower()
    if re.match(r"\.env\.(example|sample|template|dist)$", low):
        return False
    if low == ".env" or low.startswith(".env."):
        return True
    if base in PROTECTED_NAMES:
        return True
    ext = low.rsplit(".", 1)[-1] if "." in low else ""
    if ext in PROTECTED_EXTS:
        return True
    if re.match(r"secrets?\.(ya?ml|json|env|txt)$", low):
        return True
    return False

# --------------------------------------------------------------------------- dangerous shell
def _rm_danger(cmd):
    for m in re.finditer(r"\brm\b([^\n;&|]*)", cmd):
        args = m.group(1)
        flagset = "".join(re.findall(r"-(\w+)", args))
        if "r" in flagset and "f" in flagset:
            if re.search(r"(?:^|\s)(?:/|/\*|~|\$HOME|\.|\*)(?:\s|$)", args):
                return True
    return False

def _force_push_main(cmd):
    if re.search(r"\bgit\s+push\b", cmd) and re.search(r"(?:--force\b|-f\b)", cmd):
        if "--force-with-lease" in cmd:
            return False
        return bool(re.search(r"\b(?:main|master)\b", cmd))
    return False

BASH_DENY = [
    (re.compile(r"(?:curl|wget)\b[^|]*\|\s*(?:sudo\s+)?(?:ba|z|d)?sh\b"), "Piping a downloaded script straight into a shell."),
    (re.compile(r":\s*\(\s*\)\s*\{\s*:\s*\|\s*:"), "Fork bomb."),
    (re.compile(r"\bmkfs(?:\.\w+)?\b"), "Filesystem format (mkfs)."),
    (re.compile(r"\bdd\b[^\n]*\bof=/dev/(?:sd|nvme|disk|hd)"), "Raw write to a disk device (dd)."),
    (re.compile(r">\s*/dev/(?:sd|nvme|disk|hd)\w*"), "Redirect onto a disk device."),
    (re.compile(r"\bchmod\s+-R\s+777\s+/(?:\s|$)"), "chmod -R 777 on /."),
    (re.compile(r"\bchown\s+-R\b[^\n]*\s/(?:\s|$)"), "Recursive chown on /."),
]
BASH_ASK = [
    (re.compile(r"\bgit\s+push\b[^\n]*(?:--force\b|-f\b)"), "Force-push rewrites history."),
    (re.compile(r"\bchmod\s+(?:-R\s+)?777\b"), "World-writable permissions (chmod 777)."),
    (re.compile(r"\bsudo\s+rm\b"), "Elevated delete (sudo rm)."),
    (re.compile(r"\b(?:reboot|shutdown|halt|poweroff)\b"), "Power/state change."),
    (re.compile(r"\bkill\s+-9\s+-1\b"), "Kill all processes."),
]

def classify_command(cmd):
    """Return ('deny'|'ask'|'allow', reason). Defensive: deny clearly-destructive, ask on risky."""
    cmd = cmd or ""
    if _rm_danger(cmd):
        return ("deny", "Recursive force-delete of /, ~, $HOME, ., or * — this destroys data.")
    if _force_push_main(cmd):
        return ("deny", "Force-push to main/master rewrites shared history.")
    for rx, why in BASH_DENY:
        if rx.search(cmd):
            return ("deny", why)
    for rx, why in BASH_ASK:
        if rx.search(cmd):
            return ("ask", why)
    return ("allow", "")

# --------------------------------------------------------------------------- scanning
SKIP_DIRS = {".git", "node_modules", "venv", ".venv", "__pycache__", "dist", "build",
             ".next", ".cache", "vendor", ".idea", ".mypy_cache", ".pytest_cache", "target", ".gradle"}
MAX_BYTES = 1_000_000

def _read_text(fp):
    try:
        if os.path.getsize(fp) > MAX_BYTES:
            return None
        with open(fp, "rb") as f:
            raw = f.read()
        if b"\x00" in raw[:8192]:
            return None
        return raw.decode("utf-8", "replace")
    except Exception:
        return None

def _scan_line(findings, fname, lineno, content):
    for st, sev, val in find_secrets_in_text(content):
        findings.append({"kind": "secret", "subtype": st, "severity_hint": sev,
                         "file": fname, "line": lineno, "masked": mask(val),
                         "detail": "possible secret/credential"})
    for st, rx, sev, msg in RISKY_PATTERNS:
        if rx.search(content):
            findings.append({"kind": "risky", "subtype": st, "severity_hint": sev,
                             "file": fname, "line": lineno, "snippet": redact(content), "detail": msg})
    if LICENSE_RE.search(content):
        findings.append({"kind": "license", "subtype": "copyleft", "severity_hint": "HIGH",
                         "file": fname, "line": lineno, "snippet": redact(content),
                         "detail": "copyleft signal (GPL/AGPL/LGPL) — check license compatibility"})

def scan_path(root):
    findings = []
    if os.path.isfile(root):
        files = [root]
    else:
        files = []
        for dp, dns, fns in os.walk(root):
            dns[:] = [d for d in dns if d not in SKIP_DIRS]
            for fn in fns:
                files.append(os.path.join(dp, fn))
    for fp in files:
        if is_protected_file(fp):
            try:
                present = os.path.getsize(fp) > 0
            except OSError:
                present = False
            if present:
                findings.append({"kind": "protected_file", "subtype": "present", "severity_hint": "MEDIUM",
                                 "file": fp, "line": 0,
                                 "detail": "sensitive/credential file present — ensure it's git-ignored and holds no real secret"})
        text = _read_text(fp)
        if text is None:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            _scan_line(findings, fp, i, line)
    return findings

def scan_diff(diff_text):
    findings = []
    cur = None
    newline = 0
    for line in diff_text.splitlines():
        if line.startswith("+++ "):
            m = re.match(r"\+\+\+ (?:b/)?(.*)", line)
            cur = (m.group(1).strip() if m else None)
            continue
        if line.startswith("@@"):
            m = re.search(r"\+(\d+)", line)
            newline = int(m.group(1)) if m else 0
            continue
        if line.startswith("+") and not line.startswith("+++"):
            _scan_line(findings, cur or "(diff)", newline, line[1:])
            newline += 1
        elif line.startswith("-") and not line.startswith("---"):
            continue
        elif not line.startswith("\\"):
            newline += 1
    return findings

def main(argv):
    ap = argparse.ArgumentParser(description="GuardForge deterministic scanner")
    ap.add_argument("target", nargs="?", help="file or directory to scan")
    ap.add_argument("--stdin", action="store_true", help="read a unified diff from stdin")
    ap.add_argument("--diff", help="read a unified diff from a file")
    ap.add_argument("--format", choices=["json", "text"], default="json")
    a = ap.parse_args(argv)

    if a.stdin:
        findings, scope = scan_diff(sys.stdin.read()), "<stdin diff>"
    elif a.diff:
        with open(a.diff, encoding="utf-8", errors="replace") as f:
            findings, scope = scan_diff(f.read()), a.diff
    elif a.target:
        findings, scope = scan_path(a.target), a.target
    else:
        ap.print_help(sys.stderr)
        return 0

    order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "INFO": 4}
    findings.sort(key=lambda f: order.get(f.get("severity_hint", "INFO"), 5))
    summary = {}
    for f in findings:
        summary[f["kind"]] = summary.get(f["kind"], 0) + 1
    result = {"scope": scope, "count": len(findings), "summary": summary, "findings": findings}

    if a.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"GuardForge scan: {scope}")
        print("  " + (", ".join(f"{k}={v}" for k, v in summary.items()) or "no findings"))
        for f in findings:
            extra = f"  ({f['masked']})" if f.get("masked") else ""
            print(f"  [{f['severity_hint']}] {f['kind']}/{f.get('subtype','')} "
                  f"{f.get('file','?')}:{f.get('line',0)} — {f.get('detail','')}{extra}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
