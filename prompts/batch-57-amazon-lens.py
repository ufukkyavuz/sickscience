"""Batch 57 — Amazon store v4 (2026-10-20). Concern cards: body area on white with a real glass magnifying lens drawing attention (marketing callout, not macro).
NX35 cards: plant source in a glass petri dish on white. No products, no text. Nano Banana Pro, Unlimited, web UI. Card image 750x1100 → generate 2:3."""
FIN = ("PHOTOGRAPHIC FINISH 85mm lens at f/8, bright high-key studio light, soft diffused key from the upper left, white bounce fill, "
       "clean neutral colour, fine photographic grain. Realistic skin with natural pores and fine texture, no plastic retouching. "
       "Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos, no products, no packaging.")
LENS = ("A real round glass magnifying lens, about 9 cm across, with a thin polished silver metal rim and a short slim silver handle, "
        "is held by a hand coming in from the frame edge and hovers a few centimetres in front of the area, slightly tilted; through the lens the area is "
        "shown about 1.6 times larger with real optical refraction and a crisp bright rim reflection — it draws the eye to the area like a clean beauty-marketing callout.")
P = {
 'lens_jaw': f"""A clean premium beauty-campaign studio photograph about the JAWLINE AND NECK. A strikingly beautiful woman in her late 20s, model-like features, shown from the side in a three-quarter profile, cropped from just below the eyes to the collarbones, chin slightly lifted so the jawline and the side of the neck are the hero. {LENS} The lens hovers over the jaw angle and the line under the chin. COMPOSITION AND FRAMING Vertical 2:3 frame. The face and neck sit in the centre and right; the lens sits on the jawline in the middle of the frame; generous calm white space around. BACKGROUND Pure seamless bright white studio backdrop, nothing else. {FIN} Negative: full face, eyes in frame looking at the camera, makeup-heavy look, jewellery, products, bottles, text, extreme macro, grey or dark background, coloured background, distorted anatomy, extra fingers, more than one hand, warped lens, cartoon, CGI, 3D render.""",
 'lens_glow': f"""A clean premium beauty-campaign studio photograph about SKIN GLOW AND TEXTURE. A strikingly beautiful woman in her late 20s, model-like features, softly lit, cropped close from the forehead to the chin, face turned three-quarter to the side, natural fresh dewy skin. {LENS} The lens hovers over her cheekbone, showing smooth luminous skin texture with natural pores. COMPOSITION AND FRAMING Vertical 2:3 frame, face in the centre-right, the lens on the cheek in the middle of the frame, calm white space around. BACKGROUND Pure seamless bright white studio backdrop, nothing else. {FIN} Negative: heavy makeup, glitter, oily skin, blemishes exaggerated, products, bottles, text, extreme macro, grey or dark background, coloured background, distorted anatomy, extra fingers, more than one hand, warped lens, cartoon, CGI, 3D render.""",
 'lens_hair': f"""A clean premium beauty-campaign studio photograph about HAIR DENSITY. A strikingly beautiful woman in her late 20s with long healthy dark-brown hair, seen from slightly above and behind at a three-quarter angle, head gently tilted down so the centre parting and the top of the scalp are visible, cropped from the top of the head to the shoulders. {LENS} The lens hovers over the hair parting, showing the strands and the parting line magnified. COMPOSITION AND FRAMING Vertical 2:3 frame, head in the centre, the lens on the parting in the upper-middle of the frame, calm white space around. BACKGROUND Pure seamless bright white studio backdrop, nothing else. {FIN} Negative: bald patches, balding man, visible face looking at camera, products, bottles, dropper, text, extreme macro, grey or dark background, coloured background, distorted anatomy, extra fingers, more than one hand, warped lens, cartoon, CGI, 3D render.""",
 'lens_body': f"""A clean premium body-care campaign studio photograph about CELLULITE ON THE THIGH. A fit woman in her late 20s with a natural healthy body, wearing simple seamless white high-cut briefs, shown from the side at hip and thigh level, cropped from the waist to just above the knee; the outer thigh and the side of the buttock are the hero, with a very mild, realistic, everyday dimpled skin texture on the outer thigh. {LENS} The lens hovers over the outer thigh, showing the mild dimpled texture magnified. COMPOSITION AND FRAMING Vertical 2:3 frame, hip and thigh in the centre, the lens on the outer thigh in the middle of the frame, calm white space around. Tasteful, non-sexual, clinical-beauty campaign look. BACKGROUND Pure seamless bright white studio backdrop, nothing else. {FIN} Negative: nudity, lingerie styling, sexualised pose, severe cellulite, stretch marks exaggerated, products, tubes, text, extreme macro, grey or dark background, coloured background, distorted anatomy, extra fingers, more than one hand, warped lens, cartoon, CGI, 3D render.""",
}
DISH = ("A clean premium laboratory still-life photograph. A single round clear borosilicate glass petri dish, about 10 cm across, stands on a glossy white laboratory surface, "
        "seen from about 35 degrees above, in the centre of a square frame with generous white space; real refraction in the glass, a soft contact shadow and crisp caustics on the white surface. ")
