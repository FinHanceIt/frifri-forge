# Render guide — WaveForge shared brain

The Render Engineer owns this. The generator is `../scripts/binaural.py` (relative to this skill). Only dependency is **numpy**; WAV is written with the standard library.

## Setup
```bash
pip install numpy --break-system-packages    # only dependency
```
If the plugin path is awkward to locate at runtime, the Render Engineer may copy `binaural.py` into the working directory or recreate it — it is self-contained.

## Generate a track
```bash
python binaural.py --carrier 200 --beat 10 --duration 20 \
    --noise pink --noise-db -15 --out calm_alpha.wav
```

Key flags:
| Flag | Meaning |
|------|---------|
| `--carrier` | constant carrier Hz (see frequency-protocols.md) |
| `--beat` | constant beat Hz |
| `--beat-start / --beat-end` | linear glide across the whole track |
| `--schedule "0:10,5m:6,20m:2.5"` | control points `time:beat`; beat is interpolated & phase-integrated (smooth glide) |
| `--duration` | minutes; if longer than the schedule, the last beat is held |
| `--mode` | `binaural` (headphones), `isochronic` (speakers), `monaural` (speakers) |
| `--noise` | `none / white / pink / brown` + `--noise-db` (level vs tones) |
| `--pad` | adds a soft sub-octave drone (`--pad-db`) |
| `--fade-in / --fade-out` | seconds (use long fade-out for sleep) |
| `--peak-dbfs` | normalisation peak (default −3) |
| `--samplerate / --bitdepth` | default 44100 / 16 (use 24 for masters) |
| `--seed` | reproducible noise |

The script prints a render log and, for binaural mode, an **FFT-measured beat** for a quick sanity check.

## Translate a Protocol Spec → command
- `mode` → `--mode`
- `carrier_hz` → `--carrier`
- `beat_schedule` (list of `time:beat`) → `--schedule` (join with commas)
- `samplerate/bitdepth` → `--samplerate/--bitdepth`
- Sound Design Spec `noise` + `mix.noise_db` → `--noise/--noise-db`; `fade` → `--fade-in/--fade-out`; pad → `--pad/--pad-db`

Always echo the exact command into the **render_log** of the Render Package.

## QC verification (Mastering & QC agent)
Confirm the realised beat per segment with an independent FFT (don't trust the render blindly):
```python
import numpy as np, wave
w = wave.open("calm_alpha.wav", "rb"); sr = w.getframerate()
raw = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype(float)
L, R = raw[0::2], raw[1::2]
win = min(sr * 60, len(L)); start = max(0, len(L)//2 - win//2)
sl = slice(start, start + win)
f = np.fft.rfftfreq(win, 1/sr); band = f >= 50        # ignore low-freq noise bed
hann = np.hanning(win)
def peak(x):
    m = np.abs(np.fft.rfft(x[sl] * hann)); m[~band] = 0
    return f[int(np.argmax(m))]
pL, pR = peak(L), peak(R)
print("carrier L:", round(pL, 2), "carrier R:", round(pR, 2), "beat:", round(abs(pR - pL), 3))
```
Pass if `|measured − target| ≤ 0.1 Hz` and `carrier L ≈ carrier`. Also confirm L and R carriers differ (stereo isolation intact). For 24-bit files read with `dtype="<i4"`-style unpacking instead.

### Loudness (optional, if ffmpeg present)
```bash
ffmpeg -i calm_alpha.wav -af ebur128 -f null -   # read Integrated LUFS / True Peak
```
Targets: ≈ −16 LUFS general, −20 LUFS sleep; true-peak ≤ −1 dBTP.

### Export to MP3/FLAC for delivery (optional, if ffmpeg present)
```bash
ffmpeg -i calm_alpha.wav -b:a 320k calm_alpha.mp3
ffmpeg -i calm_alpha.wav calm_alpha.flac
```

## Render rules
- Keep carriers isolated L/R — never run reverb/stereo-widening over the carrier bus (kills the binaural effect). Bed/pad processing is fine.
- Long renders are large: 60 min stereo 16-bit ≈ 600 MB WAV. Offer MP3/FLAC for sharing, and consider rendering a short **preview** (e.g. 60 s) first for approval.
- Everything reproducible: same params + `--seed` → same file.
