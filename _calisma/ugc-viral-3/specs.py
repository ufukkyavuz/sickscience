# UGC viral 3 specs (2026-11-11). Times: segs in SOURCE seconds; texts/big/inserts/emoji/sfx in OUTPUT seconds.
import os
R = os.path.dirname(os.path.abspath(__file__)) + '/src/'
SDR = '/private/tmp/claude-501/v3/sdr/'   # Apple-tone-mapped copies of the HLG iPhone raws (tools/hlg2sdr), rebuildable
PX = "/Users/ufo/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/INO Claude Ads/motion-assets/_music/pixabay/"
G = R + 'myth-gorsel/'
W = (255, 255, 255)

SPEC = {

 # ---------------------------------------------------------------- 1 · Puffy face (no raw of the first steps: Berk's edit, cropped below his burned-in captions; finale from raw IMG_2946)
 'P': dict(name='NetWork – Puffy morning face', caps=False,
   music=(PX + 'penguinmusic-lazy-day-239287.mp3', 0.0, 0),
   segs=[dict(src=R + 'ref/berk_puffy_face.mp4', a=0.0, b=2.0, crop='844:1490:118:430'),
         dict(src=R + 'ref/berk_puffy_face.mp4', a=2.3, b=5.8, speed=1.4, crop='844:1490:118:430'),
         dict(src=R + 'ref/berk_puffy_face.mp4', a=7.0, b=11.5, speed=1.3, crop='844:1490:118:430'),
         dict(src=R + 'ref/berk_puffy_face.mp4', a=13.0, b=19.5, speed=1.5, crop='844:1490:118:430'),
         dict(src=R + 'ref/berk_puffy_face.mp4', a=20.3, b=25.8, speed=1.8, crop='844:1490:118:430'),
         dict(src=SDR + 'puffy_2946.mov', a=27.0, b=33.1, speed=1.3, crop='940:1670:70:150')],
   # kinetic words per step (land in turn, alternating sides), zoom punch + whoosh on every cut, pop per step, ding on 'ready'
   kin=[(0.15, 2.0, [[('puffy', 86, W), ('morning', 86, W)], [('FACE?', 170, W)]], 1150),
        (2.05, 4.5, [[('headband', 86, W)], [('ON', 170, W)]], 1150),
        (4.55, 7.96, [[('NetWork', 150, W)], [('all over the face', 76, W)]], 1150),
        (8.0, 12.29, [[('gua sha', 150, W)], [('jaw & neck', 86, W)]], 1150),
        (12.33, 15.35, [[('quick', 86, W)], [('GLAM', 170, W)]], 1150),
        (15.6, 20.0, [[('ready.', 190, W)]], 1180)],
   punch=[2.0, 4.5, 7.96, 12.29, 15.35],
   sfx=[(0.15, 'pop'), (2.1, 'pop'), (4.6, 'pop'), (8.05, 'pop'), (12.4, 'pop'), (15.6, 'ding')]),

 # ---------------------------------------------------------------- 2 · ShapeShift before/after (DropOff format)
 'B': dict(name='ShapeShift – That was my before', caps=True, fix={'before': 'before.', 'after': 'after.'},
   music=(PX + 'bombinsound-happy-advertising-hip-hop-magic-moments-628139.mp3', 2.0, -17),
   # 'that was my before' -> her own before photo pops up where her finger points (upper right), she keeps pointing
   segs=[dict(src=R + 'ssba_edit.mp4', a=0.45, b=8.05, audio=True),
         dict(src=R + 'ssba_edit.mp4', a=8.05, b=10.12, audio=True),
         dict(src=SDR + 'ssba_2959.mov', a=2.0, b=3.6),
         dict(src=SDR + 'ssba_2961.mov', a=8.0, b=9.6),
         dict(src=SDR + 'ssba_2961.mov', a=11.5, b=22.5, speed=1.35),   # Polen: application longer (was 3 s)
         dict(src=SDR + 'ssba_2962.mov', a=17.6, b=19.8)],
   inserts=[(1.67, 4.4, R + 'ss_before_jaw.jpg', 760, 390, 380, 'card', None)],
   texts=[(1.8, 4.4, 'BEFORE', 'pop', 600, 76, W, 760),
          (9.67, 11.27, 'ShapeShift', 'slide', 330, 110, W),
          (11.27, 12.87, '1–2 pumps', 'slide', 330, 100, W),
          (12.87, 21.02, 'upward,\nneck to jaw', 'slide', 330, 100, W),
          (21.02, 23.22, 'twice a day', 'slide', 330, 100, W)],
   big=[(5.03, 7.5, 'AFTER', 1480, W)],
   sfx=[(1.67, 'swish'), (5.03, 'swish')]),


 # ---------------------------------------------------------------- 3 · Myth or fact (voice first: music barely there, data above her head)
 'M': dict(name='Myth or fact – Plant exosomes and human cells', caps=True, cap_y=1230,
   music=(PX + 'amaksi-night-detective-226857.mp3', 0.0, -24),
   fix={'cell.': 'cells.'},
   segs=[dict(src=R + 'lab_fun.mp4', a=11.3, b=15.8, asrc=R + 'vo_myth_open.wav', aa=0.0, ab=4.48, nocap=True),
         dict(src=R + 'myth_raw.mp4', a=0.0, b=1.5, audio=True),
         dict(src=R + 'myth_raw.mp4', a=1.52, b=3.45, audio=True),
         dict(src=R + 'myth_raw.mp4', a=4.1, b=7.5, audio=True),
         dict(src=R + 'myth_raw.mp4', a=13.15, b=17.52, audio=True),
         dict(src=R + 'myth_raw.mp4', a=17.9, b=24.85, audio=True),
         dict(src=R + 'myth_raw.mp4', a=29.95, b=34.45, audio=True),
         dict(src=R + 'myth_raw.mp4', a=75.3, b=78.1, audio=True),
         dict(src=R + 'myth_raw.mp4', a=79.2, b=81.85, audio=True)],
   # opening = her pipetting in the lab (active, no phone, no idle waiting); statement read by her cloned voice (polen_real_vo_raw.mpeg)
   kin=[(0.0, 3.1, [[('Plant', 104, W, 0.0), ('exosomes', 104, W, 0.34)], [('cannot talk', 104, W, 1.1)], [('with human cells.', 104, W, 1.92)]], 300)],
   texts=[(3.1, 4.5, 'MYTH', 'pop', 470, 150, W, 290), (3.48, 4.5, 'or', 'blur', 470, 70, W, 540), (3.8, 4.5, 'FACT', 'pop', 470, 150, W, 790)],
   tag=[(4.7, 7.9, 'Dr. Polen Koçak', 'SickScience Co-Founder', 90, 230), (27.3, 99, 'Dr. Polen Koçak', 'SickScience Co-Founder', 90, 230)],
   big=[(4.5, 5.9, 'MYTH', 610, W, 'behind')],
   inserts=[(7.93, 22.65, G + 'fibro uptake.png', 540, 330, 860, 'card', (858, 375, 75, 8.57)),
            (22.65, 27.15, G + 'paper1.png', 540, 250, 840, 'card', None),
            (24.15, 27.15, G + 'paper2.png', 540, 420, 840, 'card', None),
            (25.65, 27.15, G + 'paper3.png', 540, 615, 840, 'card', None)],
   sfx=[(3.1, 'pop'), (3.8, 'pop'), (4.5, 'impact'), (7.93, 'whoosh'), (22.65, 'swish'), (24.15, 'swish'), (25.65, 'swish')]),

 # ---------------------------------------------------------------- 4 · Lab, fun (one line of text, ends on her laugh)
 'L': dict(name='Lab – POV you work at SickScience', caps=False,
   music=(PX + 'poradovskyi-funk-funky-music-628015.mp3', 4.0, 0),
   segs=[dict(src=R + 'lab_fun.mp4', a=0.0, b=2.2), dict(src=R + 'lab_fun.mp4', a=12.0, b=14.0),
         dict(src=R + 'lab_fun.mp4', a=4.0, b=5.6), dict(src=R + 'lab_fun.mp4', a=20.5, b=23.0),
         dict(src=R + 'lab_fun.mp4', a=24.0, b=25.5), dict(src=R + 'lab_fun.mp4', a=16.8, b=18.8)],
   texts=[(0.0, 3.4, 'POV:', 'pop', 330, 110, W), (0.2, 3.4, 'you work at SickScience', 'blur', 470, 72, W)],
   punch=[2.2, 4.2, 5.8, 8.3],
   emoji=[(0.7, '\U0001F9EA', 1, 860), (6.1, '\U0001F483', -1, 900)],
   metal=4.2),

 # ---------------------------------------------------------------- 5 · Ayşim: kinetic type + steps, zoom drift, punch on cuts
 'A': dict(name='ShapeShift – How to apply in the lab', caps=False,
   music=(PX + 'coma-media-this-minimal-technology_pure-12327.mp3', 0.0, 0),
   segs=[dict(src=R + 'aysim_lab.MOV', a=24.0, b=25.6, zoom=(1.12, 1.0)),
         dict(src=R + 'aysim_lab.MOV', a=0.0, b=1.6, zoom=(1.0, 1.08)),
         dict(src=R + 'aysim_lab.MOV', a=3.0, b=4.6, zoom=(1.08, 1.0)),
         dict(src=R + 'aysim_lab.MOV', a=6.0, b=8.0, zoom=(1.0, 1.1)),
         dict(src=R + 'aysim_lab.MOV', a=11.0, b=14.0, speed=1.5, zoom=(1.1, 1.0)),
         dict(src=R + 'aysim_lab.MOV', a=16.0, b=19.2, speed=1.6, zoom=(1.0, 1.08)),
         dict(src=R + 'aysim_lab.MOV', a=25.6, b=27.0, zoom=(1.08, 1.0)),
         dict(src=R + 'aysim_lab.MOV', a=29.0, b=30.6, zoom=(1.0, 1.06))],
   kin=[(0.0, 1.6, [[('my', 70, W)], [('JAWLINE', 190, W)], [('routine', 90, W)]], 230),
        (1.6, 3.2, [[('ShapeShift', 150, W)]], 300),
        (3.2, 4.8, [[('1–2', 200, W), ('PUMPS', 120, W)]], 280),
        (4.8, 6.8, [[('gel-serum', 90, W)], [('TEXTURE', 160, W)]], 260),
        (6.8, 8.8, [[('UPWARD', 170, W)], [('neck to jaw', 80, W)]], 250),
        (8.8, 10.8, [[('MORNING', 160, W)], [('& NIGHT', 120, W)]], 250),
        (10.8, 12.2, [[('sculpted', 90, W)], [('LOOK', 200, W)]], 250),
        (12.2, 13.8, [[('ShapeShift', 140, W)], [('V-Line Jaw Defining Serum', 52, W)]], 280)],
   punch=[1.6, 3.2, 4.8, 6.8, 8.8, 10.8, 12.2],
   sfx=[(0.0, 'swish')]),
}


