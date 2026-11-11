# Batch-85: ShapeShift, lab x Halloween (user refs 2026-11-01: backlit white, black silhouettes, glass, microscope).
# Web UI: Nano Banana Pro, 2K, Unlimited, 9:16, count 1, element ss-shapeshift. Output: _calisma/batch-85-lab-halloween/
import json, pathlib

IDENT = ("Preserve the exact identity of the product: proportions, construction, colours and printed branding. Use the element reference for "
         "identity only and do not redraw it. PROPORTIONS ARE CRITICAL: a slim, tall capsule with fully rounded ends at the top AND the bottom, "
         "height 3.4 times its width; the violet metallic chrome cap is exactly the upper half and the mirror-silver body exactly the lower half. "
         "A narrow vertical BLACK stripe runs the full height over both halves, and every word ('SickScience' on the cap, 'ShapeShift' on the "
         "silver half) is printed vertically in pure white on that stripe, never directly on the chrome, never black or grey letters. Never "
         "stubby, chubby, squat or flat-bottomed. Exactly one product, no extra product.")
SCALE = ("SCALE\nThe capsule is 12 cm tall and 3.5 cm wide. {s} Keep these real proportions; if in doubt make the product smaller, never bigger.")
LIGHT = ("LIGHT AND SHADOW\nPure white backlit studio panel behind everything, high-key, blown-out clean white. Every prop reads as a crisp black "
         "silhouette with thin rim light on its edges, the way a backlit microscope or a backlit hand looks. The product alone gets a soft frontal "
         "fill so its violet chrome stays saturated and every printed word is bright and legible; thin black reflections run down the edges of the "
         "chrome. {l}")
BG = ("BACKGROUND\nOnly seamless luminous white. No wall, no horizon line, no room, no people, no extra decoration.")
FIN = ("PHOTOGRAPHIC FINISH\nHigh-end scientific beauty campaign, 100mm macro lens at f/11, razor sharp, restrained palette of white, black and "
       "the violet of the product only. All product text must be perfectly legible, sharp, and accurate - no blurry or distorted letters. Ultra "
       "photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail, fine grain. No text, no letters, no logos added to "
       "the scene (product label only).")
INT = ("INTEGRATION\nThe product was photographed in this set: same light direction and softness, the chrome reflects the black props and the white "
       "panel, a real contact shadow and a faint reflection where it touches a surface, same sharpness and grain as the frame, no outline or halo.")
NEG = ("Negative: stubby, chubby or wide bottle, flat-bottomed bottle, extra products, redrawn or invented product, fake brand names, misspelled text, "
       "black letters, dark or grey text on the product, text directly on chrome, oversized product, blurred product, unreadable text, added text, "
       "watermark, pasted or composited look, cut-out edges, sticker look, halo, floating product, grey or dark background, orange or yellow colour "
       "cast, cartoon, illustration, CGI, 3D render, plastic textures, HDR glow, blood, gore, horror, cheap party-shop decorations{n}.")

