# Handoff contracts — WaveForge shared brain

Teams fail at the seams. Each agent consumes a named artifact and produces the next one. Pass **only** what the next stage needs. Keep all artifacts in one running **Session File**.

## The artifacts (in pipeline order)

### 1. Session Brief — *Studio Director → everyone*
```
intent/state: <relax | focus | sleep | meditation | creative | content>
use_case: <one line: who, when, where listening>
duration_min: <number>
listener_notes: <beginner? sensitive? headphones guaranteed?>
platform: <personal | YouTube | Spotify | app | other>
language: <RO | EN | both>
guided_voice: <yes/no — triggers Voice & Script>
safety_profile: <any flags: epilepsy/pregnancy/child/none>
```

### 2. Protocol Spec — *Frequency Architect → Sound Designer, Voice & Script, Render*
```
mode: <binaural | isochronic | monaural>
carrier_hz: <constant carrier>
beat_schedule: [ "time:beat", … ]   # control points, e.g. "0:10","5m:6","12m:2.5"
band_target: <delta|theta|alpha|beta|gamma + why>
arc: <induction / hold / exit description>
samplerate: 44100   bitdepth: 16|24
rationale: <1–3 lines, evidence-honest>
safety_flags: <beat<10Hz? pulsed? → yes/no>
```

### 3. Sound Design Spec — *Sound Designer → Render*
```
noise: <none|pink|brown|white> @ level_db
pads: <key, mood, level_db>
nature: <texture, level_db> | none
mix: { carrier_db, noise_db, pad_db, nature_db }
stereo_rules: <confirm carriers isolated; reverb only off-carrier>
loop/fade: <fade_in_s, fade_out_s, loop strategy>
```

### 4. Voice Script + Voice Spec — *Voice & Script → Render* (only if guided_voice = yes)
```
script: <full text, in the target language(s)>
cue_sheet: [ "time → line / pause" ]   # aligned to the arc
voice_spec: <gender/age feel, pace WPM, warmth, accent, TTS or human>
mix_note: <where speech sits; ducking; silence gaps>
```

### 5. Render Package — *Render Engineer → Mastering & QC*
```
files: [ paths to rendered .wav ]
render_log: <exact params used: carrier, schedule, noise, fades, samplerate, peak>
variants: <binaural / isochronic / lengths>
```

### 6. QC Report — *Mastering & QC → Studio Director*
```
measured_beat_hz: <FFT result vs target, per segment>
loudness_LUFS: <value vs target>   true_peak_dBTP: <value>
stereo_check: <carriers isolated? pass/fail>
safety_gate: <checklist pass/fail with notes>
verdict: PASS | FIX (with specific fixes routed back)
```

### 7. Release Kit — *Release Producer → Fri* (only for content/brand)
```
title: <RO/EN>   description: <hedged, claims-checked>
tags/keywords: […]
platform_specs: <format, art size, length, loudness for the platform>
cover_concept: <one paragraph art direction>
disclaimer: <RO/EN from safety-and-claims.md>
```

## Loop-back rule
If **QC Report.verdict = FIX**, the Studio Director routes the specific fix to the owning agent (wrong beat → Render; too loud → Mastering; unsafe copy → Release/Voice), then re-runs QC. **Nothing ships on a FIX.**
