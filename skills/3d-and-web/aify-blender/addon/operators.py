"""
Blender operators for Ai.Fy text-to-image and PBR texture workflows.
"""

import os
import sys
import json
import random
import subprocess
import bpy
from bpy.types import Operator
from .properties import EXAMPLE_PROMPTS
from . import pbr_tools

# Global process handle for asynchronous background generation
_GENERATION_PROCESS = None
_GENERATION_INFO = {}


def find_system_python():
    """Find a Python executable capable of running inference."""
    import shutil
    candidates = [
        r"C:\Users\mikea\AppData\Local\Programs\Python\Python311\python.exe",
        shutil.which("python"),
        shutil.which("python3"),
        sys.executable
    ]
    for c in candidates:
        if c and os.path.exists(c):
            return c
    return sys.executable


class AIFY_OT_shuffle_prompt(Operator):
    """Pick a random curated game/3D prompt preset"""
    bl_idname = "aify.shuffle_prompt"
    bl_label = "Shuffle Prompt"
    bl_description = "Pick a random prompt from curated 3D and game art presets"

    def execute(self, context):
        settings = context.scene.aify_settings
        settings.prompt = random.choice(EXAMPLE_PROMPTS)
        self.report({'INFO'}, "Prompt updated")
        return {'FINISHED'}


class AIFY_OT_randomize_seed(Operator):
    """Generate a new random seed"""
    bl_idname = "aify.randomize_seed"
    bl_label = "Randomize Seed"
    bl_description = "Generate a new random integer seed"

    def execute(self, context):
        settings = context.scene.aify_settings
        settings.seed = random.randint(100000, 999999)
        return {'FINISHED'}


class AIFY_OT_generate_image(Operator):
    """Run text-to-image diffusion inference in background"""
    bl_idname = "aify.generate_image"
    bl_label = "Generate Image"
    bl_description = "Run diffusion model to generate image from text prompt"

    def execute(self, context):
        global _GENERATION_PROCESS, _GENERATION_INFO
        settings = context.scene.aify_settings

        if settings.is_generating:
            self.report({'WARNING'}, "Generation is already in progress.")
            return {'CANCELLED'}

        if not settings.prompt.strip():
            self.report({'ERROR'}, "Please enter a prompt.")
            return {'CANCELLED'}

        out_dir = bpy.path.abspath(settings.output_dir)
        os.makedirs(out_dir, exist_ok=True)
        out_filename = f"{settings.seed}.png"
        out_path = os.path.join(out_dir, out_filename)

        addon_dir = os.path.dirname(os.path.realpath(__file__))
        runner_script = os.path.join(addon_dir, "inference_runner.py")
        python_exe = find_system_python()

        models_dir = bpy.path.abspath(settings.models_dir)

        # Check if model files exist; fallback to mock if models dir missing
        mode = settings.generation_mode
        if mode == "onnx" and not os.path.exists(os.path.join(models_dir, "unet")):
            self.report({'WARNING'}, f"DiffusionModel not found at {models_dir}. Switching to procedural preview mode.")
            mode = "mock"

        cmd = [
            python_exe,
            runner_script,
            "--prompt", settings.prompt,
            "--negative-prompt", settings.negative_prompt,
            "--width", settings.width,
            "--height", settings.height,
            "--steps", str(settings.steps),
            "--guidance-scale", str(settings.guidance_scale),
            "--seed", str(settings.seed),
            "--device", settings.execution_device,
            "--models-dir", models_dir,
            "--output-path", out_path,
            "--mode", mode
        ]

        print(f"[Ai.Fy] Launching generator: {' '.join(cmd)}")
        try:
            _GENERATION_PROCESS = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
            )
        except Exception as e:
            self.report({'ERROR'}, f"Failed to start generator: {e}")
            return {'CANCELLED'}

        settings.is_generating = True
        settings.status_message = "Generating texture in background..."

        _GENERATION_INFO = {
            "out_path": out_path,
            "seed": settings.seed,
            "auto_material": settings.auto_setup_material,
            "auto_plane": settings.auto_create_plane,
            "prompt": settings.prompt,
            "auto_seed": settings.auto_randomize_seed
        }

        # Start timer for background polling
        bpy.app.timers.register(self.poll_generation_status, first_interval=0.2)
        return {'FINISHED'}

    @classmethod
    def poll_generation_status(cls):
        global _GENERATION_PROCESS, _GENERATION_INFO
        if _GENERATION_PROCESS is None:
            return None

        ret = _GENERATION_PROCESS.poll()
        if ret is None:
            # Still running; keep polling
            return 0.2

        # Process has finished
        stdout, stderr = _GENERATION_PROCESS.communicate()
        _GENERATION_PROCESS = None

        context = bpy.context
        scene = getattr(context, "scene", None)
        settings = getattr(scene, "aify_settings", None) if scene else None

        if settings:
            settings.is_generating = False

        if ret != 0:
            err_msg = stderr.strip().splitlines()[-1] if stderr.strip() else f"Process exited with code {ret}"
            print(f"[Ai.Fy Error] {stderr}")
            if settings:
                settings.status_message = f"Error: {err_msg}"
            return None

        out_path = _GENERATION_INFO.get("out_path")
        if not out_path or not os.path.exists(out_path):
            if settings:
                settings.status_message = "Error: Output file was not created"
            return None

        # Load image into Blender
        try:
            # If already open, reload
            img_name = os.path.basename(out_path)
            if img_name in bpy.data.images:
                bpy.data.images.remove(bpy.data.images[img_name])
            
            bl_img = bpy.data.images.load(out_path)
            bl_img.colorspace_settings.name = 'sRGB'
            if settings:
                settings.last_generated_image = bl_img.name
                settings.status_message = f"Success! Generated {bl_img.name}"

            # Auto setup material or plane
            if _GENERATION_INFO.get("auto_material"):
                # Automatically generate Normal and Roughness
                normal_img = pbr_tools.generate_normal_map(bl_img, strength=settings.normal_strength if settings else 5.0)
                rough_img = pbr_tools.generate_roughness_map(
                    bl_img,
                    contrast=settings.specular_contrast if settings else 1.5,
                    cutoff=settings.specular_cutoff if settings else 0.4,
                    invert_for_roughness=settings.invert_specular if settings else True
                )
                
                target_obj = context.active_object if context else None
                mat_name = f"M_Aify_{_GENERATION_INFO.get('seed')}"
                mat = pbr_tools.create_pbr_material(
                    mat_name,
                    base_color_img=bl_img,
                    normal_img=normal_img,
                    roughness_img=rough_img,
                    target_object=target_obj
                )

                if _GENERATION_INFO.get("auto_plane"):
                    # Spawn plane mesh and assign material
                    bpy.ops.mesh.primitive_plane_add(size=2.0, enter_editmode=False, location=(0, 0, 0))
                    plane_obj = context.active_object
                    plane_obj.name = f"Aify_Canvas_{_GENERATION_INFO.get('seed')}"
                    plane_obj.data.materials.append(mat)

            if _GENERATION_INFO.get("auto_seed") and settings:
                settings.seed = random.randint(100000, 999999)

        except Exception as e:
            print(f"[Ai.Fy Error loading image] {e}")
            if settings:
                settings.status_message = f"Error loading image: {e}"

        # Redraw viewports
        for window in bpy.context.window_manager.windows:
            for area in window.screen.areas:
                area.tag_redraw()

        return None