C = {
 "01_spider_microscope": dict(o="The capsule stands upright on the flat black stage of a large microscope, label facing the camera. A thin black spider hangs on one fine silk thread from the objective lens, stopped just above the cap. Camera level with the stage. No fisheye, no wide-angle distortion.",
   c="Vertical 9:16 frame. The black microscope silhouette enters from the upper right with two or three objective lenses pointing down; the black stage and stand fill the lowest 25% of the frame. The capsule stands in the middle of the frame, vertically between 42% and 66%. Upper left stays empty white.",
   s="The spider is 2 cm across, its body far smaller than the width of the cap.", l="", n=", giant spider"),
 "02_skeleton_hand": dict(o="An anatomical skeleton hand rises from the bottom right and pinches the capsule between thumb bone and finger bones, holding it upright, tilted about 8 degrees, label facing the camera. Camera slightly below. No fisheye, no wide-angle distortion.",
   c="Vertical 9:16 frame, inspired by a backlit hand holding a glass. The bones of the anatomical teaching skeleton form a clean black silhouette with fine thin gaps of white light between the bones. Capsule centred, vertically between 40% and 64%. Everything fits inside the frame; the wrist bones leave through the bottom edge. Top 35% stays empty white.",
   s="The skeleton hand is adult size, about 18 cm from wrist to fingertip, so the capsule is about two-thirds of the hand length.", l="", n=", more than five fingers, extra finger bones, fleshy hand"),
 "03_vampire_profile": dict(o="An extreme close-up side profile of a woman, facing right, her nose, lips and a razor-sharp sculpted jawline forming the black silhouette. Her gloved fingers enter from the lower right and hold the capsule upright beside her lips at the same distance from the camera as her face, label facing the camera. No fisheye, no wide-angle distortion.",
   c="Vertical 9:16 frame, inspired by a backlit silhouette portrait. Her profile fills the left 55% of the frame between 28% and 74% of the height; the jawline and neck curve are the hero line. Her lips are slightly parted and one small white vampire fang catches the light, elegant and subtle. The capsule stands to the right of her lips, vertically between 34% and 62%. Top 22% stays empty white.",
   s="From chin to hairline her face is about 19 cm, so the capsule is about 0.6 of that height and never as tall as her head.", l="Her skin keeps a faint rim of visible pores along the edge, as in a real backlit portrait.", n=", dracula costume, cape, big fangs, open mouth snarl, plastic teeth, extra hands, extra fingers"),
 "04_specimen_jar": dict(o="The capsule stands upright inside a tall clear laboratory specimen jar with a ground-glass stopper, submerged in water-clear liquid with a few fine silver bubbles rising, label facing the camera. Camera level. No fisheye, no wide-angle distortion.",
   c="Vertical 9:16 frame. The jar stands centred on a slim black lab stand with one black clamp arm holding its neck, like a preserved monster specimen in a laboratory. Jar occupies the frame vertically between 30% and 78%, the capsule between 40% and 68%. Top 25% stays empty white.",
   s="The jar is 26 cm tall and 11 cm wide.", l="The glass shows thin black edge lines, as backlit glass does.", n=", murky liquid, green liquid, coloured liquid, distorted label from refraction"),
 "05_bats_flask": dict(o="The capsule stands upright on a white glass lab bench to the left of a large round-bottom glass flask, label facing the camera. Camera level with the bench. No fisheye, no wide-angle distortion.",
   c="Vertical 9:16 frame. A clear round-bottom flask with a long neck sits on a black ring stand. Out of the open neck a loose stream of small black bats flies upward in a rising curve to the upper right, from dense at the neck to scattered at the top of the frame, as real backlit bat silhouettes with thin wing membranes. Bench line at 76% of the height. Capsule and flask between 46% and 76%.",
   s="The flask body is 14 cm wide, the bats are 4 to 6 cm across.", l="", n=", cartoon bats, paper-cut bats, identical bats, smoke"),
 "06_web_droplets": dict(o="The capsule stands upright on a white lab bench in the exact centre of a black retort stand, label facing the camera. Camera level. No fisheye, no wide-angle distortion.",
   c="Vertical 9:16 frame. A real spider web is strung between the black retort stand rod and two black clamp arms above and around the capsule, its fine silk threads beaded with round drops of a translucent gel-serum - semi-transparent with a soft milky haze, neither opaque white cream nor water-clear, glossy and slightly viscous - each drop catching the backlight. The web occupies the frame between 18% and 58%; the capsule stands below its centre between 46% and 72%.",
   s="The web is about 22 cm across, the gel drops are 2 to 5 mm.", l="", n=", opaque white cream, thick lotion, cobwebs like fake cotton, spider"),
 "07_black_cat": dict(o="The capsule stands upright on a white lab bench, label facing the camera. A black cat sits right beside it, in side profile facing left, its long tail curled once around the base of the capsule without covering any printed word. Camera level with the bench. No fisheye, no wide-angle distortion.",
   c="Vertical 9:16 frame. The cat is a pure backlit silhouette with soft rim light on its fur. A slim black microscope stands behind them on the right, partly hidden by the cat. Bench line at 72% of the height. Capsule and cat vertically between 44% and 72%. Top 38% stays empty white.",
   s="The sitting cat is 30 cm tall, so the capsule reaches about its shoulder height and looks small and real beside it.", l="", n=", cartoon cat, cat touching the label, cat larger than a real cat"),
 "08_electric_arc": dict(o="The capsule stands upright on a small black insulated platform, label facing the camera, between two tall black laboratory electrodes. Camera level. No fisheye, no wide-angle distortion.",
   c="Vertical 9:16 frame, a mad-scientist laboratory reduced to minimal silhouettes. The two black electrodes rise left and right with round black spheres on top; a thin real electric arc in the violet of the product jumps between the spheres above the cap. A black knife switch sits at the lower left on the same base. Capsule between 44% and 70%, arc around 30%.",
   s="The electrodes are 30 cm tall.", l="The arc adds a faint violet glow on the top of the cap only.", n=", lightning bolt clipart, sparks everywhere, purple background, purple fog"),
 "09_skull_calipers": dict(o="The capsule stands upright on a white lab bench beside an anatomical teaching skull, label facing the camera. Camera level with the bench. No fisheye, no wide-angle distortion.",
   c="Vertical 9:16 frame. An anatomical skull in strict side profile facing right is a black backlit silhouette with its hinged jaw clearly defined. A pair of slim black measuring calipers grips the jawbone, as if the jawline is being measured in a laboratory. The capsule stands to the right of the skull at the same distance from the camera. Bench line at 72% of the height. Skull and capsule vertically between 40% and 72%. Top 35% stays empty white.",
   s="The skull is 21 cm from front to back and 15 cm tall. RELATIVE SIZE: the capsule height is exactly four-fifths of the skull height, so its cap stays below the top of the skull, and the capsule width is one sixth of the skull length.", l="", n=", real human remains look, cracked or dirty skull, scary expression"),
 "10_pumpkin_belljar": dict(o="The capsule stands upright on a white lab bench to the right of a glass bell jar, label facing the camera. Camera level with the bench. No fisheye, no wide-angle distortion.",
   c="Vertical 9:16 frame. A tall clear glass bell jar stands on a black round base, and under it a small white pumpkin is kept like a laboratory specimen, sliced open by one clean vertical cut with a thin black scalpel resting beside it. Only the pumpkin's stem and the cut edge read dark; the pumpkin stays white on white. Bench line at 74% of the height. Bell jar between 34% and 74%, capsule between 50% and 74%. Top 30% stays empty white.",
   s="The bell jar is 28 cm tall, the pumpkin 12 cm wide. RELATIVE SIZE: the capsule is exactly as tall as the pumpkin is wide and reaches less than half the height of the bell jar; the capsule width is one quarter of the pumpkin width.", l="", n=", orange pumpkin, carved jack-o-lantern face, candle, autumn leaves"),
}

