"""Batch 24 (2026-10-08) — more creative Ulta Holiday 2026 concepts (user: 'daha yaratıcı şeyler').
Same rules as batch-23 (Uniquely Ulta magenta/orange palette, textless, white product text, real scale)."""
import json, importlib.util, sys, io
def load(n, f):
    spec = importlib.util.spec_from_file_location(n, f); m = importlib.util.module_from_spec(spec)
    o = sys.stdout; sys.stdout = io.StringIO(); spec.loader.exec_module(m); sys.stdout = o; return m
b19 = load('b19', 'batch-19-build.py'); b21 = load('b21', 'batch-21-build.py')
S, TUBE, p, ident_set = b19.caps, b19.TUBE, b19.p, b21.ident_set
SMALL, FULL = b21.SMALL, b21.FULL
PAL = ('Holiday palette: hot magenta pink, bright orange, soft blush pink, tiny touches of lime green; '
       'bright, joyful, premium retail-holiday campaign styling. ')
VERT = ('VERTICAL 9:16 frame. CRITICAL LAYOUT: the UPPER 42% of the frame is calm, empty background for text added later; '
        'the main subject sits in the band between 46% and 85% of the frame height inside the central 75% of the width. ')
SQ = ('SQUARE 1:1 frame. CRITICAL LAYOUT: the UPPER 32% of the frame is calm, empty background for text added later; '
      'the main subject sits in the band between 36% and 92% of the frame height inside the central 75% of the width. ')
NEGX = 'other brand logos, red-and-green christmas cliches, santa, snowmen, people, hands, numbers, written words'
GLP = ident_set('NetWork (red chrome capsule bottle, 12 cm tall), ShapeShift (violet chrome capsule bottle, 12 cm tall) and a flat SOLID polished stainless-steel gua sha tool (9 cm)','three items: two bottles and the steel gua sha')
J = {}
def add(k, *a, fmt='v', small=True):
    x = p('A real high-end holiday beauty campaign photograph featuring ', *a)
    x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\n' + FULL + PAL, 1)
    x[2] = x[2].replace(b19.FRAME, VERT if fmt == 'v' else SQ)
    if fmt == 'v': x[2] = x[2].replace('entire square frame', 'entire vertical frame')
    x[2] = x[2].replace('Negative: ', 'Negative: borders, letterbox bands, ' + NEGX + ', ')
    J[k + '_' + fmt] = x

