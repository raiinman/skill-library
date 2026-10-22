"""
Standalone Inference Runner for Ai.Fy ONNX Diffusion Model.
Runs in a background subprocess to avoid freezing Blender's UI.
Supports both DirectML GPU acceleration and CPU execution, plus a procedural mock fallback.
"""

import sys
import os
import argparse
import json
import time
import struct
import zlib
import numpy as np


def write_raw_png(filename, width, height, rgb_bytes):
    """Zero-dependency pure-python PNG writer using zlib."""
    def chunk(tag, data):
        return struct.pack("!I", len(data)) + tag + data + struct.pack("!I", zlib.crc32(tag + data) & 0xffffffff)
    
    ihdr = struct.pack("!IIBBBBB", width, height, 8, 2, 0, 0, 0)
    raw_lines = bytearray()
    row_bytes = width * 3
    for y in range(height):
        raw_lines.append(0)  # Filter type None
        start = y * row_bytes
        raw_lines.extend(rgb_bytes[start : start + row_bytes])
    idat = zlib.compress(raw_lines, 6)
    
    with open(filename, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(chunk(b"IHDR", ihdr))
        f.write(chunk(b"IDAT", idat))
        f.write(chunk(b"IEND", b""))


def parse_args():
    parser = argparse.ArgumentParser(description="Ai.Fy ONNX Stable Diffusion Runner")
    parser.add_argument("--prompt", type=str, required=True, help="Text prompt")
    parser.add_argument("--negative-prompt", type=str, default="", help="Negative prompt")
    parser.add_argument("--width", type=int, default=512, help="Image width")
    parser.add_argument("--height", type=int, default=512, help="Image height")
    parser.add_argument("--steps", type=int, default=30, help="Inference steps")
    parser.add_argument("--guidance-scale", type=float, default=7.5, help="Guidance scale")
    parser.add_argument("--seed", type=int, default=1, help="Random seed")
    parser.add_argument("--device", type=str, choices=["dml", "cpu"], default="dml", help="Execution provider")
    parser.add_argument("--models-dir", type=str, required=True, help="Path to DiffusionModel directory")
    parser.add_argument("--output-path", type=str, required=True, help="Destination PNG path")
    parser.add_argument("--mode", type=str, choices=["onnx", "mock"], default="onnx", help="Inference mode")
    return parser.parse_args()


def generate_mock_texture(prompt: str, width: int, height: int, seed: int, output_path: str):
    """Generate high-quality procedural pattern for testing and offline preview."""
    np.random.seed(seed % 2147483647)
    
    # Generate multi-frequency coordinates
    y, x = np.mgrid[0:height, 0:width]
    fx = x / float(width)
    fy = y / float(height)
    
    # Harmonic waves based on prompt hash and seed
    h_val = sum(ord(c) for c in prompt) % 360
    color_base = np.array([
        0.5 + 0.4 * np.sin(fx * 6.28 + h_val * 0.01),
        0.5 + 0.4 * np.cos(fy * 6.28 + seed * 0.02),
        0.5 + 0.3 * np.sin((fx + fy) * 12.56)
    ]).transpose((1, 2, 0))
    
    # Add cellular/tile variation
    grid_x = (x % (width // 8)) / float(width // 8)
    grid_y = (y % (height // 8)) / float(height // 8)
    dist_to_center = np.sqrt((grid_x - 0.5)**2 + (grid_y - 0.5)**2)
    tile_pattern = np.clip(1.0 - dist_to_center * 1.5, 0.0, 1.0)[..., np.newaxis]
    
    # Mix textures
    final_rgb = color_base * 0.7 + tile_pattern * 0.3
    final_rgb = np.clip(final_rgb * 255.0, 0, 255).astype(np.uint8)
    
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    write_raw_png(output_path, width, height, final_rgb.tobytes())
    return output_path


def run_onnx_inference(args):
    """Execute ONNX Stable Diffusion inference with DirectML or CPU."""
    try:
        import onnxruntime as ort
        from diffusers import OnnxStableDiffusionPipeline
    except ImportError as e:
        print(json.dumps({
            "status": "fallback_mock",
            "warning": f"Required packages not found ({e}). Falling back to procedural generation.",
            "output_path": generate_mock_texture(args.prompt, args.width, args.height, args.seed, args.output_path)
        }))
        return

    models_dir = os.path.abspath(args.models_dir)
    unet_dir = os.path.join(models_dir, "unet")
    if not os.path.exists(unet_dir):
        raise FileNotFoundError(f"UNet directory not found at {unet_dir}")

    sess_options = ort.SessionOptions()
    sess_options.enable_mem_pattern = False

    provider = "DmlExecutionProvider" if args.device == "dml" else "CPUExecutionProvider"
    print(f"[Ai.Fy Runner] Loading pipeline from {models_dir} with provider {provider}...", file=sys.stderr)

    generator = np.random
    generator.seed(args.seed)

    pipe = OnnxStableDiffusionPipeline.from_pretrained(
        models_dir,
        provider=provider,
        sess_options=sess_options,
        safety_checker=None
    )

    print(f"[Ai.Fy Runner] Starting diffusion: steps={args.steps}, cfg={args.guidance_scale}...", file=sys.stderr)
    result = pipe(
        prompt=args.prompt,
        negative_prompt=args.negative_prompt if args.negative_prompt else None,
        width=args.width,
        height=args.height,
        num_inference_steps=args.steps,
        guidance_scale=args.guidance_scale,
        generator=generator
    )

    image = result.images[0]
    os.makedirs(os.path.dirname(os.path.abspath(args.output_path)), exist_ok=True)
    image.save(args.output_path)
    print(json.dumps({
        "status": "success",
        "output_path": os.path.abspath(args.output_path),
        "seed": args.seed
    }))


def main():
    args = parse_args()
    if args.mode == "mock":
        out = generate_mock_texture(args.prompt, args.width, args.height, args.seed, args.output_path)
        print(json.dumps({"status": "success", "output_path": os.path.abspath(out), "seed": args.seed}))
    else:
        run_onnx_inference(args)


if __name__ == "__main__":
    main()
