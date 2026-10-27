"""Batch 45 — Dr. Merve's ShapeShift challenge, Meta cut (≤20 s, 9:16), honest 12-day diary (no before/after claim).
Sources (raw 4K, camera dates): IMG_2162/2164 = 2 Apr (Day 0), IMG_2417 = 8 Apr (Day 6), IMG_2602 = 13 Apr (Day 11),
IMG_2638 = 14 Apr (Day 12). The July clip (IMG_8738) is NOT used — it was labelled "Day 14" in the client edit but is ~16 weeks later.
Voice: client edit VO (demucs vocals) for the hook + mechanism lines; Merve's own on-camera intro from IMG_2162.
usage: ~/motion-tools/.venv/bin/python render45.py -> out/ss_challenge_meta.mp4"""
import os, sys, json, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import recipes

HERE = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(HERE, 'raw'); AU = os.path.join(HERE, 'audio')
OUT = os.path.join(HERE, 'out'); os.makedirs(OUT, exist_ok=True)
FD = os.path.expanduser('~/Library/Fonts/'); FB = FD + 'FoundersGrotesk-Bold.otf'; FM = FD + 'FoundersGrotesk-Medium.otf'
LOGO = os.path.join(HERE, '..', 'video-01-bcrf', 'assets', 'logo.png')  # black "Sick" + magenta "Science"; black turned white below
W, H, FPS = 1080, 1920, 30
VO = os.path.join(AU, 'vo_edit_vocals.wav'); INTRO = os.path.join(AU, 'merve_intro_vocals.wav')
FIX = {'Shapeshift': 'ShapeShift', 'Meriwe,': 'Merve,', 'Six': 'SickScience', 'Science': None, 'Labs.': 'Labs.'}

# (video file, in, dur, audio file or None, audio in, day label)
SHOTS = [
    ('IMG_2164', 1.6, 3.40, VO, 0.00, 'DAY 0'),      # hook: product to camera / "Not another peptide. It's an exosome."
    ('IMG_2162', 3.00, 5.50, INTRO, 3.00, 'DAY 0'),  # "I'm Dr. Merve, co-founder of SickScience Labs. Today I'm starting my ShapeShift challenge."
    ('IMG_2164', 13.0, 2.82, VO, 6.60, 'DAY 0'),     # "Plant-derived exosomes help signal skin…"
    ('IMG_2602', 8.0, 3.13, VO, 9.42, 'DAY 11'),     # "…for a firmer, more sculpted-looking jawline."
    ('IMG_2164', 47.6, 0.85, None, 0, 'DAY 0'),      # profile diary
    ('IMG_2417', 29.7, 0.85, None, 0, 'DAY 6'),
    ('IMG_2602', 22.0, 0.85, None, 0, 'DAY 11'),
    ('IMG_2638', 37.6, 0.85, None, 0, 'DAY 12'),
    ('IMG_2164', 49.35, 1.70, None, 0, None),        # end: smile to camera + logo + URL
]

def words(key, t0, t1):
    ws = json.load(open(os.path.join(AU, 'words.json')))[key]
    out = []
    for w, s, e in ws:
        if s >= t0 - 0.05 and s < t1:
            if w in FIX:
                if FIX[w] is None: continue
                w = FIX[w]
            if w.startswith('-') and out:                    # whisper splits "co-founder" into "co" + "-founder"
                pw, ps, _ = out[-1]; out[-1] = (pw + w, ps, e - t0)
            else:
                out.append((w, s - t0, e - t0))
    return out

def groups(ws, n=3):
    gs, cur = [], []
    for w in ws:
        cur.append(w)
        if len(cur) == n or w[0][-1:] in '.,': gs.append(cur); cur = []
    if cur: gs.append(cur)
    return [(' '.join(x[0] for x in g), g[0][1], g[-1][2]) for g in gs]

def text_png(path, txt, size, y, font=FB, stroke=7):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im); f = ImageFont.truetype(font, size)
    tw = d.textlength(txt, font=f)
    while tw > W - 140: size -= 4; f = ImageFont.truetype(font, size); tw = d.textlength(txt, font=f)
    d.text(((W - tw) / 2, y), txt, font=f, fill=(255, 255, 255, 255), stroke_width=stroke, stroke_fill=(12, 10, 14, 220))
    im.save(path)

def label_png(path, txt):
    """small day chip in the upper safe band (y≈300)"""
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im); f = ImageFont.truetype(FB, 52)
    tw = d.textlength(txt, font=f); pw, ph = tw + 64, 84; x0 = (W - pw) / 2
    d.rounded_rectangle((x0, 300, x0 + pw, 300 + ph), 42, fill=(169, 33, 192, 235))
    d.text((x0 + 32, 300 + 14), txt, font=f, fill=(255, 255, 255, 255)); im.save(path)

