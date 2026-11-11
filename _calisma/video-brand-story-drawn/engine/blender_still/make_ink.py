# final notebook spread ink (white bg) exactly as the film draws it
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../v4')
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/../v4')
import storyboard5 as sb
from PIL import Image, ImageDraw, ImageChops
sb.base = lambda: Image.new('RGB', (sb.SW, sb.SH), (255, 255, 255))
random.seed(11)
final = sb.base(); fd = ImageDraw.Draw(final)
for _, _, fns, _ in sb.BEATS:
    for fn in fns: fn(fd)
final = ImageChops.multiply(final, sb.dish_layer())
final.save(sys.argv[1]); print(sb.SW, sb.SH, sb.PL, sb.PR, sb.PT, sb.PB)
