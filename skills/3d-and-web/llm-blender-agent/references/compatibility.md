# Compatibility and runtime status

This is a Codex adapter for an application, not an original SKILL.md import. The source archive preserves all 56 tracked files, including UI, provider clients, Blender add-on, socket client, Hunyuan integration and images.

On Blender 5.2.1 LTS, the original add-on imported, registered and unregistered in an isolated background process. No socket server, network request, paid provider or model download ran. Ordinary Codex modeling uses native Blender without the Gradio/provider environment. The optional app's SDK dependencies and cloud accounts are not configured. Source config keys are blank.

The add-on's Hunyuan URL points to a private LAN address from the author. Replace it with the actual user-selected endpoint before a generation request. Its socket accepts Python execution and is not a Codex MCP registration by itself. Keep it on loopback; do not expose the listener. A separate official/legacy bridge may use the same port, so check existing services before starting another server.

Historical provider/model IDs and API adapters need current documentation and account-specific verification if the user chooses the external app. The root LICENSE says Apache-2.0 despite the README's MIT sentence. Full-app generation, remote downloads, provider streaming and Hunyuan were not tested.