class AIFY_OT_cancel_generation(Operator):
    """Cancel currently running generation"""
    bl_idname = "aify.cancel_generation"
    bl_label = "Cancel Generation"
    bl_description = "Stop active background diffusion generation"

    def execute(self, context):
        global _GENERATION_PROCESS
        if _GENERATION_PROCESS is not None:
            _GENERATION_PROCESS.terminate()
            _GENERATION_PROCESS = None
        settings = context.scene.aify_settings
        settings.is_generating = False
        settings.status_message = "Generation cancelled."
        return {'FINISHED'}


class AIFY_OT_generate_normal(Operator):
    """Generate Normal Map from active or selected image"""
    bl_idname = "aify.generate_normal"
    bl_label = "Generate Normal Map"
    bl_description = "Compute Sobel tangent-space normal map using NumPy filter"

    def execute(self, context):
        settings = context.scene.aify_settings
        img_name = settings.last_generated_image
        if not img_name or img_name not in bpy.data.images:
            # Check if active image in image editor
            for area in context.screen.areas:
                if area.type == 'IMAGE_EDITOR' and area.spaces.active.image:
                    img_name = area.spaces.active.image.name
                    break

        if not img_name or img_name not in bpy.data.images:
            self.report({'ERROR'}, "No valid image found to generate Normal map.")
            return {'CANCELLED'}

        src_img = bpy.data.images[img_name]
        out_img = pbr_tools.generate_normal_map(src_img, strength=settings.normal_strength)
        self.report({'INFO'}, f"Generated Normal map: {out_img.name}")
        return {'FINISHED'}


