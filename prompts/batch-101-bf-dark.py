# Batch-101: Black Friday extra series, dark/grey, NO lab glass (2026-11-05)
# Brief (user): "black friday için de ekstra ayrı görseller… gri koyu renkliler… çok fazla lab içeriği olmayan"
# + new rule: real-world imperfections in every photo (dust, hairline scratches, grain).
# Offers (CLAUDE.md Kasım takvimi): BF 22–28 Nov 30% off everything (DTC); CM 29–30 Nov 40% off. Percentages only (discount base unconfirmed).
# Visual is text-free; Figma adds copy. 9:16 master, Unlimited Nano Banana Pro 2K.
import json, sys

CAPS = ("Each capsule is a slim, tall rounded pill: height about 3.4 times its width, the glossy METALLIC coloured mirror-chrome cap is exactly the upper half, "
        "the lower half is mirror-polished silver chrome; never stubby, chubby or squat. Every word printed on the products is thin pure white, vertical, "
        "on the coloured cap and on the silver half; never black, grey or dark text. All product text must be perfectly legible, sharp, and accurate — no blurry or distorted letters.")
LABEL_LIGHT = ("A narrow black card stands opposite each capsule, out of frame, so a soft dark reflection runs down the chrome behind the white lettering and every word reads clearly.")
IMPERF = ("IMPERFECTIONS\n\nReal-world flaws, kept subtle: a few specks of dust catching the light on the dark surface, faint hairline scratches and micro swirl marks on the floor, "
          "a slight unevenness in the backdrop, real film grain and sensor noise in the shadows, a touch of lens bloom on the hottest highlights, gentle natural vignetting. "
          "The printed labels stay clean and fully legible.")
INTEG = ("INTEGRATION\n\nThe products are photographed in this scene: same light direction, softness and colour temperature; the chrome reflects this dark room, not a generic studio; "
         "real contact shadow and a faint reflection on the surface; same sharpness and grain as the scene; no outline, no halo.")
END = ("Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos, no numbers added to the scene; only the products' own printed labels.")
NEG = ("laboratory glassware, beakers, flasks, test tubes, pipettes, petri dishes, stubby, chubby or wide bottle, cap shorter or longer than half, matte or plastic cap, "
       "black letters, dark or grey text on the product, misspelled text, extra products, pasted or composited look, cut-out edges, sticker look, halo, floating product, "
       "CGI-clean surfaces, perfectly smooth gradients, plastic perfection, CGI, 3D render, watermark, added text, people, hands")
COMP = ("Keep the upper 14–40% of the frame calm dark negative space for a headline. Every product stays inside the central band from 18% to 82% of the frame width.")
SAFE_LOW = "No product goes below 68% of the frame height; the bottom of the frame is calm surface."

def P(opening, identity, orient, comp, scale, light, bg, finish, key, neg_extra=""):
    return [opening, identity, "PRODUCT ORIENTATION", orient, "COMPOSITION AND FRAMING", comp + " " + COMP + " " + SAFE_LOW,
            "SCALE", scale, "LIGHT AND SHADOW", light + " " + LABEL_LIGHT, "BACKGROUND", bg, "PHOTOGRAPHIC FINISH", finish + " " + END,
            IMPERF, INTEG, "KEY COMPOSITION", key, "Negative: " + NEG + (", " + neg_extra if neg_extra else "") + "."]

ID1 = "Preserve the exact identity of the product: match the element reference exactly, for identity only, never redrawn. " + CAPS + " Exactly one product, no extra product."

