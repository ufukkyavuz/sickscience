"""Batch 75b — ShapeShift proven-format series v2, cool studio / scientific (user 2026-10-22: "bunlar güzel ama daha cool, daha stüdyo ve bilimsel tarz yap").
Same 8 designs as batch-75 (travertine set), new set: cool-white cyclorama, glass/acrylic plinths, lab glass, 5600-6500K light.
Composer: type "Match the @ss-shapeshift" and pick the element, then the sections below are inserted (first one continues the sentence).
Nano Banana Pro 2K Unlimited, 9:16. Lessons from batch-75: centred product shots come out hero-sized (42-44 %) -> place off-centre
and give an explicit top/base band; model frames need "about 3 metres behind her, one fifth of her head height" to land at ~0.5x head."""
import json

OPEN = " element reference exactly for the ShapeShift bottle: shape, purple chrome cap, silver body and label layout."
PERSON = ("The person is a strikingly beautiful woman in her late 20s with model-like features and smooth realistic skin with natural texture and pores, "
          "dark hair pulled back into a sleek low bun so the jawline and neck are fully visible, wearing a simple fitted white ribbed tank top; "
          "exactly two arms and two hands; she does not hold the product.")
NOPERSON = "No person appears; a premium scientific product still life in the studio."
PROP = ("PROPORTIONS ARE CRITICAL: a slim, tall capsule with fully rounded ends at the top AND the bottom, height 3.4 times its width; the purple chrome cap "
        "is exactly the upper half and the mirror-silver body exactly the lower half. A narrow vertical BLACK stripe runs the full height over both halves, "
        "and every word ('SickScience' on the cap, 'ShapeShift' on the silver half) is printed vertically in pure white on that black stripe - never text "
        "directly on the chrome, never black or grey letters. Never stubby, chubby or flat-bottomed.")
# K1 dollop read whitish with the softer wording; K3 onward use the explicit "clearly SEE-THROUGH ... NOT white" version.
GEL = ("a small glossy, clearly SEE-THROUGH dollop of a translucent gel-serum (you can see the glass through it; it is NOT white) - semi-transparent with "
       "a soft milky haze, neither opaque white cream nor water-clear; glossy, smooth, slightly viscous")
LIGHT = ("LIGHT AND SHADOW: Cool neutral daylight-balanced studio light, 5600-6500K: one large softbox key from the upper left, a clean thin rim light from "
         "behind on the right, crisp but soft shadows; crisp specular highlights along the chrome; a faint lilac glow reflected in the glass edges; "
         "cool, clean, editorial clinical-beauty light on skin.")
SET = ("SET (identical in every shot of this series): a seamless cool-white to very light grey studio cyclorama with a soft gradient, clear glass and clear "
       "acrylic blocks of different heights as plinths with crisp refracting edges, one clear laboratory glass element (a small borosilicate beaker, a petri "
       "dish or a watch glass), optionally a thin brushed-steel tray; whites and cool greys only, the only colour is the ShapeShift purple; premium, "
       "minimal, scientific lab feel; no plants, no towels, no stone, no wood.")
FINISH = ("PHOTOGRAPHIC FINISH: Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail, premium clinical-beauty campaign. "
          "All product text must be perfectly legible, sharp, and accurate - no blurry or distorted letters. No text, no letters, no logos added to the "
          "scene (product labels only).")
INTEG = ("INTEGRATION: The product shares the scene's cool studio light; the chrome shows real reflections of the white cyclorama and the glass blocks; "
         "real contact shadow and a faint reflection on the glass surface; same sharpness and grain everywhere; no outline or halo.")
NEG = ("Negative: oversized bottle, bottle close to the camera, large bottle filling the frame, stubby chubby or flat-bottomed bottle, black or grey letters "
       "on the product, text on the chrome, missing black stripe, warped label, pasted or composited look, halo, floating product, white cream dollop, "
       "opaque white blob, lotion, gel on the side of a block, plants, olive branch, towel, travertine, stone, wood, beige, warm golden light, extra arms, "
       "extra fingers, plastic skin, heavy retouching, added text, watermark, CGI, 3D render, cartoon, dark background, saturated colours, clutter.")
# K1-K2 used "3 metres / one fifth" -> K1 came out 0.70x head; K3 onward (and retries) use "4 metres / one sixth".
MODEL_SCALE = ("SCALE IS CRITICAL: the bottle is only 12 cm tall. It stands on a low clear acrylic block right against the cyclorama, about 4 metres "
               "behind her, so by perspective it looks clearly SMALL - its height is only about one sixth of her head height (chin to crown), shorter "
               "than her ear. Keep it sharp and readable.")
