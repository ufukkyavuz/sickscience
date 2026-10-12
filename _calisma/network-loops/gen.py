"""NetWork / NX35 explainer loops (1080x1080, seamless). Source: Canva deck 'NetWork Presentation 2026' (DAG_mTNwzQ0)."""
import math, os, shutil, json

ROOT = os.path.dirname(os.path.abspath(__file__))
MAG, RED, INK, DARK = "#A921C0", "#D6141F", "#141414", "#0B0A0F"

HEAD = """<!doctype html>
<html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1080" />
<title>{title}</title>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
  @font-face {{ font-family: "FG"; src: url("assets/FoundersGrotesk-Regular.otf"); font-weight: 400; }}
  @font-face {{ font-family: "FG"; src: url("assets/FoundersGrotesk-Medium.otf"); font-weight: 500; }}
  @font-face {{ font-family: "FG"; src: url("assets/FoundersGrotesk-Semibold.otf"); font-weight: 600; }}
  @font-face {{ font-family: "FG"; src: url("assets/FoundersGrotesk-Bold.otf"); font-weight: 700; }}
  html, body {{ margin: 0; background: #000; }}
  #root {{ position: relative; width: 1080px; height: 1080px; overflow: hidden; font-family: "FG", sans-serif; }}
  .fill {{ position: absolute; inset: 0; }}
  .abs {{ position: absolute; }}
  .logo {{ position: absolute; left: 70px; bottom: 56px; width: 230px; height: auto; }}
  .t {{ position: absolute; line-height: 1.05; }}
  {css}
</style></head><body>
<div id="root" data-composition-id="main" data-width="1080" data-height="1080" data-duration="{dur}">
  <div class="fill" style="background:{bg}"></div>
{body}
  <img class="logo" src="assets/{logo}" />
</div>
<script>
  window.__timelines = window.__timelines || {{}};
  const tl = gsap.timeline({{ paused: true }});
{js}
  tl.set({{}}, {{}}, {dur});
  window.__timelines["main"] = tl;
</script></body></html>
"""

def write(name, title, dur, bg, logo, body, css, js):
    d = os.path.join(ROOT, name); os.makedirs(os.path.join(d, "assets"), exist_ok=True)
    for f in os.listdir(os.path.join(ROOT, "shared")):
        shutil.copy(os.path.join(ROOT, "shared", f), os.path.join(d, "assets", f))
    open(os.path.join(d, "index.html"), "w").write(HEAD.format(title=title, dur=dur, bg=bg, logo=logo, body=body, css=css, js=js))

# ---------- L1 NX35 signal network (dark) ----------
cx, cy, R = 540, 640, 290
nodes = [(cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a))) for a in range(-90, 270, 60)]
b, j = [], []
for i, (x, y) in enumerate(nodes):
    ang = math.degrees(math.atan2(y - cy, x - cx))
    b.append(f'<div class="abs ln" style="left:{cx}px;top:{cy-2}px;width:{R}px;transform:rotate({ang:.1f}deg)"></div>')
for i, (x, y) in enumerate(nodes):
    b.append(f'<div class="abs node" id="n{i}" style="left:{x-58:.0f}px;top:{y-58:.0f}px"><div class="glow" id="g{i}"></div><div class="core"></div></div>')
b.append(f'<div class="abs hub" id="hub" style="left:{cx-80}px;top:{cy-80}px"><span>NX35</span></div>')
k = 0
for wave_t, idxs in [(0.3, [0, 2, 4]), (2.3, [1, 3, 5]), (4.1, [0, 1, 2, 3, 4, 5])]:
    for i in idxs:
        x, y = nodes[i]; dx, dy = x - cx, y - cy
        b.append(f'<div class="abs dot" id="d{k}" style="left:{cx-11}px;top:{cy-11}px"></div>')
        j.append(f'tl.fromTo("#d{k}",{{x:0,y:0,opacity:0,scale:0.6}},{{x:{dx*0.12:.0f},y:{dy*0.12:.0f},opacity:1,scale:1,duration:0.2,ease:"power1.out"}},{wave_t});')
        j.append(f'tl.to("#d{k}",{{x:{dx*0.82:.0f},y:{dy*0.82:.0f},duration:1.0,ease:"power1.inOut"}},{wave_t+0.2});')
        j.append(f'tl.to("#d{k}",{{opacity:0,scale:0.2,duration:0.18}},{wave_t+1.2});')
        j.append(f'tl.to("#g{i}",{{opacity:1,scale:1.35,duration:0.25,ease:"power2.out"}},{wave_t+1.2});')
        j.append(f'tl.to("#g{i}",{{opacity:0,scale:1,duration:0.6,ease:"power2.in"}},{wave_t+1.45});')
        k += 1