PROMPTS = {
# 1 ShapeShift: wet black slate, single spotlight cone through haze
"D1_ss": ("ss-shapeshift", P(
 "A real high-end night campaign photograph featuring the ShapeShift capsule from the element reference, standing alone on a slab of wet black slate under one hard spotlight cone that cuts through a thin haze. The idea: one night, one product, all eyes on it.",
 ID1 + " The label reads 'ShapeShift' on the silver half and 'SickScience' on the violet cap.",
 "The capsule stands upright, label facing the camera, text vertical. Camera low, at the height of the capsule's middle, very slightly looking up.",
 "Vertical 9:16, 85mm lens. The capsule sits horizontally centred, its body between 44% and 66% of the frame height. The visible cone of light falls from the top centre onto the capsule.",
 "The capsule is 12 cm tall and 3.5 cm wide. The slate slab is 60 cm wide, the light cone is about 30 cm wide where it meets the slate, so the capsule fills about a third of the pool of light.",
 "One hard narrow spotlight from directly above and slightly in front, a visible beam in thin haze, a crisp pool of light on the wet slate with tiny water beads, everything else falls to charcoal grey and black. A faint violet bounce from the cap colours the wet surface.",
 "Deep charcoal to black studio, thin haze in the beam only, no objects.",
 "f/5.6. Wet honed slate with fine natural texture and tiny water droplets, mirror chrome with true reflections of the beam, soft haze."
 , "ONE VIOLET CAPSULE ON WET BLACK SLATE IN A SINGLE HARD SPOTLIGHT CONE, DARK HAZE, READABLE WHITE LABELS.")),
# 2 NetWork: brushed steel slab, raking light
"D2_nw": ("ss-network-v2", P(
 "A real high-end campaign photograph featuring the NetWork capsule from the element reference, standing on a thick slab of brushed dark steel, lit by a long low raking light that pulls every brushed line out of the metal. The idea: a precision tool for the biggest night of the year.",
 ID1 + " The label reads exactly 'NetWork' with a capital N and a capital W, and 'SickScience' on the red cap.",
 "The capsule stands upright slightly right of centre, label facing the camera, text vertical. Camera at product height, straight on.",
 "Vertical 9:16, 100mm lens. The capsule body sits between 44% and 66% of the frame height. The steel slab edge runs horizontally across the frame at about 66% height.",
 "The capsule is 12 cm tall and 3.5 cm wide. The steel slab is 8 cm thick and 70 cm long, so the slab is two thirds of the capsule height.",
 "A long hard light raking from the left at surface level, a crisp hard shadow of the capsule stretching right across the steel, a soft deep-red reflection of the cap on the metal, background graded from graphite grey to black.",
 "Graphite grey seamless paper falling into black, nothing else.",
 "f/8. Brushed dark steel with fine directional grain, a few machining marks, deep red mirror chrome, silver chrome.",
 "ONE RED NETWORK CAPSULE ON BRUSHED DARK STEEL, LONG RAKING LIGHT AND HARD SHADOW, GRAPHITE BACKGROUND.")),
# 3 PowerCycle: black acrylic blocks + rim light, mirror floor
"D3_pc": ("ss-powercycle", P(
 "A real high-end campaign photograph featuring the PowerCycle capsule from the element reference, standing on top of three stacked glossy black acrylic blocks of different heights, like a podium, edged by two thin rim lights. The idea: the top step, tonight only.",
 ID1 + " The label reads 'PowerCycle' on the silver half and 'SickScience' on the green cap.",
 "The capsule stands upright on the highest block, label facing the camera, text vertical. Camera slightly below product height, looking a little up.",
 "Vertical 9:16, 70mm lens. The capsule body sits between 38% and 58% of the frame height, the block stack below it down to 68%.",
 "The capsule is 14 cm tall and 4.5 cm wide. The highest block is 20 cm tall and 14 cm wide, the others 12 cm and 6 cm tall, so the top block is a little taller than the capsule.",
 "Two thin strip lights behind on the left and right draw cool white rim lines along the capsule and the block edges; a soft frontal fill keeps the label bright; a faint green glow from the cap on the black acrylic; the room is dark grey.",
 "Dark grey seamless fading to black, a black mirror floor.",
 "f/8. Glossy black acrylic with true reflections and fine edge chips, green mirror chrome, silver chrome.",
 "ONE GREEN POWERCYCLE CAPSULE ON TOP OF A BLACK ACRYLIC BLOCK PODIUM, THIN RIM LIGHTS, DARK GREY ROOM.")),
# 4 DropOff: charcoal velvet + blind-slit light
"D4_do": ("ss-dropoff", P(
 "A real high-end campaign photograph featuring the DropOff tube from the element reference, lying diagonally on charcoal velvet while hard slits of light from a window blind fall across the scene. The idea: after hours, the deal is in the light.",
 "Preserve the exact identity of the product: match the element reference exactly, for identity only, never redrawn. DropOff is a matte cobalt-blue squeeze tube with a blue screw cap and white vertical text 'SickScience' and 'DropOff'; never a stripe or band on the tube. Exactly one product, no extra product.",
 "The tube lies diagonally from lower left to upper right, cap at the lower left, label readable and facing up to the camera. Camera from above at about 60 degrees.",
 "Vertical 9:16, 50mm lens. The tube sits in the middle of the frame between 40% and 66% of the frame height. Three bright parallel slits of light cross the tube and the velvet at an angle; one slit falls across the printed label so it reads clearly.",
 "The tube is 19 cm long and 4 cm wide. The light slits are each about 3 cm wide with 5 cm gaps.",
 "Hard directional light through blinds from the upper right, sharp-edged bright slits, deep charcoal shadow between them, no other light.",
 "Charcoal grey crushed velvet filling the whole frame.",
 "f/8. Crushed velvet with visible pile and soft folds, matte cobalt tube with a slight satin sheen.",
 "ONE COBALT DROPOFF TUBE LYING DIAGONALLY ON CHARCOAL VELVET, HARD BLIND-SLIT LIGHT ACROSS IT.",
 "stripe or band on the tube")),
}

