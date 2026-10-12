"""Batch 16 — ShapeShift product video start frames (2026-10-04). Writes batch-16.json (9:16, Higgsfield Unlimited)."""
import json

LAB = ("LABEL TEXT: every word printed on the product is PURE WHITE on the black stripe — on the violet cap AND on the silver half; "
       "never black, grey or dark letters. The label reads exactly 'ShapeShift'.")
FIN = ("All product text stays perfectly legible, sharp and accurate. Ultra photorealistic, hyperrealistic, indistinguishable from a real "
       "photograph, 8K detail. No text, no letters, no numbers, no logos added to the scene other than the product's own printed label.")
INTEG = ("INTEGRATION\nThe product was physically in the scene when this photograph was taken, not added later: same light direction, softness "
         "and colour temperature as everything around it; its chrome reflects the real surroundings; a soft real contact shadow; same focus, "
         "grain and noise as the rest of the photograph; no outline, no halo.")
NEG = ("opaque white cream, thick white lotion, whipped or peaked cream, water-clear liquid, fully transparent gel, black letters, dark or grey text on the product, extra products, redrawn or invented product, fake brand names, misspelled text, extra "
       "text, oversized product, product in the foreground closer to the camera than the model, giant product, blurred product, CGI, 3D render "
       "look, plastic skin, HDR glow, watermark, pasted-on or composited look, halo, casual home snapshot, messy bathroom")
CAPS = ("Preserve the exact identity of the product: proportions, construction, colours and printed branding exactly as the element shows it. "
        "Use the element for identity only; do not redraw any part of it. Capsule bottle with a rounded pill silhouette: top half glossy "
        "metallic violet chrome cap, bottom half mirror-polished silver chrome, vertical PURE WHITE printed text on a black stripe. Exactly one product.")
OPEN = ("Preserve the exact identity of the product: proportions, construction, colours and printed branding exactly as the element shows it. "
        "Use the element for identity only; do not redraw any part of it. The opened capsule bottle: mirror-polished silver chrome body with a "
        "white pump head on top, vertical PURE WHITE printed text on a black stripe. Exactly one product.")
WOMAN = ("a strikingly beautiful woman in her late 20s with model-like features, luminous glowing skin with real fine pores, long sleek dark "
         "hair pulled back in a low ponytail so her neck and jawline are fully visible, wearing a simple matte lilac strapless bandeau top "
         "that leaves her neck, collarbones and shoulders bare")
SET = ("a styled studio set built as a minimal luxury bathroom: smooth white plaster walls rising very high, a sculptural white stone vanity, "
       "a soft oval mirror, a folded white towel and a small glass vase with a single lilac stem — clearly an art-directed campaign set")