for t in [0, 1, 2, 3, 4, 5]:
    j.append(f'tl.to("#hub",{{scale:1.08,duration:0.5,ease:"sine.inOut"}},{t});tl.to("#hub",{{scale:1,duration:0.5,ease:"sine.inOut"}},{t+0.5});')
b.insert(0, f'<div class="t" style="left:70px;top:64px;font-size:132px;font-weight:700;color:{MAG}">NX35<sup style="font-size:48px">™</sup></div>')
b.insert(1, '<div class="t" style="left:72px;top:212px;width:880px;font-size:40px;font-weight:500;color:#fff;line-height:1.2">A biomimetic exosome technology that signals cells with <b style="color:#E9B6F2">coded information</b> at the molecular level.</div>')
css = f""".ln {{ height:4px; background:linear-gradient(90deg, rgba(169,33,192,.9), rgba(169,33,192,.25)); transform-origin:0 50%; }}
.node {{ width:116px; height:116px; }} .node .core {{ position:absolute; inset:18px; border-radius:50%; border:4px solid {MAG}; background:#1b1222; }}
.node .glow {{ position:absolute; inset:0; border-radius:50%; background:radial-gradient(circle, rgba(233,182,242,.95) 0%, rgba(169,33,192,.55) 45%, rgba(169,33,192,0) 70%); opacity:0; }}
.hub {{ width:160px; height:160px; border-radius:50%; background:{MAG}; box-shadow:0 0 60px rgba(169,33,192,.7); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:700; font-size:44px; }}
.dot {{ width:22px; height:22px; border-radius:50%; background:#F3D3F8; box-shadow:0 0 18px #E9B6F2; opacity:0; }}"""
write("01-nx35-signal", "NX35 signal network", 6, DARK, "logo_white.png", "\n".join("  " + x for x in b), css, "\n".join("  " + x for x in j))