FIN2 = ("BACKGROUND Pure seamless bright white backdrop, nothing else. PHOTOGRAPHIC FINISH 100mm lens at f/8, bright high-key studio light from the upper left, clean neutral colour, fresh natural textures, fine grain. "
        "Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos, no products, no bottles. "
        "Negative: products, bottles, labels, text, coloured background, dark scene, juice spills, CGI, 3D render, plastic textures.")
P['nx_sculpt'] = DISH + "Inside the dish: two thin fresh pineapple slices with their golden rind, and beside them one soft bead of a translucent gel-serum, semi-transparent with a soft milky haze. " + FIN2
P['nx_radiance'] = DISH + "Inside the dish: a few thin fresh radish slices with pink rims and a few thin fresh cucumber slices, neatly overlapping, and one soft bead of a translucent gel-serum, semi-transparent with a soft milky haze. " + FIN2
P['nx_growth'] = DISH + "Inside the dish: three peeled garlic cloves and a small bundle of golden wheat ears laid across, and one soft bead of a translucent gel-serum, semi-transparent with a soft milky haze. " + FIN2
if __name__=='__main__':
    for k,v in P.items(): open(f'/private/tmp/claude-501/p57_{k}.txt','w').write(v); print(k,len(v))

# v2 (user 2026-10-20: "mercekler uzaktan tutulmalı daha geniş bi alanı göstermeli… daha artistik… kendi tutmasın")
LENS2 = ("A large round optical glass lens, about 22 cm across, frameless with a polished bevelled edge, is suspended in mid-air about 25 cm in front of the body, "
         "held only by an almost invisible thin clear acrylic arm coming from outside the frame; nobody holds it and the model's hands do not touch it. "
         "Because it is held further away it magnifies a wider area, about 1.3 times, with real optical refraction and a crisp bright edge; "
         "the lens also casts a soft graphic shadow and a bright focused caustic ring of light onto the skin beside it.")
ART = ("Fine-art editorial beauty photograph, sculptural minimal composition, gallery-like calm, soft directional studio light that models the body, "
       "pure white seamless backdrop with a gentle soft shadow. ")
FIN3 = ("PHOTOGRAPHIC FINISH medium-format look, 90mm lens at f/8, clean neutral colour, realistic skin with natural pores and fine texture, no plastic retouching, fine grain. "
        "Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos, no products, no packaging. "
        "Negative: hand holding the lens, handle, magnifying glass with handle, model touching the lens, visible stand clutter, extreme macro, products, text, grey or dark background, coloured background, distorted anatomy, extra limbs, warped lens, cartoon, CGI, 3D render.")
P['lens2_jaw'] = ART + "A strikingly beautiful woman in her late 20s, model-like features, in elegant three-quarter profile, cropped from the cheekbones to the collarbones, chin lifted so the jawline and neck line are the hero; her hands rest out of frame. " + LENS2 + " The lens hangs in front of the jaw angle and the line under the chin. Vertical 2:3 frame, generous white space. " + FIN3
P['lens2_glow'] = ART + "A strikingly beautiful woman in her late 20s, model-like features, face in three-quarter view with eyes softly closed, fresh dewy luminous skin, cropped from the forehead to the shoulders; her hands are not in frame. " + LENS2 + " The lens hangs in front of her cheek and cheekbone. Vertical 2:3 frame, generous white space. " + FIN3
P['lens2_hair'] = ART + "A strikingly beautiful woman in her late 20s with long glossy dark-brown hair, seen from behind and slightly above, head gently bowed so the centre parting and the crown are visible, hair falling down her back, cropped from the top of the head to the mid back; her hands are not in frame. " + LENS2 + " The lens hangs above the parting and crown. Vertical 2:3 frame, generous white space. " + FIN3
P['lens2_body'] = ART + "A fit woman in her late 20s with a natural healthy body in simple seamless white high-cut briefs, shown from the side at hip and thigh level, cropped from the waist to the knee, standing in a calm sculptural pose; a very mild, realistic everyday dimpled texture on the outer thigh; tasteful, non-sexual. " + LENS2 + " The lens hangs in front of the outer thigh. Vertical 2:3 frame, generous white space. " + FIN3.replace("Negative:", "Negative: nudity, sexualised pose, severe cellulite,")
if __name__=='__main__':
    for k in ['lens2_jaw','lens2_glow','lens2_hair','lens2_body']: open(f'/private/tmp/claude-501/p57_{k}.txt','w').write(P[k]); print(k,len(P[k]))

