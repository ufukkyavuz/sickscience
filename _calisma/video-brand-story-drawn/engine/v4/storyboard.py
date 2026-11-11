# v4 rough outline: third-person narrator, INO-style two-page lab notebook spread. Flat sketch only (no effects).
import math, os
from PIL import Image, ImageDraw, ImageFont

R = os.path.dirname(os.path.abspath(__file__))
F = os.path.expanduser('~/Library/Fonts/')
hand = lambda s: ImageFont.truetype(F + 'Caveat-Bold.ttf', s)
grot = lambda s: ImageFont.truetype(F + 'FoundersGrotesk-Medium.otf', s)
INK, GRID, YEL, VIO, BLUE = (25, 28, 40), (205, 214, 226), (255, 226, 70), (169, 33, 192), (60, 90, 200)
SW, SH = 2040, 1480                      # spread px
PL, PR = (60, 1000), (1040, 1980)        # page x ranges
PT, PB = 150, 1420


def base():
    im = Image.new('RGB', (SW, SH), (238, 239, 240))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((30, 40, SW - 30, SH - 20), 18, fill=(250, 250, 250), outline=(225, 225, 228), width=3)   # white cover
    for x0, x1 in (PL, PR):
        d.rectangle((x0, 60, x1, SH - 40), fill=(253, 252, 248))
        for x in range(x0 + 20, x1 - 10, 28):
            d.line((x, PT - 20, x, PB), fill=GRID)
        for y in range(PT - 20, PB, 28):
            d.line((x0 + 20, y, x1 - 20, y), fill=GRID)
        d.text((x0 + 24, 78), 'LAB NOTEBOOK', font=grot(30), fill=(120, 125, 140))
        d.text((x1 - 330, 78), 'PROJECT: SICKSCIENCE', font=grot(26), fill=(120, 125, 140))
    d.text((PL[0] + 24, 112), 'page 01', font=hand(30), fill=(120, 125, 140))
    d.text((PR[0] + 24, 112), 'page 02', font=hand(30), fill=(120, 125, 140))
    d.line((1020, 50, 1020, SH - 30), fill=(215, 215, 218), width=6)
    return im


def txt(d, x, y, s, size, col=INK, hl=None, strike=False):
    f = hand(size)
    bb = d.textbbox((x, y), s, font=f)
    if hl:
        d.rectangle((bb[0] - 8, bb[1] + (bb[3] - bb[1]) * 0.45, bb[2] + 8, bb[3] + 6), fill=hl)
    d.text((x, y), s, font=f, fill=col)
    if strike:
        ym = (bb[1] + bb[3]) / 2 + 4
        d.line((bb[0] - 4, ym, bb[2] + 4, ym - 6), fill=INK, width=5)
    return bb


def figure(d, x, y, coat=True):          # stick scientist
    d.ellipse((x - 22, y, x + 22, y + 44), outline=INK, width=4)
    d.line((x, y + 44, x, y + 130), fill=INK, width=4)
    if coat:
        d.polygon([(x - 34, y + 60), (x + 34, y + 60), (x + 44, y + 150), (x - 44, y + 150)], outline=INK, width=4)
    d.line((x - 34, y + 70, x - 60, y + 130), fill=INK, width=4); d.line((x + 34, y + 70, x + 60, y + 130), fill=INK, width=4)
    d.line((x - 16, y + 150, x - 26, y + 220), fill=INK, width=4); d.line((x + 16, y + 150, x + 26, y + 220), fill=INK, width=4)


