import json, os, re, html
meta=json.load(open('work/meta.json'))
END=3.2
CFG={
 'kathy':{'tx':'E','ba':['latina','blonde_d30','curly'],'asp':0.8,'hook':("TWO WEEKS.","LEGIT DIFFERENCE."),'hookdur':2.45,
   'hl':{'sculpted','smoother','jawline','neck','exosomes','two','weeks','difference','gorgeous','before','after','love','hard','legit'},
   'end':{'img':'product.png','name':'ShapeShift','sub':'V-Line Jaw Defining Serum'}},
 'kathy65':{'tx':'E','ba':['kathy65L','kathy65L','blonde_d30'],'asp':0.82,'hook':("SHE'S 65.","TWO WEEKS IN."),'hookdur':2.2,
   'hl':{'65','kathy','tighter','exosomes','sculpt','smooth','tighten','two','weeks','legit','difference','gorgeous','sculpted','jawline','month'},
   'end':{'img':'product.png','name':'ShapeShift','sub':'V-Line Jaw Defining Serum'}},
 'tester':{'tx':'R1','hook':("TODAY TESTED IT","FOR 6 WEEKS"),'hookdur':3.75,
   'hl':{'jawline','neck','sickscience','obsessed','40s','six','weeks','incredible','tech','sagging','upward','defined','twice'},
   'end':{'img':'product.png','name':'ShapeShift','sub':'V-Line Jaw Defining Serum'}},
 'best25':{'tx':'PC','hook':("TODAY'S","BEST OF 2025"),'hookdur':2.3,
   'hl':{'sickscience','awards','today','hair','growth','jaw','incredible','months','six','weeks','results','consistency','neck'},
   'end':{'img':'duo.png','name':'ShapeShift + PowerCycle','sub':"TODAY's Best of 2025"}},
}
ASP={'E':638/1040,'R1':518/650,'PC':640/740}
PANEL={'story':(300,1010),'feed':(110,860),'square':(300,1030)}
FMT={
 'story': {'W':1080,'H':1920,'vtop':0,'band':(1040,1260),'cap':84,'hook':92,'logo':None,'overlay':True,
           'end':{'logo':(170,340),'name':(290,128),'sub':(440,48),'url':(512,44),'img':(640,1500)}},
 'feed':  {'W':1080,'H':1350,'vtop':0,'band':(900,1130),'cap':72,'hook':86,'logo':None,'overlay':True,
           'end':{'logo':(70,300),'name':(140,104),'sub':(262,44),'url':(322,40),'img':(420,1270)}},
 'square':{'W':1080,'H':1080,'vtop':0,'band':(40,260),'cap':72,'hook':84,'logo':None,'overlay':True,
           'end':{'logo':(50,280),'name':(110,96),'sub':(222,42),'url':(278,38),'img':(360,1040)}},
}
def words_for(name):
    c=CFG[name]; d=json.load(open(f"assets/tx/{c['tx']}.json"))
    allw=[w for s in d['segments'] for w in s.get('words',[])]
    out=[]
    for sg in meta[name]['segs']:
        for w in allw:
            if sg['a0']-0.02<=w['start']<sg['a1']-0.05:
                out.append([w['word'].strip(), round(sg['t']+w['start']-sg['a0'],3)])
    # text fixes
    txt=' '.join(w for w,_ in out)
    fixed=[]; i=0
    while i<len(out):
        w,t=out[i]; nx=out[i+1][0] if i+1<len(out) else ''
        lw=w.lower().strip('.,!?')
        if lw in ('sick','six') and nx.lower().startswith('science'):
            fixed.append(['SickScience'+nx[len('science'):] ,t]); i+=2; continue
        if lw=='shop' and nx.lower().startswith('today'):
            fixed.append(['Shop',t]); fixed.append(['TODAY'+nx[5:],out[i+1][1]]); i+=2; continue
        fixed.append([w,t]); i+=1
    ded=[]
    for w in fixed:
        if ded and w[0].lower().strip('.,')==ded[-1][0].lower().strip('.,') and w[1]-ded[-1][1]<0.6: continue
        ded.append(w)
    return ded
