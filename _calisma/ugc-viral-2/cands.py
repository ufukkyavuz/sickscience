import os, re, subprocess, json
R = "/Users/ufo/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/.shortcut-targets-by-id/1yyhSrn9b9nAyKMqtNFz3D81sEOQiloUI/SickScience Brand Assets/All UGC"
USED = ['Thuy Lam Tik Tok','izzysatsuki_1764757846302','izzysatsuki_1764757822980','ShapeShift unedited.mp4','Dr Felica Brown','f4693864-97f8','Dropoffugc-1080x1920','Angela - new','PowerCycle unedited 3','Jenny Ly.MOV']
seen = {}
for dp, dn, fn in os.walk(R):
    for f in fn:
        if not f.lower().endswith(('.mp4','.mov')) or f.startswith('.'): continue
        p = os.path.join(dp, f)
        if any(u in p for u in USED): continue
        sz = os.path.getsize(p)
        seen.setdefault(sz, p)   # dedupe copies by size
for sz, p in sorted(seen.items(), key=lambda x: x[1]): print(sz//10**6, p.replace(R + '/', ''))
