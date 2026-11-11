# Batch-102: November promo windows, one section each, 4–5 visuals per window (2026-11-05)
# User brief: separate designs per date window (DTC 9–21 sets 25%, 22–28 30%, 29–30 40%;
# Ulta 15–21 app-only 30%, 22–28 30% stores+online, 29–30 40%). Dark Black-Friday look.
# Reference (user, Pinterest "product lab photography", top pin LABRATS – Frederik Lindstrøm Studio):
# cool steel-blue / grey moody lab photography, few lab instruments (lab jack, clamp stand, one flask, pipette).
# Do NOT call the 9–21 window "Early Black Friday". Text is added in Figma; images text-free.
# Placement is compact (group 40–64% height, central 26–74% width) so Story/Feed/Square crop from one 9:16 master.
import json, sys

CAPS = ("Each capsule is a slim tall rounded pill, height about 3.4 times its width. TWO-TONE IS CRITICAL: only the upper half is the glossy METALLIC coloured mirror-chrome cap; "
        "the lower half is bright mirror-polished SILVER chrome. Every word printed on the products is small, thin, pure white and vertical, exactly the size in the element references; "
        "never black, grey or dark text, never large bold text. All product text must be perfectly legible, sharp, and accurate — no blurry or distorted letters.")
SIZE = {"SS": "ShapeShift violet capsule 12 cm tall, 3.5 cm wide", "NW": "NetWork red capsule 12 cm tall, 3.5 cm wide, its label reads exactly 'NetWork' with a capital N and a capital W",
        "PC": "PowerCycle green capsule 14 cm tall, 4.5 cm wide — visibly 17% taller and 25% wider than the violet and red capsules",
        "DO": "DropOff matte cobalt-blue squeeze tube 19 cm tall standing on its blue screw cap, white vertical text, no stripe or band, the tallest product",
        "GS": "flat SOLID polished stainless-steel gua sha, about 9 cm, single-notch heart/wing shape, 'SickScience' engraved, lying flat"}
NAME = {"SS": "the ShapeShift capsule", "NW": "the NetWork capsule", "PC": "the PowerCycle capsule", "DO": "the DropOff tube", "GS": "the stainless-steel gua sha"}
MENT = {"SS": "ss-shapeshift", "NW": "ss-network-v2", "PC": "ss-powercycle", "DO": "ss-dropoff", "GS": "ss-guasha"}
LABEL = "A narrow black card stands opposite each capsule, out of frame, so a soft dark reflection runs down the chrome behind the white lettering and every word reads clearly."
IMPERF = ("Real-world flaws, kept subtle: a few specks of dust catching the light, faint hairline scratches and micro swirl marks on the surfaces, a fingerprint smudge on the glass, "
          "slight unevenness in the backdrop, real film grain and sensor noise in the shadows, a touch of lens bloom on the hottest highlights, gentle natural vignetting. Product labels stay clean and legible.")
INTEG = ("The products are photographed in this scene: same light direction, softness and colour temperature; the chrome reflects this room and its instruments, not a generic studio; "
         "real contact shadows and faint reflections; same sharpness and grain as the scene; no outline, no halo.")
LOOK = ("Moody high-end lab still life in the style of a cinematic science editorial: cool steel-blue and graphite grey palette, soft directional light, deep shadows, "
        "only one or two real laboratory instruments as props, never a cluttered lab.")
COMP = ("PRODUCTS ARE SMALL IN THE FRAME: the camera is pulled back; the tallest product is only about 20% of the frame height and its top edge is BELOW 46% of the frame height; everything above 46% is empty dark space. PLACEMENT IS CRITICAL: the whole product group sits between 46% and 66% of the frame height and inside the central band from 26% to 74% of the frame width; "
        "props may extend beyond but never cover the products. The upper 46% of the frame is calm, dark, uncluttered negative space for a headline; the bottom third is calm surface.")