# ---------- L2 1/1000th the size of a cell (white) ----------
b, j = [], []
b.append(f'<div class="t" style="left:70px;top:70px;width:940px;font-size:84px;font-weight:700;color:{INK}">Exosomes are <span style="color:{MAG}">1/1000th</span> the size of a cell</div>')
b.append('<div class="t" style="left:72px;top:262px;width:820px;font-size:36px;font-weight:500;color:#555;line-height:1.2">Small enough to effectively penetrate the epidermis.</div>')
b.append('<div class="abs" id="cell" style="left:520px;top:400px;width:470px;height:470px"><div class="cellm"></div><div class="nuc"></div></div>')
b.append('<div class="t" style="left:690px;top:890px;font-size:32px;font-weight:600;color:#A921C0">skin cell</div>')
b.append('<div class="t" style="left:80px;top:890px;font-size:32px;font-weight:600;color:#555">plant exosomes</div>')
j.append('tl.to("#cell",{scale:1.03,duration:1.5,ease:"sine.inOut"},0);tl.to("#cell",{scale:1,duration:1.5,ease:"sine.inOut"},1.5);tl.to("#cell",{scale:1.03,duration:1.5,ease:"sine.inOut"},3);tl.to("#cell",{scale:1,duration:1.5,ease:"sine.inOut"},4.5);')
T, period = 2.2, 0.3
lanes = [500, 560, 620, 680, 740, 800, 860]
spawns = [round(-T + i * period, 2) for i in range(int((6 + T) / period) + 1)]
k = 0
for n, s in enumerate(spawns):
    if s >= 6: continue
    y0 = lanes[n % len(lanes)]; x0, x1 = 60, 610; y1 = 635 + (y0 - 680) * 0.35
    b.append(f'<div class="abs exo" id="e{k}" style="left:0px;top:0px"></div>')
    def pos(t):
        p = max(0, min(1, (t - s) / T)); return x0 + (x1 - x0) * p, y0 + (y1 - y0) * p, p
    t0 = max(0, s); t1 = min(6, s + T)
    xa, ya, pa = pos(t0); xb, yb, pb = pos(t1)
    oa = 0 if pa <= 0.001 else (1 if pa < 0.85 else (1 - pa) / 0.15)
    j.append(f'tl.set("#e{k}",{{x:{xa:.0f},y:{ya:.0f},opacity:{oa:.2f}}},{t0});')
    if pa < 0.85:
        tm = min(t1, s + T * 0.85); xm, ym, _ = pos(tm)
        j.append(f'tl.to("#e{k}",{{x:{xm:.0f},y:{ym:.0f},opacity:1,duration:{tm-t0:.3f},ease:"none"}},{t0});')
        if t1 > tm:
            j.append(f'tl.to("#e{k}",{{x:{xb:.0f},y:{yb:.0f},opacity:{0 if pb>=0.999 else (1-pb)/0.15:.2f},duration:{t1-tm:.3f},ease:"none"}},{tm});')
    else:
        j.append(f'tl.to("#e{k}",{{x:{xb:.0f},y:{yb:.0f},opacity:0,duration:{t1-t0:.3f},ease:"none"}},{t0});')
    if s + T <= 6: j.append(f'tl.set("#e{k}",{{opacity:0}},{s+T:.2f});')
    k += 1
css = f""".cellm {{ position:absolute; inset:0; border-radius:50%; background:radial-gradient(circle at 40% 35%, #fbeefd 0%, #f2d6f6 55%, #e7bdef 100%); border:5px solid {MAG}; }}
.nuc {{ position:absolute; left:150px; top:140px; width:170px; height:170px; border-radius:50%; background:rgba(169,33,192,.35); border:4px solid rgba(169,33,192,.7); }}
.exo {{ width:22px; height:22px; margin:-11px 0 0 -11px; border-radius:50%; background:{MAG}; box-shadow:0 0 10px rgba(169,33,192,.6); opacity:0; }}"""
write("02-tiny-exosome", "1/1000th the size of a cell", 6, "#FFFFFF", "logo.png", "\n".join("  " + x for x in b), css, "\n".join("  " + x for x in j))