def arrow(d, a, b, dotted=False):
    if dotted:
        n = int(math.dist(a, b) // 18)
        for i in range(0, n, 2):
            p = (a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n)
            q = (a[0] + (b[0] - a[0]) * (i + 1) / n, a[1] + (b[1] - a[1]) * (i + 1) / n)
            d.line((p, q), fill=INK, width=4)
    else:
        d.line((a, b), fill=INK, width=4)
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    for s in (2.6, -2.6):
        d.line((b, (b[0] - 22 * math.cos(ang + s / 6), b[1] - 22 * math.sin(ang + s / 6))), fill=INK, width=4)


# ---- beats: (time, narration, draw fn, focus box on spread) ----
def b1(d):
    figure(d, 170, 190); figure(d, 300, 190)
    txt(d, 400, 210, '2 geneticists', 64)
    txt(d, 420, 300, '2009', 70, hl=YEL)
def b2(d):
    d.line((110, 560, 950, 560), fill=INK, width=5)
    for i, yr in enumerate(['2009', '2012', '2015', '2018', '2021', '2023']):
        x = 120 + i * 162; d.line((x, 545, x, 575), fill=INK, width=4); txt(d, x - 26, 585, yr, 30)
    txt(d, 380, 640, '14 YEARS', 84, hl=YEL)
def b3(d):
    x, y = 150, 790                         # microscope
    d.rectangle((x - 50, y + 170, x + 60, y + 190), outline=INK, width=4)
    d.line((x + 30, y + 170, x + 30, y + 40), fill=INK, width=5); d.line((x + 30, y + 40, x - 20, y + 10), fill=INK, width=5)
    d.rectangle((x - 40, y - 20, x - 5, y + 40), outline=INK, width=4); d.line((x - 30, y + 110, x + 30, y + 110), fill=INK, width=4)
    txt(d, 260, 780, 'cancer research', 50); txt(d, 260, 840, 'regenerative medicine', 50)
    txt(d, 260, 910, 'patents +', 50); txt(d, 470, 900, '20–30 papers', 62, hl=YEL)
def b4(d):
    x, y = 150, 1080                       # small heart
    d.polygon([(x, y + 50), (x - 40, y + 10), (x - 25, y - 15), (x, y + 2), (x + 25, y - 15), (x + 40, y + 10)], outline=INK, width=4)
    txt(d, 220, 1040, "Merve's mom", 50); txt(d, 220, 1100, 'no cure', 46); txt(d, 470, 1100, 'still preclinical', 46)
def b5(d):
    txt(d, 130, 1250, 'the lab', 64, strike=True)
    arrow(d, (340, 1290), (470, 1290))
    x, y = 540, 1240                       # house
    d.polygon([(x, y + 30), (x + 60, y - 20), (x + 120, y + 30)], outline=INK, width=4); d.rectangle((x + 12, y + 30, x + 108, y + 110), outline=INK, width=4)
    txt(d, 690, 1250, 'homes', 70, hl=YEL)
def b6(d):
    txt(d, 1080, 180, 'exosomes =', 56); txt(d, 1080, 240, 'tiny messengers', 66, hl=YEL)
    d.ellipse((1090, 360, 1230, 500), outline=INK, width=4); d.ellipse((1140, 410, 1180, 450), outline=INK, width=4)
    d.ellipse((1790, 360, 1930, 500), outline=INK, width=4); d.ellipse((1840, 410, 1880, 450), outline=INK, width=4)
    x, y = 1510, 380                       # drone + envelope
    d.line((x - 70, y, x + 70, y), fill=INK, width=4)
    for dx in (-70, 70): d.line((x + dx, y, x + dx, y - 20), fill=INK, width=4); d.line((x + dx - 22, y - 20, x + dx + 22, y - 20), fill=INK, width=4)
    d.rectangle((x - 35, y + 30, x + 35, y + 80), outline=INK, width=4); d.line((x - 35, y + 30, x, y + 58, x + 35, y + 30), fill=INK, width=4)
    arrow(d, (1240, 430), (1420, 420), dotted=True); arrow(d, (1600, 420), (1780, 430), dotted=True)
def b7(d):
    for i, s in enumerate(['pineapple', 'garlic', 'wheat', 'radish']):
        x = 1100 + i * 220
        d.ellipse((x, 560, x + 170, 730), outline=INK, width=4); d.ellipse((x + 12, 572, x + 158, 718), outline=(160, 170, 185), width=2)
        txt(d, x + 10, 740, f'FIG. 0{i + 1}', 30); txt(d, x + 10, 775, s, 34)
    txt(d, 1090, 830, 'THOUSANDS', 76, hl=YEL); txt(d, 1520, 850, 'plant library', 50)
def b8(d):
    x, y = 1120, 955                       # thermometer
    d.rounded_rectangle((x, y, x + 34, y + 130), 17, outline=INK, width=4); d.ellipse((x - 14, y + 115, x + 48, y + 175), outline=INK, width=4)
    txt(d, 1180, 950, 'room temp', 50)
    sx, sy = 1470, 1000                    # snowflake, struck
    for a in range(0, 180, 60):
        r = math.radians(a); d.line((sx - 40 * math.cos(r), sy - 40 * math.sin(r), sx + 40 * math.cos(r), sy + 40 * math.sin(r)), fill=INK, width=4)
    d.line((sx - 55, sy + 45, sx + 55, sy - 45), fill=INK, width=6)
    txt(d, 1530, 980, 'no cold chain', 46)
    txt(d, 1560, 1030, 'NX35', 100, hl=YEL)
def b9(d):
    txt(d, 1090, 1150, 'scientist?', 60, strike=True); arrow(d, (1360, 1190), (1460, 1190)); txt(d, 1480, 1150, 'marketer.', 60)
def b10(d):
    d.rounded_rectangle((1080, 1240, 1430, 1310), 30, outline=INK, width=4); txt(d, 1110, 1242, '"That\'s sick!"', 52)
    d.rounded_rectangle((1470, 1240, 1950, 1310), 30, outline=INK, width=4); txt(d, 1490, 1244, '"No, that\'s science."', 48)
    txt(d, 1330, 1320, 'Sick', 84); txt(d, 1480, 1320, 'Science', 84, col=VIO)

BEATS = [
    ('COVER', 'For the first time: how SickScience began.', None, 'spread'),
    ('01', 'SickScience started with two geneticists, who met in a chemistry class in 2009.', b1, (60, 150, 1000, 700)),
    ('02', 'For the next fourteen years, they lived in the lab.', b2, (60, 400, 1000, 900)),
    ('03', 'Cancer research. Regenerative medicine. Patents, and twenty to thirty peer-reviewed papers.', b3, (60, 700, 1000, 1200)),
    ('04', "Then it got personal. Merve's mother had a cancer with no cure, and their research was still preclinical.", b4, (60, 950, 1000, 1420)),
    ('05', "So they decided to take their science out of the lab, and into people's homes.", b5, (60, 950, 1000, 1420)),
    ('06', 'Their tool: exosomes. Tiny messengers that cells send each other, like delivery drones.', b6, (1040, 150, 1980, 700)),
    ('07', 'They take them from plants: pineapple, garlic, wheat, radish. A library of thousands.', b7, (1040, 450, 1980, 950)),
    ('08', 'Then they made them stable at room temperature, with no cold chain. They called it NX35.', b8, (1040, 850, 1980, 1200)),
    ('09', "Everyone in beauty says they're a scientist. Most are marketers.", b9, (1040, 1000, 1980, 1420)),
    ('10', "When a beauty executive saw their data, she said: \"That's sick!\" They said: \"No, that's science.\"", b10, (1040, 1000, 1980, 1420)),
    ('END', 'SickScience. Science, but never boring.', None, 'spread'),
]


NEWBOX = {'01': (95, 170, 700, 420), '02': (90, 530, 970, 750), '03': (90, 760, 800, 1000),
          '04': (95, 1030, 730, 1170), '05': (110, 1215, 870, 1360), '06': (1070, 170, 1950, 510),
          '07': (1085, 545, 1960, 935), '08': (1090, 940, 1800, 1150), '09': (1080, 1150, 1700, 1225),
          '10': (1070, 1230, 1960, 1415)}


def sick_science(d):
    txt(d, 1500, 1395 - 0, '', 10)


def panel(spread, focus, title, narration, done):
    P = Image.new('RGB', (540, 960), (245, 245, 246))
    d = ImageDraw.Draw(P)
    if focus == 'spread':
        s = spread.resize((540, int(540 * SH / SW)))
        y = 300
        P.paste(s, (0, y))
        head = 'FOR THE FIRST TIME' if title == 'COVER' else 'SICK SCIENCE'
        sub = 'How SickScience began' if title == 'COVER' else 'Science, but never boring.'
        f = grot(40); tw = d.textlength(head, font=f); d.text(((540 - tw) / 2, 150), head, font=f, fill=INK)
        f2 = hand(44); tw = d.textlength(sub, font=f2); d.text(((540 - tw) / 2, 205), sub, font=f2, fill=VIO if title == 'END' else INK)
        if title == 'END':
            d.rectangle((60, 730, 480, 900), outline=(150, 150, 160), width=3)
            d.text((80, 780), 'real 4-product photo', font=grot(30), fill=(120, 120, 130))
            d.text((80, 820), '(client shot S_0723)', font=grot(26), fill=(120, 120, 130))
        if title == 'COVER':
            d.text((60, 760), 'finished spread first (ending shown first),', font=grot(24), fill=(120, 120, 130))
            d.text((60, 790), 'then cut to the empty page 01', font=grot(24), fill=(120, 120, 130))
    else:
        x0, y0, x1, y1 = focus
        sp2 = spread.copy(); dd = ImageDraw.Draw(sp2)
        nb = NEWBOX.get(title)
        if nb:
            dd.rounded_rectangle(nb, 16, outline=VIO, width=6)
        w = 832; h = SH
        pc = (PL[0] + PL[1]) / 2 - 8 if x0 < 1020 else (PR[0] + PR[1]) / 2 - 8
        P = sp2.crop((int(pc - w / 2), 0, int(pc + w / 2), h)).resize((540, 960))
    return P


def main():
    sp = base()
    d = ImageDraw.Draw(sp)
    panels = []
    for i, (k, nar, fn, focus) in enumerate(BEATS):
        if fn:
            fn(d)
        if k == 'END':
            txt(d, 1600, 1395, '', 10)
        panels.append((k, nar, panel(sp.copy(), focus, k, nar, i)))
    # final spread title line on page 02 bottom
    txt(d, 1500, 1390, '', 10)
    sp.save(os.path.join(R, 'spread_final.png'))
    panels[0] = (panels[0][0], panels[0][1], panel(sp.copy(), 'spread', 'COVER', '', 0))
    # sheet: 6 x 2 panels with captions
    cw, ch, cap = 300, 533, 150
    sheet = Image.new('RGB', (cw * 6 + 70, (ch + cap) * 2 + 40), 'white')
    sd = ImageDraw.Draw(sheet)
    for i, (k, nar, p) in enumerate(panels):
        x = 10 + (i % 6) * (cw + 10); y = 10 + (i // 6) * (ch + cap + 10)
        sheet.paste(p.resize((cw, ch)), (x, y))
        sd.rectangle((x, y, x + cw - 1, y + ch - 1), outline=(200, 200, 205))
        sd.text((x, y + ch + 6), k, font=grot(26), fill=VIO)
        # wrap narration
        words, line, ly = nar.split(), '', y + ch + 38
        f = grot(20)
        for wd in words:
            t = (line + ' ' + wd).strip()
            if sd.textlength(t, font=f) > cw - 6:
                sd.text((x, ly), line, font=f, fill=INK); ly += 24; line = wd
            else:
                line = t
        sd.text((x, ly), line, font=f, fill=INK)
    sheet.save(os.path.join(R, 'storyboard_v4.jpg'), quality=90)
    print('ok')


if __name__ == "__main__":
    main()