# ---------------------------------------------------------------- R · ShapeShift – real customer review (Polen's footage + a real woman's review and her real before/after)
import copy
SPEC['R'] = copy.deepcopy(SPEC['B'])
_R = SPEC['R']; _R['name'] = 'ShapeShift – Real customer review'; OFF = 4.6   # the real review opens the film
_R['segs'] = [dict(src=R + 'review/review_card.mp4', a=0.0, b=4.6)] + _R['segs'][:4] + [dict(src=SDR + 'ssba_2961.mov', a=11.5, b=15.0, speed=1.35)]
def _sh(lst): return [(x[0] + OFF, x[1] + OFF) + tuple(x[2:]) for x in lst]
_R['texts'] = _sh([x for x in _R['texts'] if x[0] < 12.8] + [(12.87, 15.47, 'upward,\nneck to jaw', 'slide', 330, 100, W)])
_R['inserts'] = _sh(_R['inserts']); _R['big'] = _sh(_R['big'])
_R['sfx'] = [(x[0] + OFF,) + tuple(x[1:]) for x in _R['sfx']] + [(0.3, 'pop')]


# ---------------------------------------------------------------- S · Success story (lab footage -> TODAY -> real review). Sound: stand-in Pixabay track; the Instagram sound (Tame Impala - Loser) is licensed and is added in the IG editor.
DJ = "/Users/ufo/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/.shortcut-targets-by-id/1yyhSrn9b9nAyKMqtNFz3D81sEOQiloUI/SickScience Brand Assets/Videos/SickScience Lab Videos (Experiments)/"
TODAY = "/Users/ufo/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/.shortcut-targets-by-id/1yyhSrn9b9nAyKMqtNFz3D81sEOQiloUI/SickScience Brand Assets/All UGC/SHAPESHIFT- UGC/TodayShow Edited Desktop.mp4"
def _dj(n): return DJ + [f for f in __import__('os').listdir(DJ) if f'_00{n}_D' in f][0]
SPEC['S'] = dict(name='SickScience – Success story from the lab', caps=False,
   music=(PX + 'amaksi-reflections-146299.mp3', 20.0, 0),
   segs=[dict(src=_dj(61), a=2.0, b=4.6, zoom=(1.0, 1.08)),            # scientist at the microscope
         dict(src=_dj(60), a=3.0, b=5.2, zoom=(1.08, 1.0)),
         dict(src=_dj(48), a=3.0, b=5.2, zoom=(1.0, 1.08)),
         dict(src=_dj(53), a=3.0, b=5.0, zoom=(1.08, 1.0)),
         dict(src=TODAY, a=9.0, b=12.0, crop='608:1080:656:0'),
         dict(src=R + 'review/review_card.mp4', a=0.0, b=3.2),
         dict(src=_dj(50), a=3.0, b=5.4, zoom=(1.0, 1.06))],
   kin=[(0.2, 2.5, [[('5 YEARS', 170, W)], [('in a lab', 86, W)]], 1150),
        (2.7, 4.7, [[('NO', 150, W)], [('shortcuts', 100, W)]], 1150),
        (4.9, 6.9, [[('ONE', 150, W)], [('formula', 100, W)]], 1150),
        (7.1, 9.0, [[('then it', 100, W)], [('WORKED', 160, W)]], 1150),
        (9.2, 12.1, [[('seen on', 90, W)], [('TODAY', 170, W)]], 1150),
        (15.2, 17.5, [[('just getting', 90, W)], [('STARTED', 170, W)]], 1150)],
   punch=[2.6, 4.8, 7.0, 9.1, 12.2], sfx=[(0.2, 'pop'), (2.7, 'pop'), (4.9, 'pop'), (7.1, 'pop'), (9.2, 'ding')])

