import os, sys
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import sfx, recipes
R = os.path.dirname(os.path.abspath(__file__))
EV = {'vault': [(0.4, 'whoosh'), (1.8, 'coin'), (2.6, 'pop'), (3.2, 'stamp'), (3.8, 'pop')],
      'network': [(0.4, 'whoosh'), (1.8, 'coin'), (2.6, 'pop'), (3.6, 'pop')],
      'powercycle': [(0.2, 'whoosh'), (2.0, 'coin'), (2.8, 'pop'), (3.6, 'pop')],
      'shapeshift': [(0.4, 'whoosh'), (1.8, 'coin'), (2.6, 'pop'), (3.6, 'pop')]}
STYLE = {'vault': ('trap', dict(bpm=140, key='F', mode='minor')), 'network': ('future_bass', dict(bpm=150, key='A')),
         'powercycle': ('techno', dict(bpm=126, key='D', mode='minor')), 'shapeshift': ('synthwave', dict(bpm=110, key='E', mode='minor'))}
for name, ev in EV.items():
    rname, kw = STYLE[name]
    try:
        m = getattr(recipes, rname)(duration=12.0, music_level=-19.0, outro=10.5, **kw)
    except TypeError:
        kw.pop('mode', None); m = getattr(recipes, rname)(duration=12.0, music_level=-19.0, outro=10.5, **kw)
    print(name, rname)
    for s in range(12): m.sfx(sfx.tick('clock', level=-30), at=float(s), gain=-4)
    for i, (t, k) in enumerate(ev):
        snd = {'whoosh': lambda: sfx.whoosh(0.5, seed=i, level=-24), 'coin': lambda: sfx.coin(level=-22), 'pop': lambda: sfx.pop(level=-26),
               'stamp': lambda: sfx.stamp(level=-24, seed=i)}[k]()
        m.sfx(snd, at=t, gain=-2)
    m.export(os.path.join(R, f'{name}.wav'), lufs=-14.0, analyze=False); print(name)