# ---------- L3 Safe / Effective / Stable (dark) ----------
ICON = {
 "safe": '<svg viewBox="0 0 100 100" width="96" height="96"><path d="M50 88 V48" stroke="#fff" stroke-width="6" stroke-linecap="round" fill="none"/><path d="M50 54 C30 54 18 40 18 22 C36 22 50 34 50 54Z" fill="#fff"/><path d="M50 46 C66 46 80 36 82 18 C64 18 50 28 50 46Z" fill="#fff"/></svg>',
 "eff": '<svg viewBox="0 0 100 100" width="96" height="96"><circle cx="50" cy="50" r="38" stroke="#fff" stroke-width="6" fill="none"/><circle cx="50" cy="50" r="22" stroke="#fff" stroke-width="6" fill="none"/><circle cx="50" cy="50" r="7" fill="#fff"/></svg>',
 "stab": '<svg viewBox="0 0 100 100" width="96" height="96"><line x1="50" y1="24" x2="24" y2="72" stroke="#fff" stroke-width="6"/><line x1="50" y1="24" x2="76" y2="72" stroke="#fff" stroke-width="6"/><line x1="24" y1="72" x2="76" y2="72" stroke="#fff" stroke-width="6"/><circle cx="50" cy="24" r="12" fill="#fff"/><circle cx="24" cy="72" r="12" fill="#fff"/><circle cx="76" cy="72" r="12" fill="#fff"/></svg>',
}
cols = [("safe", "Safe", "100% vegan + plant-based"), ("eff", "Effective", "Exosome “code” customization"), ("stab", "Stable", "Shelf-life stable")]
b, j = [], []
b.append(f'<div class="t" style="left:70px;top:70px;font-size:36px;font-weight:600;color:{MAG}">Game-changing IP —</div>')
b.append('<div class="t" style="left:68px;top:118px;font-size:140px;font-weight:700;color:#fff">NX35<sup style="font-size:50px">™</sup></div>')
for i, (k_, title, line) in enumerate(cols):
    x = 70 + i * 330
    b.append(f'<div class="abs col" id="c{i}" style="left:{x}px;top:470px"><div class="ic" id="ic{i}">{ICON[k_]}</div><div class="ct">{title}</div><div class="cl">{line}</div></div>')
    t = 0.25 + i * 0.25
    j.append(f'tl.fromTo("#c{i}",{{y:60,opacity:0}},{{y:0,opacity:1,duration:0.55,ease:"back.out(1.7)"}},{t});')
    j.append(f'tl.fromTo("#ic{i}",{{scale:0.4,rotation:-20}},{{scale:1,rotation:0,duration:0.6,ease:"back.out(2.2)",immediateRender:false}},{t});')
    for q in range(3):
        j.append(f'tl.to("#ic{i}",{{y:-12,duration:0.6,ease:"sine.inOut"}},{t+0.7+q*1.2});tl.to("#ic{i}",{{y:0,duration:0.6,ease:"sine.inOut"}},{t+1.3+q*1.2});')
    j.append(f'tl.to("#c{i}",{{y:-40,opacity:0,duration:0.4,ease:"power2.in"}},{5.1+i*0.15});')
css = f""".col {{ width:300px; }} .ic {{ width:220px; height:220px; border-radius:50%; background:{MAG}; display:flex; align-items:center; justify-content:center; box-shadow:0 0 50px rgba(169,33,192,.5); }}
.ct {{ margin-top:34px; font-size:60px; font-weight:700; color:#fff; }} .cl {{ margin-top:10px; font-size:32px; font-weight:500; color:#cfc6d4; line-height:1.2; }}"""
write("03-safe-effective-stable", "Safe Effective Stable", 6, DARK, "logo_white.png", "\n".join("  " + x for x in b), css, "\n".join("  " + x for x in j))

# ---------- L4 Collagen Type I chart (white) ----------
b, j = [], []
b.append(f'<div class="t" style="left:70px;top:70px;width:940px;font-size:66px;font-weight:700;color:{INK}">Radish exosomes reinforce <span style="color:{MAG}">Collagen Type I</span> signaling</div>')
b.append('<div class="t" style="left:72px;top:240px;font-size:34px;font-weight:500;color:#666">Collagen Type I (COL1A1) expression levels</div>')
base_y, x_axis = 900, 200
b.append(f'<div class="abs" style="left:{x_axis}px;top:{base_y}px;width:700px;height:4px;background:#222"></div>')
b.append(f'<div class="abs" style="left:{x_axis}px;top:360px;width:4px;height:{base_y-360+4}px;background:#222"></div>')
bars = [("Control", 300, "#C9C3CD", 330), ("Radish Exosomes", 480, MAG, 610)]
for i, (lab, h, col, x) in enumerate(bars):
    b.append(f'<div class="abs bar" id="b{i}" style="left:{x}px;top:{base_y-h}px;width:170px;height:{h}px;background:{col}"></div>')
    b.append(f'<div class="abs err" id="er{i}" style="left:{x+75}px;top:{base_y-h-50}px;width:20px;height:100px"><i></i><i></i><i></i></div>')
    b.append(f'<div class="t" style="left:{x-60}px;width:290px;text-align:center;top:{base_y+22}px;font-size:32px;font-weight:600;color:{INK}">{lab}</div>')
    t = 0.3 + i * 0.35
    j.append(f'tl.fromTo("#b{i}",{{scaleY:0}},{{scaleY:1,duration:0.9,ease:"power3.out"}},{t});')
    j.append(f'tl.fromTo("#er{i}",{{opacity:0}},{{opacity:1,duration:0.3}},{t+0.8});')
    j.append(f'tl.to("#er{i}",{{opacity:0,duration:0.25}},{5.0});')
    j.append(f'tl.to("#b{i}",{{scaleY:0,duration:0.6,ease:"power2.in"}},{5.2+i*0.1});')