STILL_SCALE = ("SCALE: The bottle is 12 cm tall and 3.5 cm wide; the glass block is 45 cm wide, so the bottle is small on it. The camera is pulled far "
               "back: the bottle's height is only 16% of the frame height. Never larger; if in doubt, smaller.")


def model(orient, comp):
    return [OPEN, PERSON, "PRODUCT ORIENTATION: " + orient + " " + PROP, "COMPOSITION AND FRAMING: Vertical 9:16, 50mm, eye level. " + comp,
            MODEL_SCALE, LIGHT, SET, FINISH, INTEG, NEG]


def still(orient, comp):
    return [OPEN, NOPERSON, "PRODUCT ORIENTATION: " + orient + " " + PROP, "COMPOSITION AND FRAMING: Vertical 9:16, 50mm, eye level, wide still life. " + comp,
            STILL_SCALE, LIGHT, SET, FINISH, INTEG, NEG]


BEHIND = ("The closed ShapeShift bottle stands upright on a clear acrylic block in the background on the right, label facing the camera, further back, "
          "behind her; beside it on the block sits " + GEL + ".")

P = {
    "K1": model("She faces the camera in a three-quarter view, head turned slightly toward the light, calm confident gaze into the lens, a crisp defined "
                "jawline. " + BEHIND,
                "She is on the left half, the top of her head at 24% and her chin at 44% of the frame height. The bottle on its block stands at 80% of "
                "the frame width, its base at about 56% of the frame height, well clear of her face. The right 45% of the frame above and below the "
                "bottle is clean cyclorama for text tiles; the top 18% is clean."),
    "K2": model("She is in clean side profile facing right, chin slightly up, showing a crisp, elegant jawline and long neck. " + BEHIND,
                "Framed from the waist up with a LOT of empty cyclorama above her. The top of her head (the bun) is at 38% of the frame height and her "
                "chin at 56%; everything above 36% of the frame is clean, empty, softly graded cyclorama with nothing in it. Her profile is on the left "
                "half. The bottle on its block stands at the right, its base at about 70% of the frame height, well to the right of her face."),
    "K3": model("She faces the camera with a soft confident smile, head tilted very slightly, the back of the fingers of one hand resting lightly under "
                "her chin. " + BEHIND,
                "She is on the left 60% of the frame, the top of her head at 26% and her chin at 46% of the frame height. The upper-right area (from "
                "64% to 96% of the frame width, 18% to 34% of the height) is clean cyclorama for a round badge. The bottle on its block stands at 82% "
                "of the frame width, its base at about 60% of the frame height."),
    "K4": model("She looks slightly up and to the right, the fingertips of one hand rest gently on the FRONT-SIDE of her NECK, low on the throat just "
                "above the collarbone - clearly on the neck, NOT on the jaw and NOT on the cheek; her chin is lifted so the smooth, firm neck is fully "
                "visible. " + BEHIND,
                "She is on the left half, the top of her head at 26% and her chin at 46% of the frame height, the neck and hand clearly visible. The "
                "upper-right area (from 62% to 96% of the width, 22% to 38% of the height) is clean cyclorama for a text card. The bottle on its block "
                "stands at 80% of the frame width, its base at about 66% of the frame height."),
    "K5": still("The closed ShapeShift bottle stands upright, centred, on a low wide clear acrylic block, label facing the camera; in front of it on "
                "the same top surface lies one small glossy curved swipe of " + GEL.replace("a small glossy, clearly SEE-THROUGH dollop of ", "a clearly SEE-THROUGH ") + "; a small empty "
                "borosilicate beaker stands far back on the left edge and a thin brushed-steel tray at the far right edge.",
                "The bottle is centred horizontally; its rounded top is at 44% and its base at 60% of the frame height, so it occupies only that "
                "narrow band. Wide clean cyclorama on both sides of the bottle for two columns of ingredient cards; the top 30% is clean."),
    "K6": still("The closed ShapeShift bottle stands upright on the top of a clear glass cube on the LEFT side of the frame, label facing the camera; "
                "right beside it on the same top surface sits " + GEL + "; an empty glass petri dish lies flat on a lower acrylic block at the far "
                "left edge.",
                "The bottle stands at 30% of the frame width, its rounded top at 46% and its base at 62% of the frame height. The right half of the "
                "frame above the blocks is clean cyclorama for text tiles; the top 30% is clean."),
    "K7": still("The closed ShapeShift bottle stands upright on a thin brushed-steel tray resting on a clear acrylic block on the RIGHT side of the "
                "frame, label facing the camera; beside it on the tray sits " + GEL + " in a small clear watch glass.",
                "The bottle stands at 74% of the frame width, its rounded top at 44% and its base at 60% of the frame height. The whole left 55% of the "
                "frame is clean, calm cyclorama for a column of step photos; the top 26% is clean."),
    "K8": still("The closed ShapeShift bottle stands upright on the top of a tall clear acrylic column on the LEFT side of the frame, label facing the "
                "camera; beside it on the same top surface sits " + GEL + "; a small clear borosilicate beaker stands on a lower glass block behind it.",
                "The bottle stands at 30% of the frame width, its rounded top at 44% and its base at 60% of the frame height. The right 55% of the frame "
                "above the blocks is clean cyclorama for a column of icon cards; the top 30% is clean."),
}

