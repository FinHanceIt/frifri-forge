# Changelog

## v1.0.0 — 2026-06-17
Initial release. 7-agent binaural & brainwave audio studio.
- Orchestrator skill `waveforge` + 7 agents (studio-director, frequency-architect, sound-designer, voice-script-writer, render-engineer, mastering-qc, release-producer).
- Shared brain: frequency-protocols, sound-design-guide, safety-and-claims, handoff-contracts, render-guide.
- Real audio engine `scripts/binaural.py` (numpy-only): binaural / isochronic / monaural, gliding beat schedules, pink/brown/white noise beds, pad drone, fades, 16/24-bit WAV, reproducible seeds, built-in FFT beat read.
- Pipeline with 3 human gates (protocol · safety/QC · release). FFT beat verification (±0.1 Hz). Honest non-medical claims with RO/EN disclaimers and a mandatory safety gate.
- Engine tested in-sandbox (2026-06-17): a constant-beat render reports an FFT-measured beat of **exactly 10.00 Hz** (target 10 Hz); gliding schedules and isochronic mode produce valid stereo WAVs. Ships a built-in FFT self-check + a QC verification snippet; golden tests 5–8 in `golden-tests