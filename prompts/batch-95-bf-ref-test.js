// Batch-95: Black Friday, reference test (2026-11-03). User: pins read badly, wrong sizes, tones, depth, flat 3D; test whether an image reference helps.
// Every scene runs twice with the same text: A = text only, B = text + pin attached (REF line added). Composer 3:4, Nano Banana Pro, 2K, Unlimited.
// S1 always carries the real box photo (refs/box_shapeshift.jpg), it is not the variable under test.
// Paste into the Higgsfield page: window.__B = {...}.
window.__B = (() => {
const ID = "Preserve the exact identity of every product from its element: shape, proportions, colours, construction and printed branding. The elements are the only source of truth for the products. A capsule is a rounded pill: its glossy coloured chrome cap is exactly the upper half, its lower half is mirror silver chrome, with one full-height black stripe carrying vertical text. Every word printed on a product is pure white, never black or grey. All product text must be perfectly legible, sharp, and accurate, no blurry or distorted letters.";
const SLIM = "PROPORTIONS ARE CRITICAL: the ShapeShift and NetWork capsules are slim and tall, height 3.4 times width, never stubby, chubby or squat.";
const END = "Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos added to the scene; only the products' own printed labels.";
const INT = "INTEGRATION\n\nThe products are physically in this scene: same light direction, softness and colour temperature, their chrome reflects this environment, real contact shadow, real reflection on the surface below, same sharpness and grain as the scene, no outline, no halo.";
const NEG = "stubby or wide bottle, cap shorter or longer than half, black or grey letters on the product, misspelled text, extra products, pasted or composited look, cut-out edges, sticker look, halo, floating product, flat lighting, flat 2D look, CGI, 3D render, watermark, added text";
const P = {
V1:{m:["ss-powercycle","ss-dropoff","ss-shapeshift"],t:`A real science campaign photograph. The idea: the three formulas sealed in one glass specimen cylinder, cold and precious.

${ID} ${SLIM} Exactly three products, no extra product.

PRODUCT ORIENTATION

Inside the cylinder the tube stands upright on its cap in the centre, slightly behind. The PowerCycle capsule stands front left and the ShapeShift capsule front right, both overlapping the tube a little so the group has real depth. Labels face the camera, text vertical.

COMPOSITION AND FRAMING

85mm lens at product height, level. One tall straight-walled glass cylinder with a softly rounded flat top, never a dome, horizontally centred, taking 40% of the frame width and running from 6% to 85% of the frame height, standing on a low round black plinth that reaches 90%. Blurred out-of-focus laboratory glass stands far behind on both sides, a flask and a tall column on the left, a stand and beaker on the right.

SCALE

The cylinder is 36 cm tall and 22 cm wide. The tube is 20 cm tall, a little over half the cylinder height. PowerCycle capsule 14 cm tall, 4.5 cm wide. ShapeShift capsule 12 cm tall, 3.5 cm wide, so the PowerCycle capsule is visibly bigger: 17% taller and 25% wider.

LIGHT AND SHADOW

A disc of white light in the base inside the cylinder lights everything from below and glows through the glass floor. Long thin vertical highlights run down both cylinder walls. A soft frontal fill keeps every printed word readable.

BACKGROUND

A smooth slate grey-blue backdrop, lighter around the cylinder and falling to dark at the corners. Dark glossy bench that mirrors the plinth.

PHOTOGRAPHIC FINISH

f/5.6. Monochrome steel-blue grade: everything in the frame is silver, slate and blue-grey, the only saturated colours are on the products. Thousands of fine condensation droplets cling to the inside of the glass, denser near the top, a few larger drops running down. Fine photographic grain. ${END}

${INT}

KEY COMPOSITION

ONE TALL STRAIGHT GLASS CYLINDER, BEADED WITH CONDENSATION, THREE PRODUCTS INSIDE, LIT FROM BELOW, STEEL-BLUE MONOCHROME, BLURRED GLASS BEHIND.

Negative: ${NEG}, dome, bell jar, green capsule same size as violet capsule, vapour, fog, smoke, warm colour cast, hands, people.`},
A1:{m:["ss-shapeshift","ss-powercycle"],t:`A real high-end product campaign photograph. The idea: a light gauge sweeping up to full power behind two award winners.

${ID} ${SLIM} Exactly two products, no extra product.

PRODUCT ORIENTATION

Both capsules stand upright side by side, touching the lower part of the ring of light from in front, labels facing the camera, text vertical. Camera slightly below the middle of the products.

COMPOSITION AND FRAMING

70mm lens. Behind the products floats one large open circular gauge made of about seventy separate glowing white rectangular bars, every bar pointing to the centre like the marks of a dial. The gauge is an OPEN ring with a gap at the bottom. It begins at the 7 o'clock position with tiny thin faint short dashes, then travels clockwise over the top, and every bar becomes wider, longer and brighter, until it ends at the 5 o'clock position in huge thick blown-out glowing blocks. The upper left of the ring is soft and slightly out of focus, the lower right is intense. Ring diameter 86% of the frame width, centred at 44% of the frame height. The capsules are horizontally centred and large, running from 34% to 90% of the frame height, overlapping the lower part of the ring.

SCALE

ShapeShift capsule 12 cm tall, 3.5 cm wide. PowerCycle capsule 14 cm tall, 4.5 cm wide, so it is visibly bigger: 17% taller and 25% wider. The ring is 30 cm across.

LIGHT AND SHADOW

The bars are the only strong light. They draw clean thin vertical highlights down both capsules, stronger on the right side. A soft low front fill keeps every printed word readable.

BACKGROUND

A smooth charcoal gradient, mid grey behind the ring centre falling to black at the corners, one continuous tone from top to bottom, no horizon line, no floor edge, no visible seam.

PHOTOGRAPHIC FINISH

f/8. Long soft bloom around the thick bars, black and silver grade with neutral greys, a very faint mirror reflection directly under each capsule. Fine photographic grain. ${END}

${INT}

KEY COMPOSITION

AN OPEN DIAL OF LIGHT BARS GROWING FROM THIN DASHES TO THICK GLOWING BLOCKS, TWO LARGE CAPSULES IN FRONT, CHARCOAL GRADIENT.

Negative: ${NEG}, closed full ring, even ring, small LED dots, ring light, neon tube, coloured light, green capsule same size as violet capsule, visible floor line, people, hands.`},
S1:{m:["ss-shapeshift","ss-guasha"],t:`A real luxury campaign photograph. The idea: a black-gloved hand draws the capsule out of its own carton. Capture the moment the capsule is half out of the box.

${ID} ${SLIM} The gua sha is a flat SOLID polished stainless-steel tool. Exactly two products and one carton, no extra product.

PRODUCT ORIENTATION

The attached box photo is the real SickScience carton: a tall slim rectangular carton in silver paper with a soft violet and green iridescent haze, the word SickScience printed vertically in violet on the front. Keep its design and colours exactly, never black. The carton stands upright with its top flaps open and folded out at different angles. One matte black gloved hand comes straight down from the top of the frame and pinches the violet cap between thumb and two fingers; the capsule rises vertically out of the open carton, its lower half still inside. The steel gua sha leans against the bottom of the carton.

COMPOSITION AND FRAMING

50mm lens, camera low and level with the carton, so it feels tall. The carton is horizontally centred, from 44% to 90% of the frame height, 26% of the frame width. The capsule rises from 26% to 52%. The hand and forearm fill the top of the frame.

SCALE

The carton is 14 cm tall and 5 cm wide. The capsule is 12 cm tall and 3.5 cm wide, so it fits inside the carton. The gua sha is 9 cm long, about two-thirds of the carton height.

LIGHT AND SHADOW

The glove reads as a pure black silhouette with a thin sheen on the knuckles. Soft even light on the carton keeps the print clean, a soft shadow pools under it.

BACKGROUND

A smooth vertical gradient: deep teal navy at the top, steel blue in the middle, pale cool grey-white just above the horizon. A soft horizon at 86% of the frame height, below it a pale grey floor that darkens toward the camera.

PHOTOGRAPHIC FINISH

f/8. Fine paper grain on the carton, mirror chrome, soft matte glove. Fine photographic grain. ${END}

${INT}

KEY COMPOSITION

BLACK GLOVED HAND FROM ABOVE, CAPSULE HALF OUT OF ITS REAL SILVER IRIDESCENT CARTON WITH OPEN FLAPS, TEAL-TO-PALE GRADIENT.

Negative: ${NEG}, black box, plain box, second hand, extra fingers, malformed hand, bare skin, pink gua sha, rose quartz, jade, stone, translucent, melted shape.`},
G1:{m:["ss-network-v2","ss-shapeshift","ss-guasha"],t:`A real science editorial photograph. The idea: looking between lab glass at the protocol, three clear planes of depth.

${ID} ${SLIM} The label reads exactly 'NetWork' with a capital N and a capital W. The gua sha is a flat SOLID polished stainless-steel tool. Exactly three products, no extra product.

PRODUCT ORIENTATION

The NetWork capsule and the ShapeShift capsule stand upright close together, labels facing the camera, text vertical. The steel gua sha leans against the base of the NetWork capsule. Camera level at the middle of the capsules, straight on.

COMPOSITION AND FRAMING

100mm lens, three planes. FOREGROUND PLANE: one huge clear round-bottom flask very close to the lens on the left, cropped by the left edge, covering the left 36% of the frame from 8% to 100% of the height, heavily out of focus, its curved edge passing in front of the left side of the products. MIDDLE PLANE: the products, razor sharp, horizontally centred, from 34% to 88% of the frame height. BACK PLANE: one tall conical flask behind and to the right, cropped by the right edge, softly out of focus, with white graduation marks and numberless ticks on its glass.

SCALE

Both capsules 12 cm tall, 3.5 cm wide. The gua sha is 9 cm long, three-quarters of a capsule. The conical flask behind is 26 cm tall, more than twice the capsule height.

LIGHT AND SHADOW

The backdrop glows pale behind the middle of the frame. Bright thin rims outline all the glass. Clean vertical highlights on the chrome, every printed word in clear light.

BACKGROUND

A vertical gradient: near-black across the top 15%, melting into pale ice-blue grey through the middle and near white behind the products. Glossy pale surface with a soft mirror reflection under everything.

PHOTOGRAPHIC FINISH

f/4. Cold silver-blue monochrome grade, the only saturated colours are on the products. The foreground flask refracts the backdrop. Fine photographic grain. ${END}

${INT}

KEY COMPOSITION

HUGE BLURRED ROUND FLASK IN FRONT, SHARP PRODUCTS IN THE MIDDLE, SOFT CONICAL FLASK BEHIND, ICE-BLUE MONOCHROME, NEAR-BLACK TOP.

Negative: ${NEG}, products in front of all the glass with nothing overlapping them, 'Network' with a lowercase w, pink gua sha, rose quartz, jade, stone, translucent, melted shape, coloured liquid, warm colour cast, numbers.`},
H1:{m:["ss-powercycle","ss-dropoff"],t:`A real science editorial photograph. The idea: head-to-toe routine standing in a working cold-blue laboratory.

${ID} Exactly two products, no extra product.

PRODUCT ORIENTATION

The tube stands upright on its cap in the centre, the PowerCycle capsule stands just in front of it to the left, overlapping it slightly. Labels face the camera, text vertical. Camera low, just above the bench, level.

COMPOSITION AND FRAMING

50mm lens, four planes. FOREGROUND: two clear empty petri dishes on the bench at the bottom left, out of focus. MIDDLE: the products, sharp, horizontally centred, from 22% to 84% of the frame height. LEFT: a clear conical flask with a little clear liquid on a small steel dish, slightly soft. BACK RIGHT: a polished steel stand rod with clamps, glass columns and more beakers melting into bright bokeh, and more flasks far behind on the left.

SCALE

The tube is 20 cm tall, 4.5 cm wide at its widest. PowerCycle capsule 14 cm tall, 4.5 cm wide, so the tube is 1.4 times the capsule height. The conical flask is 22 cm tall, about the same height as the tube.

LIGHT AND SHADOW

Bright soft cold daylight from behind and from the left. Sparkling specular points on the glass. Real reflections of both products run straight down into the bench.

BACKGROUND

An out-of-focus cold-blue laboratory, tall window light, pale steel blue on the left, deeper blue on the right. A polished glass bench with bright streaks.

PHOTOGRAPHIC FINISH

f/4. Cold steel-blue monochrome grade, the only saturated colours are on the products. Fine photographic grain. ${END}

${INT}

KEY COMPOSITION

TUBE AND CAPSULE SHARP ON A MIRROR BENCH, CLEAR GLASS IN FRONT AND BEHIND, COLD BLUE BOKEH LAB.

Negative: ${NEG}, tube lying down, floating glass disc, plinth, warm colour cast, numbers, hands, people.`},
D1:{m:["ss-dropoff"],t:`A real still life photograph on a laboratory shelf. The idea: one product standing among old glass like a specimen.

${ID} Exactly one product, no extra product.

PRODUCT ORIENTATION

The tube stands upright on its cap in the middle of the shelf, label facing the camera, text vertical. Camera level with the shelf surface, straight on.

COMPOSITION AND FRAMING

70mm lens, all objects on one lit shelf that runs across the frame at 84% of the height. Left: a clear glass funnel, standing on its wide mouth, cropped slightly by the left edge. Centre: the tube, from 40% to 84% of the frame height. Behind it to the right: a very large clear conical flask, rising to 12% of the frame height, with a pale cloudy band low in the glass. Right edge: a tall beaker cropped by the frame. In front on the right: a tiny stoppered glass jar. Under the shelf the frame falls to black.

SCALE

The tube is 20 cm tall. The funnel is 24 cm tall. The conical flask is 38 cm tall, almost twice the tube. The little jar is 8 cm tall.

LIGHT AND SHADOW

A hard narrow strip of white light lies along the shelf and lights all the glass from below, with bright thin rim lines on the glass edges. Above it the light falls away fast.

BACKGROUND

Pure black behind everything, one continuous tone. The shelf has a soft mirror reflection.

PHOTOGRAPHIC FINISH

f/8. Slightly warm neutral silver grade like an old print, deep blacks, visible film grain. ${END}

${INT}

KEY COMPOSITION

ONE TUBE ON A LIT SHELF AMONG A GLASS FUNNEL, A HUGE CONICAL FLASK AND A BEAKER, PURE BLACK ABOVE.

Negative: ${NEG}, grey background, light beam, gradient wall, coloured liquid, numbers, hands, people.`},
P1:{m:["ss-powercycle"],t:`A real macro product photograph with strong three-dimensional presence. The idea: the capsule tipped toward the lens, standing on a mirror where white meets black.

${ID} Exactly one product, no extra product.

PRODUCT ORIENTATION

The PowerCycle capsule rests on its rounded silver end on a polished mirror surface, tipped over about 35 degrees to the right and also leaning toward the camera, so its silver lower half comes forward and its green cap recedes. You see it from slightly above, the body clearly round with real foreshortening. The black stripe and the white text stay visible along the capsule.

COMPOSITION AND FRAMING

28mm lens, very close, camera above the surface looking down at about 25 degrees. The capsule is horizontally centred inside the middle 70% of the frame width, from 14% to 66% of the frame height. Its full mirror reflection continues below it, from 66% to 92%, fading softly.

SCALE

The capsule is 14 cm tall and 4.5 cm wide, height 3.1 times width. It looks large only because it is close to the lens.

LIGHT AND SHADOW

Big soft overhead window light gives one long clean white highlight along the body and a smooth falloff to dark on the opposite side, so the roundness reads clearly. A soft contact shadow where it touches the surface.

BACKGROUND

White and black meet in one big smooth CURVED sweep: the upper left of the frame is clean bright white, the lower right is pure black, the boundary is a large arc like the edge of a huge circle, passing behind the capsule. The surface mirrors this too.

PHOTOGRAPHIC FINISH

f/11. Mirror chrome that shows the white and black world on its curves. Fine photographic grain. ${END}

${INT}

KEY COMPOSITION

ONE CAPSULE TIPPED TOWARD THE LENS, REAL PERSPECTIVE, FULL MIRROR REFLECTION BELOW, CURVED WHITE AND BLACK SWEEP.

Negative: ${NEG}, straight diagonal line, flat side view, orthographic view, capsule lying flat, no reflection, floating in air, grey background, hands, people.`},
T1:{m:["ss-shapeshift"],t:`A real photograph through a sheet of wet frosted glass. The idea: something is behind the glass and you cannot quite see it yet.

${ID} The capsule stays a blurred shape, so nothing on it is readable and that is intended. Exactly one product, no extra product.

PRODUCT ORIENTATION

The ShapeShift capsule stands upright far behind the frosted glass, centred.

COMPOSITION AND FRAMING

100mm lens, straight on to the glass, which fills the whole frame. Behind it the capsule is only a tall pale column of light from 14% to 84% of the frame height, about 26% of the frame width, its upper half a faint violet-grey shadow, a soft darker band where the stripe sits. In the top left corner and the bottom right corner, a large curved ribbon of clear translucent gel-serum sits on the glass surface, sharp, like a clear wave of water with a thick bright edge, leaving the centre empty.

SCALE

The capsule is 12 cm tall and 3.5 cm wide behind the glass. The gel ribbons on the glass are about the length of the capsule.

LIGHT AND SHADOW

Soft bright backlight through the frost, a pale glow around the capsule, no hard shadows.

BACKGROUND

The frosted glass itself: pale misty grey-teal at the edges, near white in the centre, with fine condensation droplets scattered over it, sharp and in focus, more toward the corners.

PHOTOGRAPHIC FINISH

f/2.8, focus on the glass surface. The capsule is extremely diffused, low contrast, almost dissolved into the mist, no sharp edge at all. Fine photographic grain. Ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail. No text, no letters, no logos added to the scene.

KEY COMPOSITION

WET FROSTED GLASS, A GHOST OF A CAPSULE BEHIND IT, TWO CLEAR GEL RIBBONS IN OPPOSITE CORNERS, PALE TEAL MIST.

Negative: sharp capsule, dark saturated capsule, readable label, opaque white cream, thick white lotion, coloured or gold serum, added text, watermark, hands, people.`}
};
const REF = "IMAGE REFERENCE\n\nThe attached reference photo is the authority for lighting, colour grade, tonal range, glass behaviour, depth layering and composition. Match them as closely as possible. Take nothing else from it: none of its products, packaging, brand names, labels or text. The only products come from the elements.";
return {P, REF};
})();
window.__go = (key, withRef) => {
  const {P, REF} = window.__B;
  const parts = P[key].t.split('\n\n');
  const i = parts.indexOf('PRODUCT ORIENTATION');
  const out = withRef ? [...parts.slice(0, i), ...REF.split('\n\n'), ...parts.slice(i)] : parts;
  return out;
};

