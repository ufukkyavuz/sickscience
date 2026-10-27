"""Batch 56 — Amazon Store v2: white background, clear lab-glass science theme (user 2026-10-20: "daha cam bilim ve beyaz arkaplan").
1:1 tiles (product right, left 45% clean white for text) + 21:9 hero (products right-centre, left-centre empty). Text added in Figma."""
CAP = {
 'shapeshift': ('ShapeShift', 'violet', 12, 3.5, 'a small petri dish holding one soft bead of the gel-serum and a few thin slices of fresh pineapple on a glass dish'),
 'network':    ('NetWork', 'red', 12, 3.5, 'a small petri dish holding one soft bead of the gel-serum with a very subtle pearly shimmer, and two thin slices of cucumber and one sliced radish on a glass dish'),
 'powercycle': ('PowerCycle', 'green', 14, 4.5, 'a glass pipette resting on a petri dish with a single drop of the gel-serum, and one small sprig of fresh rosemary'),
}
TEX = ("a translucent gel-serum — semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, smooth, "
       "slightly viscous, it holds a soft rounded bead and lets light pass through its edges")
COMMON_FINISH = """LIGHT AND SHADOW

Bright, soft, high-key studio daylight from the upper left through a large diffuser, crisp clean caustics from the glassware falling on the white surface, never across any printed word. Every printed word on the product sits in clear light and is fully legible. White bounce fill; no dark areas.

BACKGROUND

Pure seamless bright white laboratory backdrop fading softly to white, nothing else — no windows, no shelves, no people, no coloured walls, no plants.

PHOTOGRAPHIC FINISH

100mm lens at f/8. Thin clear borosilicate laboratory glass with crisp edges and real refraction, white glossy lab surface, mirror chrome and metallic colour on the capsule. Subtle optical depth, fine photographic grain, clean neutral colour, bright airy high-key premium science look. All product text must be perfectly legible, sharp, and accurate — no blurry or distorted letters. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail.

INTEGRATION

The product is photographed in this scene, not composited: same light direction, softness and colour temperature as the glassware; its chrome reflects the real white room and the nearby glass; a real soft contact shadow and a faint reflection on the glossy surface; same sharpness, grain and noise as the rest of the photo; no outline, no halo.

No text, no letters, no logos added to the scene — only the product's own printed label."""
NEG = ("Negative: stubby, chubby, squat or wide bottle, oversized product, product closer to the camera than the glassware, extra products, redrawn or invented products, "
       "black letters, dark or grey text on the product, misspelled label, fake brand names, opaque white cream, thick white lotion, whipped or peaked cream, body butter, "
       "water-clear liquid, fully transparent gel, coloured or gold serum, coloured liquids in the glassware, dark or grey scene, coloured background, orange or yellow colour cast, "
       "pasted or composited look, cut-out edges, sticker look, halo, product lit differently, floating product, CGI, 3D render, plastic textures, HDR glow, extra text, watermark, frame, border")

def capsule(key):
    name, col, h, d, props = CAP[key]
    ratio = '3.4' if h == 12 else '3.1'
    return f"""A real premium laboratory still-life photograph featuring the element reference.

Match the element reference exactly: proportions, construction, colours and printed branding. Use the element for identity only; do not redraw any part of it. PROPORTIONS ARE CRITICAL: slim and tall capsule, height {ratio}× its width, the {col} metallic chrome cap is exactly the upper half and the mirror-polished silver chrome is the lower half, rounded pill ends; never stubby, chubby or squat. Every word printed on the product is pure white on the black stripe — on the coloured cap AND on the silver half; never black, grey or dark text. {'The label reads exactly NetWork with a capital N and a capital W. ' if key=='network' else ''}Exactly one product, no extra product.

PRODUCT ORIENTATION

The closed capsule stands upright on its rounded base, front label facing the camera, the vertical text reading bottom to top. Camera at product height, straight on, almost orthographic. No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING

Square frame. A clean white glossy laboratory bench. The capsule stands in the RIGHT half of the frame, its centre about 64% from the left and slightly below the middle, at the same distance from the camera as the glassware. Around and behind it on the right: two or three thin clear empty laboratory glass pieces — a tall beaker, a small conical flask — and {props}; the serum in the dish is {TEX}. Keep the LEFT 45% of the frame as calm, empty, clean white surface and white backdrop for text to be added later. Every object fits completely inside the frame.

SCALE

The capsule is {h} cm tall and {d} cm wide. The beaker is about 14 cm tall, the flask about 12 cm, the petri dish 9 cm across. Keep these real proportions; if in doubt make the product smaller, never bigger. The product fills no more than about 38% of the frame height.

{COMMON_FINISH}

{NEG}"""

