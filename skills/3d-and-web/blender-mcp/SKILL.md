---
name: blender-mcp
description: Inspect and manipulate Blender through an available MCP connection, extract
  scene/material/animation data and diagnose bridge failures. Use for Blender MCP
  work and export-loss troubleshooting; supports a local bpy fallback.
license: MIT
---

# Blender MCP

Use an available Blender MCP bridge for live scene inspection, targeted edits and viewport evidence. Discover the actual tools first; tool names, ports, integrations and timeout limits vary by server. Identify the intended Blender instance and scene before editing.

## Connection and fallback

Check scene-info, a harmless Python query (such as the Blender version) and viewport capture when supported. If a bridge is missing, report that plainly. For saved-file work, use an installed Blender background process with `bpy` instead of inventing tool calls or blocking work on an optional bridge. A headless process reads the saved scene, not live unsaved changes.

Read [runtime and troubleshooting](references/runtime.md) for connection checks and export decisions. This skill installs instructions; it does not claim to enable an add-on, register a server, or authenticate asset services. Configure a live bridge when needed within the user's authorized scope, using its own current setup documentation.

## Scene inspection and edits

Inspect hierarchy, transforms, modifiers/instances, visibility, materials, linked resources, active actions/NLA, frame range and units. Use structured tools for simple queries and Python for data not exposed by the server. Use iterative traversal for large hierarchies and version-appropriate animation APIs; historical `action.fcurves` examples may not cover layered actions.

Keep work scoped to named objects/collections. Preserve state or checkpoint before changes. For long exports/renders, use the bridge if it supports jobs, otherwise a dedicated background process with an explicit output and a failure exit code. Treat a timeout as an unknown outcome: inspect artifacts before retrying.

For glTF, inspect shader losses, bounds, instances, naming and requested clips after export. Decide modifier evaluation from the required geometry rather than a blanket rule. glTF does not preserve arbitrary Blender procedural node graphs or an unevaluated Array modifier. Inspect exported node names rather than assuming dots/spaces are always rewritten. Keep an uncompressed export and validate each optimization step in the target viewer.

Read [asset services](references/asset-services.md) only when importing external assets. Discover available integrations and user authentication; preserve license/source records and honor the user's generation or spending scope.

Deliver saved artifacts and concrete inspection/render evidence. Report whether the live MCP route or saved-file fallback was used. Original source and its three supporting guides are archived under `references/upstream/` and [upstream-skill.md](references/upstream-skill.md); those contain machine-specific assumptions and unverified universal claims, and are not the active execution procedure. See [SOURCE.md](SOURCE.md).
