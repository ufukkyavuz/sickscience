# Batch-121 (2026-11-09): set plates for the Early-BF 25% set countdown films.
# User: the set films showed single products; every film must show the set it sells. Same visual worlds as before
# (black/red studio = batch-115, chrome-gold knot on navy = client S_0421-0470, red foil = client S_0319-0355).
import json, os, importlib.util
spec = importlib.util.spec_from_file_location('b115', os.path.join(os.path.dirname(__file__), 'batch-115-bf-black.py'))
b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
ID, LIGHT, FINISH, NEG = b.COMMON_ID, b.LIGHT, b.FINISH, b.NEG
GUA = ("The gua sha is a flat SOLID polished stainless-steel tool, about 9 cm, single-notch heart/wing shape with 'SickScience' engraved, "
       "silver mirror metal (never pink, never stone, never jade, never translucent).")
SCALE_DUO = "SCALE\n\nShapeShift 12 cm tall and 3.5 cm wide; PowerCycle 14 cm tall and 4.5 cm wide, so the green capsule is clearly 17% taller and 25% wider than the violet one."
SCALE_GLP = "SCALE\n\nNetWork 12 cm tall and 3.5 cm wide, ShapeShift 12 cm tall and 3.5 cm wide (the two capsules are exactly the same size), gua sha 9 cm long, lying flat."
SCALE_H2T = "SCALE\n\nPowerCycle capsule 14 cm tall and 4.5 cm wide; DropOff tube 19 cm tall, about 1.36 times the height of the capsule."
NEGX = NEG.replace('people, hands.', 'people, hands, pink gua sha, rose quartz, jade, stone gua sha, stripe or band on the tube, dimension lines, numbers.')
KNOT = ("BACKGROUND\n\nThe same world as the attached reference photo: a thick sculptural chrome-gold rope knot on a deep navy studio background, "
        "warm gold reflections, the products nested in and leaning against the knot. Match the reference's light, colours and lens exactly; only the products change.")
FOIL = ("BACKGROUND\n\nThe same world as the attached reference photo: crumpled glossy red metallic foil filling the whole frame, deep black shadows in the folds. "
        "Match the reference's hard flash light, colours and lens exactly; only the products change.")
def black(title, orient, scale, extra=''):
    return [title, ID + extra,
     "PRODUCT ORIENTATION\n\n" + orient,
     "COMPOSITION AND FRAMING\n\nVertical 9:16, a WIDE studio shot taken from far away: the products are SMALL, standing in the lower-middle of the frame. Their tops sit at 50% of the frame height and their bases at 72%, so each capsule is only about one fifth of the frame height tall. The whole group spans 36%-64% of the frame width. The upper half of the frame is empty black studio, with wide empty black on both sides. The capsules stand perfectly upright and every word on them runs VERTICALLY along the capsule, reading bottom to top, exactly as on the element.",
     scale, "LIGHT AND SHADOW\n\n" + LIGHT,
     "BACKGROUND\n\nA seamless deep black studio sweep with a faint crimson glow low behind the products. Nothing else.",
     "PHOTOGRAPHIC FINISH\n\n" + FINISH, NEGX]
def ref(title, orient, scale, bg, extra=''):
    return [title, ID + extra, "PRODUCT ORIENTATION\n\n" + orient,
     "COMPOSITION AND FRAMING\n\nVertical 9:16, wider than the reference: camera 1.8 metres back with a 50mm lens, so the products are SMALL in the frame. The products and the knot sit in the lower-middle: capsule tops at 50% of the frame height, the lowest point of the set at 76%; the whole group spans 30%-70% of the frame width. The upper half of the frame is calm empty background for type.",
     scale, "LIGHT AND SHADOW\n\nThe light of the reference photo. A dark reflection falls behind the white lettering on each capsule so every word reads clearly.",
     bg, "PHOTOGRAPHIC FINISH\n\n" + FINISH, NEGX]
P = {
 'BF_award': black("A real Black Friday campaign studio photograph featuring two element references: ShapeShift (violet capsule) and PowerCycle (green capsule). Exactly two products, no extra product.",
   "Both capsules stand upright side by side on glossy black acrylic, a hand's width apart, ShapeShift on the left, PowerCycle on the right, labels facing the camera, lettering vertical. Camera at product height.", SCALE_DUO),
 'BF_glp1': black("A real Black Friday campaign studio photograph featuring three element references: NetWork (red capsule), ShapeShift (violet capsule) and the stainless-steel gua sha. Exactly these three items, no extra product.",
   "NetWork and ShapeShift stand upright side by side on glossy black acrylic, NetWork on the left, labels facing the camera; the steel gua sha lies flat on the floor in front of them, slightly angled. Camera at product height, a little above.", SCALE_GLP, ' ' + GUA),
 'KNOT_award': ref("A real campaign studio photograph in the exact style of the attached reference photo, featuring two element references: ShapeShift (violet capsule) and PowerCycle (green capsule). Exactly two products.",
   "The two capsules lean together inside the loops of the gold knot, ShapeShift on the left and PowerCycle on the right, tilted about 15 degrees, labels facing the camera.", SCALE_DUO, KNOT),
 'KNOT_glp1': ref("A real campaign studio photograph in the exact style of the attached reference photo, featuring three element references: NetWork (red capsule), ShapeShift (violet capsule) and the stainless-steel gua sha. Exactly these three items.",
   "NetWork and ShapeShift lean together inside the loops of the gold knot, NetWork on the left, tilted about 15 degrees, labels facing the camera; the steel gua sha rests on the knot in front of them.", SCALE_GLP, KNOT, ' ' + GUA),
 'FOIL_h2t': ref("A real campaign studio photograph in the exact style of the attached reference photo, featuring two element references: PowerCycle (green capsule) and DropOff (matte cobalt tube). Exactly two products.",
   "PowerCycle and the DropOff tube lie diagonally side by side on the red foil, parallel, PowerCycle on the right, labels facing the camera. DropOff is a matte cobalt squeeze tube with white vertical text.", SCALE_H2T, FOIL),
}
EL = {'BF_award': ['ss-shapeshift', 'ss-powercycle'], 'BF_glp1': ['ss-network-v2', 'ss-shapeshift', 'ss-guasha'],
      'KNOT_award': ['ss-shapeshift', 'ss-powercycle'], 'KNOT_glp1': ['ss-network-v2', 'ss-shapeshift', 'ss-guasha'], 'FOIL_h2t': ['ss-powercycle', 'ss-dropoff']}
REF = {'KNOT_award': 'S_0469.jpg', 'KNOT_glp1': 'S_0431.jpg', 'FOIL_h2t': 'S_0333.jpg'}
out = {k: {'text': '\n\n'.join(v), 'els': EL[k], 'ref': REF.get(k)} for k, v in P.items()}
json.dump(out, open(os.path.join(os.path.dirname(__file__), '..', '_calisma', 'batch-120-ebf-set25', 'p121.json'), 'w'), indent=1)
json.dump({k: out[k] for k in ('BF_award', 'BF_glp1', 'KNOT_award', 'KNOT_glp1', 'FOIL_h2t')}, open(os.path.join(os.path.dirname(__file__), '..', '_calisma', 'batch-120-ebf-set25', 'p121b.json'), 'w'))
print({k: len(v['text']) for k, v in out.items()})
