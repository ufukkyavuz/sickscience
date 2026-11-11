# UGC viral 3 specs (2026-11-11). Times: segs in SOURCE seconds; texts/big/inserts/emoji/sfx in OUTPUT seconds.
import os
R = os.path.dirname(os.path.abspath(__file__)) + '/src/'
SDR = '/private/tmp/claude-501/v3/sdr/'   # Apple-tone-mapped copies of the HLG iPhone raws (tools/hlg2sdr), rebuildable
PX = "/Users/ufo/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/INO Claude Ads/motion-assets/_music/pixabay/"
G = R + 'myth-gorsel/'
W = (255, 255, 255)

SPEC = {
 # ---------------------------------------------------------------- 2 · ShapeShift before/after (DropOff format)
 'B': dict(name='ShapeShift – That was my before', caps=True, fix={'before': 'before.', 'after': 'after.'},
   music=(PX + 'bombinsound-happy-advertising-hip-hop-magic-moments-628139.mp3', 2.0, -17),
   # 'that was my before' -> her own before photo pops up where her finger points (upper right), she keeps pointing
   segs=[dict(src=R + 'ssba_edit.mp4', a=0.45, b=8.05, audio=True),
         dict(src=R + 'ssba_edit.mp4', a=8.05, b=10.12, audio=True),
         dict(src=SDR + 'ssba_2959.mov', a=2.0, b=3.6),
         dict(src=SDR + 'ssba_2961.mov', a=8.0, b=9.6),
         dict(src=SDR + 'ssba_2961.mov', a=12.0, b=15.0),
         dict(src=SDR + 'ssba_2962.mov', a=17.6, b=19.8)],
   inserts=[(1.67, 4.4, R + 'ss_before_jaw.jpg', 760, 390, 380, 'card', None)],
   texts=[(1.8, 4.4, 'BEFORE', 'pop', 600, 76, W, 760),
          (9.67, 11.27, 'ShapeShift', 'slide', 330, 110, W),
          (11.27, 12.87, '1–2 pumps', 'slide', 330, 100, W),
          (12.87, 15.87, 'upward,\nneck to jaw', 'slide', 330, 100, W),
          (15.87, 18.07, 'twice a day', 'slide', 330, 100, W)],
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