NEG = ("products filling the frame, large close-up products, product in the upper half of the frame, fully coloured capsule, capsule without a silver half, large bold lettering, stubby, chubby or wide bottle, cap shorter or longer than half, matte or plastic cap, black letters, "
       "dark or grey text on the product, misspelled text, extra products, printed graduations, numbers, text or logos on glassware, cluttered lab, many instruments, pasted or composited look, "
       "cut-out edges, sticker look, halo, floating product, CGI-clean surfaces, perfectly smooth gradients, plastic perfection, CGI, 3D render, watermark, added text, people, hands, "
       "warm orange cast unless requested, stripe or band on the DropOff tube, pink gua sha, rose quartz, jade, stone gua sha")

def build(prods, idea, arrange, props, light, bg, lens="85mm", extra_neg=""):
    names = ", ".join(NAME[p] for p in prods[:-1]) + (" and " if len(prods) > 1 else "") + NAME[prods[-1]]
    ident = ("Preserve the exact identity of every product: match each element reference exactly, for identity only, never redrawn. " + CAPS +
             f" Exactly {len(prods)} product{'s' if len(prods)>1 else ''}, no extra product.")
    scale = "; ".join(SIZE[p] for p in prods) + "."
    return [f"A real high-end campaign photograph featuring {names} from the element references. {idea}",
            ident, "PRODUCT ORIENTATION", arrange + " Labels face the camera, text vertical.",
            "COMPOSITION AND FRAMING", f"Vertical 9:16, {lens} lens. {LOOK} Props: {props} {COMP}",
            "SCALE", scale, "LIGHT AND SHADOW", light + " " + LABEL, "BACKGROUND", bg,
            "PHOTOGRAPHIC FINISH", "f/8. Clear borosilicate glass with true refraction, brushed and anodised lab metal, mirror chrome, matte cobalt tube. "
            "Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos, no numbers added to the scene; only the products' own printed labels.",
            "IMPERFECTIONS", IMPERF, "INTEGRATION", INTEG, "KEY COMPOSITION", idea.upper(),
            "Negative: " + NEG + (", " + extra_neg if extra_neg else "") + "."]

C = {}
# ---------- A · DTC 9–21 Nov · bundles 25% (no "Early Black Friday" wording) · cool blue-grey, soft violet bounce
C["A1_vault"]  = (["PC","DO","SS"], "The three-serum set raised on a lab jack like a specimen ready for inspection.",
  "Green capsule left, cobalt tube middle, violet capsule right, upright side by side on the top plate of a brushed steel laboratory scissor jack.",
  "one brushed steel lab scissor jack under the products; one empty clear glass flask far behind, out of focus.",
  "Cool soft key light from the upper left, a faint violet bounce from the right, steel-blue shadows.", "Graphite to steel-blue gradient backdrop, misty.")
C["A2_duo"]    = (["SS","PC"], "Two award winners held side by side in a lab clamp stand, like samples under review.",
  "Violet capsule left, green capsule right, upright on a dark honed stone base, the jaws of a steel retort-stand clamp just above them without touching.",
  "one steel retort stand with a single clamp; nothing else.",
  "A narrow cool top light, long soft shadows, a thin cold rim on the chrome.", "Deep steel-blue to charcoal backdrop.")
C["A3_sculpt"] = (["SS","GS"], "The sculpting set: the capsule and its steel gua sha laid out on a glass lab plate like precision tools.",
  "The violet capsule stands upright; the stainless-steel gua sha lies flat in front of it on a round thick clear glass plate.",
  "one round thick clear glass plate on a dark surface; a slim glass pipette lying behind, out of focus.",
  "Soft cool overhead light, crisp reflections on the steel gua sha, steel-blue shadows.", "Dark graphite backdrop with a soft blue haze.", {"neg":"extra gua sha"})
