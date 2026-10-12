"""Batch 21 — 50-creative overnight run (2026-10-07). New single-product / set scenes, square masters, subject in central ~46%."""
import json, importlib.util, sys, io, copy
def load(n, f):
    spec = importlib.util.spec_from_file_location(n, f); m = importlib.util.module_from_spec(spec)
    o = sys.stdout; sys.stdout = io.StringIO(); spec.loader.exec_module(m); sys.stdout = o; return m
b18 = load('b18', 'batch-18-build.py'); b19 = load('b19', 'batch-19-build.py')
PROP, caps, TUBE, p = b18.PROP, b19.caps, b19.TUBE, b19.p
SMALL = ("SIZE IS CRITICAL: photographed from further back; the product is SMALL in the frame — only about 26% of the frame height — "
         "with lots of calm empty background around it. ")
def ident_set(desc, n):
    return ("Preserve the exact identity of every item in the set: proportions, construction, colours and printed branding exactly as the element shows them. "
            f"Use the element for identity only; do not redraw any part of it. The set contains {desc}. Exactly {n}, no extra product. " + PROP)
def ident_obj(desc):
    return ("Preserve the exact identity of the item: proportions, construction, colours and printed branding exactly as the element shows it. "
            f"Use the element for identity only; do not redraw any part of it. {desc} Exactly one, no extra product.")
S = lambda c: caps(c)
J = {}
def add(k, el, ident, orient, scene, scale, light, back, finish, neg, small=True, opener='A real high-end editorial still-life photograph featuring '):
    x = p(opener, el, ident, orient, scene, scale, light, back, finish, neg)
    if small: x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\n' + SMALL, 1); x[2] = x[2].replace('Negative: ', 'Negative: giant product filling the frame, ')
    J[k] = x
add('b21_bath','ss-shapeshift',S('violet'),'The product stands upright on the white marble ledge of a bathroom sink, front label facing the camera.',
    'A clean white marble washbasin edge with a small ribbed glass cup holding a bamboo toothbrush to one side and a folded white waffle hand towel; soft morning light; the product is centred.',
    'The product is 12 cm tall; the glass cup is 9 cm tall.','Soft morning window light from the left, gentle reflections on marble, crisp chrome highlights.',
    'Out-of-focus white tiled bathroom wall; calm, fresh, airy.','70mm at f/5.6. Marble, glass, waffle cotton, mirror chrome. Fine grain, fresh clean colour.','text, logos on cup, toothpaste tube, clutter')
add('b21_night','ss-shapeshift',S('violet'),'The product stands upright on a light oak nightstand, front label facing the camera.',
    'Beside it a closed linen-bound book with a pair of tortoiseshell reading glasses resting on top and a small ceramic dish; a warm bedside lamp glows out of focus behind; the product is centred.',
    'The product is 12 cm tall; the book is 22 cm long.','Warm evening lamp light from the back-right, soft cool fill from the front, gentle chrome highlights.',
    'Soft-focus bedroom with warm beige linen headboard; calm cosy evening mood.','70mm at f/4. Oak grain, linen, ceramic, mirror chrome. Fine grain, warm cosy colour.','text on the book, clocks, phones, clutter')
add('b21_lab','ss-shapeshift',S('violet'),'The product stands upright on a white laboratory bench, front label facing the camera.',
    'Around it, neatly arranged and slightly behind: two clear glass laboratory beakers, a glass Petri dish holding a few drops of translucent gel-serum, and a slim glass pipette; clean, precise, scientific; the product is centred.',
    'The product is 12 cm tall; the beakers are 10 cm tall; the Petri dish is 9 cm wide.','Bright cool clinical key light from above, crisp reflections in the glass, clean shadows.',
    'A bright white laboratory with a soft pale-grey wall, out of focus; clean and modern.','85mm at f/8. Clear lab glass, white bench, mirror chrome. Fine grain, crisp clean colour.','text, measurement markings, coloured liquids, people, hands')
