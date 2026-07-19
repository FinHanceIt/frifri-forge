# AI Tells — how detection works & what actually signals AI (EN + RO)

This is the analytical core for `ai-forensics`, `humanizer`, and `qc-rescan`. Read the mechanism first, then the tells. Interpret, never accuse — every read is probabilistic.

## How modern AI detectors actually work
Detectors combine three signal families (none is a lie detector):

1. **Perplexity** — how *predictable* the text is to a language model. AI text tends to be **low-perplexity** (the model wrote exactly the expected next word). Human text makes more surprising choices. Low perplexity → looks AI.
2. **Burstiness** — *variation* in sentence length and complexity across a passage (classic metric: standard deviation of sentence length, plus variance of syntactic complexity). Humans are bursty (mix of long and short); AI is flat and uniform. Low burstiness → looks AI.
3. **Supervised classifiers** — fine-tuned transformers trained on human-vs-AI examples, reading embeddings, POS patterns, rare n-grams, and error signatures. This is what the strongest tools (Originality.ai, Pangram, GPTZero) lean on; classifier-based tools resist paraphrase/humanizer tricks far better than pure-perplexity tools.

Operational consequence: the two things that *most* move a text toward "human" are **higher burstiness** and **higher genuine perplexity through real specificity** — not synonym swaps. See `humanization-playbook.md`.

## Strong tells (these actually correlate with AI)
- **Low burstiness:** sentences clustered around one length, even rhythm, no fragments, no very-short punch lines.
- **Low lexical surprise:** safe, mid-frequency vocabulary; few rare or domain-specific words; everything "fluent but flavorless."
- **Formulaic macro-structure:** intro that restates the prompt → 3 balanced body chunks → "In conclusion" that summarizes; every section the same shape.
- **Connective over-scaffolding:** dense "Moreover, Furthermore, Additionally, In addition, It's worth noting, That said."
- **Balanced-hedge reflex:** "While X, it's also important to consider Y"; "not only… but also"; relentless both-sides symmetry.
- **Generic specificity:** claims with no concrete names, numbers, dates, or lived detail; examples that could apply to anything.
- **Suspicious cleanliness:** zero typos, zero idiosyncrasy, perfectly parallel lists — human drafts have quirks.
- **Listicle reflex & bold-label sentences:** "**Key point:** …" patterns, tidy enumerations where prose was expected.
- **Closing moralizing:** a tidy "Ultimately, …" life-lesson wrap-up.

## Folklore tells (weak on their own — do NOT accuse on these)
- **Em dashes (—):** popularly "the ChatGPT hyphen," but unreliable; many humans (and editors) use them. Weight near zero alone.
- **The word "delve" / "tapestry" / "testament":** real humans use these; only meaningful in *clusters* with other signals.
- **Any single phrase.** Treat single-word/phrase signals as supporting evidence at most, never proof.

## English AI-phrase clusters (signal only in combination)
"delve into", "it's worth noting", "in today's fast-paced world", "plays a crucial/pivotal role", "navigate the complexities", "a testament to", "underscores the importance", "in conclusion", "moreover/furthermore" stacks, "it is important to note that", "rich tapestry", "ever-evolving landscape."

## Romanian AI tells (use with the `romanian-grammar` skill)
RO models default to a *neutral, over-correct, slightly translated* register. Watch for:
- **Anglicisme / calcuri:** "în termeni de", "la sfârșitul zilei", "a face sens" (corect: "a avea sens"), "locație" peste tot, "implementa/livra" pe contexte non-tehnice.
- **Connector clustering:** "De asemenea, În plus, Prin urmare, Totodată, Astfel" la început de propoziție, repetat.
- **Register too flat/formal** for the context; no regionalisme, no oralitate, no colocviale firești.
- **Uniform sentence length** and textbook syntax; lipsa frazelor scurte, eliptice.
- **Over-hedging:** "este important de menționat că", "merită subliniat faptul că", "în concluzie."
- **Diacritice perfecte + zero greșeli** within otherwise generic prose (humans writing fast slip).
- **Safe, mid-frequency lexis;** absence of specific Romanian names, places, sums, dates, lived detail.

## How `ai-forensics` should read a text
1. Run `scripts/textstats.py` for the numbers (sentence-length mean/stdev, burstiness, type-token ratio, hapax %, transition density, punctuation profile).
2. Map numbers → signals (low stdev = low burstiness; low TTR + low hapax = low lexical surprise).
3. Add qualitative tells from the lists above, in the right language.
4. Output an **AI-likelihood band** — `Low / Lean-human / Mixed / Lean-AI / High` — with the 3-5 strongest reasons and the specific passages that drive it.
5. Caveat explicitly: short texts (<300 words) are unreliable; ESL/edited/technical human writing often reads "AI" (false positives ~60% on ESL essays in the 2023 Stanford study); this is an estimate, not proof.

Sources: dev.to "How AI Text Detection Works" (perplexity/burstiness/classifiers); GPTZero "How Do AI Detectors Work"; NetusAI stylometry; Liang et al. 2023 (arXiv 2304.02819, GPT detectors biased against non-native writers); Rolling Stone / Yahoo on em-dash folklore.
