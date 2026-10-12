"""Batch 18 — countdown concept visuals with sets (2026-10-05). User: "bu cartoonu istemiyorum, daha cool şeyler, setlerden de kullanabiliriz".
One SQUARE 1:1 master per concept; Story/Feed are centre crops of the same image (subjects kept in the central 50% width),
so every format uses the same visual without expansion."""
import json

LAB = ("LABEL TEXT: every word printed on the products is PURE WHITE on the black stripe, on the coloured cap and on the silver half alike; "
       "never black, grey or dark letters. NetWork, if present, is spelled with a capital N and a capital W.")
PROP = ("PROPORTIONS ARE CRITICAL: every capsule bottle is SLIM AND TALL — its height is about 3.4 times its width, the coloured cap is exactly "
        "the upper half and the mirror-silver base the lower half, straight parallel sides and fully rounded ends; never stubby, chubby, squat or wide.")
FIN = ("All product text stays perfectly legible, sharp and accurate. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, "
       "8K detail. No text, no letters, no numbers, no logos added to the scene other than the products' own printed labels.")
INTEG = ("INTEGRATION\nThe products were physically in the scene when this photograph was taken: same light direction, softness and colour temperature "
         "as everything around them; their chrome reflects the real surroundings; real contact shadows and a faint reflection on the surface; same focus "
         "and grain as the rest of the photograph; no outline, no halo.")
NEG = ("black, grey or dark letters on the products, extra products, missing product, redrawn or invented product, fake brand names, misspelled text, "
       "extra text, numbers, digits, clock face, oversized products, stubby or chubby bottles, wide squat capsules, blurred product, CGI, 3D render look, "
       "HDR glow, watermark, pasted-on look, halo, people, hands")
FRAME = ("SQUARE 1:1 frame. CRITICAL LAYOUT: all products and the main props stay inside the CENTRAL 46% of the frame width (the left 27% and right 27% "
         "are only calm continuous background), so the image can later be cropped to a tall vertical format. The upper 38% of the frame is calm, "
         "empty background for text added later; the products sit in the band between 40% and 72% of the frame height; the lower part is calm floor.")

def p(opener, el, items, n, orient, scene, scale, light, back, finish, neg):
    body = f"""Preserve the exact identity of every item in the set: proportions, construction, colours and printed branding exactly as the element shows them. Use the element for identity only; do not redraw any part of it. The set contains {items}. Exactly {n} products, no extra product.

PRODUCT ORIENTATION
{orient} {PROP} Camera at product height, straight on; no fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING
{FRAME} {scene}

SCALE
{scale} Keep real proportions; if in doubt make the products smaller, never bigger.

LIGHT AND SHADOW
{light} Every printed word stays clearly lit and legible.

BACKGROUND
{back}

PHOTOGRAPHIC FINISH
{finish} {FIN}

{INTEG}

{LAB}

Negative: {NEG}, {neg}"""
    return [opener, el, ' \n\n' + body]