b.append(f'<div class="abs spark" id="sp" style="left:830px;top:380px">↑</div>')
j.append('tl.fromTo("#sp",{scale:0,opacity:0},{scale:1,opacity:1,duration:0.4,ease:"back.out(2.5)"},1.6);tl.to("#sp",{y:-14,duration:0.6,ease:"sine.inOut"},2.1);tl.to("#sp",{y:0,duration:0.6,ease:"sine.inOut"},2.7);tl.to("#sp",{y:-14,duration:0.6,ease:"sine.inOut"},3.3);tl.to("#sp",{y:0,duration:0.6,ease:"sine.inOut"},3.9);tl.to("#sp",{scale:0,opacity:0,duration:0.3},4.9);')
css = f""".bar {{ transform-origin:50% 100%; border-radius:14px 14px 0 0; }}
.err {{ opacity:0; }} .err i {{ position:absolute; background:#222; }} .err i:nth-child(1) {{ left:8px; top:0; width:4px; height:100px; }} .err i:nth-child(2) {{ left:0; top:0; width:20px; height:4px; }} .err i:nth-child(3) {{ left:0; top:96px; width:20px; height:4px; }}
.spark {{ width:90px; height:90px; border-radius:50%; background:{MAG}; color:#fff; font-size:64px; font-weight:700; text-align:center; line-height:88px; }}"""
write("04-collagen-chart", "Collagen Type I", 6, "#FFFFFF", "logo.png", "\n".join("  " + x for x in b), css, "\n".join("  " + x for x in j))

# ---------- L5 Clinical results (dark) ----------
stats = [(94, "Feels smoother skin"), (84, "Feels that fine lines visually reduced"), (90, "Increases the firmness of the skin"),
         (86, "Feels healthy glow in their skin"), (94, "Feels deeply moisturized"), (100, "Experienced decrease in wrinkle count")]
SL = 1.2; dur5 = round(SL * len(stats), 2)
b, j = [], []
b.append(f'<div class="t" style="left:70px;top:70px;font-size:40px;font-weight:600;color:{MAG}">Clinical Test Results</div>')
b.append('<div class="t" style="left:70px;top:122px;font-size:60px;font-weight:700;color:#fff">NX35<sup style="font-size:26px">™</sup> Activate</div>')
for i, (n, lab) in enumerate(stats):
    b.append(f'<div class="abs st" id="s{i}"><div class="num"><span id="sn{i}">{n}</span>%</div><div class="lab">{lab}</div></div>')
    t = i * SL
    j.append(f'tl.fromTo("#s{i}",{{x:120,opacity:0}},{{x:0,opacity:1,duration:0.3,ease:"power3.out"}},{t:.2f});')
    j.append(f'const c{i}={{v:{max(0,n-30)}}}; tl.to(c{i},{{v:{n},duration:0.45,ease:"power2.out",onUpdate:()=>{{document.getElementById("sn{i}").textContent=Math.round(c{i}.v);}}}},{t:.2f});')
    j.append(f'tl.to("#s{i}",{{x:-120,opacity:0,duration:0.25,ease:"power2.in"}},{t+SL-0.25:.2f});')
    b.append(f'<div class="abs pd" id="p{i}" style="left:{70+i*44}px;top:820px"></div>')
    j.append(f'tl.to("#p{i}",{{backgroundColor:"{MAG}",scale:1.25,duration:0.2}},{t:.2f});tl.to("#p{i}",{{backgroundColor:"#3a3340",scale:1,duration:0.2}},{t+SL-0.2:.2f});')
