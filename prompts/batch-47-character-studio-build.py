"""Batch 47 (2026-10-15): SickScience studio campaign stills with the deep-skin character elements (batch-46 v3/v4).
One 9:16 master per creative (Feed/Square are crops). In the web composer the element mentions are typed first,
then this body is pasted; prompts are single-line because a newline submits the composer."""
import json

CAPS = ('PROPORTIONS ARE CRITICAL: every capsule bottle is SLIM AND TALL, its height about 3.4 times its width (PowerCycle about 3.1 times), '
        'the coloured metallic chrome cap is exactly the upper half and the mirror-polished silver chrome base the lower half, straight parallel sides, '
        'fully rounded pill ends; never stubby, chubby, squat or wide. ')
WHITE = ('LABEL TEXT: every word printed on the products is PURE WHITE on the black stripe, on the coloured cap and on the silver half alike; '
         'never black, grey or dark letters; NetWork, if present, is spelled with a capital N and a capital W. ')
STUDIO = ('CAMERA: Phase One XF IQ4 150MP, Schneider Kreuznach 80mm LS lens at f/11, ISO 50, 1/160s, camera at face height, straight-on; deep depth of field so her face, hair, hands and the product are all tack-sharp. '
          'LIGHTING: Profoto D2 key light in a 150cm Deep White octabox 45 degrees camera-left slightly above eye level; two 30x180cm strip boxes behind her left and right as rim lights; '
          'white V-flat fill camera-right; the seamless paper backdrop lit separately by two heads with a soft falloff. Crisp catchlights in both eyes, clean chrome highlights. ')
LAYOUT = ('COMPOSITION: full-bleed VERTICAL 9:16 photograph, edge to edge, no borders. She is framed from the chest up; her face and the product sit side by side in the SAME band, '
          'between 38% and 72% of the frame height; the UPPER 32% is clean empty backdrop for text added later (only the top of her hair may reach into it); '
          'her face is in the central 60% of the width. Exactly two arms and two hands, natural relaxed fingers. ')
FINISH = ('FINISH: high-end beauty campaign photograph, real skin texture with visible pores, true-to-life skin tone never ashy or lightened, fine grain, punchy premium colour. '
          'All product text perfectly legible, sharp and accurate. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. '
          'No text, letters, numbers or logos added to the scene other than the products\' own printed labels. '
          'INTEGRATION: the product was physically in her hand when this was shot: same light direction and colour temperature, its chrome reflects the coloured backdrop and her skin, '
          'real contact shadows from her fingers, same focus and grain as the rest of the photograph, no outline, no halo. ')
NEG = ('Negative: black, grey or dark letters on the products, extra products, redrawn or invented product, misspelled text, extra text, oversized product, product pushed towards the camera, '
       'bottle bigger than her face, stubby or chubby or wide squat bottle, blurred product, deformed fingers, extra fingers, extra arms, different face from the reference, '
       'lightened or ashy skin, older woman, plastic skin, heavy retouching, black clothing, white clothing, shallow depth of field, bokeh, CGI, 3D render look, HDR glow, '
       'pasted-on look, halo, watermark')
GEL = ('a translucent gel-serum, semi-transparent with a soft milky haze, neither opaque white cream nor water-clear, glossy')

def p(who, products, orient, scene, scale, backdrop, neg=''):
    return (f'A real high-end beauty campaign photograph shot in a professional photo studio. {who} '
            f'Preserve the exact identity of the product{"s" if products > 1 else ""}: proportions, construction, colours and printed branding exactly as the element shows; '
            f'use the element for identity only, do not redraw it. Exactly {products} product{"s" if products > 1 else ""}, no extra product. {CAPS}'
            f'PRODUCT ORIENTATION: {orient} Front label facing the camera, text vertical. No fisheye, no wide-angle distortion. '
            f'{LAYOUT}SCENE: {scene} SCALE: {scale} Keep real proportions; if in doubt make the product smaller, never bigger. '
            f'{STUDIO}BACKGROUND: {backdrop} {FINISH}{WHITE}{NEG}{", " + neg if neg else ""}.')

HAND12 = ('The bottle is held at the SAME distance from the camera as her face; it is 12 cm tall, about two thirds of the length of her hand '
          'and about 0.6 times her chin-to-hairline height.')
HAND14 = ('The bottle is held at the SAME distance from the camera as her face; it is 14 cm tall and 4.5 cm wide, about 0.7 times her chin-to-hairline height, '
          'slightly taller than eyebrows-to-chin.')
