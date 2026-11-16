"""SickScience text-animation library (PIL, deterministic, frame-by-frame).

Usage:
    from textfx import render, EFFECTS
    layer = render('mask-reveal-up', 'Sculpted\nin 4 weeks', t, W=1080, H=1920, cy=700,
                   size=150, weight='Bold', color=(255,255,255), accent=(169,33,192),
                   accent_words={'4','weeks'}, shadow=True, dur=2.0, exit='blur-out-up')
    frame.alpha_composite(layer)

t = seconds since the element appeared. dur = total on-screen time (exit plays in the last `exit_t` s).
Fonts: Founders Grotesk family only (weights Light/Regular/Medium/Semibold/Bold, italics, Text cut).
Colours are free per call: white, ink, magenta, product colours, gradients/texture fills.
"""
import math, random, os
from functools import lru_cache
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

FD = os.path.expanduser('~/Library/Fonts')
BRAND = dict(white=(255, 255, 255), ink=(18, 18, 20), ivory=(246, 243, 236), magenta=(169, 33, 192),
             ss=(115, 0, 199), nw=(200, 30, 40), pc=(30, 130, 60), do=(25, 60, 190), silver=(200, 204, 210))

def font_path(weight='Bold', italic=False, cut=''):
    name = f"FoundersGrotesk{cut}-{weight}{'Italic' if italic else ''}.otf"
    return os.path.join(FD, name)

@lru_cache(maxsize=64)
def F(weight, size, italic=False, cut=''):
    return ImageFont.truetype(font_path(weight, italic, cut), int(size))

# ---------------- easing ----------------
def cl(p): return 0.0 if p < 0 else 1.0 if p > 1 else p
def out_cubic(p): p = cl(p); return 1 - (1 - p) ** 3
def out_quart(p): p = cl(p); return 1 - (1 - p) ** 4
def out_expo(p): p = cl(p); return 1.0 if p >= 1 else 1 - 2 ** (-10 * p)
def in_cubic(p): p = cl(p); return p ** 3
def inout_sine(p): p = cl(p); return -(math.cos(math.pi * p) - 1) / 2
def inout_cubic(p): p = cl(p); return 4 * p ** 3 if p < .5 else 1 - (-2 * p + 2) ** 3 / 2
def out_back(p, s=1.9): p = cl(p); return 1 + (s + 1) * (p - 1) ** 3 + s * (p - 1) ** 2
def spring(p, k=7.0, w=11.0): p = cl(p); return 1 - math.exp(-k * p) * math.cos(w * p)
def bounce(p):
    p = cl(p); n, d = 7.5625, 2.75
    if p < 1 / d: return n * p * p
    if p < 2 / d: p -= 1.5 / d; return n * p * p + .75
    if p < 2.5 / d: p -= 2.25 / d; return n * p * p + .9375
    p -= 2.625 / d; return n * p * p + .984375
def lux(p):  # cubic-bezier(.4,0,.2,1) approximation: premium, unhurried
    return inout_cubic(cl(p)) * .35 + out_quart(cl(p)) * .65

# ---------------- layout ----------------
class U:  # one unit (char / word / line)
    __slots__ = ('s', 'x', 'y', 'w', 'li', 'wi', 'ci', 'n', 'accent')

def layout(text, font, cx, cy, lh=1.0, tracking=0.0, align='center', maxw=None):
    lines = text.split('\n')
    asc, desc = font.getmetrics(); L = int((asc + desc) * lh * .86)
    total = L * len(lines); y0 = cy - total / 2 + asc * .86
    chars, words, lns = [], [], []
    wi = ci = 0
    for li, line in enumerate(lines):
        trk = tracking * font.size
        widths = [font.getlength(c) for c in line]
        lw = sum(widths) + trk * max(0, len(line) - 1)
        x = cx - lw / 2 if align == 'center' else (cx if align == 'left' else cx - lw)
        y = y0 + li * L
        ln = U(); ln.s, ln.x, ln.y, ln.w, ln.li, ln.wi, ln.ci = line, x, y, lw, li, wi, ci; lns.append(ln)
        cur = None
        for c, cw in zip(line, widths):
            u = U(); u.s, u.x, u.y, u.w, u.li, u.wi, u.ci = c, x, y, cw, li, wi, ci; chars.append(u)
            if c == ' ':
                if cur: words.append(cur); cur = None; wi += 1
            else:
                if cur is None:
                    cur = U(); cur.s, cur.x, cur.y, cur.w, cur.li, cur.wi, cur.ci = '', x, y, 0, li, wi, ci
                cur.s += c; cur.w = x + cw - cur.x
            x += cw + trk; ci += 1
        if cur: words.append(cur); wi += 1
    for g in (chars, words, lns):
        for u in g: u.n = len(g)
    for u in chars: u.wi = min(u.wi, len(words) - 1)
    return chars, words, lns, L