C["A4_glp1"]   = (["NW","SS","GS"], "The recovery system laid out on a smoked-glass lab tray, ready to use.",
  "Red capsule left, violet capsule right, upright; the stainless-steel gua sha lies flat in front of them on a dark smoked-glass tray.",
  "one dark smoked-glass tray; a single small glass beaker far behind, out of focus, empty.",
  "Cool box light from above, soft gradient falloff, a faint red bounce on the tray.", "Charcoal backdrop fading to steel blue.", {"neg":"extra gua sha"})
C["A5_h2t"]    = (["PC","DO"], "Head to toe: two serums standing at the end of a long dark lab bench.",
  "Green capsule left, cobalt tube right, upright side by side on a dark epoxy lab bench top.",
  "the dark epoxy lab bench top running into the distance; one out-of-focus microscope silhouette far behind on the right.",
  "Cool side light from the left, deep shadows on the right, cold reflections on the bench.", "Dark blue-grey lab interior out of focus.", {"lens":"70mm"})
# ---------- B · DTC 22–28 Nov · 30% everything · near-black, cold white light
C["B1_four"]   = (["SS","NW","PC","DO"], "The whole line-up under a single cold lab lamp in a dark lab.",
  "From left to right: violet capsule, red capsule, green capsule, cobalt tube, upright in one line with small even gaps on a black lab bench.",
  "one articulated steel lab lamp above, its head just entering the top of the frame, pointing down at the products.",
  "One cold white pool of light from the lab lamp on the products, everything else falling to near black.", "Near-black lab interior.")
C["B2_ss"]     = (["SS"], "One capsule on a black lab jack, lit like evidence.",
  "The violet capsule stands upright, centred, on the top plate of a black anodised lab scissor jack.",
  "one black anodised lab scissor jack under the capsule; nothing else.",
  "A hard narrow top light and a cold blue rim from behind, deep black shadows.", "Black to deep steel-blue gradient.")
C["B3_nw"]     = (["NW"], "A single capsule reflected in a dark glass petri dish of still water.",
  "The red capsule stands upright, centred, on a black glass surface next to a wide clear glass petri dish filled with still water that reflects it.",
  "one wide clear glass petri dish with still water; nothing else.",
  "A cold soft top light, crisp reflections in the water and chrome, deep blue-black falloff.", "Near-black backdrop.", {"neg":"coloured water"})
C["B4_pcdo"]   = (["PC","DO"], "Two serums framed by the dark silhouette of a microscope in a night lab.",
  "Green capsule left, cobalt tube right, upright on a dark brushed steel surface in front of a large out-of-focus microscope.",
  "one large black microscope behind the products, out of focus, partly cropped by the frame edge.",
  "A cold rim light from behind outlining the products, a soft frontal fill, deep shadows.", "Dark steel-blue lab interior.")
# ---------- C · DTC 29–30 Nov · 40% everything · blue-black, one bright light line, urgent
C["C1_four"]   = (["SS","NW","PC","DO"], "The full line-up on black glass with one bright thin light line under them, the last two days.",
  "From left to right: violet capsule, red capsule, green capsule, cobalt tube, upright in one line on a black glass shelf.",
  "a thin cool-white light tube lying horizontally just behind the products at their base; nothing else.",
  "The thin light line draws bright edges and long streaks in the black glass; soft frontal fill; blue-black room.", "Blue-black void.")
C["C2_ssnw"]   = (["SS","NW"], "Two capsules in a dark lab under a scanning line of light.",
  "Violet capsule left, red capsule right, upright on a black brushed steel surface.",
  "one thin bright horizontal light beam crossing the backdrop at the products' middle height, like a scanner line.",
  "The scanning line throws a sharp horizontal highlight across both capsules; cold soft fill; deep blue shadows.", "Deep blue-black backdrop with faint haze.")