# v3 (user 2026-10-20, reference: DUMAIN glasses through a lens): lens in the foreground, centred, sharp inside / soft outside
def V3(area, subject):
    return ("A refined editorial beauty photograph shot THROUGH a magnifying lens. A large round magnifying lens with a very thin dark metal rim and no handle "
            "sits in the foreground very close to the camera, perfectly centred in the frame and filling about 75% of the frame width; no hand, no handle, no stand is visible. "
            f"Through the lens the camera focuses sharply on {area}, magnified about 1.5 times with crisp detail and real optical refraction at the edge. "
            f"{subject} Everything OUTSIDE the lens circle is softly out of focus with a creamy shallow depth of field — the same body continues outside the rim but blurred and slightly smaller. "
            "The lens rim itself is a thin, slightly soft dark line. Vertical 2:3 frame. BACKGROUND soft warm white seamless studio backdrop, out of focus. "
            "PHOTOGRAPHIC FINISH 100mm macro lens at f/2.8, soft warm daylight from the upper left, gentle natural shadows, realistic skin with natural pores and fine texture, no plastic retouching, fine grain. "
            "Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos, no products, no packaging. "
            "Negative: hand, fingers holding the lens, handle, stand, everything sharp, lens off-centre, two lenses, products, text, dark background, coloured background, distorted anatomy, warped lens, cartoon, CGI, 3D render.")
P['v3_jaw']  = V3("the jawline, the angle of the jaw and the smooth line under the chin", "A strikingly beautiful woman in her late 20s in three-quarter profile, chin slightly lifted; the jaw and neck fill the lens.")
P['v3_glow'] = V3("her cheekbone and cheek skin, smooth and luminous with fine natural pores", "A strikingly beautiful woman in her late 20s, face turned three-quarter, eyes softly closed; the cheek fills the lens.")
P['v3_hair'] = V3("the centre hair parting and the dense glossy strands beside it", "A woman in her late 20s with long glossy dark-brown hair seen from above and behind, head gently bowed; the parting runs through the lens.")
P['v3_body'] = V3("the outer thigh with a very mild, realistic everyday dimpled skin texture", "A fit woman in her late 20s in simple seamless white briefs, seen from the side at thigh level, tasteful and non-sexual; the outer thigh fills the lens.")
if __name__=='__main__':
    for k in ['v3_jaw','v3_glow','v3_hair','v3_body']: open(f'/private/tmp/claude-501/p57_{k}.txt','w').write(P[k])

# What's inside flat-lays (user: "ürünlerin içinde çok az içerik varmış gibi gözüküyo") — abundance, no product
def FL(items):
    return ("A clean premium overhead flat-lay laboratory photograph, shot straight down from above. On a glossy white laboratory surface, "
            f"a neat, generous arrangement of six clear borosilicate glass petri dishes and watch glasses of slightly different sizes, each holding one ingredient: {items}. "
            "The dishes fill the square frame evenly with small white gaps, a few touching, like an organised lab ingredient board. Real refraction in the glass, soft contact shadows, crisp caustics. "
            "BACKGROUND pure bright white. PHOTOGRAPHIC FINISH 100mm lens at f/8, bright high-key soft daylight from the upper left, fresh natural textures, clean neutral colour, fine grain. "
            "Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no labels, no letters, no logos, no products, no bottles, no packaging. "
            "Negative: products, bottles, capsules, tubes, labels, text, coloured background, dark scene, messy spills, CGI, 3D render, plastic textures.")
