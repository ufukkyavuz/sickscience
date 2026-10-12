import mlx_whisper, json, sys
files = sys.argv[1:]
for f in files:
    r = mlx_whisper.transcribe(f, path_or_hf_repo="mlx-community/whisper-large-v3-turbo", word_timestamps=True, language="en")
    name = f.replace('/','_').replace('.mp4','')
    json.dump(r, open(f'_tx/{name}.json','w'))
    with open(f'_tx/{name}.txt','w') as o:
        for s in r['segments']: o.write(f"[{s['start']:6.2f}-{s['end']:6.2f}] {s['text'].strip()}\n")
    print('done', f)
