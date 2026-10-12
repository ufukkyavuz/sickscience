"""Batch 17 — ShapeShift competitor-driven push (2026-10-05). Statics (photographic) + Pixar-style animated keyframes.
Refs: StriVectin neck ads/IG cover, 'doctor sculpting a bust' neck ad, SpoiledChild A22 Pixar testimonial, Pixar doctor explainer."""
import json, importlib.util
spec = importlib.util.spec_from_file_location('b16', 'batch-16-build.py'); b16 = importlib.util.module_from_spec(spec)
import sys, io; _o = sys.stdout; sys.stdout = io.StringIO(); spec.loader.exec_module(b16); sys.stdout = _o
p, CAPS, WOMAN, NEG, LAB = b16.p, b16.CAPS, b16.WOMAN, b16.NEG, b16.LAB

out = {}
# ---------- photographic statics ----------
out['ss_sculpt'] = p('A real high-end fine-art still-life photograph in a sculptor\'s studio, featuring ', 'ss-shapeshift', CAPS,
    'The product stands upright on the top of the white plinth right beside the base of the bust, perfectly vertical, front label facing the camera.',
    'Vertical 9:16, 70mm lens, camera at plinth-top height. A life-size, smooth white plaster bust of a beautiful young woman\'s head, neck and shoulders, seen in a three-quarter profile, chin slightly lifted so her sharply sculpted, elegant jawline and long neck catch the light; the bust stands on a tall white plinth. On the plinth top beside the base of the bust stands the product, and a steel sculptor\'s chisel and a small wooden mallet lie flat next to it. The bust and product occupy the band between 38% and 80% of the frame height; the upper 34% of the frame is a calm, plain warm-white plaster wall for text added later.',
    'The bust\'s head is life-size, about 23 cm from chin to crown; the product is 12 cm tall, so it reaches roughly half the height of the head. The chisel is 20 cm long. The product is at the same distance from the camera as the bust.',
    'Soft directional window-like light from the upper left, one large source, sculpting deep soft shadows under the jawline of the bust; gentle fill from the right. Fine plaster dust hangs faintly in the light.',
    'A minimal, clean sculptor\'s studio: warm white plaster walls, a pale stone floor out of focus; no clutter, no other sculptures, no people.',
    'Shot on a medium-format camera, 70mm at f/8. Matte chalky plaster texture with fine tool marks, brushed steel, raw wood, mirror chrome. Fine grain, warm neutral gallery colour with a soft lilac accent from the product.',
    'human skin on the bust, painted bust, cracked or broken bust, marble veining, grey or dark studio, multiple busts, hands, people')

out['ss_profile'] = p('A real high-end beauty campaign photograph shot in a studio, featuring ', 'ss-shapeshift', CAPS,
    'She holds the product upright in one hand at collarbone height, front label facing the camera, fingers below the printed word so it stays fully readable.',
    f'Vertical 9:16, 85mm lens. Editorial close crop of {WOMAN}: we see her in pure side profile from the tip of her nose down to her collarbones, chin lifted, so the clean, sculpted line of her jaw and the long smooth neck form the hero of the image. One hand rests near her collarbone holding the product upright. Her jawline sits at about 48% of the frame height; the upper 36% of the frame is clean seamless backdrop for text added later; the lower part shows her shoulder and the product.',
    'The product is held in her hand, so it is exactly as far from the camera as she is: it is 12 cm tall, about two thirds of the length of her hand and a little shorter than her neck.',
    'Large soft key light from behind and slightly in front of her face, a crisp rim light tracing the jawline and neck, soft fill on the front of the neck. Every printed word on the product stays lit.',
    'A seamless backdrop in soft pale lilac-grey, smooth and even; no pattern.',
    'Medium-format beauty look, 85mm at f/8 so both the jawline and the product are sharp. Real skin with fine pores and a soft dewy sheen, polished but not plastic. Clean premium editorial colour.',
    'eye visible looking at camera, front-facing face, hair covering the neck, necklace, earrings, turtleneck, double chin')

