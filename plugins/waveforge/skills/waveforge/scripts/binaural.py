#!/usr/bin/env python3
"""
WaveForge binaural-beat generator.

Synthesises a REAL stereo .wav: pure-tone carriers with a precise, optionally
gliding beat frequency, plus an optional colored-noise bed, pad drone, and fades.

Design notes:
  * Binaural  : Left = carrier, Right = carrier + beat(t). Needs headphones.
  * Isochronic: single carrier gated on/off at beat(t). Speaker-friendly.
  * Monaural  : the two tones summed before output. Speaker-friendly.
  * The beat can GLIDE: pass a --schedule of "time:beat" control points and the
    instantaneous beat is linearly interpolated and phase-integrated (smooth).

Only dependency is numpy. WAV is written with the standard-library `wave` module.

Examples
--------
# 20-min calm alpha track, pink-noise bed, headphones (binaural)
python binaural.py --carrier 200 --beat 10 --duration 20 --noise pink \
    --noise-db -15 --out calm_alpha.wav

# 45-min sleep journey gliding alpha->theta->delta, brown bed, long fade
python binaural.py --carrier 120 --schedule "0:10,5m:6,12m:2.5,45m:2.5" \
    --noise brown --noise-db -12 --fade-out 20 --out deep_sleep.wav

# Focus track, isochronic so it works on speakers
python binaural.py --carrier 220 --beat 15 --duration 30 --mode isochronic \
    --noise brown --noise-db -16 --out focus_beta.wav
"""
import argparse
import sys
import wave
import numpy as np


# ---------- parsing helpers ----------
def parse_time(tok: str) -> float:
    """'90' -> 90s, '5m' -> 300s, '1h' -> 3600s, '500ms' -> 0.5s."""
    tok = tok.strip().lower()
    if tok.endswith("ms"):
        return float(tok[:-2]) / 1000.0
    if tok.endswith("s"):
        return float(tok[:-1])
    if tok.endswith("m"):
        return float(tok[:-1]) * 60.0
    if tok.endswith("h"):
        return float(tok[:-1]) * 3600.0
    return float(tok)


def build_schedule(args):
    """Return (times[], beats[]) control points sorted by time."""
    if args.schedule:
        pts = []
        for tok in args.schedule.split(","):
            t, b = tok.split(":")
            pts.append((parse_time(t), float(b)))
        pts.sort(key=lambda p: p[0])
    elif args.beat_start is not None and args.beat_end is not None:
        total = (args.duration or 10) * 60.0
        pts = [(0.0, args.beat_start), (total, args.beat_end)]
    elif args.beat is not None:
        total = (args.duration or 10) * 60.0
        pts = [(0.0, args.beat), (total, args.beat)]
    else:
        sys.exit("ERROR: give --beat, or --beat-start/--beat-end, or --schedule.")
    return np.array([p[0] for p in pts]), np.array([p[1] for p in pts])


# ---------- DSP ----------
def colored_noise(n: int, exponent: float, rng) -> np.ndarray:
    """Power spectral density ~ 1/f**exponent.  white=0, pink=1, brown=2."""
    white = rng.standard_normal(n)
    if exponent == 0:
        y = white
    else:
        X = np.fft.rfft(white)
        f = np.fft.rfftfreq(n)
        f[0] = f[1] if len(f) > 1 else 1.0
        X = X / (f ** (exponent / 2.0))
        y = np.fft.irfft(X, n=n)
    peak = np.max(np.abs(y)) + 1e-12
    return y / peak


def apply_fade(sig: np.ndarray, sr: int, fade_in: float, fade_out: float):
    n_in = int(fade_in * sr)
    n_out = int(fade_out * sr)
    if n_in > 0:
        sig[:n_in] *= np.sin(np.linspace(0, np.pi / 2, n_in)) ** 2
    if n_out > 0:
        sig[-n_out:] *= np.sin(np.linspace(np.pi / 2, 0, n_out)) ** 2
    return sig


