import os, json, subprocess, numpy as np
from faster_whisper import WhisperModel
R = "/Users/ufo/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/.shortcut-targets-by-id/1yyhSrn9b9nAyKMqtNFz3D81sEOQiloUI/SickScience Brand Assets/All UGC"
USED = ['Thuy Lam Tik Tok','izzysatsuki_1764757846302','izzysatsuki_1764757822980','ShapeShift unedited.mp4','Dr Felica Brown','f4693864-97f8','Dropoffugc-1080x1920','Angela - new','PowerCycle unedited 3','Jenny Ly.MOV']
SKIP = ['1080x1080','polen','Eylul','WhatsApp','focusshift','mute.mp4']
seen = {}
for dp, dn, fn in os.walk(R):
    for f in fn:
        p = os.path.join(dp, f)
        if not f.lower().endswith(('.mp4','.mov')) or f.startswith('.') or any(u in p for u in USED+SKIP): continue
        seen.setdefault(os.path.getsize(p), p)
m = WhisperModel('small', device='cpu', compute_type='int8'); idx = {}
for sz, p in sorted(seen.items(), key=lambda x: x[1]):
    key = f'{sz}'; o = f'words/{key}.json'; idx[key] = p.replace(R + '/', '')
    json.dump(idx, open('index.json','w'), indent=0)
    if os.path.exists(o): continue
    try:
        a = subprocess.run(['ffmpeg','-v','error','-i',p,'-ac','1','-ar','16000','-f','s16le','-'], capture_output=True).stdout
        arr = np.frombuffer(a, np.int16).astype(np.float32)/32768
        if len(arr) < 16000: json.dump({'dur':0,'w':[]}, open(o,'w')); continue
        segs,_ = m.transcribe(arr, language='en', word_timestamps=True)
        ws = [[round(w.start,2), round(w.end,2), w.word.strip()] for s in segs for w in s.words]
        json.dump({'dur': round(len(arr)/16000,1), 'w': ws}, open(o,'w')); print(key, idx[key], len(ws), flush=True)
    except Exception as e: print('ERR', p, e, flush=True)
print('DONE')
