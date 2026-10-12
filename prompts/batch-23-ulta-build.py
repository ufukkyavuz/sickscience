"""Batch 23 (2026-10-08) — Ulta Beauty Holiday 2026 ('the magic starts with you').
Source: Ulta/FY26-Holiday-BrandSocialContentGuidelines.pdf + Ulta/Uniquely-Ulta-Brand-Partner-Playbook-Q3-2026.pdf.
Uniquely Ulta cues: holiday hot-pink (magenta #E90B5A) bag, orange #E35200, gifts with orange/pink/lime ribbons, bright soft light, clean backgrounds.
All 4 SKUs are 'Only at Ulta' (SS $64, NW $74, PC $64, DO $52). No sets at Ulta -> single-product scenes only."""
import json, importlib.util, sys, io
def load(n, f):
    spec = importlib.util.spec_from_file_location(n, f); m = importlib.util.module_from_spec(spec)
    o = sys.stdout; sys.stdout = io.StringIO(); spec.loader.exec_module(m); sys.stdout = o; return m
b19 = load('b19', 'batch-19-build.py'); b21 = load('b21', 'batch-21-build.py')
S, TUBE, p = b19.caps, b19.TUBE, b19.p
SMALL, FULL = b21.SMALL, b21.FULL
J = {}
VERT = ('VERTICAL 9:16 frame. CRITICAL LAYOUT: the UPPER 45% of the frame is calm, completely empty seamless background for text added later (no props, no ribbons, no bag handles, no tissue reaching into it); '
        'the product and all props sit in the band between 50% and 80% of the frame height and inside the central 70% of the width; the bottom 20% is calm floor. '
        'SIZE IS CRITICAL: photographed from further back; the product is SMALL — only about 14% of the frame height. ')
PAL = ('Holiday palette: hot magenta pink, bright orange, soft blush pink, with tiny touches of lime green; '
       'clean, bright, joyful, premium retail-holiday campaign styling. ')
BAG = ('a glossy hot-magenta-pink paper holiday shopping bag with orange ribbon handles and the white word "ULTA" printed once on its front in a clean wordmark, '
       'spelled exactly U-L-T-A, perfectly legible')
NEGX = 'misspelled bag text, extra letters on the bag, other brand logos, red-and-green christmas cliches, snowmen, santa, people, hands'
def add(k, *a):
    x = p('A real high-end holiday beauty campaign photograph featuring ', *a)
    x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\n' + FULL + SMALL + PAL, 1)
    x[2] = x[2].replace('Negative: ', 'Negative: borders, letterbox bands, giant product filling the frame, ' + NEGX + ', ')
    x[2] = x[2].replace(b19.FRAME, VERT).replace(SMALL, '').replace('entire square frame', 'entire vertical frame')
    J[k] = x

add('u23_bag', 'ss-shapeshift', S('violet'),
    'The product stands upright just in front of the bag on the floor of the set, front label facing the camera.',
    f'{BAG} stands open on a blush-pink floor, a puff of magenta tissue paper rising from it; a few small wrapped gifts in orange and pink paper with lime ribbons sit around it; the product stands in front of the bag, centred.',
    'The product is 12 cm tall; the bag is 32 cm tall and 25 cm wide, clearly much bigger than the product.',
    'Bright soft frontal studio light, gentle shadows, crisp chrome highlights.', 'Seamless blush-pink studio backdrop with a soft gradient.',
    '85mm at f/8. Glossy paper, tissue, mirror chrome. Fine grain, joyful saturated colour.', 'product inside the bag, text other than ULTA')
add('u23_selfgift', 'ss-shapeshift', S('violet'),
    'The product stands upright on top of a small square gift box, front label facing the camera.',
    'A small hot-magenta gift box wrapped with a wide orange satin ribbon and bow; a blank blush-pink paper gift tag hangs from the ribbon on a thin string (the tag is completely blank); a few loose ribbon curls on the table; the product centred on top of the box.',
    'The product is 12 cm tall; the gift box is 12 cm wide and 8 cm tall.',
    'Bright soft key light from the upper left, soft shadows, crisp chrome highlights.', 'Seamless soft pink backdrop, clean and bright.',
    '85mm at f/8. Satin ribbon, paper, mirror chrome. Fine grain, bright playful colour.', 'writing on the tag, text on the box')
add('u23_stocking', 'ss-powercycle', S('lime-green'),
    'The product stands upright on a white mantel shelf right next to a hanging stocking, front label facing the camera.',
    'A chunky hot-magenta knit holiday stocking with an orange cuff hangs from a white mantel; a garland of small orange and pink baubles runs along the mantel; the product stands on the mantel next to the stocking, centred.',
    'The product is 14 cm tall and 4.5 cm in diameter; the stocking is 45 cm long.',
    'Warm soft interior light with a gentle glow, crisp chrome highlights.', 'Out-of-focus soft white wall with warm fairy-light bokeh.',
    '50mm at f/4. Knit wool, ceramic baubles, mirror chrome. Fine grain, cosy bright colour.', 'fireplace flames, text, pine tree cliches')
add('u23_cake', 'ss-network', S('red'),
    'The product stands upright on the top tier of a two-tier cake stand, front label facing the camera.',
    'A glossy hot-pink ceramic two-tier cake stand on a blush table; the lower tier holds small pink and orange macarons and a few shiny pink and orange baubles; the product stands on the top tier, centred; festive holiday treat table.',
    'The product is 12 cm tall; the cake stand is 30 cm wide.',
    'Bright soft party light, gentle shadows, crisp chrome highlights.', 'Seamless blush-pink backdrop with soft gradient.',
    '85mm at f/8. Glazed ceramic, sugar, mirror chrome. Fine grain, joyful pastel and magenta colour.', 'candles, text, numbers, cake slices')
add('u23_lab', 'ss-network', S('red'),
    'The product stands upright on a white laboratory bench among glassware, front label facing the camera.',
    'Clear glass lab beakers and an Erlenmeyer flask on a bright white lab bench are filled with small shiny hot-pink and orange holiday baubles instead of liquid; a glass test-tube rack holds thin rolls of pink and orange ribbon; science meets holiday; the product centred.',
    'The product is 12 cm tall; the beakers are 15 cm tall.',
    'Bright clean daylight lab light, soft shadows, crisp chrome and glass highlights.', 'Out-of-focus bright white laboratory.',
    '70mm at f/5.6. Borosilicate glass, glossy baubles, mirror chrome. Fine grain, clean bright colour.', 'liquids, text, labels on glassware, people')
add('u23_gifts', 'ss-dropoff', TUBE,
    'The tube stands upright on its cap on the floor in front of a pile of wrapped gifts, front label facing the camera.',
    'A tall playful pile of wrapped gift boxes in hot magenta, orange, blush pink and orange-and-pink checkerboard paper with lime-green and orange ribbons, on a little drift of white artificial snow; the tube stands in front of the pile, centred.',
    'The tube is about 20 cm tall; the gift boxes are 15 to 40 cm wide.',
    'Bright soft studio light, gentle shadows, crisp highlights.', 'Seamless hot-pink studio backdrop.',
    '50mm at f/8. Wrapping paper, satin ribbon, matte tube. Fine grain, saturated joyful colour.', 'text on gifts, tags with writing')

for k in list(J): J[k+'_v']=J.pop(k)
json.dump(J, open('batch-23.json', 'w'), ensure_ascii=True)
print(len(J), list(J))
