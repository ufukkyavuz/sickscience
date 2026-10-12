import json, subprocess, os
# shot maps: (t0,t1,cx)  cx=None -> B/A card range
SM = {
 'E': [(0,3.4,560),(3.4,8.7,1250),(8.7,15.6,1350),(15.6,19.5,560),(19.5,28.1,None),(28.1,32.6,560),(32.6,35.7,760),(35.7,39.0,1250),(39.0,44.6,560),(44.6,48.2,840),(48.2,58,600)],
 'R1':[(0,5.0,850),(5.0,14.8,1100),(14.8,17.2,1060),(17.2,28.3,None),(28.3,30.6,960),(30.6,33.2,1000),(33.2,41,980)],
 'PC':[(0,2.2,980),(2.2,5.0,1300),(5.0,10.4,1000),(10.4,16.8,1100),(16.8,20.8,1100),(20.8,24.2,940),(24.2,40.8,None),(40.8,42.6,1100),(42.6,44.8,700),(44.8,50.2,1300),(50.2,59,1000)],
}
EDITS = {
 'kathy': ('E', [(21.76,22.92,21.76),(12.90,21.64,12.90),(34.64,41.20,34.64),(41.40,42.36,24.0),(43.70,44.92,25.2),(55.72,57.18,48.5)]),
 'kathy65':('E', [(24.90,27.88,15.62),(28.98,33.44,19.6),(34.64,41.20,34.64),(41.40,44.92,23.8),(48.40,50.32,20.2),(55.72,57.18,48.5)]),
 'tester':('R1',[(18.28,21.96,18.28),(2.84,7.34,5.2),(8.04,13.66,0.5),(13.72,18.12,13.72),(22.34,26.10,22.34),(26.66,29.12,28.4),(33.32,36.32,33.32)]),
 'best25':('PC',[(0.0,6.14,0.0),(6.32,10.44,16.8),(16.58,22.86,5.0),(32.42,40.30,27.2),(40.84,45.04,42.6)]),
}
FMTS={'story':(608,1080,1080,1920),'feed':(864,1080,1080,1350),'square':(1080,1080,1080,1080)}
PAD=0.06
def run(c): subprocess.run(c, check=True, capture_output=True)
os.makedirs('work/cut2', exist_ok=True)
meta=json.load(open('work/meta.json'))
for name,(src,segs) in EDITS.items():
    cards=[]
    for fk,(cw,ch,ow,oh) in FMTS.items():
        parts=[]; k=0; tl=0.0
        for (a0,a1,v0) in segs:
            a0p=max(0,a0-PAD); a1p=a1+PAD; d=a1p-a0p; vs=v0-(a0-a0p); t=vs; end=vs+d
            for (c0,c1,cx) in SM[src]:
                if c1<=t or c0>=end: continue
                p0=max(t,c0); p1=min(end,c1)
                if p1-p0<0.02: continue
                if cx is None:
                    if fk=='story': cards.append([round(tl+(p0-vs),3),round(tl+(p1-vs),3)])
                    cx=960
                x0=int(min(max(cx-cw/2,0),1920-cw))
                out=f'work/cut2/{name}_{fk}_{k:03d}.mp4'; k+=1
                vf=f'crop={cw}:{ch}:{x0}:0,scale={ow}:{oh}:flags=lanczos,unsharp=5:5:0.6,setsar=1,fps=30' if cw!=1080 else f'crop=1080:1080:{x0}:0,setsar=1,fps=30'
                run(['ffmpeg','-y','-ss',f'{p0:.3f}','-i',f'src/{src}.mp4','-t',f'{p1-p0:.3f}','-vf',vf,'-an','-c:v','libx264','-crf','14','-preset','fast','-pix_fmt','yuv420p',out])
                parts.append(out); t=p1
            tl+=d
        open('work/cut2/list.txt','w').write(''.join(f"file '{os.path.basename(p)}'\n" for p in parts))
        run(['ffmpeg','-y','-f','concat','-safe','0','-i','work/cut2/list.txt','-c','copy',f'assets/{name}_{fk}_v.mp4'])
    # merge adjacent card intervals
    cards.sort(); m=[]
    for c in cards:
        if False: pass
        else: m.append(c)
    meta[name]['cards']=m; print(name, m)
json.dump(meta,open('work/meta.json','w'),indent=1)
