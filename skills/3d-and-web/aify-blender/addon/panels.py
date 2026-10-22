"""
User Interface panels for Ai.Fy Blender Add-on.
"""

import bpy
from bpy.types import Panel


class VIEW3D_PT_aify_main(Panel):
    """Main Ai.Fy Panel in 3D Viewport sidebar"""
    bl_label = "Ai.Fy: Text To Image"
    bl_idname = "VIEW3D_PT_aify_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Ai.Fy'

    def draw(self, context):
        layout = self.layout
        settings = context.scene.aify_settings

        # Status box
        box_status = layout.box()
        row = box_status.row()
        row.label(text="Status:", icon='INFO')
        row.label(text=settings.status_message)

        # Prompt Section
        col = layout.column(align=True)
        col.label(text="Prompt:", icon='TEXT')
        col.prop(settings, "prompt", text="")
        
        row_shuffle = col.row(align=True)
        row_shuffle.operator("aify.shuffle_prompt", text="Shuffle Preset Prompt", icon='FILE_REFRESH')

        col.separator()
        col.label(text="Negative Prompt:", icon='CANCEL')
        col.prop(settings, "negative_prompt", text="")

        # Resolution & Generation Settings
        box_settings = layout.box()
        box_settings.label(text="Generation Parameters", icon='PREFERENCES')

        row_res = box_settings.row(align=True)
        row_res.prop(settings, "width", text="W")
        row_res.prop(settings, "height", text="H")

        row_sliders = box_settings.row(align=True)
        row_sliders.prop(settings, "steps", text="Steps")
        row_sliders.prop(settings, "guidance_scale", text="CFG")

        row_seed = box_settings.row(align=True)
        row_seed.prop(settings, "seed", text="Seed")
        row_seed.operator("aify.randomize_seed", text="", icon='DICE')
        row_seed.prop(settings, "auto_randomize_seed", text="Auto")

        box_backend = layout.box()
        box_backend.label(text="Backend Engine", icon='SETTINGS')
        box_backend.prop(settings, "generation_mode", text="Mode")
        box_backend.prop(settings, "execution_device", text="Device")

        # Main Action Button
        layout.separator()
        if settings.is_generating:
            layout.operator("aify.cancel_generation", text="Cancel Generation", icon='CANCEL')
        else:
            row_gen = layout.row()
            row_gen.scale_y = 1.8
            row_gen.operator("aify.generate_image", text="Generate Image", icon='RENDER_STILL')


class VIEW3D_PT_aify_pbr(Panel):
    """PBR Texture synthesis and material panel"""
    bl_label = "Ai.Fy: PBR Texture Tools"
    bl_idname = "VIEW3D_PT_aify_pbr"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Ai.Fy'

    def draw(self, context):
        layout = self.layout
        settings = context.scene.aify_settings

        # Active image indicator
        box = layout.box()
        box.label(text="Active Texture", icon='IMAGE_DATA')
        box.prop_search(settings, "last_generated_image", bpy.data, "images", text="Source")

        # Normal map controls
        box_norm = layout.box()
        box_norm.label(text="Normal Map (Sobel)", icon='NODE_TEXTURE')
        box_norm.prop(settings, "normal_strength", text="Strength")
        box_norm.operator("aify.generate_normal", text="Generate Normal Map", icon='SNAP_NORMAL')

        # Roughness / Specular controls
        box_rough = layout.box()
        box_rough.label(text="Roughness / Specular", icon='MATERIAL')
        box_rough.prop(settings, "specular_contrast", text="Contrast")
        box_rough.prop(settings, "specular_cutoff", text="Cutoff")
        box_rough.prop(settings, "invert_specular", text="Invert to Roughness")
        box_rough.operator("aify.generate_roughness", text="Generate Roughness Map", icon='NODE_MATERIAL')

        # Height / Displacement
        box_disp = layout.box()
        box_disp.label(text="Displacement / Height", icon='MOD_DISPLACE')
        box_disp.operator("aify.generate_displacement", text="Generate Height Map", icon='MOD_DISPLACE')

        # Full Material Setup
        layout.separator()
        col = layout.column(align=True)
        col.scale_y = 1.4
        col.operator("aify.setup_pbr", text="Setup PBR Material on Active", icon='MATERIAL_DATA')
        col.operator("aify.spawn_plane", text="Spawn Canvas Display Plane", icon='MESH_PLANE')


class VIEW3D_PT_aify_paths(Panel):
    """Paths and Automation Settings"""
    bl_label = "Ai.Fy: Paths & Automation"
    bl_idname = "VIEW3D_PT_aify_paths"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Ai.Fy'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        settings = context.scene.aify_settings

        col = layout.column(align=True)
        col.prop(settings, "models_dir", text="Models Dir")
        col.prop(settings, "output_dir", text="Output Dir")

        col.separator()
        col.prop(settings, "auto_setup_material", text="Auto Setup Material")
        col.prop(settings, "auto_create_plane", text="Auto Spawn Plane")


class IMAGE_PT_aify_tools(Panel):
    """Ai.Fy Texture Tools in Image Editor"""
    bl_label = "Ai.Fy PBR Tools"
    bl_idname = "IMAGE_PT_aify_tools"
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Ai.Fy'

    def draw(self, context):
        layout = self.layout
        settings = context.scene.aify_settings

        col = layout.column(align=True)
        col.prop(settings, "normal_strength", text="Normal Strength")
        col.operator("aify.generate_normal", text="Generate Normal Map", icon='SNAP_NORMAL')

        col.separator()
        col.prop(settings, "specular_contrast", text="Contrast")
        col.prop(settings, "specular_cutoff", text="Cutoff")
        col.prop(settings, "invert_specular", text="Invert to Roughness")
        col.operator("aify.generate_roughness", text="Generate Roughness Map", icon='NODE_MATERIAL')

        col.separator()
        col.operator("aify.generate_displacement", text="Generate Height Map", icon='MOD_DISPLACE')
        col.operator("aify.setup_pbr", text="Setup PBR Material", icon='MATERIAL_DATA')
