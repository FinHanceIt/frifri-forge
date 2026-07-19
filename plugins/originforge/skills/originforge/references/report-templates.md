# Report Templates — Originality Report & Revision Report

The Director assembles these. Keep them concise and honest. Bands, not fake precision. Deliver in RO/EN per the Brief.

## Originality Report (DETECT / VERIFY mode)
```
ORIGINALITY REPORT — <title/snippet> · <lang> · <word count>

PROVENANCE: <as stated by user / integrity verdict>

AI-LIKELIHOOD: <Low | Lean-human | Mixed | Lean-AI | High>
  Why: <3-5 strongest reasons, tied to real tells>
  Metrics: burstiness <n>, sentence-len mean/stdev <n/n>, TTR <n>, transition density <n>
  Flagged passages: <quote the 1-3 most AI-reading spans>
  Confidence: <high/med/low> — <note short-text / ESL / technical caveats>

SIMILARITY / PLAGIARISM:
  Overlap: <none / minor / notable> vs <web/sources>
  Matches: <passage → source/URL>, marked [cited-OK] or [uncredited-RISK]
  Caveat: web-view only; closed corpora (Turnitin) not visible here

ENGINE-MIRROR (likely reads, ranges — not guarantees):
  Perplexity-based (GPTZero/Turnitin-style): <range + why>
  Classifier-based (Originality.ai/Pangram-style): <range + why>
  Plagiarism (Turnitin/Copyscape-style): <range + why>
  Honesty: detectors disagree and carry real false-positive rates; this is an estimate.

VERDICT: <one honest paragraph>
NEXT ACTION: <single recommended step>
```

## Revision Report (REVISE / HUMANIZE mode)
```
REVISION REPORT — <title> · <lang>

INTEGRITY: <OWN | AI-ASSISTED-OWN | LICENSED> (Gate 0 passed)

WHAT CHANGED & WHY:
  - <move> → <effect> (e.g. raised burstiness; cut connective scaffolding; added real specificity)
  - meaning preserved: <yes + how checked>
  - voice preserved: <yes + audience fit>
  - sources: <transformed + cited, list>

QC RE-SCAN (residual, honest):
  AI-likelihood now: <band> (was <band>) — <why; never "0%/undetectable">
  Similarity now: <band>
  Residual risk: <plainly stated>

DRAFT: <the revised text, or pointer>
NEXT ACTION: <single step — e.g. "your review at Gate 2">
```

## Tone rules for both
- Lead with the answer, then the reasons.
- Every number carries a caveat; every match carries a source.
- Never output a banned claim (see `integrity-policy.md`).
- End with exactly one next action.
