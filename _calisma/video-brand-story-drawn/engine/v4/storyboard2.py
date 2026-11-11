# v4b rough outline: more information, two spreads (pages 01-02, 03-04). Flat sketch only.
import math, os
from PIL import Image, ImageDraw
from storyboard import hand, grot, txt, figure, arrow, INK, GRID, YEL, VIO, SW, SH, PL, PR, PT, PB

R = os.path.dirname(os.path.abspath(__file__))
RED, GRN, COB = (205, 40, 50), (40, 150, 70), (40, 60, 170)
GREY = (120, 125, 140)


def base(n):
    im = Image.new('RGB', (SW, SH), (238, 239, 240))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((30, 40, SW - 30, SH - 20), 18, fill=(250, 250, 250), outline=(225, 225, 228), width=3)
    for j, (x0, x1) in enumerate((PL, PR)):
        d.rectangle((x0, 60, x1, SH - 40), fill=(253, 252, 248))
        for x in range(x0 + 20, x1 - 10, 28):
            d.line((x, PT - 20, x, PB), fill=GRID)
        for y in range(PT - 20, PB, 28):
            d.line((x0 + 20, y, x1 - 20, y), fill=GRID)
        d.text((x0 + 24, 78), 'LAB NOTEBOOK', font=grot(30), fill=GREY)
        d.text((x1 - 330, 78), 'PROJECT: SICKSCIENCE', font=grot(26), fill=GREY)
        d.text((x0 + 24, 112), f'page 0{n + j}', font=hand(30), fill=GREY)
    d.line((1020, 50, 1020, SH - 30), fill=(215, 215, 218), width=6)
    return im


def circ(d, x, y, r, w=4, col=INK):
    d.ellipse((x - r, y - r, x + r, y + r), outline=col, width=w)


