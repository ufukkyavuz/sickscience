"""Batch 26 (2026-10-08) — energetic studio model shots, product in hand at face depth (refs: Anua wink/palm, Straand eye-frame).
Replaces batch-25 lifestyle model scenes (user disliked). One 9:16 master per creative; Feed + Square are crops of it.
Bold single-colour Ulta holiday backdrops; solid-colour wardrobe (no black/white)."""
import json, importlib.util, sys, io
def load(n, f):
    spec = importlib.util.spec_from_file_location(n, f); m = importlib.util.module_from_spec(spec)
    o = sys.stdout; sys.stdout = io.StringIO(); spec.loader.exec_module(m); sys.stdout = o; return m
b18 = load('b18', 'batch-18-build.py'); b19 = load('b19', 'batch-19-build.py'); b21 = load('b21', 'batch-21-build.py')
PROP, p, S, TUBE = b18.PROP, b19.p, b19.caps, b19.TUBE
FULL = b21.FULL.replace('square', 'vertical')
GEL = ('a translucent gel-serum — semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, it lets light pass through its edges')
WOMAN = ('a strikingly beautiful woman in her late 20s with model-like features, realistic skin texture with visible pores, fresh glowing skin, natural makeup, '
         'neatly manicured nude nails; high-end beauty campaign shot in a professional photo studio with a seamless single-colour backdrop, big soft key light, '
         'crisp clean highlights, editorial colour; playful, energetic, full of personality; ')
VERT = ('VERTICAL 9:16 frame. CRITICAL LAYOUT: she is framed from the chest up; her face and the product are side by side in the SAME band, between 38% and 72% '
        'of the frame height; the UPPER 32% of the frame is clean empty backdrop for text added later (only the top of her hair may reach into it); '
        'her face is in the central 60% of the width. ')
HAND = ('The bottle is held at the SAME distance from the camera as her face (not pushed towards the lens); it is 12 cm tall — about two thirds of the length of her hand '
        'and about half the height of her face-plus-hair; real proportions. ')
NEGX = ('product pushed towards the camera, oversized bottle, bottle bigger than her face, stubby or chubby bottle, deformed fingers, extra fingers, '
        'black clothing, white clothing, strapless, bare chest, older woman, wrinkles, plastic skin, heavy retouching, text, logos, props')
J = {}
def add(k, el, ident, orient, scene, scale, light, back, finish, neg):
    x = p('A real high-end beauty campaign photograph featuring ', el, ident, orient, VERT + WOMAN + scene, scale, light, back, finish, neg + ', ' + NEGX)
    x[2] = x[2].replace(b19.FRAME, '').replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\n' + FULL, 1)
    J[k] = x

add('u26_ss', 'ss-shapeshift', S('violet'),
    'She holds the closed bottle upright on her open palm just beside her jaw, front label facing the camera, fingers relaxed and natural.',
    'She wears a solid hot-orange fine-knit top. With the fingertips of her other hand she sweeps upward along her jawline, chin lifted, big genuine smile, eyes looking at the camera; a very subtle glossy sheen on her jawline.',
    HAND, 'Bright soft beauty light from the front-left, gentle fill, clean chrome highlights.', 'Seamless saturated hot-magenta studio backdrop with a soft light falloff behind her head.',
    '85mm at f/4. Skin, knit, mirror chrome. Fine grain, punchy premium colour.', 'pinching, hand covering the mouth')
add('u26_pc', 'ss-open-powercycle', "Preserve the exact identity of the product: an open PowerCycle bottle with its lime-green chrome dropper exactly as the element shows it. Use the element for identity only. " + PROP,
    'With one hand she holds the open bottle upright beside her temple, front label facing the camera; with the other hand she holds the slim dropper over the parting of her hair.',
    f'She wears a solid soft-blush ribbed top. Her glossy hair is parted in the middle; the dropper releases a single drop of {GEL} onto the parting; she looks up at the dropper with a playful raised-eyebrow smile.',
    HAND.replace('12 cm', '14 cm'), 'Bright soft top-front beauty light so the parting and the drop are clearly lit; crisp chrome highlights.', 'Seamless bright tangerine-orange studio backdrop.',
    '85mm at f/4. Hair, skin, mirror chrome. Fine grain, punchy premium colour.', 'gold oil, coloured liquid, messy hair')
add('u26_do', 'ss-dropoff', TUBE,
    'She holds the tube upright in one hand at shoulder height beside her face, front label facing the camera.',
    f'She wears a solid hot-magenta sleeveless ribbed top. Her other arm is bent with a glossy ribbon of {GEL} on the back of the upper arm that she smooths in; she laughs with her head slightly tilted, confident and joyful.',
    'The tube is held at the SAME distance from the camera as her face; it is about 20 cm tall — about as tall as her face; real proportions. ',
    'Bright soft beauty light from the front-right, gentle fill.', 'Seamless soft blush-pink studio backdrop.',
    '85mm at f/4. Skin, ribbed cotton, matte tube. Fine grain, punchy premium colour.', 'bare torso, swimwear, measuring tape')
add('u26_nw', 'ss-network', S('red'),
    'She holds the closed bottle upright on her open palm right next to her cheek, front label facing the camera.',
    'She wears a solid pink mesh long-sleeve top. She gives a big playful wink and a wide smile, head slightly tilted towards the bottle; her cheeks have a fresh luminous glow.',
    HAND, 'Bright soft beauty light, luminous skin highlights, crisp chrome highlights.', 'Seamless saturated raspberry-pink studio backdrop with a soft glow behind her.',
    '85mm at f/4. Skin, mesh fabric, mirror chrome. Fine grain, punchy premium colour.', 'closed eyes on both sides')
json.dump(J, open('batch-26.json', 'w'), ensure_ascii=True)
print(len(J), list(J))