def end_png(path):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    lg = Image.open(LOGO).convert('RGBA'); px = lg.load()
    for yy in range(lg.height):
        for xx in range(lg.width):
            r, g, b, a = px[xx, yy]
            if a and max(r, g, b) < 90: px[xx, yy] = (255, 255, 255, a)
    lw = 560; lg = lg.resize((lw, round(lg.height * lw / lg.width)), Image.LANCZOS)
    plate = Image.new('RGBA', (W, 260), (0, 0, 0, 0)); ImageDraw.Draw(plate).rectangle((0, 0, W, 260), fill=(10, 8, 12, 120))
    im.alpha_composite(plate, (0, 960)); im.alpha_composite(lg, ((W - lw) // 2, 1000))
    f = ImageFont.truetype(FM, 44); t = 'SickScienceLabs.com'; tw = d.textlength(t, font=f)
    d.text(((W - tw) / 2, 1000 + lg.height + 36), t, font=f, fill=(255, 255, 255, 255)); im.save(path)

def main():
    tmp = tempfile.mkdtemp(prefix='b45_'); ins, fc, ov = [], [], []
    t = 0.0; starts = []
    for i, (v, vin, dur, af, ain, lab) in enumerate(SHOTS):
        ins += ['-ss', f'{vin:.3f}', '-t', f'{dur + 0.1:.3f}', '-i', os.path.join(RAW, v + '.MOV')]
        hold = ',tpad=stop_mode=clone:stop_duration=1' if v == 'IMG_2164' and vin > 49 else ''
        fc.append(f'[{i}:v]scale={W}:{H}:flags=lanczos,fps={FPS},setsar=1,format=yuv420p{hold},trim=0:{dur},setpts=PTS-STARTPTS[v{i}]')
        starts.append(t); t += dur
    total = t; n = len(SHOTS)
    fc.append(''.join(f'[v{i}]' for i in range(n)) + f'concat=n={n}:v=1:a=0[vc]')
    # overlays: day chips, captions, end card
    k = n; last = '[vc]'
    def add(png, a, b):
        nonlocal k, last
        ins.extend(['-loop', '1', '-t', f'{total:.3f}', '-i', png])
        fc.append(f"{last}[{k}:v]overlay=0:0:enable='between(t,{a:.3f},{b:.3f})'[o{k}]"); last = f'[o{k}]'; k += 1
    for i, (v, vin, dur, af, ain, lab) in enumerate(SHOTS):
        if lab:
            p = os.path.join(tmp, f'lab{i}.png'); label_png(p, lab); add(p, starts[i], starts[i] + dur)
        if af:
            key = 'vo' if af == VO else 'intro'
            for j, (txt, s, e) in enumerate(groups(words(key, ain, ain + dur))):
                p = os.path.join(tmp, f'cap{i}_{j}.png'); text_png(p, txt, 84, 1080)
                add(p, starts[i] + max(0, s - 0.03), min(starts[i] + dur, starts[i] + e + 0.12))
    p = os.path.join(tmp, 'end.png'); end_png(p); add(p, starts[-1] + 0.15, total)
    # audio: voice pieces placed on the timeline + lo-fi bed
    vo_parts = []
    for i, (v, vin, dur, af, ain, lab) in enumerate(SHOTS):
        if af:
            vo_parts.append((af, ain, dur, starts[i]))
    m = recipes.lofi(duration=round(total, 3), drop=starts[1], outro=starts[-1], keys='rhodes', flavor='chill')
    bed = os.path.join(tmp, 'bed.wav'); m.export(bed)
    aidx0 = k
    for af, ain, dur, st in vo_parts: ins += ['-i', af]
    ins += ['-i', bed]
    alabels = []
    for j, (af, ain, dur, st) in enumerate(vo_parts):
        fc.append(f'[{aidx0 + j}:a]atrim={ain:.3f}:{ain + dur:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={dur - 0.04:.3f}:d=0.04,'
                  f'adelay={int(st * 1000)}|{int(st * 1000)},aresample=48000[va{j}]'); alabels.append(f'[va{j}]')
    fc.append(''.join(alabels) + f'amix=inputs={len(alabels)}:duration=longest:normalize=0,apad=whole_dur={total:.3f},asplit=2[vox][sc]')
    fc.append(f'[{aidx0 + len(vo_parts)}:a]aresample=48000,volume=-10dB[mus];[mus][sc]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=300[duck]')
    fc.append('[vox][duck]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[ao]')
    out = os.path.join(OUT, 'ss_challenge_meta.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *ins, '-filter_complex', ';'.join(fc), '-map', last, '-map', '[ao]',
                    '-t', f'{total:.3f}', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-r', str(FPS),
                    '-c:a', 'aac', '-b:a', '192k', out], check=True)
    print('->', out, round(total, 2), 's')

if __name__ == '__main__':
    main()