out['ss_cover'] = p('A real fashion magazine cover photograph shot in a studio, featuring ', 'ss-shapeshift', CAPS,
    'She holds the product upright close to her jaw on one side, front label facing the camera, fingers below the printed word.',
    f'Vertical 9:16, 85mm lens. Fashion-magazine cover portrait of {WOMAN}, shot from the chest up, body turned three-quarters, face turned towards the camera with a confident, calm gaze and chin slightly lifted, her sculpted jawline clearly defined. She holds the product up beside her jaw at the same depth as her face. Her face is centred horizontally with her eyes at about 42% of the frame height; the upper 26% of the frame is plain backdrop for a masthead added later; the left and right edges of the lower half are calm backdrop for cover lines.',
    'The product is held in her hand at the same depth as her face; it is 12 cm tall, slightly shorter than her face from chin to hairline.',
    'Classic beauty-dish key light from the front above, soft fill from below, a subtle rim along the jaw; glossy fashion-cover finish.',
    'A seamless studio backdrop in a soft lilac, clean and even.',
    'Medium-format fashion look, 85mm at f/8. Real skin with fine pores, glossy healthy hair, polished but not plastic. Saturated clean premium colour.',
    'product held in front of her face, product bigger than her face, hands covering the jaw, heavy jewellery')

# ---------- Pixar-style animated keyframes ----------
TOON = ('a 3D animated-feature-film character in the style of a modern Pixar or Disney movie: a beautiful young woman in her late 20s with big expressive '
        'hazel eyes, long lashes, warm light-olive skin, a softly rounded face, glossy dark-brown hair tied in a high ponytail, small gold stud earrings, '
        'wearing a fitted lilac ribbed tank top')
PROD_TOON = ('THE PRODUCT IS NOT CARTOONISED: it keeps the exact shape, proportions, colours and printed label of the element reference, rendered as a real, '
             'precisely modelled chrome object lit by the same scene light. Capsule bottle with a rounded pill silhouette: top half glossy metallic violet '
             'chrome cap, bottom half mirror-polished silver chrome, vertical white printed text on a black stripe reading exactly \'ShapeShift\'. '
             'It is 12 cm tall: about two thirds of the length of her hand. Exactly one product; never enlarged, squashed, bent or melted.')
TFIN = ('High-end 3D animated feature-film still: soft subsurface skin shading, expressive eyes, cinematic lighting, rich soft colour, shallow depth of field. '
        'No text, captions, letters or logos added to the scene other than the product\'s own printed label.')
TNEG = ('empty grey band at the bottom, border, blank area, product in the foreground closer to the camera than her, cartoon product, redrawn product, oversized product, giant bottle, squashed or bent bottle, extra products, misspelled label, black or grey letters on '
        'the product, 2D flat cartoon, anime, photorealistic human, uncanny face, extra fingers, deformed hands, text, subtitles, watermark')
def t(scene, comp, light, back):
    body = f"""Character: {TOON}. Keep this exact character design in every frame.

PRODUCT
{PROD_TOON}

COMPOSITION AND FRAMING
Vertical 9:16. {comp} The scene is full-bleed and continues all the way to the bottom edge of the frame (the vanity, bed or floor fills the lower part); no empty band, no border, no blank area. Everything fits inside the frame.

LIGHT
{light}

BACKGROUND
{back}

FINISH
{TFIN}

Negative: {TNEG}"""
    return ['A still frame from a 3D animated feature film. ' + scene + ' The product in the scene is ', 'ss-shapeshift', ' \n\n' + body]

BATH = ('a bright, stylish animated-film bathroom: soft white walls, a rounded mirror with warm vanity bulbs, a white stone vanity with a folded towel and a small lilac flower in a vase')
out['toon_mirror'] = t('She stands at her bathroom mirror in three-quarter view, lifting her chin and pinching the soft skin under her jaw with her fingertips, eyebrows raised in a frustrated, slightly comic pout.',
    'Medium shot from the waist up, her face at about 32% to 48% of the frame height, the mirror behind her on the left; the product stands on the vanity near her hand, at the same depth as she is.',
    'Warm vanity bulb light from the mirror plus soft daylight; gentle rim light on her hair.', BATH + '.')
