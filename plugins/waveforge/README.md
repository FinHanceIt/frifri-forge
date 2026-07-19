# WaveForge — binaural & brainwave audio studio

A 7-agent studio that turns an intent — **relax · focus · sleep · meditation · creative · publishable content** — into a finished, headphone-ready audio track. It doesn't just *describe* a track: the Render Engineer synthesises a **real stereo `.wav`** and the QC engineer **verifies the beat with an FFT** before anything ships.

Built for Fri. Reasons in English, delivers listener-facing text in **RO/EN**. Honest, non-medical claims; mandatory safety gate.

## The team
| Agent | Role |
|-------|------|
| **studio-director** | Orchestrator — classifies the request, fills the brief, routes the pipeline, holds the gates. |
| **frequency-architect** | Picks carrier + beat + band and designs the session arc (induction → hold → exit). |
| **sound-designer** | Builds the ambient bed (noise color, pads, nature) so it's pleasant for the whole length. |
| **voice-script-writer** | Writes guided-meditation scripts + cue sheets + voice specs (RO/EN). |
| **render-engineer** | Runs `binaural.py` to produce the real `.wav` (binaural / isochronic / monaural). |
| **mastering-qc** | FFT-verifies the beat, checks loudness/true-peak, runs the safety gate. PASS/FIX. |
| **release-producer** | Titles, descriptions, tags, platform specs, cover concept, disclaimer (claims-checked). |

## Pipeline
```
Brief → Frequency Architect → Sound Designer → [Voice & Script] → ⟦Gate 1: protocol⟧
      → Render Engineer → Mastering & QC ⟦Gate 2: safety⟧ → [Release Producer] → ⟦Gate 3: release⟧ → deliver
```

## Install
Copy the `waveforge` folder into your Claude plugins, or load it from your marketplace. It exposes the `waveforge` skill plus the 7 agents.

## Use it
Just describe what you want:
- "Fă-mi un sunet binaural de 20 de minute pentru relaxare."
- "Make a 45-minute deep-sleep track I can publish on YouTube."
- "What frequency for focus, and render a speaker-friendly version?"
- "10-minute guided breathing meditation in Romanian, with a theta bed."

## Make audio directly (the engine)
`skills/waveforge/scripts/binaural.py` (numpy only):
```bash
pip install numpy --break-system-packages
python binaural.py --carrier 200 --beat 10 --duration 20 --noise pink --noise-db -15 --out calm.wav
python binaural.py --carrier 120 --schedule "0:10,5m:6,12m:2.5,45m:2.5" --noise brown --fade-out 20 --out sleep.wav
python binaural.py --carrier 220 --beat 15 --duration 30 --mode isochronic --noise brown --out focus.wav
```

## The science, honestly
Binaural beats are a **wellness/relaxation aid, not a medical treatment**. Evidence is **emerging and mixed** — some studies show small-to-moderate effects on anxiety, attention, and sleep; others show none; effects vary by person. WaveForge hedges every benefit, bans medical claims, and attaches a disclaimer. Binaural beats need **headphones** (isochronic/monaural work on speakers). Keep volume moderate; not while driving. If you have epilepsy, a heart condition, or are pregnant, talk to a doctor first.

## Structure
```
waveforge/
  .claude-plugin/plugin.json
  skills/waveforge/
    SKILL.md
    references/  frequency-protocols · sound-design-guide · safety-and-claims · handoff-contracts · render-guide
    scripts/binaural.py
  agents/  studio-director · frequency-architect · sound-designer · voice-script-writer · render-engineer · mastering-qc · release-producer
  README.md · CHANGELOG.md
```
