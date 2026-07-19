# Detector Landscape — the market map (2025-26)

The reference for `engine-mirror`. Use it to estimate what real tools would likely report — and to stay honest about how unreliable they are. Accuracy figures below are **vendor- or reviewer-reported and contested**; treat them as rough, not gospel. Always pair an estimate with the uncertainty.

## AI-text detectors

| Tool | Primary signal | Reported accuracy* | False-positive notes | Humanizer-resistant? |
|---|---|---|---|---|
| **Originality.ai** | Trained classifier | ~98-100% (vendor/reviews) | Can flag dense human writing | **Yes** — strong vs spinners/humanizers |
| **Pangram** | Trained classifier | High (reviews) | Newer; fewer independent tests | **Yes** |
| **Winston AI** | Classifier + stats | ~99.98% (vendor) | Lower specificity; flags technical human text | Partial |
| **GPTZero** | Perplexity + burstiness + classifier | ~99% on pure AI (reviews) | Struggles on edited/borderline; flagged a human story 62% AI | Weaker (perplexity-leaning) |
| **Turnitin AI** | Classifier (closed) | 92-100% (vendor) | Real-world FP ~4%+; paused at several universities | Weaker |
| **Copyleaks** | Classifier | ~99% (vendor) | Multilingual; FP on formal writing | Medium |
| **Sapling / ZeroGPT** | Perplexity-leaning | Lower / variable | Higher FP; ZeroGPT notably noisy | Weak |

\*Numbers come from vendor pages and review round-ups (Medium "Most Accurate AI Detectors 2025", GPTZero "9 Best AI Detectors", Originality.ai meta-analysis). They disagree with each other — that disagreement is the point.

**Key split for estimation:** perplexity-leaning tools (GPTZero, Turnitin, ZeroGPT) are mathematically more foolable by paraphrase/humanizers; classifier tools (Originality.ai, Pangram) are much harder to fool. So a text can read "human" on one and "AI" on another — report a **range across families**, not one number.

## Plagiarism / similarity engines

| Tool | What it compares against | How it matches | Blind spot |
|---|---|---|---|
| **Turnitin / iThenticate** | 1.6B+ student papers + web + publications (≈7T matches) | 8-12 word phrase fingerprints | Clever paraphrase; closed corpus you can't pre-check |
| **Copyscape** | Public web | Phrase/passage match | Non-web & paywalled sources |
| **Quetext** | Web + its index | "DeepSearch" phrase match + citation aid | Smaller corpus than Turnitin |
| **PlagScan / Grammarly** | Web + databases | Phrase match | Paraphrase, translation |

Critical truth: **similarity ≠ plagiarism.** A properly quoted+cited passage still shows as a match; a cleverly paraphrased uncredited passage may show **nothing**. The score is a pointer for human judgment, not a verdict. (Turnitin's own guidance says exactly this.)

## "Humanizers" (what they claim vs reality)
Undetectable AI, QuillBot, StealthGPT, HIX/Phrasly, BypassGPT, GPTHuman. They rewrite AI text with transformer models to raise "human" scores.

- **Claims:** "99% bypass across Turnitin/GPTZero/Originality/Winston/Copyleaks."
- **Reality (independent tests):** inconsistent. StealthGPT scored **46% AI** on an AI sample in one review; Undetectable AI varies by content/detector/mode; **no humanizer is fully undetectable, and a perfect one does not exist** — every honest review ends with "manually polish and proofread."
- **OriginForge's stance:** we don't ship a black-box bypass. We make the user's *own* draft genuinely better (real specificity, burstiness, voice), which is what actually reads human *and* survives the classifier-based detectors that humanizers fail against. We never promise a score.

## The honest reliability box (say this out loud in reports)
- AI detectors carry real **false-positive** risk: the 2023 Stanford study (Liang et al., arXiv 2304.02819) found detectors misflagged **~61%** of non-native-English (TOEFL) essays as AI.
- **Vanderbilt, Michigan State, and Northwestern** disabled Turnitin's AI detector over reliability concerns.
- Short texts (<300 words), technical writing, and heavily-edited text are the least reliable to judge.
- Detectors change monthly; any specific number is a snapshot. Report **bands and reasons**, never false precision.

Sources: medium.com/@jericho.w.blanco (2025 detector tests); gptzero.me/news/best-ai-detectors; originality.ai/blog/ai-detection-studies-round-up; turnitin.com/products/similarity; guides.turnitin.com (similarity score); arxiv.org/pdf/2304.02819 (ESL bias); lawlibguides.sandiego.edu (false positives/negatives); stealthgpt & undetectable independent reviews (twaingpt, gptinf).
