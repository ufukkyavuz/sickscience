"""Batch 12 — BCRF alternative formats: mirror scene (handwriting added in Figma)."""
import json
IDENT = ("Preserve the exact identity of the product: proportions, construction, colours and printed branding exactly as the element "
         "shows it. Use the element for identity only; do not redraw any part of it. The capsule bottle keeps its rounded pill silhouette: "
         "top half glossy metallic red chrome cap, bottom half mirror-polished silver chrome, and one black vertical label stripe running "
         "the full length over both halves. Exactly one product, no extra product.")
body = f"""{IDENT}

PRODUCT ORIENTATION
The product stands upright on the white marble vanity top right in front of the mirror, perfectly vertical, front label facing the camera and fully readable. An uncapped pink lipstick lies on its side on the vanity beside it. Camera at vanity height, straight on to the mirror. No fisheye, no wide-angle distortion.

COMPOSITION AND FRAMING
Vertical 9:16 bright bathroom still life with a 35mm lens. A large frameless rectangular mirror fills the upper 65% of the frame, its surface clean, bright and completely empty, reflecting only a soft out-of-focus pale bathroom wall; the mirror surface stays perfectly clear for handwritten lipstick words to be added later, with nothing written on it. Below the mirror, a white marble vanity top runs across the frame at about 72% of the frame height. The product stands slightly right of centre on the vanity, its top at about 56% and its base at about 72% of the frame height, its reflection softly visible in the mirror. A small white folded hand towel sits at the far left of the vanity. Every object fits completely inside the frame.

SCALE
The product is a capsule-shaped bottle 12 cm tall and 3.5 cm in diameter. The lipstick is 8 cm long. The towel is 25 cm wide. Keep these real proportions; if in doubt make the product smaller, never bigger.

LIGHT AND SHADOW
Soft bright morning daylight from a window on the left, out of frame, clean reflections in the mirror, the chrome catching soft highlights that never cover any printed word; every printed word stays clearly lit and legible.

BACKGROUND
Only the empty mirror reflecting a soft pale wall, and the marble vanity; no person, no reflection of a person or camera, no shelves of products, no plants.

PHOTOGRAPHIC FINISH
35mm look at f/5.6. Veined white marble, clean silvered mirror glass, mirror chrome, satin lipstick. Fine grain, bright airy natural colour, intimate morning-routine mood. All product text stays perfectly legible, sharp and accurate. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no numbers, no logos added to the scene other than the product's own printed label; nothing written on the mirror.

LABEL TEXT: the words SickScience and NetWork on the black stripe are PURE WHITE, on the red cap and on the silver half alike; never black, grey or dark letters. NetWork is spelled with a capital N and a capital W.

Negative: writing on the mirror, lipstick marks, hearts, words, letters, black, grey or dark letters on the product, 'Network' with a lowercase w, extra products, redrawn or invented product, fake brand names, misspelled text, tilted product, oversized product, blurred product, unreadable text, person, reflection of a person, reflection of a camera, phone, CGI, 3D render look, HDR glow, watermark"""
json.dump({'mirror': ['A real bathroom lifestyle photograph featuring ', 'ss-network', ' \n\n' + body]}, open('batch-12.json', 'w'), ensure_ascii=True)
print(len(body))
