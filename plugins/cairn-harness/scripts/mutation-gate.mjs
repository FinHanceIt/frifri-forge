#!/usr/bin/env node
// Cairn L2 — Assertion Integrity gate.
// Mutation-tests the source files changed since a base ref (diff-scoped, so it is
// affordable in a loop), compares the score to a stored baseline, and emits a verdict
// the AGENT CANNOT AUTHOR. No LLM anywhere in here — a number vs a number.
//
// Proven behaviour: it FIRES when a diff reduces what is actually tested (a deleted or
// gutted test that loses coverage). It correctly STAYS SILENT when a test is weakened
// but the behaviour is still covered elsewhere (no hole opened). It is a COVERAGE-LOSS
// detector, not a tamper detector.
//
// Usage:
//   node scripts/mutation-gate.mjs                  # shadow (default): record, never block
//   node scripts/mutation-gate.mjs --enforce        # exit 1 on a real regression
//   node scripts/mutation-gate.mjs --set-baseline   # store the current score
//   node scripts/mutation-gate.mjs --since <ref>    # mutate files changed since <ref> (default HEAD)
//   node scripts/mutation-gate.mjs --all            # mutate everything under SRC_GLOBS (for baselining)
//
// Configure SRC_GLOBS below for your repo layout. Exit: 0 pass/shadow · 1 blocked (--enforce) · 2 tooling error
import { execSync } from "node:child_process";
import { readFileSync, writeFileSync, existsSync, mkdirSync } from "node:fs";

const EPSILON = 3.0;                                   // allowed wobble (points). Tune from shadow data.
const SRC_DIRS = ["src", "lib", "core", "app", "adapters"]; // where source lives; edit per repo
const REPORT = "reports/mutation.json";
const BASE = ".cairn/mutation-baseline.json";
const argv = process.argv.slice(2);
const enforce = argv.includes("--enforce");
const setBase = argv.includes("--set-baseline");
const all = argv.includes("--all");
const since = (() => { const i = argv.indexOf("--since"); return i >= 0 && argv[i + 1] ? argv[i + 1] : "HEAD"; })();

const isSrc = (f) =>
  /\.(ts|tsx|js|jsx|mjs)$/.test(f) && !/\.(spec|test)\./.test(f) && !f.endsWith(".d.ts") &&
  SRC_DIRS.some((d) => f === `${d}` || f.startsWith(`${d}/`));

function changedSource() {
  try {
    return execSync(`git diff --name-only ${since}`, { encoding: "utf8" })
      .split("\n").map((s) => s.trim()).filter(isSrc);
  } catch { return []; }
}

const mutate = all ? SRC_DIRS.map((d) => `${d}/**/*.{ts,tsx,js,jsx,mjs}`) : changedSource();
if (!all && mutate.length === 0) {
  console.log(JSON.stringify({ gate: "L2", verdict: "SKIP",
    human_note: `No source files changed since ${since} — nothing to check.` }, null, 2));
  process.exit(0);
}

const cfg = {
  $schema: "./node_modules/@stryker-mutator/core/schema/stryker-schema.json",
  packageManager: "npm", testRunner: "vitest",
  reporters: ["json"], jsonReporter: { fileName: REPORT },
  coverageAnalysis: "off", mutate,
  mutator: { excludedMutations: ["StringLiteral"] },
  concurrency: 4, timeoutMS: 15000,
};
mkdirSync("reports", { recursive: true });
writeFileSync(".stryker.gate.json", JSON.stringify(cfg, null, 2));

try { execSync("npx stryker run .stryker.gate.json", { stdio: "ignore" }); }
catch { console.error(JSON.stringify({ gate: "L2", verdict: "ERROR", reason: "stryker failed to run" })); process.exit(2); }

function scoreFromReport() {
  const r = JSON.parse(readFileSync(REPORT, "utf8"));
  let killed = 0, timeout = 0, survived = 0, nocov = 0;
  for (const f of Object.values(r.files)) for (const m of f.mutants) {
    if (m.status === "Killed") killed++; else if (m.status === "Timeout") timeout++;
    else if (m.status === "Survived") survived++; else if (m.status === "NoCoverage") nocov++;
  }
  const denom = killed + timeout + survived + nocov;
  return { score: denom ? ((killed + timeout) / denom) * 100 : 0, killed, timeout, survived, nocov };
}

const cur = scoreFromReport();
const round = (n) => Math.round(n * 100) / 100;

if (setBase || !existsSync(BASE)) {
  mkdirSync(".cairn", { recursive: true });
  writeFileSync(BASE, JSON.stringify({ score: round(cur.score) }, null, 2));
  console.log(JSON.stringify({ gate: "L2", verdict: "BASELINE_SET", score: round(cur.score), mutated: mutate, ...cur }, null, 2));
  process.exit(0);
}

const baseline = JSON.parse(readFileSync(BASE, "utf8")).score;
const drop = baseline - cur.score;
const failed = drop > EPSILON;
const verdict = failed ? (enforce ? "BLOCK" : "WOULD_BLOCK") : "PASS";

console.log(JSON.stringify({
  gate: "L2-assertion-integrity", mode: enforce ? "enforce" : "shadow",
  verdict, baseline: round(baseline), score: round(cur.score), drop: round(drop),
  epsilon: EPSILON, mutated: mutate, mutants: cur,
  human_note: failed
    ? `Tests weakened: the score dropped ${round(drop)} points (${round(baseline)} -> ${round(cur.score)}) on ${mutate.join(", ")}. Coverage was lost — a test was gutted or deleted.`
    : `Tests hold: score ${round(cur.score)} (baseline ${round(baseline)}). No coverage lost.`,
  exit_code: failed && enforce ? 1 : 0,
}, null, 2));
process.exit(failed && enforce ? 1 : 0);