WHO = 'The woman is the first element reference: keep her exact face, features, hair and skin tone; she is in her mid 20s, slim and beautiful.'

J = {
 'b47_pc_kiara': ('kiara-v3', ['ss-powercycle'], p(WHO, 1,
    'She holds the closed PowerCycle bottle (second element reference) upright on her open palm just beside her temple, fingers relaxed.',
    'She wears a solid emerald-green fine-knit top. With the fingertips of her other hand she lightly touches her front hairline at the edge of her big rounded afro, '
    'chin slightly lifted, confident genuine smile, eyes to the camera. Her edges look soft, full and healthy.',
    HAND14, 'Seamless saturated lime-green paper backdrop.')),
 'b47_nw_ama': ('ama-v3', ['ss-network'], p(WHO, 1,
    'She holds the closed NetWork bottle (second element reference) upright on her open palm right next to her cheek, fingers relaxed.',
    'She wears a solid tomato-red ribbed top. She gives a playful wink and a wide bright smile, head tilted slightly toward the bottle; '
    'her deep skin looks even-toned, smooth and luminous with a healthy glow on the cheekbones.',
    HAND12, 'Seamless warm coral-red paper backdrop.', 'closed eyes on both sides')),
 'b47_ss_leila': ('leila-v4', ['ss-shapeshift'], p(WHO, 1,
    'She holds the closed ShapeShift bottle (second element reference) upright on her open palm just beside her jaw, fingers relaxed.',
    'She wears a solid lilac fine-knit top. With the fingertips of her other hand she sweeps upward along her jawline, chin lifted, '
    'big genuine smile, eyes to the camera; a very subtle glossy sheen on her jawline and neck.',
    HAND12, 'Seamless saturated violet paper backdrop.', 'pinching, hand covering the mouth')),
 'b47_duo_nia': ('nia-v3', ['ss-shapeshift', 'ss-powercycle'], p(WHO, 2,
    'She holds the closed ShapeShift bottle (second element reference) upright on her left open palm beside her jaw, and the closed PowerCycle bottle (third element reference) '
    'upright on her right open palm beside her temple, one product on each side of her face.',
    'She wears a solid hot-magenta fine-knit top. She laughs with her head slightly tilted, joyful and confident, eyes to the camera; her long sleek hair falls over her shoulders.',
    'Both bottles are held at the SAME distance from the camera as her face. ShapeShift is 12 cm tall, about 0.6 times her chin-to-hairline height; '
    'PowerCycle is 14 cm tall and wider, about 0.7 times her chin-to-hairline height, so PowerCycle is visibly a little taller and wider than ShapeShift.',
    'Seamless soft blush-pink paper backdrop.')),
 'b47_do_zara': ('zara-v3', ['ss-dropoff'], p(WHO, 1,
    'She holds the DropOff tube (second element reference, a matte cobalt-blue squeeze tube with white vertical text, NOT a capsule) upright in one hand at shoulder height beside her face.',
    f'She wears a solid cobalt-blue sleeveless ribbed top. Her other arm is bent with a glossy ribbon of {GEL} on the back of her upper arm that she smooths in; '
    'she laughs with her head slightly tilted, confident and joyful.',
    'The tube is held at the SAME distance from the camera as her face; it is about 20 cm tall, about as tall as her face.',
    'Seamless soft sky-blue paper backdrop.', 'capsule-shaped DropOff, chrome DropOff, bare torso, swimwear')),
}
json.dump(J, open('batch-47.json', 'w'), ensure_ascii=True)
for k, (c, pr, t) in J.items(): print(k, c, pr, len(t))

# 2026-10-15 run notes (the prompts actually sent were patched in the composer):
# - WHITE variant: "pure-white <knit/ribbed> top" + "Seamless BRIGHT PURE-WHITE (not grey) paper studio backdrop";
#   chrome "reflects the white studio ... crisp dark edge lines from black flags"; negatives swap white clothing -> coloured clothing/backdrop.
# - SCALE anchored to the face (works better than cm alone): base on palm at chin level, SS/NW top at eye level,
#   PC top at eyebrows, "clearly shorter than her face". PowerCycle still comes out ~0.9-1.0x face height (target ~0.75).
# - Kiara/PC also needed "MEDIUM SHOT from further back ... face is about one eighth of the frame height".
# Picks: _calisma/batch-47-characters/secim/ (renkli_* and beyaz_*).