def chunks(ws, maxw=4, maxc=21):
    ch=[]; cur=[]
    for w,t in ws:
        if cur and (len(cur)>=maxw or len(' '.join(x for x,_ in cur+[[w,t]]))>maxc):
            ch.append(cur); cur=[]
        cur.append([w,t])
        if w[-1:] in '.?!,': ch.append(cur); cur=[]
    if cur: ch.append(cur)
    return ch
for name,c in CFG.items():
    dur=round(meta[name]['dur'],2); total=round(dur+END,2)
    ws=words_for(name); ch=chunks([w for w in ws if w[1]>=c['hookdur']-0.12])
    for fk,f in FMT.items():
        d=f'r/{name}_{fk}'; os.makedirs(d,exist_ok=True)
        if not os.path.exists(d+'/assets'): os.symlink(os.path.abspath('assets'),d+'/assets')
        W,H=f['W'],f['H']; b0,b1=f['band']
        caps=[]; pops=[]; cpops=[]
        for i,cw in enumerate(ch):
            s=max(cw[0][1]-0.05,0); e=ch[i+1][0][1]-0.05 if i+1<len(ch) else min(cw[-1][1]+0.9,dur)
            spans=[]
            for j,(w,t) in enumerate(cw):
                key=re.sub(r"[^a-z0-9']",'',w.lower())
                cls='w hl' if key in c['hl'] or key.rstrip("s") in c['hl'] else 'w'
                spans.append(f'<span class="{cls}" id="c{i}w{j}">{html.escape(w)}</span>'); pops.append([f'#c{i}w{j}',round(t,3)])
            caps.append(f'<section class="clip layer" data-start="{s:.2f}" data-duration="{max(0.2,e-s):.2f}" data-track-index="6"><div class="cap" id="cap{i}">{" ".join(spans)}</div></section>'); cpops.append([f'#cap{i}',round(s,3)])
        E=f['end']; img=c['end']['img']
        logo_html=f'<img id="logo" class="clip" src="assets/logo.png" data-start="0" data-duration="{dur}" data-track-index="7" style="top:{f["logo"][0]}px;width:{f["logo"][1]}px;left:{(W-f["logo"][1])//2}px" />' if f['logo'] else ''
        p0_,p1_=PANEL[fk]; asp=c.get('asp',ASP[c['tx']]); ph=p1_-p0_; pw=int(min((W-100)/2, ph*asp)); ph=int(min(ph, pw/asp)); pt=p0_+((p1_-p0_)-ph)//2; gx=(W-2*pw-24)//2
        cards_html=''.join(f'''<section id="ba{k}" class="clip layer" data-start="{a:.2f}" data-duration="{b-a:.2f}" data-track-index="4"><div id="ba-bg"></div><div class="pn pnb" style="left:{gx}px"><img src="assets/ba_{(c['ba'][k%len(c['ba'])] if 'ba' in c else c['tx'])}_before.png" /><div class="pl b">BEFORE</div></div><div class="pn pna" style="left:{gx+pw+24}px"><img src="assets/ba_{(c['ba'][k%len(c['ba'])] if 'ba' in c else c['tx'])}_after.png" /><div class="pl a">AFTER</div></div></section>''' for k,(a,b) in enumerate(meta[name]['cards']))
        cardanim=''.join(f'tl.from("#ba{k} .pnb", {{ x: -80, opacity: 0, duration: 0.4, ease: "power3.out" }}, {a+0.02:.2f}); tl.from("#ba{k} .pna", {{ x: 80, opacity: 0, duration: 0.4, ease: "power3.out" }}, {a+0.12:.2f}); tl.from("#ba{k} .pl", {{ scale: 0.3, opacity: 0, duration: 0.3, ease: "back.out(2.5)", stagger: 0.12 }}, {a+0.35:.2f}); tl.fromTo("#ba{k} .pn img", {{ scale: 1.0 }}, {{ scale: 1.06, duration: {b-a:.2f}, ease: "none", immediateRender: false }}, {a:.2f});\n' for k,(a,b) in enumerate(meta[name]['cards']))
        namesize=E['name'][1] if len(c['end']['name'])<14 else int(E['name'][1]*0.62)
        doc=f'''<!doctype html>
<html lang="en"><head><meta charset="UTF-8" />
<meta name="viewport" content="width={W}, height={H}" />
<title>SickScience TODAY — {name} {fk}</title>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
@font-face {{ font-family:"FG"; src:url("assets/fonts/FoundersGrotesk-Regular.otf"); font-weight:400; }}
@font-face {{ font-family:"FG"; src:url("assets/fonts/FoundersGrotesk-Medium.otf"); font-weight:500; }}
@font-face {{ font-family:"FG"; src:url("assets/fonts/FoundersGrotesk-Semibold.otf"); font-weight:600; }}
@font-face {{ font-family:"FG"; src:url("assets/fonts/FoundersGrotesk-Bold.otf"); font-weight:700; }}
:root {{ --ink:#141414; --violet:#7300C7; --lilac:#F3ECF9; }}
html,body {{ margin:0; background:#000; }}
#root {{ position:relative; width:{W}px; height:{H}px; overflow:hidden; font-family:"FG",sans-serif; color:var(--ink); }}
.bg {{ position:absolute; inset:0; background:var(--lilac); }}
#vid {{ position:absolute; left:0; top:0; width:{W}px; height:{H}px; object-fit:cover; }}
.layer {{ position:absolute; inset:0; pointer-events:none; }}
#logo {{ position:absolute; height:auto; }}
.cap, .hook {{ position:absolute; left:50px; width:{W-100}px; top:{b0}px; height:{b1-b0}px; display:flex; flex-wrap:wrap; align-content:center; justify-content:center; text-align:center; font-weight:700; line-height:1.04; }}
.cap {{ font-size:{f['cap']}px; }}
.cap .w {{ display:inline-block; margin:0 0.13em; }}
.cap .hl {{ color:var(--violet); }}
.hook {{ font-size:{f['hook']}px; flex-direction:column; flex-wrap:nowrap; align-items:center; justify-content:center; letter-spacing:-0.01em; }}
.hook span {{ display:block; }}
.hook .l2 {{ color:var(--violet); }}
{'''.cap, .hook { color:#fff; text-shadow: 0 0 3px #1d0b2b, 4px 4px 0 #1d0b2b, -4px 4px 0 #1d0b2b, 4px -4px 0 #1d0b2b, -4px -4px 0 #1d0b2b, 0 10px 26px rgba(0,0,0,0.35); }
.cap .hl, .hook .l2 { color:#fff; background:var(--violet); padding:0.02em 0.18em 0.08em; border-radius:0.16em; text-shadow:none; box-shadow:0 7px 0 #1d0b2b; }''' if f['overlay'] else ''}
#endbg {{ position:absolute; inset:0; background: radial-gradient(120% 80% at 50% 70%, #ffffff 0%, #f3ecf9 50%, #e2d2f2 100%); }}
.ct {{ position:absolute; left:0; width:{W}px; text-align:center; }}
#e-name {{ top:{E['name'][0]}px; font-weight:700; font-size:{namesize}px; line-height:1; letter-spacing:-0.01em; }}
#e-sub {{ top:{E['sub'][0]+(0 if namesize==E['name'][1] else -int(E['name'][1]*0.3))}px; font-weight:400; font-size:{E['sub'][1]}px; }}
#e-url {{ top:{E['url'][0]+(0 if namesize==E['name'][1] else -int(E['name'][1]*0.3))}px; font-weight:600; font-size:{E['url'][1]}px; color:var(--violet); }}
#e-img {{ position:absolute; top:{E['img'][0]}px; height:{E['img'][1]-E['img'][0]}px; left:50%; transform:translateX(-50%); }}
#e-logo {{ position:absolute; top:{E['logo'][0]}px; width:{E['logo'][1]}px; left:{(W-E['logo'][1])//2}px; }}
#ba-bg {{ position:absolute; inset:0; background: radial-gradient(120% 90% at 50% 40%, #ffffff 0%, #f3ecf9 55%, #e2d2f2 100%); }}
.pn {{ position:absolute; top:{pt}px; width:{pw}px; height:{ph}px; border-radius:28px; overflow:hidden; box-shadow:0 18px 40px rgba(40,10,70,0.18); }}
.pn img {{ width:100%; height:100%; object-fit:cover; display:block; }}
.pl {{ position:absolute; left:20px; bottom:20px; padding:10px 24px 12px; border-radius:40px; font-weight:700; font-size:34px; letter-spacing:0.04em; }}
.pl.b {{ background:#fff; color:var(--ink); }} .pl.a {{ background:var(--violet); color:#fff; }}
#flash {{ position:absolute; inset:0; background:#fff; opacity:0; }}
</style></head>
<body>
<div id="root" data-composition-id="main" data-width="{W}" data-height="{H}" data-duration="{total}">
  <div class="bg"></div>
  <video id="vid" class="clip" src="assets/{name}_{fk}_v.mp4" data-start="0" data-duration="{dur}" data-media-start="0" data-track-index="1" muted playsinline></video>
  {logo_html}
  {cards_html}
  <section class="clip layer" data-start="0" data-duration="{c['hookdur']}" data-track-index="5"><div class="hook" id="hook"><span class="l1">{html.escape(c['hook'][0])}</span><span class="l2">{html.escape(c['hook'][1])}</span></div></section>
  {chr(10).join('  '+x for x in caps)}
  <section id="s-end" class="clip layer" data-start="{dur}" data-duration="{END}" data-track-index="8">
    <div id="endbg"></div>
    <img id="e-logo" src="assets/logo.png" />
    <div class="ct" id="e-name">{html.escape(c['end']['name'])}</div>
    <div class="ct" id="e-sub">{html.escape(c['end']['sub'])}</div>
    <div class="ct" id="e-url">SickScienceLabs.com</div>
    <img id="e-img" src="assets/{img}" />
  </section>
  <div id="flash" class="clip layer" data-start="0" data-duration="{total}" data-track-index="9"></div>
  <audio id="a-vo" src="assets/{name}_a.wav" data-start="0" data-duration="{dur}" data-track-index="10" data-volume="1"></audio>
  <audio id="a-bgm" src="assets/bgm.mp3" data-start="0" data-duration="{total}" data-media-start="2" data-track-index="11" data-volume="0.07"></audio>
  <audio id="x1" src="assets/sfx/whoosh-cinematic.mp3" data-start="{dur-0.12:.2f}" data-duration="1.6" data-track-index="12" data-volume="0.3"></audio>
</div>
<script>
window.__timelines = window.__timelines || {{}};
const tl = gsap.timeline({{ paused: true }});
tl.from("#hook .l1", {{ scale: 0.4, opacity: 0, duration: 0.3, ease: "back.out(2.5)" }}, 0.02);
tl.from("#hook .l2", {{ scale: 0.4, opacity: 0, duration: 0.3, ease: "back.out(2.5)" }}, 0.3);
{json.dumps(cpops)}.forEach(([s, t]) => tl.from(s, {{ scale: 0.82, opacity: 0, duration: 0.18, ease: "back.out(2.5)" }}, t));
{json.dumps(pops)}.forEach(([s, t]) => tl.fromTo(s, {{ opacity: {0.5 if f['overlay'] else 0.28} }}, {{ opacity: 1, duration: 0.08, ease: "none", immediateRender: true }}, t));
{json.dumps([round(s['t'],2) for s in meta[name]['segs'][1:]])}.forEach(t => tl.fromTo("#vid", {{ scale: 1.05 }}, {{ scale: 1.0, duration: 0.35, ease: "power2.out", immediateRender: false }}, t));
tl.to("#flash", {{ opacity: 0.7, duration: 0.07 }}, {dur-0.05:.2f});
tl.to("#flash", {{ opacity: 0, duration: 0.35 }}, {dur+0.02:.2f});
tl.from("#e-img", {{ y: 70, opacity: 0, duration: 0.7, ease: "power3.out" }}, {dur:.2f});
tl.from("#e-name", {{ y: 30, opacity: 0, duration: 0.5, ease: "power3.out" }}, {dur+0.15:.2f});
tl.from("#e-sub", {{ y: 20, opacity: 0, duration: 0.45, ease: "power3.out" }}, {dur+0.4:.2f});
tl.from("#e-url", {{ y: 20, opacity: 0, duration: 0.45, ease: "power3.out" }}, {dur+0.65:.2f});
tl.to("#a-bgm", {{ volume: 0.25, duration: 0.4 }}, {dur:.2f});
tl.to("#a-bgm", {{ volume: 0.0, duration: 0.8 }}, {total-0.85:.2f});
{cardanim}
window.__timelines["main"] = tl;
</script>
</body></html>'''
        open(d+'/index.html','w').write(doc)
    print(name, dur, len(ch),'chunks', ' / '.join(' '.join(w for w,_ in x) for x in ch[:6]))