out['toon_find'] = t('She sits cross-legged on a cosy bed holding the product up at chest height in one hand, looking at it with wide, delighted, curious eyes and a little hopeful smile; a phone lies on the duvet beside her.',
    'Medium shot, her face at about 28% to 44% of the frame height; the product in her hand at about 50% height, its front label with the printed name turned towards the camera and fully readable.',
    'Soft warm morning light from a window on the right, gentle fill.', 'A bright animated-film bedroom with white bedding, lilac cushions and a soft blurred window.')
out['toon_apply'] = t('She stands at the bathroom vanity with her eyes gently closed and chin lifted, the flat fingers of both hands sweeping upward along both sides of her jawline, a serene, blissful smile; the product stands on the vanity beside her.',
    'Medium close-up from the chest up, her face at about 26% to 46% of the frame height; the product stands upright on the vanity right beside her elbow at exactly the same distance from the camera as she is, so it looks small — about as tall as her hand is long — front label facing the camera.',
    'Soft warm vanity light, glowing highlights along her jaw and neck.', BATH + '.')
out['toon_glow'] = t('Two weeks later: she takes a confident selfie with a phone held up in one hand, chin lifted, a beautifully defined, sculpted jawline, a big radiant smile; her other hand holds the product up beside her face.',
    'Medium shot from the waist up, her face at about 28% to 44% of the frame height; the product in her hand at the same depth as her face, front label facing the camera.',
    'Bright, glowing golden-hour light with soft lens bloom and a few gentle sparkles in the air.', 'A sunny animated-film city rooftop terrace with soft blurred greenery and a pale sky.')


# v2 statics (2026-10-05): subject was placed too high; push down with tall-room framing
import copy
def low(k, find, rep, extra_neg):
    x = copy.deepcopy(out[k]); x[2] = x[2].replace(find, rep).replace('Negative: ', 'Negative: ' + extra_neg + ', '); out[k + '2'] = x
low('ss_sculpt', 'The bust and product occupy the band between 38% and 80% of the frame height; the upper 34% of the frame is a calm, plain warm-white plaster wall for text added later.',
    'Photographed from far back in a tall studio with a very high ceiling: the top of the bust\'s head is at 46% of the frame height and the plinth top at about 76%; the entire upper 44% of the frame is a calm, plain warm-white plaster wall for text added later.',
    'bust in the upper half of the frame, head near the top edge')
low('ss_profile', 'Her jawline sits at about 48% of the frame height; the upper 36% of the frame is clean seamless backdrop for text added later; the lower part shows her shoulder and the product.',
    'Photographed from further back in a tall studio: the top of her head is at 40% of the frame height, her jawline at about 58%, her collarbones at about 76%; the entire upper 38% of the frame is clean empty seamless backdrop for text added later.',
    'head near the top edge, head cropped at the top')
low('ss_cover', 'Her face is centred horizontally with her eyes at about 42% of the frame height; the upper 26% of the frame is plain backdrop for a masthead added later; the left and right edges of the lower half are calm backdrop for cover lines.',
    'Photographed from further back in a tall studio: the top of her head is at 34% of the frame height and her eyes at about 44%; the entire upper 32% of the frame is plain empty backdrop for a masthead added later; the left and right edges of the lower half are calm backdrop for cover lines.',
    'head near the top edge, head cropped at the top')

for k in ['toon_mirror','toon_find','toon_apply','toon_glow']: out[k.replace('toon_','toon2_')] = out[k]

