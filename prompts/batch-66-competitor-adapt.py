"""Batch 66 — adaptations of Grüns / Spoiled Child ads (user 2026-10-20, references in Figma beside each row).
A selfie (Have this? / Try this!), B PowerCycle gold bokeh (GLP-1 USERS), C DropOff gym still life (Don't wait till Jan 1st),
D-G problem illustrations (The Problem / The Solution). Text-free; copy goes in Figma. Mentions where noted."""
import json
WHITE = ("Every word printed on the product is pure white on the black stripe - on the coloured cap AND on the silver half; never black, grey or dark text.")
GEL = ("a translucent gel-serum - semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, smooth, slightly viscous, "
       "it holds a soft rounded bead and lets light pass through its edges")
INT = ("INTEGRATION\nThe product shares the scene's light direction, softness and colour temperature; the chrome shows the real reflections of this set; "
       "a real contact shadow and faint reflection where it touches a surface; same sharpness and grain as the rest of the frame; no outline or halo.")
FIN = ("PHOTOGRAPHIC FINISH\nUltra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. All product text must be perfectly legible, "
       "sharp, and accurate - no blurry or distorted letters. Fine natural grain. No text, no letters, no logos added to the scene (product labels only).")
NEG_P = ("pasted or composited look, cut-out edges, sticker look, halo, product lit differently, floating product, stubby chubby or wide bottle, "
         "black letters, dark or grey text on the product, warped label, extra products, text, headline, watermark, CGI, 3D render, cartoon")
X = {
 # A — no element
 'A_selfie': ["A real candid smartphone-style photo of a woman checking her tech-neck, natural and relatable.",
   "The woman is in her late 20s, pretty, natural everyday look, hair in a loose bun, wearing a simple grey t-shirt. Realistic skin with natural pores, no retouching. Exactly two arms.",
   "PRODUCT ORIENTATION\nNo product appears. She sits on a sofa looking down at her phone held at chest height, chin tucked down so soft horizontal creases are visible across the front of her neck (everyday tech-neck lines), her free hand lightly touching the side of her neck.",
   "COMPOSITION AND FRAMING\nVertical 3:4 frame, chest-up, slightly from the side so the neck and jawline are clearly visible in the centre of the frame. The face is partly turned down, not looking at the camera.",
   "SCALE\nReal human proportions.",
   "LIGHT AND SHADOW\nSoft natural window daylight from the side, gentle realistic shadows, true-to-life colour.",
   "BACKGROUND\nA bright, tidy modern living room softly out of focus behind her; neutral beige and white tones.",
   "PHOTOGRAPHIC FINISH\nLooks like a real iPhone photo: natural, unposed, slight grain. Ultra photorealistic, indistinguishable from a real photograph. No text, no letters, no logos.",
   "Negative: text, logos, products, bottles, exaggerated wrinkles, aged skin, heavy makeup, studio backdrop, distorted anatomy, extra fingers, more than two arms, plastic skin, CGI, 3D render, cartoon."],
 # B — mention ss-open-powercycle
 'B_pc_gold': ["Match the ELEMENT reference exactly for the open PowerCycle bottle and its glass dropper: shape, colours, chrome finish and label layout.",
   "A hand with natural nude manicure holds the glass dropper just above the open bottle. Realistic skin. Exactly one hand.",
   "PRODUCT ORIENTATION\nThe open PowerCycle bottle stands upright, label facing the camera; the dropper hovers a few centimetres above its neck and releases a single drop of " + GEL + ". PROPORTIONS ARE CRITICAL: the bottle is slim and tall, never stubby or wide. " + WHITE,
   "COMPOSITION AND FRAMING\nVertical 9:16 frame, camera straight on at bottle height. The bottle stands on a surface whose edge is at 66% of the frame height; the bottle occupies 46% to 66% of the frame height and the dropper with the hand just above it, centred; the top 40% is open warm golden bokeh with soft floating sparkles - clean space for text; the bottom 34% is the same calm out-of-focus golden surface, no objects.",
   "SCALE\nThe bottle is 14 cm tall and 4.5 cm wide; the dropper about 8 cm; the hand is far larger than the bottle. If in doubt make the product smaller, never bigger.",
   "LIGHT AND SHADOW\nWarm glowing golden backlight with soft sparkles and lens bokeh, a soft key on the bottle from the front left, glossy highlights on the chrome.",
   "BACKGROUND\nDreamy warm gold and champagne bokeh of out-of-focus lights and glitter, darker gold at the bottom, lighter at the top.",
   FIN, INT, "Negative: " + NEG_P + ", gold or yellow serum, coloured liquid, spray, mist, extra hands, distorted fingers."],
 # C — mention ss-dropoff
 'C_do_gym': ["Match the ELEMENT reference exactly for the DropOff tube: shape, colour, cap and label layout.",
   "No person appears; this is a premium sunlit wellness still life.",
   "PRODUCT ORIENTATION\nThe DropOff tube stands upright on its cap, label facing the camera, on a light stone floor beside a rolled peach yoga mat, a small peach dumbbell and a soft folded white towel; a single glossy bead of " + GEL + " on the floor in front of it. " + WHITE,
   "COMPOSITION AND FRAMING\nVertical 9:16 frame, camera at a low angle near floor level, straight on. The floor line is at 66% of the frame height; the tube stands centred and occupies 44% to 66% of the frame height, props beside it; the top 42% is a calm warm plaster wall with sunlight - clean space for a headline; the bottom 34% is calm empty stone floor in soft focus.",
   "SCALE\nThe tube is 20 cm tall; the yoga mat roll about 60 cm long and 12 cm thick; the dumbbell about 20 cm long. Real relative sizes.",
   "LIGHT AND SHADOW\nWarm golden-hour sunlight from the right through a window, long soft diagonal light beams and shadows on the wall, warm and energising.",
   "BACKGROUND\nWarm off-white plaster wall and light stone floor; nothing else.",
   FIN, INT, "Negative: " + NEG_P + ", people, hands, gym machines, clutter, dark background."],
}
ILL = ("A polished semi-realistic digital illustration in a clean modern beauty-advertising style - smooth painterly shading, soft gradients, gentle highlights, "
       "like a premium skincare infographic illustration.")
