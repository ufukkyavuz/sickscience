"""Batch 68 — "after" versions of the batch-66 problem illustrations (user 2026-10-21: 4-grid should show before/after pairs
like the SpoiledChild E27 grid). Each prompt is sent with its "before" image attached as the image input (composer "+").
Realistic B/A rule: modest, believable improvement; same person, pose, crop, light, style."""
import json
BASE = ("Edit the attached reference illustration. Keep EVERYTHING identical: the same woman, the same pose, the same framing and crop, "
        "the same camera angle, the same lighting, the same warm neutral background and the same polished semi-realistic illustration style. "
        "Change ONLY this: {change} The improvement is modest, realistic and believable - a natural 'after' a few weeks later, never dramatic, "
        "never a different person.\n\nNo text, no letters, no labels, no icons, no logos, no products.\n\n"
        "Negative: different face, different pose, different crop, photo-realistic photograph, dramatic transformation, plastic skin, airbrushed, "
        "text, labels, products.")
X = {
 'D_after': BASE.format(change="the jawline is more defined and contoured, with a cleaner angle where the jaw meets the neck and slightly less fullness under the chin."),
 'E_after': BASE.format(change="the cheek skin looks smoother, more even in tone and softly radiant, with less visible pores and a healthy natural glow; real skin texture stays."),
 'F_after': BASE.format(change="the centre part looks narrower and the hair around it looks denser and thicker, so less scalp shows through."),
 'G_after': BASE.format(change="the outer thigh skin looks smoother and firmer with much less visible dimpling; the body shape stays the same."),
}
if __name__ == '__main__':
    print(json.dumps(X)[:200])
