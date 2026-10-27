"""Frame-accurate sound design for the ShapeShift reel (30 fps, 540 frames)."""
import numpy as np, scipy.signal as sg
from scipy.io import wavfile
SR, FPS, N = 44100, 30, 540
L = int(N / FPS * SR) + SR // 2
mix = np.zeros(L)
rng = np.random.default_rng(7)
fr = lambda f: int(f / FPS * SR)
t_ = lambda d: np.arange(int(d * SR)) / SR
def add(sig, f, g=1.0):
    i = fr(f); n = min(len(sig), L - i); mix[i:i + n] += sig[:n] * g
def hp(x, c): return sg.sosfilt(sg.butter(2, c, 'hp', fs=SR, output='sos'), x)
def lp(x, c): return sg.sosfilt(sg.butter(2, c, 'lp', fs=SR, output='sos'), x)
def kick():
    t = t_(0.25); ph = 2 * np.pi * np.cumsum(45 + 110 * np.exp(-28 * t)) / SR
    return np.sin(ph) * np.exp(-t / 0.12)
def hat(): t = t_(0.08); return hp(rng.standard_normal(len(t)), 7000) * np.exp(-t / 0.012)
def whoosh(d):
    t = t_(d); n = rng.standard_normal(len(t)); env = np.sin(np.pi * t / d) ** 2
    cut = 300 + 5000 * env; y = np.zeros_like(n); a = 0.0
    for i in range(len(n)):
        k = 1 - np.exp(-2 * np.pi * cut[i] / SR); a += k * (n[i] - a); y[i] = a
    return y * env
def swish(d=0.16): t = t_(d); return hp(rng.standard_normal(len(t)), 3000) * np.sin(np.pi * t / d) ** 3
def tick(f0=3000): t = t_(0.05); return np.sin(2 * np.pi * f0 * t) * np.exp(-t / 0.008)
def bounce():
    t = t_(0.18); ph = 2 * np.pi * np.cumsum(np.linspace(400, 140, len(t))) / SR
    return np.sin(ph) * np.exp(-t / 0.05) + 0.4 * tick(2500)[:len(t)].tolist().__len__() * 0 + np.pad(tick(2500), (0, len(t) - len(tick(2500)))) * 0.4
def impact():
    t = t_(1.2); sub = np.sin(2 * np.pi * 38 * t) * np.exp(-t / 0.35)
    return sub + lp(rng.standard_normal(len(t)), 900) * np.exp(-t / 0.08) * 0.6
def riser(d):
    t = t_(d); f = 120 * (2400 / 120) ** (t / d); ph = 2 * np.pi * np.cumsum(f) / SR
    return (np.sin(ph) * 0.5 + hp(rng.standard_normal(len(t)), 1500) * 0.35) * (t / d) ** 2
def chime():
    t = t_(2.0); out = np.zeros_like(t)
    for f0, dec, g in ((1318.5, 1.2, 1), (1975.5, 0.8, .6), (2637, 0.5, .4), (987.8, 1.6, .5)):
        out += g * np.sin(2 * np.pi * f0 * t) * np.exp(-t / dec)
    return out / 2.5
def hum(d):
    t = t_(d); trem = 0.75 + 0.25 * np.sin(2 * np.pi * 5.5 * t)
    s = sum(np.sin(2 * np.pi * f * t) / k for k, f in enumerate((55, 110, 165), 1))
    return s * trem * np.minimum(1, t / 0.15) * np.minimum(1, (d - t) / 0.1)
def pluck(f0):
    t = t_(0.4); return (np.sin(2 * np.pi * f0 * t) + 0.3 * np.sin(4 * np.pi * f0 * t)) * np.exp(-t / 0.13)

# scene 1: torch
add(hum(85 / FPS), 3, 0.22)
for f in (3, 6, 8): add(tick(1800), f, 0.5)
add(riser(24 / FPS), 58, 0.35)
add(impact(), 82, 0.8); add(chime(), 82, 0.45)
# scene 2: stats + pendulum
add(swish(), 100, 0.35); add(swish(), 106, 0.25)
for k in range(4):
    c = 135 + 22.5 + 45 * k
    add(whoosh(0.6), c - 9, 0.55)
add(swish(), 296, 0.3); add(swish(), 304, 0.3)
add(tick(3200), 302, 0.35); add(tick(3600), 308, 0.35)
# scene 4: end card
add(whoosh(0.7), 404, 0.6)
for i in range(13): add(tick(2600 + 90 * i), 428 + i * 1.3, 0.12)
for f, g in ((454, 0.9), (472, 0.6)): add(bounce(), f, g)
add(impact(), 486, 0.35); add(chime(), 486, 0.6)
add(swish(), 498, 0.25)
# light groove 120 BPM (one beat = 15 frames) from the first stat to the end
notes = [110.0, 110.0, 130.8, 98.0]
for i, f in enumerate(range(90, 526, 15)):
    add(kick(), f, 0.42); add(hat(), f + 7.5, 0.12); add(pluck(notes[(i // 4) % 4]), f, 0.16)
# master
y = np.tanh(mix * 1.3)
y /= np.abs(y).max() / 10 ** (-1 / 20)
end = fr(N); y = y[:end]; fade = int(0.5 * SR); y[-fade:] *= np.linspace(1, 0, fade)
wavfile.write('audio/sfx.wav', SR, (y * 32767).astype(np.int16))
print('ok', len(y) / SR)