# v3 toon (2026-10-05): product on vanity still read too big — push it back, behind her forearm
for k in ['toon2_mirror','toon2_apply']:
    x = copy.deepcopy(out[k])
    x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\nThe product stands FURTHER BACK on the vanity, near the wall behind her forearm, so it looks small: clearly shorter than her hand, about one third of the height of her head. ')
    x[2] = x[2].replace('Negative: ', 'Negative: product taller than her hand, product at the front edge of the vanity, ')
    out[k.replace('toon2_','toon3_')] = x

# v4 (2026-10-05): user — "ürün doğru değil": bottle came out stubby/wide. Real ShapeShift is slim: 12 cm x 3.5 cm (height = 3.4 x width).
PROP = ("PROPORTIONS ARE CRITICAL: the bottle is SLIM AND TALL like a slender lipstick-shaped capsule — its height is 3.4 times its width "
        "(12 cm tall, only 3.5 cm wide, about as wide as two fingers); the glossy violet cap is the upper half and the mirror-silver base the lower half, "
        "with straight parallel sides and fully rounded ends. Never stubby, chubby, squat, wide or barrel-shaped. ")
PNEG = 'stubby bottle, chubby or wide bottle, squat capsule, barrel-shaped bottle, bottle wider than three fingers'
for k in ['ss_sculpt2','ss_profile2','ss_cover2','toon3_mirror','toon2_find','toon3_apply','toon2_glow']:
    x = copy.deepcopy(out[k])
    if 'PRODUCT\n' in x[2]: x[2] = x[2].replace('PRODUCT\n', 'PRODUCT\n' + PROP, 1)
    else: x[2] = x[2].replace('PRODUCT ORIENTATION\n', 'PRODUCT ORIENTATION\n' + PROP, 1)
    x[2] = x[2].replace('Negative: ', 'Negative: ' + PNEG + ', ')
    out['v4_' + k.split('_',1)[1].rstrip('2')] = x

# v5 find (2026-10-05): bottle in hand still bigger than her hand
x = copy.deepcopy(out['v4_find'])
x[0] = x[0].replace('holding the product up at chest height in one hand', 'holding the small product up at chest height between her thumb and fingers')
x[2] = x[2].replace('PROPORTIONS ARE CRITICAL:', 'SIZE: the bottle is SMALL in her hand — clearly shorter than her hand, about two thirds of her hand length, her fingers wrap around its lower half and the label stays readable. PROPORTIONS ARE CRITICAL:')
x[2] = x[2].replace('Negative: ', 'Negative: bottle longer than her hand, big bottle, ')
out['v5_find'] = x

# v5 glow: v4 came out too thin with a short cap
x = copy.deepcopy(out['v4_glow'])
x[2] = x[2].replace('PROPORTIONS ARE CRITICAL:', 'SIZE AND SHAPE: the violet cap and the silver base are EXACTLY EQUAL in length (cap = upper half); the capsule is about as wide as her two fingers and clearly shorter than her hand. PROPORTIONS ARE CRITICAL:')
x[2] = x[2].replace('Negative: ', 'Negative: short cap, thin stick-like tube, pen-like bottle, ')
out['v5_glow'] = x

# v6 statics: v2/v4 drifted (male torso, printed magazine text, stubby bottle)
for k, extra_pos, extra_neg in [
    ('v4_sculpt', 'The bust is a CLASSICAL FEMALE PORTRAIT BUST — only the head, long neck and the top of the shoulders of a serene young woman, like a Greek goddess bust; ', 'torso, male body, chest, abdomen, full figure, clutter, sketches on the wall, multiple sculptures'),
    ('v4_profile', '', 'printed text, letters, logos in the scene'),
    ('v4_cover', 'This is the clean photograph only, BEFORE any magazine text is added: ', 'magazine masthead, cover lines, printed words, letters, titles, any text in the image, metallic top'),
]:
    x = copy.deepcopy(out[k])
    x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\n' + extra_pos, 1)
    x[2] = x[2].replace('Negative: ', 'Negative: ' + extra_neg + ', ')
    out['v6_' + k.split('_',1)[1]] = x

