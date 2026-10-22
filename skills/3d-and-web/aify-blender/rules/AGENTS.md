# Ai.Fy Blender Development & Generation Rules

These rules govern all Text-to-Image diffusion inference, PBR texture synthesis, and shader setup tasks using the `aify-blender` toolkit.

## 1. Non-Blocking Execution Discipline
- Always run diffusion inference in a detached subprocess or background worker (`inference_runner.py`). Never execute heavy diffusion loops directly inside Blender's main thread to prevent UI freezing or application crashes.
- Monitor execution via `bpy.app.timers` polling and provide real-time status messages in the UI.

## 2. Hardware and Device Selection
- **DirectML GPU Acceleration (`dml`):** Default to DirectML on Windows. It provides native DirectX 12 hardware acceleration across NVIDIA, AMD Radeon, and Intel Arc/Iris GPUs without requiring CUDA toolkit dependencies.
- **CPU Fallback (`cpu`):** Use CPU mode only when discrete or integrated DirectX 12 GPU acceleration is unavailable or during headless CI runs.
- **Procedural Mock Mode (`mock`):** Use instant procedural generation during UI testing, pipeline verification, or layout composition before running full multi-step diffusion.

## 3. PBR Color Space and Node Standards
- **Color Space Integrity:**
  - Base Color textures MUST always use `sRGB`.
  - Normal, Roughness, Specular, and Height/Displacement maps MUST always use `Non-Color`.
- **Principled BSDF Connections:**
  - Base Color -> Principled BSDF `Base Color`.
  - Normal Map -> `ShaderNodeNormalMap` (Tangent Space) -> Principled BSDF `Normal`.
  - Roughness -> Principled BSDF `Roughness`.
  - Displacement -> `ShaderNodeDisplacement` -> Material Output `Displacement`.
- **Vectorized Math:** All normal map (Sobel) and roughness/specular filters must use vectorized NumPy operations on padded arrays for instant sub-second calculation.
