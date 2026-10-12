"""Batch 19 — award creatives (2026-10-05). Awards from sicksciencelabs.com/pages/home-v2 (data-awards).
Square 1:1 masters, subject in the central ~46% width so Story/Feed are centre crops of the same image."""
import json, importlib.util, sys, io
spec = importlib.util.spec_from_file_location('b18', 'batch-18-build.py'); b18 = importlib.util.module_from_spec(spec)
_o = sys.stdout; sys.stdout = io.StringIO(); spec.loader.exec_module(b18); sys.stdout = _o
LAB, PROP, FIN, INTEG, NEG, FRAME = b18.LAB, b18.PROP, b18.FIN, b18.INTEG, b18.NEG, b18.FRAME

def caps(color):
    return ("Preserve the exact identity of the product: proportions, construction, colours and printed branding exactly as the element shows it. "
            "Use the element for identity only; do not redraw any part of it. Capsule bottle with a rounded pill silhouette: top half glossy metallic "
            f"{color} chrome cap, bottom half mirror-polished silver chrome, vertical PURE WHITE printed text on a black stripe. Exactly one product. " + PROP)
TUBE = ("Preserve the exact identity of the product: proportions, construction, colours and printed branding exactly as the element shows it. "
        "Use the element for identity only; do not redraw any part of it. A matte cobalt-blue squeeze tube about 20 cm tall standing upright on its blue screw cap, "
        "vertical white printed text exactly as the element shows it. Exactly one product; slim tube, never oversized.")

def p(opener, el, ident, orient, scene, scale, light, back, finish, neg):
    body = f"""{ident}

PRODUCT ORIENTATION
{orient} Camera at product height, straight on; no fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING
{FRAME} {scene}

SCALE
{scale} Keep real proportions; if in doubt make the product smaller, never bigger.

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
 'aw_carpet': p('A real high-end celebrity-event style product photograph featuring ', 'ss-shapeshift', caps('violet'),
    'The product stands upright and perfectly vertical in the middle of a red carpet, front label facing the camera, like a star arriving at a premiere.',
    'A strip of plush red carpet runs from the foreground into the distance; on both sides two short polished-chrome stanchions with violet velvet ropes frame the product; in the soft-focus background bright white camera flash bursts and soft bokeh sparkle like paparazzi. The product stands centred.',
    'The product is 12 cm tall and 3.5 cm in diameter; the stanchions are 20 cm tall, scaled as a miniature set around the product.',
    'Bright frontal key light like a camera flash, crisp highlights on the violet chrome, warm glow from behind.',
    'Soft out-of-focus event backdrop in pale lilac and white with flash bursts; no people, no logos, no text.',
    '85mm at f/5.6 so the product is sharp and the background melts into bokeh. Velvet carpet texture, polished chrome. Glamorous premium colour.',
    'people, photographers, cameras visible, step-and-repeat wall, logos, text on backdrop'),
 'aw_podium': p('A real high-end studio product photograph featuring ', 'ss-powercycle', caps('lime-green'),
    'The product stands upright and perfectly vertical on the top step of a winners podium, front label facing the camera.',
    'A clean three-step winners podium in glossy white with the highest step in the centre (blank faces, no numbers); the product stands on the centre step. Fine silver and pale-green metallic confetti floats in the air and a few pieces rest on the podium.',
    'The product is 14 cm tall and 4.5 cm in diameter; the centre podium step is 10 cm tall and 14 cm wide.',
    'Bright soft key light from above, a spotlight cone on the winner, crisp highlights on the chrome and sparkle on the confetti.',
    'A seamless soft pale-grey to white studio backdrop; only the podium and confetti.',
    '85mm at f/8. Glossy podium, mirror chrome, metallic confetti. Fine grain, crisp premium colour.',
    'numbers on the podium, medals, trophies, text, gold colour cast'),
 'aw_mags': p('A real high-end editorial still-life photograph featuring ', 'ss-dropoff', TUBE,
    'The tube stands upright on its cap on top of a neat stack of glossy magazines, front label facing the camera.',
    'A tidy stack of six thick glossy fashion magazines lies on a white surface, spines facing the camera with plain coloured spines (cobalt, white, pale pink, lilac) and absolutely no printed titles; the product stands on top of the stack, centred. A soft shadow falls to the right.',
    'The tube is about 20 cm tall; each magazine is 1 cm thick and 28 cm wide; the stack is about 7 cm high.',
    'Bright soft window light from the upper left, gentle shadows, glossy highlights on the magazine edges.',
    'A clean white wall and white tabletop, airy and minimal; no other objects.',
    '70mm at f/8. Glossy paper edges, matte tube. Fine grain, airy high-key editorial colour.',
    'magazine titles, cover text, readable covers, letters on the spines, cobalt colour cast'),
 'aw_museum': p('A real high-end gallery still-life photograph featuring ', 'ss-network', caps('red'),
    'The product stands upright and perfectly vertical inside a clear glass museum display case, front label facing the camera.',
    'A white gallery plinth topped with a clean rectangular glass vitrine, centred; inside the vitrine the product stands alone like a precious exhibit, with a small blank white placard on a stand in front of it (no text).',
    'The product is 12 cm tall and 3.5 cm in diameter; the vitrine is 30 cm tall and 22 cm wide.',
    'A single soft museum spotlight from above lighting the product, faint reflections on the glass, gentle falloff into the room.',
    'A calm white gallery wall and pale stone floor; no other artworks, no people.',
    '85mm at f/8. Clear glass with true reflections, matte plinth, mirror chrome. Fine grain, quiet premium gallery colour.',
    'text on the placard, labels, ropes, people, artworks'),
 'aw_confetti': p('A real high-end celebration still-life photograph featuring ', 'ss-set-vault',
    'Preserve the exact identity of every item in the set: proportions, construction, colours and printed branding exactly as the element shows them. Use the element for identity only; do not redraw any part of it. The set contains PowerCycle (lime-green chrome capsule bottle, 14 cm tall), DropOff (matte cobalt squeeze tube about 20 cm tall, standing on its cap) and ShapeShift (violet chrome capsule bottle, 12 cm tall). Exactly three products, no extra product. ' + PROP,
    'The three products stand upright side by side, touching, on a round white pedestal, front labels facing the camera.',
    'TIGHT CLUSTER: the group is only about 26% of the frame width, centred. Fine iridescent silver and lilac confetti and a few thin metallic streamers fall around them in mid-air.',
    'PowerCycle 14 cm, DropOff about 20 cm (the tallest, about 1.6 times ShapeShift), ShapeShift 12 cm tall; the pedestal is 8 cm tall and 30 cm wide.',
    'Bright celebratory key light from the front, a soft lilac backlight making the confetti sparkle, crisp chrome highlights.',
    'A seamless soft white-to-lilac backdrop; only the pedestal and confetti.',
    '85mm at f/8, confetti crisp. Mirror chrome, matte tube, metallic foil confetti. Fine grain, joyful premium colour.',
    'balloons, champagne, trophies, text, numbers'),
}

import copy
x = copy.deepcopy(out['aw_carpet'])
x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\nSIZE IS CRITICAL: photographed from far back; the product is SMALL in the frame — only about 22% of the frame height — and clearly SHORTER than the chrome stanchions, which are about twice its height. ', 1)
x[2] = x[2].replace('Negative: ', 'Negative: product taller than the stanchions, giant product filling the frame, ')
out['aw_carpet2'] = x
json.dump(out, open('batch-19.json', 'w'), ensure_ascii=True)
for k, v in out.items(): print(k, v[1], len(v[0] + v[2]))