def p(opener, el, ident, orient, comp, scale, light, back, finish, neg):
    body = f"""{ident}

PRODUCT ORIENTATION
{orient} No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING
{comp} Every object fits completely inside the frame.

SCALE
The ShapeShift capsule is 12 cm tall and 3.5 cm in diameter. {scale} Keep real proportions; if in doubt make the product smaller, never bigger.

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
 'ss_hook': p('A real high-end beauty campaign photograph shot on a styled studio set, featuring ', 'ss-shapeshift', CAPS,
    'The product stands upright on the white stone vanity right beside the model, at the same distance from the camera as she is, front label facing the camera.',
    f'Vertical 9:16, 50mm lens, {SET}. {WOMAN} stands in a three-quarter profile facing the mirror on the left, chin slightly lifted, the fingertips of one hand gently tracing along her jawline from chin to ear; calm, confident expression. Medium shot from the waist up; her head is at about 40% to 55% of the frame height; the upper 35% of the frame is plain white wall for text added later. The product stands on the vanity at the lower left, at her hip height.',
    'The product is at the same depth as the model, so it appears at its true size: about two thirds of the length of her hand.',
    'Soft large octabox key light from the front left, gentle white fill, a soft rim light along her jaw and neck that accentuates the jawline.',
    'Only the styled white set; no clutter, no window, no other people.',
    'Medium-format look, 50mm at f/5.6. Real skin with fine pores, polished but not plastic. Clean, bright, premium editorial colour with soft lilac accents.',
    'hand covering the face, chin down, turtleneck, necklace'),
 'ss_dispense': p('A real high-end beauty macro photograph featuring ', 'ss-open-shapeshift', OPEN,
    'One hand holds the open product upright, pressing the white pump; the front label faces the camera and stays fully readable, fingers never covering the printed word.',
    'Vertical 9:16 macro beauty shot, 90mm macro lens. Two hands of a woman in her late 20s with natural short nails in front of a seamless soft lilac backdrop: one hand presses the pump of the open product, and a small glossy bead of translucent gel-serum — semi-transparent with a soft milky haze, neither opaque white cream nor water-clear, with a soft rounded shape rests on the fingertips of the other hand. The product and hands sit between 40% and 85% of the frame height; the upper 35% is plain lilac backdrop for text added later.',
    'An adult hand is about 18 cm long; the product is 12 cm tall. The bead of gel-serum is about 1.5 cm wide.',
    'Soft studio light from the upper left, light passing through the edges of the gel-serum and a crisp highlight on its glossy surface.',
    'Only the seamless soft lilac backdrop; no props, no people other than the two hands.',
    '90mm macro at f/8. Real skin texture, translucent gel-serum with a soft milky haze and glossy surface, mirror chrome, white pump. Clean premium colour.',
    'clear gel, transparent gel, watery serum, dripping, extra fingers, deformed hands, rings, nail polish'),
 'ss_apply': p('A real high-end beauty campaign photograph shot on a styled studio set, featuring ', 'ss-shapeshift', CAPS,
    'The product stands upright on the white stone vanity right beside the model, at the same distance from the camera as she is, front label facing the camera.',
    f'Vertical 9:16, 50mm lens, {SET}. {WOMAN} faces the camera with her eyes gently closed and chin lifted, the flat fingers of both hands sweeping upward from the base of her neck along both sides of the jawline, applying a thin, barely visible layer of translucent gel-serum, serene and confident. Medium close-up from the chest up; her face is at about 40% to 58% of the frame height; the upper 32% of the frame is plain white wall for text added later. The product stands on the vanity at the lower left.',
    'The product is at the same depth as the model, so it appears at its true size: about two thirds of the length of her hand.',
    'Soft large octabox key light from the front, gentle fill, a soft rim light along her jaw and neck.',
    'Only the styled white set; no clutter, no window, no other people.',
    'Medium-format look, 50mm at f/5.6. Real skin with fine pores and a soft dewy finish where the serum is applied. Clean, bright, premium editorial colour.',
    'hands covering the face, eyes open wide, necklace, turtleneck'),
 'ss_hero': p('A real high-end studio product photograph featuring ', 'ss-shapeshift', CAPS,
    'The product stands upright on a frosted lilac acrylic plinth, perfectly vertical, front label facing the camera. Camera at product height, straight on.',
    'Vertical 9:16 minimal product still life with a 100mm lens, photographed from far away so the scene occupies only the LOWER HALF of the frame; the entire upper half is clean empty backdrop for text added later. The product stands centred on the plinth with its top at about 58% and the plinth base at about 82% of the frame height; a single lilac stem lies at the base of the plinth.',
    'The plinth is 6 cm tall and 14 cm wide.',
    'Large soft key light from the upper left and a thin strip light on the right edge drawing clean vertical highlights on the violet chrome.',
    'Only a seamless backdrop in a smooth gradient from soft white at the top to pale lilac at the bottom; no pattern, no horizon line.',
    '100mm at f/11. Mirror chrome with true reflections, frosted acrylic. Fine grain, clean premium colour.',
    'people, hands, flowers other than the single stem, purple colour cast'),
}
json.dump(out, open('batch-16.json', 'w'), ensure_ascii=True)
for k, v in out.items():
    print(k, v[1], len(v[0] + v[2]))
