// Batch-105 (2026-11-06): second pass on the OneSkin variants after the user's notes:
//  - B_ss cards 2/3: background and set must match the reference (pale ice-blue gradient + palm; grey-white top-down texture of the opened product)
//  - C1/C2: the women must be as cool as the reference women (editorial, confident, rings, high-key white studio)
//  - D: a woman version with the reference's pose (dots of product on the cheekbone, ring finger, grey seamless, headline space on top)
//  - Men's hair: PowerCycle in a man's palm for the men's carousel
// Paste into the Higgsfield page (window.__P), then window.__fill(key). Mentions are typed first by hand.
const SKIN="Real human skin with visible pores, fine natural texture, tiny peach fuzz and slight unevenness; no retouched plastic skin, no airbrushing.";
const GEL="a translucent gel-serum — semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, smooth, slightly viscous, it holds a soft rounded bead and lets light pass through its edges";
const IMP="Real-world flaws, kept subtle: real film grain and slight sensor noise in the shadows, gentle natural vignetting, a soft bloom on the brightest highlight, a few tiny stray hairs.";
const FIN="Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos added to the scene.";
const NEGW="ordinary or plain look, tired, sad or awkward expression, frumpy styling, messy hair, wrinkled elderly skin, plastic skin, airbrushed skin, CGI, 3D render, extra fingers, six fingers, deformed hand, more than two arms, text, letters, watermark, opaque white cream, thick white lotion, whipped cream, water-clear liquid, coloured or gold serum, product bottle in frame, dim light, beige or brown room, window frames";
window.__P = window.__P || {};
window.__P.J1_meno=[
"A real high-end editorial skincare campaign portrait for a premium clinical beauty brand, shot like a New York beauty campaign. A strikingly beautiful, effortlessly cool woman in her early 50s with long, glossy silver-grey hair swept back off her face, high cheekbones, a big genuine laugh showing her teeth, eyes looking straight into the camera. Her right hand is raised beside her face, two chunky polished silver rings on her fingers; one fingertip rests on her lower cheek just above the jawline beside a fresh soft dab of "+GEL+".",
"IDENTITY AND ANATOMY","Exactly one person, exactly two arms, one hand visible with exactly five fingers, natural short nails. Her whole face is in frame. Radiant, healthy, confident. "+SKIN,
"COMPOSITION AND FRAMING","Vertical 9:16, 85mm portrait lens, a tight beauty crop: the top of her head is just cut by the top edge, her eyes sit at about 26% of the frame height, the gel dab and fingertip at about 40%, her chin at about 50%. The face is centred between 18% and 82% of the width. From 55% down: her neck and a crisp light-blue oxford shirt with an open collar, smooth and calm (headline area).",
"LIGHT AND SHADOW","Bright high-key beauty light: a large soft frontal source, white bounce from below, clean catchlights in the eyes, a crisp specular highlight on the gel dab and on the rings.",
"BACKGROUND","Seamless bright white studio, softly lit, nothing in it.",
"PHOTOGRAPHIC FINISH","f/4, eyes, rings and gel tack sharp. Fresh, luminous, natural colour. "+FIN,
"IMPERFECTIONS",IMP,"KEY COMPOSITION","EFFORTLESSLY COOL SILVER-HAIRED WOMAN LAUGHING INTO CAMERA, RINGED FINGERTIP BESIDE A GEL DAB ON HER CHEEK, BRIGHT WHITE STUDIO.","Negative: "+NEGW+"."];
window.__P.J2_glp1=[
"A real high-end editorial skincare campaign portrait for a premium clinical beauty brand. A strikingly beautiful, cool and composed woman in her early 40s with dark brunette hair pulled into a sleek low bun, sharp brows, a calm self-assured expression, gazing past the camera to the right. Her face is in close three-quarter profile turned to the right and fills the frame; the left edge of the frame cuts through her ear. With the fingertips of her right hand she smooths a fresh dab of "+GEL+" onto her cheekbone.",
"IDENTITY AND ANATOMY","Exactly one person, exactly two arms, one hand visible with exactly five fingers, natural nails, a thin gold ring. The near eye, cheek, nose, lips and jaw are in frame. "+SKIN,
"COMPOSITION AND FRAMING","Vertical 9:16, 100mm lens, close crop. The near eye sits at about 22% of the frame height near 34% of the width; the gel dab on the cheekbone at about 34% of the height and 40% of the width, fingertips just below it; her lips at about 46%. The upper-right area (from 60% to 94% of the width, 12% to 32% of the height) is calm bright background with nothing in it. From 55% down: her jaw, neck and a crisp white shirt collar, calm (headline area).",
"LIGHT AND SHADOW","Bright, clean daylight-style beauty light from the upper left, soft fill, a crisp highlight on the gel dab.",
"BACKGROUND","Seamless bright cool-white studio wall, softly out of focus.",
"PHOTOGRAPHIC FINISH","f/4, eye, fingertips and gel tack sharp. "+FIN,
"IMPERFECTIONS",IMP,"KEY COMPOSITION","SLEEK, COOL BRUNETTE IN CLOSE PROFILE SMOOTHING A GEL DAB ONTO HER CHEEKBONE, EMPTY BRIGHT UPPER RIGHT.","Negative: "+NEGW+"."];
window.__P.J4_d_woman=[
"A real high-end editorial skincare campaign portrait for a premium clinical beauty brand. A strikingly beautiful, cool and confident woman around 50 with shoulder-length ash-blonde hair parted in the middle, a calm knowing half-smile, looking straight into the camera. With her ring finger, which wears a bold polished silver signet ring, she dots three small fresh beads of "+GEL+" in a neat row along the top of her cheekbone under her right eye; her other fingers curl softly beside her cheek.",
"IDENTITY AND ANATOMY","Exactly one person, exactly two arms, one hand visible with exactly five fingers, natural nails. "+SKIN,
"COMPOSITION AND FRAMING","Vertical 9:16, 85mm portrait lens. Her face fills the lower part of the frame: the top of her head is at about 42% of the frame height, her eyes at about 62%, the three gel dots at about 66%, her chin at about 88%; the frame cuts at her upper neck. The face is centred between 20% and 80% of the width. The upper 40% is a smooth empty seamless backdrop for a headline.",
"LIGHT AND SHADOW","Soft frontal beauty light, gentle fill, a tiny crisp highlight on each gel dot and on the ring.",
"BACKGROUND","Seamless warm light-grey studio backdrop, smooth, very slightly lighter at the top.",
"PHOTOGRAPHIC FINISH","f/4, eyes, ring and gel dots tack sharp. "+FIN,
"IMPERFECTIONS",IMP,"KEY COMPOSITION","COOL ASH-BLONDE WOMAN LOOKING INTO CAMERA, RINGED FINGER DOTTING THREE GEL BEADS UNDER HER EYE, EMPTY GREY UPPER 40%.","Negative: "+NEGW+"."];
const CAPS="Each capsule is a slim tall rounded pill, height about 3.4 times its width. TWO-TONE IS CRITICAL: only the upper half is the glossy METALLIC coloured mirror-chrome cap; the lower half is bright mirror-polished SILVER chrome. Every word printed on the products is small, thin, pure white and vertical, exactly the size in the element references; never black, grey or dark text, never large bold text. All product text must be perfectly legible, sharp, and accurate — no blurry or distorted letters.";
const LABEL="A narrow black card stands opposite the capsule, out of frame, so a soft dark reflection runs down the chrome behind the white lettering and every word reads clearly.";
const IMPP="Real-world flaws, kept subtle: a few specks of dust catching the light, faint hairline scratches and micro swirl marks on the chrome, slight unevenness in the backdrop, real film grain and sensor noise in the shadows, gentle natural vignetting. Product labels stay clean and legible.";
const INTEG="The product is photographed in this scene: same light direction, softness and colour temperature; the chrome reflects this room, real contact shadows and faint reflections; same sharpness and grain as the scene; no outline, no halo.";
const NEGP="stubby, chubby, squat or wide bottle, product tilted, fully coloured capsule, capsule without a silver half, matte or plastic cap, black letters, dark or grey text on the product, misspelled text, extra products, pasted or composited look, cut-out edges, halo, CGI-clean surfaces, plastic perfection, CGI, 3D render, watermark, added text, opaque white cream, whipped cream, water-clear liquid, coloured or gold serum";
// J3: B_ss card 3 (ref = top-down macro of the opened jar with a cream swirl, grey-white seamless, product big in the lower half)
window.__P.J3_ss_open=[
"A real high-end product campaign photograph seen from directly above: the opened ShapeShift capsule from the element reference, its violet cap removed and lying beside it, the silver body with the white pump lying on a seamless pale grey-white surface. In front of the pump a generous glossy swirl of "+GEL+" is smeared on the surface, like a texture swatch.",
"Preserve the exact identity of the product: match the element reference exactly, for identity only, never redrawn. "+CAPS+" Exactly one product: the silver body with its white pump plus its own violet cap.",
"PRODUCT ORIENTATION","Top-down view. The silver body lies diagonally from the lower right toward the centre, pump pointing up-left; the violet cap lies just to its right; the label reads 'ShapeShift' along the silver body.",
"COMPOSITION AND FRAMING","Vertical 9:16, 100mm macro, camera straight above. The product, cap and gel swirl fill the area from 52% to 92% of the frame height and from 18% to 86% of the width; nothing is cut by the frame edges. The upper half is calm, empty pale grey-white surface for text.",
"SCALE","ShapeShift capsule 12 cm long, 3.5 cm wide; the gel swirl is about 7 cm long.",
"LIGHT AND SHADOW","Soft daylight from the upper left, a gentle soft shadow to the lower right, crisp highlights on the gel ridges showing its translucency. "+LABEL,
"BACKGROUND","Seamless pale grey-white surface with a very soft gradient, clean and clinical.",
"PHOTOGRAPHIC FINISH","f/8, gel texture and label tack sharp. "+FIN+" Only the product's own printed label.",
"IMPERFECTIONS",IMPP,"INTEGRATION",INTEG,"KEY COMPOSITION","TOP-DOWN MACRO: OPENED SHAPESHIFT, ITS CAP BESIDE IT AND A GLOSSY GEL-SERUM SWIRL, LOWER HALF; EMPTY PALE GREY UPPER HALF.","Negative: "+NEGP+", hands, people."];
// J5: SS in palm, retry with the capsule SMALLER in frame (proportions break when it is large)
window.__P.J5_ss_palm=[
"A real high-end product campaign photograph: one woman's open hand, palm up, rises into the frame from the lower right and holds the slender violet ShapeShift capsule from the element reference standing upright on her palm. A single small soft bead of "+GEL+" sits on the top of the rounded cap.",
"Preserve the exact identity of the product: match the element reference exactly, for identity only, never redrawn. "+CAPS+" Exactly one product.",
"PRODUCT ORIENTATION","The capsule stands perfectly vertical, label facing the camera, text vertical. PROPORTIONS ARE CRITICAL: slim and tall like a lipstick tube, its height is 3.4 times its width; the violet cap is exactly the upper half. Never stubby, chubby, squat or short.",
"COMPOSITION AND FRAMING","Vertical 9:16, 70mm lens, camera a little further back. The capsule is SMALL in the frame: about 26% of the frame height. Its top with the gel bead sits at about 44% of the frame height, its base on the palm at about 70%; centred near 52% of the width. The whole hand and wrist are visible, the wrist leaving the frame at the lower right. The upper 40% is calm empty background for text.",
"SCALE","ShapeShift capsule 12 cm tall, 3.5 cm wide; the adult hand is about 18–19 cm long, so the capsule is two-thirds of the hand's length and only about as wide as two fingers.",
"LIGHT AND SHADOW","Soft large softbox from the upper left, gentle bounce from the right, true reflections of the hand in the chrome. "+LABEL,
"BACKGROUND","A seamless soft gradient from pale ice-blue at the top to light blue-grey at the bottom, a clean clinical studio.",
"PHOTOGRAPHIC FINISH","f/5.6. "+FIN+" Only the product's own printed label.",
"IMPERFECTIONS",IMPP,"INTEGRATION",INTEG,"KEY COMPOSITION","OPEN PALM WITH A SMALL, SLENDER UPRIGHT CAPSULE AND A GEL BEAD ON ITS CAP, PALE ICE-BLUE GRADIENT, EMPTY UPPER 40%.","Negative: "+NEGP+", fist, closed hand, more than one hand, six fingers, deformed hand, face."];
// J6: men's hair carousel card 2 = a man's palm holding PowerCycle (same set as the women's card)
window.__P.J6_pc_palm_man=[
"A real high-end product campaign photograph: one man's open hand, palm up, rises into the frame from the lower right and holds the green PowerCycle capsule from the element reference standing upright on his palm, fingers gently curled around its silver lower half; a plain dark-navy knit sleeve at the wrist. A single small soft bead of "+GEL+" sits on the top of the rounded cap.",
"Preserve the exact identity of the product: match the element reference exactly, for identity only, never redrawn. "+CAPS+" Exactly one product.",
"PRODUCT ORIENTATION","The capsule stands perfectly vertical, label facing the camera, text vertical and fully visible from top to bottom.",
"COMPOSITION AND FRAMING","Vertical 9:16, 70mm lens. The capsule is about 30% of the frame height; its top with the gel bead at about 42%, its base on the palm at about 72%; centred near 52% of the width. The whole hand is visible, the wrist and sleeve leaving the frame at the lower right. The upper 38% is calm empty background for text.",
"SCALE","PowerCycle green capsule 14 cm tall, 4.5 cm wide; a man's hand is about 19–20 cm long, so the capsule is about two-thirds of the hand's length.",
"LIGHT AND SHADOW","Soft large softbox from the upper left, gentle bounce from the right, true reflections of the hand in the chrome. "+LABEL,
"BACKGROUND","A seamless soft gradient from cool light grey at the top to slate grey at the bottom, a clean clinical studio.",
"PHOTOGRAPHIC FINISH","f/5.6. "+FIN+" Only the product's own printed label.",
"IMPERFECTIONS",IMPP,"INTEGRATION",INTEG,"KEY COMPOSITION","A MAN'S OPEN PALM HOLDING THE GREEN CAPSULE UPRIGHT, GEL BEAD ON THE CAP, COOL GREY GRADIENT, EMPTY UPPER THIRD.","Negative: "+NEGP+", fist, closed hand, more than one hand, six fingers, deformed hand, face, woman's hand, nail polish."];
