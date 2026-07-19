# Frequency protocols — WaveForge shared brain

The science layer. Every protocol the team produces is built from this file. When in doubt, prefer gentle, evidence-honest choices over dramatic ones.

## How binaural beats actually work
- Play two pure tones, one in each ear, at slightly different frequencies. The brain perceives a third "beat" equal to the **difference**: `beat = |f_right − f_left|`. Example: L = 200 Hz, R = 204 Hz → a **4 Hz** binaural beat.
- The beat is a **neural illusion** created in the brainstem from the interaural difference — it is NOT an acoustic beat in the air. Therefore binaural beats **require stereo separation and headphones**.
- **Carrier (base) frequency** = the audible pitch both tones sit around. **Beat frequency** = the small difference that targets a brain state.
- **Frequency-following response (FFR):** brain rhythms tend to drift toward the beat frequency. This is the proposed entrainment mechanism (evidence is mixed — see `safety-and-claims.md`).

### Alternatives when headphones aren't guaranteed
- **Isochronic tones:** a single tone switched on/off at the target rate. Works on speakers, no headphones needed, often stronger entrainment but more "obvious". Offer for focus/daytime tracks.
- **Monaural beats:** the two tones are summed *before* playback, so the beat exists acoustically. Speaker-friendly, milder.
- Default to **binaural** for headphone listeners (sleep, meditation); offer **isochronic** as a speaker alternative for focus/content.

## Brainwave bands → states → target beat frequency
| Band | Range (Hz) | Mental state | Use for |
|------|-----------|--------------|---------|
| Delta | 0.5–4 | Deep dreamless sleep, restoration | Deep sleep, long naps |
| Theta | 4–8 | Deep meditation, drowsiness, REM, creativity, hypnagogia | Meditation, deep relaxation, falling asleep, creative flow |
| Alpha | 8–12 | Relaxed alertness, calm, light meditation | Relaxation, anxiety relief, wind-down, light focus |
| Beta | 13–30 | Alert, active thinking, concentration | Focus, study, work (prefer **low beta 13–16** for calm focus) |
| Gamma | 30–50 (esp. **40**) | Peak focus, high-level cognition, binding attention | Intense focus, deep work, "in the zone" |

Notes:
- Band edges vary slightly by source; treat them as soft boundaries.
- **High beta (20–30 Hz)** can feel jittery / anxious for some — reach for it only on request.
- **40 Hz gamma** is the single most-studied focus frequency.

## Carrier frequency guidance
- Binaural perception is strongest with carriers roughly **200–500 Hz**. Below ~200 Hz tones get muddy and reproduce poorly on small speakers/earbuds; above ~1000 Hz the binaural illusion weakens.
- Suggested carriers by purpose (warm = lower, brighter = higher):
  - Delta / sleep: **100–180 Hz** (warm, non-fatiguing)
  - Theta / meditation: **140–220 Hz**
  - Alpha / relax: **180–280 Hz**
  - Beta / focus: **200–340 Hz**
  - Gamma / deep work: **240–400 Hz**
- Keep the carrier **constant** (or drifting only very slowly). Precision lives in the **beat** difference, not the carrier.
- Avoid carriers below ~80 Hz (poor reproduction, can feel oppressive).
- Pick a carrier near a musical pitch so the Sound Designer can tune pads to it (see `sound-design-guide.md`). E.g. 220 Hz ≈ A3, 196 Hz ≈ G3, 261.6 Hz ≈ C4.

## The session arc (the "journey")
Brains follow **gradual** change better than a jump. A good session ramps in, holds, and exits deliberately. Express the arc as control points of `time → beat`:

1. **Induction / ramp-in (2–5 min):** start near the listener's likely current state (often alpha ~10 Hz) and glide toward the target.
2. **Target hold:** sustain the target beat for the bulk of the session.
3. **Exit — depends on goal:**
   - **Sleep:** stay low (theta→delta) and **fade to silence** — never wake them.
   - **Focus / energize:** ramp **up** toward beta in the last 1–2 min to leave them alert.
   - **Meditation / relax:** glide gently back to alpha (~10 Hz) before ending so they return softly.

## Ready-made protocols (starting points — adapt, don't worship)
Format: carrier @ schedule `time:beat → …` · bed · length.

- **Deep Sleep (delta):** 120 Hz · `0:10 → 5m:6 → 12m:2.5 → hold → fade` · brown noise + warm low pad · 45–90 min.
- **Power Nap:** 140 Hz · `0:10 → 3m:5 → 18m:5 → 20m:10` (gentle wake) · soft pad · 20 min.
- **Calm / Anxiety Relief (alpha):** 200 Hz · `0:12 → 4m:10 → hold 10` · light rain + soft pad · 15–30 min.
- **Deep Meditation (theta):** 150 Hz · `0:10 → 6m:6 → hold 6 → exit 10` · pad + distant nature · 20–30 min.
- **Focus / Study (low beta):** 220 Hz · `0:10 → 3m:15 → hold 15` · brown noise, minimal · 25–50 min (Pomodoro-friendly). Offer isochronic alt.
- **Deep Work / Flow (gamma):** 250 Hz · `0:14 → 4m:40 → hold 40` · very minimal bed · 25–50 min.
- **Creative Flow (theta–alpha border):** 180 Hz · `0:10 → 5m:7.5 → hold 7.5` · airy pad · 20–40 min.

## Production defaults & hard rules
- **True stereo**, sample rate **44.1 kHz**, **16-bit** minimum (24-bit for masters).
- **Beat accuracy is non-negotiable** — the Mastering & QC agent must confirm the rendered beat with an FFT (target vs measured, tolerance ±0.1 Hz).
- **Protect the binaural effect:** keep the two carriers cleanly separated L/R. No stereo-widening, no reverb, no bus processing that bleeds one carrier into the other channel (it kills the illusion). Reverb belongs on pads/textures only.
- **Loudness:** gentle. Master ≈ **−16 LUFS** for general content, **−20 LUFS** for sleep tracks; true-peak **≤ −1 dBTP**.
- Any target beat **below 10 Hz** or any strongly pulsed/isochronic content triggers the **safety gate** in `safety-and-claims.md`.