if __name__ == "__main__":
    print(json.dumps(P))


# ---------------------------------------------------------------------------------------------------------------------------------------
# v2b — TABLE staging (user 2026-10-22: v1/K-set "unbalanced: product too low, model too high"; Pinterest refs ~/sickscience-work/b75/pinrefs).
# Camera at table-top height, she leans/rests on a white glossy lab table, the bottle STANDS ON THE SAME TABLE beside her face/hands at the
# same depth -> face and product share one horizontal band. Scene structure (table edge, camera height) controls placement, not percentages.
TSET = ("SET (identical in every shot of this series): a seamless cool-white to very light grey studio cyclorama, a white glossy lab table top "
        "with a soft mirror-like reflection running across the full width of the frame, clear glass or acrylic accents (a small borosilicate "
        "beaker or a petri dish); whites and cool greys only, the only colour is the ShapeShift purple; premium, minimal, scientific; no plants, "
        "no towels, no stone, no wood.")
TLIGHT = ("LIGHT AND SHADOW: Crisp cool daylight-balanced studio light, 5600-6500K: one large softbox key from the upper left, a clean rim light "
          "from behind, soft crisp shadows on the table; crisp specular highlights along the chrome; a faint lilac reflection of the cap in the "
          "glossy table; cool, clean, editorial clinical-beauty light on skin.")
TINTEG = ("INTEGRATION: The product shares the scene's cool studio light; the chrome reflects the white table and the cyclorama; real contact "
          "shadow and a soft reflection of the bottle in the glossy table; same sharpness and grain everywhere; no outline or halo.")
TMODEL_SCALE = ("SCALE IS CRITICAL: the bottle is 12 cm tall and 3.5 cm wide and her head is about 23 cm from chin to crown. The bottle stands on "
                "the table at the same distance from the camera as the model, so it is about HALF her head height: standing on the table its "
                "rounded top reaches only to about her chin. Never taller than half her head; since her head is only about 20% of the frame "
                "height, the bottle is only about 10% of the frame height.")
TSTILL_SCALE = ("SCALE: The bottle is 12 cm tall and 3.5 cm wide; the beaker is 9 cm tall. The camera is pulled back for a wide still life: the "
                "bottle's height is about 24% of the frame height. Never larger.")
TGEL = ("a small glossy, clearly SEE-THROUGH dollop of a translucent gel-serum on the table (you can see the white table through it; it is NOT "
        "white) - semi-transparent with a soft milky haze, neither opaque white cream nor water-clear")
# T1 (first try) came out as a close-up (head 42% of frame, bottle 0.7x head) -> explicit WIDE-shot sentence added from T3 on.
TOPEN_MODEL = ("Vertical 9:16, 50mm, the camera is at table-top height, eye-level with her face as she leans on the table. This is a WIDE shot: "
               "the camera is about 2.5 metres away, she is seen from the waist up with generous empty space around her, and her whole head (chin "
               "to crown) is only about 20% of the frame height - never a close-up. The front edge of the "
               "table top runs straight across the whole frame at 66% of the frame height; below it only the calm glossy white table front with "
               "soft reflections. The top 32% of the frame is clean, empty cyclorama. ")
TOPEN_STILL = ("Vertical 9:16, 50mm, wide still life, the camera is low at table-top height. The front edge of the table top runs straight across "
               "the whole frame at 70% of the frame height; below it only the calm glossy white table with soft reflections. The top 30% of the "
               "frame is clean, empty cyclorama. ")
BESIDE = ("The closed ShapeShift bottle STANDS UPRIGHT ON THE SAME TABLE right beside her {where}, at the same distance from the camera as her "
          "face, label facing the camera; next to it on the table sits " + TGEL + ".")


