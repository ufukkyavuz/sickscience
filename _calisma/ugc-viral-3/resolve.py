import json, re
from edits import E
def norm(s): return re.sub(r"[^a-z0-9']", '', s.lower())
def toks(p): return [norm(t) for t in p.split() if norm(t)]
def resolve(k):
    ws = json.load(open(f'w/{k}.json')); W = [norm(w[2]) for w in ws]
    def find(ph, start):
        t = toks(ph)
        for i in range(start, len(W)):
            j, m = i, 0
            while m < len(t) and j < len(W):
                if W[j] == '': j += 1; continue
                if W[j] != t[m]: break
                j += 1; m += 1
            if m == len(t): return i, j - 1
        raise ValueError(f'{k}: not found {ph!r} after {start}')
    out = []; pos = 0
    for a, b in E[k]['segs']:
        if isinstance(a, (int, float)): out.append((a, b, 0, 0)); continue
        i0, _ = find(a, 0 if a.lower().startswith(('retinol', 'peptides', 'niacinamide', 'exosomes')) else 0)
        # search start phrase from previous position when duplicates exist
        try: i0, _ = find(a, pos)
        except ValueError: pass
        _, i1 = find(b, i0)
        if out and i0 > out[-1][3]: pass
        s = max(ws[i0][0] - 0.08, ws[i0 - 1][1] if i0 else 0); e = min(ws[i1][1] + 0.12, ws[i1 + 1][0] if i1 + 1 < len(ws) else ws[i1][1] + 0.3)
        if out and i0 > out[-1][3]: s = max(s, out[-1][1])
        out.append((round(s, 2), round(e, 2), i0, i1)); pos = i1 + 1
    return ws, out
if __name__ == '__main__':
    for k in E:
        ws, segs = resolve(k); tot = sum(e - s for s, e, *_ in segs)
        print(k, round(tot, 1), [(s, e) for s, e, *_ in segs])
