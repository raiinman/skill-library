# Source and Reverse Engineering Provenance

- **Upstream Asset:** `Ai.Fy - Text To Image – Unity`
- **Developer / Publisher:** AiKodex (Unity Asset Store)
- **Original Package:** `Ai.Fy - Text To Image - Unity.unitypackage` (2.45 GB)
- **Target Platform:** Blender 4.0+, 4.2+ LTS, 5.0+, and 5.2+ LTS
- **Reverse Engineered & Adapted:** 2026-10-22 using REA (Reverse Engineer Anything) methodologies.

## Technical Reverse Engineering Findings

1. **Architecture Decomposition:**
   - The upstream Unity asset contained two parallel subsystems:
     - `AifyEditor.cs`: Online cloud editor verifying Asset Store invoices against an external HTTP licensing endpoint (`http://3.219.85.134:5000/verify`).
     - `OfflineAifyEditor.cs`: Offline local editor that executed an embedded Python process (`main.py`) using Unity's `PythonRunner`.
   - `NormalMapper.cs`: C# algorithmic texture filters for Normal Map generation (3x3 spatial Sobel gradient) and Specular Map generation (grayscale luminance squared with contrast multiplier and cutoff threshold).

2. **Neural Model Pipeline:**
   - The embedded diffusion model in `Assets/Aify/DiffusionModel/` is a complete ONNX-exported Stable Diffusion pipeline formatted for HuggingFace `diffusers.OnnxStableDiffusionPipeline`:
     - UNet (`unet/model.onnx`, `unet/weights.pb` - 1.65 GB)
     - CLIP Text Encoder (`text_encoder/model.onnx` - 650 MB)
     - VAE Decoder (`vae_decoder/model.onnx`, `vae_decoder/weights.pb` - 94 MB)
     - VAE Encoder (`vae_encoder/model.onnx` - 130 MB)
     - Tokenizer (`vocab.json`, `merges.txt`)
     - PNDM Scheduler (`scheduler/scheduler_config.json`)
   - Hardware acceleration uses `onnxruntime-directml` (`DmlExecutionProvider`), enabling GPU acceleration on Windows across AMD, NVIDIA, and Intel hardware without CUDA.

3. **Blender Reconstruction:**
   - Ported C# editor window into a native Blender Add-on (`aify_blender`) compatible with Blender 4.x and 5.x LTS.
   - Re-implemented all C# `NormalMapper.cs` image processing in pure vectorized NumPy (`pbr_tools.py`), eliminating all external image library dependencies inside Blender.
   - Added asynchronous subprocess execution with `bpy.app.timers` non-blocking progress polling.
   - Implemented automated Principled BSDF PBR material node graph setup and one-click 3D display plane spawning.
