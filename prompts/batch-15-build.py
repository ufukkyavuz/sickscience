"""Batch 15 — NetWork × BCRF: X-ray self-check + top-down 'pair' with ring light (2026-10-04). Writes batch-15.json."""
import json

LAB = ("LABEL TEXT: every word printed on the product is PURE WHITE on the black stripe; the red cap carries SickScience and the silver half "
       "carries NetWork with a capital N and a capital W; never black, grey or dark letters.")
FIN = ("All product text stays perfectly legible, sharp and accurate. Ultra photorealistic, hyperrealistic, indistinguishable from a real "
       "photograph, 8K detail. No text, no letters, no numbers, no logos added to the scene other than the product's own printed label.")
INTEG = ("INTEGRATION\nThe product was physically in the scene when this photograph was taken, not added later. It shares exactly the same light "
         "direction, softness and colour temperature as everything around it; its chrome reflects the real surroundings as soft natural "
         "reflections; it casts a soft real contact shadow; same focus, grain and slight noise as the rest of the photograph; no outline, no halo.")
NEG = ("black letters, dark or grey text on the product, 'Network' with a lowercase w, redrawn or invented product, fake brand names, misspelled "
       "text, extra text, oversized product, blurred product, CGI, 3D render look, HDR glow, watermark, pasted-on or composited look, cut-out "
       "edges, sticker look, halo, floating product")

XRAY = """Preserve the exact identity of the product: proportions, construction, colours and printed branding exactly as the element shows it. Use the element for identity only; do not redraw any part of it. Capsule bottle: top half glossy metallic red chrome cap, bottom half mirror-polished silver chrome, one black vertical label stripe. Exactly one product, no extra product.

PRODUCT ORIENTATION
The product stands upright on a white ledge in front of a radiology light box, perfectly vertical, front label facing the camera and fully readable. Camera straight on at product height. No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING
{ar} clean scientific editorial still life with an 85mm lens, photographed from far away so the scene occupies only the LOWER part of the frame; the upper part is plain clean white lab wall for text to be added later. A slim white radiology light box glows evenly on the wall; clipped to it is one blue-toned X-ray film showing an elegant, clinical radiograph of a human upper torso from the side during a breast self-check: the ribcage, collarbone and the bones of the raised arm behind the head, and the finger bones of the other hand with three fingertips resting flat on the side of the chest near the armpit. Soft tissue appears only as a faint, smooth, translucent glow with no anatomical detail; the image is tasteful, scientific and non-sexual. The light box spans from about {lb1}% to {lb2}% of the frame height, centred; the product stands on the white ledge just right of centre in front of its lower edge, its top at about {pt}% and its base at about {pb}% of the frame height. Every object fits completely inside the frame.

SCALE
The product is a capsule-shaped bottle 12 cm tall and 3.5 cm in diameter. The X-ray film is 35 × 43 cm, so the product is about a third of the film height. Keep these real proportions; if in doubt make the product smaller, never bigger.

LIGHT AND SHADOW
Cool even glow from the light box behind the film, a soft white key light from the front left on the product, the chrome catching the cool blue glow of the film as a soft reflection that never covers any printed word; every printed word stays clearly lit and legible.

BACKGROUND
Only a clean bright white laboratory wall and the white ledge; no equipment, no screens with text, no people.

PHOTOGRAPHIC FINISH
85mm at f/8. Translucent film with real X-ray grain, matte white light box, mirror chrome. Fine grain, clean cool-white scientific colour with a soft blue cast from the film, premium editorial mood. {FIN}

{INTEG}

{LAB}

Negative: {NEG}, nudity, nipples, visible breast detail, sexualised anatomy, skull, skeleton full body, text, numbers or markers on the X-ray film, hospital clutter, dark moody scene, blood, disease, tumour, red marks on the film"""

PAIR = """Preserve the exact identity of the product: proportions, construction, colours and printed branding exactly as the element shows it. Use the element for identity only; do not redraw any part of it. Capsule bottle: rounded pill silhouette, top half glossy metallic red chrome cap with a smooth round dome, bottom half mirror-polished silver chrome, one black vertical label stripe. Exactly TWO identical products of this same kind, no third product.

PRODUCT ORIENTATION
The two products stand upright side by side, their caps almost touching, photographed perfectly top-down from directly above, so that only their two round, glossy red chrome domed caps are seen as two perfect circles of the same size next to each other; the thin black label stripe crosses the top of each dome. Camera exactly above, looking straight down. No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING
{ar} minimal top-down studio still life with a 100mm macro lens, on a seamless soft blush-pink surface. The two red domes sit side by side, centred horizontally, in the {band} of the frame, each dome about {w}% of the frame width, with a soft shadow ring around each base. A large ring light directly above the camera reflects in each glossy chrome dome as one bright, soft, perfectly circular ring highlight exactly in the centre of each dome. {space} Every object fits completely inside the frame.

SCALE
Each cap is 3.5 cm in diameter; the two domes are identical in size. Keep these real proportions.

LIGHT AND SHADOW
One large ring light directly above, creating a centred circular ring reflection in each dome, soft even falloff, gentle soft shadows around the bases on the pink surface.

BACKGROUND
Only the seamless soft blush-pink surface; no props, no pattern, no text, no people.

PHOTOGRAPHIC FINISH
100mm macro at f/11. Deep glossy red chrome with true reflections of the ring light, smooth matte pink paper. Fine grain, clean rich colour, witty premium campaign look. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no numbers, no logos added to the scene.

{INTEG}

Negative: {NEG}, side view, product lying down, more than two products, one product, different sizes, labels facing the camera, nipples, skin, body, anatomy, fruit, extra objects"""

out = {}
for k, ar, lb1, lb2, pt, pb in [('xr', 'Vertical 9:16', 46, 80, 66, 84), ('xr_sq', 'Square 1:1', 50, 86, 70, 92)]:
    out[k] = ['A real scientific editorial photograph featuring ', 'ss-network', ' \n\n' + XRAY.format(ar=ar, lb1=lb1, lb2=lb2, pt=pt, pb=pb, FIN=FIN, INTEG=INTEG, LAB=LAB, NEG=NEG)]
for k, ar, band, w, space in [('pair', 'Vertical 9:16', 'middle band between 45% and 65%', 30, 'The upper 42% of the frame is plain pink surface for text to be added later.'),
                              ('pair_sq', 'Square 1:1', 'lower-middle band between 45% and 80%', 32, 'The upper 40% of the frame is plain pink surface for text to be added later.')]:
    out[k] = ['A real top-down studio product photograph featuring ', 'ss-network', ' \n\n' + PAIR.format(ar=ar, band=band, w=w, space=space, INTEG=INTEG, NEG=NEG)]
json.dump(out, open('batch-15.json', 'w'), ensure_ascii=True)
for k, v in out.items():
    print(k, len(v[0] + v[2]))