# 5 Vault trio and 6 Cyber Monday four — multi element
ID3 = ("Preserve the exact identity of every product: match each element reference exactly, for identity only, never redrawn. " + CAPS +
       " The green PowerCycle capsule is visibly bigger, 17% taller and 25% wider than the violet ShapeShift capsule. The cobalt DropOff tube is matte with white vertical text and no stripe, the tallest product, 1.58 times the ShapeShift height.")
PROMPTS["D5_vault"] = ("ss-powercycle ss-dropoff ss-shapeshift", P(
 "A real high-end campaign photograph featuring the PowerCycle capsule, the DropOff tube and the ShapeShift capsule from the element references, standing together on a raw dark concrete plinth while a slow curl of smoke drifts behind them. The idea: the full set, the biggest saving of the year.",
 ID3 + " Exactly three products, no extra product.",
 "Green capsule on the left, cobalt tube in the middle, violet capsule on the right, upright side by side with small gaps, labels facing the camera, text vertical. Camera at product height, straight on.",
 "Vertical 9:16, 85mm lens. The group sits horizontally centred, between 42% and 66% of the frame height, on the top of a square concrete plinth whose front face fills the frame below.",
 "ShapeShift 12 cm tall, 3.5 cm wide; PowerCycle 14 cm tall, 4.5 cm wide; DropOff 19 cm tall. The plinth top is 45 cm wide, so the three products take about half of its width.",
 "One soft overhead light shaped into a narrow pool on the plinth top, a thin cool rim from behind, the smoke lit softly from the side, the rest of the room in deep grey and black.",
 "Deep grey to black room, a thin curl of real smoke behind the products, nothing else.",
 "f/8. Raw cast concrete with air pockets, small chips on the plinth edge and fine dust, mirror chrome, matte cobalt tube, real soft smoke.",
 "THREE PRODUCTS ON A RAW DARK CONCRETE PLINTH, SOFT OVERHEAD POOL OF LIGHT, A CURL OF SMOKE, DEEP GREY ROOM.",
 "stripe or band on the tube, equal-size capsules"))
ID4 = ID3.replace("The cobalt", "The red NetWork capsule is the same size as the violet one and its label reads exactly 'NetWork' with a capital N and a capital W. The cobalt")
PROMPTS["D6_cm"] = ("ss-shapeshift ss-network-v2 ss-powercycle ss-dropoff", P(
 "A real high-end campaign photograph featuring the ShapeShift capsule, the NetWork capsule, the PowerCycle capsule and the DropOff tube from the element references, standing in one line on a black mirror floor in front of a single thin horizontal light bar. The idea: the whole line-up, the final two days.",
 ID4 + " Exactly four products, no extra product.",
 "From left to right: violet capsule, red capsule, green capsule, cobalt tube, upright in one straight line with small even gaps, labels facing the camera, text vertical. Camera at product height, straight on.",
 "Vertical 9:16, 85mm lens. The line of products is horizontally centred within the central 64% of the frame width, between 44% and 66% of the frame height. The thin light bar runs horizontally behind them at about 40% of the frame height, wider than the group.",
 "ShapeShift and NetWork 12 cm tall and 3.5 cm wide; PowerCycle 14 cm tall, 4.5 cm wide; DropOff 19 cm tall. The light bar is 1 cm high and 80 cm long.",
 "The thin cool-white light bar behind draws a bright edge on every product and a long streak in the black mirror floor; a soft frontal fill keeps the labels bright; the room is near-black graphite.",
 "Near-black graphite seamless, black mirror floor, nothing else.",
 "f/8. Black mirror floor with true reflections, faint swirl marks and dust specks, mirror chrome caps in their colours, matte cobalt tube.",
 "FOUR PRODUCTS IN ONE LINE ON A BLACK MIRROR FLOOR, ONE THIN HORIZONTAL LIGHT BAR BEHIND, NEAR-BLACK ROOM.",
 "stripe or band on the tube, equal-size capsules"))

if __name__ == "__main__":
    out = {k: {"mentions": v[0].split(), "paras": v[1]} for k, v in PROMPTS.items()}
    json.dump(out, open(sys.argv[1], "w"))
    print(list(out))
