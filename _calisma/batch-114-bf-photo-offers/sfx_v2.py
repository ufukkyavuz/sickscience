# SFX pass v2 (user ref reel: cinematic boom, camera charge, timer slowing down, stutter riser, whoosh,
# small gear shift, flash, bass drop, metallic riser). Built from mgaudio, nothing copied from the reel.
import os, sys
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import sfx, recipes
R = os.path.dirname(os.path.abspath(__file__))
DUR = 12.0

# per-video moments: number in, price in, pills, seal, CTA
PHOTO = dict(num=0.4, price=1.8, pills=2.6, seal=None, cta=3.6)
EV = {
    'vault': dict(PHOTO, seal=3.2, cta=3.8), 'network': PHOTO, 'powercycle': dict(PHOTO, num=0.2, price=2.0, pills=2.8),
    'shapeshift': PHOTO,
    'vault_bf': dict(num=0.2, price=2.0, pills=2.8, seal=3.2, cta=3.6), 'network_bf': dict(num=0.2, price=2.0, pills=2.8, seal=None, cta=3.6),
    'shapeshift_bf': dict(num=0.2, price=2.0, pills=2.8, seal=None, cta=3.6),
    'price': dict(num=3.0, price=4.6, pills=5.4, seal=6.2, cta=7.0),
    'receipt': dict(num=1.2, price=5.6, pills=6.0, seal=6.4, cta=6.45, type_lines=[1.2 + 0.55 * i for i in range(8)]),
    'equation': dict(num=0.5, price=4.6, pills=5.4, seal=6.0, cta=6.6, hits=[3.2]),
    'chart': dict(num=0.6, price=3.6, pills=5.4, seal=6.2, cta=7.0),
}


def build(name, e):
    m = recipes.ambient(duration=DUR, music_level=-90.0)
    seed = sum(map(ord, name))
    m.sfx(sfx.boom(2.2, f0=46.0, seed=seed, level=-16), at=0.0, gain=0)                       # cinematic boom on frame 0
    # timer: steady ticks, slowing down over the last seconds
    t = 0.0; step = 1.0
    while t < DUR - 0.5:
        m.sfx(sfx.tick('clock', level=-27), at=t, gain=-2)
        if t > DUR - 4.5: step *= 1.18
        t += step
    m.sfx(sfx.stutter(sfx.whoosh(0.35, seed=seed, level=-22), slice_sec=0.05, repeats=5, pitch_step=1.0), at=max(0.0, e['num'] - 0.3), gain=-2)  # stutter riser into the number
    m.sfx(sfx.impact('cinematic', size=0.8, seed=seed, level=-18), at=e['num'], gain=0)
    m.sfx(sfx.charge(0.9, level=-24), at=max(0.0, e['price'] - 0.9), gain=-2)               # camera charge ...
    m.sfx(sfx.shutter('dslr', level=-18, seed=seed), at=e['price'], gain=0)                   # ... flash on the price
    m.sfx(sfx.whoosh(0.45, kind='swoosh', seed=seed + 1, level=-22), at=e['price'] - 0.05, gain=-3)
    m.sfx(sfx.click('soft', level=-22), at=e['pills'], gain=0)                                # small gear shift
    m.sfx(sfx.toggle(True, level=-24), at=e['pills'] + 0.12, gain=0)
    if e.get('seal'):
        m.sfx(sfx.lock_on(0.6, note='E6', level=-24), at=e['seal'], gain=-2)
    m.sfx(sfx.riser(0.8, kind='hybrid', note='E4', end='cut', seed=seed, level=-24), at=e['cta'] - 0.8, gain=-3)  # metallic riser
    m.sfx(sfx.sub_drop(1.0, level=-18), at=e['cta'], gain=0)                                  # bass drop on the CTA
    for tl in e.get('type_lines', []):
        m.sfx(sfx.typewriter(level=-26, seed=int(tl * 10)), at=tl, gain=-2)
    for h in e.get('hits', []):
        m.sfx(sfx.text_hit('slam', level=-22, seed=seed), at=h, gain=-2)
    out = os.path.join(R, 'sfx2', f'{name}.wav'); os.makedirs(os.path.dirname(out), exist_ok=True)
    m.export(out, lufs=-21.0, analyze=False)
    return out


if __name__ == '__main__':
    for n, e in EV.items():
        build(n, e); print(n)
