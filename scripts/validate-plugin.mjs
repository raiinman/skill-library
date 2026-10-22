import { readFile, readdir, lstat } from 'node:fs/promises';
import assert from 'node:assert/strict';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { parseSkill, markdownReferences } from './lib/index.mjs';

const root = fileURLToPath(new URL('../', import.meta.url));
const plugin = path.join(root, 'plugins/dsi-skill-library');
const load = async file => JSON.parse(await readFile(file, 'utf8'));
const manifest = await load(path.join(plugin, 'plugin.json'));
assert.equal(manifest.$schema, 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json');
assert.equal(manifest.name, 'dsi-skill-library');
assert.match(manifest.version, /^\d+\.\d+\.\d+$/);
assert(!('license' in manifest), 'Do not apply a blanket license to imports');
for (const field of ['skills', 'mcpServers', 'apps', 'interface']) assert(!(field in manifest));
const presentation = manifest.extensions['com.openai'].interface;
assert(presentation.shortDescription.length <= 30);
const legacy = await load(path.join(plugin, '.codex-plugin/plugin.json'));
for (const field of ['name', 'version']) assert.equal(legacy[field], manifest[field]);
assert.equal(legacy.skills, './skills/');
for (const field of ['displayName', 'shortDescription', 'developerName', 'category']) {
  assert.equal(legacy.interface[field], presentation[field]);
}
const marketplace = await load(path.join(root, '.agents/plugins/marketplace.json'));
assert.equal(marketplace.name, 'dsi-skill-library');
assert.equal(marketplace.plugins.length, 1);
assert.equal(marketplace.plugins[0].source.path, './plugins/dsi-skill-library');
assert.equal(marketplace.plugins[0].policy.installation, 'AVAILABLE');

let skillCount = 0, fileCount = 0;
async function inspect(directory) {
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const file = path.join(directory, entry.name);
    assert(!entry.isSymbolicLink(), `Symlink in package: ${file}`);
    if (entry.isDirectory()) await inspect(file);
    else {
      fileCount++;
      assert(!/\.(?:env|pem|key)$/.test(file), `Unexpected credential file: ${file}`);
      if (entry.name === 'SKILL.md') {
        const text = await readFile(file, 'utf8');
        const skill = parseSkill(text, file);
        assert.equal(skill.name, path.basename(directory));
        assert.equal(skill.name, 'dsi-library-router');
        skillCount++;
      }
      if (!entry.name.endsWith('.md')) continue;
      for (const ref of markdownReferences(await readFile(file, 'utf8'))) {
        const target = path.resolve(directory, decodeURIComponent(ref.target.split('#')[0]));
        const relative = path.relative(plugin, target);
        assert(!relative.startsWith('..') && !path.isAbsolute(relative), `Reference escapes package: ${file}`);
        await lstat(target);
      }
    }
  }
}
await inspect(plugin);
assert.equal(skillCount, 1, 'Only the router should be bundled');
console.log(`Validated plugin manifests, marketplace, ${skillCount} bundled skill and ${fileCount} package files.`);