@lru_cache(maxsize=4096)
def glyph(s, weight, size, col, italic=False, cut='', stroke=0, outline_only=False):
    f = F(weight, size, italic, cut); asc, desc = f.getmetrics()
    pad = int(size * .25) + stroke
    w = int(f.getlength(s)) + 2 * pad + 4; h = asc + desc + 2 * pad
    im = Image.new('RGBA', (max(w, 2), max(h, 2)), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if outline_only:
        d.text((pad, pad + asc), s, font=f, anchor='ls', fill=(0, 0, 0, 0), stroke_width=max(2, stroke), stroke_fill=col + (255,))
    else:
        d.text((pad, pad + asc), s, font=f, anchor='ls', fill=col + (255,), stroke_width=stroke, stroke_fill=col + (255,))
    return im, pad, asc  # image, padding, ascent (baseline at pad+asc)

def blit(layer, u, o, P, col=None):
    """draw unit u with transform o = dict(dx,dy,s,sx,sy,rot,a,blur,col,weight,italic,clip)"""
    a = o.get('a', 1.0)
    if a <= 0.003: return
    c = o.get('col') or col or P['color']
    im, pad, asc = glyph(u.s, o.get('weight', P['weight']), P['size'], tuple(c), o.get('italic', P['italic']),
                         P['cut'], P['stroke'], o.get('outline', False))
    sx = o.get('s', 1) * o.get('sx', 1); sy = o.get('s', 1) * o.get('sy', 1)
    ox, oy = pad, pad + asc  # baseline-left origin inside glyph image
    if abs(sx - 1) > .002 or abs(sy - 1) > .002:
        nw, nh = max(1, int(im.width * sx)), max(1, int(im.height * sy))
        im = im.resize((nw, nh), Image.BICUBIC); ox, oy = ox * sx, oy * sy
        # keep visual centre of the unit fixed
        cxu = u.x + u.w / 2; ox_c = ox + u.w * sx / 2
    else:
        cxu = u.x + u.w / 2; ox_c = ox + u.w / 2
    r = o.get('rot', 0)
    if abs(r) > .05:
        cx0, cy0 = ox_c, oy - P['size'] * .35 * sy
        im = im.rotate(r, Image.BICUBIC, expand=False, center=(cx0, cy0))
    b = o.get('blur', 0)
    if b > .4:
        e = int(b * 2) + 2; big = Image.new('RGBA', (im.width + 2 * e, im.height + 2 * e)); big.paste(im, (e, e))
        im = big.filter(ImageFilter.GaussianBlur(b)); ox_c += e; oy += e
    if a < .999:
        im = im.copy(); im.putalpha(im.getchannel('A').point(lambda v: int(v * a)))
    x = cxu - ox_c + o.get('dx', 0); y = u.y - oy + o.get('dy', 0)
    clip = o.get('clip')  # (x0,y0,x1,y1) in layer coords
    if clip:
        tmp = Image.new('RGBA', layer.size); tmp.alpha_composite(im, (int(round(x)), int(round(y))))
        m = Image.new('L', layer.size, 0); ImageDraw.Draw(m).rectangle([int(v) for v in clip], fill=255)
        tmp.putalpha(ImageChops.multiply(tmp.getchannel('A'), m)); layer.alpha_composite(tmp)
    else:
        layer.alpha_composite(im, (int(round(x)), int(round(y))))

def _stagger(i, n, total):
    return 0 if n <= 1 else i * total / (n - 1)

# ---------------- effects: per-unit transform functions ----------------
# signature f(u, t, P) -> dict ; P has 'stag' (total stagger s), 'in' (unit in-duration s)
def _p(u, t, P, order=None):
    i = u.ci if P['_g'] == 'char' else u.wi if P['_g'] == 'word' else u.li
    if order is not None: i = order(u)
    return (t - _stagger(i, u.n, P['stag'])) / P['in']

def e_soft_blur_in(u, t, P):
    p = _p(u, t, P); e = out_cubic(p); return dict(a=e, blur=14 * (1 - e), dy=10 * (1 - e))
def e_rise(u, t, P):
    p = _p(u, t, P); e = out_expo(p); return dict(a=cl(p * 2), dy=P['size'] * .55 * (1 - e))
def e_drop(u, t, P):
    p = _p(u, t, P); e = out_expo(p); return dict(a=cl(p * 3), dy=-P['size'] * 1.1 * (1 - e))
def e_bounce_drop(u, t, P):
    p = _p(u, t, P); return dict(a=cl(p * 4), dy=-P['size'] * 1.4 * (1 - bounce(p)))
def e_center_out(u, t, P):
    m = (u.n - 1) / 2; p = _p(u, t, P, order=lambda u: abs(u.ci - m) * 2); e = out_back(p, 1.4)
    return dict(a=cl(p * 2), s=.4 + .6 * e)
def e_edges_in(u, t, P):
    m = (u.n - 1) / 2; p = _p(u, t, P, order=lambda u: (m - abs(u.ci - m)) * 2); e = out_cubic(p)
    side = -1 if u.ci < m else 1; return dict(a=e, dx=side * 120 * (1 - e))
def e_wave(u, t, P):
    p = _p(u, t, P); e = out_cubic(p)
    return dict(a=e, dy=P['size'] * .4 * (1 - e) + math.sin(t * 7 - u.ci * .55) * P['size'] * .05 * min(1, p))
def e_flip(u, t, P):  # 3D-ish card flip per letter
    p = _p(u, t, P); e = out_back(p, 1.2); return dict(a=cl(p * 3), sx=max(.02, abs(math.cos((1 - e) * math.pi / 2))), dy=8 * (1 - e))
def e_elastic(u, t, P):  # stretch from middle letter, keeps baseline
    m = (u.n - 1) / 2; d = abs(u.ci - m) / max(1, m); p = cl((t - d * .35) / .9)
    k = math.sin(p * math.pi) * (1 - d * .55); return dict(sy=1 + .55 * k, sx=1 - .28 * k, dy=0)
def e_spring_word(u, t, P):
    p = _p(u, t, P); return dict(a=cl(p * 4), s=max(.01, spring(p)))
def e_slide_right(u, t, P):
    p = _p(u, t, P); e = out_quart(p); return dict(a=e, dx=-70 * (1 - e))
def e_slide_down(u, t, P):
    p = _p(u, t, P); e = out_quart(p); return dict(a=e, dy=-60 * (1 - e))
def e_shared_axis_y(u, t, P):
    p = _p(u, t, P); e = lux(p); return dict(a=e, dy=40 * (1 - e))
def e_crossfade(u, t, P):
    p = _p(u, t, P); return dict(a=inout_sine(p))
def e_depth(u, t, P):
    p = _p(u, t, P); e = out_cubic(p); z = 1 + (u.wi % 3) * .35
    return dict(a=e, s=1 + .9 * z * (1 - e), blur=10 * z * (1 - e))
def e_tracking_in(u, t, P):  # letters converge from wide tracking
    p = cl(t / (P['in'] + P['stag'])); e = lux(p); m = (u.n - 1) / 2
    return dict(a=e, dx=(u.ci - m) * P['size'] * .22 * (1 - e))
def e_focus(u, t, P):
    p = cl(t / P['in']); e = out_cubic(p); return dict(a=cl(p * 2.5), blur=22 * (1 - e), s=1.06 - .06 * e)
def e_micro_scale(u, t, P):
    p = cl(t / P['in']); e = lux(p); return dict(a=e, s=.94 + .06 * e)
def e_fade_through(u, t, P):
    p = cl(t / P['in']); e = out_cubic(p); return dict(a=e, s=.92 + .08 * e)
def e_shared_axis_z(u, t, P):
    p = cl(t / P['in']); e = lux(p); return dict(a=e, s=1.25 - .25 * e)
def e_slam(u, t, P):
    p = cl(t / .2); e = in_cubic(p); sh = 0
    if t > .2: q = t - .2; sh = math.exp(-q * 14) * math.sin(q * 70) * 16
    return dict(a=cl(p * 3), s=2.6 - 1.6 * e, dx=sh, dy=sh * .5)
def e_typewriter(u, t, P):
    return dict(a=1.0 if t >= u.ci * P['cps'] else 0.0)
def e_scramble(u, t, P):
    settle = .25 + u.ci * P['stag'] / max(1, u.n - 1)
    if t >= settle or u.s == ' ': return dict(a=1)
    if t < u.ci * .015: return dict(a=0)
    return dict(a=.85, glyph=random.Random(int(t * 30) * 131 + u.ci).choice('ABCDEFGHJKLMNPRSTVXYZ0123456789#%&'), col=P['accent'])
def e_weight_wave(u, t, P):  # Light -> Bold travelling wave
    p = _p(u, t, P); return dict(weight='Bold' if p > .5 else 'Light', s=1 + .06 * math.sin(cl(p) * math.pi))
def e_line_slide(u, t, P):
    p = _p(u, t, P); e = out_quart(p); return dict(a=e, dx=-140 * (1 - e))
def e_mask_up(u, t, P):
    p = _p(u, t, P); e = lux(p); h = P['L']
    return dict(dy=h * 1.05 * (1 - e), clip=(0, u.y - P['size'] * .95, P['W'], u.y + P['size'] * .32))
def e_mask_down(u, t, P):
    p = _p(u, t, P); e = lux(p); h = P['L']
    return dict(dy=-h * 1.05 * (1 - e), clip=(0, u.y - P['size'] * .95, P['W'], u.y + P['size'] * .32))
def e_blur_out_up(u, t, P):  # exit as an entrance-style effect (used by exit=)
    p = cl(t); e = in_cubic(p); return dict(a=1 - e, blur=12 * e, dy=-50 * e)

EFFECTS = {
    # per-character
    'soft-blur-in': ('char', e_soft_blur_in, .55, .5), 'per-character-rise': ('char', e_rise, .5, .45),
    'drop-letters': ('char', e_drop, .55, .5), 'bounce-letters': ('char', e_bounce_drop, .8, .5),
    'stagger-from-center': ('char', e_center_out, .45, .5), 'stagger-from-edges': ('char', e_edges_in, .5, .5),
    'wave': ('char', e_wave, .5, .5), 'flip-letters': ('char', e_flip, .5, .55), 'elastic-stretch': ('char', e_elastic, 1, 0),
    'tracking-in': ('char', e_tracking_in, .9, .3), 'typewriter': ('char', e_typewriter, .1, 0),
    'scramble-decode': ('char', e_scramble, .1, .8), 'weight-wave': ('char', e_weight_wave, .35, .6),
    # per-word
    'word-pop': ('word', e_spring_word, .5, .5), 'short-slide-right': ('word', e_slide_right, .45, .45),
    'short-slide-down': ('word', e_slide_down, .45, .45), 'shared-axis-y': ('word', e_shared_axis_y, .6, .45),
    'word-crossfade': ('word', e_crossfade, .45, .5), 'depth-parallax': ('word', e_depth, .7, .45),
    'kinetic-center-build': ('word', None, .35, .5), 'karaoke-pill': ('word', None, .3, 0),
    'highlighter': ('word', None, .4, 0), 'underline-sweep': ('word', None, .5, 0),
    'strike-through': ('word', None, .45, 0), 'word-swap': ('word', None, .45, 0), 'accent-color-shift': ('word', None, .4, 0),
    # per-line
    'mask-reveal-up': ('line', e_mask_up, .7, .25), 'mask-reveal-down': ('line', e_mask_down, .7, .25),
    'line-by-line-slide': ('line', e_line_slide, .55, .3),
    # whole
    'focus-blur-resolve': ('whole', e_focus, .6, 0), 'micro-scale-fade': ('whole', e_micro_scale, .6, 0),
    'fade-through': ('whole', e_fade_through, .5, 0), 'shared-axis-z': ('whole', e_shared_axis_z, .7, 0),
    'slam-shake': ('whole', e_slam, .2, 0), 'glitch-rgb': ('whole', None, .35, 0), 'glow-pulse': ('whole', None, .5, 0),
    'shimmer-sweep': ('whole', None, 1.0, 0), 'outline-to-fill': ('whole', None, .8, 0),
    'texture-fill-rise': ('whole', None, 1.3, 0), 'counter-roll': ('whole', None, 1.0, 0), 'odometer': ('whole', None, 1.0, 0),
}
EXITS = {'fade': None, 'blur-out-up': None, 'scale-down-fade': None, 'slide-out-left': None, 'mask-down-out': None}

def _exit_o(kind, q):  # q = 0..1 exit progress
    e = in_cubic(q)
    if kind == 'blur-out-up': return dict(a=1 - e, blur=12 * e, dy=-50 * e)
    if kind == 'scale-down-fade': return dict(a=1 - e, s=1 - .12 * e)
    if kind == 'slide-out-left': return dict(a=1 - e, dx=-160 * e)
    return dict(a=1 - e)

def _merge(o, x):
    if not x: return o
    o = dict(o)
    for k, v in x.items():
        if k == 'a': o['a'] = o.get('a', 1) * v
        elif k == 's': o['s'] = o.get('s', 1) * v
        elif k in ('dx', 'dy', 'blur'): o[k] = o.get(k, 0) + v
        else: o[k] = v
    return o

def _shadow(layer, strength=.55, r=14, off=(0, 6)):
    a = layer.getchannel('A').filter(ImageFilter.GaussianBlur(r)).point(lambda v: int(v * strength))
    sh = Image.new('RGBA', layer.size, (0, 0, 0, 0)); sh.putalpha(a)
    out = Image.new('RGBA', layer.size); out.alpha_composite(sh, off); out.alpha_composite(layer); return out

def render(effect, text, t, W=1080, H=1920, cx=None, cy=None, size=130, weight='Medium', italic=False, cut='',
           color=(255, 255, 255), accent=(169, 33, 192), accent_words=(), lh=1.0, tracking=0.0, shadow=False,
           stroke=0, dur=None, exit='fade', exit_t=.3, stag=None, tin=None, swap=None, number=None, suffix='',
           texture=None, pill=(255, 255, 255), pill_text=(18, 18, 20), word_times=None, cps=.045):
    """Return an RGBA layer (W,H) with `text` animated by `effect` at local time t."""
    g, fn, din, dstag = EFFECTS[effect]
    cx = W / 2 if cx is None else cx; cy = H / 2 if cy is None else cy
    f = F(weight, size, italic, cut)
    chars, words, lns, L = layout(text, f, cx, cy, lh, tracking)
    P = dict(size=size, weight=weight, italic=italic, cut=cut, color=tuple(color), accent=tuple(accent), stroke=stroke,
             stag=dstag if stag is None else stag, **{'in': din if tin is None else tin}, _g=g, L=L, W=W, H=H, cps=cps)
    acc = {w.lower().strip('.,!?') for w in accent_words}
    layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ex = None
    if dur is not None and t > dur - exit_t: ex = _exit_o(exit, cl((t - (dur - exit_t)) / exit_t))
    def wcol(wi):
        return P['accent'] if words and words[min(wi, len(words) - 1)].s.lower().strip('.,!?') in acc else P['color']
    # word timing: real word onsets (from transcript) override the stagger
    def wstart(i):
        if word_times: return word_times[min(i, len(word_times) - 1)]
        return stag_(i)
    def stag_(i): return _stagger(i, len(words), P['stag'])

    if fn is not None:
        units = chars if g == 'char' else words if g == 'word' else lns if g == 'line' else lns
        for u in units:
            tt = t
            if g == 'word' and word_times: tt = t - wstart(u.wi) + stag_(u.wi)
            o = fn(u, tt, P) if g != 'whole' else fn(u, t, P)
            o = _merge(o, ex)
            if g == 'char':
                c = o.pop('col', None) or wcol(u.wi)
                gl = o.pop('glyph', None)
                if gl: u2 = U(); u2.s, u2.x, u2.y, u2.w = gl, u.x, u.y, u.w; blit(layer, u2, o, P, c)
                elif u.s != ' ': blit(layer, u, o, P, c)
            elif g == 'word':
                blit(layer, u, o, P, wcol(u.wi))
            else:  # line / whole: draw per word so accent colours survive, sharing one transform
                sub = [w for w in words if w.li == u.li]
                if o.get('s', 1) != 1 or o.get('rot', 0):
                    # scale around line centre: shift each word towards centre
                    s = o.get('s', 1); lc = u.x + u.w / 2
                    for w in sub:
                        o2 = dict(o); o2['dx'] = o.get('dx', 0) + (w.x + w.w / 2 - lc) * (s - 1); blit(layer, w, o2, P, wcol(w.wi))
                else:
                    for w in sub: blit(layer, w, o, P, wcol(w.wi))
    else:
        layer = _special(effect, layer, t, P, chars, words, lns, wcol, wstart, ex, locals())
    if effect == 'typewriter':  # blinking caret after the last typed char
        vis = [c for c in chars if t >= c.ci * cps]
        if vis and (int(t * 2.2) % 2 == 0 or len(vis) < len(chars)) and (ex is None or ex.get('a', 1) > .5):
            c = vis[-1]; x = c.x + c.w + size * .04
            ImageDraw.Draw(layer).rectangle([x, c.y - size * .72, x + max(5, size * .05), c.y + size * .08], fill=tuple(accent) + (255,))
    if shadow: layer = _shadow(layer)
    return layer

def _special(effect, layer, t, P, chars, words, lns, wcol, wstart, ex, kw):
    size = P['size']
    def word_in(w, extra=None, how='rise'):
        p = cl((t - wstart(w.wi)) / P['in']); e = out_quart(p)
        o = dict(a=e, dy=size * .25 * (1 - e)) if how == 'rise' else dict(a=e)
        return _merge(_merge(o, extra), ex)
    if effect == 'kinetic-center-build':
        # words appear one by one and the line re-centres smoothly around them
        for ln in lns:
            sub = [w for w in words if w.li == ln.li]
            vis = [w for w in sub if t >= wstart(w.wi)]
            if not vis: continue
            def wid(k): return sub[k - 1].x + sub[k - 1].w - sub[0].x if k else 0
            k = len(vis); last = vis[-1]; pe = out_cubic((t - wstart(last.wi)) / .35)
            wnow = wid(k - 1) + (wid(k) - wid(k - 1)) * pe
            shift = (ln.w - wnow) / 2
            for w in vis:
                o = word_in(w, dict(dx=shift), how='pop'); pp = cl((t - wstart(w.wi)) / .35)
                o['s'] = o.get('s', 1) * (.6 + .4 * out_back(pp, 1.6)); blit(layer, w, o, P, wcol(w.wi))
    elif effect == 'karaoke-pill':
        d = ImageDraw.Draw(layer)
        act = max([w for w in words if t >= wstart(w.wi)], key=lambda w: w.wi, default=None)
        if act is not None:
            prev = words[act.wi - 1] if act.wi > 0 else act; p = out_cubic((t - wstart(act.wi)) / .18)
            x0 = prev.x + (act.x - prev.x) * p; x1 = prev.x + prev.w + (act.x + act.w - prev.x - prev.w) * p
            y0 = prev.y + (act.y - prev.y) * p
            a = 1 if ex is None else ex.get('a', 1)
            d.rounded_rectangle([x0 - size * .18, y0 - size * .82, x1 + size * .18, y0 + size * .22], radius=size * .5,
                                fill=tuple(P['accent']) + (int(255 * a),))
        for w in words:
            on = t >= wstart(w.wi); o = _merge(dict(a=1 if on else .45), ex)
            blit(layer, w, o, P, P['color'])
    elif effect in ('highlighter', 'underline-sweep', 'strike-through'):
        marks = Image.new('RGBA', layer.size); d = ImageDraw.Draw(marks)
        for w in words:
            o = word_in(w); blit(layer, w, o, P, wcol(w.wi) if effect != 'highlighter' else P['color'])
            if w.s.lower().strip('.,!?') in {x for x in kw['acc']} or not kw['acc']:
                p = out_cubic((t - wstart(w.wi) - .2) / .4)
                if p <= 0: continue
                x0, x1 = w.x - 8, w.x + (w.w + 16) * p - 8
                a = int(255 * (1 if ex is None else ex.get('a', 1)))
                if effect == 'highlighter':
                    d.rectangle([x0, w.y - size * .62, x1, w.y + size * .08], fill=tuple(P['accent']) + (int(a * .85),))
                elif effect == 'underline-sweep':
                    d.rectangle([x0, w.y + size * .1, x1, w.y + size * .1 + max(6, size * .06)], fill=tuple(P['accent']) + (a,))
                else:
                    yy = w.y - size * .3; d.rectangle([x0, yy, x1, yy + max(7, size * .07)], fill=tuple(P['accent']) + (a,))
        if effect == 'highlighter':
            out = Image.new('RGBA', layer.size); out.alpha_composite(marks); out.alpha_composite(layer); layer = out
        else:
            layer.alpha_composite(marks)
    elif effect == 'accent-color-shift':
        for w in words:
            o = word_in(w); is_acc = w.s.lower().strip('.,!?') in kw['acc']
            if is_acc:
                p = cl((t - wstart(w.wi) - .35) / .3); c = tuple(int(P['color'][i] + (P['accent'][i] - P['color'][i]) * p) for i in range(3))
                o['s'] = o.get('s', 1) * (1 + .08 * math.sin(p * math.pi))
            else: c = P['color']
            blit(layer, w, o, P, c)
    elif effect == 'word-swap':
        # last word of the text cycles through kw['swap'] in a clipped slot
        swap = kw['swap'] or [words[-1].s]; last = words[-1]
        for w in words[:-1]: blit(layer, w, _merge(dict(a=out_cubic(t / .4)), ex), P, wcol(w.wi))
        per = 0.75; k = min(int(t / per), len(swap) - 1); q = out_expo((t - k * per) / .35) if k else 1
        clip = (0, last.y - size * .95, P['W'], last.y + size * .3)
        for j, txt in ((k, swap[k]), (k - 1, swap[k - 1] if k else None)):
            if txt is None: continue
            u = U(); u.s, u.x, u.y = txt, last.x, last.y; u.w = F(P['weight'], size, P['italic'], P['cut']).getlength(txt)
            dy = size * 1.1 * (1 - q) if j == k else -size * 1.1 * q
            if j == k and k == 0: dy = 0
            blit(layer, u, _merge(dict(dy=dy, clip=clip, a=1 if j == k else 1 - q), ex), P, P['accent'])
    elif effect in ('glitch-rgb', 'glow-pulse', 'shimmer-sweep', 'outline-to-fill', 'texture-fill-rise'):
        base = Image.new('RGBA', layer.size)
        o0 = _merge(dict(a=cl(t / .12)), ex)
        for w in words: blit(base, w, o0, P, wcol(w.wi))
        if effect == 'glitch-rgb':
            if t < P['in']:
                r, gch, b, a = base.split(); amt = int(26 * (1 - t / P['in']))
                rnd = random.Random(int(t * 24))
                r = ImageChops.offset(r, amt, 0); b = ImageChops.offset(b, -amt, 0)
                img = Image.merge('RGBA', (r, gch, b, ImageChops.lighter(a, ImageChops.offset(a, amt, 0))))
                for _ in range(5):  # row slices
                    y = rnd.randrange(0, layer.height - 40); h = rnd.randrange(8, 40); dx = rnd.randrange(-50, 50)
                    sl = img.crop((0, y, layer.width, y + h)); img.paste((0, 0, 0, 0), (0, y, layer.width, y + h)); img.paste(sl, (dx, y))
                layer = img
            else: layer = base
        elif effect == 'glow-pulse':
            k = .5 + .5 * math.sin(t * 4.2)
            gl = Image.new('RGBA', layer.size, tuple(P['accent']) + (0,)); gl.putalpha(base.getchannel('A').filter(ImageFilter.GaussianBlur(26)).point(lambda v: int(min(255, v * (1.2 + 1.3 * k)))))
            layer = Image.new('RGBA', layer.size); layer.alpha_composite(gl); layer.alpha_composite(base)
        elif effect == 'shimmer-sweep':
            band = Image.new('L', layer.size, 0); d = ImageDraw.Draw(band)
            xpos = -400 + (layer.width + 800) * inout_sine((t % 1.6) / 1.2)
            for i in range(-90, 91, 6):
                v = int(255 * math.exp(-(i / 55) ** 2)); d.polygon([(xpos + i, 0), (xpos + i + 6, 0), (xpos + i + 6 - 500, layer.height), (xpos + i - 500, layer.height)], fill=v)
            m = ImageChops.multiply(band, base.getchannel('A'))
            white = Image.new('RGBA', layer.size, (255, 255, 255, 0)); white.putalpha(m.point(lambda v: int(v * .9)))
            layer = base; layer.alpha_composite(white)
        elif effect == 'outline-to-fill':
            ol = Image.new('RGBA', layer.size)
            for w in words: blit(ol, w, _merge(dict(a=cl(t / .15), outline=True), ex), dict(P, stroke=3), wcol(w.wi))
            p = cl((t - .25) / P['in']); e = lux(p)
            # fill rises bottom->top
            top = min(w.y - size * .75 for w in words); bot = max(w.y + size * .1 for w in words)
            yl = bot - (bot - top) * e; m = Image.new('L', layer.size, 0); ImageDraw.Draw(m).rectangle([0, yl, layer.width, layer.height], fill=255)
            fill = base.copy(); fill.putalpha(ImageChops.multiply(base.getchannel('A'), m))
            layer = ol; layer.alpha_composite(fill)
        else:  # texture-fill-rise: photo/texture only inside the letters, edge rises
            tex = kw['texture']
            if tex is None: tex = Image.new('RGBA', layer.size, tuple(P['accent']) + (255,))
            tex = tex.convert('RGBA').resize(layer.size)
            top = min(w.y - size * .75 for w in words); bot = max(w.y + size * .1 for w in words)
            e = lux(cl(t / P['in'])); yl = bot - (bot - top) * e
            ol = Image.new('RGBA', layer.size)
            for w in words: blit(ol, w, _merge(dict(a=.9, outline=True), ex), dict(P, stroke=2), P['color'])
            m = Image.new('L', layer.size, 0); ImageDraw.Draw(m).rectangle([0, yl, layer.width, layer.height], fill=255)
            a = ImageChops.multiply(base.getchannel('A'), m); tx = tex.copy(); tx.putalpha(a)
            layer = ol; layer.alpha_composite(tx)
            if 0 < e < 1:  # edge marker line
                ImageDraw.Draw(layer).rectangle([min(w.x for w in words) - 20, yl - 2, max(w.x + w.w for w in words) + 20, yl + 2], fill=tuple(P['accent']) + (255,))
    elif effect in ('counter-roll', 'odometer'):
        target = kw['number'] if kw['number'] is not None else 92
        if effect == 'counter-roll':
            v = int(round(target * out_expo(cl(t / P['in'])))); s = f"{v}{kw['suffix']}"
            u = U(); f = F(P['weight'], size, P['italic'], P['cut']); u.w = f.getlength(s); u.s = s
            u.x = P['W'] / 2 - u.w / 2 if kw['cx'] is None else kw['cx'] - u.w / 2; u.y = lns[0].y
            blit(layer, u, _merge(dict(a=cl(t / .1)), ex), P, P['color'])
        else:
            s = f"{target}{kw['suffix']}"; f = F(P['weight'], size, P['italic'], P['cut'])
            x = (P['W'] if kw['cx'] is None else 2 * kw['cx']) / 2 - f.getlength(s) / 2; y = lns[0].y
            clip = (0, y - size * .95, P['W'], y + size * .3)
            for i, ch in enumerate(s):
                cw = f.getlength(ch)
                if ch.isdigit():
                    d = int(ch); turns = 2 + i; pos = (turns * 10 + d) * out_expo(cl((t - i * .08) / P['in']))
                    base_d = int(pos) % 10; frac = pos - int(pos)
                    for k2, dd in ((0, base_d), (1, (base_d + 1) % 10)):
                        u = U(); u.s, u.x, u.y, u.w = str(dd), x, y, cw
                        blit(layer, u, _merge(dict(dy=(k2 - frac) * size * 1.1, clip=clip), ex), P, P['color'])
                else:
                    u = U(); u.s, u.x, u.y, u.w = ch, x, y, cw; blit(layer, u, _merge(dict(a=cl(t / .3)), ex), P, P['accent'])
                x += cw
    return layer

