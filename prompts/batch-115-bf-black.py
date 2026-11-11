# Batch-115 (2026-11-06): Black Friday colour plates for the kinetic "XX% OFF" row videos.
# User: "aynı fotoğraflara yapmak zorunda değilsin… git görsel üret… Black Friday renklerinde". Text-free; rows are added in code behind the product.
import json, os
COMMON_ID = ("Preserve the exact identity of every product: proportions, construction, colours and printed branding. Use the element for identity only; do not redraw any part. "
 "Capsules: top half glossy metallic chrome cap in the product colour, bottom half mirror-polished silver chrome, rounded pill silhouette, slim and tall (height about 3.1 times the width), "
 "the cap is exactly the upper half; every word is printed in thin pure white letters, made readable by a dark reflection behind it, never black or grey text. NetWork is spelled with a capital N and a capital W.")
LIGHT = ("A narrow black card stands opposite each product, out of frame, so a soft dark reflection runs down the chrome behind the white lettering and every word reads clearly. "
 "Hard crimson-red rim light from behind on both sides, a soft white key from the front-left keeps the labels bright, deep black everywhere else.")
FINISH = ("85mm lens at f/8, real studio photograph: mirror chrome with true reflections of the red lights and the black set, glossy black acrylic floor with a soft mirror reflection of the product. "
 "All product text stays perfectly legible, sharp and accurate. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail.\n\n"
 "IMPERFECTIONS\n\nA few specks of dust on the black floor, faint hairline swirl marks in the acrylic, a light fingerprint smudge on the floor edge, real sensor grain in the blacks, slight bloom on the brightest chrome highlight, gentle vignette. Labels stay clean.\n\n"
 "INTEGRATION\n\nThe product is photographed in this set: same red rim light and colour temperature, real contact shadow and floor reflection, same sharpness and grain, no outline or halo.")
NEG = ("Negative: any text, letters, numbers, logos or price added to the scene, extra products, redrawn or invented products, stubby, chubby, squat or wide bottle, black or grey letters on the product, "
       "misspelled text, Network with a lowercase w, floating product, pasted or composited look, cut-out edges, sticker look, halo, CGI-clean surfaces, plastic perfection, 3D render, orange or yellow colour cast, people, hands.")
P = {
 'BF_trio': [
  "A real Black Friday campaign studio photograph featuring three element references: PowerCycle (green), DropOff (cobalt tube) and ShapeShift (violet). Exactly three products, no extra product.",
  COMMON_ID + " DropOff is a matte cobalt squeeze tube standing on its cap with white vertical text.",
  "PRODUCT ORIENTATION\n\nAll three stand upright side by side, touching shoulders, slightly staggered in depth: PowerCycle on the left, DropOff in the middle and a little behind, ShapeShift on the right, labels facing the camera. Camera at product height, straight on.",
  "COMPOSITION AND FRAMING\n\nVertical 9:16. The group is SMALL and centred: together they span only the middle 34% of the frame width, from 33% to 67%, and stand between 38% and 72% of the frame height. Lots of empty black space on both sides and above.",
  "SCALE\n\nShapeShift 12 cm tall, PowerCycle 14 cm tall and visibly wider (17% taller and 25% wider than ShapeShift), DropOff tube 19 cm tall. Keep these real proportions.",
  "LIGHT AND SHADOW\n\n" + LIGHT,
  "BACKGROUND\n\nA seamless deep black studio sweep with a faint crimson glow low behind the products. Nothing else.",
  "PHOTOGRAPHIC FINISH\n\n" + FINISH,
  "KEY COMPOSITION\n\nTHREE REAL SICKSCIENCE PRODUCTS, SMALL AND CENTRED, STANDING ON GLOSSY BLACK UNDER RED RIM LIGHT, BLACK SPACE ALL AROUND.",
  NEG],
 'BF_network': [
  "A real Black Friday campaign studio photograph featuring the NetWork element (red capsule). Exactly one product.",
  COMMON_ID,
  "PRODUCT ORIENTATION\n\nThe capsule stands upright on a small polished black stone plinth, label facing the camera, the lettering running vertically. Camera at product height.",
  "COMPOSITION AND FRAMING\n\nVertical 9:16. The capsule is SMALL and centred: it is only 12% of the frame width and stands between 36% and 70% of the frame height. Wide empty black space on both sides.",
  "SCALE\n\nThe capsule is 12 cm tall and 3.5 cm wide; the plinth is 9 cm wide and 3 cm tall.",
  "LIGHT AND SHADOW\n\n" + LIGHT + " A thin warm-gold accent reflection runs down one edge of the chrome.",
  "BACKGROUND\n\nA seamless deep black sweep with a soft blood-red glow behind the plinth. Nothing else.",
  "PHOTOGRAPHIC FINISH\n\n" + FINISH,
  "KEY COMPOSITION\n\nONE REAL NETWORK CAPSULE, SMALL AND CENTRED ON A BLACK PLINTH, RED GLOW, BLACK SPACE ALL AROUND.",
  NEG],
 'BF_shapeshift': [
  "A real Black Friday campaign studio photograph featuring the ShapeShift element (violet capsule). Exactly one product.",
  COMMON_ID,
  "PRODUCT ORIENTATION\n\nThe capsule stands upright on glossy black acrylic, label facing the camera, the lettering running vertically. Camera at product height.",
  "COMPOSITION AND FRAMING\n\nVertical 9:16. The capsule is SMALL and centred: it is only 12% of the frame width and stands between 36% and 70% of the frame height. Wide empty black space on both sides.",
  "SCALE\n\nThe capsule is 12 cm tall and 3.5 cm wide.",
  "LIGHT AND SHADOW\n\n" + LIGHT + " One diagonal streak of red light crosses the black background behind the capsule.",
  "BACKGROUND\n\nA seamless deep black studio sweep, one soft diagonal red light streak behind the product. Nothing else.",
  "PHOTOGRAPHIC FINISH\n\n" + FINISH,
  "KEY COMPOSITION\n\nONE REAL SHAPESHIFT CAPSULE, SMALL AND CENTRED ON GLOSSY BLACK, RED LIGHT STREAK, BLACK SPACE ALL AROUND.",
  NEG],
}
json.dump({k: {'paras': v} for k, v in P.items()}, open(os.path.join(os.path.dirname(__file__), '..', '_calisma', 'p115.json'), 'w'))
print('ok')
