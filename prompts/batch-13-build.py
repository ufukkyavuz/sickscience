"""Batch 13 — NetWork × BCRF self-check concepts (Oct 2026). Writes batch-13.json."""
import json

IDENT = ("Preserve the exact identity of the product: proportions, construction, colours and printed branding exactly as the element "
         "shows it. Use the element for identity only; do not redraw any part of it. The capsule bottle keeps its rounded pill silhouette: "
         "top half glossy metallic red chrome cap, bottom half mirror-polished silver chrome, and one black vertical label stripe running "
         "the full length over both halves. Exactly one product, no extra product.")
LAB = ("LABEL TEXT: every word printed on the product is PURE WHITE on the black stripe, on the red cap and on the silver half alike; "
       "never black, grey or dark letters. The label reads exactly 'NetWork' with a capital N and a capital W.")
FIN = ("All product text stays perfectly legible, sharp and accurate. Ultra photorealistic, hyperrealistic, indistinguishable from a real "
       "photograph, 8K detail. No text, no letters, no numbers, no logos added to the scene other than the product's own printed label.")
NEG = ("black letters, dark or grey text on the product, 'Network' with a lowercase w, extra products, redrawn or invented product, fake brand names, "
       "misspelled text, extra text, tilted product, oversized product, blurred product, unreadable text, CGI, 3D render look, HDR glow, watermark, "
       "pasted-on or composited look, cut-out edges, sticker look, outline or halo around the product, product lit differently from the scene, "
       "product sharper or cleaner than its surroundings, floating product without contact shadow, flat studio reflections on the chrome")
SCALE = "The product is a capsule-shaped bottle 12 cm tall and 3.5 cm in diameter."
FAR = ("photographed from far away so the scene occupies only the LOWER HALF of the frame; the entire upper part of the frame is nothing but "
       "clean, calm, empty background for text to be added later")


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

INTEGRATION
The product was physically in the room when this photograph was taken, not added later. It shares exactly the same light direction, softness and colour temperature as everything around it. Its chrome reflects the real surroundings of this scene (the walls, the surface it stands on, the window light, nearby colours) as soft, slightly distorted natural reflections, not clean studio reflections. It casts a soft, real contact shadow and leaves a faint natural reflection on the surface it touches. It has the same focus depth, sharpness, grain and slight noise as the rest of the photograph; its edges blend naturally into the scene with no outline and no halo.

{LAB}

