# v4c outline from ChatGPT's script (chatgpt-v4-answer.txt): one two-page spread, 22 beats, ~119 s. Flat sketch only.
import math, os
from PIL import Image, ImageDraw
from storyboard import hand, grot, txt, figure, arrow, INK, YEL, VIO, SW, SH, PL, PR
from storyboard2 import base, circ, capsule, page_panel, wide_panel, RED, GRN, COB, GREY

R = os.path.dirname(os.path.abspath(__file__))


def star(d, x, y, r):
    pts = [(x + r * math.cos(math.radians(-90 + k * 36)) * (1 if k % 2 == 0 else 0.45), y + r * math.sin(math.radians(-90 + k * 36)) * (1 if k % 2 == 0 else 0.45)) for k in range(10)]
    d.polygon(pts, outline=INK, width=4)


def drone(d, x, y, s=1.0):
    d.line((x - 60 * s, y, x + 60 * s, y), fill=INK, width=4)
    for dx in (-60 * s, 60 * s):
        d.line((x + dx, y, x + dx, y - 16 * s), fill=INK, width=4); d.line((x + dx - 18 * s, y - 16 * s, x + dx + 18 * s, y - 16 * s), fill=INK, width=4)
    d.rectangle((x - 28 * s, y + 24 * s, x + 28 * s, y + 64 * s), outline=INK, width=4); d.line((x - 28 * s, y + 24 * s, x, y + 46 * s, x + 28 * s, y + 24 * s), fill=INK, width=4)


# ---- left page (00-64 s) ----
def l1(d):
    txt(d, 110, 150, 'THE BEGINNING', 40); figure(d, 170, 215); figure(d, 330, 215)
def l2(d):
    txt(d, 105, 445, 'POLEN', 38); txt(d, 270, 445, 'MERVE', 38)
    txt(d, 470, 215, '2009', 90, hl=YEL)
def l3(d):
    d.line((110, 540, 950, 540), fill=INK, width=5)
    for i in range(6): x = 120 + i * 162; d.line((x, 527, x, 553), fill=INK, width=4)
    txt(d, 110, 565, '14 YEARS', 84, hl=YEL); txt(d, 520, 590, 'Yeditepe · PhD ×2', 46)
def l4(d):
    txt(d, 480, 330, 'Polen: Harvard–MIT HST', 46); txt(d, 490, 390, 'research scholar', 34)