DROPOFF = f"""A real premium laboratory still-life photograph featuring the element reference.

Match the element reference exactly: matte cobalt-blue squeeze tube standing on its blue screw cap, white vertical printed text, proportions, construction and colours. Use the element for identity only; do not redraw any part of it. Every word printed on the tube is pure white; never black, grey or dark text. Exactly one product, no extra product.

PRODUCT ORIENTATION

The tube stands upright on its cap, the crimped end at the top, front label facing the camera, the vertical text reading bottom to top. Camera at product height, straight on, almost orthographic. No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING

Square frame. A clean white glossy laboratory bench. The tube stands in the RIGHT half of the frame, its centre about 64% from the left, at the same distance from the camera as the glassware. Around and behind it on the right: two or three thin clear empty laboratory glass pieces — a tall graduated cylinder, a beaker — and a wide glass petri dish holding one soft swirl of {TEX}. Keep the LEFT 45% of the frame as calm, empty, clean white surface and white backdrop for text to be added later. Every object fits completely inside the frame.

SCALE

The tube is about 20 cm tall and 5 cm wide. The graduated cylinder is about 24 cm tall, the beaker about 12 cm, the petri dish 10 cm across. Keep these real proportions; if in doubt make the product smaller, never bigger. The product fills no more than about 50% of the frame height.

{COMMON_FINISH}

{NEG}"""

HERO = f"""A real premium laboratory still-life photograph featuring the four element references: NetWork capsule, ShapeShift capsule, PowerCycle capsule and DropOff tube.

Match every element reference exactly: proportions, construction, colours and printed branding. Use the elements for identity only; do not redraw any part of them. The capsules are slim and tall pills — ShapeShift and NetWork height 3.4× width, PowerCycle a little larger — the coloured metallic chrome cap is exactly the upper half, the lower half mirror-polished silver chrome; never stubby or squat. DropOff is a matte cobalt-blue squeeze tube standing on its blue cap. Every word printed on the products is pure white; never black, grey or dark text. The red capsule label reads exactly NetWork with a capital N and a capital W. Exactly four products, no extra product.

PRODUCT ORIENTATION

All four stand upright in one loose row, labels facing the camera, vertical text reading bottom to top: NetWork, ShapeShift, PowerCycle, DropOff from left to right, small gaps between them. Camera at product height, straight on, almost orthographic. No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING

Very wide panoramic frame for a website banner. A clean white glossy laboratory bench across the whole width. The product row sits in the RIGHT-CENTRE, spanning roughly 56% to 82% of the frame width, vertically centred. Clear empty laboratory glassware — beakers, conical flasks, a graduated cylinder, petri dishes with small beads of {TEX} — stands among and behind the products and continues thinly to the far right edge. The LEFT-CENTRE of the frame, from 14% to 52% of the width, stays calm, empty, clean white for a headline to be added later; a few soft out-of-focus glass shapes may sit at the far left edge. Everything sits in the middle 60% of the frame height; top and bottom stay plain white. Every object fits completely inside the frame.

SCALE

ShapeShift and NetWork capsules are 12 cm tall, PowerCycle 14 cm, DropOff about 20 cm. Beakers about 14 cm, flasks 12–18 cm, graduated cylinder 24 cm. Keep these real proportions; if in doubt make the products smaller, never bigger.

{COMMON_FINISH}

{NEG}"""

PROMPTS = {'tile_shapeshift': ('@ss-shapeshift', '1:1', capsule('shapeshift')), 'tile_network': ('@ss-network', '1:1', capsule('network')),
           'tile_powercycle': ('@ss-powercycle', '1:1', capsule('powercycle')), 'tile_dropoff': ('@ss-dropoff', '1:1', DROPOFF),
           'hero': ('@ss-network @ss-shapeshift @ss-powercycle @ss-dropoff', '21:9', HERO)}
if __name__ == '__main__':
    import json; json.dump(PROMPTS, open('prompts/batch-56.json', 'w'), indent=1); print({k: len(v[2]) for k, v in PROMPTS.items()})
