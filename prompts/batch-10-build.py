"""Batch 10 prompts (competitor patterns v2: Nutrafol / Vegamour). Writes batch-10.json for the Higgsfield page."""
import json

LAB = ("LABEL TEXT: every word printed on the products is PURE WHITE on the black stripe, on the coloured cap and on the silver "
       "half alike; never black, grey or dark letters. NetWork, if present, is spelled with a capital N and a capital W.")
FIN = ("All product text stays perfectly legible, sharp and accurate. Ultra photorealistic, hyperrealistic, indistinguishable "
       "from a real photograph, 8K detail. No text, no letters, no logos added to the scene other than the products' own printed labels.")
NEG = ("black, grey or dark letters on the product, extra products, redrawn or invented product, fake brand names, misspelled text, "
       "extra text, tilted product, oversized product, blurred product, unreadable text, CGI, 3D render look, plastic skin, HDR glow, watermark")

CAPS = {
    'ss': ('ss-shapeshift', 'violet', 'ShapeShift', '12 cm tall and 3.5 cm in diameter'),
    'nw': ('ss-network', 'red', 'NetWork', '12 cm tall and 3.5 cm in diameter'),
    'pc': ('ss-powercycle', 'lime-green', 'PowerCycle', '14 cm tall and 4.5 cm in diameter'),
}
BACK = {'ss': 'soft pale lavender', 'nw': 'soft warm blush pink', 'pc': 'soft pale sage green', 'do': 'soft pale powder blue'}

def ident_caps(color):
    return ("Preserve the exact identity of the product: proportions, construction, colours and printed branding exactly as the element "
            "shows it. Use the element for identity only; do not redraw any part of it. The capsule bottle keeps its rounded pill "
            f"silhouette: top half glossy metallic {color} chrome cap, bottom half mirror-polished silver chrome, vertical printed text "
            "on a black stripe exactly as the element shows it. Exactly one product, no extra product.")

IDENT_DO = ("Preserve the exact identity of the product: proportions, construction, colours and printed branding exactly as the element "
            "shows it. Use the element for identity only; do not redraw any part of it. The product is a glossy cobalt-blue squeeze tube "
            "with a blue screw cap and vertical white printed text exactly as the element shows it. Exactly one product, no extra product.")

def hand(key):
    if key == 'do':
        el, ident, scale = 'ss-dropoff', IDENT_DO, 'The tube is about 20 cm tall; an adult hand is about 18 cm long.'
        orient = ("A woman's hand, early-to-mid 30s, natural short nails, enters from the lower right and holds the tube upright, "
                  "fingers wrapped around its lower third only, the front label facing the camera and fully readable, never covered by fingers.")
    else:
        el, color, name, size = CAPS[key]
        ident, scale = ident_caps(color), f'The product is a capsule-shaped bottle {size}; an adult palm is about 18 cm long, so the capsule is about two thirds of the hand length.'
        orient = ("A woman's open hand, early-to-mid 30s, natural short nails, palm facing up, enters from the lower right; the product "
                  "stands upright on the flat open palm, perfectly vertical, front label facing the camera and fully readable.")
    body = f"""{ident}

PRODUCT ORIENTATION
{orient} Camera straight on at product height. No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING
Vertical 9:16 minimal beauty still life with an 85mm full-frame lens, inspired by calm premium supplement ads. A plain seamless backdrop in {BACK[key]} fills the frame. The hand and the product sit in the lower middle of the frame, centred horizontally: the top of the product at about 46% of the frame height and the palm at about 66%; the wrist and forearm continue out of the bottom right edge. Keep the upper 42% of the frame as clean empty backdrop for text to be added later. Every object fits completely inside the frame except the forearm.

SCALE
{scale} Keep these real proportions; if in doubt make the product smaller, never bigger.

LIGHT AND SHADOW
Soft diffused window light from the upper left, a gentle soft shadow of the hand on the backdrop, the chrome catching soft highlights that never cover any printed word; every printed word stays clearly lit and legible.

BACKGROUND
Only the plain {BACK[key]} seamless backdrop; no props, no pattern, no horizon line, no other people.

PHOTOGRAPHIC FINISH
85mm lens at f/5.6. Real skin texture on the hand with fine pores and natural creases, mirror chrome with soft reflections. Fine photographic grain, calm natural colour, soft premium mood. {FIN}

{LAB}

Negative: {NEG}, product lying down, fingers covering the label, extra fingers, deformed hand, face, rings, nail polish, props."""
    return ['A real editorial beauty photograph featuring ', el, ' \n\n' + body]

