"""Batch 71 — reference-faithful alternatives (user 2026-10-21).
R1 ShapeShift pile on a white cornered studio cyc, direct on-camera flash (Grüns "We're sorry." layout: big headline + paragraph on top).
R2 PowerCycle hero on flat pale background, big and tilted (Grüns quote ad: quote top-left, product big right).
R3 DropOff on white with its PDP ingredients (pineapple stem / bromelain, coffee beans for caffeine), long hard shadows (Grüns stat-callout ad).
R4 PowerCycle small at bottom right on flat cream (Grüns "That's menopause" emoji grid).
R5 NetWork vampire: gothic woman at an antique mirror, Halloween (SpoiledChild "The older I get, the younger I look.")."""
import json
CAP = ("PROPORTIONS ARE CRITICAL: a slim, tall capsule with fully rounded ends at the top AND the bottom, height 3.4 times its width; the "
       "coloured chrome cap is exactly the upper half and the mirror-silver body exactly the lower half. A narrow vertical BLACK stripe runs the "
       "full height of the bottle over both halves, and every word ('SickScience' on the cap, the product name on the silver half) is printed "
       "vertically in pure white on that black stripe - never text directly on the chrome, never black or grey letters. Never stubby, chubby, "
       "squat or flat-bottomed.")
TUBE = ("The DropOff tube is a cobalt-blue squeeze tube about 20 cm tall standing on its round cobalt screw cap with a flat crimp at the top; "
        "vertical pure white text 'SickScience' and 'DropOff'; never black or grey text.")
GEL = "a translucent gel-serum - semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, slightly viscous"
FIN = ("PHOTOGRAPHIC FINISH\nUltra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. All product text must be "
       "perfectly legible, sharp, and accurate - no blurry or distorted letters. No text, no letters, no logos added to the scene (product labels only).")
INT = ("INTEGRATION\nThe products share the scene's light; the chrome shows the real reflections of this set; real contact shadows; same sharpness and "
       "grain everywhere; no outline or halo.")
NEG = ("Negative: pasted or composited look, cut-out edges, sticker look, halo, floating product, stubby chubby wide or flat-bottomed bottle, text "
       "printed directly on chrome, missing black stripe, black letters, dark or grey text on the product, 'Network' with a lowercase w, warped "
       "label, text, headline, watermark, CGI, 3D render, cartoon, illustration")
