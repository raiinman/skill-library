"""
Ai.Fy - Text To Image & PBR Texture Toolkit for Blender.
Reconstructed from the Unity asset Ai.Fy by AiKodex.
Supports offline ONNX Stable Diffusion inference with DirectML GPU acceleration,
preset prompt libraries, Sobel normal map filtering, and automated PBR material node trees.
"""

bl_info = {
    "name": "Ai.Fy - Text To Image & PBR Textures",
    "author": "Reconstructed from AiKodex Ai.Fy by Antigravity",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "3D View > Sidebar > Ai.Fy / Image Editor > Sidebar > Ai.Fy",
    "description": "Offline Text-to-Image Diffusion (DirectML/CPU) and PBR Texture Synthesis (Normal, Roughness, Height) in Blender.",
    "category": "Paint",
    "doc_url": "https://github.com/raiinman/skill-library",
}

import bpy
from bpy.props import PointerProperty

from .properties import AifySettings
from .operators import (
    AIFY_OT_shuffle_prompt,
    AIFY_OT_randomize_seed,
    AIFY_OT_generate_image,
    AIFY_OT_cancel_generation,
    AIFY_OT_generate_normal,
    AIFY_OT_generate_roughness,
    AIFY_OT_generate_displacement,
    AIFY_OT_setup_pbr,
    AIFY_OT_spawn_plane
)
from .panels import (
    VIEW3D_PT_aify_main,
    VIEW3D_PT_aify_pbr,
    VIEW3D_PT_aify_paths,
    IMAGE_PT_aify_tools
)

CLASSES = [
    AifySettings,
    AIFY_OT_shuffle_prompt,
    AIFY_OT_randomize_seed,
    AIFY_OT_generate_image,
    AIFY_OT_cancel_generation,
    AIFY_OT_generate_normal,
    AIFY_OT_generate_roughness,
    AIFY_OT_generate_displacement,
    AIFY_OT_setup_pbr,
    AIFY_OT_spawn_plane,
    VIEW3D_PT_aify_main,
    VIEW3D_PT_aify_pbr,
    VIEW3D_PT_aify_paths,
    IMAGE_PT_aify_tools
]


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)
    bpy.types.Scene.aify_settings = PointerProperty(type=AifySettings)
    print("[Ai.Fy] Registered Ai.Fy Text To Image & PBR Toolkit for Blender")


def unregister():
    if hasattr(bpy.types.Scene, "aify_settings"):
        del bpy.types.Scene.aify_settings
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
    print("[Ai.Fy] Unregistered Ai.Fy")


if __name__ == "__main__":
    register()
