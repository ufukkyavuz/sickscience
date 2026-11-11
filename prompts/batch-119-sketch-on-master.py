# Batch-119 (2026-11-07): every scene redrawn on ONE blank master page so all pages match (paper, light, framing).
# Existing scenes: refs = [master blank page, old sketch]. New scenes: ref = [master] + description.
import json, os
P118 = json.load(open(os.path.join(os.path.dirname(__file__), '..', '_calisma', 'p118.json')))
def subj(k): return P118[k].split('\n\n')[0]
EDIT = ("Image 1 is a photograph of a blank sheet of cream drawing paper. Keep image 1 exactly: the same paper, grain, sheet position, "
        "camera angle, daylight and shadow gradient. Draw onto that blank sheet, by hand, {what} "
        "Black fine-liner ink with confident, slightly imperfect hand lines and light cross-hatching, a few pencil guide marks; only the "
        "marker colours named. The drawing sits in the middle and lower part of the sheet; the top 25% of the sheet stays empty. "
        "Ultra photorealistic photo of a real drawing on this exact sheet. Negative: changed paper, changed light, changed framing, "
        "extra words, misspelled words, typed text, digital font, vector art, 3D render, hands, pen, logos, faces of real people.")
COPY = "exactly the same sketch as in image 2 (same drawing, same words, same layout, same marker colours): " 
S = {
 'm01_two_minds': EDIT.format(what="a sketch: two simple side-profile head silhouettes facing each other, drawn in black ink, a small hand-drawn question mark between them coloured in magenta marker, and tiny sparks of curiosity around it; below, the hand-lettered words \"TWO CURIOUS MINDS\" in black ink capital letters with a quick underline."),
 'm02_met_2009': EDIT.format(what=COPY + subj('s02_met_2009')),
 'm03_research': EDIT.format(what=COPY + subj('s04_research')),
 'm04_mother': EDIT.format(what="a quiet, sober sketch with lots of empty paper: two hands gently holding each other, an older hand and a younger hand, drawn in fine black ink with soft cross-hatching; nothing else, no words. Calm and respectful."),
 'm05_not_yet': EDIT.format(what="a quiet, sober sketch: a hand-drawn research curve rising from left to right across the sheet, drawn in black ink with small data points, that stops abruptly before the right edge, followed by a few faint dots and empty paper; under the gap the small hand-written words \"not yet\"."),
 'm06_lab_to_home': EDIT.format(what=COPY + subj('s07_lab_to_home')),
 'm07_exosomes': EDIT.format(what=COPY + subj('s08_exosomes')),
 'm08_plants': EDIT.format(what=COPY + subj('s09_plants')),
 'm09_nx35': EDIT.format(what=COPY + subj('s10_nx35')),
 'm11_skincare': EDIT.format(what="a sketch: an open lab notebook drawn in black ink on the left with tiny scribbled formulas, and a long hand-drawn arrow that curves to the right into a slim skincare serum bottle with a pump, the bottle coloured in magenta marker; above, the hand-lettered words \"REAL SCIENCE\" in black ink capital letters."),
 'm12_thats_sick': EDIT.format(what=COPY + subj('s01_two_geneticists').replace(subj('s01_two_geneticists'), "a hand-drawn speech bubble in the upper middle containing the hand-lettered words \"THAT'S SICK!\" in black ink capital letters; below it, a smaller hand-lettered word \"SCIENCE.\" written in magenta marker, with a quick underline. Around them, small doodles: a beaker, a pineapple slice, a molecule and a few sparkle marks, all black ink.")),
 'm13_products': EDIT.format(what=COPY + subj('s13_products')),
 'm14_awards': EDIT.format(what=COPY + subj('s14_awards')),
 'm15_never_boring': EDIT.format(what=COPY + subj('s15_never_boring')),
}
json.dump({k: v.replace('\n', ' ') for k, v in S.items()}, open(os.path.join(os.path.dirname(__file__), '..', '_calisma', 'p119.json'), 'w'), indent=1)
print(len(S))
