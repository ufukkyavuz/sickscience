---
name: feedback-photographic-prompt-format
description: "Photographic image prompts must follow the user's sectioned template (identity, orientation, composition, scale in cm, light, background, finish, negative list)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 43d77aec-642b-4770-8d35-b961af17ba24
  modified: 2026-10-02T08:34:28.985Z
---

Every photographic (realistic scene) image prompt is written in the user's sectioned structure: opening line naming the element → identity-preservation paragraph (product-specific details, "exactly N products") → PRODUCT ORIENTATION → COMPOSITION AND FRAMING → SCALE (real cm for every item, "if in doubt make the products smaller") → LIGHT AND SHADOW → BACKGROUND → PHOTOGRAPHIC FINISH → comma-separated Negative list. Template and verbatim example: `prompts/TEMPLATE-photographic.md` in the SickScience project.

**Why:** user (2026-10-02) supplied this structure as the standard so results look more realistic; one-paragraph prompts are retired.

**How to apply:** use it for all photographic Higgsfield prompts; keep project rules (textless, textures, model age, wide framing). SCALE uses the real sizes in [[sickscience-product-dimensions]]. Related: [[sickscience-client]], [[feedback-models-in-30s]].

**2026-10-20 correction (user: "prompt şeklini de bizim prompt şeklinde kullanmadığını görüyorum inodan kontrol edip düzelt"):**
- I had flattened prompts into one line and skipped the template sections. That is wrong for every still prompt, including scenes with no product (people, flat-lays, backgrounds).
- Keep the INO "PROMPT KALIBI" section order and keep the line breaks.
- In the Higgsfield composer, type each section separately: `shift+Enter` for a line break, `shift+Enter shift+Enter` between sections. Plain Enter is not used.
- Never put an aspect or resolution line ("Vertical 2:3 frame") inside the prompt. Those are set only in the composer.
- When there is no product, still keep the sections. PRODUCT ORIENTATION then describes the prop (e.g. the glass disc).
- Builder: `prompts/batch-58-lens-template.py`.