# v6 glow: hand-held bottle keeps distorting; standing bottles render correctly -> put it on the terrace table
x = copy.deepcopy(out['v4_glow'])
x[0] = x[0].replace('her other hand holds the product up beside her face.', 'her other hand rests on her hip; the product stands upright on the small round terrace table beside her elbow.')
x[2] = x[2].replace("the product in her hand at the same depth as her face, front label facing the camera.", "the product stands upright on a small round white table right beside her elbow, at exactly the same distance from the camera as she is, so it looks small — shorter than her hand — front label facing the camera.")
x[2] = x[2].replace('Negative: ', 'Negative: product in her hand, extra bottles, cosmetics in the foreground, ')
out['v6_glow'] = x

# 1:1 versions for Square (crop could not keep the product in frame)
for k in ['v6_profile','v6_cover']:
    x = copy.deepcopy(out[k])
    x[2] = x[2].replace('Vertical 9:16', 'Square 1:1')
    x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\nSQUARE 1:1 FRAME, photographed from further back: the whole product and her hand are fully inside the frame with space below them; the top of her head is at about 24% of the frame height; the upper 22% of the frame is empty backdrop for text. ', 1)
    out[k + '_sq'] = x

# ---------- countdown concepts (user 2026-10-05: first order 15% off, countdown animated later in Figma) ----------
CD_PROD = PROP + 'The product is 12 cm tall, shown at its true size; never enlarged.'
out['cd_hourglass'] = p('A real high-end studio product photograph featuring ', 'ss-shapeshift', CAPS,
    'The product stands upright on a frosted lilac acrylic block, perfectly vertical, front label facing the camera. Camera at product height, straight on. ' + CD_PROD,
    'Vertical 9:16 minimal still life photographed from far back in a tall studio: the product stands on the right of centre and a tall elegant glass hourglass with fine pale-lilac sand stands on the left, sand visibly streaming through the neck and a soft mound in the lower bulb. The objects sit in the band between 50% and 82% of the frame height; the entire upper 46% of the frame is clean empty backdrop for a headline and a countdown timer added later.',
    'The hourglass is 22 cm tall, almost twice the height of the product; the acrylic block is 5 cm tall.',
    'Large soft key light from the upper left, a thin strip light on the right edge drawing clean vertical highlights on the violet chrome and the glass; soft real contact shadows.',
    'Only a seamless backdrop in a smooth gradient from soft white at the top to pale lilac at the bottom; no pattern, no horizon line.',
    '100mm at f/11. Mirror chrome and clear glass with true reflections, fine sand grains, frosted acrylic. Fine grain, clean premium colour.',
    'clock face numbers, digits, people, hands, flowers, extra products, stubby bottle, ' + PNEG)
out['cd_flipclock'] = p('A real high-end studio product photograph featuring ', 'ss-shapeshift', CAPS,
    'The product stands upright on the white surface beside the clock, perfectly vertical, front label facing the camera. Camera slightly above product height. ' + CD_PROD,
    'Vertical 9:16 minimal still life: a large retro white desk flip clock with three wide blank flip-card windows (completely blank white cards, NO numbers printed on them) stands in the centre, and the product stands just right of it. The objects sit in the band between 46% and 80% of the frame height; the upper 40% of the frame is clean empty lilac backdrop for a headline added later.',
    'The flip clock is 26 cm wide and 14 cm tall; the product is 12 cm tall, a little shorter than the clock.',
    'Soft directional studio light from the upper left, gentle fill, soft real contact shadows on the white surface.',
    'A seamless soft lilac backdrop meeting a matte white surface with a smooth curve; no pattern.',
    '85mm at f/11. Glossy white plastic, mirror chrome, matte surface. Fine grain, clean premium colour.',
    'numbers on the clock, digits, letters on the clock, time displayed, people, hands, extra products, ' + PNEG)
