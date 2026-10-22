"""
PBR Texture Processing Tools for Blender.
Vectorized implementation of Normal, Roughness/Specular, and Height generation algorithms
reconstructed from the Ai.Fy Unity asset (NormalMapper.cs).
"""

import bpy
import numpy as np


def get_image_rgb_array(image: bpy.types.Image) -> np.ndarray:
    """Extract RGB float array of shape (H, W, 3) with values in [0, 1]."""
    w, h = image.size[0], image.size[1]
    if w == 0 or h == 0:
        raise ValueError("Image has 0 dimensions.")
    
    px = np.zeros(w * h * 4, dtype=np.float32)
    image.pixels.foreach_get(px)
    rgba = px.reshape((h, w, 4))
    return rgba[..., :3]


def create_or_get_image(name: str, width: int, height: int, colorspace: str = 'sRGB') -> bpy.types.Image:
    """Create a new bpy.data.images with specified colorspace."""
    if name in bpy.data.images:
        bpy.data.images.remove(bpy.data.images[name])
    img = bpy.data.images.new(name, width=width, height=height)
    try:
        if img.colorspace_settings.name != colorspace:
            img.colorspace_settings.name = colorspace
    except Exception:
        pass
    return img


def generate_normal_map(source_image: bpy.types.Image, strength: float = 5.0, name_suffix: str = "_normal") -> bpy.types.Image:
    """
    Generate tangent-space normal map using Sobel gradient filters.
    Faithful vectorized port of Ai.Fy's NormalMapper.cs CreateNormalmap.
    """
    w, h = source_image.size[0], source_image.size[1]
    rgb = get_image_rgb_array(source_image)
    
    # Calculate luminance: 0.3333 * (R + G + B)
    gray = np.dot(rgb, [0.3333, 0.3333, 0.3333])
    
    # Pad borders with edge values to handle boundaries seamlessly
    padded = np.pad(gray, 1, mode='edge')
    
    # Extract 3x3 neighbor slices
    # Row 0: y - 1, Row 1: y, Row 2: y + 1
    # Col 0: x - 1, Col 1: x, Col 2: x + 1
    s_negX_negY = padded[0:h, 0:w]
    s_zerX_negY = padded[0:h, 1:w+1]
    s_posX_negY = padded[0:h, 2:w+2]
    
    s_negX_zerY = padded[1:h+1, 0:w]
    s_posX_zerY = padded[1:h+1, 2:w+2]
    
    s_negX_posY = padded[2:h+2, 0:w]
    s_zerX_posY = padded[2:h+2, 1:w+1]
    s_posX_posY = padded[2:h+2, 2:w+2]
    
    # Sobel gradient calculation
    edgeX = (s_posX_negY - s_negX_negY) * 0.25 + (s_posX_zerY - s_negX_zerY) * 0.5 + (s_posX_posY - s_negX_posY) * 0.25
    edgeY = (s_negX_posY - s_negX_negY) * 0.25 + (s_zerX_posY - s_zerX_negY) * 0.5 + (s_posX_posY - s_posX_negY) * 0.25
    
    vx = edgeX * float(strength)
    vy = edgeY * float(strength)
    vz = np.ones_like(vx)
    
    # Normalize 3D vectors
    length = np.sqrt(vx**2 + vy**2 + vz**2)
    length[length == 0] = 1.0
    
    norm_x = vx / length * 0.5 + 0.5
    norm_y = vy / length * 0.5 + 0.5
    norm_z = vz / length * 0.5 + 0.5
    
    out_rgba = np.zeros((h, w, 4), dtype=np.float32)
    out_rgba[..., 0] = norm_x
    out_rgba[..., 1] = norm_y
    out_rgba[..., 2] = norm_z
    out_rgba[..., 3] = 1.0
    
    out_name = f"{source_image.name.rsplit('.', 1)[0]}{name_suffix}"
    out_img = create_or_get_image(out_name, w, h, colorspace='Non-Color')
    out_img.pixels.foreach_set(out_rgba.ravel())
    out_img.update()
    try:
        out_img.pack()
    except Exception:
        pass
    return out_img


