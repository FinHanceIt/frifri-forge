# Sound design guide — WaveForge shared brain

How to make the track **pleasant for its whole length** without harming the binaural effect. The Sound Designer owns this; the Render Engineer implements it.

## Noise colors (the bed foundation)
- **White** — flat energy, harsh/hissy. Rarely used alone; avoid for sleep.
- **Pink** — equal energy per octave, natural and balanced (rain-like). Default for **relaxation, meditation, light focus**, and for masking environmental noise.
- **Brown (red)** — heavy low end, deep and soothing (distant waterfall/thunder rumble). Best for **deep sleep and deep focus**; masks low-frequency distractions.
- Default picks: Sleep → brown · Focus → brown or pink · Relax/Meditation → pink.

## Ambient layers
- **Pads / drones:** sustained, slowly evolving, tuned to the carrier's key (see harmony). Provide warmth and hide the "test-tone" character of pure carriers.
- **Nature textures:** rain, ocean swells, forest, stream, soft wind. Keep them **transient-free** for sleep (no thunder cracks, no bird startles). Loop seamlessly.
- **Optional chimes/bells:** only for meditation cue points, never during sleep hold.

## Harmony (make the carrier musical)
- Treat the carrier as a root note and tune pads to a **consonant** key so nothing beats against the carrier.
- Reference pitches: 196 Hz ≈ G3 · 220 Hz ≈ A3 · 246.9 Hz ≈ B3 · 261.6 Hz ≈ C4.
- Prefer simple consonant intervals (root, fifth, octave) and minor/major pads matching the mood (minor = introspective/sleep, major = calm/uplift).

## Mix levels (starting point)
- Carrier tones: clear and present but **never piercing** — they carry the effect, keep them clean.
- Noise bed: roughly **−12 to −18 dB** under the tones.
- Pads: subtle, **−15 to −22 dB**, supporting not masking.
- Nature: −18 to −24 dB, background.
- Voice (if guided): sits **on top**, clearly intelligible, tones/bed duck ~3–6 dB under speech.

## Stereo rules (protect the binaural effect — critical)
- The two carriers must stay **cleanly in their own channels** (L = carrier, R = carrier + beat). 
- **No** stereo wideners, **no** reverb, **no** chorus, **no** bus glue on the carriers — anything that bleeds one carrier into the other channel destroys the binaural illusion.
- Pads, nature, and voice **may** be stereo/reverberant and panned wide — just keep them off the carrier bus.
- For **isochronic** versions this rule relaxes (mono-compatible by design).

## Anti-fatigue & looping
- Use **gentle carriers** and **slow** evolution; nothing should grab attention during a hold.
- Avoid abrupt level changes; automate everything with smooth ramps.
- Loop beds with **equal-power crossfades** (no clicks, no audible seam).
- Always **fade in/out** (≥3 s; longer for sleep) to avoid clicks and startle.

## Per-use-case recipes
- **Sleep:** brown noise + warm low minor pad + very slow evolution + long fade-out to silence.
- **Focus/Study:** brown or pink noise, minimal/no melodic content, steady, no surprises; optional isochronic.
- **Meditation:** soft pad + distant nature + optional sparse chimes at section changes.
- **Relax/Anxiety:** gentle rain + soft pad in a warm key, alpha beat.
- **Content/brand:** as above but polished — intro/outro consideration, consistent series palette, cover-art-friendly mood.