def phone(key):
    el, color, name, size = CAPS[key]
    body = f"""{ident_caps(color)}

PRODUCT ORIENTATION
The product stands upright on the table top, perfectly vertical, front label facing the camera and fully readable, right next to a vintage {color} rotary telephone. Camera at table height, straight on. No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING
Vertical 9:16 retro editorial fashion photograph with a 35mm lens, camera pulled back, waist-up. A woman in her early-to-mid 30s with very long glossy dark hair flowing over her shoulders leans forward on a plain white table, resting on her forearms, holding the curly-corded {color} handset of the vintage rotary phone to her ear with one hand and looking calmly into the camera. The {color} rotary phone sits on the table in front of her and the product stands upright beside the phone. The person occupies only the central 55% of the frame width. Her face and the product sit in the same horizontal band, between 48% and 72% of the frame height. The entire upper 45% of the frame is nothing but smooth plain pale grey backdrop for text to be added later. Every object fits completely inside the frame.

SCALE
The product is a capsule-shaped bottle {size}; the rotary phone body is about 22 cm wide, so the product is about half the phone width. Keep these real proportions; if in doubt make the product smaller, never bigger.

LIGHT AND SHADOW
Soft even studio light from the front left, gentle shadows, the chrome catching soft highlights that never cover any printed word; every printed word stays clearly lit and legible.

BACKGROUND
Only a smooth plain pale grey seamless studio backdrop; no props other than the phone and the product, no pattern, no other people.

PHOTOGRAPHIC FINISH
50mm look at f/5.6, real skin texture with visible pores, no heavy retouching, glossy healthy hair, glossy plastic phone, mirror chrome. Fine grain, soft natural colour, playful retro-chic mood. {FIN}

{LAB}

Negative: {NEG}, modern smartphone, mobile phone, extra fingers, deformed hands, heavy makeup, plastic skin, text on the phone."""
    return ['A real retro editorial photograph featuring ', el, ' \n\n' + body]

def cake(key):
    if key == 'award':
        el, items, scale, back = ('ss-set-award-duo', 'ShapeShift (violet chrome capsule bottle, 12 cm tall) and PowerCycle (lime-green chrome capsule bottle, 14 cm tall)',
                                  'ShapeShift is 12 cm tall and 3.5 cm in diameter; PowerCycle is 14 cm tall and 4.5 cm in diameter.', 'soft pale lavender')
    else:
        el, items, scale, back = ('ss-set-body-duo', 'DropOff (glossy cobalt squeeze tube about 20 cm tall, standing on its blue screw cap) and ShapeShift (violet chrome capsule bottle, 12 cm tall)',
                                  'DropOff is about 20 cm tall; ShapeShift is 12 cm tall and 3.5 cm in diameter, so DropOff is about 1.6 times taller.', 'soft pale powder blue')
    body = f"""Preserve the exact identity of every item in the set: proportions, construction, colours and printed branding exactly as the element shows them. Use the element for identity only; do not redraw any part of it. The set contains {items}. Exactly two products from the set, no extra product.

PRODUCT ORIENTATION
The two products stand side by side on the top tier of a wedding cake like a bride and groom cake topper, both upright and perfectly vertical, about 3 cm apart, front labels facing the camera and fully readable. Camera at top-tier height, straight on. No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING
Vertical 9:16 playful wedding still life with an 85mm full-frame lens. A three-tier white wedding cake with smooth white buttercream and delicate piped pearl borders stands centred on a white cake stand. The two products stand on the top tier as the cake topper. The top of the taller product is at about 44% of the frame height; the cake fills the lower half and runs off the bottom edge of the frame. Keep the upper 42% of the frame as clean empty backdrop for text to be added later. Every object fits completely inside the frame except the lower cake tiers.

SCALE
{scale} The top tier of the cake is 15 cm wide and 10 cm tall. Keep these real proportions; if in doubt make the products smaller, never bigger.

LIGHT AND SHADOW
Soft bright window light from the upper left, gentle shadows in the piped details, chrome with soft highlights that never cover any printed word; every printed word stays clearly lit and legible.

BACKGROUND
Only a plain {back} seamless backdrop; no flowers, no candles, no people, no table setting.

PHOTOGRAPHIC FINISH
85mm lens at f/8. Velvety buttercream with real piping texture, glossy chrome, smooth tube plastic. Fine grain, airy high-key natural colour, romantic premium mood. {FIN}

{LAB}

Negative: {NEG}, toy figurines, bride and groom figurines, flowers, candles, sparkles, products lying down, products sinking into the cake, cake slices, knife."""
    return ['A real editorial still-life photograph featuring ', el, ' \n\n' + body]

out = {f'hand_{k}': hand(k) for k in ['ss', 'nw', 'pc', 'do']}
out.update({f'phone_{k}': phone(k) for k in ['ss', 'pc']})
out.update({f'cake_{k}': cake(k) for k in ['award', 'body']})
json.dump(out, open('batch-10.json', 'w'), ensure_ascii=True)
for k, v in out.items():
    print(k, v[1], len(v[0] + v[2]))