X = {
 'R1_ss_pile': ["Match the ELEMENT reference exactly for the ShapeShift bottles: shape, colours, chrome finish and label layout.",
   "No person appears; a bold, playful product-pile photograph like a fashion flash shoot.",
   "PRODUCT ORIENTATION\nA casual pile of about nine closed ShapeShift bottles heaped on the floor in the corner of a white studio - some standing, some lying at angles, some leaning on each other, labels mostly facing the camera. " + CAP,
   "COMPOSITION AND FRAMING\nVertical 9:16 frame, camera slightly above, straight on into the corner where the white floor meets the white wall (a crisp visible corner line, not an infinity cove). The pile sits between 52% and 80% of the frame height, centred. The top 48% is clean white wall - space for a headline and a paragraph.",
   "SCALE\nEach bottle is 12 cm tall and 3.5 cm wide; the pile is about 40 cm wide. Real proportions.",
   "LIGHT AND SHADOW\nDirect on-camera flash: bright, crisp, slightly hard light, specular hot spots on the chrome, a sharp dark flash shadow cast behind the pile onto the wall and floor; the room edges slightly darker - the raw editorial flash look.",
   "BACKGROUND\nA plain white painted studio wall and white floor meeting in a sharp corner; nothing else.",
   FIN + " Slight film grain, editorial flash photography.", INT, NEG + ", other products, people, hands, coloured background, soft diffuse light."],
 'R2_pc_hero': ["Match the ELEMENT reference exactly for the PowerCycle bottle: shape, colours, chrome finish and label layout.",
   "No person appears; a bold, graphic product hero photograph.",
   "PRODUCT ORIENTATION\nOne closed PowerCycle bottle, tilted about 20 degrees to the left, standing on its rounded base with a soft shadow, label facing the camera and fully readable. " + CAP,
   "COMPOSITION AND FRAMING\nVertical 9:16 frame, camera straight on. The bottle is large and occupies the right half of the frame: its centre at 62% of the width and 62% of the height, its height about 45% of the frame height, fully inside the frame with margin. The left half and the top 35% are clean, flat, empty background for big text.",
   "SCALE\nThe bottle is 14 cm tall and 4.5 cm wide, photographed close; proportions exactly as real.",
   "LIGHT AND SHADOW\nBright soft studio key light from the upper left, crisp highlights on the green and silver chrome, one soft grounded shadow.",
   "BACKGROUND\nA flat, seamless, pale butter-cream backdrop (#FFF6DA), completely even; nothing else.",
   FIN, INT, NEG + ", extra products, people, hands, glitter, bokeh, gold."],
 'R3_do_ingredients': ["Match the ELEMENT reference exactly for the DropOff tube: shape, colour, cap and label layout.",
   "No person appears; a clean, sunny ingredient still life.",
   "PRODUCT ORIENTATION\nThe DropOff tube stands upright on its cap in the centre of a white table, label facing the camera. Around it, neatly spaced: on the left a fresh pineapple slice and a piece of fibrous pineapple stem; on the right a small heap of roasted coffee beans; in front, a single glossy swipe of " + GEL + ". " + TUBE,
   "COMPOSITION AND FRAMING\nVertical 9:16 frame, camera slightly above, straight on. The tube and ingredients sit between 40% and 72% of the frame height, centred, with clear space left and right of the tube. The top 35% is clean white wall for a headline; the bottom 25% is calm white table.",
   "SCALE\nThe tube is 20 cm tall; the pineapple slice about 9 cm across; coffee beans 1 cm each. Real relative sizes.",
   "LIGHT AND SHADOW\nLow, hard late-afternoon sunlight from the right casting long, crisp, elegant shadows of the tube and the ingredients across the white table to the left - a soft, sunny long-shadow look.",
   "BACKGROUND\nA white wall and a white matte table; nothing else.",
   FIN, INT, NEG + ", extra products, people, hands, clutter, coloured background."],
 'R4_pc_flat': ["Match the ELEMENT reference exactly for the PowerCycle bottle: shape, colours, chrome finish and label layout.",
   "No person appears; a minimal product photograph for a typographic ad.",
   "PRODUCT ORIENTATION\nOne closed PowerCycle bottle standing upright, label facing the camera, with a single bead of " + GEL + " on the surface beside it. " + CAP,
   "COMPOSITION AND FRAMING\nVertical 9:16 frame, camera straight on at bottle height. The bottle stands in the lower right: its centre at 75% of the width, its base at 84% of the frame height, its height about 24% of the frame height. Everything else - the whole top 60% and the left two thirds - is clean, flat, empty background.",
   "SCALE\nThe bottle is 14 cm tall and 4.5 cm wide. Real proportions.",
   "LIGHT AND SHADOW\nSoft bright studio light from the upper left, one soft contact shadow, gentle highlights on the chrome.",
   "BACKGROUND\nA flat, seamless, warm off-white cream backdrop (#FBF6EC) and matching surface, completely even; nothing else.",
   FIN, INT, NEG + ", extra products, people, hands, props, glitter, bokeh."],
 'R5_nw_vampire': ["Match the ELEMENT reference exactly for the NetWork bottle: shape, colours, chrome finish and label layout.",
   "The person is a strikingly beautiful woman in her late 20s styled as an elegant gothic vampire for Halloween: long glossy black hair, deep red lips, a black lace corset gown with a high collar, luminous, flawless-looking glowing porcelain skin with real natural texture, not plastic. No fangs, no blood. Exactly two arms and two hands.",
   "PRODUCT ORIENTATION\nShe stands in three-quarter profile admiring her glowing skin in a tall ornate antique gold mirror, one hand lightly touching her cheek; in her other hand she holds the closed NetWork bottle upright at chest height, label facing the camera, at the same distance from the camera as her body. The label reads exactly 'NetWork' with a capital N and a capital W. " + CAP,
   "COMPOSITION AND FRAMING\nVertical 9:16 frame, 35mm lens, waist-up. Her face and the mirror sit between 40% and 62% of the frame height, the bottle at about 66%. The top 36% is dark, calm candlelit room - clean space for a headline.",
   "SCALE\nThe bottle is 12 cm tall and 3.5 cm wide - about two thirds of the length of her hand and about half the height of her face. Never larger.",
   "LIGHT AND SHADOW\nWarm candlelight from candelabras, deep moody shadows, a glowing highlight on her cheekbones, candle reflections on the red and silver chrome.",
   "BACKGROUND\nA dark gothic boudoir: an ornate gold mirror, tall lit candles, deep red roses, black and burgundy velvet; cinematic.",
   FIN + " Cinematic campaign photograph, fine grain.", INT, NEG + ", fangs, blood, horror, gore, extra arms, extra fingers, plastic skin, bottle close to the camera."],
}
if __name__ == '__main__':
    print(json.dumps(X))
