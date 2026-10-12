---
name: feedback-product-integration-not-pasted
description: "Products must look photographed in the scene, not pasted in; every Higgsfield prompt carries an INTEGRATION section + composite-look negatives"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-04T12:03:34.929Z
---

User, 2026-10-04: "ürün çok photoshopla koyulmuş gibi duruyo çoğu karede bunu da düzeltelim". Products in generated scenes looked composited: studio-clean chrome, different light than the room, no contact shadow, sharper than surroundings.

**Why:** a pasted-looking product kills realism and reads as a cheap ad.

**How to apply:**
- Every photographic prompt gets an INTEGRATION paragraph after PHOTOGRAPHIC FINISH:
  - same light direction, softness and colour temperature as the scene;
  - chrome reflects the real surroundings, not studio reflections;
  - real contact shadow and a faint surface reflection;
  - same focus, grain and noise as the rest of the photo; no outline or halo.
- Add the matching negatives: pasted/composited look, cut-out edges, sticker look, halo, product lit differently, floating product.
- Avoid pixel-pasting the clean element PNG into scenes, except to fix tiny unreadable labels.
- Template: prompts/batch-13-build.py.

Related: [[feedback-photographic-prompt-format]], [[feedback-product-text-white-and-network-spelling]].
