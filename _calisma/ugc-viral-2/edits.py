# 10 new UGC viral edits (2026-11-10). segs = (first words, last words) of the creator's own speech, or (t0, t1) seconds.
E = {
 '01': dict(name='ShapeShift – Today show best jawline', caps=True, zoom=False, pk='ss', srcdim=(1920,1080),
     lcrop={0:(0.30,0.50), 1:(0.45,0.52), 2:(0.38,0.72), 3:(0.50,0.56), 4:(0.28,0.28)},
     segs=[('This is a new brand','science is insane.'), ("So it's called",'Jaw -Defining Serum'), ('Look at this','before and after.'),
           ('So the chemists','smooth, and tighten.'), ('Gorgeous sculpted jawline.','love it.')]),
 '02': dict(name='DropOff – Workout in a bottle', caps=True, zoom=False, pk='do',
     segs=[('This is basically','exaggerating.'), ("It's a body sculpting",'SixScience.'), ('My skin looks tighter','confident in my body.'),
           ('Honestly, my stomach','biggest insecurity,'), ("I'm toned smooth",'super confident.')]),
 '03': dict(name='DropOff – Stretch marks after baby', caps=True, zoom=False, pk='do',
     segs=[('but are we thinking','rest of our body?'), ('It helps to sculpt','smoother look and feel.'), ('It also helps reduce','of cellulite.'),
           ('Also helps fade','had a baby,'), ('All you need to do','morning and night.')]),
 '04': dict(name='Routine – 6.30 AM three steps', caps=True, zoom=False, pk='do',
     segs=[("Good morning, it's 6",'in the morning'), ('after birth I hate','sagging'), ('then my hero product','shape shifts'),
           ('last step we have power','cycle'), ("that's why I prefer",'twice a day')]),
 '05': dict(name='ShapeShift – 30 day jawline', caps=False, zoom=False, pk='ss',
     segs=[("Here's my jawline before",'Shapeshift.'), ("It's on the cutting",'edge of science.'), ('The founders spent','results prove it.')]),
 '06': dict(name='ShapeShift – Science in a bottle', caps=True, zoom=False, pk='ss',
     segs=[('I cannot believe','this smart.'), ('This is science','in a bottle.'), ('It improves skin firmness','sculpted jawline.'),
           ('Time for proof.','day 27.'), ('You want to try it?','try it?')]),
 '07': dict(name='NetWork – Skin cells talking', caps=True, zoom=False, pk='nw',
     segs=[('Exosomes help skin','real regeneration.'), ('This is Six Science','exosome technology.'), ('I layer it under','perfect combo.')]),
 '08': dict(name='NetWork – Blurs pores like a primer', caps=True, zoom=False, pk='nw',
     segs=[('Its smooth texture','like a primer.'), ('Sick Sciences Network','cellular level.'), ('I love applying','hydrated all day.')]),
 '09': dict(name='PowerCycle – Not just another serum', caps=False, zoom=False, pk='pc',
     segs=[('This is not just','another serum.'), ("It's powered by exosomes",'regeneration.'), ('PowerCycle helps restore','from the root.')]),
 '10': dict(name='PowerCycle – Thicker and fuller in 4 weeks', caps=True, zoom=False, pk='pc',
     segs=[('My hair is thicker','fuller.'), ('PowerCycle is a liquid','hair structure.'), ('I apply the serum','massage it.'), ("I'm happy with",'4 weeks.')]),

 '11': dict(name='Exosomes – The delivery truck', caps=True, zoom=False, pk='ss',
     segs=[(0, 2.35), (2.85, 11.9), (12.3, 39.05), (39.45, 50.65), (51.55, 53.0)],
     spot=[],
     ptr=[(1.0, 2.8, 'truck', 'EXOSOME', 'big'),
          (15.9, 17.3, 'blue', 'PROTEINS', 'thin'), (18.6, 19.7, 'pink', 'LIPIDS', 'thin'), (21.2, 22.6, 'yellow', 'OTHER|MOLECULES', 'thin')],
     mini=[(34.2, 41.9)],
     trucks=[dict(app=9.0, cargo=[16.5, 19.6, 21.6], drive=(23.4, 26.9), hide=27.8), dict(app=47.6, cargo=[-1, -1, -1], drive=(49.6, 52.6), hide=52.99)]),
}
STYLE = {
 '11': dict(cap='blur', big='spin', bpm=100, key='C'),
 '01': dict(cap='blur', big='drop', bpm=108, key='C'),
 '02': dict(cap='pop', big='spin', bpm=116, key='A', tick=True),
 '03': dict(cap='slide', big='blur', bpm=104, key='F'),
 '04': dict(cap='pop', big='slide', bpm=112, key='D', tick=True),
 '05': dict(cap='pop', big='spin', bpm=100, key='G'),
 '06': dict(cap='spin', big='pop', bpm=118, key='E'),
 '07': dict(cap='slide', big='blur', bpm=106, key='A'),
 '08': dict(cap='blur', big='drop', bpm=110, key='B'),
 '09': dict(cap='pop', big='spin', bpm=114, key='D'),
 '10': dict(cap='drop', big='pop', bpm=112, key='C'),
}
BIG = {
 '01': [('INSANE', 'insane.', 0, 'ss')],
 '02': [('WORKOUT', 'workout', 0, 'do')],
 '03': [('CELLULITE', 'cellulite.', 2, 'do')],
 '04': [('6:30 AM', '6', 0, 'do')],
 '05': [('BEFORE', 'before', 0, 'ss'), ('AFTER', 'after', 0, 'ss')],
 '06': [('SMART', 'smart.', 0, 'ss')],
 '07': [('COMMUNICATE', 'communicate', 0, 'nw')],
 '08': [('PRIMER', 'primer.', 0, 'nw')],
 '09': [('EXOSOMES', 'exosomes', 1, 'pc')],
 '10': [('4 WEEKS', '4', 3, 'pc')],
}
METAL = {}
FUN = {'02': dict(punch=['workout', 'bottle', 'insecurity,', 'confident.'], emoji={'bottle': '\U0001F4AA'}, shake=[])}
# (t_in, t_out, kind, line1/num, line2, product) in OUTPUT seconds
CHIPS = {
 '01': [(0.3, 3.3, 'chip', 'As seen on TODAY', '', 'ss')],
 '02': [(3.6, 6.8, 'chip', 'DropOff', 'Body Sculpting Serum', 'do')],
 '03': [(2.4, 5.6, 'chip', 'DropOff', 'Body Sculpting Serum', 'do')],
 '04': [(3.6, 6.5, 'chip', '1 · DropOff', 'Body Sculpting Serum', 'do'), (6.7, 10.8, 'chip', '2 · ShapeShift', 'V-Line Jaw Defining Serum', 'ss'),
        (11.0, 15.5, 'chip', '3 · PowerCycle', 'Hair Growth Scalp Serum', 'pc')],
 '05': [(5.2, 8.8, 'chip', 'ShapeShift', 'V-Line Jaw Defining Serum', 'ss'), (9.0, 11.9, 'chip', 'NX35 exosome technology', '', 'ss')],
 '06': [(3.6, 7.0, 'chip', 'ShapeShift', 'V-Line Jaw Defining Serum', 'ss'), (7.2, 11.2, 'chip', 'DAY 1 TO DAY 27', '', 'ss')],
 '07': [(3.7, 7.5, 'chip', 'NetWork', 'Rich Concentrated Serum', 'nw')],
 '08': [(6.0, 10.0, 'chip', 'NetWork', 'Rich Concentrated Serum', 'nw')],
 '09': [(2.6, 7.0, 'chip', 'PowerCycle', 'Hair Growth Scalp Serum', 'pc')],
 '10': [(2.2, 5.6, 'chip', 'PowerCycle', 'Hair Growth Scalp Serum', 'pc')],
}

INSERTS = {'11': []}

PX = "/Users/ufo/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/INO Claude Ads/motion-assets/_music/pixabay/"
MUSIC = {  # one different real track per video (Pixabay, from the INO library), start offset in s
 '01': (PX + 'sub_clair-luxury-595403.mp3', 12), '02': (PX + 'bransboynd-fresh-457883.mp3', 20), '03': (PX + 'alexgrohl-sweet-life-438146.mp3', 10),
 '04': (PX + 'penguinmusic-lazy-day-239287.mp3', 8), '05': (PX + '9jackjack8-luxury-snap-565802.mp3', 5), '06': (PX + 'jaystacksbeats-luxury-fashion-perfume-456773.mp3', 25),
 '07': (PX + 'pumpupthemind-once-in-paris-168895.mp3', 15), '08': (PX + 'lnplusmusic-fashion-fashion-music-611042.mp3', 10), '09': (PX + 'andriih-luxury-luxury-music-614300.mp3', 20),
 '10': (PX + 'paulyudin-fashion-fashion-music-574009.mp3', 18), '11': (PX + 'amaksi-reflections-146299.mp3', 60),
}

SYNTH = {'01','02','03','04','05','06','07','08','09','10'}   # approved edits keep their original bed