C["C3_pc"]     = (["PC"], "One capsule at the end of a dark corridor of lab light rails.",
  "The green capsule stands upright, centred, on a black glossy floor.",
  "two rows of thin cool light rails converging in one-point perspective behind the capsule; nothing else.",
  "Cool light rails behind, a soft frontal fill, mirror reflections on the floor.", "Black corridor.", {"lens":"35mm"})
C["C4_dodo"]   = (["DO","SS"], "A tube and a capsule caught between two clear glass plates in a cold lab beam.",
  "Cobalt tube left, violet capsule right, upright between two thick vertical clear glass plates standing on a dark surface.",
  "two thick vertical clear glass plates, one on each side; nothing else.",
  "A cold beam from the upper right refracting through the glass plates, crisp caustics on the surface, deep blue-black shadows.", "Blue-black backdrop.")
# ---------- D · Ulta 15–21 Nov · app-only 30% · cool lab + Ulta orange accent glow (#E35200), Ulta 4 SKUs only
ORG = " A warm Ulta-orange accent light (#E35200 colour) glows from behind as a soft rim and bounce, the rest stays cool steel-blue."
C["D1_ss"]     = (["SS"], "One capsule on a lab jack with an orange glow behind it, like a notification lighting up the dark.",
  "The violet capsule stands upright, centred, on a brushed steel lab scissor jack.",
  "one brushed steel lab scissor jack; nothing else.", "Cool soft key light from the front left." + ORG, "Dark steel-blue backdrop with an orange glow behind the product.", {"neg":""})
C["D2_nwpc"]   = (["NW","PC"], "Two capsules on black acrylic with an orange light rising behind them.",
  "Red capsule left, green capsule right, upright on a black acrylic block.",
  "one black acrylic block; one slim clear glass pipette lying in front.", "Cool top light." + ORG, "Charcoal backdrop with a low orange horizon glow.", {"neg":""})
C["D3_do"]     = (["DO"], "The tube standing in a dark lab with an orange light behind a clear glass flask.",
  "The cobalt tube stands upright on its cap, centred, on a dark brushed steel surface, a clear empty glass flask a little behind it.",
  "one clear empty glass Erlenmeyer flask behind the tube, catching orange light.", "Cool side light from the left." + ORG, "Dark blue-grey backdrop.", {"neg":""})
C["D4_four"]   = (["SS","NW","PC","DO"], "All four serums in a dark lab line, an orange glow behind like a screen lighting up.",
  "From left to right: violet capsule, red capsule, green capsule, cobalt tube, upright in one line on a dark lab bench.",
  "nothing but the dark bench.", "Cool soft front light." + ORG, "Dark steel-blue backdrop with a soft orange glow band behind the products.", {"neg":""})
# ---------- E · Ulta 22–28 Nov · 30% stores + online · cool lab + orange, retail shelf feel
C["E1_shelf"]  = (["SS","NW","PC","DO"], "All four serums on a dark lab-steel shelf lit by a thin orange LED strip, like a night-time store display.",
  "From left to right: violet capsule, red capsule, green capsule, cobalt tube, upright in one line on a brushed steel shelf.",
  "the brushed steel shelf with a thin orange LED strip along its front edge; nothing else.", "Cool soft front light, the orange LED strip glowing at the base." + ORG, "Dark graphite wall.", {"neg":""})
C["E2_ssdo"]   = (["SS","DO"], "A capsule and the tube resting on orange tissue paper on a steel lab tray, like a fresh store bag unpacked in a dark lab.",
  "Violet capsule left, cobalt tube right, upright on a steel lab tray with crumpled warm-orange tissue paper around their base.",
  "one steel lab tray; crumpled orange tissue paper; nothing else.", "Cool soft key light from above." + ORG, "Dark steel-blue backdrop.", {"neg":"logo, text on paper"})
C["E3_pc"]     = (["PC"], "One capsule in a long beam of orange light cutting through a dark lab.",
  "The green capsule stands upright, centred, on a dark concrete lab floor.",
  "a single diagonal orange light beam through faint haze; nothing else.", "A diagonal orange beam from the upper right through haze, cool blue fill elsewhere.", "Dark blue-grey room with haze.", {"neg":""})
