import json, subprocess, numpy as np, os, sys
from faster_whisper import WhisperModel
m = WhisperModel('small', device='cpu', compute_type='int8')
for p in sys.argv[1:]:
    o = 'words/' + os.path.splitext(os.path.basename(p))[0] + '.json'
    if os.path.exists(o): continue
    a = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-map', '0:a:0', '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True).stdout
    arr = np.frombuffer(a, np.int16).astype(np.float32) / 32768
    segs, info = m.transcribe(arr, word_timestamps=True)
    ws = [[round(w.start, 2), round(w.end, 2), w.word.strip()] for s in segs for w in s.words]
    json.dump(ws, open(o, 'w')); print(os.path.basename(p), info.language, len(ws), ' '.join(w[2] for w in ws)[:700], flush=True)