def P(subject, detail):
    return [ILL,
            "The person is a woman in her late 20s with smooth, natural-looking skin; tasteful, non-sexual, clinical-beauty look.",
            "PRODUCT ORIENTATION\nNo product appears. " + detail,
            "COMPOSITION AND FRAMING\nVertical 3:4 frame, a tight close-up of the area, centred, filling the frame.",
            "SCALE\nReal human proportions.",
            "LIGHT AND SHADOW\nSoft even beauty lighting with gentle shading that models the form.",
            "BACKGROUND\nA soft plain warm neutral background behind the subject.",
            "PHOTOGRAPHIC FINISH\nClean illustration finish, crisp edges, smooth gradients, high detail. No text, no letters, no labels, no icons, no logos.",
            "Negative: text, labels, icons, photo-realistic photograph, gore, exaggerated ageing, harsh wrinkles, nudity, products, cartoon chibi style, flat vector."]
X['D_ill_jaw'] = P('jaw', "Side profile of the lower face and neck: a soft, undefined jawline with a little fullness under the chin where the jaw meets the neck.")
X['E_ill_glow'] = P('glow', "Close-up of a cheek with a dull, uneven skin texture: slightly rough surface, a few enlarged pores and a lacklustre, matte tone.")
X['F_ill_hair'] = P('hair', "Top-down view of the crown of the head with dark brown hair: a widening centre part where the hair looks thinner and the scalp shows through.")
X['G_ill_body'] = P('body', "Side view of the outer thigh and hip in simple seamless white briefs, with a mild, everyday dimpled cellulite texture on the outer thigh.")
if __name__ == '__main__':
    open('/private/tmp/claude-501/p66.js', 'w').write('window.__p66=' + json.dumps(X) + ';"ok"')
    print(list(X))

# v3 (2026-10-20): B_pc_gold v1/v2 put the bottle in the bottom 35% (Story UI zone) - the model ignores "lower third" style
# percentages unless the product is also told to be SMALL. B3_pc = B_pc_gold with these two sections replaced (sent from the page):
B3_COMPOSITION = ("COMPOSITION AND FRAMING\nVertical 9:16 frame, camera straight on, pulled back so the bottle is SMALL in the frame. The bottle stands on a "
  "softly reflective golden surface whose front edge is at exactly 60% of the frame height; the bottle base sits at 58% of the frame height and its "
  "height is only 18% of the frame height (from 40% to 58%); the hand with the dropper is just above it, inside 25% to 40%. The top 24% is open warm "
  "golden bokeh - clean space for text; everything below 62% is the same calm out-of-focus golden surface and bokeh, no objects.")
B3_SCALE = ("SCALE\nThe bottle is 14 cm tall and 4.5 cm wide (height about 3 times its width); the dropper about 8 cm; the hand is far larger than the bottle. "
  "The bottle is small in the frame - never larger than 18% of the frame height.")
# A2_selfie = A_selfie with "a strikingly beautiful woman in her late 20s, model-like features" (A v1 read as 30s/plain - model rule).
