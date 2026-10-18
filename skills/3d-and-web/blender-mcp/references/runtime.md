# Runtime and troubleshooting

A skill package is instructions, not a running bridge. Discover the available MCP server and tool schemas instead of guessing names or using another application's tools. Verify target scene identity with a read-only query. If a bridge is configured, inspect its actual host, socket transport, version and add-on status before testing execution and capture. Keep a local bridge bound to loopback and avoid exposing an arbitrary-Python endpoint to the network.

When unavailable, saved-file inspection and exports can run in Blender's bundled Python. Locate Blender, use `--background --factory-startup --disable-autoexec`, load the intended saved file and supply `--python-exit-code 1` before a reviewed script. Use a separate output path. Loading a saved file does not include another Blender window's unsaved edits. A running bridge can be configured as a separate requested setup task using its maintained installation instructions and the actual Codex configuration.

For slow work, prefer the server's background-job feature if present, or CLI for saved files. Timeout length is server-specific. After timeout, check job/artifact status before retrying. A refused connection calls for an add-on/server check, not repeated scene mutation.

For inspection, filter shader nodes by type, handle missing materials and preserve source graphs. Blender animation APIs vary: inspect layered actions, slots and NLA using the installed API rather than assuming every action exposes the old `fcurves` attribute.

Export geometry intentionally: `export_apply=False` is not a universal space-saving solution because modifier-generated geometry may disappear. Blender names are not universally rewritten in glTF; distinguish exported node names from a loader's sanitized runtime names and use explicit stable custom IDs when needed. Compression re-encoding and CLI optimization depend on tool/version/settings; retain raw inputs and compare outputs rather than assuming all re-encoding corrupts meshes or every optimizer necessarily simplifies them.

The local machine has Blender 5.2.1 with usable background Python. No live Blender MCP registration or authenticated asset integration is established by importing these skill instructions. The sibling blender-web-pipeline package provides a tested native export/LOD helper if installed.
