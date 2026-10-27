"""Local re-render of the Figma Story statics (user's ShapeShift layout, section 1139:1026) for the overview:
same geometry as the reels at rest (no reveal)."""
import sys; sys.path.insert(0, '.')
import reel
from PIL import Image
bg = reel.bg_crop(Image.open('selfie.png').convert('RGB'))
for k, sp in reel.SPEC.items():
    card, circ = reel.build_card(sp)
    reel.compose(bg.convert('RGBA'), 3.0, sp, card, circ).convert('RGB').save(f'out/{k}_story.jpg', quality=92)
print('ok')