def generate_roughness_map(source_image: bpy.types.Image, contrast: float = 1.5, cutoff: float = 0.4, invert_for_roughness: bool = True, name_suffix: str = "_roughness") -> bpy.types.Image:
    """
    Generate Roughness / Smoothness map.
    Reconstructed from NormalMapper.cs CreateSpecular:
    bw = gray * gray * contrast
    bw = -1 if bw < (contrast * cutoff) else bw
    bw = clamp(bw, -1, 1) * 0.5 + 0.5
    """
    w, h = source_image.size[0], source_image.size[1]
    rgb = get_image_rgb_array(source_image)
    
    # Grayscale
    gray = np.dot(rgb, [0.3333, 0.3333, 0.3333])
    
    # Non-linear contrast transfer function
    bw = gray * gray * float(contrast)
    cutoff_threshold = float(contrast * cutoff)
    bw = np.where(bw < cutoff_threshold, -1.0, bw)
    bw = np.clip(bw, -1.0, 1.0) * 0.5 + 0.5
    
    if invert_for_roughness:
        # Invert smoothness (specular) to roughness for Principled BSDF
        bw = 1.0 - bw
        
    out_rgba = np.zeros((h, w, 4), dtype=np.float32)
    out_rgba[..., 0] = bw
    out_rgba[..., 1] = bw
    out_rgba[..., 2] = bw
    out_rgba[..., 3] = 1.0
    
    out_name = f"{source_image.name.rsplit('.', 1)[0]}{name_suffix}"
    out_img = create_or_get_image(out_name, w, h, colorspace='Non-Color')
    out_img.pixels.foreach_set(out_rgba.ravel())
    out_img.update()
    try:
        out_img.pack()
    except Exception:
        pass
    return out_img


def generate_displacement_map(source_image: bpy.types.Image, name_suffix: str = "_displacement") -> bpy.types.Image:
    """Generate normalized height/displacement map from luminance."""
    w, h = source_image.size[0], source_image.size[1]
    rgb = get_image_rgb_array(source_image)
    gray = np.dot(rgb, [0.299, 0.587, 0.114])
    
    min_val, max_val = gray.min(), gray.max()
    if max_val > min_val:
        height = (gray - min_val) / (max_val - min_val)
    else:
        height = gray
        
    out_rgba = np.zeros((h, w, 4), dtype=np.float32)
    out_rgba[..., 0] = height
    out_rgba[..., 1] = height
    out_rgba[..., 2] = height
    out_rgba[..., 3] = 1.0
    
    out_name = f"{source_image.name.rsplit('.', 1)[0]}{name_suffix}"
    out_img = create_or_get_image(out_name, w, h, colorspace='Non-Color')
    out_img.pixels.foreach_set(out_rgba.ravel())
    out_img.update()
    try:
        out_img.pack()
    except Exception:
        pass
    return out_img


def create_pbr_material(
    material_name: str,
    base_color_img: bpy.types.Image,
    normal_img: bpy.types.Image = None,
    roughness_img: bpy.types.Image = None,
    displacement_img: bpy.types.Image = None,
    target_object: bpy.types.Object = None
) -> bpy.types.Material:
    """Create or update a Principled BSDF material connecting all provided PBR maps."""
    if material_name in bpy.data.materials:
        mat = bpy.data.materials[material_name]
    else:
        mat = bpy.data.materials.new(name=material_name)
        
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()
    
    # 1. Material Output Node
    output_node = nodes.new("ShaderNodeOutputMaterial")
    output_node.location = (400, 0)
    
    # 2. Principled BSDF Node
    bsdf_node = nodes.new("ShaderNodeBsdfPrincipled")
    bsdf_node.location = (100, 0)
    links.new(bsdf_node.outputs["BSDF"], output_node.inputs["Surface"])
    
    # 3. Base Color Texture Node
    tex_base = nodes.new("ShaderNodeTexImage")
    tex_base.location = (-300, 200)
    tex_base.image = base_color_img
    links.new(tex_base.outputs["Color"], bsdf_node.inputs["Base Color"])
    
    # 4. Roughness Texture Node
    if roughness_img:
        tex_rough = nodes.new("ShaderNodeTexImage")
        tex_rough.location = (-300, -100)
        tex_rough.image = roughness_img
        links.new(tex_rough.outputs["Color"], bsdf_node.inputs["Roughness"])
        
    # 5. Normal Map Node & Texture Node
    if normal_img:
        tex_norm = nodes.new("ShaderNodeTexImage")
        tex_norm.location = (-550, -400)
        tex_norm.image = normal_img
        
        node_norm_map = nodes.new("ShaderNodeNormalMap")
        node_norm_map.location = (-250, -400)
        links.new(tex_norm.outputs["Color"], node_norm_map.inputs["Color"])
        links.new(node_norm_map.outputs["Normal"], bsdf_node.inputs["Normal"])
        
    # 6. Displacement Node
    if displacement_img:
        tex_disp = nodes.new("ShaderNodeTexImage")
        tex_disp.location = (-300, -700)
        tex_disp.image = displacement_img
        node_disp = nodes.new("ShaderNodeDisplacement")
        node_disp.location = (100, -500)
        links.new(tex_disp.outputs["Color"], node_disp.inputs["Height"])
        links.new(node_disp.outputs["Displacement"], output_node.inputs["Displacement"])
        
    # Assign to target object if supplied
    if target_object and target_object.type == 'MESH':
        if len(target_object.data.materials) == 0:
            target_object.data.materials.append(mat)
        else:
            target_object.data.materials[0] = mat
            
    return mat