def tmodel(orient, comp):
    return [OPEN, PERSON, "PRODUCT ORIENTATION: " + orient + " " + PROP, "COMPOSITION AND FRAMING: " + TOPEN_MODEL + comp,
            TMODEL_SCALE, TLIGHT, TSET, FINISH, TINTEG, NEG]


def tstill(orient, comp):
    return [OPEN, NOPERSON, "PRODUCT ORIENTATION: " + orient + " " + PROP, "COMPOSITION AND FRAMING: " + TOPEN_STILL + comp,
            TSTILL_SCALE, TLIGHT, TSET, FINISH, TINTEG, NEG]


T = {
    "T1": tmodel("She leans forward over the white table, both forearms folded flat on the table top, her head tilted slightly and resting just "
                 "above her folded arms, calm confident gaze into the lens. " + BESIDE.format(where="folded arms, about 20 cm to the right of her face"),
                 "Her face is slightly left of centre, between 46% and 62% of the frame height. The bottle stands on the table at 72% of the frame "
                 "width, its base on the table edge line and its top level with her chin. Clean cyclorama at the upper right for text."),
    "T2": tmodel("She leans on the table with one elbow, in a three-quarter profile facing right, her chin lifted and resting lightly on the back "
                 "of her hand, the jawline crisp and clear. " + BESIDE.format(where="hand, about 25 cm in front of her face on the right"),
                 "Her face is left of centre, between 44% and 60% of the frame height. The bottle stands on the table at 74% of the frame width, "
                 "its top level with her chin, well clear of her nose and hand."),
    "T3": tmodel("She leans on the table with both forearms, the fingertips of one hand resting lightly under her chin, a soft confident smile, "
                 "looking into the lens. " + BESIDE.format(where="forearm, about 20 cm to the right of her face"),
                 "Her face is slightly left of centre, between 46% and 62% of the frame height. The bottle stands on the table at 74% of the frame "
                 "width, its top level with her chin. Clean cyclorama at the upper right for a round badge."),
    "T4": tmodel("She leans on the table with one forearm, chin lifted, the fingertips of her other hand resting gently on the FRONT-SIDE of her "
                 "NECK, low on the throat just above the collarbone - clearly on the neck, NOT on the jaw and NOT on the cheek. "
                 + BESIDE.format(where="forearm, about 20 cm to the right of her face"),
                 "Her face is slightly left of centre, between 42% and 58% of the frame height, the neck and hand fully visible. The bottle stands "
                 "on the table at 76% of the frame width, its top level with her chin. Clean cyclorama at the upper right for a text card."),
    "T5": tstill("The closed ShapeShift bottle stands upright on the white glossy table at the centre, label facing the camera; in front of it "
                 "lies one small glossy curved swipe of a clearly SEE-THROUGH translucent gel-serum (you can see the table through it; NOT white); "
                 "a small empty borosilicate beaker stands far back at the left edge.",
                 "The bottle is centred; its rounded top is at 46% and its base on the table at 70% of the frame height. Wide clean cyclorama on "
                 "both sides of the bottle for two columns of ingredient cards."),
    "T6": tstill("The closed ShapeShift bottle stands upright on the white glossy table on the LEFT side of the frame, label facing the camera; "
                 "right beside it sits " + TGEL + "; an empty glass petri dish lies flat on the table at the far left edge.",
                 "The bottle stands at 30% of the frame width; its rounded top is at 46% and its base on the table at 70% of the frame height. The "
                 "right half of the frame above the table is clean cyclorama for text tiles."),
    "T7": tstill("The closed ShapeShift bottle stands upright on the white glossy table on the RIGHT side of the frame, label facing the camera; "
                 "beside it sits " + TGEL + " in a small clear watch glass.",
                 "The bottle stands at 72% of the frame width; its rounded top is at 46% and its base on the table at 70% of the frame height. The "
                 "left 55% of the frame above the table is clean cyclorama for a column of step photos."),
    "T8": tstill("The closed ShapeShift bottle stands upright on the white glossy table on the LEFT side of the frame, label facing the camera; "
                 "beside it sits " + TGEL + "; a small clear borosilicate beaker stands on the table just behind it.",
                 "The bottle stands at 32% of the frame width; its rounded top is at 46% and its base on the table at 70% of the frame height. The "
                 "right 55% of the frame above the table is clean cyclorama for a column of icon cards."),
}

if __name__ == "__main__" and len(__import__("sys").argv) > 1 and __import__("sys").argv[1] == "T":
    print(json.dumps(T))