# Retries of 01 (two capsules drawn) and 02 (stubby capsule), scale given relative to the scene (user 2026-11-01)
C["01b_spider_microscope"] = dict(C["01_spider_microscope"],
    o=C["01_spider_microscope"]["o"].replace("The capsule stands", "One single capsule, only one, stands"),
    s="The spider is 2 cm across. RELATIVE SIZE: the capsule is exactly as wide as one objective lens barrel, and the microscope stage is five times wider than the capsule. The spider body is smaller than the width of the cap.",
    n=", giant spider, two capsules, double bottle, twin bottles side by side, mirrored copy")
C["02b_skeleton_hand"] = dict(C["02_skeleton_hand"],
    o=C["02_skeleton_hand"]["o"].replace("holding it upright, tilted about 8 degrees", "holding it perfectly upright with no tilt, the slim capsule shown at its full length"),
    s="The skeleton hand is adult size, about 18 cm from wrist to fingertip. RELATIVE SIZE: the capsule is as long as the distance from the wrist to the first knuckle of the middle finger, about two-thirds of the hand length, and only as wide as two finger bones side by side.")

def build(k, v):
    return "\n\n".join([
        "A real high-key scientific beauty campaign photograph featuring the ShapeShift element reference. Laboratory meets Halloween: quiet, elegant, graphic.",
        IDENT, "PRODUCT ORIENTATION\n" + v["o"], "COMPOSITION AND FRAMING\n" + v["c"], SCALE.format(s=v["s"]),
        LIGHT.format(l=v["l"]).strip(), BG, FIN, INT, NEG.format(n=v["n"])])

out = pathlib.Path(__file__).with_name("batch-85-lab-halloween.json")
out.write_text(json.dumps({k: build(k, v) for k, v in C.items()}, ensure_ascii=False, indent=1))
print(len(C), "prompts", max(len(build(k, v)) for k, v in C.items()), "chars max")
