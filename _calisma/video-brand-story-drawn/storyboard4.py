# v4d outline: ChatGPT v4b script (chatgpt-v4b-answer.txt), 2 pages, Biro Script Plus, wobbly ballpoint-pen sketches.
import math, os, random
from PIL import Image, ImageDraw, ImageFont

R = os.path.dirname(os.path.abspath(__file__))
F = os.path.expanduser('~/Library/Fonts/')
random.seed(11)
BIRO = lambda s: ImageFont.truetype(F + 'BiroScriptUSPlus-Regular.ttf', s)
BIROB = lambda s: ImageFont.truetype(F + 'BiroScriptUSPlus-Bold.ttf', s)
GROT = lambda s: ImageFont.truetype(F + 'FoundersGrotesk-Medium.otf', s)
INK, GRID, YEL, VIO = (28, 34, 70), (206, 215, 228), (255, 226, 70), (169, 33, 192)
RED, GRN, COB, GREY = (205, 40, 50), (40, 150, 70), (40, 60, 170), (120, 125, 140)
SW, SH = 2040, 1480
PL, PR = (60, 1000), (1040, 1980)
PT, PB = 150, 1420


# ---------- ballpoint helpers: every stroke wobbles and is gone over twice ----------
def wob(pts, amp=1.6, step=10):
    out = []
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        n = max(1, int(math.dist(pts[i], pts[i + 1]) / step))
        for k in range(n):
            t = k / n
            out.append((x0 + (x1 - x0) * t + random.uniform(-amp, amp), y0 + (y1 - y0) * t + random.uniform(-amp, amp)))
    out.append(pts[-1])
    return out


def pen(d, pts, w=3, col=INK, passes=2):
    for p in range(passes):
        d.line(wob(pts), fill=col, width=w if p == 0 else max(1, w - 1), joint='curve')


def pline(d, a, b, **k): pen(d, [a, b], **k)


def pcirc(d, x, y, r, **k):
    n = max(18, int(r / 2))
    a0 = random.uniform(0, 6.28)
    pen(d, [(x + r * math.cos(a0 + 6.4 * i / n), y + r * math.sin(a0 + 6.4 * i / n)) for i in range(n + 1)], **k)


def prect(d, x0, y0, x1, y1, **k): pen(d, [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)], **k)