import copy as _c
SPEC['S2'] = _c.deepcopy(SPEC['S']); SPEC['S2']['name'] = 'SickScience – Success story (müziksiz, IG sesi için)'
SPEC['S2']['music'] = (PX + 'amaksi-reflections-146299.mp3', 20.0, -80)
SPEC['S2']['sfx'] = []


# ---------------------------------------------------------------- S3 · Success story cut to the reel sound (user-supplied file, ~83 BPM, drop at 9.98 s, beat = 0.719 s)
REEL = R + 'reel/reel_audio.wav'
SPEC['S3'] = dict(name='SickScience – Success story (reel sesiyle)', caps=False,
   music=(REEL, 0.0, 0),
   segs=[dict(src=_dj(61), a=2.0, b=4.79, zoom=(1.0, 1.08)),
         dict(src=_dj(60), a=3.0, b=5.87, zoom=(1.08, 1.0)),
         dict(src=_dj(48), a=3.0, b=5.88, zoom=(1.0, 1.08)),
         dict(src=_dj(53), a=3.0, b=4.44, zoom=(1.08, 1.0)),
         dict(src=TODAY, a=9.0, b=10.44, crop='608:1080:656:0'),
         dict(src=TODAY, a=21.7, b=22.78, crop='608:1080:230:0'),
         dict(src=TODAY, a=22.78, b=23.86, crop='608:1080:690:0'),
         dict(src=R + 'review/review_card_fast.mp4', a=0.0, b=2.88),
         dict(src=_dj(50), a=3.0, b=4.54, zoom=(1.0, 1.06))],
   kin=[(0.2, 2.7, [[('5 YEARS', 170, W)], [('in a lab', 86, W)]], 1150),
        (2.95, 5.6, [[('NO', 150, W)], [('shortcuts', 100, W)]], 1150),
        (5.8, 8.5, [[('ONE', 150, W)], [('formula', 100, W)]], 1150),
        (8.6, 9.95, [[('then it', 100, W)]], 1150),
        (10.0, 11.4, [[('WORKED', 190, W)]], 1150),
        (11.5, 13.5, [[('seen on', 90, W)], [('TODAY', 170, W)]], 1150),
        (16.5, 17.95, [[('just getting', 90, W)], [('STARTED', 170, W)]], 1150)],
   punch=[2.79, 5.66, 8.54, 9.98, 11.42, 13.58, 16.46], sfx=[])