P['in_ss'] = FL("thin fresh pineapple slices; a smooth scoop of ivory shea butter; roasted coffee beans; fine white crystalline powder; a soft bead of translucent gel-serum with a milky haze; a small swirl of soft white cream")
P['in_nw'] = FL("thin fresh radish slices; thin fresh cucumber slices; whole sweet almonds; a clear golden oil droplet pool; a few small golden vitamin E softgels; a soft bead of translucent gel-serum with a milky haze")
P['in_pc'] = FL("peeled garlic cloves; golden wheat ears; fresh rosemary sprigs; roasted coffee beans; fine white crystalline powder; a soft bead of translucent gel-serum with a milky haze")
P['in_do'] = FL("a fresh pineapple stem core slice; roasted coffee beans; a smooth scoop of ivory shea butter; fine white crystalline powder; a soft bead of translucent gel-serum with a milky haze; a few clear water droplets")
P['hero_min'] = ("A minimal premium laboratory still-life photograph for an ultra-wide website banner background. Almost empty: a soft seamless white backdrop with a very subtle pale lilac glow and a glossy white surface. "
    "Only ONE slim clear borosilicate conical flask stands at the far left edge and ONE small clear beaker with a glass rod at the far right edge, both slightly soft-focused; "
    "a few gentle, crisp caustic light patterns from the glass fall across the white surface. The whole centre 70% of the frame is calm, empty and clean for a headline. "
    "PHOTOGRAPHIC FINISH 100mm lens at f/4, bright high-key soft daylight from the upper left, airy luminous, faint lilac tint, fine grain. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. "
    "No text, no letters, no logos, no products, no packaging. Negative: many glass objects, clutter, products, bottles with labels, capsules, tubes, text, coloured liquids, dark or grey scene, saturated colour, CGI, 3D render.")
if __name__=='__main__':
    for k in ['in_ss','in_nw','in_pc','in_do','hero_min']: open(f'/private/tmp/claude-501/p57_{k}.txt','w').write(P[k])

# v4 (user: "büyüteçin kenarları yok direkt cam… stüdyo çekimi olmalı ilk görsellerdeki gibi")
def V4(area, subject):
    return ("A bright, clean high-key studio beauty photograph shot THROUGH a large round piece of optical glass. "
            "The lens is completely RIMLESS: a plain round disc of clear polished glass with no frame, no metal ring, no handle; its edge shows only as a thin bright refraction line where the glass ends. "
            "The glass disc sits in the foreground very close to the camera, perfectly centred in the frame and filling about 75% of the frame width; no hand or stand is visible. "
            f"Through the glass the camera focuses sharply on {area}, magnified about 1.5 times with crisp detail. {subject} "
            "Everything OUTSIDE the glass circle is softly out of focus with a creamy shallow depth of field — the same body continues outside the edge but blurred. "
            "Vertical 2:3 frame. BACKGROUND pure bright white seamless studio backdrop. "
            "PHOTOGRAPHIC FINISH professional beauty-campaign studio lighting: large soft white key light, white bounce fill, bright and airy, clean neutral white balance (not warm, not yellow), "
            "100mm macro lens at f/2.8, realistic skin with natural pores and fine texture, no plastic retouching, fine grain. "
            "Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos, no products, no packaging. "
            "Negative: metal rim, black ring, frame around the lens, magnifying glass handle, hand, fingers, stand, warm yellow or beige tone, dim moody light, everything sharp, lens off-centre, products, text, coloured background, distorted anatomy, warped glass, cartoon, CGI, 3D render.")
P['v4_jaw']  = V4("the jawline, the angle of the jaw and the smooth line under the chin", "A strikingly beautiful woman in her late 20s in three-quarter profile, chin slightly lifted, bare shoulders; the jaw and neck fill the glass.")
P['v4_glow'] = V4("her cheekbone and cheek skin, smooth and luminous with fine natural pores", "A strikingly beautiful woman in her late 20s, face turned three-quarter, eyes softly closed, hair pulled back; the cheek fills the glass.")
P['v4_hair'] = V4("the centre hair parting and the dense glossy strands beside it", "A woman in her late 20s with long glossy dark-brown hair seen from above and behind, head gently bowed; the parting runs through the glass.")
P['v4_body'] = V4("the outer thigh with a very mild, realistic everyday dimpled skin texture", "A fit woman in her late 20s in simple seamless white briefs, seen from the side at thigh level, tasteful and non-sexual; the outer thigh fills the glass.")
if __name__=='__main__':
    for k in ['v4_jaw','v4_glow','v4_hair','v4_body']: open(f'/private/tmp/claude-501/p57_{k}.txt','w').write(P[k])