// Sonuç (2026-11-03). Görseller _calisma/batch-95-bf-ref-test/final (A = refsiz, B = pin refli), Figma Kasım 2026 section 1533:97.
// Seçilen B: V1 5dc94545 (ikinci tur) · A1 f9592961 · S1 bd9827af · G1 56b1df48 · H1 75f5f4a7 (ikinci tur) · D1 03c93463 · P1 86fb11ad · T1 7ff05d37.
// A: V1 412d009e · A1 203ad94e · S1 221b19ce · G1 264dc558 · H1 47d1b70c · D1 f6ca8f7f · P1 4b4a6d91 · T1 d4852ff7.
// Ölçüm (görselden): V1 PC/SS boy 1.14, tüp/PC 1.75 (hedef 1.17, 1.43); H1 tüp/PC 1.66; A1 PC/SS boy 1.21, en 1.17.
// İkinci tur SCALE metni ölçü oranlarıyla: "if the ShapeShift capsule height is 100, PowerCycle 117, tube 165".
// Etkisi az oldu: referans görseldeki hero ürün tüpü büyük çizdiriyor.
// 2026-11-03: Figma Kasım 2026 section 1524:49 (BF1-BF8) görselleri B (refli) ile değiştirildi.
// Feed: Photo 1080x1440 y=-45 (3:4 kırpım). Story: Photo 1080x1440 y=240 → Figma Expand Portrait 9:16 → 1080x1920.
// BF8 ters renk grubu (1529:160/150) gizlendi (soluk kapakta beyaz harf okunmuyordu); BF4 Story yazı+logo beyaz (genişleyen üst koyu);
// BF2 fiyat satırı ve BF7 teklif yazılarına gölge. Eski batch-93 görselleri Figma geçmişinde / _calisma/batch-93-black-friday.
