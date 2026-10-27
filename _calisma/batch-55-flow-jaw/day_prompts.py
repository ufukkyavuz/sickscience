"""Day-by-day stills (Higgsfield web, Nano Banana Pro 2K Unlimited). Identity ref = before.png (Leila, untreated jaw).
Each day = a different real-life moment (hair, top, light, room) + jawline a touch more defined than the day before. Realistic, modest."""
import json
GEL = ("a translucent gel-serum — semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, smooth, slightly viscous, "
       "it holds a soft rounded bead and lets light pass through its edges")
DAYS = [
 ('d01', 'early morning in a bright white bathroom, soft window light from the left, hair up in a messy claw clip, white waffle robe',
  'two fingertips placing a small bead of the gel-serum on her jawline under the ear',
  'exactly as in Image 1: a soft jaw angle with a slight fullness under the chin, matte tired skin'),
 ('d03', 'evening at home, warm table-lamp light from the right, hair down and tucked behind the ear, black ribbed tank top',
  'smoothing the gel-serum upward along her jawline with two fingers',
  'almost the same as Image 1, the jaw only a hair firmer, skin a little fresher'),
 ('d05', 'daytime by a large window, cool natural daylight, hair in a low bun, heather-grey t-shirt',
  'a glossy bead of the gel-serum on her fingertips, about to smooth it along the jaw',
  'very slightly more defined than Image 1: the jaw angle a little cleaner, still a touch of softness under the chin'),
 ('d07', 'bathroom mirror light after a shower, hair wrapped in a white towel, bare shoulders',
  'stroking the gel-serum up the side of her neck toward the jaw with her fingertips',
  'a little more defined: cleaner jaw line, less fullness under the chin, skin dewy'),
 ('d09', 'morning in the bedroom, golden side light, sleek high ponytail, white tank top',
  'tracing one finger along her jawline from chin to ear, a thin dewy sheen of gel-serum on the skin',
  'noticeably more defined: a crisper jaw angle and a tighter line under the chin, natural and believable'),
 ('d11', 'evening, soft warm light, hair down over one shoulder, silk pajama shirt in champagne',
  'massaging the gel-serum under her chin with the backs of her fingers',
  'clearly defined jaw and smooth neck, only the faintest softness left under the chin'),
 ('d14', 'bright clean studio-like bathroom, even soft daylight, hair down, sleek and glossy, white t-shirt',
  'fingertips resting lightly on her jawline, gentle confident smile',
  'the most defined of the series: crisp sculpted-looking jawline, taut smooth neck, glowing dewy skin — still the same natural young woman, not altered beyond realism'),
]
def prompt(scene, action, jaw):
    return (
 "Image 1 is the identity reference. Keep the exact same woman as Image 1 — same face, same freckles across the nose and cheeks, same brown eyes, same eyebrows, same lips, "
 "same long straight black hair, same skin tone; a strikingly beautiful woman in her late 20s with model-like features. This is a new photograph from a different day of her jawline routine.\n\n"
 f"SCENE: {scene}.\n\nPOSE AND ACTION: three-quarter profile facing left, chin slightly lifted so the jaw and neck are clearly visible; {action}. Exactly one hand visible, five fingers, natural nails.\n\n"
 f"JAWLINE AND SKIN: {jaw}.\n\nTEXTURE: the product on her skin is {GEL}. No bottle, pump or packaging in frame.\n\n"
 "COMPOSITION AND FRAMING: vertical 9:16 close-up from the eyebrows to the collarbone, face in the upper middle, jaw and neck in the centre of the frame; handheld beauty-vlog feel, slightly different camera distance than Image 1.\n\n"
 "PHOTOGRAPHIC FINISH: shot on a full-frame camera with an 85mm lens at f/2.8, ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail, real skin texture with visible pores, "
 "natural colour, no retouching plastic look. No text, no letters, no logos added to the scene.\n\n"
 "Negative: different person, different face, aged face, heavier face, fine lines, dramatic transformation, opaque white cream, thick white lotion, water-clear liquid, coloured serum, bottle, product packaging, "
 "extra fingers, extra hands, deformed hands, text, watermark, plastic skin, CGI.")
if __name__ == '__main__':
    print(json.dumps([[d, prompt(s, a, j)] for d, s, a, j in DAYS]))