C["E4_nwss"]   = (["NW","SS"], "Two capsules on a black display cube lit from the side with warm orange light.",
  "Red capsule left, violet capsule right, upright on a black matte display cube.",
  "one black matte display cube; one clear glass petri dish leaning behind.", "Warm orange side light from the right, cool steel-blue light from the left.", "Graphite backdrop.", {"neg":""})
# ---------- F · Ulta 29–30 Nov · 40% · cool lab + Ulta holiday magenta (#E90B5A)
MAG = " A magenta accent light (#E90B5A colour) glows from behind as a rim and bounce, the rest stays cool steel-blue and near black."
C["F1_four"]   = (["SS","NW","PC","DO"], "All four serums on a black mirror bench with a magenta glow behind, the final two days.",
  "From left to right: violet capsule, red capsule, green capsule, cobalt tube, upright in one line on a black mirror bench.",
  "nothing but the black mirror bench.", "Cool soft front light." + MAG, "Near-black backdrop with a magenta glow behind the group.", {"neg":""})
C["F2_sspc"]   = (["SS","PC"], "Two capsules in a clamp stand under magenta light and thin smoke.",
  "Violet capsule left, green capsule right, upright on a dark steel base, a steel retort-stand clamp above them without touching.",
  "one steel retort stand with a clamp; a thin curl of smoke behind.", "Cool top light." + MAG, "Dark steel-blue backdrop with smoke.", {"neg":""})
C["F3_do"]     = (["DO"], "The tube standing behind a clear glass flask that bends a streak of magenta light.",
  "The cobalt tube stands upright on its cap, centred, on black glass, a clear round-bottom flask on a small steel ring stand in front-left of it.",
  "one clear round-bottom flask on a small steel ring stand; nothing else.", "Cool soft front light." + MAG, "Near-black backdrop.", {"neg":""})
C["F4_nw"]     = (["NW"], "One capsule on a lab jack in front of a soft magenta circle of light.",
  "The red capsule stands upright, centred, on a black anodised lab scissor jack.",
  "one black anodised lab scissor jack; a soft round magenta glow on the backdrop behind the capsule.", "Cool soft key light from the front left." + MAG, "Near-black backdrop with a magenta circle glow.", {"neg":""})

if __name__ == "__main__":
    out = {}
    for k, v in C.items():
        prods, idea, arr, props, light, bg = v[:6]
        opt = v[6] if len(v) > 6 else {}
        out[k] = {"mentions": [MENT[p] for p in prods],
                  "paras": build(prods, idea, arr, props, light, bg, lens=opt.get("lens","85mm"), extra_neg=opt.get("neg",""))}
    json.dump(out, open(sys.argv[1], "w"))
    print(len(out), list(out))

# --- Run notes (2026-11-05) ---
# Edits made in the composer at generation time (not in the builders above):
#   - "PRODUCTS ARE VERY SMALL ... LOW IN THE PICTURE, top of every product at 50% or lower"
#     plus a 50mm camera pulled far back. Without it Nano Banana draws the products too big
#     and they collide with the headline.
#   - Label order: "coloured cap reads 'SickScience', silver half reads the product name; never swapped".
#     D4's first version came out swapped.
#   - F1 size ratios given as SS/NW 100, PC 117, DO 158 (the first version had PC 37% taller).
#   - B1 rebuilt with no lamp in frame (the lamp competed with the logo).
# Rejected and regenerated: A1, A3, A5, B1 (x2), C4, D1, D2, D4, E1, E2, F1.
# Final images: _calisma/batch-102-bf-windows/<key>.png
# Figma: Kasım 2026, sections 1667:132 / 223 / 296 / 369 / 598 / 827.
# Headline/offset fit: per format, product top fraction measured with ptop.py.