Negative: {NEG}, {neg}"""
    return [opener, 'ss-network', ' \n\n' + body]


out = {
 # 1 · Add one step to your routine — mirror self-check pose
 'ck_mirror': p('A real editorial wellness photograph featuring ',
    'The product stands upright on a small white floating shelf on the wall at her shoulder height, to her left side of the frame, perfectly vertical, front label facing the camera and fully readable. Camera at chest height, straight on, as if the camera were her bathroom mirror.',
    f'Vertical 9:16 calm bathroom portrait with a 35mm lens, {FAR}. A woman in her early-to-mid 30s with shoulder-length dark hair tied back loosely, natural glowing skin and a calm, focused expression, wearing a plain soft blush-pink sports bra and high-waisted soft grey lounge trousers, stands facing the camera doing a breast self-check in front of her mirror: her right arm is raised with her hand resting behind her head, and the flat pads of the three middle fingers of her left hand rest gently on the side of her chest just below the raised arm, over the sports bra. The pose is calm, natural and non-sexual. The top of her head is at about 50% of the frame height; her face sits between 52% and 60%; the floating shelf with the product is at about 66% of the frame height on the left side; she is cropped at the waist by the bottom edge. The person occupies only the central 55% of the frame width.',
    'An adult hand is about 18 cm long, so the capsule is about two thirds of the hand length. The floating shelf is 30 cm wide and 3 cm thick.',
    'Soft diffused daylight from a window on the left, gentle shadows, natural skin tones.',
    'Only a plain warm white bathroom wall with very subtle large pale tiles at the lower edge, softly out of focus; no mirror frame visible, no towels with text, no other people.',
    '35mm look at f/4, real skin texture with visible pores, no heavy retouching, soft matte sports-bra fabric, mirror chrome. Fine grain, airy warm natural colour, calm empowering mood.',
    'nudity, bare breasts, cleavage focus, lingerie, sexualised pose, hand inside the bra, medical setting, sad expression, heavy makeup, plastic skin, extra fingers, deformed hands, red ribbon, tattoo'),
 # 2 · Shower fog — circle and tick drawn in condensation
 'ck_fog': p('A real editorial bathroom still-life photograph featuring ',
    'The product stands upright on a white marble bathroom ledge in the foreground, perfectly vertical, front label facing the camera and fully readable, completely dry and sharp. Camera at ledge height, straight on.',
    f'Vertical 9:16 steamy bathroom still life with a 50mm lens, {FAR}. Behind the ledge, a frameless glass shower screen fills the whole background, evenly fogged with soft white condensation and a few small water droplets running down. A simple hand-drawn circle about 20 cm wide with a check mark inside it has been wiped into the fog with a fingertip, at about 44% to 56% of the frame height, slightly left of centre; through the wiped lines a soft blush-pink tiled wall is faintly visible. No letters or words are drawn in the fog, only the circle and the check mark. The product stands slightly right of centre with its top at about 58% of the frame height and its base at about 76%; a small folded white towel lies on the ledge to the left.',
    'The ledge is 15 cm deep; the folded towel is 20 cm wide; the drawn circle is about 20 cm wide.',
    'Soft diffused light from above and the left, gentle glow through the fogged glass, soft shadows on the ledge.',
    'Only the evenly fogged glass shower screen with the blush-pink tiles faintly behind it; no shower head, no taps, no bottles, no people, no silhouettes behind the glass.',
    '50mm at f/5.6. Fine condensation texture and real droplets on glass, polished white marble, soft cotton towel, mirror chrome. Fine grain, airy soft-pink natural colour, calm hopeful mood.',
    'letters or words in the fog, emoji, hearts, person behind the glass, silhouettes, nudity, wet or dripping product, fog on the product, extra bottles, shampoo bottles, dark mood'),
 # 3 · Phone reminder — blank screen, notification added in Figma
 'ck_phone': p('A real editorial lifestyle photograph featuring ',
    'The product stands upright on a white marble vanity, perfectly vertical, front label facing the camera and fully readable, just to the right of a modern smartphone. Camera at the height of the phone screen centre, straight on and perfectly square to the phone screen.',
    f'Vertical 9:16 calm morning vanity still life with a 50mm lens. A modern black smartphone with thin even bezels stands upright in portrait orientation, leaning back very slightly against a pale blush-pink tiled wall, its screen facing the camera perfectly square and flat, completely dark and blank, a plain glossy black screen with a soft reflection, no icons, no text, no wallpaper image. The phone stands slightly left of centre and the product stands to its right. The top of the phone is at about 44% of the frame height and both stand on the vanity at about 80% of the frame height; the phone is about 46% of the frame width wide. A small soft-pink satin awareness ribbon lies flat on the marble in front of the phone. Keep the upper 40% of the frame as clean, plain pale blush-pink tiled wall for text to be added later.',
    'The smartphone is 15 cm tall and 7 cm wide, so the 12 cm product is a little shorter than the phone. The ribbon is about 8 cm tall.',
    'Soft diffused morning window light from the left, gentle soft shadows, a clean soft reflection on the black screen that never hides it.',
    'Only the pale blush-pink square-tiled wall with thin white grout, softly lit; no mirror, no other objects, no people.',
    '50mm at f/8. Polished white marble with fine veins, glossy glass screen, satin ribbon, mirror chrome. Fine grain, airy soft-pink natural colour, calm premium morning mood.',
    'text on the phone screen, icons, app interface, notifications, wallpaper, cracked screen, phone lying flat, tilted phone, perspective distortion of the screen, brand logo on the phone, hands, people'),
 # 4 · Know your normal — flat lay sweater, fingertips on the chest of the sweater
 'ck_hand': p('A real editorial flat-lay photograph featuring ',
    'The product lies flat on the knit sweater, its full length resting on the fabric, front label facing straight up to the camera and fully readable, never standing upright. Camera directly overhead, perfectly top-down.',
    f'Vertical 9:16 top-down flat lay with a 50mm lens on a seamless soft blush-pink paper surface, {FAR}. A soft blush-pink chunky knit sweater lies neatly folded flat in the lower half of the frame, front facing up, sleeves folded in. A woman\'s hand, early-to-mid 30s, natural short nails, enters from the lower right edge; the flat pads of her three middle fingers, held together, rest gently on the left chest area of the sweater, as if demonstrating a gentle circular self-check. A small pink satin awareness ribbon is pinned on the sweater. The product lies diagonally on the lower part of the sweater, below the hand. The top edge of the sweater is at about 50% of the frame height; the fingertips are at about 60%; the product is at about 72% of the frame height.',
    'The folded sweater is about 45 cm wide; an adult hand is about 18 cm long, so the capsule is about two thirds of the hand length; the ribbon is about 6 cm tall.',
    'Soft even overhead daylight, very soft shadows, real knit texture visible.',
    'Only the seamless soft blush-pink paper surface; no props, no pattern, no other objects, no people other than the single hand.',
    '50mm at f/8, perfectly top-down. Chunky knit wool texture, real skin texture on the hand with fine pores, satin ribbon, mirror chrome. Fine grain, airy soft-pink natural colour, calm caring mood.',
    'product standing upright, body, face, torso, nudity, extra hands, extra fingers, deformed hand, rings, nail polish, red ribbon, text on the sweater, logos'),
}

# v3 (2026-10-04): small shelf product had garbled label, lying flat-lay product looked pasted
out['ck_mirror2'] = p('A real editorial wellness photograph featuring ',
    'The product stands upright on the edge of a white bathroom counter in the lower-left foreground, about one metre closer to the camera than the woman, perfectly vertical, front label facing the camera, sharp and fully readable. Camera at chest height, straight on, as if the camera were her bathroom mirror.',
    f'Vertical 9:16 calm bathroom portrait with a 35mm lens, {FAR}. A woman in her early-to-mid 30s with shoulder-length dark hair tied back loosely, natural glowing skin and a calm, focused expression, wearing a plain soft blush-pink sports bra and high-waisted soft grey lounge trousers, stands a little behind the counter facing the camera doing a breast self-check in front of her mirror: her right arm is raised with her hand resting behind her head, and the flat pads of the three middle fingers of her left hand rest gently on the side of her chest just below the raised arm, over the sports bra. The pose is calm, natural and non-sexual. The top of her head is at about 50% of the frame height and her face sits between 52% and 60%; she stands right of centre. The white counter edge runs across the lower-left foreground; the product stands on it at the left with its top at about 62% and its base at about 78% of the frame height. She is cropped at the waist by the bottom edge.',
    'Because the product is much closer to the camera than the woman, it appears about as tall as her head in the photograph, while keeping its real 12 cm size.',
    'Soft diffused daylight from a window on the left, gentle shadows, natural skin tones.',
    'Only a plain warm white bathroom wall with very subtle large pale tiles at the lower edge; no mirror frame visible, no towels with text, no other people.',
    '35mm look at f/8 so both the product and the woman are sharp, real skin texture with visible pores, no heavy retouching, soft matte sports-bra fabric, matte white counter, mirror chrome. Fine grain, airy warm natural colour, calm empowering mood.',
    'nudity, bare breasts, cleavage focus, lingerie, sexualised pose, hand inside the bra, medical setting, sad expression, heavy makeup, plastic skin, extra fingers, deformed hands, red ribbon, tattoo, product on a shelf, tiny product')
out['ck_hand2'] = p('A real editorial still-life photograph featuring ',
    'The product stands upright on the pink table surface just left of the folded sweater, perfectly vertical, front label facing the camera and fully readable. Camera about 35 degrees above the table, looking down gently, straight on to the product.',
    f'Vertical 9:16 soft still life with a 50mm lens on a seamless soft blush-pink table and backdrop, {FAR}. A soft blush-pink chunky knit sweater lies neatly folded flat on the table, centred, front facing up, sleeves folded in, with a small pink satin awareness ribbon pinned on its chest. A woman\'s hand, early-to-mid 30s, natural short nails, enters from the right edge; the flat pads of her three middle fingers, held together, rest gently on the chest area of the sweater, as if demonstrating a gentle circular self-check. The product stands on the table just left of the sweater. The top edge of the sweater is at about 54% of the frame height; the product top is at about 60% and its base at about 76% of the frame height.',
    'The folded sweater is about 45 cm wide; an adult hand is about 18 cm long, so the capsule is about two thirds of the hand length; the ribbon is about 6 cm tall.',
    'Soft diffused daylight from the upper left, soft natural shadows, real knit texture visible.',
    'Only the seamless soft blush-pink table surface curving up into the backdrop; no props, no pattern, no other objects, no people other than the single hand.',
    '50mm at f/8. Chunky knit wool texture, real skin texture on the hand with fine pores, satin ribbon, mirror chrome. Fine grain, airy soft-pink natural colour, calm caring mood.',
    'product lying down, top-down view, body, face, torso, nudity, extra hands, extra fingers, deformed hand, rings, nail polish, red ribbon, text on the sweater, logos')

# v4 (2026-10-04): user — "more like a studio shoot, more professional; women younger and more beautiful"
def studio(ar, top, base):
    return p('A real high-end beauty campaign photograph shot on a styled studio set, featuring ',
    'The product stands upright on the white stone vanity top in the lower-left foreground, about one metre closer to the camera than the model, perfectly vertical, front label facing the camera, sharp and fully readable. Camera low at hip height, straight on. ',
    f'{ar} high-end beauty campaign on a styled studio set built as a minimal luxury bathroom, wide shot with a 35mm lens: smooth clean white plaster walls rising very high, a sculptural white stone vanity with a soft oval mirror behind the model, a neatly folded white towel and a small glass vase with a single pale-pink stem on the vanity. Everything is styled, clean and art-directed, clearly a produced campaign set rather than a real home. The tall empty white wall above her head fills the entire upper half of the frame for text to be added later, and her head is in the lower half of the frame. A strikingly beautiful woman in her late 20s with model-like features, luminous glowing skin, long sleek dark hair in a low ponytail and a calm, confident expression looking at the camera, wearing a matte blush-pink sports bra and matching high-waisted soft pink leggings, stands right of centre, framed from the knees up, body turned slightly in three-quarter view, doing a breast self-check from the side: her right arm is raised high with her right hand resting behind her head, and her left hand reaches across her body so that the flat pads of its three middle fingers press gently on the OUTER SIDE of her right breast, at the edge of the sports bra just below the raised armpit, clearly at the side of the chest near the armpit, NOT on the centre of the chest and NOT over the heart. The pose is elegant, calm and non-sexual. The white stone vanity runs across the lower-left foreground; the product on it has its top at about {top}% and its base at about {base}% of the frame height.',
    'The vanity is 85 cm high and the oval mirror is 70 cm tall. Because the product is much closer to the camera than the model, it appears about as tall as her head in the photograph, while keeping its real 12 cm size.',
    'Flawless professional studio lighting: a large octabox key light from the front left, a soft white fill from the right, a gentle rim light separating her from the backdrop, a soft natural shadow falling on the backdrop behind her.',
    'Only the styled white set: clean white plaster walls, the white stone vanity, the oval mirror, the folded towel and the single-stem vase; soft blush-pink accents only from the stem and her outfit; no clutter, no toiletries, no window, no other people.',
    'Shot on a medium-format camera, 35mm-equivalent lens at f/8 so both the product and the model are sharp. High-end beauty campaign finish: real skin texture with fine pores, polished but not plastic, glossy healthy hair, matte sports-bra fabric, honed white stone, smooth plaster, mirror chrome. Clean, bright, airy, premium editorial colour with soft blush accents.',
    'hand on the centre of the chest, hand over the heart, pledge pose, photography studio equipment visible, softbox, light stand, tripod, backdrop stand, messy real home bathroom, window, toiletries, clutter, casual snapshot look, plain coloured paper backdrop, older woman, plain or tired look, nudity, bare breasts, cleavage focus, lingerie, sexualised pose, hand inside the bra, medical setting, heavy makeup, plastic skin, extra fingers, deformed hands, red ribbon, tattoo, head in the upper half of the frame, close-up portrait, waist-up framing')
out['ck_studio'] = studio('Vertical 9:16', 64, 82)
out['ck_studio_sq'] = studio('Square 1:1', 68, 92)

# v5 (2026-10-04): user — product was oversized via foreground trick; keep true scale (same depth as model)
_s = out['ck_studio']
def realscale(x):
    x[2] = (x[2]
      .replace("The product stands upright on the white stone vanity top in the lower-left foreground, about one metre closer to the camera than the model,",
               "The product stands upright on the white stone vanity right beside the model, at exactly the same distance from the camera as she is,")
      .replace("The white stone vanity runs across the lower-left foreground; the product on it has its top",
               "The white stone vanity stands beside her at hip height on the left; the product on it, next to her hip, has its top")
      .replace("Because the product is much closer to the camera than the model, it appears about as tall as her head in the photograph, while keeping its real 12 cm size.",
               "The product is at the same depth as the model, so it appears at its true size: about two thirds of the length of her hand and much shorter than her forearm. It must look small next to her.")
      .replace("Negative: ", "Negative: product in the foreground, product closer to the camera than the model, giant product, product as tall as her head, "))
    return x
out['ck_set2'] = realscale(list(studio('Vertical 9:16', 66, 72)))
out['ck_set2_45'] = realscale(list(studio('Vertical 4:5', 70, 77)))
out['ck_set2_sq'] = realscale(list(studio('Square 1:1', 72, 80)))
json.dump(out, open('batch-13.json', 'w'), ensure_ascii=True)
for k, v in out.items():
    print(k, len(v[0] + v[2]))
