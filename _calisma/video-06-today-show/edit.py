import json, subprocess, os
# crop maps: (t0, t1, mode, x, w)  mode 'c' = 1080 crop at x ; 'f' = fit region [x, x+w] to width 1080 with lilac pad
CM = {
 'E': [(0,3.4,'c',420,0),(3.4,8.7,'c',420,0),(8.7,15.6,'c',560,0),(15.6,19.5,'c',380,0),(19.5,28.1,'f',200,1500),
       (28.1,32.6,'c',440,0),(32.6,35.7,'c',420,0),(35.7,39.0,'c',420,0),(39.0,44.6,'c',440,0),(44.6,48.2,'c',460,0),(48.2,58,'c',380,0)],
 'R1':[(0,5.0,'c',280,0),(5.0,14.8,'c',300,0),(14.8,17.2,'c',420,0),(17.2,28.3,'c',330,0),(28.3,30.6,'c',360,0),(30.6,33.2,'c',320,0),(33.2,41,'c',500,0)],
 'PC':[(0,2.2,'c',240,0),(2.2,5.0,'c',560,0),(5.0,10.4,'c',400,0),(10.4,16.8,'c',260,0),(16.8,20.8,'c',340,0),(20.8,24.2,'c',600,0),
       (24.2,40.8,'f',120,1680),(40.8,42.6,'c',200,0),(42.6,44.8,'c',150,0),(44.8,50.2,'c',560,0),(50.2,59,'c',600,0)],
}
EDITS = {
 'kathy': ('E', [(21.76,22.92,21.76),(12.90,21.64,12.90),(34.64,41.20,34.64),(41.40,42.36,24.0),(43.70,44.92,25.2),(55.72,57.18,48.5)]),
 'kathy65':('E', [(24.90,27.88,15.62),(28.98,33.44,19.6),(34.64,41.20,34.64),(41.40,44.92,23.8),(48.40,50.32,20.2),(55.72,57.18,48.5)]),
 'tester':('R1',[(18.28,21.96,18.28),(2.84,7.34,5.2),(8.04,13.66,0.5),(13.72,18.12,13.72),(22.34,26.10,22.34),(26.66,29.12,28.4),(33.32,36.32,33.32)]),
 'best25':('PC',[(0.0,6.14,0.0),(6.32,10.44,16.8),(16.58,22.86,5.0),(32.42,40.30,27.2),(40.84,45.04,42.6)]),
}
PAD=0.06
def run(c): subprocess.run(c, check=True, capture_output=True)
os.makedirs('work/cut', exist_ok=True); os.makedirs('assets', exist_ok=True)
meta={}
for name,(src,segs) in EDITS.items():
    parts=[]; k=0; tl=0.0; segmeta=[]
    for (a0,a1,v0) in segs:
        a0p=max(0,a0-PAD); a1p=a1+PAD; d=a1p-a0p; vs=v0-(a0-a0p)
        segmeta.append({'a0':a0p,'a1':a1p,'t':tl}); tl+=d
        # split video range [vs, vs+d] by crop map
        t=vs; end=vs+d
        for (c0,c1,mode,x,w) in CM[src]:
            if c1<=t or c0>=end: continue
            p0=max(t,c0); p1=min(end,c1)
            if p1-p0<0.02: continue
            out=f'work/cut/{name}_{k:03d}.mp4'; k+=1
            if mode=='c': vf=f'crop=1080:1080:{x}:0,setsar=1,fps=30'
            else:
                h=round(1080*1080/w/2)*2; vf=f'crop={w}:1080:{x}:0,scale=1080:{h},pad=1080:1080:0:(1080-{h})/2:color=0xF3ECF9,setsar=1,fps=30'
            run(['ffmpeg','-y','-ss',f'{p0:.3f}','-i',f'src/{src}.mp4','-t',f'{p1-p0:.3f}','-vf',vf,'-an','-c:v','libx264','-crf','14','-preset','fast','-pix_fmt','yuv420p',out])
            parts.append(out); t=p1
    open('work/cut/list.txt','w').write(''.join(f"file '{os.path.basename(p)}'\n" for p in parts))
    run(['ffmpeg','-y','-f','concat','-safe','0','-i','work/cut/list.txt','-c','copy',f'assets/{name}_v.mp4'])
    # audio: trim each seg with tiny fades, concat, loudnorm
    fl=[]; inputs=[]
    for i,s in enumerate(segmeta):
        d=s['a1']-s['a0']
        fl.append(f"[0:a]atrim={s['a0']:.3f}:{s['a1']:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={d-0.04:.3f}:d=0.04[a{i}]")
    fl.append(''.join(f'[a{i}]' for i in range(len(segmeta)))+f'concat=n={len(segmeta)}:v=0:a=1,loudnorm=I=-14:TP=-1.5:LRA=11[out]')
    run(['ffmpeg','-y','-i',f'src/{src}.mp4','-filter_complex',';'.join(fl),'-map','[out]','-ar','48000','-ac','2',f'assets/{name}_a.wav'])
    meta[name]={'src':src,'segs':segmeta,'dur':tl}
    print(name, round(tl,2), len(parts),'parts')
json.dump(meta,open('work/meta.json','w'),indent=1)
