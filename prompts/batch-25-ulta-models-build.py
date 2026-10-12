"""Batch 25 (2026-10-08) — Ulta Holiday, models showing each product's use area (user: 'ürün kullanım alanlarını modellerle göster').
Ulta 'Show, don't tell': real application. Wardrobe solid colour, no black/white (Ulta). Bottles stand on a plinth beside the model (held bottles distort).
ShapeShift = jawline/neck upward strokes · PowerCycle = scalp, dropper on hair part · DropOff = body (upper arm) · NetWork = face/cheekbone."""
import json, importlib.util, sys, io
def load(n, f):
    spec = importlib.util.spec_from_file_location(n, f); m = importlib.util.module_from_spec(spec)
    o = sys.stdout; sys.stdout = io.StringIO(); spec.loader.exec_module(m); sys.stdout = o; return m
b18 = load('b18', 'batch-18-build.py'); b19 = load('b19', 'batch-19-build.py'); b21 = load('b21', 'batch-21-build.py')
PROP, p, TUBE = b18.PROP, b19.p, b19.TUBE
FULL = b21.FULL
GEL = ('a translucent gel-serum — semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, smooth, '
       'slightly viscous, it holds a soft rounded bead and lets light pass through its edges')
HUMAN = ('a strikingly beautiful woman in her late 20s with model-like features and realistic skin texture with visible pores, natural minimal makeup; '
         'LIFESTYLE moment shot with STUDIO-QUALITY production: a beautifully art-directed real-life set (built set, not a plain backdrop), '
         'polished campaign lighting with soft large sources and clean highlights, editorial colour grading; a few holiday touches in hot magenta and orange '
         '(a wrapped gift with a lime ribbon, a small glossy bauble) placed naturally in the scene; candid, unposed feeling; shot on a 35mm lens from the waist up; ')
VERT = ('VERTICAL 9:16 frame. CRITICAL LAYOUT: the UPPER 42% of the frame is calm empty plaster wall for text added later; '
        'the woman stands in the central 55% of the frame width; her face and the product sit in the band between 48% and 75% of the frame height. ')
SQ = ('SQUARE 1:1 frame. CRITICAL LAYOUT: the UPPER 30% of the frame is calm empty plaster wall for text added later; '
      'the woman is in the central 60% of the width; her face and the product sit in the band between 36% and 80% of the frame height. ')
OPEN = lambda name, part: (f"Preserve the exact identity of the product: an open {name} bottle with its {part} exactly as the element shows it. "
                           "Use the element for identity only; do not redraw it. " + PROP)
NEGX = ('black clothing, white clothing, black-and-white outfit, strapless top, bare chest, lingerie, product held in the hand, oversized bottle, '
        'bottle closer to the camera than the woman, opaque white cream, thick white lotion, water-clear liquid, older woman, wrinkles, plastic skin, text, logos')
J = {}
def add(k, el, ident, orient, scene, scale, light, back, finish, neg):
    for fmt, F in (('v', VERT), ('sq', SQ)):
        x = p('A real high-end holiday beauty campaign photograph featuring ', el, ident, orient, F + HUMAN + scene, scale, light, back, finish, neg + ', ' + NEGX)
        x[2] = x[2].replace(b19.FRAME, '').replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\n' + FULL.replace('square', 'vertical' if fmt == 'v' else 'square'), 1)
        J[f'{k}_{fmt}'] = x

add('u25_ss', 'ss-open-shapeshift', OPEN('ShapeShift', 'white pump'),
    'The open bottle stands upright on the white plaster plinth right beside the woman at shoulder height, at the same distance from the camera as she is, front label facing the camera.',
    f'She wears a solid hot-magenta fine-knit sweater with a wide boat neckline. With the fingertips of both hands she sweeps the product, {GEL}, upward along her jawline and the sides of her neck, chin slightly lifted, eyes softly closed; a small glossy translucent sheen of gel is visible on her jawline.',
    'The bottle is 12 cm tall — about two thirds of the length of her hand; the plinth top is at her shoulder height.',
    'Bright soft key light from the front-left, gentle fill, crisp highlights on the chrome and on the gel sheen.', 'Blush-pink plaster studio wall.',
    '35mm at f/4. Skin, knit, plaster, mirror chrome. Fine grain, warm premium holiday colour.', 'hands covering the face, pinching')
add('u25_pc', 'ss-open-powercycle', OPEN('PowerCycle', 'lime-green chrome dropper'),
    'The open bottle stands upright on the white plaster plinth right beside the woman at shoulder height, same distance from the camera as she is, front label facing the camera; she holds only its separate dropper.',
    f'She wears a solid bright-orange ribbed knit top. Her long glossy hair is parted at the crown; with one hand she holds the part open and with the other she holds the slim dropper just above her scalp, releasing a single drop of {GEL} onto the parting; head slightly tilted towards the camera so the parting is visible.',
    'The bottle is 14 cm tall and 4.5 cm wide; the dropper is 8 cm long.',
    'Bright soft key light from above-front so the scalp parting and the drop are clearly lit; crisp chrome highlights.', 'Blush-pink plaster studio wall.',
    '35mm at f/4. Hair, skin, knit, mirror chrome. Fine grain, warm premium holiday colour.', 'gold oil, coloured liquid, bald patches, messy hair')
add('u25_do', 'ss-dropoff', TUBE,
    'The tube stands upright on its cap on the white plaster plinth right beside the woman at hip height, same distance from the camera as she is, front label facing the camera.',
    f'She wears a solid hot-magenta ribbed lounge set: a fitted long-sleeve top with one sleeve pushed up above the elbow and matching wide trousers. With her other hand she smooths a glossy ribbon of {GEL} onto the back of her bare upper arm in a gentle upward motion; relaxed confident pose, looking at her arm.',
    'The tube is about 20 cm tall; the plinth top is at her hip height.',
    'Bright soft key light from the front-right, gentle fill, crisp highlights on the gel.', 'Blush-pink plaster studio wall.',
    '35mm at f/4. Skin, ribbed cotton, plaster, matte tube. Fine grain, warm premium holiday colour.', 'bare torso, swimwear, measuring tape, before-after')
add('u25_nw', 'ss-open-network', OPEN('NetWork', 'white pump'),
    'The open bottle stands upright on the white plaster plinth right beside the woman at shoulder height, same distance from the camera as she is, front label facing the camera.',
    f'She wears a solid blush-pink satin blouse. With her fingertips she presses the product, {GEL} with a very subtle pearly shimmer, onto her cheekbone; her skin has a fresh luminous glow; soft smile, looking just past the camera.',
    'The bottle is 12 cm tall — about two thirds of the length of her hand.',
    'Bright soft beauty key light from the front, gentle fill, luminous skin highlights, crisp chrome highlights.', 'Blush-pink plaster studio wall.',
    '35mm at f/4. Skin, satin, plaster, mirror chrome. Fine grain, warm premium holiday colour.', 'heavy makeup, glitter on face')
json.dump(J, open('batch-25.json', 'w'), ensure_ascii=True)
print(len(J), list(J))
