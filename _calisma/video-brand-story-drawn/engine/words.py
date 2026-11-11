import sys, json, glob, os, mlx_whisper
out={}
for f in sorted(glob.glob('vo/*.mp3')):
    r=mlx_whisper.transcribe(f, path_or_hf_repo='mlx-community/whisper-large-v3-turbo', word_timestamps=True, language='en')
    out[os.path.basename(f)]={'text':r['text'],'words':[{'w':w['word'],'s':round(w['start'],3),'e':round(w['end'],3)} for s in r['segments'] for w in s['words']]}
    print(f, r['text'], flush=True)
json.dump(out,open('words.json','w'),indent=1)
