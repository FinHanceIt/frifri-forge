#!/usr/bin/env node
// frifri-forge — Claude Code plugin marketplace + generic npx installer. Zero runtime deps.
import { existsSync, mkdirSync, readdirSync, readFileSync, cpSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "..");
const market = JSON.parse(readFileSync(join(ROOT, ".claude-plugin", "marketplace.json"), "utf8"));
const pkg = JSON.parse(readFileSync(join(ROOT, "package.json"), "utf8"));
const argv = process.argv.slice(2);
const has = (f) => argv.includes(f);
const flag = (n, d) => { const i = argv.indexOf(n); return i >= 0 && argv[i + 1] ? argv[i + 1] : d; };
const byName = Object.fromEntries(market.plugins.map((p) => [p.name, p]));

function copyTree(src, dest, force) {
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
  })(src, dest);
  return { copied, skipped, missing: false };
}

// positional names only: skip flags and the value that follows --dir
function positionals(arr) {
  const out = [];
  for (let i = 0; i < arr.length; i++) {
    const a = arr[i];
    if (a === "--dir") { i++; continue; }
    if (a.startsWith("-")) continue;
    out.push(a);
  }
  return out;
}

function list() {
  console.log(`${market.name} - ${market.plugins.length} plugins\n`);
  for (const p of market.plugins) console.log(`  ${p.name}`);
  console.log(`\nNative install (recommended), inside Claude Code:`);
  console.log(`  /plugin marketplace add FinHanceIt/frifri-forge`);
  console.log(`  /plugin install <name>@frifri-forge`);
  console.log(`Copy prompts into any repo:`);
  console.log(`  npx github:FinHanceIt/frifri-forge add <name>`);
}

function add() {
  const names = positionals(argv.slice(1));
  const targets = has("--all") ? market.plugins.map((p) => p.name) : names;
  if (!targets.length) { console.error("Usage: add <plugin> [more...] | --all  [--dir <path>] [--force]"); process.exit(1); }
  const dir = resolve(flag("--dir", process.cwd()));
  const force = has("--force");
  for (const name of targets) {
    const p = byName[name];
    if (!p) { console.error(`  ? unknown plugin: ${name} (try 'list')`); continue; }
    const psrc = join(ROOT, p.source);
    const claude = join(dir, ".claude");
    const parts = ["agents", "skills", "commands"]
      .map((sub) => [sub, copyTree(join(psrc, sub), join(claude, sub), force)])
      .filter(([, r]) => !r.missing)
      .map(([sub, r]) => `${sub}:${r.copied}${r.skipped ? ` (+${r.skipped} kept)` : ""}`);
    const extras = ["scripts", "hooks"].filter((d) => existsSync(join(psrc, d)));
    console.log(`  ${name}  ->  ${parts.join("  ") || "nothing to copy"}${extras.length ? `   [has ${extras.join("/")}: use native install]` : ""}`);
  }
  console.log(`\nCopied into ${join(dir, ".claude")}. Activates in a Claude Code-compatible runtime.`);
}

const cmd = argv[0];
if (has("--version") || has("-v")) console.log(pkg.version);
else if (cmd === "list" || cmd === "ls") list();
else if (cmd === "add" || cmd === "install") add();
else {
  console.log(`${market.name} ${pkg.version} - ${market.plugins.length} Claude Code plugins

Usage:
  npx github:FinHanceIt/frifri-forge list
  npx github:FinHanceIt/frifri-forge add <plugin> [--dir <path>] [--force]
  npx github:FinHanceIt/frifri-forge add --all

Native (recommended), inside Claude Code:
  /plugin marketplace add FinHanceIt/frifri-forge
  /plugin install <plugin>@frifri-forge`);
}