xt = copy.deepcopy(out['v6_glow'])
xt[0] = 'A still frame from a 3D animated feature film. In her bright bathroom, she points excitedly upward with one hand at the empty space above her head, mouth open in a delighted gasp, eyes wide with excitement, as if a big countdown just appeared; the product stands upright on the vanity beside her elbow. The product in the scene is '
xt[2] = xt[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\nShe stands in the LOWER half of the frame: the top of her head is at about 46% of the frame height; the entire upper 42% of the frame is a calm, softly lit plain bathroom wall for a countdown added later. ', 1)
xt[2] = xt[2].replace('A sunny animated-film city rooftop terrace with soft blurred greenery and a pale sky.', 'A bright, stylish animated-film bathroom: soft white walls, a white stone vanity, a small lilac flower in a vase.')
xt[2] = xt[2].replace("the product stands upright on a small round white table right beside her elbow", "the product stands upright on the white stone vanity right beside her elbow")
xt[2] = xt[2].replace('Medium shot from the waist up, her face at about 28% to 44% of the frame height; ', 'Medium-wide shot from the hips up, photographed from further back; ').replace('Bright, glowing golden-hour light with soft lens bloom and a few gentle sparkles in the air.', 'Bright soft morning light from a window, warm vanity bulbs, a few playful sparkles around her pointing hand.')
out['cd_toon'] = xt

x = copy.deepcopy(out['cd_hourglass'])
x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\nSIZE IS CRITICAL: the product is SMALL and SLIM — exactly HALF the height of the hourglass, its top reaching only the narrow neck of the hourglass. ', 1)
x[2] = x[2].replace('Negative: ', 'Negative: product as tall as the hourglass, product taller than the hourglass neck, ')
out['cd_hourglass2'] = x

for ar, tag in [('4:5','45'),('1:1','sq')]:
    x = copy.deepcopy(out['cd_toon'])
    x[2] = x[2].replace('Vertical 9:16', ar.replace(':','x') + ' frame').replace('the top of her head is at about 46% of the frame height; the entire upper 42%', 'the top of her head is at about 40% of the frame height; the entire upper 36%')
    x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\n' + ('Horizontal-ish 4:5 portrait frame' if tag=='45' else 'Square 1:1 frame') + ', photographed from further back so her hips, the vanity and the whole product are fully inside the frame. ', 1)
    out['cd_toon_' + tag] = x

# v2 video beats (2026-10-05: user wants a livelier, funnier video)
base = out['cd_toon']
def beat(scene, comp):
    x = copy.deepcopy(base)
    x[0] = 'A still frame from a 3D animated feature film. ' + scene + ' The product in the scene is '
    i = x[2].index('COMPOSITION AND FRAMING\n'); j = x[2].index('\n\nLIGHT')
    x[2] = x[2][:i] + 'COMPOSITION AND FRAMING\nVertical 9:16. ' + comp + ' The product stands upright on the white stone vanity beside her, at exactly the same distance from the camera as she is, so it looks small — shorter than her hand — front label facing the camera. The scene is full-bleed to the bottom edge; no empty band. Everything fits inside the frame.' + x[2][j:]
    return x
out['beat_shock'] = beat('In her bright bathroom she holds up her phone and stares at a selfie on its screen (we see the back of the phone) with a hilarious over-the-top cartoon horror face: eyes huge, eyebrows shooting up, teeth clenched in a comic grimace, one hand slapped against her cheek.',
    'Medium close-up from the chest up, her face at about 30% to 50% of the frame height, the phone on the left side of the frame.')
out['beat_dance'] = beat('In her bright bathroom she does a joyful little victory dance: one arm thrown up in the air, hips swaying, ponytail flying, eyes closed with a huge happy grin, a few playful sparkles around her.',
    'Medium-wide shot from the knees up, photographed from further back, her head at about 20% to 34% of the frame height.')
json.dump(out, open('batch-17.json', 'w'), ensure_ascii=True)
for k, v in out.items(): print(k, v[1], len(v[0] + v[2]))
