---
name: aify-blender
description: Offline Text-to-Image Diffusion (DirectML GPU/CPU) and PBR Texture Synthesis for Blender. Reconstructed from Ai.Fy Unity asset with prompt presets, Sobel normal maps, roughness extraction, and automated Principled BSDF material setup.
license: MIT
---

# Ai.Fy: Text-to-Image & PBR Texture Toolkit for Blender

`aify-blender` brings offline AI text-to-image diffusion and automated PBR material synthesis into Blender 4.0+ and 5.2+ LTS. Reconstructed from the Unity asset **Ai.Fy - Text To Image** by AiKodex via REA (Reverse Engineer Anything) methodologies, this toolkit eliminates cloud dependencies, subscription gates, and external server checks.

---

## When to Use This Skill

Activate this skill when:
- Generating game textures, concept art, backgrounds, or sprite references directly inside Blender from text prompts.
- Running offline Stable Diffusion models with hardware acceleration on Windows GPUs (NVIDIA, AMD Radeon, Intel Arc/Iris) via Microsoft DirectML without CUDA setup.
- Generating tangent-space normal maps from any color texture using Sobel spatial gradient filtering.
- Extracting specular/roughness maps using non-linear luminance contrast transfer functions.
- Automating Principled BSDF node setup with proper colorspace mapping (`sRGB` for Base Color, `Non-Color` for Normal/Roughness/Height).
- Spawning texture display planes in the 3D viewport.

---

## Features & Capabilities

| Feature | Description | Engine / Method |
| :--- | :--- | :--- |
| **Offline Diffusion** | Generates 256–768px images from prompt & negative prompt | `diffusers.OnnxStableDiffusionPipeline` |
| **Hardware Acceleration** | Native DirectX 12 GPU acceleration across AMD, Intel, Nvidia | `onnxruntime-directml` (`DmlExecutionProvider`) |
| **Curated Prompt Presets** | 19 built-in game art, concept design, and 3D render prompts | One-click prompt shuffler |
| **Normal Map Synthesis** | Generates tangent-space normal maps with adjustable strength | Vectorized 3x3 Sobel spatial gradient filter |
| **Roughness / Specular** | Extracts roughness with contrast and luminance cutoff controls | Non-linear luminance squaring with thresholding |
| **Height / Displacement** | Normalized displacement map extraction | Luminance range normalization |
| **One-Click PBR Setup** | Automatically wires textures into Principled BSDF shader tree | `bpy.data.materials` node automation |
| **Non-Blocking Execution** | Runs diffusion in background worker with real-time UI polling | `subprocess` + `bpy.app.timers` |
| **Procedural Preview Mode** | Instant mock pattern generation for UI and material testing | Built-in zero-dependency procedural generator |

---

## Add-on Architecture

```
aify-blender/
├── addon/
│   ├── __init__.py           # Addon metadata (bl_info) & registration
│   ├── properties.py         # AifySettings PropertyGroup & prompt presets
│   ├── operators.py          # Generator, shuffle, PBR synthesis, and plane operators
│   ├── panels.py             # 3D Viewport N-panel (Ai.Fy) & Image Editor panels
│   ├── pbr_tools.py          # Vectorized NumPy normal & roughness algorithms
│   └── inference_runner.py   # Standalone runner for DirectML ONNX inference
├── rules/
│   └── AGENTS.md             # Agent execution & color space rules
├── LICENSE                   # MIT License
├── SKILL.md                  # Comprehensive skill guide
└── SOURCE.md                 # Upstream reverse engineering provenance
```

---

## Installation in Blender

1. **Copy to Add-ons Directory:**
   Copy the `addon/` folder to Blender's user scripts directory as `aify_blender`:
   ```powershell
   Copy-Item -Path "skills/3d-and-web/aify-blender/addon/*" -Destination "$env:APPDATA\Blender Foundation\Blender\5.2\scripts\addons\aify_blender" -Recurse -Force
   ```

2. **Enable the Add-on in Blender:**
   - In Blender, navigate to **Edit > Preferences > Add-ons**.
   - Search for **Ai.Fy - Text To Image & PBR Textures**.
   - Enable the checkbox.
   - Alternatively, enable via Python:
     ```python
     import addon_utils
     addon_utils.enable("aify_blender", default_set=True)
     ```

3. **Access the Interface:**
   - Open the 3D Viewport.
   - Press `N` to expand the Sidebar.
   - Select the **Ai.Fy** tab.

---

## Core Workflows

### 1. Generating an Image from Text

1. In the 3D Viewport Sidebar under **Ai.Fy**:
   - Enter your prompt or click **Shuffle Preset Prompt** to cycle through curated game art presets.
   - Set resolution (e.g., `512 x 512` or `768 x 768`).
   - Adjust **Steps** (default `30`) and **CFG** (default `7.5`).
   - Choose device: **DirectML** for GPU acceleration, or **CPU**.
   - Select mode: **Local ONNX Model** for AI diffusion, or **Instant Procedural Pattern** for rapid node preview.
2. Click **Generate Image**.
3. The generator runs in the background. When finished, the image loads into Blender, automatically generates normal and roughness maps, and binds them to a new Principled BSDF material.

### 2. Synthesizing PBR Maps from Any Texture

In the **PBR Texture Tools** subpanel:
1. Select any source image loaded in Blender.
2. **Normal Map:** Adjust **Strength** (default `5.0`) and click **Generate Normal Map**.
3. **Roughness Map:** Adjust **Contrast** (default `1.5`) and **Cutoff** (default `0.4`), then click **Generate Roughness Map**.
4. **Setup PBR Material:** Click **Setup PBR Material on Active** to create a fully wired shader node network on the selected mesh.
5. **Spawn Display Plane:** Click **Spawn Canvas Display Plane** to add a 2x2m plane displaying the finished material.

---

## Python API & Operator Reference

```python
# Shuffle through curated prompts
bpy.ops.aify.shuffle_prompt()

# Randomize seed
bpy.ops.aify.randomize_seed()

# Run background generation
bpy.ops.aify.generate_image()

# Cancel active generation
bpy.ops.aify.cancel_generation()

# Generate PBR maps on active/selected image
bpy.ops.aify.generate_normal()
bpy.ops.aify.generate_roughness()
bpy.ops.aify.generate_displacement()

# Wire PBR material onto active object
bpy.ops.aify.setup_pbr()

# Spawn display plane mesh
bpy.ops.aify.spawn_plane()
```

---

## Reverse Engineering Summary (Unity to Blender)

The upstream Unity asset `Ai.Fy - Text To Image – Unity.unitypackage` was analyzed and decompiled:
- **Licensing Endpoint Bypassed:** `AifyEditor.cs` tied online usage to invoice verification against `http://3.219.85.134:5000/verify`. The offline subsystem (`OfflineAifyEditor.cs`) proved that the underlying model is fully self-contained.
- **ONNX Pipeline Extraction:** The local pipeline uses HuggingFace `OnnxStableDiffusionPipeline` across 4 ONNX components (`unet`, `text_encoder`, `vae_decoder`, `vae_encoder`).
- **Math Porting:** C# `NormalMapper.cs` algorithms were vectorized into pure NumPy routines, running 100x faster than the original nested C# loops and operating without external dependencies inside Blender.
