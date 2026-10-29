"""
Property definitions and presets for Ai.Fy Blender Add-on.
"""

import bpy
from bpy.props import (
    StringProperty,
    IntProperty,
    FloatProperty,
    BoolProperty,
    EnumProperty,
    PointerProperty
)
from bpy.types import PropertyGroup, AddonPreferences

EXAMPLE_PROMPTS = [
    "Shopping mall, city, sunshine, pixel art",
    "Japanese classroom scene, wooden table chair, tiled floor, green blackboard, teacher, students, pixel art",
    "Axe, sword, mining, character, various assets, pixel art, 8 bit, game design, sprite sheet",
    "Farm isometric, pixel art, detailed, retro design, green, vibrant",
    "car high speed, intense, dynamic, detailed, cartoon style, wide angled, overhead view, vibrant colors, whimsical, absurd, surreal, fun, isometric, low poly, 123rf, gettyimages, illustrator, photoshop",
    "Anime girl, bikini, full body, full chest, curvy, toned abs, minimalistic background, anime waifu, beautiful, good looking girl, anime style, Japanese, manga, otaku",
    "Japanese Beach, blue water, sunny, children, crowded, enjoying, splashes, manga, bright, vibrant, day time, Japan children, 4k",
    "darth vader, standing pose, barren land, greyscale, full body, metallic, render, vray, octane render, 3d model",
    "Vintage sports car with classic curves, captured in a moody, low key light with selective focus on the grille, classic, retro, moody, detailed, 3D model, artstation, blender render, 3ds max render",
    "Game design, cyberpunk style, 3D models",
    "A jungle city, with vines and roots serving as roads and buildings made of leaves, colorful, detailed, natural, tropical",
    "Lonely lighthouse on a rocky coast during a storm, with waves crashing and lightning flashing, moody, atmospheric, seascape, high detail",
    "Powerful sorceress, flowing robes and mystical staff, standing in dark and ominous forest, mysterious, detailed, high detail, fantasy portrait",
    "Editorial Style Photo, Bonsai Apple Tree, Task Lighting, Inspiring and Awesome, Sunset, Afternoon, Beautiful, Symmetric, 4k",
    "Rustic kitchen with exposed brick wall, reclaimed wood cabinetry, large farmhouse sink, industrial lighting fixtures, antique baking tools on open shelving, cast iron cookware, vintage accents, warm and inviting, detailed textures",
    "Luxurious bathroom with freestanding bathtub, rain shower, heated flooring, marble tiles, brass fixtures, floating vanity with double sink, elegant chandelier, high contrast lighting, spa-like atmosphere, high resolution",
    "Skilled archer, bow and quiver of arrows, standing in forest clearing, intense, detailed, high detail, portrait",
    "A medieval town with disco lights and a fountain, by Josef Thoma, matte painting trending on artstation HQ, concept art",
    "Majestic dragon, perched atop a cliff overlooking a fiery landscape, with smoke and ash rising into the air, intense, detailed, scales, dynamic, epic"
]

DIMENSION_OPTIONS = [
    ("512", "512 x 512 (Standard)", "Standard 512x512 resolution"),
    ("768", "768 x 768 (High)", "High quality 768x768 resolution"),
    ("384", "384 x 384 (Fast)", "Fast 384x384 preview"),
    ("256", "256 x 256 (Draft)", "Draft 256x256 resolution"),
    ("448", "448 x 448 (Medium)", "448x448 intermediate resolution"),
    ("320", "320 x 320 (Light)", "320x320 lightweight resolution"),
]

DEVICE_OPTIONS = [
    ("dml", "DirectML (GPU - Direct3D 12)", "Hardware-accelerated inference across Nvidia, AMD, and Intel GPUs via DirectML"),
    ("cpu", "CPU (Standard)", "Run inference on CPU"),
]