def measure_beat(left, right, sr, floor_hz=50.0) -> float:
    """Estimate the realised beat = |peak(R) - peak(L)| over a long mid window.

    The peak search is constrained to freqs >= floor_hz so the low-frequency
    energy of a brown/pink-noise bed can't be mistaken for the carrier.
    """
    win = min(len(left), sr * 60)
    start = max(0, len(left) // 2 - win // 2)
    sl = slice(start, start + win)
    w = np.hanning(win)
    freqs = np.fft.rfftfreq(win, 1.0 / sr)
    band = freqs >= floor_hz

    def peak(x):
        mag = np.abs(np.fft.rfft(x[sl] * w))
        mag[~band] = 0.0
        return freqs[int(np.argmax(mag))]

    return abs(peak(right) - peak(left))


def write_wav(path, left, right, sr, bitdepth):
    inter = np.empty(left.size + right.size, dtype=np.float64)
    inter[0::2] = left
    inter[1::2] = right
    if bitdepth == 16:
        data = np.clip(inter * 32767.0, -32768, 32767).astype("<i2").tobytes()
        sw = 2
    elif bitdepth == 24:
        ints = np.clip(inter * 8388607.0, -8388608, 8388607).astype("<i4")
        b = ints.view(np.uint8).reshape(-1, 4)[:, :3]
        data = np.ascontiguousarray(b).tobytes()
        sw = 3
    else:
        sys.exit("ERROR: --bitdepth must be 16 or 24.")
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(sw)
        w.setframerate(sr)
        w.writeframes(data)


# ---------- main ----------
def main():
    p = argparse.ArgumentParser(description="WaveForge binaural-beat generator")
    p.add_argument("--carrier", type=float, default=200.0, help="carrier Hz (constant)")
    p.add_argument("--beat", type=float, help="constant beat Hz")
    p.add_argument("--beat-start", type=float, help="glide start beat Hz")
    p.add_argument("--beat-end", type=float, help="glide end beat Hz")
    p.add_argument("--schedule", type=str,
                   help='control points "t:beat,..." e.g. "0:10,5m:6,20m:2.5"')
    p.add_argument("--duration", type=float, help="minutes (holds last beat if longer)")
    p.add_argument("--mode", choices=["binaural", "isochronic", "monaural"],
                   default="binaural")
    p.add_argument("--noise", choices=["none", "white", "pink", "brown"], default="none")
    p.add_argument("--noise-db", type=float, default=-15.0, help="bed level vs tones")
    p.add_argument("--pad", action="store_true", help="add a soft sub-octave drone")
    p.add_argument("--pad-db", type=float, default=-20.0)
    p.add_argument("--fade-in", type=float, default=4.0, help="seconds")
    p.add_argument("--fade-out", type=float, default=6.0, help="seconds")
    p.add_argument("--peak-dbfs", type=float, default=-3.0, help="normalisation peak")
    p.add_argument("--samplerate", type=int, default=44100)
    p.add_argument("--bitdepth", type=int, default=16, choices=[16, 24])
    p.add_argument("--seed", type=int, default=7, help="noise RNG seed (reproducible)")
    p.add_argument("--out", type=str, required=True)
    args = p.parse_args()

    sr = args.samplerate
    times, beats = build_schedule(args)
    total = float(times[-1])
    if args.duration:
        total = max(total, args.duration * 60.0)
    if total <= 0:
        sys.exit("ERROR: total duration is zero — set --duration or a --schedule.")

    n = int(total * sr)
    t = np.arange(n) / sr
    beat_t = np.interp(t, times, beats)          # smooth, clamped holds
    rng = np.random.default_rng(args.seed)

    tone_amp = 0.7
    # phase = 2*pi * integral(freq) dt   (cumulative sum / sr)
    phase_carrier = 2 * np.pi * args.carrier * t
    phase_right = 2 * np.pi * np.cumsum(args.carrier + beat_t) / sr

    if args.mode == "binaural":
        left = tone_amp * np.sin(phase_carrier)
        right = tone_amp * np.sin(phase_right)
    elif args.mode == "monaural":
        mono = tone_amp * 0.5 * (np.sin(phase_carrier) + np.sin(phase_right))
        left = mono.copy()
        right = mono.copy()
    else:  # isochronic — gate the carrier on/off at the beat rate
        phase_beat = 2 * np.pi * np.cumsum(beat_t) / sr
        gate = (np.sin(phase_beat) > 0).astype(np.float64)
        k = max(1, int(0.005 * sr))               # 5 ms smoothing to kill clicks
        gate = np.convolve(gate, np.ones(k) / k, mode="same")
        mono = tone_amp * np.sin(phase_carrier) * gate
        left = mono.copy()
        right = mono.copy()

    if args.pad:
        pad_amp = tone_amp * 10 ** (args.pad_db / 20.0)
        pad = pad_amp * np.sin(2 * np.pi * (args.carrier / 2.0) * t)
        left += pad
        right += pad

    if args.noise != "none":
        exp = {"white": 0.0, "pink": 1.0, "brown": 2.0}[args.noise]
        noise_amp = tone_amp * 10 ** (args.noise_db / 20.0)
        left += noise_amp * colored_noise(n, exp, rng)
        right += noise_amp * colored_noise(n, exp, rng)

    apply_fade(left, sr, args.fade_in, args.fade_out)
    apply_fade(right, sr, args.fade_in, args.fade_out)

    peak_lin = 10 ** (args.peak_dbfs / 20.0)
    m = max(np.max(np.abs(left)), np.max(np.abs(right))) + 1e-12
    g = peak_lin / m
    left *= g
    right *= g

    write_wav(args.out, left, right, sr, args.bitdepth)

    measured = measure_beat(left, right, sr) if args.mode == "binaural" else float("nan")
    print("WaveForge render complete")
    print(f"  out         : {args.out}")
    print(f"  mode        : {args.mode}")
    print(f"  carrier     : {args.carrier:.2f} Hz")
    print(f"  beat        : {beats[0]:.2f} -> {beats[-1]:.2f} Hz "
          f"(schedule pts: {list(zip(times.tolist(), beats.tolist()))})")
    print(f"  duration    : {total/60:.2f} min ({n} samples @ {sr} Hz, {args.bitdepth}-bit)")
    print(f"  bed         : {args.noise} @ {args.noise_db} dB"
          f"{', +pad' if args.pad else ''}")
    if args.mode == "binaural":
        print(f"  measured beat (FFT, mid window): {measured:.2f} Hz")


if __name__ == "__main__":
    main()
