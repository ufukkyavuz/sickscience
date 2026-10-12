"""Batch 11 — NetWork × BCRF (Breast Cancer Awareness Month, Oct 2026). Writes batch-11.json."""
import json

IDENT = ("Preserve the exact identity of the product: proportions, construction, colours and printed branding exactly as the element "
         "shows it. Use the element for identity only; do not redraw any part of it. The capsule bottle keeps its rounded pill silhouette: "
         "top half glossy metallic red chrome cap, bottom half mirror-polished silver chrome, and one black vertical label stripe running "
         "the full length over both halves. Exactly one product, no extra product.")
LAB = ("LABEL TEXT: the words SickScience and NetWork on the black stripe are PURE WHITE, on the red cap and on the silver half alike; "
       "never black, grey or dark letters. NetWork is spelled with a capital N and a capital W.")
FIN = ("All product text stays perfectly legible, sharp and accurate. Ultra photorealistic, hyperrealistic, indistinguishable from a real "
       "photograph, 8K detail. No text, no letters, no numbers, no logos added to the scene other than the product's own printed label.")
NEG = ("black, grey or dark letters on the product, 'Network' with a lowercase w, extra products, redrawn or invented product, fake brand names, "
       "misspelled text, extra text, tilted product, oversized product, blurred product, unreadable text, CGI, 3D render look, HDR glow, watermark")
SCALE = "The product is a capsule-shaped bottle 12 cm tall and 3.5 cm in diameter."
RIBBON = ("a soft pink satin breast-cancer-awareness ribbon tied in the classic looped ribbon shape, about 9 cm tall")
FAR = ("photographed from far away so the scene occupies only the LOWER HALF of the frame; the entire upper half of the frame is nothing but "
       "clean empty backdrop for text to be added later")

def p(opener, orient, comp, scale, light, back, finish, neg):
    body = f"""{IDENT}

PRODUCT ORIENTATION
{orient} No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING
{comp} Every object fits completely inside the frame.

SCALE
{SCALE} {scale} Keep these real proportions; if in doubt make the product smaller, never bigger.

LIGHT AND SHADOW
{light} The chrome catches soft highlights that never cover any printed word; every printed word stays clearly lit and legible.

BACKGROUND
{back}

PHOTOGRAPHIC FINISH
{finish} {FIN}

{LAB}

Negative: {NEG}, {neg}"""
    return [opener, 'ss-network', ' \n\n' + body]

out = {
 'bc_ribbon': p('A real studio beauty photograph featuring ',
    'The product stands upright on a low pale pink acrylic block, perfectly vertical, front label facing the camera. Camera at product height, straight on.',
    f'Vertical 9:16 minimal still life with a 85mm lens, {FAR}. The product stands centred with {RIBBON} lying at its base, the ribbon loop leaning gently against the silver half without covering any printed word. The top of the product is at about 56% of the frame height and the acrylic block at about 78%.',
    'The ribbon is about 9 cm tall, three quarters of the product height. The acrylic block is 4 cm tall and 14 cm wide.',
    'Soft diffused light from the upper left, a gentle warm glow behind the product, soft contact shadow.',
    'Only a seamless soft blush-pink paper backdrop with a subtle lighter glow behind the product; no props, no pattern, no horizon line, no people.',
    '85mm at f/8. Mirror chrome, satin ribbon sheen, frosted acrylic. Fine grain, airy soft-pink natural colour, hopeful premium mood.',
    'flowers, hearts, confetti, candles, people, hands, red ribbon, extra ribbons'),
 'bc_lab': p('A real editorial laboratory photograph featuring ',
    'The product stands upright on a clean white laboratory bench, perfectly vertical, front label facing the camera. Camera at bench height, straight on.',
    f'Vertical 9:16 bright daylight lab still life with a 50mm lens, {FAR}. The product stands slightly right of centre; {RIBBON} lies flat on the bench to its left; a white microscope stands softly out of focus in the back left, and a small rack of clear glass test tubes stands softly out of focus at the back right. The top of the product is at about 58% of the frame height and the bench edge at about 80%.',
    'The microscope is about 40 cm tall and stands far behind, so it looks small and soft.',
    'Bright soft daylight from large windows on the left, clean white bounce, very soft shadows.',
    'Only a bright, clean, softly blurred white laboratory with pale walls; no people, no screens with text, no labels on the glassware, no signs.',
    '50mm at f/4 with soft background blur. Matte white lab bench, clear glass, mirror chrome, satin ribbon. Fine grain, clean bright natural colour, hopeful scientific mood.',
    'people, hands, text on glassware, warning signs, biohazard symbols, syringes, blood, dark or clinical-cold blue mood, flowers'),
 'bc_human': p('A real editorial portrait photograph featuring ',
    'She holds the product upright in one hand, raised beside her cheek, perfectly vertical, front label facing the camera and fully readable, fingers around the lower half only, never covering any printed word. Camera at eye level, straight on.',
    f'Vertical 9:16 warm portrait with a 35mm lens, {FAR}. A woman in her early-to-mid 30s with shoulder-length dark hair, natural glowing skin and a soft hopeful smile, wearing a soft blush-pink knit sweater with a small pink satin awareness-ribbon pin on her chest, holds the product beside her cheek. The top of her head is at about 54% of the frame height; her face and the product sit side by side in the same band between 58% and 72% of the frame height; her shoulders continue to the bottom edge. The person occupies only the central 55% of the frame width.',
    'An adult hand is about 18 cm long, so the capsule is about two thirds of the hand length. The ribbon pin is about 4 cm tall.',
    'Soft warm window light from the left, gentle shadows, natural skin tones.',
    'Only a plain warm off-white plaster wall softly out of focus; no props, no text, no other people.',
    '35mm look at f/4, real skin texture with visible pores, no heavy retouching, soft knit texture, mirror chrome. Fine grain, warm natural colour, hopeful intimate mood.',
    'heavy makeup, plastic skin, extra fingers, deformed hands, sad expression, hospital, bald head, red ribbon, large ribbon'),
 'bc_20': p('A real studio product photograph featuring ',
    'The product stands upright on a glossy pink acrylic plinth, perfectly vertical, front label facing the camera. Camera at product mid-height, straight on.',
    f'Vertical 9:16 bold minimal studio still life with a 100mm lens, {FAR}. The product stands alone, centred, on a glossy transparent pink acrylic plinth, with a crisp reflection in the plinth. The top of the product is at about 56% of the frame height and the plinth base at about 82%.',
    'The plinth is 6 cm tall and 16 cm wide.',
    'Large soft key light from the upper left and a thin strip light on the right edge drawing clean vertical highlights, never covering any printed word.',
    'Only a seamless backdrop in a smooth gradient from soft blush pink at the top to deeper rose pink at the bottom; no props, no pattern, no horizon line, no people.',
    '100mm at f/11. Mirror chrome with true reflections, glossy pink acrylic. Fine grain, rich clean colour, confident premium campaign look.',
    'ribbons, flowers, hearts, props, people, hands, orange or purple colour cast'),
}
json.dump(out, open('batch-11.json', 'w'), ensure_ascii=True)
for k, v in out.items():
    print(k, len(v[0] + v[2]))