def arrow(d, a, b, dotted=False):
    if dotted:
        n = int(math.dist(a, b) // 16)
        for i in range(0, n, 2):
            pline(d, (a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n), (a[0] + (b[0] - a[0]) * (i + 1) / n, a[1] + (b[1] - a[1]) * (i + 1) / n), passes=1)
    else:
        pline(d, a, b)
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    for s in (0.45, -0.45):
        pline(d, b, (b[0] - 22 * math.cos(ang + s), b[1] - 22 * math.sin(ang + s)), passes=1)


def check(d, x, y, s=1):
    pen(d, [(x, y), (x + 12 * s, y + 16 * s), (x + 36 * s, y - 18 * s)], w=4)


def txt(d, x, y, s, size, col=INK, hl=None, strike=None, bold=False):
    f = (BIROB if bold else BIRO)(size)
    bb = d.textbbox((x, y), s, font=f)
    if hl:   # ragged highlighter stroke
        h0, h1 = bb[1] + (bb[3] - bb[1]) * 0.42, bb[3] + 4
        top = [(xx, h0 + random.uniform(-3, 3)) for xx in range(bb[0] - 10, bb[2] + 12, 14)]
        bot = [(xx, h1 + random.uniform(-3, 3)) for xx in range(bb[2] + 12, bb[0] - 10, -14)]
        d.polygon(top + bot, fill=hl)
    d.text((x, y), s, font=f, fill=col)
    if strike is not None:
        if strike == 'all':
            sx0, sx1 = bb[0], bb[2]
        else:   # strike only the substring
            pre = s[:s.index(strike)]
            sx0 = x + d.textlength(pre, font=f); sx1 = sx0 + d.textlength(strike, font=f)
        ym = (bb[1] + bb[3]) / 2 + 6
        pen(d, [(sx0 - 6, ym + 3), (sx1 + 6, ym - 5)], w=4)
        pen(d, [(sx0 - 4, ym - 4), (sx1 + 4, ym - 9)], w=3, passes=1)
    return bb


def scientist(d, x, y, hair_up=True):
    """lab-coat woman, ballpoint sketch, ~240 px tall"""
    pcirc(d, x, y + 30, 26)
    if hair_up:
        pcirc(d, x + 4, y - 2, 13)                                     # bun
    else:
        pen(d, [(x - 26, y + 26), (x - 32, y + 70)], passes=1); pen(d, [(x + 26, y + 26), (x + 32, y + 70)], passes=1)   # long hair
    pen(d, [(x - 8, y + 56), (x - 8, y + 70)], passes=1); pen(d, [(x + 8, y + 56), (x + 8, y + 70)], passes=1)  # neck
    pen(d, [(x - 40, y + 76), (x + 40, y + 76), (x + 52, y + 200), (x - 52, y + 200), (x - 40, y + 76)])        # coat
    pen(d, [(x, y + 76), (x - 6, y + 200)], passes=1)                                                            # coat opening
    pen(d, [(x - 22, y + 76), (x, y + 104), (x + 22, y + 76)], passes=1)                                         # lapels
    prect(d, x + 14, y + 120, x + 34, y + 134, passes=1)                                                         # pocket
    pen(d, [(x - 40, y + 82), (x - 62, y + 160), (x - 50, y + 166)])                                             # arms
    pen(d, [(x + 40, y + 82), (x + 64, y + 150), (x + 52, y + 156)])
    pen(d, [(x - 22, y + 200), (x - 24, y + 250)]); pen(d, [(x + 22, y + 200), (x + 24, y + 250)])               # legs


def cell(d, x, y, r):
    pcirc(d, x, y, r); pcirc(d, x + r * 0.15, y - r * 0.1, r * 0.32)
    for k in range(7):
        a = random.uniform(0, 6.28); rr = random.uniform(r * 0.45, r * 0.8)
        pcirc(d, x + rr * math.cos(a), y + rr * math.sin(a), 4, passes=1)


def petri(d, x, y, r, inner):
    pcirc(d, x, y, r); pcirc(d, x, y, r - 8, passes=1)
    inner(d, x, y, r - 14)


def pineapple(d, x, y, r):
    pcirc(d, x, y, r * 0.55)
    for k in range(-2, 3): pline(d, (x - r * 0.5, y + k * 12 - 10), (x + r * 0.5, y + k * 12 + 10), passes=1)
    pen(d, [(x - 10, y - r * 0.55), (x - 22, y - r * 0.95)], passes=1); pen(d, [(x + 6, y - r * 0.55), (x + 14, y - r * 0.98)], passes=1)
def garlic(d, x, y, r):
    for dx in (-18, 0, 18): pen(d, [(x + dx, y - r * 0.55), (x + dx - 14, y), (x + dx, y + r * 0.5), (x + dx + 14, y), (x + dx, y - r * 0.55)], passes=1)
def wheat(d, x, y, r):
    pline(d, (x, y + r * 0.8), (x, y - r * 0.6))
    for k in range(5):
        yy = y - r * 0.5 + k * 14
        pen(d, [(x, yy), (x - 14, yy - 10)], passes=1); pen(d, [(x, yy), (x + 14, yy - 10)], passes=1)
def radish(d, x, y, r):
    pcirc(d, x, y + 6, r * 0.4); pen(d, [(x, y + 6 + r * 0.4), (x + 4, y + r * 0.9)], passes=1)
    pen(d, [(x - 6, y - r * 0.3), (x - 20, y - r * 0.85)], passes=1); pen(d, [(x + 6, y - r * 0.3), (x + 20, y - r * 0.85)], passes=1)


def drone(d, x, y, s=1.0):
    pline(d, (x - 60 * s, y), (x + 60 * s, y))
    for dx in (-60 * s, 60 * s):
        pline(d, (x + dx, y), (x + dx, y - 16 * s), passes=1); pline(d, (x + dx - 20 * s, y - 16 * s), (x + dx + 20 * s, y - 16 * s), passes=1)
    prect(d, x - 28 * s, y + 24 * s, x + 28 * s, y + 64 * s, passes=1); pen(d, [(x - 28 * s, y + 24 * s), (x, y + 46 * s), (x + 28 * s, y + 24 * s)], passes=1)


def snow(d, x, y, r):
    for a in range(0, 180, 60):
        q = math.radians(a); pline(d, (x - r * math.cos(q), y - r * math.sin(q)), (x + r * math.cos(q), y + r * math.sin(q)), passes=1)


def capsule(d, x, y, col, h, wd):
    d.rounded_rectangle((x + 3, y + 3, x + wd - 3, y + h // 2), wd // 2, fill=col)
    d.rounded_rectangle((x, y, x + wd, y + h), wd // 2, outline=INK, width=3)
    pline(d, (x + 2, y + h // 2), (x + wd - 2, y + h // 2), passes=1)


def star(d, x, y, r):
    pts = [(x + r * math.cos(math.radians(-90 + k * 36)) * (1 if k % 2 == 0 else 0.45), y + r * math.sin(math.radians(-90 + k * 36)) * (1 if k % 2 == 0 else 0.45)) for k in range(11)]
    pen(d, pts)


def base():
    im = Image.new('RGB', (SW, SH), (238, 239, 240))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((30, 40, SW - 30, SH - 20), 18, fill=(250, 250, 250), outline=(225, 225, 228), width=3)
    for j, (x0, x1) in enumerate((PL, PR)):
        d.rectangle((x0, 60, x1, SH - 40), fill=(253, 252, 248))
        for x in range(x0 + 20, x1 - 10, 28): d.line((x, PT - 20, x, PB), fill=GRID)
        for y in range(PT - 20, PB, 28): d.line((x0 + 20, y, x1 - 20, y), fill=GRID)
        d.text((x0 + 24, 80), 'LAB NOTEBOOK', font=GROT(28), fill=GREY)
        d.text((x1 - 300, 80), 'PROJECT: SICKSCIENCE', font=GROT(24), fill=GREY)
    d.line((1020, 50, 1020, SH - 30), fill=(215, 215, 218), width=6)
    return im


# ---------------- left page: the researchers (00-64 s) ----------------
def L01(d): txt(d, 110, 148, '01 / ORIGIN', 40); txt(d, 760, 148, 'the story', 34, col=GREY)
def L02(d): scientist(d, 175, 225, True); scientist(d, 345, 225, False)
def L03(d):
    txt(d, 118, 485, 'Polen', 40); txt(d, 296, 485, 'Merve', 40)
    pen(d, [(215, 330), (240, 318), (265, 330), (290, 318), (305, 330)], passes=1)   # chemical-bond zigzag between them
    txt(d, 520, 200, '2009', 96, hl=YEL, bold=True)
def L04(d):
    arrow(d, (520, 425), (930, 425)); txt(d, 520, 435, '2009', 30); txt(d, 870, 435, '2023', 30)
    txt(d, 520, 325, '14 YEARS', 72, hl=YEL, bold=True)
def L05(d):
    for k, x in enumerate((112, 196)):
        prect(d, x, 560, x + 70, 610); pcirc(d, x + 50, 600, 10, passes=1)        # diplomas
    txt(d, 290, 556, 'Yeditepe · PhD ×2', 44)
    txt(d, 560, 492, 'Polen: Harvard–MIT HST', 44)
def L06(d):
    cell(d, 175, 715, 58)
    pcirc(d, 400, 715, 40); arrow(d, (448, 690), (470, 730)); arrow(d, (360, 745), (338, 700))
    for k in range(6): pcirc(d, 610 + (k % 3) * 30, 690 + (k // 3) * 32, 9, passes=1)
    arrow(d, (720, 715), (800, 715), dotted=True); cell(d, 860, 715, 44)
    txt(d, 110, 790, 'stem cells', 34); txt(d, 320, 790, 'regenerative med.', 34); txt(d, 600, 790, 'exosomes · cancer', 34)
def L07(d):
    prect(d, 112, 860, 182, 950); txt(d, 120, 866, 'PAT.', 26); pcirc(d, 165, 935, 18, passes=1)
    for k in range(3): d.rectangle((210 + k * 14, 864 + k * 10, 278 + k * 14, 948 + k * 10), fill=(253, 252, 248)); prect(d, 210 + k * 14, 864 + k * 10, 278 + k * 14, 948 + k * 10, passes=1)
    txt(d, 350, 870, '20–30 PAPERS', 74, hl=YEL, bold=True)
def L08(d): txt(d, 110, 1000, 'for mom', 40); txt(d, 300, 1004, 'preclinical', 36); pline(d, (300, 1052), (520, 1052), passes=1)
def L09(d):
    prect(d, 640, 990, 712, 1080)
    for k in range(4): pline(d, (652, 1010 + k * 16), (700, 1010 + k * 16), passes=1)
    txt(d, 730, 1000, 'published', 40); check(d, 900, 1030)
def L10(d): txt(d, 110, 1100, 'in the lab', 60, strike='lab')
def L11(d): txt(d, 410, 1080, 'at home', 70, hl=YEL, bold=True)
def L12(d): cell(d, 210, 1300, 92); txt(d, 340, 1190, 'exosomes', 44)
def L13(d):
    d.ellipse((376, 1296, 384, 1304), fill=INK); arrow(d, (470, 1262), (392, 1294))
    txt(d, 520, 1235, '1/1000', 84, hl=YEL, bold=True)
def L14(d): drone(d, 560, 1355, 0.7); arrow(d, (640, 1380), (760, 1380), dotted=True); cell(d, 830, 1375, 40); txt(d, 470, 1400, 'coded messages', 28)


# ---------------- right page: platform + brand (64-114 s) ----------------
FIGS = [('PINEAPPLE', pineapple), ('GARLIC', garlic), ('WHEAT', wheat), ('RADISH', radish)]
def R01(d):
    txt(d, 1080, 148, '02 / APPLICATION', 40)
    for i, (nm, fn) in enumerate(FIGS):
        x = 1160 + i * 220
        petri(d, x, 290, 66, fn); txt(d, x - 60, 362, f'FIG. 0{i + 1}', 28); txt(d, x - 60, 394, nm, 30)
def R02(d):
    for i in range(4): pline(d, (1160 + i * 220, 432), (1290, 470), passes=1)
    txt(d, 1080, 458, 'THOUSANDS', 78, hl=YEL, bold=True); txt(d, 1430, 600, '100% plant-based · vegan', 38)
def R03(d): txt(d, 1080, 548, 'NX35', 112, hl=YEL, bold=True)
def R04(d):
    for i, s in enumerate(['SEPARATION', 'STABILIZATION', 'LIBRARY']):
        x = 1080 + i * 292
        prect(d, x, 690, x + 252, 756); txt(d, x + 16, 700, s, 36)
        if i < 2: arrow(d, (x + 256, 723), (x + 288, 723))
    txt(d, 1080, 766, 'biomimetic', 34)
def R05(d):
    snow(d, 1330, 790, 26); pline(d, (1296, 822), (1364, 758), w=4)
    txt(d, 1390, 768, 'ROOM TEMPERATURE', 40)
def R06(d):
    x, y = 1100, 850
    pen(d, [(x, y), (x + 60, y), (x + 70, y + 70), (x - 10, y + 70), (x, y)]); pline(d, (x + 4, y + 30), (x + 64, y + 30), passes=1)
    arrow(d, (1200, 885), (1290, 885)); d.rounded_rectangle((1310, 845, 1350, 925), 14, outline=INK, width=3)
    txt(d, 1390, 852, 'LAB', 58, hl=YEL, bold=True); arrow(d, (1510, 885), (1590, 885)); txt(d, 1610, 852, 'HOME', 58, hl=YEL, bold=True)
def R07(d): txt(d, 1080, 950, 'scientist?', 58, strike='all'); arrow(d, (1350, 985), (1440, 985)); txt(d, 1460, 950, 'marketer.', 58)
def R08(d):
    for k, h in enumerate([20, 38, 30, 56]): prect(d, 1090 + k * 26, 1110 - h, 1110 + k * 26, 1110, passes=1)
    txt(d, 1220, 1030, '"THAT\'S SICK!"', 80, bold=True)
def R09(d): txt(d, 1080, 1130, "No, that's science.", 52); txt(d, 1520, 1118, 'SickScience', 82, col=VIO, bold=True)
def R10(d):
    for i, (col, nm, part) in enumerate([(VIO, 'ShapeShift', 'neck + jaw'), (RED, 'NetWork', 'face'), (GRN, 'PowerCycle', 'hair'), (COB, 'DropOff', 'body')]):
        x = 1110 + i * 150; big = nm == 'PowerCycle'
        capsule(d, x, 1222, col, 128 if big else 110, 44 if big else 36)
        txt(d, x - 28, 1356, nm, 28); txt(d, x - 28, 1386, part, 24)
def R11(d): star(d, 1745, 1250, 36); txt(d, 1700, 1290, '14 AWARDS', 52, hl=YEL, bold=True); txt(d, 1700, 1352, 'Oprah · InStyle · Esquire', 26)


BEATS = [  # (time, page side, fns, narration)
    ('0:00', 'W', [], "We're telling this story for the first time."),
    ('0:03', 'L', [L01, L02], 'SickScience began with two geneticists.'),
    ('0:06', 'L', [L03], 'Polen Koçak-Denizci and Merve Yıldırım-Canpolat. They met in a chemistry and biology class in 2009.'),
    ('0:12', 'L', [L04], 'Then came fourteen years of working together.'),
    ('0:15', 'L', [L05], 'Both earned biotechnology PhDs at Yeditepe. Polen was also a research scholar at Harvard–MIT Health Sciences and Technology.'),
    ('0:22', 'L', [L06], 'They studied stem cell production, regenerative medicine, and exosome applications in cancer research.'),
    ('0:28', 'L', [L07], 'International patents. Twenty to thirty peer-reviewed papers.'),
    ('0:32', 'L', [], 'But there was a problem.'),
    ('0:34', 'L', [L08], "Merve's mother had mesothelioma. No treatment was available. And their research was still preclinical."),
    ('0:41', 'L', [L09], 'After her mother passed, they finished and published the research.'),
    ('0:46', 'L', [L10], "Then they made a decision. Science couldn't stay in the lab."),
    ('0:50', 'L', [L11], "It needed to reach people's homes."),
    ('0:53', 'L', [L12], 'At the center? Exosomes.'),
    ('0:56', 'L', [L13], "Tiny carriers, about one-thousandth of a cell's size, delivering coded messages between cells."),
    ('1:02', 'L', [L14], 'Think delivery drones.'),
    ('1:04', 'R', [R01], 'Their source? Plants. Pineapple, garlic, wheat, and radish.'),
    ('1:09', 'R', [R02], 'Thousands of plant messages. One hundred percent plant-based and vegan.'),
    ('1:13', 'R', [R03], 'Then came NX35.'),
    ('1:15', 'R', [R04], 'A biomimetic platform: exosome separation, room-temperature stabilization, and their plant library.'),
    ('1:21', 'R', [R05], 'No cold chain.'),
    ('1:23', 'R', [R06], 'Why beauty? Clinical-level science, in formulas people could use at home.'),
    ('1:28', 'R', [R07], "Everyone in beauty says they're a scientist. Most are marketers."),
    ('1:32', 'R', [R08], "Then a beauty executive saw their data. 'That's sick!'"),
    ('1:36', 'R', [R09], "Their answer? 'No, that's science.' And SickScience was born."),
    ('1:40', 'R', [R10], 'ShapeShift for neck and jawline. NetWork for face. PowerCycle for hair. DropOff for body.'),
    ('1:48', 'R', [R11], 'Four products. Fourteen awards. Oprah, InStyle, and Esquire.'),
    ('1:52', 'W', [], 'Science, but never boring.'),
]


def page_view(sp, side):
    pc = (PL[0] + PL[1]) / 2 - 8 if side == 'L' else (PR[0] + PR[1]) / 2 - 8
    return sp.crop((int(pc - 416), 0, int(pc + 416), SH)).resize((540, 960))


def wide(sp, head, sub, note, col=INK):
    P = Image.new('RGB', (540, 960), (245, 245, 246)); d = ImageDraw.Draw(P)
    P.paste(sp.resize((540, int(540 * SH / SW))), (0, 300))
    f = GROT(38); tw = d.textlength(head, font=f); d.text(((540 - tw) / 2, 150), head, font=f, fill=INK)
    f2 = BIRO(40); tw = d.textlength(sub, font=f2); d.text(((540 - tw) / 2, 205), sub, font=f2, fill=col)
    for i, ln in enumerate(note): d.text((40, 740 + i * 32), ln, font=GROT(24), fill=GREY)
    return P


def main():
    final = base(); fd = ImageDraw.Draw(final)
    random.seed(11)
    for _, _, fns, _ in BEATS:
        for fn in fns: fn(fd)
    final.save(os.path.join(R, 'spread_v4d.png'))
    random.seed(11)
    sp = base(); d = ImageDraw.Draw(sp); panels = []
    for t, side, fns, nar in BEATS:
        for fn in fns: fn(d)
        if side == 'W':
            P = wide(final, 'FOR THE FIRST TIME', 'the SickScience story', ['finished spread first,', 'then cut to the empty page']) if t == '0:00' else \
                wide(final, 'SICK SCIENCE', 'Science, but never boring.', ['pull back to the wide spread,', 'the real 4 products on the bench'], VIO)
        else:
            P = page_view(sp, side)
        panels.append((t, nar, P))
    cols = 9; cw, ch, cap = 220, 391, 180
    rows = math.ceil(len(panels) / cols)
    sheet = Image.new('RGB', (cols * (cw + 10) + 10, rows * (ch + cap + 10) + 10), 'white'); sd = ImageDraw.Draw(sheet)
    for i, (t, nar, p) in enumerate(panels):
        x = 10 + (i % cols) * (cw + 10); y = 10 + (i // cols) * (ch + cap + 10)
        sheet.paste(p.resize((cw, ch)), (x, y)); sd.rectangle((x, y, x + cw - 1, y + ch - 1), outline=(200, 200, 205))
        sd.text((x, y + ch + 6), t, font=GROT(22), fill=VIO)
        f = GROT(16); words, line, ly = nar.split(), '', y + ch + 34
        for wd in words:
            tt = (line + ' ' + wd).strip()
            if sd.textlength(tt, font=f) > cw - 6: sd.text((x, ly), line, font=f, fill=INK); ly += 20; line = wd
            else: line = tt
        sd.text((x, ly), line, font=f, fill=INK)
    sheet.save(os.path.join(R, 'storyboard_v4d.jpg'), quality=90)
    print('ok', len(panels))


if __name__ == '__main__':
    main()
