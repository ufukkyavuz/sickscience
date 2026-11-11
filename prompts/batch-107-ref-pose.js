// Batch-107 (2026-11-06): user: "referansla alakası var mı kadınların… duruşu kamera açısı kameraya bakışı bile benzemiyor… profesyonel fotoğraf gibi değiller".
// Fix: attach the reference photo itself (crop of OneSkin 4.png right card / 6.png left card) as an IMAGE reference for pose, camera, crop, gaze, light, grade.
// Identity rule (CLAUDE.md): never copy the reference woman's face -> a clearly different woman is described.
const GEL="a translucent gel-serum (semi-transparent with a soft milky haze, glossy, slightly viscous; not opaque white cream)";
const KEEP="Use the attached reference photo ONLY for camera angle, lens, crop and framing, head position and tilt, gaze direction, hand and finger pose, light direction and quality, background and colour grade: match all of these as exactly as possible. Do NOT copy the woman in the reference: the face, identity and features must belong to a clearly different woman as described here. Ignore and remove every piece of text, number, dotted line and graphic in the reference: the result has no text at all.";
const PRO="A real high-end beauty campaign photograph by a professional fashion photographer for a premium clinical skincare brand: perfect professional retouching that keeps real skin texture (pores, fine lines, natural tone), professional hair and make-up (fresh, minimal), clean polished styling, crisp professional studio lighting, shot on a medium-format camera, 8K detail. Ultra photorealistic, indistinguishable from a real photograph.";
const NEG="AI look, CGI, plastic skin, poreless skin, uncanny eyes, extra fingers, six fingers, deformed or fused fingers, more than two arms, text, letters, numbers, dotted lines, graphics, watermark, opaque white cream, thick white lotion, product bottle in frame";
window.__P = window.__P || {};
window.__P.L1_glp1=[KEEP,
"SUBJECT: a beautiful woman in her mid 30s with sleek dark brown hair pulled back, warm olive skin, defined brows, natural lashes. Exactly as in the reference: her face is turned three-quarters, the left edge of the frame cuts through her face so only one eye, the side of her nose, her cheek and the corner of her lips are visible; that eye looks straight into the camera with a calm, confident gaze; her ear is near the top. Her hand rises from the lower right with long straight fingers held together; the tip of her index finger smooths a fresh dab of "+GEL+" on her upper cheekbone near the ear. Exactly one person, exactly one hand with five fingers.",
"COMPOSITION AND FRAMING","Vertical 9:16. Same tight crop as the reference, with the plain bright white area to the upper right kept empty. From about 70% down: her neck and a pale light-blue top, as in the reference.",
"LIGHT AND BACKGROUND","Same as the reference: soft, bright, even studio light, clean white background.",
"PHOTOGRAPHIC FINISH",PRO+" No text, no letters, no logos.",
"Negative: "+NEG+"."];
window.__P.L2_d_woman=[KEEP,
"SUBJECT: a beautiful woman in her early 50s with a sleek shoulder-length honey-blonde bob with soft grey strands, parted in the middle, light hazel eyes. Exactly as in the reference: frontal, eye level, she looks straight into the camera with a calm closed-lip half-smile; her hand is raised on the right side of the frame with the fingers up, the tip of the ring finger at the outer corner under her eye, where three small dots of "+GEL+" sit in a neat row; a chunky silver ring with a black stone on her little finger. Exactly one person, exactly one hand with five fingers.",
"COMPOSITION AND FRAMING","Vertical 9:16. Her face sits in the lower 60% of the frame exactly as in the reference (top of the head at about 40% of the frame height, the frame cutting just below her lips); the upper 40% is smooth empty seamless backdrop for a headline.",
"LIGHT AND BACKGROUND","Same as the reference: soft frontal light, warm light-grey seamless backdrop, soft natural shadows.",
"PHOTOGRAPHIC FINISH",PRO+" No text, no letters, no logos.",
"Negative: "+NEG+"."];
# batch-107 used the reference photo as an image ref and copied the women; not used (user: 'çalmak oluyo').