def l5(d):
    circ(d, 170, 740, 60); circ(d, 170, 740, 18)                                       # cell
    arrow(d, (360, 700), (420, 740)); arrow(d, (420, 760), (360, 800)); circ(d, 330, 750, 34)   # regen loop
    for k in range(6): circ(d, 560 + (k % 3) * 34, 720 + (k // 3) * 36, 11, 3)           # exosomes
    arrow(d, (680, 750), (760, 750), dotted=True); circ(d, 820, 750, 46)
    txt(d, 110, 820, 'stem cells', 34); txt(d, 300, 820, 'regenerative medicine', 34); txt(d, 600, 820, 'exosomes · cancer research', 34)
def l6(d):
    d.rectangle((110, 890, 190, 990), outline=INK, width=4); circ(d, 175, 975, 22); txt(d, 120, 900, 'PAT.', 28)
    for k in range(3): d.rectangle((215 + k * 14, 895 + k * 10, 285 + k * 14, 985 + k * 10), outline=INK, width=3, fill=(253, 252, 248))
    txt(d, 350, 900, '20–30 PAPERS', 76, hl=YEL)
def l7(d):
    txt(d, 110, 1030, 'for mom', 40)
def l8(d):
    txt(d, 300, 1032, 'preclinical research', 36); d.line((300, 1085, 640, 1085), fill=INK, width=2)
def l9(d):
    d.rectangle((690, 1025, 760, 1110), outline=INK, width=4); txt(d, 780, 1040, 'published', 40); d.line((935, 1070, 950, 1088, 980, 1045), fill=INK, width=5)
def l10(d):
    txt(d, 110, 1130, 'in the', 54); txt(d, 270, 1130, 'lab', 54, strike=True); txt(d, 380, 1110, 'at home', 66, hl=YEL)
def l11(d):
    circ(d, 220, 1310, 95); circ(d, 220, 1310, 26); d.ellipse((376, 1306, 384, 1314), fill=INK)
    arrow(d, (450, 1270), (392, 1302)); txt(d, 460, 1240, 'exosome', 40); txt(d, 640, 1225, '1/1000', 84, hl=YEL)
def l12(d):
    drone(d, 560, 1345, 0.7); arrow(d, (640, 1370), (760, 1370), dotted=True); circ(d, 830, 1370, 40)
    txt(d, 460, 1395, 'coded messages', 30)

# ---- right page (64-119 s) ----
def r1(d):
    txt(d, 1080, 150, 'THE SCIENCE', 40)
    for i, s in enumerate(['PINEAPPLE', 'GARLIC', 'WHEAT', 'RADISH']):
        x = 1160 + i * 220
        circ(d, x, 290, 62); circ(d, x, 290, 52, 2, (160, 170, 185))
        txt(d, x - 60, 360, f'FIG. 0{i + 1}', 28); txt(d, x - 60, 392, s, 30)
def r2(d):
    for i in range(4): d.line((1160 + i * 220, 430, 1500, 470), fill=(140, 145, 160), width=2)
    txt(d, 1080, 460, 'THOUSANDS', 80, hl=YEL); txt(d, 1500, 485, '100% plant-based · vegan', 40)
def r3(d):
    txt(d, 1080, 560, 'NX35', 110, hl=YEL)
    for i, s in enumerate(['SEPARATION', 'STABILIZATION', 'LIBRARY']):
        x = 1080 + i * 295
        d.rounded_rectangle((x, 690, x + 255, 760), 14, outline=INK, width=4); txt(d, x + 14, 700, s, 38)
        if i < 2: arrow(d, (x + 258, 725), (x + 292, 725))
    txt(d, 1080, 772, 'room temperature · no cold chain · biomimetic', 36)
def r4(d):
    txt(d, 1080, 830, 'scientist?', 58, strike=True); arrow(d, (1350, 866), (1440, 866)); txt(d, 1460, 830, 'marketer.', 58)
def r5(d):
    x, y = 1100, 920                                       # beaker -> bottle
    d.polygon([(x, y), (x + 60, y), (x + 70, y + 70), (x - 10, y + 70)], outline=INK, width=4)
    arrow(d, (1200, 955), (1300, 955)); d.rounded_rectangle((1320, 915, 1360, 995), 14, outline=INK, width=4)
    txt(d, 1400, 925, 'LAB', 58, hl=YEL); arrow(d, (1530, 960), (1610, 960)); txt(d, 1630, 925, 'HOME', 58, hl=YEL)
def r6(d):
    for k, h in enumerate([20, 38, 30, 56]): d.rectangle((1090 + k * 26, 1080 - h, 1110 + k * 26, 1080), outline=INK, width=3)
    txt(d, 1220, 1005, '"THAT\'S SICK!"', 80)
def r7(d):
    txt(d, 1080, 1100, "No, that's science.", 54); txt(d, 1520, 1090, 'SickScience', 84, col=VIO)
def r8(d):
    for i, (col, nm, part) in enumerate([(VIO, 'ShapeShift', 'neck + jaw'), (RED, 'NetWork', 'face'), (GRN, 'PowerCycle', 'hair'), (COB, 'DropOff', 'body')]):
        x = 1110 + i * 150
        big = nm == 'PowerCycle'
        capsule(d, x, 1200, col, '', h=110 if not big else 128, wd=36 if not big else 44)
        txt(d, x - 30, 1335, nm, 28); txt(d, x - 30, 1365, part, 26)
def r9(d):
    star(d, 1740, 1240, 36); txt(d, 1700, 1280, '14 AWARDS', 54, hl=YEL); txt(d, 1700, 1345, 'Oprah · InStyle · Esquire', 28)


BEATS = [
    ('COVER', 'L', None, None, '(finished spread) "For the first time, here\'s how SickScience began."'),
    ('00', 'L', l1, (95, 145, 460, 460), 'For the first time, here\'s how SickScience began. With two geneticists.'),
    ('05', 'L', l2, (95, 200, 700, 490), 'Polen Koçak-Denizci and Merve Yıldırım-Canpolat met in a chemistry and biology class in 2009.'),
    ('11', 'L', l3, (95, 520, 990, 660), 'They worked together for fourteen years. Both earned biotechnology PhDs at Yeditepe University.'),
    ('17', 'L', l4, (180, 320, 990, 440), 'Polen was also a research scholar at Harvard–MIT Health Sciences and Technology.'),
    ('23', 'L', l5, (95, 670, 990, 870), 'Together, they studied stem cell production, regenerative medicine, and exosome applications in cancer research.'),
    ('30', 'L', l6, (95, 880, 900, 1010), 'Their work includes international patents and twenty to thirty peer-reviewed papers.'),
    ('35', 'L', l7, (95, 1020, 280, 1090), 'For Merve, the research was personal. Her mother had mesothelioma, with no treatment available.'),
    ('43', 'L', l8, (290, 1020, 660, 1095), 'Their research was still preclinical when her mother passed away.'),
    ('48', 'L', l9, (680, 1015, 990, 1120), 'Afterward, they finished and published the research.'),
    ('51', 'L', l10, (95, 1100, 720, 1200), "Then they made a decision: take science beyond the lab, into people's homes."),
    ('55', 'L', l11, (95, 1205, 990, 1410), 'At the center of their work were exosomes. Tiny carriers, roughly one-thousandth the size of a cell.'),
    ('60', 'L', l12, (440, 1300, 990, 1430), 'Like delivery drones, they carry coded messages between cells.'),
    ('64', 'R', r1, (1070, 145, 1960, 435), 'Their exosomes come from plants: pineapple, garlic, wheat, and radish.'),
    ('69', 'R', r2, (1070, 440, 1960, 550), 'A library of thousands of plant messages. One hundred percent plant-based and vegan.'),
    ('75', 'R', r3, (1070, 555, 1960, 815), 'Then came NX35. A biomimetic platform combining exosome separation, room-temperature stabilization without a cold chain, and their plant library.'),
    ('84', 'R', r4, (1070, 820, 1750, 905), "Why beauty? Everyone says they're a scientist. Most are marketers."),
    ('89', 'R', r5, (1070, 905, 1760, 1005), 'These two wanted clinical-level science in formulas people could use at home.'),
    ('94', 'R', r6, (1070, 1000, 1700, 1090), "Then La Mer's marketing director saw their data and said, 'That's sick!'"),
    ('100', 'R', r7, (1070, 1085, 1960, 1185), "Their answer? 'No, that's science.' And that's how SickScience got its name."),
    ('105', 'R', r8, (1070, 1190, 1680, 1410), 'ShapeShift for the neck and jawline. NetWork for the face. PowerCycle for hair. DropOff for the body.'),
    ('112', 'R', r9, (1690, 1195, 1965, 1385), 'Four products. Fourteen awards, including recognition from Oprah, InStyle, and Esquire.'),
    ('116', 'R', None, None, 'Science, but never boring.'),
]


def main():
    sp = base(1); d = ImageDraw.Draw(sp)
    for b in BEATS:
        if b[2]: b[2](d)
    sp.save(os.path.join(R, 'spread_v4c.png'))
    sp = base(1); d = ImageDraw.Draw(sp); panels = []
    for k, side, fn, box, nar in BEATS:
        if fn:
            fn(d); panels.append((k, nar, page_panel(sp, side, box)))
    final = Image.open(os.path.join(R, 'spread_v4c.png'))
    panels.insert(0, ('0:00', BEATS[0][4], wide_panel(final, 'FOR THE FIRST TIME', "here's how SickScience began", ['finished spread first,', 'then cut to the empty page'])))
    panels.append(('1:56', BEATS[-1][4], wide_panel(final, 'SICK SCIENCE', 'Science, but never boring.', ['back to the wide spread,', 'real 4-product photo below'], VIO)))
    cols = 8; cw, ch, cap = 240, 427, 190
    rows = math.ceil(len(panels) / cols)
    sheet = Image.new('RGB', (cols * (cw + 10) + 10, rows * (ch + cap + 10) + 10), 'white'); sd = ImageDraw.Draw(sheet)
    for i, (k, nar, p) in enumerate(panels):
        x = 10 + (i % cols) * (cw + 10); y = 10 + (i // cols) * (ch + cap + 10)
        sheet.paste(p.resize((cw, ch)), (x, y)); sd.rectangle((x, y, x + cw - 1, y + ch - 1), outline=(200, 200, 205))
        lab = k if ':' in k else f'0:{int(k):02d}' if int(k) < 60 else f'{int(k) // 60}:{int(k) % 60:02d}'
        sd.text((x, y + ch + 6), lab, font=grot(24), fill=VIO)
        f = grot(17); words, line, ly = nar.split(), '', y + ch + 36
        for wd in words:
            t = (line + ' ' + wd).strip()
            if sd.textlength(t, font=f) > cw - 6: sd.text((x, ly), line, font=f, fill=INK); ly += 21; line = wd
            else: line = t
        sd.text((x, ly), line, font=f, fill=INK)
    sheet.save(os.path.join(R, 'storyboard_v4c.jpg'), quality=90)
    print('ok', len(panels))


main()
