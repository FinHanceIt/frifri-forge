# Handoff Contracts — the Originality Brief & named artifacts

Every agent consumes a named artifact and produces a named artifact. The Director keeps one **Session File** that accumulates them. Pass each agent only what it needs.

## The Originality Brief (Director fills this first)
```
text:            <the text under review, or a pointer to the file>
language:        RO | EN | both
provenance:      original-by-Fri | ai-assisted-by-Fri | draws-on-sources | unknown
  └ sources:     <list any source texts/URLs the draft used, if known>
goal:            detect | defend | revise | full
audience:        <who reads it — e.g. parents of 3-6yo, US SaaS buyers, general>
voice:           <brand/voice notes; for kids' books: age band + reading level>
platform:        <book, blog, KDP, social, academic, client deliverable>
constraints:     <length limits, must-keep phrases, deadline, tone>
```
Ask only what you genuinely cannot infer. Default language = mirror the user.

## Artifacts produced/consumed

| Agent | Consumes | Produces |
|---|---|---|
| `integrity-gate` | Brief (provenance) | **Integrity Verdict** (OWN / AI-ASSISTED-OWN / LICENSED / THIRD-PARTY-UNCLEAR / LAUNDERING + reasoning) |
| `ai-forensics` | text + language | **AI-Forensics Report** (textstats numbers + tell analysis + AI-likelihood band + flagged passages) |
| `plagiarism-scanner` | text + sources | **Similarity Report** (matched passages, sources/URLs, cited-vs-uncredited split, overlap estimate) |
| `engine-mirror` | AI-Forensics + Similarity reports | **Engine-Mirror Report** (per-detector-family estimates + honesty caveat) |
| `humanizer` | text + AI-Forensics Report | **Humanized Draft** + change log |
| `originality-transformer` | draft + sources + Similarity Report | **Transformed Draft** + citation list |
| `voice-keeper` | revised draft + Brief.voice | **Voice-Checked Draft** + voice notes |
| `qc-rescan` | revised draft | **QC Re-Scan Report** (residual AI-likelihood + similarity + meaning/voice preserved) |
| `forge-director` | all of the above | **Originality Report** and/or **Revision Report** + next action |

## Pipelines by mode
- **DETECT:** `ai-forensics` ∥ `plagiarism-scanner` → `engine-mirror` → Originality Report.
- **DEFEND:** `integrity-gate` → `ai-forensics` (explain) → light edits → `qc-rescan`.
- **REVISE:** `integrity-gate` (Gate 0) → `humanizer` → `originality-transformer` (if sources) → `voice-keeper` → `qc-rescan` (Gate 2) → Revision Report.
- **FULL:** DETECT → REVISE → `qc-rescan`.

## Rules of the relay
- Nothing gets rewritten before **Gate 0** (integrity) passes.
- Reports carry their **uncertainty**: bands and ranges, never invented precision.
- Every claim of similarity carries its **source**; every AI-likelihood read carries its **reasons**.
- The Director never silently drops a flagged risk — it surfaces in the final report.