def capsule(d, x, y, col, label, h=150, wd=46):
    d.rounded_rectangle((x, y, x + wd, y + h), wd // 2, outline=INK, width=4)
    d.rounded_rectangle((x + 3, y + 3, x + wd - 3, y + h // 2), wd // 2, fill=col)
    txt(d, x - 30, y + h + 8, label, 36)


# ---------------- spread A: pages 01 (who) + 02 (what) ----------------
def a1(d):
    figure(d, 170, 180); figure(d, 320, 180)
    txt(d, 115, 410, 'Polen, PhD', 34); txt(d, 270, 410, 'Merve, PhD', 34)
    txt(d, 450, 190, '2 geneticists', 66)
def a2(d):
    txt(d, 450, 280, 'chemistry class', 44); txt(d, 760, 270, '2009', 70, hl=YEL)
    x, y = 470, 380                                   # grad cap
    d.polygon([(x, y), (x + 60, y - 25), (x + 120, y), (x + 60, y + 25)], outline=INK, width=4)
    d.line((x + 30, y + 12, x + 30, y + 45), fill=INK, width=4); d.line((x + 90, y + 12, x + 90, y + 45), fill=INK, width=4)
    txt(d, 610, 360, 'PhD Biotechnology ×2', 44)
def a3(d):
    txt(d, 110, 480, 'Harvard–MIT', 58, hl=YEL); txt(d, 470, 498, '(research scholar, Polen)', 34)
    x, y = 150, 590                                   # microscope
    d.rectangle((x - 50, y + 150, x + 60, y + 170), outline=INK, width=4)
    d.line((x + 30, y + 150, x + 30, y + 30), fill=INK, width=5); d.line((x + 30, y + 30, x - 20, y), fill=INK, width=5)
    d.rectangle((x - 40, y - 25, x - 5, y + 30), outline=INK, width=4); d.line((x - 30, y + 95, x + 30, y + 95), fill=INK, width=4)
    for i, s in enumerate(['stem cells', 'regenerative medicine', 'exosomes in cancer treatment']):
        txt(d, 260, 580 + i * 52, '• ' + s, 44)
def a4(d):
    d.line((110, 820, 950, 820), fill=INK, width=5)
    for i, yr in enumerate(['2009', '2012', '2015', '2018', '2021', '2023']):
        x = 120 + i * 162; d.line((x, 805, x, 835), fill=INK, width=4); txt(d, x - 26, 842, yr, 28)
    txt(d, 110, 900, '14 YEARS', 76, hl=YEL)
    circ(d, 520, 945, 52); txt(d, 478, 925, 'PATENT', 30)
    txt(d, 600, 905, '20–30 papers', 62, hl=YEL)
def a5(d):
    x, y = 140, 1065
    d.polygon([(x, y + 50), (x - 40, y + 10), (x - 25, y - 15), (x, y + 2), (x + 25, y - 15), (x + 40, y + 10)], outline=INK, width=4)
    txt(d, 210, 1030, "Merve's mom · no cure", 46); txt(d, 210, 1088, 'research: still preclinical', 42)
def a6(d):
    txt(d, 110, 1180, 'finished ✓  published ✓', 46)
    txt(d, 110, 1270, 'the lab', 62, strike=True); arrow(d, (320, 1305), (440, 1305))
    x, y = 500, 1255
    d.polygon([(x, y + 30), (x + 60, y - 20), (x + 120, y + 30)], outline=INK, width=4); d.rectangle((x + 12, y + 30, x + 108, y + 110), outline=INK, width=4)
    txt(d, 650, 1265, 'homes', 70, hl=YEL)
def a7(d):
    txt(d, 1080, 170, 'exosomes =', 56); txt(d, 1080, 232, 'coded messages to cells', 58, hl=YEL)
    circ(d, 1160, 410, 70); circ(d, 1160, 410, 20); circ(d, 1860, 410, 70); circ(d, 1860, 410, 20)
    x, y = 1510, 370
    d.line((x - 70, y, x + 70, y), fill=INK, width=4)
    for dx in (-70, 70): d.line((x + dx, y, x + dx, y - 20), fill=INK, width=4); d.line((x + dx - 22, y - 20, x + dx + 22, y - 20), fill=INK, width=4)
    d.rectangle((x - 35, y + 30, x + 35, y + 80), outline=INK, width=4); d.line((x - 35, y + 30, x, y + 58, x + 35, y + 30), fill=INK, width=4)
    arrow(d, (1240, 415), (1420, 410), dotted=True); arrow(d, (1600, 410), (1780, 415), dotted=True)
    txt(d, 1430, 470, 'like a delivery drone', 36)
def a8(d):
    circ(d, 1180, 640, 100); txt(d, 1110, 750, 'a cell', 40)
    d.ellipse((1396, 636, 1404, 644), fill=INK); arrow(d, (1470, 600), (1412, 634))
    txt(d, 1480, 560, 'an exosome', 44)
    txt(d, 1480, 620, '1/1000', 84, hl=YEL); txt(d, 1480, 720, 'the size of a cell', 44)
def a9(d):
    for i, s in enumerate(['pineapple', 'garlic', 'wheat', 'radish']):
        x = 1110 + i * 215
        circ(d, x + 80, 900, 78); circ(d, x + 80, 900, 66, 2, (160, 170, 185))
        txt(d, x + 15, 985, f'FIG. 0{i + 1}', 28); txt(d, x + 15, 1018, s, 34)
    txt(d, 1090, 1075, '100% plant-derived · vegan', 50)
def a10(d):
    txt(d, 1090, 1170, 'a library of', 48); txt(d, 1350, 1150, 'THOUSANDS', 84, hl=YEL)
    for r in range(3):                               # little library rack
        for c in range(14):
            circ(d, 1110 + c * 58, 1290 + r * 44, 14, 3)


# ---------------- spread B: pages 03 (how) + 04 (what you get) ----------------
def b1(d):
    txt(d, 110, 170, 'the hard part:', 50); txt(d, 430, 160, 'fragile', 70, hl=YEL)
    sx, sy = 180, 330
    for a in range(0, 180, 60):
        r = math.radians(a); d.line((sx - 50 * math.cos(r), sy - 50 * math.sin(r), sx + 50 * math.cos(r), sy + 50 * math.sin(r)), fill=INK, width=4)
    txt(d, 270, 300, 'usually needs to stay cold', 46)
def b2(d):
    txt(d, 110, 430, 'NX35', 130, hl=YEL)
    for i, s in enumerate(['separate', 'stabilise', 'match']):
        x = 110 + i * 300
        d.rounded_rectangle((x, 620, x + 250, 720), 16, outline=INK, width=4); txt(d, x + 24, 640, s, 46)
        if i < 2: arrow(d, (x + 255, 670), (x + 295, 670))
    txt(d, 160, 735, 'exosomes', 32); txt(d, 430, 735, 'room temp', 32); txt(d, 720, 735, 'from the library', 32)
    x, y = 130, 820                                   # thermometer ✓
    d.rounded_rectangle((x, y, x + 30, y + 110), 15, outline=INK, width=4); circ(d, x + 15, y + 125, 26)
    txt(d, 190, 840, 'room temp ✓', 48)
    sx, sy = 560, 880
    for a in range(0, 180, 60):
        r = math.radians(a); d.line((sx - 36 * math.cos(r), sy - 36 * math.sin(r), sx + 36 * math.cos(r), sy + 36 * math.sin(r)), fill=INK, width=4)
    d.line((sx - 50, sy + 40, sx + 50, sy - 40), fill=INK, width=6); txt(d, 620, 850, 'no cold chain', 48)
def b3(d):
    txt(d, 110, 1010, 'why beauty?', 50)
    txt(d, 110, 1080, 'scientist?', 62, strike=True); arrow(d, (390, 1118), (490, 1118)); txt(d, 510, 1080, 'marketer.', 62)
def b4(d):
    x, y = 150, 1250                                  # clinic cross
    d.rectangle((x - 15, y - 45, x + 15, y + 45), outline=INK, width=4); d.rectangle((x - 45, y - 15, x + 45, y + 15), outline=INK, width=4)
    txt(d, 220, 1210, 'clinic-level science', 50); arrow(d, (230, 1300), (330, 1300)); txt(d, 350, 1265, 'at home', 66, hl=YEL)
def b5(d):
    txt(d, 1080, 170, '4 formulas', 66, hl=YEL)
    for i, (col, nm, part) in enumerate([(VIO, 'ShapeShift', 'jaw + neck'), (RED, 'NetWork', 'face'), (GRN, 'PowerCycle', 'hair'), (COB, 'DropOff', 'body')]):
        x = 1130 + i * 215
        capsule(d, x, 290, col, nm, h=170 if nm != 'PowerCycle' else 200, wd=50 if nm != 'PowerCycle' else 60)
        txt(d, x - 20, 540, part, 40)
def b6(d):
    x, y = 1150, 700                                  # star
    pts = [(x + 60 * math.cos(math.radians(-90 + k * 36)) * (1 if k % 2 == 0 else 0.45), y + 60 * math.sin(math.radians(-90 + k * 36)) * (1 if k % 2 == 0 else 0.45)) for k in range(10)]
    d.polygon(pts, outline=INK, width=4)
    txt(d, 1240, 650, '14 awards', 80, hl=YEL); txt(d, 1240, 750, 'incl. Oprah, InStyle & Esquire', 44)
def b7(d):
    txt(d, 1080, 880, 'the name?', 50)
    d.rounded_rectangle((1080, 960, 1430, 1040), 30, outline=INK, width=4); txt(d, 1110, 964, '"That\'s sick!"', 52)
    txt(d, 1450, 975, '— a beauty exec', 38)
    d.rounded_rectangle((1080, 1070, 1560, 1150), 30, outline=INK, width=4); txt(d, 1100, 1074, '"No, that\'s science."', 50)
    txt(d, 1580, 1085, '— them', 38)
def b8(d):
    txt(d, 1180, 1210, 'Sick', 120); txt(d, 1450, 1210, 'Science', 120, col=VIO)


SPREADS = {'A': 1, 'B': 3}
BEATS = [  # (key, spread, narration, fn, page side, new-element box)
    ('COVER', 'A', 'For the first time: the story of SickScience.', None, None, None),
    ('01', 'A', 'SickScience started with two geneticists: Polen Koçak-Denizci and Merve Yıldırım-Canpolat.', a1, 'L', (95, 165, 860, 450)),
    ('02', 'A', 'They met in a chemistry class in 2009, and both went on to a PhD in biotechnology.', a2, 'L', (440, 260, 990, 430)),
    ('03', 'A', 'Polen became a research scholar at Harvard–MIT. Together they worked on stem cells, regenerative medicine, and exosomes in cancer treatment.', a3, 'L', (95, 470, 990, 770)),
    ('04', 'A', 'Fourteen years in the lab. International patents. Twenty to thirty peer-reviewed papers.', a4, 'L', (95, 790, 990, 1000)),
    ('05', 'A', "Then it got personal. Merve's mother had a cancer with no cure, and their research was still preclinical.", a5, 'L', (95, 1020, 860, 1150)),
    ('06', 'A', "They finished the research and published it. And they decided their science shouldn't stay in the lab.", a6, 'L', (95, 1170, 880, 1375)),
    ('07', 'A', 'Their tool: exosomes. Tiny carriers that deliver coded messages to cells, like delivery drones.', a7, 'R', (1070, 160, 1960, 520)),
    ('08', 'A', 'And they really are tiny: about one-thousandth the size of a cell.', a8, 'R', (1070, 530, 1960, 800)),
    ('09', 'A', "Theirs come from plants: pineapple, garlic, wheat, radish. One hundred percent plant-derived, and vegan.", a9, 'R', (1070, 810, 1960, 1135)),
    ('10', 'A', 'Over the years they built a library of thousands of plant messages.', a10, 'R', (1070, 1140, 1960, 1400)),
    ('11', 'B', 'The hard part? Exosomes are fragile. They usually need to stay cold.', b1, 'L', (95, 150, 990, 390)),
    ('12', 'B', 'So they built NX35: it separates the exosomes, keeps them stable at room temperature, and matches them from the library. No cold chain.', b2, 'L', (95, 420, 990, 960)),
    ('13', 'B', "Why beauty? Because everyone in beauty says they're a scientist. Most are marketers.", b3, 'L', (95, 1000, 860, 1160)),
    ('14', 'B', 'Their goal: clinic-level science, in a formula you use at home.', b4, 'L', (95, 1190, 860, 1360)),
    ('15', 'B', 'Four formulas. ShapeShift for the jawline and neck. NetWork for the face. PowerCycle for the hair. DropOff for the body.', b5, 'R', (1070, 160, 1960, 590)),
    ('16', 'B', 'Fourteen awards so far, including Oprah, InStyle and Esquire.', b6, 'R', (1070, 630, 1960, 810)),
    ('17', 'B', 'And the name? A beauty executive saw their data and said: "That\'s sick!" They said: "No, that\'s science."', b7, 'R', (1070, 870, 1960, 1160)),
    ('18', 'B', 'SickScience.', b8, 'R', (1070, 1190, 1960, 1370)),
    ('END', 'B', 'Science, but never boring.', None, None, None),
]


def page_panel(sp, side, box):
    s2 = sp.copy(); dd = ImageDraw.Draw(s2)
    if box: dd.rounded_rectangle(box, 16, outline=VIO, width=6)
    pc = (PL[0] + PL[1]) / 2 - 8 if side == 'L' else (PR[0] + PR[1]) / 2 - 8
    return s2.crop((int(pc - 416), 0, int(pc + 416), SH)).resize((540, 960))


def wide_panel(sp, head, sub, note=None, sub_col=INK):
    P = Image.new('RGB', (540, 960), (245, 245, 246)); d = ImageDraw.Draw(P)
    P.paste(sp.resize((540, int(540 * SH / SW))), (0, 300))
    f = grot(40); tw = d.textlength(head, font=f); d.text(((540 - tw) / 2, 150), head, font=f, fill=INK)
    f2 = hand(44); tw = d.textlength(sub, font=f2); d.text(((540 - tw) / 2, 205), sub, font=f2, fill=sub_col)
    if note:
        for i, ln in enumerate(note): d.text((40, 740 + i * 32), ln, font=grot(24), fill=GREY)
    return P


def main():
    sp = {'A': base(1), 'B': base(3)}
    dr = {k: ImageDraw.Draw(v) for k, v in sp.items()}
    panels = []
    for k, s, nar, fn, side, box in BEATS:
        if fn: fn(dr[s])
        if k == 'COVER':
            panels.append([k, nar, None])
        elif k == 'END':
            P = wide_panel(sp['B'], 'SICK SCIENCE', 'Science, but never boring.', ['zoom out to the full spread,', 'then the real 4-product photo (S_0723)'], VIO)
            panels.append([k, nar, P])
        else:
            panels.append([k, nar, page_panel(sp[s], side, box)])
        if k == '10':
            panels.append(['TURN', 'Page turn: pull back to spread 01–02, flip to 03–04.', wide_panel(sp['A'], 'PAGE TURN', 'pages 01–02 done', ['pull back to the full spread,', 'flip the page to the empty 03–04'])])
    panels[0][2] = wide_panel(sp['A'], 'FOR THE FIRST TIME', 'the story of SickScience', ['finished spread first (ending shown first),', 'then cut to the empty page 01'])
    sp['A'].save(os.path.join(R, 'spread_A.png')); sp['B'].save(os.path.join(R, 'spread_B.png'))
    cols = 7; cw, ch, cap = 270, 480, 175
    rows = math.ceil(len(panels) / cols)
    sheet = Image.new('RGB', (cols * (cw + 10) + 10, rows * (ch + cap + 10) + 10), 'white'); sd = ImageDraw.Draw(sheet)
    for i, (k, nar, p) in enumerate(panels):
        x = 10 + (i % cols) * (cw + 10); y = 10 + (i // cols) * (ch + cap + 10)
        sheet.paste(p.resize((cw, ch)), (x, y)); sd.rectangle((x, y, x + cw - 1, y + ch - 1), outline=(200, 200, 205))
        sd.text((x, y + ch + 6), k, font=grot(26), fill=VIO)
        f = grot(19); words, line, ly = nar.split(), '', y + ch + 38
        for wd in words:
            t = (line + ' ' + wd).strip()
            if sd.textlength(t, font=f) > cw - 6: sd.text((x, ly), line, font=f, fill=INK); ly += 23; line = wd
            else: line = t
        sd.text((x, ly), line, font=f, fill=INK)
    sheet.save(os.path.join(R, 'storyboard_v4b.jpg'), quality=90)
    words = sum(len(n.split()) for _, _, n, *_ in BEATS)
    print('ok words', words, 'est sec', round(words / 2.5))


if __name__ == "__main__":
    main()