class AIFY_OT_generate_roughness(Operator):
    """Generate Roughness Map from active or selected image"""
    bl_idname = "aify.generate_roughness"
    bl_label = "Generate Roughness Map"
    bl_description = "Compute contrast-filtered roughness map from image luminance"

    def execute(self, context):
        settings = context.scene.aify_settings
        img_name = settings.last_generated_image
        if not img_name or img_name not in bpy.data.images:
            for area in context.screen.areas:
                if area.type == 'IMAGE_EDITOR' and area.spaces.active.image:
                    img_name = area.spaces.active.image.name
                    break

        if not img_name or img_name not in bpy.data.images:
            self.report({'ERROR'}, "No valid image found to generate Roughness map.")
            return {'CANCELLED'}

        src_img = bpy.data.images[img_name]
        out_img = pbr_tools.generate_roughness_map(
            src_img,
            contrast=settings.specular_contrast,
            cutoff=settings.specular_cutoff,
            invert_for_roughness=settings.invert_specular
        )
        self.report({'INFO'}, f"Generated Roughness map: {out_img.name}")
        return {'FINISHED'}


class AIFY_OT_generate_displacement(Operator):
    """Generate Height / Displacement Map"""
    bl_idname = "aify.generate_displacement"
    bl_label = "Generate Height Map"
    bl_description = "Compute normalized height/displacement map from image luminance"

    def execute(self, context):
        settings = context.scene.aify_settings
        img_name = settings.last_generated_image
        if not img_name or img_name not in bpy.data.images:
            for area in context.screen.areas:
                if area.type == 'IMAGE_EDITOR' and area.spaces.active.image:
                    img_name = area.spaces.active.image.name
                    break

        if not img_name or img_name not in bpy.data.images:
            self.report({'ERROR'}, "No valid image found to generate Height map.")
            return {'CANCELLED'}

        src_img = bpy.data.images[img_name]
        out_img = pbr_tools.generate_displacement_map(src_img)
        self.report({'INFO'}, f"Generated Height map: {out_img.name}")
        return {'FINISHED'}


class AIFY_OT_setup_pbr(Operator):
    """Create complete Principled BSDF PBR material from current image set"""
    bl_idname = "aify.setup_pbr"
    bl_label = "Setup PBR Material"
    bl_description = "Connect Base Color, Normal Map, and Roughness to Principled BSDF on active object"

    def execute(self, context):
        settings = context.scene.aify_settings
        base_name = settings.last_generated_image
        if not base_name or base_name not in bpy.data.images:
            self.report({'ERROR'}, "No Base Color image selected.")
            return {'CANCELLED'}

        base_img = bpy.data.images[base_name]
        stem = base_name.rsplit('.', 1)[0]
        normal_img = bpy.data.images.get(f"{stem}_normal") or bpy.data.images.get(f"{stem}_normal.png")
        rough_img = bpy.data.images.get(f"{stem}_roughness") or bpy.data.images.get(f"{stem}_roughness.png")
        disp_img = bpy.data.images.get(f"{stem}_displacement") or bpy.data.images.get(f"{stem}_displacement.png")

        # Generate missing maps on demand
        if not normal_img:
            normal_img = pbr_tools.generate_normal_map(base_img, strength=settings.normal_strength)
        if not rough_img:
            rough_img = pbr_tools.generate_roughness_map(
                base_img,
                contrast=settings.specular_contrast,
                cutoff=settings.specular_cutoff,
                invert_for_roughness=settings.invert_specular
            )

        mat_name = f"M_{stem}"
        mat = pbr_tools.create_pbr_material(
            mat_name,
            base_color_img=base_img,
            normal_img=normal_img,
            roughness_img=rough_img,
            displacement_img=disp_img,
            target_object=context.active_object
        )
        self.report({'INFO'}, f"Configured PBR Material: {mat.name}")
        return {'FINISHED'}


class AIFY_OT_spawn_plane(Operator):
    """Spawn a 3D Plane displaying the generated PBR material"""
    bl_idname = "aify.spawn_plane"
    bl_label = "Spawn Display Plane"
    bl_description = "Create a 3D Plane mesh and assign the active Ai.Fy PBR material"

    def execute(self, context):
        bpy.ops.mesh.primitive_plane_add(size=2.0, enter_editmode=False, location=(0, 0, 0))
        plane = context.active_object
        plane.name = "Aify_Texture_Plane"

        settings = context.scene.aify_settings
        stem = settings.last_generated_image.rsplit('.', 1)[0]
        mat_name = f"M_{stem}"
        mat = bpy.data.materials.get(mat_name)
        if mat:
            plane.data.materials.append(mat)
            self.report({'INFO'}, f"Assigned material {mat.name} to {plane.name}")
        return {'FINISHED'}
