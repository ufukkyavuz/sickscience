"""Rising pop on every number change + a big hit on the final '14 AWARDS?!?!' (mixed under the reference sound)."""
import numpy as np
from scipy.io import wavfile
SR = 44100; DUR = 10.7; mix = np.zeros(int(SR * DUR))
def add(sig, t, g):
    i = int(t * SR); n = min(len(sig), len(mix) - i); mix[i:i + n] += sig[:n] * g
def pop(f0):
    t = np.arange(int(0.16 * SR)) / SR; f = f0 * (1 + 0.6 * np.exp(-t * 40))
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 22)
    click = np.random.default_rng(1).standard_normal(len(t)) * np.exp(-t * 300) * 0.3
    return s + click
def hit():
    t = np.arange(int(1.2 * SR)) / SR
    sub = np.sin(2 * np.pi * (45 + 80 * np.exp(-t * 18)) * t) * np.exp(-t * 3)
    noise = np.random.default_rng(2).standard_normal(len(t)) * np.exp(-t * 9) * 0.5
    bell = sum(np.sin(2 * np.pi * f * t) * np.exp(-t * d) for f, d in ((1318, 3), (1976, 4), (2637, 6))) * 0.25
    return sub + noise + bell
def riser(d):
    t = np.arange(int(d * SR)) / SR; f = 300 * (6 ** (t / d))
    return (np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.4 + np.random.default_rng(3).standard_normal(len(t)) * 0.15) * (t / d) ** 2
CHANGES = [1.667, 4.6, 6.267, 7.867, 8.4, 8.867]           # number changes before the final
for k, t in enumerate(CHANGES): add(pop(520 * (1.16 ** k)), t, 0.55)
add(riser(0.5), 8.9, 0.5); add(hit(), 9.4, 0.9)
mix = mix / (np.abs(mix).max() + 1e-9) * 0.9
wavfile.write('sfx.wav', SR, (mix * 32767).astype(np.int16)); print('ok')
