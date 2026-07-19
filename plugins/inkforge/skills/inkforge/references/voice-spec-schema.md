# Voice-spec schema — the personality engine

`voice-caster` fills this into a **Voice Card** for every assignment. This is what makes
"a different personality each time" real and *measurable*, not just a label like "friendly".
A weak voice = an AI tell (uniform, generic). A strong, specific voice is the single
biggest lever on sounding human.

## The Voice Card (fill every dial)
- **Persona** — who is writing? Age-ish, background, what they do, their relationship to
  this topic, why they care or are tired of it. One vivid sentence, not a résumé.
- **Stance** — their point of view / the axe they grind. What do they believe about this
  that colors every line? What are they a little wrong or biased about? (Bias = humanity.)
- **Rhythm** — sentence-length habit (clipped / flowing / mixed-jagged), paragraph shape,
  pace. Give a target: e.g. "mostly short, one long sentence per paragraph that spirals."
- **Lexicon** — register (street ↔ academic), domain words they reach for, 3–5 favorite
  words, 3–5 words they would NEVER use, any regional/era flavor.
- **Syntax habits** — fragments? run-ons? parentheticals? em-dashes? starts sentences with
  "And/But"? rhetorical questions? lists? present tense? Choose 2–3, not all.
- **Tics & signature moves** — 2–3 recurring moves: a kind of image they return to, a verbal
  habit, how they open, how they land an ending. These are the fingerprint.
- **Temperature** — emotional heat, humour, irony, warmth or distance, how much they show.
- **Won't-do list** — anti-patterns that break character (e.g. "never sentimental", "never
  uses exclamation marks", "never explains the joke").
- **Cadence sample** — 2–4 lines written *in the voice* as a tuning fork `the-pen` matches.
  This is the most important field. Make it unmistakable.

## Distinctiveness rule
When a voice should differ from a previous/reference one, it must differ on **at least 3
dials** — and one of them must be rhythm OR lexicon (the dials that move the numbers).
`authenticity-qc` can confirm with `textstats.py file1 file2` → `voice_distance ≥ 0.6`.

## Match the voice to the job
Voice serves the brief: a children's-book narrator, a hard-boiled noir PI, a dry policy
essayist, a breathless DTC founder, a grieving memoirist. The format and audience constrain
the voice; within that, make a *specific person*, not a register.

## Worked contrast (two voices, same topic: "morning coffee")
- **Voice A — tired lighthouse keeper, 60s.** Rhythm: short, plain, one long melancholy
  spiral per paragraph. Lexicon: weather, sea, small domestic nouns; never a brand name.
  Tic: understatement, treats routine as quiet ritual. Sample: *"He made coffee. It was bad.
  He drank it anyway, because forty years is forty years."*
- **Voice B — over-caffeinated startup founder, 28.** Rhythm: jagged, fragments, ALL the
  energy, em-dashes. Lexicon: metrics, "ship", "insane", brand names. Tic: hype, then a
  self-aware aside. Sample: *"Third espresso. Don't judge. The roadmap doesn't ship itself —
  and yeah, I know how that sounds."*

Same subject, two unmistakable humans. That's the bar.

## RO/EN
Cast the voice in the target language's own idiom — a Romanian voice is not a translated
English one. For RO, hand off through `romanian-grammar`. Note dialect/register choices
(e.g. neologisms vs. neaoș) on the Lexicon dial.