SC = [
 ('u24_ornament', 'ss-set-glp1-v2', GLP,
  'The two capsule bottles and the steel gua sha HANG as ornaments on the branches, each from a thin orange satin ribbon loop tied around it, front labels facing the camera.',
  'A small flocked holiday tree with hot-magenta and blush-pink branches, decorated with glossy orange, pink and lime baubles; the two chrome capsule bottles and the steel gua sha hang among the baubles like the shiniest ornaments; seen close, the tree fills the lower-middle of the frame.',
  'Each bottle is 12 cm tall and 3.5 cm wide; the baubles are 7 to 9 cm in diameter, similar in size to the bottles; the gua sha is 9 cm.',
  'Bright soft studio light with warm sparkle highlights on the chrome and baubles.', 'Seamless blush-pink backdrop.',
  '85mm at f/5.6. Flocked branches, glossy glass baubles, mirror chrome, brushed steel. Fine grain, joyful colour.', 'bottles lying down, bottles on the floor, pink gua sha, rose quartz, stone gua sha'),
 ('u24_advent', 'ss-powercycle', S('lime-green'),
  'The product stands upright inside one open compartment of the calendar, front label facing the camera.',
  'A large hot-magenta wooden advent-calendar house with a grid of small closed doors (doors are completely plain, no numbers, no text) and orange trims; one door near the middle is swung open revealing a small lit compartment where the product stands; a few tiny wrapped gifts sit in front of the house.',
  'The product is 14 cm tall and 4.5 cm wide; the open compartment is 18 cm tall; each door is 16 cm square; the calendar house is 70 cm wide.',
  'Bright soft frontal light, a warm glow inside the open compartment, crisp chrome highlights.', 'Seamless pale pink backdrop.',
  '70mm at f/8. Painted wood, mirror chrome. Fine grain, joyful colour.', 'numbers on doors, writing, oversized product'),
 ('u24_fooh', 'ss-shapeshift', S('violet'),
  'A giant sculpture of the bottle stands upright rising out of the bag, front label facing the camera.',
  'FOOH public art installation: on a snowy city plaza at blue hour with warm shop windows and string lights out of focus behind, a GIANT glossy hot-magenta paper holiday shopping bag stands on the ground with orange ribbon handles and the white word "ULTA" printed once on its front, spelled exactly U-L-T-A, perfectly legible; a giant chrome sculpture of the bottle rises out of the bag; light snowfall.',
  'This is a giant public art installation: the bag is 4 metres tall and the bottle sculpture is 3 metres tall, keeping exactly the bottle\'s real proportions (height 3.4 times its width); street lamps 5 metres tall give the scale.',
  'Cool blue-hour ambient light with warm glow from shop windows reflecting on the chrome, soft snow highlights.', 'Out-of-focus snowy city plaza with string lights.',
  '35mm at f/5.6. Glossy paper, mirror chrome, snow. Fine grain, cinematic colour.', 'misspelled bag text, extra words on the bag, crowds, cars'),
 ('u24_burst', 'ss-network', S('red'),
  'The product stands upright inside the open gift box, front label facing the camera.',
  'A hot-magenta gift box on a blush floor bursts open: its lid flies up above it frozen mid-air, a wide orange satin ribbon unfurls in the air, and a burst of magenta, orange and lime confetti and tiny glossy baubles is frozen mid-air around it; the product stands upright inside the open box, revealed.',
  'The product is 12 cm tall; the gift box is 16 cm wide and 10 cm tall; confetti pieces are 1 to 2 cm.',
  'Bright crisp high-speed flash studio light freezing the motion, crisp chrome highlights.', 'Seamless blush-pink backdrop.',
  '85mm at f/8, high-speed freeze-frame. Paper, satin, confetti, mirror chrome. Fine grain, joyful colour.', 'motion blur on the product, product flying, product floating'),
 ('u24_wishlist', 'ss-shapeshift', S('violet'),
  'TOP-DOWN flat lay shot from directly above: the product lies on its side across the lower part of the letter, front label facing up and fully readable.',
  'Overhead flat lay on a blush-pink surface: a cream holiday letter paper with faint ruled lines and NO writing at all lies slightly rotated; a magenta pen, a curl of orange ribbon, two small glossy pink baubles and a sprig of lime ribbon around it; the product lies on the paper.',
  'The product is 12 cm long; the letter paper is 21 by 28 cm; the pen is 14 cm.',
  'Bright soft even overhead light, gentle shadows, crisp chrome highlights.', 'Blush-pink flat surface.',
  'Top-down 50mm at f/8, orthographic feel. Paper, satin, mirror chrome. Fine grain, bright colour.', 'any handwriting, any letters on the paper, perspective tilt'),
 ('u24_wrap', 'ss-dropoff', TUBE,
  'TOP-DOWN flat lay shot from directly above: the tube lies flat on a sheet of wrapping paper, front label facing up and fully readable.',
  'Overhead flat lay of a gift-wrapping table: a large sheet of hot-magenta wrapping paper half folded around the tube, an orange satin ribbon spool, a pair of gold scissors, a roll of clear tape and a stack of orange-and-pink checkerboard paper at the side, on a blush surface; the tube lies on the paper, centred.',
  'The tube is about 20 cm long; the scissors are 20 cm; the ribbon spool is 8 cm wide.',
  'Bright soft even overhead light, gentle shadows.', 'Blush-pink flat surface.',
  'Top-down 50mm at f/8, orthographic feel. Paper, satin, metal, matte tube. Fine grain, bright colour.', 'writing, tags with words, perspective tilt'),
 ('u24_ornament_nw', 'ss-network', S('red'),
  'The product HANGS as an ornament on a branch from a thin orange satin ribbon loop tied around its middle, upright, front label facing the camera.',
  'A small flocked holiday tree with hot-magenta and blush-pink branches decorated with glossy orange, pink and lime baubles; the red chrome capsule bottle hangs among the baubles like the shiniest ornament, near the centre of the tree.',
  'The bottle is 12 cm tall and 3.5 cm wide; the baubles are 7 to 9 cm in diameter, similar in size to the bottle.',
  'Bright soft studio light with warm sparkle highlights on the chrome and baubles.', 'Seamless blush-pink backdrop.',
  '85mm at f/5.6. Flocked branches, glossy glass baubles, mirror chrome. Fine grain, joyful colour.', 'bottle lying down, bottle on the floor, gua sha, extra bottles'),
]
for k, el, *rest in SC:
    add(k, el, *rest, fmt='v'); add(k, el, *rest, fmt='sq')
json.dump(J, open('batch-24.json', 'w'), ensure_ascii=True)
print(len(J), list(J))
