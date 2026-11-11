# the exact previous scene (real photo plate + finished ink, no prints) at native resolution, plus print positions in its px
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../v4'); os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/../v4')
sys.argv = ['x']
import animatic_real as ar
from PIL import ImageChops
im = ar.compose(ImageChops.multiply(ar.final, ar.sb.dish_layer())).crop(ar.WIDE_BOX)
out = os.path.dirname(os.path.abspath(__file__))
im.save(os.path.join(out, 'plate_ink.png'))
json.dump(dict(size=im.size, OX=ar.OXi, OY=ar.OYi, box=ar.WIDE_BOX), open(os.path.join(out, 'plate_ink.json'), 'w'))
print(im.size, ar.OXi, ar.OYi, ar.WIDE_BOX, ar.CANW, ar.CANH)