MODE_OPTIONS = [
    ("onnx", "Local ONNX Model (DirectML/CPU)", "Use offline ONNX Stable Diffusion models extracted from Ai.Fy"),
    ("mock", "Instant Procedural Pattern (Preview/Test)", "Generate synthetic procedural texture for rapid UI testing and node preview without running heavy model"),
]


class AifySettings(PropertyGroup):
    # Text-to-Image Generation
    prompt: StringProperty(
        name="Prompt",
        description="Text description of the desired image or texture",
        default="Vintage sports car with classic curves, detailed 3D model, blender render"
    )
    
    negative_prompt: StringProperty(
        name="Negative Prompt",
        description="Elements to exclude from the generation",
        default="blurry, distorted, low quality, artifact"
    )
    
    width: EnumProperty(
        name="Width",
        items=DIMENSION_OPTIONS,
        default="512"
    )
    
    height: EnumProperty(
        name="Height",
        items=DIMENSION_OPTIONS,
        default="512"
    )
    
    steps: IntProperty(
        name="Inference Steps",
        description="Number of diffusion denoising steps",
        default=30,
        min=10,
        max=50
    )
    
    guidance_scale: FloatProperty(
        name="Guidance Scale (CFG)",
        description="How closely the generation adheres to the text prompt",
        default=7.5,
        min=1.0,
        max=20.0,
        step=50
    )
    
    seed: IntProperty(
        name="Seed",
        description="Random seed for deterministic generation",
        default=498801,
        min=0
    )
    
    auto_randomize_seed: BoolProperty(
        name="Auto Randomize",
        description="Pick a new random seed on each generation",
        default=True
    )
    
    execution_device: EnumProperty(
        name="Device",
        items=DEVICE_OPTIONS,
        default="dml"
    )
    
    generation_mode: EnumProperty(
        name="Generation Mode",
        items=MODE_OPTIONS,
        default="onnx"
    )
    
    models_dir: StringProperty(
        name="Models Directory",
        description="Path to the extracted Assets/Aify/DiffusionModel directory",
        default=r"C:\Users\mikea\Downloads\Ai.Fy - Text To Image – Unity\DiffusionModel",
        subtype='DIR_PATH'
    )
    
    output_dir: StringProperty(
        name="Output Directory",
        description="Directory where generated textures are saved",
        default=r"C:\Users\mikea\Downloads\Ai.Fy - Text To Image – Unity\GeneratedTextures",
        subtype='DIR_PATH'
    )
    
    auto_create_plane: BoolProperty(
        name="Spawn Mesh Plane",
        description="Automatically create a 3D Plane displaying the generated PBR material",
        default=True
    )
    
    auto_setup_material: BoolProperty(
        name="Auto Setup PBR Material",
        description="Automatically create a Principled BSDF material with generated maps",
        default=True
    )
    
    # Texture Tools / PBR
    normal_strength: FloatProperty(
        name="Normal Strength",
        description="Intensity multiplier for the Sobel normal map filter",
        default=5.0,
        min=0.1,
        max=20.0
    )
    
    specular_contrast: FloatProperty(
        name="Roughness Contrast",
        description="Contrast multiplier for specular/roughness luminance",
        default=1.5,
        min=0.0,
        max=3.0
    )
    
    specular_cutoff: FloatProperty(
        name="Luminance Cutoff",
        description="Threshold below which shadows become non-reflective",
        default=0.4,
        min=0.0,
        max=1.0
    )
    
    invert_specular: BoolProperty(
        name="Invert to Roughness",
        description="Invert specular highlights into Blender standard roughness",
        default=True
    )
    
    last_generated_image: StringProperty(
        name="Last Generated Image",
        description="Name of the most recently generated or imported image",
        default=""
    )
    
    status_message: StringProperty(
        name="Status",
        description="Status of current generation",
        default="Ready"
    )
    
    is_generating: BoolProperty(
        name="Is Generating",
        description="Whether a generation process is currently active",
        default=False
    )