# ---------------------------------------------------------------- S4 · Success story v2 (reel sound; nicer lab shots; no review at the end)
_NM = [l.strip() for l in open('/private/tmp/claude-501/lab/names.txt')]
def _ix(i): return DJ + _NM[i - 1]
SPEC['S4'] = dict(name='SickScience – Success story v2 (reel sesiyle)', caps=False,
   music=(REEL, 0.0, 0),
   segs=[dict(src=_ix(3), a=37.0, b=39.79, zoom=(1.0, 1.08)),                 # scientist over the magenta rack
         dict(src=_ix(9), a=6.0, b=8.87, zoom=(1.08, 1.0)),                  # pipette over the plate
         dict(src=_ix(18), a=4.2, b=7.08, zoom=(1.0, 1.06)),                 # microscope screen, purple cells
         dict(src=_ix(22), a=3.0, b=4.44, zoom=(1.06, 1.0)),                 # hand marks the pink plate
         dict(src=TODAY, a=9.0, b=10.44, crop='608:1080:656:0'),
         dict(src=TODAY, a=21.7, b=22.78, crop='608:1080:230:0'),
         dict(src=TODAY, a=22.78, b=23.86, crop='608:1080:690:0'),
         dict(src=_ix(26), a=2.0, b=4.88, zoom=(1.0, 1.08)),                 # pipetting red medium
         dict(src=_ix(7), a=14.0, b=15.54, zoom=(1.0, 1.05))],               # smiling scientist
   kin=[(0.2, 2.7, [[('5 YEARS', 170, W)], [('in a lab', 86, W)]], 340),
        (2.95, 5.6, [[('NO', 150, W)], [('shortcuts', 100, W)]], 340),
        (5.8, 8.5, [[('ONE', 150, W)], [('formula', 100, W)]], 340),
        (8.6, 9.95, [[('then it', 100, W)]], 340),
        (10.0, 11.4, [[('WORKED', 190, W)]], 340),
        (11.5, 13.5, [[('seen on', 90, W)], [('TODAY', 170, W)]], 340),
        (13.7, 16.4, [[('backed by', 90, W)], [('SCIENCE', 170, W)]], 340),
        (16.5, 17.95, [[('just getting', 90, W)], [('STARTED', 170, W)]], 340)],
   punch=[2.79, 5.66, 8.54, 9.98, 11.42, 13.58, 16.46], sfx=[])


