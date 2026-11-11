import json,sys
for k in sys.argv[1:]:
    d=json.load(open(f'words/{k}.json'))['w']; out=[]; 
    for i,w in enumerate(d):
        if i%8==0: out.append(f'\n[{w[0]}] ')
        out.append(w[2]+' ')
    print('=====',k,''.join(out))