b.append('<div class="t" style="left:70px;top:880px;width:940px;font-size:32px;font-weight:400;color:#9b93a0;line-height:1.25">Raw material only, not final formula · 50 volunteers, women aged 40–55 · Results at 28 &amp; 56 days · 3rd-party verified testing clinic</div>')
css = f""".st {{ left:70px; top:290px; width:940px; opacity:0; }} .num {{ font-size:300px; font-weight:700; color:#fff; line-height:1; }} .num span {{ color:#fff; }}
.lab {{ margin-top:16px; font-size:52px; font-weight:600; color:{MAG}; line-height:1.15; }} .pd {{ width:24px; height:24px; border-radius:50%; background:#3a3340; }}"""
write("05-clinical-results", "Clinical results", dur5, DARK, "logo_white.png", "\n".join("  " + x for x in b), css, "\n".join("  " + x for x in j))

# ---------- L6 NetWork product + attributes (light) ----------
chips = [("Fragrance-free", 40, 420), ("Vegan", 40, 560), ("Cruelty-free", 40, 700), ("Dermatologist tested", 700, 420), ("Hypoallergenic", 700, 560), ("No parabens", 700, 700)]
b, j = [], []
b.append(f'<div class="t" style="left:0;width:1080px;text-align:center;top:64px;font-size:110px;font-weight:700;color:{INK}">NetWork</div>')
b.append(f'<div class="t" style="left:0;width:1080px;text-align:center;top:184px;font-size:40px;font-weight:500;color:{RED}">Rich Concentrated Serum · powered by NX35™</div>')
b.append('<div class="abs" id="sh" style="left:430px;top:968px;width:220px;height:36px;border-radius:50%;background:radial-gradient(closest-side, rgba(90,10,20,.35), rgba(90,10,20,0))"></div>')
b.append('<img class="abs" id="prod" src="assets/network.png" style="left:443px;top:300px;width:194px;height:600px" />')
b.append(f'<div class="abs price" style="left:780px;top:960px">$74 · 30 ml</div>')
for t in [0, 1.5, 3, 4.5]:
    j.append(f'tl.to("#prod",{{y:-16,duration:0.75,ease:"sine.inOut"}},{t});tl.to("#prod",{{y:0,duration:0.75,ease:"sine.inOut"}},{t+0.75});')
    j.append(f'tl.to("#sh",{{scale:0.88,opacity:0.7,duration:0.75,ease:"sine.inOut"}},{t});tl.to("#sh",{{scale:1,opacity:1,duration:0.75,ease:"sine.inOut"}},{t+0.75});')
for i, (lab, x, y) in enumerate(chips):
    w = 340
    b.append(f'<div class="abs chip" id="ch{i}" style="left:{x}px;top:{y}px;width:{w}px">{lab}</div>')
    t = 0.3 + i * 0.22
    j.append(f'tl.fromTo("#ch{i}",{{scale:0.5,opacity:0,x:{-40 if x<500 else 40}}},{{scale:1,opacity:1,x:0,duration:0.45,ease:"back.out(2)"}},{t:.2f});')
    j.append(f'tl.to("#ch{i}",{{scale:0.6,opacity:0,duration:0.3,ease:"power2.in"}},{5.0+i*0.1:.2f});')
css = f""".chip {{ height:84px; border-radius:42px; background:#fff; box-shadow:0 10px 30px rgba(120,20,40,.12); border:2px solid rgba(214,20,31,.18); text-align:center; line-height:86px; font-size:34px; font-weight:600; color:{INK}; }}
.price {{ height:70px; padding:0 30px; border-radius:35px; background:{RED}; color:#fff; font-size:34px; font-weight:600; line-height:72px; white-space:nowrap; }}"""
write("06-network-product", "NetWork product", 6, "radial-gradient(110% 90% at 50% 60%, #ffffff 0%, #fbf0f1 55%, #f2dcdf 100%)", "logo.png", "\n".join("  " + x for x in b), css, "\n".join("  " + x for x in j))
print("ok")