add('b21_micro','ss-network',S('red'),'The product stands upright beside a modern white laboratory microscope, front label facing the camera.',
    'A sleek white modern microscope stands slightly behind and to the left of the product on a clean white bench, a single glass slide on its stage; the product is centred.',
    'The product is 12 cm tall; the microscope is 40 cm tall.','Bright cool clinical light from the upper left, crisp highlights on chrome and on the microscope.',
    'A calm white lab wall, out of focus.','85mm at f/8. Matte white plastic, mirror chrome, glass. Fine grain, clean colour.','text, logos on the microscope, people')
add('b21_barber','ss-powercycle',S('lime-green'),'The product stands upright on a black marble barber-station counter, front label facing the camera.',
    'Beside it lie a slim black fine-tooth comb and a pair of polished steel barber scissors; a round mirror reflects softly out of focus behind; the product is centred.',
    'The product is 14 cm tall and 4.5 cm in diameter; the comb is 18 cm long.','Moody warm key light from the left, crisp chrome highlights, soft shadows.',
    'Out-of-focus classic barbershop interior with dark wood and warm lights.','85mm at f/4. Black marble, polished steel, mirror chrome. Fine grain, rich warm colour.','text, people, hair clippings, logos')
add('b21_cap','ss-powercycle',S('lime-green'),'The product stands upright on a pale concrete bench, front label facing the camera.',
    'Next to it rests a plain navy baseball cap and a folded grey cotton gym towel; morning sun; the product is centred.',
    'The product is 14 cm tall; the cap is 20 cm long.','Bright low morning sun from the left casting long soft shadows, crisp chrome highlights.',
    'Out-of-focus green park and city morning light.','70mm at f/4. Concrete, cotton, mirror chrome. Fine grain, fresh natural colour.','logos on the cap, text, people')
add('b21_drybrush','ss-dropoff',TUBE,'The tube stands upright on its cap on a teak bath stool, front label facing the camera.',
    'Beside it lies a natural-bristle wooden dry body brush and a rolled white waffle towel; a few water droplets on the teak; the tube is centred.',
    'The tube is about 20 cm tall; the brush is 14 cm long.','Soft warm daylight from a frosted window on the left, gentle shadows.',
    'Out-of-focus warm white spa bathroom with pale stone tiles.','70mm at f/5.6. Teak, natural bristle, waffle cotton, matte tube. Fine grain, warm spa colour.','text, people, bottles, clutter')
add('b21_yoga','ss-dropoff',TUBE,'The tube stands upright on its cap on a light oak floor beside a rolled sage-green yoga mat, front label facing the camera.',
    'The rolled mat lies horizontally behind; a pair of small white dumbbells sit next to it; morning studio light; the tube is centred.',
    'The tube is about 20 cm tall; the rolled mat is 61 cm long and 12 cm thick.','Bright soft daylight from tall windows on the right, gentle long shadows.',
    'Out-of-focus airy white pilates studio.','50mm at f/5.6. Oak, rubber mat, matte tube. Fine grain, fresh airy colour.','people, text, logos, mirrors')
add('b21_sunrise','ss-network',S('red'),'The product stands upright on a white windowsill, front label facing the camera.',
    'Golden sunrise light pours through the window, casting a warm glow and soft window-frame shadows across the sill; a small sprig of eucalyptus lies beside the product; the product is centred.',
    'The product is 12 cm tall.','Warm golden low sunrise light from behind-left, glowing rim highlights on the red chrome, gentle soft fill.',
    'Out-of-focus window view of a soft pastel morning sky.','85mm at f/4. Painted wood, glass, mirror chrome. Fine grain, warm golden colour.','text, people, buildings in focus')
add('b21_pearls','ss-network',S('red'),'The product stands upright on a pale pink satin surface, front label facing the camera.',
    'A loose scatter of lustrous white pearls lies around the base of the product and a single strand curves in the foreground; the product is centred.',
    'The product is 12 cm tall; each pearl is about 1 cm.','Soft bright beauty key light from above-front, pearly highlights, crisp chrome.',
    'Seamless blush-pink backdrop; soft and luxurious.','100mm at f/8. Satin, pearl nacre, mirror chrome. Fine grain, soft luxe colour.','text, jewellery boxes, hands')
