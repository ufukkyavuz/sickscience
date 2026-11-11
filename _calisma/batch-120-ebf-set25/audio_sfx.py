# music bed + countdown ticks + event SFX per offer film; -14 LUFS
import os, sys
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import sfx, recipes
R = os.path.dirname(os.path.abspath(__file__))
EV = {
    'price':    [(3.0, 'whoosh'), (4.6, 'coin'), (5.4, 'pop'), (6.2, 'stamp'), (7.0, 'pop')],
    'receipt':  [(1.2 + 0.55 * i, 'type') for i in range(9)] + [(6.2, 'coin'), (7.0, 'pop'), (7.4, 'stamp'), (7.6, 'pop')],
    'equation': [(0.5, 'pop'), (1.3, 'swish'), (1.6, 'pop'), (3.2, 'hit'), (4.6, 'hit'), (6.0, 'coin'), (6.8, 'pop'), (7.4, 'stamp'), (8.0, 'pop')],
    'chart':    [(0.6, 'swish'), (3.2, 'whoosh'), (4.8, 'coin'), (5.4, 'pop'), (6.2, 'stamp'), (7.0, 'pop')],
}
for name, ev in EV.items():
    m = recipes.explainer(duration=12.0, bpm=112, key="D", music_level=-90.0, outro=9.0)
    for s in range(12):
        m.sfx(sfx.tick('clock', level=-30), at=s + 0.0, gain=-4)
    for i, (t, k) in enumerate(ev):
        snd = {'whoosh': lambda: sfx.whoosh(0.5, seed=i, level=-24), 'coin': lambda: sfx.coin(level=-22), 'pop': lambda: sfx.pop(level=-26),
               'stamp': lambda: sfx.stamp(level=-24, seed=i), 'type': lambda: sfx.typewriter(level=-26, seed=i), 'swish': lambda: sfx.swish(seed=i, level=-26),
               'hit': lambda: sfx.text_hit(level=-24, seed=i)}[k]()
        m.sfx(snd, at=t, gain=-2)
    out = os.path.join(R, f'{name}_sfx.wav'); m.export(out, lufs=-24.0, analyze=False); print(name)
