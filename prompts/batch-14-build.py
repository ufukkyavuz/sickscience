"""Batch 14 — NetWork × BCRF hand self-check cartoons (2026-10-04). Writes batch-14.json (no product element; product PNG added in Figma)."""
import json

CART = (" Flat 2D cartoon illustration in a clean modern adult-animation style: bold black outlines, flat colours with simple soft shading, "
        "slightly exaggerated expressive face. Tasteful, calm, non-sexual, fully clothed in a sports bra. No text, no letters, no numbers, "
        "no speech bubbles, no logos, no watermark.")
CHIBI = (" Cute chibi cartoon illustration like a popular webcomic: soft pastel colours, thin clean dark outlines, big expressive eyes, "
         "rosy cheeks, simple flat shading, plain white background, generous empty white space above the group for text. Tasteful, "
         "cheerful, non-sexual, everyone fully clothed in sports tops. No text, no letters, no numbers, no speech bubbles, no logos, no watermark.")

out = {
 # 2x2 meme, panel A: the self-check
 'cb_meme_a': ('A cartoon woman in her early 30s with a loose dark ponytail standing in her bright bathroom in front of the mirror, wearing a '
               'soft pink sports bra and grey joggers, doing her monthly breast self-check: her right arm raised with the hand resting behind '
               'her head, and the flat pads of three fingers of her left hand pressing gently on the side of her chest near the armpit, small '
               'curved motion lines around the fingertips showing gentle circles; her face calm, focused and determined, her reflection in the '
               'mirror doing the same. A small pink awareness ribbon sticker on the corner of the mirror.' + CART),
 # 2x2 meme, panel D: the calendar
 'cb_meme_d': ('A cartoon close-up of a paper wall calendar page pinned to a pale pink wall: a plain grid of empty day squares with no numbers, '
               'one square circled with a thick pink marker and a small pink awareness-ribbon sticker stuck inside it, a pink marker pen '
               'hanging on a string beside the calendar.' + CART),
 # group chibi: self-check squad
 'cb_group': ('A group of five young women in their early 30s with different hairstyles and skin tones, wearing matching soft pink sports tops '
              'and leggings, standing in a row like in a cheerful fitness class, all doing the breast self-check pose together: one arm raised '
              'with the hand behind the head, the flat fingertips of the other hand on the side of the chest near the armpit, little motion '
              'lines showing small circles. The woman at the front right leads the group with a big encouraging smile and sparkles around her; '
              'the others copy her with focused, determined little faces. The group fills the middle band of the frame.' + CHIBI),
 # full-bleed demonstration close-up
 'cb_hand': ('A cartoon close-up from the chin down to the waist of a woman in her early 30s in a soft pink sports bra, her right arm raised '
             'behind her head, the flat pads of the three middle fingers of her left hand pressed together on the side of her chest just '
             'below the armpit, with clear curved arrow-like motion lines drawing small circles around the fingertips. Plain soft blush-pink '
             'background; the figure sits in the lower 60% of the frame, the upper 40% is plain empty background for text.' + CART),
}
json.dump(out, open('batch-14.json', 'w'), ensure_ascii=True)
for k, v in out.items():
    print(k, len(v))
