# AI-tells checklist — the de-AI spec

This is the operational spec for `voice-editor` (which removes the tells) and
`authenticity-qc` (which checks they're gone). It's Fri's own 8-point list, turned into
detect → fix moves, EN + RO. Some are measurable with `scripts/textstats.py`.

> Honesty first: removing these makes prose **genuinely more human and better written** —
> it does NOT make it "undetectable". Never claim or imply that. Detectors are noisy both
> ways; we write well, we don't game a scanner.

## 1. Predictable phrasing (low perplexity)
AI picks the statistically most-likely next word, so phrasing feels pre-chewed.
- Tell: clichés, the expected adjective, the obvious metaphor, filler that adds no information.
- Fix: choose the second-best (truer) word, not the first. Concrete over abstract. Cut any
  clause a reader could predict from the previous one. Surprise at the level of *fact*, not
  just vocabulary.

## 2. Flat burstiness (no sentence-length variance)
Humans swing: a 3-word jab next to a 35-word coil. AI runs an even 15–20 every time.
- Measure: `burstiness_cv` ≳0.5 leans human; ≲0.3 is a flag.
- Fix: plant short sentences. Allow a fragment. Then let one sentence run long and earn it.
  Vary paragraph length too — a one-line paragraph is allowed.

## 3. Uniform style / register
AI holds one tone and formality from first word to last.
- Tell: same temperature throughout; no gear changes.
- Fix: let register drift with the content — tighter when it matters, looser in the
  connective tissue, a sudden plain line after an ornate one. The piece should breathe.

## 4. Repeated patterns
The same sentence opener, the same "X, but Y" shape, the same three-beat list, reused.
- Tell: every paragraph opens with the subject; tricolons everywhere; parallelism on a timer.
- Fix: vary openings (start on a verb, a clause, a name, a question, "And"). Use a list of
  two or four, not always three. Never run the same rhetorical move twice in a row.

## 5. Over-orderly structure
Intro → three perfectly balanced points → tidy conclusion that restates the intro.
- Tell: symmetry you could set a watch by; every section the same weight; a bow on top.
- Fix: deliberate asymmetry. Sections of uneven length. Start in the middle of things. Let
  one point dominate. End on an image, a question, or an implication — not a recap. A real
  digression that pays off is more human than a clean skeleton.

## 6. Missing concrete / lived specificity
Generic, sourceless, true-of-anything prose with no real detail.
- Tell: "studies show", "many people", "in various ways", no names/numbers/dates/textures.
- Fix: one real, checkable specific beats ten adjectives — a name, a number, a date, a
  sensory detail, a genuine opinion. NEVER fabricate facts to sound human: where the author
  must supply a real detail, mark `[author: add X]`. (Fiction invents *within its world*;
  it does not fake citable facts.)

## 7. Unnatural consistency
Too clean. No digressions, no self-correction, no rough edge, identical quality throughout.
- Tell: a machine's evenness — nothing tried and abandoned, nothing risked.
- Fix: allow controlled imperfection — an aside, a second thought ("or maybe that's wrong"),
  a sentence that doubles back. Let intensity rise and fall. Do NOT inject typos or
  grammatical errors; "human" ≠ "broken". Imperfection is in rhythm and thought, not spelling.

## 8. AI vocabulary
Words and phrases models overuse.
- EN ban-list: moreover, furthermore, additionally, delve, tapestry, testament, crucial,
  pivotal, navigate (fig.), underscore, "it's worth noting", "in conclusion", "in today's
  world", "ever-evolving", "game-changer", "when it comes to", "at the end of the day".
- RO ban-list: de asemenea, în plus, totodată, prin urmare, așadar, crucial, esențial,
  "merită menționat", "este important de menționat", "în concluzie", "în lumea de azi",
  "la sfârșitul zilei", "joacă un rol crucial".
- Measure: `transition_density_per_sentence` >0.4 and any `ai_phrase_hits` are flags.
- Fix: cut the connective or replace with a plain one (and, but, so, still, then) or just a
  full stop. Most "Moreover," sentences read better with the word deleted.

## Don't overcorrect (the failure mode of de-AI editing)
- Don't sprinkle errors, slang, or em-dashes to "seem human" — that's a new tell.
- Don't lose the meaning, the facts, or the author's intent. Voice-editing is surgery, not
  vandalism. If a fix risks the meaning, flag it instead of forcing it.
- The target is *good human writing in this voice*, full stop.