# ---------------------------------------------------------------- S5 · Success story v3: lab -> Ulta shelves at the drop (10 s) -> launch/team events -> ends with the founders
VID = "/Users/ufo/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/.shortcut-targets-by-id/1yyhSrn9b9nAyKMqtNFz3D81sEOQiloUI/SickScience Brand Assets/Videos/"
ULTA1 = VID + 'ultavids1.mp4'; LAUNCH = VID + 'Sickscience ULTA LAUNCH .mp4'
SPEC['S5'] = dict(name='SickScience – Success story v3 (reel sesiyle)', caps=False,
   music=(REEL, 0.0, 0),
   segs=[dict(src=_ix(3), a=37.0, b=39.79, zoom=(1.0, 1.08)),
         dict(src=_ix(9), a=6.0, b=8.87, zoom=(1.08, 1.0)),
         dict(src=_ix(18), a=4.2, b=7.08, zoom=(1.0, 1.06)),
         dict(src=_ix(22), a=3.0, b=4.44, zoom=(1.06, 1.0)),
         dict(src=ULTA1, a=14.5, b=15.94, zoom=(1.0, 1.06)),                 # drop: SickScience display on the Ulta shelf
         dict(src=ULTA1, a=10.5, b=12.66, zoom=(1.0, 1.05)),                 # Ulta shelves
         dict(src=LAUNCH, a=10.0, b=11.44, zoom=(1.0, 1.05)),                # team in lab coats at the Ulta counter
         dict(src=LAUNCH, a=4.6, b=6.04, zoom=(1.0, 1.05)),                  # founders cut the Ulta ribbon
         dict(src=LAUNCH, a=35.0, b=36.54, zoom=(1.04, 1.0))],               # founders with the product (end)
   kin=[(0.2, 2.7, [[('5 YEARS', 170, W)], [('in a lab', 86, W)]], 340),
        (2.95, 5.6, [[('NO', 150, W)], [('shortcuts', 100, W)]], 340),
        (5.8, 8.5, [[('ONE', 150, W)], [('formula', 100, W)]], 340),
        (8.6, 9.95, [[('then it', 100, W)]], 340),
        (10.0, 11.4, [[('WORKED', 190, W)]], 340),
        (11.5, 13.5, [[('now at', 90, W)], [('ULTA', 170, W)]], 340),
        (13.7, 16.4, [[('backed by', 90, W)], [('SCIENCE', 170, W)]], 340),
        (16.5, 17.95, [[('just getting', 90, W)], [('STARTED', 170, W)]], 340)],
   punch=[2.79, 5.66, 8.54, 9.98, 11.42, 13.58, 16.46], sfx=[], sfx_db=-9)