out = {
 'cd2_vault': p('A real high-end luxury still-life photograph featuring ', 'ss-set-vault',
    'PowerCycle (lime-green chrome capsule bottle, 14 cm tall), DropOff (glossy cobalt squeeze tube about 20 cm tall, standing on its cap) and ShapeShift (violet chrome capsule bottle, 12 cm tall)', 'three',
    'The three products stand upright side by side, about 3 cm apart, on the polished floor of an open vault, front labels facing the camera.',
    'Behind them a massive round polished-chrome bank-vault door stands half open, its thick circular edge and locking bolts catching the light; from inside the vault a soft lilac glow spills out around the products. The vault door is centred behind the products.',
    'PowerCycle 14 cm, DropOff about 20 cm, ShapeShift 12 cm tall; the vault door is about 90 cm in diameter, so it towers far above the products.',
    'Cool clean key light from the front left, a strong soft lilac-magenta glow from inside the vault behind the products creating crisp rim highlights on the chrome.',
    'A clean white-grey studio set with the round chrome vault door; seamless pale grey-white walls; no other objects.',
    'Medium-format look, 80mm at f/11. Brushed and mirror chrome, glossy floor. Fine grain, crisp premium high-key colour with lilac accents.',
    'dark scene, dollar bills, money, gold bars, safe dial numbers'),
 'cd2_float': p('A real high-end studio product photograph featuring ', 'ss-set-award-duo',
    'ShapeShift (violet chrome capsule bottle, 12 cm tall) and PowerCycle (lime-green chrome capsule bottle, 14 cm tall)', 'two',
    'The two products float in mid-air, upright and perfectly vertical, about 6 cm apart and slightly staggered in height, front labels facing the camera.',
    'They hover about 8 cm above a glossy pale-lilac mirror floor that shows their soft reflections; behind them a few thin horizontal streaks of soft white and lilac light sweep across the backdrop like long-exposure speed trails.',
    'ShapeShift 12 cm and PowerCycle 14 cm tall.',
    'Large soft key light from the upper left, thin strip lights on both sides drawing clean vertical highlights on the chrome, soft glow on the mirror floor.',
    'A seamless backdrop in a smooth gradient from white at the top to pale lilac at the floor; only the soft light streaks behind the products.',
    '100mm at f/11. Mirror chrome, glossy mirror floor, crisp reflections. Fine grain, clean premium colour.',
    'strings, wires, stands holding the products, motion blur on the products'),
 'cd2_neon': p('A real high-end editorial still-life photograph featuring ', 'ss-set-glp1-v2',
    'NetWork (red chrome capsule bottle, 12 cm tall), ShapeShift (violet chrome capsule bottle, 12 cm tall) and a rose-quartz gua sha stone', 'three items: two bottles and the gua sha stone',
    'The two bottles stand upright side by side on a white plaster plinth with the gua sha stone lying flat in front of them, front labels facing the camera.',
    'On the wall behind them hangs a large glowing lilac-magenta neon tube sign shaped like a single lightning bolt (no letters, no words), centred above the products.',
    'Each bottle is 12 cm tall; the gua sha stone is 9 cm long; the plinth is 12 cm tall and 30 cm wide; the neon bolt is about 70 cm tall.',
    'Soft white key light from the front, the neon bolt casting a lilac-magenta glow on the white wall and pink rim highlights on the chrome.',
    'A clean white plaster wall and white plinth, bright and minimal; only the neon lightning bolt.',
    '85mm at f/8. Matte plaster, glossy neon glass tube, mirror chrome, polished stone. Fine grain, bright premium colour with neon accent.',
    'neon letters, neon words, dark room, black wall'),
 'cd2_phone': p('A real high-end flat-lay-style still-life photograph featuring ', 'ss-set-body-duo',
    'DropOff (glossy cobalt squeeze tube about 20 cm tall, standing on its blue screw cap) and ShapeShift (violet chrome capsule bottle, 12 cm tall)', 'two',
    'The two products stand upright side by side on a white glossy acrylic surface, front labels facing the camera.',
    'Just in front of them, lying flat on the surface and angled towards the camera, is a modern smartphone with a completely blank glowing pale-lilac screen (no interface, no icons, no text). Small soft reflections of the products appear on the acrylic.',
    'DropOff about 20 cm tall, ShapeShift 12 cm tall; the smartphone is 15 cm long.',
    'Bright soft key light from the upper left, gentle fill, the phone screen adding a faint lilac glow on the surface.',
    'A seamless soft white-to-pale-lilac gradient backdrop; no other objects.',
    '90mm at f/11. Glossy acrylic, mirror chrome, glass phone screen. Fine grain, clean premium high-key colour.',
    'text on phone screen, app icons, notifications on the phone, hands holding the phone'),
}

# v2: products filled the width -> cluster tighter, smaller, from further back
import copy
TIGHT = ("TIGHT CLUSTER: the products stand touching or almost touching each other as one compact group whose total width is only about 26% of the frame width, "
         "centred horizontally; photographed from further back so the tallest product is only about 24% of the frame height. ")
for k in ['cd2_vault','cd2_neon','cd2_phone']:
    x = copy.deepcopy(out[k]); x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\n' + TIGHT, 1)
    x[2] = x[2].replace('Negative: ', 'Negative: products spread across the frame, products near the left or right edge, ')
    out[k + '_b'] = x
out['cd2_phone_b'][2] = out['cd2_phone_b'][2].replace('Just in front of them, lying flat on the surface and angled towards the camera, is a modern smartphone', 'Just in front of them, lying perfectly flat on the surface, is a small modern smartphone seen in gentle perspective,').replace('The two products stand upright side by side', 'The two products stand perfectly upright and vertical side by side, DropOff on its cap and ShapeShift beside it,')

out['cd2_ring'] = [ 'A real high-end studio product photograph featuring ', 'ss-shapeshift', """ 

Preserve the exact identity of the product: proportions, construction, colours and printed branding exactly as the element shows it. Use the element for identity only; do not redraw any part of it. Capsule bottle with a rounded pill silhouette: top half glossy metallic violet chrome cap, bottom half mirror-polished silver chrome, vertical PURE WHITE printed text on a black stripe. Exactly one product.

PRODUCT ORIENTATION
The product stands upright and perfectly vertical on a small polished-chrome cylindrical podium, front label facing the camera. """ + PROP + """ Camera at product height, straight on; no fisheye.

COMPOSITION AND FRAMING
""" + FRAME + """ The product and podium are centred. Directly behind the product, a large thin glowing ring light (a perfect circle of soft white-lilac light, about three times the product height in diameter) hangs centred on the backdrop, so the product is framed inside the halo of the ring.

SCALE
The product is 12 cm tall and 3.5 cm in diameter; the podium is 6 cm tall and 10 cm wide; the ring light is about 40 cm in diameter. If in doubt make the product smaller, never bigger.

LIGHT AND SHADOW
The ring light creates a crisp circular highlight reflected on the violet chrome cap and soft lilac rim light; gentle frontal fill. Every printed word stays clearly lit and legible.

BACKGROUND
A seamless soft lilac-grey studio backdrop with a matte floor; only the ring light.

PHOTOGRAPHIC FINISH
100mm at f/11. Mirror chrome, polished podium, soft glow. Fine grain, clean premium colour. """ + FIN + "\n\n" + INTEG + "\n\n" + LAB + "\n\nNegative: " + NEG + ", stubby bottle, chubby bottle, ring light stand, cables, extra lights" ]
json.dump(out, open('batch-18.json', 'w'), ensure_ascii=True)
for k, v in out.items(): print(k, v[1], len(v[0] + v[2]))
