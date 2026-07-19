#!/usr/bin/env node
// cairn-harness — npx installer + gate runner. Zero runtime deps (Node builtins only).
import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync, cpSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "..");
const pkg = JSON.parse(readFileSync(join(ROOT, "package.json"), "utf8"));
const argv = process.argv.slice(2);
const has = (f) => argv.includes(f);
const flag = (n, d) => { const i = argv.indexOf(n); return i >= 0 && argv[i + 1] ? argv[i + 1] : d; };

function copyTree(srcRel, destAbs, force) {
  const src = join(ROOT, srcRel);
  if (!existsSync(src)) return { copied: 0, skipped: 0, missing: true };
  let copied = 0, skipped = 0;
  (function walk(s, d) {
    mkdirSync(d, { recursive: true });
    for (const e of readdirSync(s, { withFileTypes: true })) {
      const sp = join(s, e.name), dp = join(d, e.name);
      if (e.isDirectory()) walk(sp, dp);
      else if (existsSync(dp) && !force) skipped++;
      else { cpSync(sp, dp); copied++; }
    }
  })(src, destAbs);
  return { copied, skipped, missing: false };
}

function init() {
  const target = resolve(flag("--dir", process.cwd()));
  const force = has("--force");
  const claude = join(target, ".claude");
  const r = {
    agents: copyTree("agents", join(claude, "agents"), force),
    skills: copyTree("skills", join(claude, "skills"), force),
    references: copyTree("references", join(claude, "references"), force),
    scripts: copyTree("scripts", join(target, "scripts"), force),
  };
  const want = {
    gate: "node scripts/mutation-gate.mjs",
    "gate:baseline": "node scripts/mutation-gate.mjs --all --set-baseline",
  };
  const pjPath = join(target, "package.json");
  let pjNote;
  if (existsSync(pjPath)) {
    const pj = JSON.parse(readFileSync(pjPath, "utf8"));
    pj.scripts ||= {};
    const added = [];
    for (const [k, v] of Object.entries(want)) if (!pj.scripts[k]) { pj.scripts[k] = v; added.push(k); }
    if (added.length) writeFileSync(pjPath, JSON.stringify(pj, null, 2) + "\n");
    pjNote = added.length ? `patched package.json (added: ${added.join(", ")})` : "package.json already has the gate scripts";
  } else {
    pjNote = 'no package.json here - add these scripts yourself:\n      "gate": "node scripts/mutation-gate.mjs",\n      "gate:baseline": "node scripts/mutation-gate.mjs --all --set-baseline"';
  }
  const line = (name, x) => `  ${name}: ${x.missing ? "- (not in package)" : `${x.copied} copied, ${x.skipped} skipped`}`;
  console.log(`cairn-harness ${pkg.version} - installed into ${target}`);
  console.log(line(".claude/agents    ", r.agents));
  console.log(line(".claude/skills    ", r.skills));
  console.log(line(".claude/references", r.references));
  console.log(line("scripts           ", r.scripts));
  console.log(`  ${pjNote}`);
  console.log("");
  console.log("Next:");
  console.log("  1. The gate needs a mutation runner in THIS repo:");
  console.log("       npm i -D vitest @stryker-mutator/core @stryker-mutator/vitest-runner");
  console.log("  2. Edit SRC_DIRS at the top of scripts/mutation-gate.mjs to match your source layout.");
  console.log("  3. Baseline once, then run the gate diff-scoped:");
  console.log("       npm run gate:baseline");
  console.log("       npm run gate            # shadow (never blocks); add --enforce to block");
  console.log("");
  console.log("  Agents + skills live under .claude/ and activate in a Claude Code-compatible runtime.");
  console.log("  The gate is plain Node and runs in any terminal.");
}

function gate() {
  const script = join(ROOT, "scripts", "mutation-gate.mjs");
  const rest = argv.slice(1);
  if (rest[0] === "--") rest.shift();
  const res = spawnSync(process.execPath, [script, ...rest], { stdio: "inherit" });
  process.exit(res.status ?? 0);
}

function help() {
  console.log(`cairn-harness ${pkg.version}
A verification harness for AI coding agents: a 5-agent crew + a mutation-testing gate.

Usage:
  npx cairn-harness init [--dir <path>] [--force]   Install agents, skills, and the gate into a repo
  npx cairn-harness gate [-- <gate args>]           Run the mutation gate (flags passed through)
  npx cairn-harness --version
  npx cairn-harness --help

Gate flags (after 'gate'): --since <ref> | --all | --set-baseline | --enforce

Docs: https://github.com/FinHanceIt/cairn-harness`);
}

const cmd = argv[0];
if (has("--version") || has("-v")) console.log(pkg.version);
else if (cmd === "init") init();
else if (cmd === "gate") gate();
else help();
