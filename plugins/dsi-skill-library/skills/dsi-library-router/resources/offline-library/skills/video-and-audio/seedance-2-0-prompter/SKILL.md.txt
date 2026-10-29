---
name: seedance-2-0-prompter
description: Design Seedance 2.0 video prompts from a creative brief and image, video, or audio references. Use for multimodal prompt construction and asset-role mapping before generation.
license: MIT
metadata:
  upstream-version: "2.1.0"
  upstream-author: "pexoai"
---

# Seedance 2.0 prompt designer

Turn the brief and available assets into one usable prompt and recommended parameters. This is a prompt-only workflow: no Pexo account, CLI, API key, or paid generation is needed to draft it.

Read [atomic element mapping](references/atomic_element_mapping.md) and [reference syntax](references/seedance_syntax_guide.md) to assign useful roles to supplied assets. Use [prompt templates](references/prompt_templates.md) when a cinematic, product, or narrative structure fits. Treat the upstream preference for reference assets as a quality heuristic: a text-only brief can still receive a useful text-only prompt.

Inspect accessible inputs, identify the intended subject/action, scene, camera, style, timing, and sound, and resolve contradictory references. Use only real supplied asset names. Reference quality or unavailable media should be stated rather than invented. Choose sensible defaults when unspecified; ask only for missing details that materially affect the requested result.

Describe subject action and camera movement distinctly, with a feasible sequence for the requested duration. Give each reference an explicit primary role (identity, product, environment, motion, style, or audio). Avoid adding unrelated visual effects or changing the user's concept.

Deliver the prompt to the user, or pass it to the requested generation workflow, in this shape unless another format was requested:

```json
{
  "final_prompt": "A slow push-in on the supplied product rotating on a studio pedestal. Use @product.png as the product identity reference; preserve its markings.",
  "recommended_parameters": {"duration": 8, "aspect_ratio": "16:9"}
}
```

The example's `product.png` stands for an actual supplied file. `@filename` in these guides is prompt-level notation, not an upload, a local-file attachment, or a universally supported API field. When generation is requested, verify the chosen provider's current schema, accepted duration/aspect ratio, and attachment IDs; map each real uploaded asset to that provider's reference syntax. Recommended parameters are suggestions until validated. A draft prompt does not mean a video was generated or media was uploaded.