add('b21_ice','ss-shapeshift',S('violet'),'The product stands upright on a block of crystal-clear ice, front label facing the camera.',
    'A few clear ice cubes are scattered around the block with tiny beads of cold condensation on the chrome; cool fresh mood; the product is centred.',
    'The product is 12 cm tall; the ice block is 15 cm wide.','Cool crisp key light from the back-left making the ice glow, sharp chrome highlights.',
    'Seamless pale icy-lilac backdrop.','100mm at f/8. Clear ice, condensation, mirror chrome. Fine grain, cool crisp colour.','frost covering the label, text, cocktail glasses')
add('b21_coffee','ss-shapeshift',S('violet'),'The product stands upright on a small round white marble bistro table, front label facing the camera.',
    'Beside it a white espresso cup and saucer with a perfect crema and a flaky croissant on a small plate; morning café mood; the product is centred.',
    'The product is 12 cm tall; the espresso cup is 6 cm tall.','Soft morning daylight from the left, gentle shadows, crisp chrome highlights.',
    'Out-of-focus Parisian café terrace in warm morning light.','50mm at f/4. Marble, porcelain, pastry, mirror chrome. Fine grain, warm morning colour.','text, logos, people, menus')
add('b21_sculpted','ss-set-sculpted-duo',ident_set('ShapeShift (violet chrome capsule bottle, 12 cm tall) and a polished stainless-steel gua sha tool','two items: one bottle and the gua sha'),
    'The bottle stands upright and the gua sha lies flat in front of it on draped ivory silk, front label facing the camera.',
    'Soft folds of ivory silk fabric; the bottle stands centred with the steel gua sha resting at its base.','The bottle is 12 cm tall; the gua sha is 9 cm long.',
    'Soft diffused beauty light from the front-left, silky highlights, crisp chrome.','Seamless warm ivory backdrop.','100mm at f/8. Silk, polished steel, mirror chrome. Fine grain, soft luxe colour.','text, extra products')
add('b21_bodyduo','ss-set-body-duo',ident_set('DropOff (matte cobalt squeeze tube about 20 cm tall standing on its cap) and ShapeShift (violet chrome capsule bottle, 12 cm tall)','two products'),
    'The two products stand upright side by side, touching, on a neat stack of folded white bath towels, front labels facing the camera.',
    'A tidy stack of three folded fluffy white towels; the two products stand on top, centred; a sprig of olive leaves beside.','DropOff about 20 cm; ShapeShift 12 cm; the towel stack is 15 cm high.',
    'Soft bright bathroom daylight from the left, gentle shadows.','Out-of-focus white spa bathroom with pale stone wall.','70mm at f/5.6. Terry cotton, matte tube, mirror chrome. Fine grain, fresh clean colour.','text, extra products')
add('b21_headtoe','ss-set-head-to-toe',ident_set('PowerCycle (lime-green chrome capsule bottle, 14 cm tall) and DropOff (matte cobalt squeeze tube about 20 cm tall standing on its cap)','two products'),
    'The two products stand upright side by side on a pale wooden hotel amenities tray, front labels facing the camera.',
    'A light wooden tray with a rolled white hand towel and a small folded linen napkin; boutique hotel bathroom; centred.','PowerCycle 14 cm; DropOff about 20 cm; the tray is 30 cm long.',
    'Soft warm hotel lighting from the left, gentle shadows.','Out-of-focus boutique hotel bathroom with warm stone and brass.','70mm at f/5.6. Wood, linen, matte tube, mirror chrome. Fine grain, warm hospitality colour.','text, extra products, hotel logos')
add('b21_otg','ss-otg-shapeshift',ident_obj('A purple zip pouch and the ShapeShift capsule bottle exactly as the element shows them.'),
    'The pouch lies on top of neatly folded clothes inside an open hard-shell carry-on suitcase, the bottle standing upright beside the pouch, front label facing the camera.',
    'An open pale-grey carry-on suitcase seen from a high three-quarter angle with folded white and beige clothes; the pouch and bottle centred.','The pouch is 21 by 16 cm; the bottle is 12 cm tall; the suitcase is 55 cm long.',
    'Bright soft daylight from above-left, gentle shadows.','A light oak floor around the suitcase; airy travel mood.','35mm at f/5.6. Fabric, hard shell, mirror chrome. Fine grain, fresh travel colour.','passports, text, airline tags, brand logos on the suitcase', small=False)
