import sys, json, numpy as np
from PIL import Image
k = sys.argv[1]
im = Image.open(f'h_{k}.png').convert('RGB'); m = Image.open(f'm_{k}.png').convert('L').resize(im.size)
rgba = im.copy(); rgba.putalpha(m); bb = m.getbbox(); cut = rgba.crop(bb); cut.save(f'cut_{k}.png')
a = np.asarray(m) > 128; g = np.asarray(im.convert('L')) < 70
ys, xs = np.where(a & g)
i = xs.argmin(); tip = (int(xs[i]), int(ys[i]))
j = (xs - ys).argmax(); end = (int(xs[j]), int(ys[j]))
L = float(np.hypot(end[0] - tip[0], end[1] - tip[1]))
d = {'file': f'cut_{k}.png', 'tip': [tip[0] - bb[0], tip[1] - bb[1]], 'px_per_cm': L / 14.0, 'pen_end': [end[0] - bb[0], end[1] - bb[1]], 'size': cut.size}
json.dump(d, open('hand.json', 'w')); print(d)
