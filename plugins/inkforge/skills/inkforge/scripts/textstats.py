#!/usr/bin/env python3
"""
textstats.py — real, dependency-free human-voice metrics for InkForge.

Used by voice-editor (to check its de-AI pass landed) and authenticity-qc
(final read). Computes the quantitative signals that separate human prose from
generic AI prose: sentence-length variance (burstiness), lexical diversity,
AI-transition density, AI-phrase hits, and a punctuation profile. EN + RO aware.

Two modes:
  python3 textstats.py draft.txt              -> metrics for one text (JSON)
  python3 textstats.py voiceA.txt voiceB.txt  -> metrics for both + a
                                                 voice_distance score, to check
                                                 two cast voices are actually
                                                 distinct (criterion: distinct
                                                 personalities per assignment).
  python3 textstats.py -                       -> read one text from stdin

These are SIGNALS, not proof, and never a claim of being "undetectable".
Short texts (<300 words) are unreliable — the script flags this.
"""
import sys, re, json, math
from collections import Counter

EN_TRANSITIONS = {
    "moreover","furthermore","additionally","however","therefore","thus",
    "consequently","nevertheless","nonetheless","hence","accordingly",
    "indeed","notably","importantly","ultimately","overall","subsequently",
    "in addition","in conclusion","that said","it is worth noting",
    "it's worth noting","on the other hand","as a result","for instance",
}
RO_TRANSITIONS = {
    "de asemenea","în plus","prin urmare","totodată","astfel","așadar",
    "în concluzie","pe de altă parte","de exemplu","în consecință",
    "cu toate acestea","totuși","în primul rând","în al doilea rând",
    "merită menționat","este important de menționat",
}
AI_PHRASES_EN = [
    "delve into","it's worth noting","in today's fast-paced world","crucial role",
    "pivotal role","navigate the complexities","a testament to","underscores the importance",
    "rich tapestry","ever-evolving","in conclusion","it is important to note",
    "plays a crucial role","when it comes to","at the end of the day","game-changer",
]
AI_PHRASES_RO = [
    "merită menționat","este important de menționat","în lumea de azi",
    "joacă un rol crucial","un rol esențial","în concluzie","la sfârșitul zilei",
    "are sens","în termeni de","într-o lume în continuă schimbare",
]

def split_sentences(text):
    parts = re.split(r"(?<=[.!?…])\s+|\n+", text.strip())
    return [p.strip() for p in parts if p.strip()]

def words(text):
    return re.findall(r"[A-Za-zĂÂÎȘȚăâîșț]+", text)

def mean(xs):
    return sum(xs)/len(xs) if xs else 0.0

def stdev(xs):
    if len(xs) < 2:
        return 0.0
    m = mean(xs)
    return math.sqrt(sum((x-m)**2 for x in xs)/(len(xs)-1))

def metrics(text):
    sents = split_sentences(text)
    toks = [w.lower() for w in words(text)]
    n_words = len(toks)
    n_sents = len(sents)
    slens = [len(words(s)) for s in sents] or [0]

    types = set(toks)
    ttr = len(types)/n_words if n_words else 0.0
    hapax = sum(1 for _, c in Counter(toks).items() if c == 1)
    hapax_ratio = hapax/n_words if n_words else 0.0

    low = text.lower()
    trans_hits = sum(low.count(t) for t in EN_TRANSITIONS) + sum(low.count(t) for t in RO_TRANSITIONS)
    trans_density = trans_hits/n_sents if n_sents else 0.0
    ai_phrase_hits = {p: low.count(p) for p in (AI_PHRASES_EN + AI_PHRASES_RO) if low.count(p) > 0}

    sl_mean = mean(slens)
    sl_sd = stdev(slens)
    burstiness = (sl_sd/sl_mean) if sl_mean else 0.0
    short = sum(1 for x in slens if x <= 6)
    long_ = sum(1 for x in slens if x >= 25)

    punct = {
        "em_dash": text.count("—"), "semicolon": text.count(";"),
        "colon": text.count(":"), "exclaim": text.count("!"),
        "question": text.count("?"), "parens": text.count("("),
        "ellipsis": text.count("…") + text.count("..."),
    }
    avg_word_len = mean([len(w) for w in toks]) if toks else 0.0

    return {
        "word_count": n_words,
        "sentence_count": n_sents,
        "sentence_len_mean": round(sl_mean, 2),
        "sentence_len_stdev": round(sl_sd, 2),
        "burstiness_cv": round(burstiness, 3),
        "short_sentences_<=6w": short,
        "long_sentences_>=25w": long_,
        "type_token_ratio": round(ttr, 3),
        "hapax_ratio": round(hapax_ratio, 3),
        "avg_word_len": round(avg_word_len, 2),
        "transition_density_per_sentence": round(trans_density, 3),
        "ai_phrase_hits": ai_phrase_hits,
        "punctuation": punct,
        "reliability": ("LOW — under 300 words, weak signal" if n_words < 300 else "OK — 300+ words"),
    }

GUIDE = {
    "burstiness_cv": "≳0.5 leans human; ≲0.3 leans uniform/AI (rough)",
    "transition_density": ">0.4/sentence suggests AI scaffolding — thin it",
    "ai_phrase_hits": "any hit is a flag — the voice-editor should have cut these",
    "ttr": "very low TTR + low hapax = flat, predictable lexis",
    "note": "Signals only. Never a claim of 'undetectable'. See references/ai-tells-checklist.md.",
}

def voice_distance(a, b):
    keys = ["sentence_len_mean","sentence_len_stdev","burstiness_cv",
            "type_token_ratio","avg_word_len","transition_density_per_sentence"]
    scale = {"sentence_len_mean":10.0,"sentence_len_stdev":6.0,"burstiness_cv":0.3,
             "type_token_ratio":0.15,"avg_word_len":1.2,"transition_density_per_sentence":0.3}
    d = 0.0
    deltas = {}
    for k in keys:
        diff = (a[k]-b[k]) / scale[k]
        deltas[k] = round(a[k]-b[k], 3)
        d += diff*diff
    dist = round(math.sqrt(d/len(keys)), 3)
    verdict = ("DISTINCT — the two voices differ measurably" if dist >= 0.6
               else "BORDERLINE — recast on more dials" if dist >= 0.35
               else "TOO SIMILAR — same writer in two hats; re-cast the voice")
    return {"voice_distance": dist, "verdict": verdict, "per_metric_delta": deltas}

def main():
    args = sys.argv[1:]
    if not args:
        print("usage: textstats.py <file|-> [file2]", file=sys.stderr); sys.exit(1)
    def read(src): return sys.stdin.read() if src == "-" else open(src, encoding="utf-8", errors="ignore").read()
    if len(args) == 1:
        report = metrics(read(args[0])); report["reading_guide"] = GUIDE
        print(json.dumps(report, ensure_ascii=False, indent=2)); return
    a, b = metrics(read(args[0])), metrics(read(args[1]))
    out = {"text_A": a, "text_B": b, "distinctiveness": voice_distance(a, b), "reading_guide": GUIDE}
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