add('b21_gift','ss-giftcard',ident_obj('The SickScience gift card exactly as the element shows it.'),
    'The card lies flat, slightly angled, on soft crinkled lilac tissue paper, its printed face fully visible to the camera.',
    'Around it: a loosely tied silk ribbon in violet and a small wrapped gift box in matte white; festive but minimal; the card centred.','The card is 8.5 by 5.4 cm; the gift box is 10 cm.',
    'Soft bright overhead light, gentle shadows, a soft sheen on the card.','Lilac tissue paper filling the frame.','70mm at f/8, top-down 60 degrees. Paper, silk, card. Fine grain, soft festive colour.','extra cards, text added to the scene, price tags', small=False)
add('b21_tote','ss-tote',ident_obj('The holographic SickScience tote bag exactly as the element shows it.'),
    'The tote hangs from the back of a curved café chair, facing the camera, slightly open with a folded scarf peeking out.',
    'A sunny café terrace with a round marble table beside the chair; the tote centred.','The tote is 30 by 40 by 10 cm; the chair back is 80 cm tall.',
    'Bright warm afternoon sun from the right, iridescent highlights on the holographic surface.','Out-of-focus Parisian café street.','50mm at f/4. Holographic film, woven chair, marble. Fine grain, bright summery colour.','people, text, other bags', small=False)
add('b21_mirror','ss-powercycle',S('lime-green'),'The product stands upright on a narrow glass bathroom shelf below a round mirror, front label facing the camera.',
    'The round frameless mirror above reflects soft morning light; a small wooden hair comb lies beside the product; the product is centred.',
    'The product is 14 cm tall; the comb is 15 cm long.','Soft cool daylight from the left, crisp chrome highlights, reflections in the glass shelf.',
    'Clean white bathroom wall with fine tiles.','85mm at f/5.6. Glass, wood, mirror chrome. Fine grain, fresh clean colour.','people or faces in the mirror, text')
add('b21_slip','ss-dropoff',TUBE,'The tube stands upright on its cap on a white linen bed, front label facing the camera.',
    'Beside it lies a neatly laid-out champagne silk slip dress and a pair of delicate gold earrings; date-night getting-ready mood; the tube is centred.',
    'The tube is about 20 cm tall.','Soft warm window light from the left, silky highlights.','Out-of-focus bright bedroom with white linen.',
    '50mm at f/4. Linen, silk, gold, matte tube. Fine grain, soft warm colour.','people, text, logos')
json.dump(J, open('batch-21.json','w'), ensure_ascii=True)
print(len(J), list(J))
# retries: cap and ice came out with baked-in letterbox/pillarbox bands
FULL = "FULL-BLEED: the photograph fills the entire square frame edge to edge; no borders, no bars, no frame, no letterbox or pillarbox bands. "
for k in ['b21_cap','b21_ice']:
    x = copy.deepcopy(J[k]); x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\n' + FULL, 1); x[2] = x[2].replace('Negative: ', 'Negative: borders, black bars, white bars, grey bands, letterbox, pillarbox, frame around the photo, ')
    J[k+'_b'] = x
json.dump(J, open('batch-21.json','w'), ensure_ascii=True)
print('retries', [k for k in J if k.endswith('_b')])
x = copy.deepcopy(J['b21_gift']); x[2] = x[2].replace('COMPOSITION AND FRAMING\n', 'COMPOSITION AND FRAMING\n' + FULL + 'The lilac tissue paper fills the ENTIRE square frame from top edge to bottom edge. ', 1); x[2] = x[2].replace('Negative: ', 'Negative: borders, solid colour bars at top or bottom, letterbox, frame around the photo, ')
J['b21_gift_b'] = x
json.dump(J, open('batch-21.json','w'), ensure_ascii=True)
print('gift_b')
