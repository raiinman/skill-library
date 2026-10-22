import { readFile, readdir, lstat } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { parseDocument } from 'yaml';

const order = (a, b) => a < b ? -1 : a > b ? 1 : 0;
export const sha256 = value => createHash('sha256').update(value).digest('hex');
const json = value => JSON.stringify(value, null, 2) + '\n';
export { json };

export function parseSkill(text, file = 'SKILL.md') {
  const match = text.replace(/^\uFEFF/, '').match(/^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/);
  if (!match) throw new Error(`${file}: missing YAML frontmatter`);
  const doc = parseDocument(match[1], { uniqueKeys: true });
  if (doc.errors.length) throw new Error(`${file}: ${doc.errors.map(e => e.message).join('; ')}`);
  const data = doc.toJS();
  if (!data || typeof data !== 'object' || Array.isArray(data)) throw new Error(`${file}: frontmatter must be a mapping`);
  for (const key of ['name', 'description']) {
    if (typeof data[key] !== 'string' || !data[key].trim()) throw new Error(`${file}: ${key} must be a nonempty string`);
  }
  if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(data.name)) throw new Error(`${file}: invalid native name ${data.name}`);
  return data;
}

async function walk(root, relative) {
  const result = [];
  for (const entry of (await readdir(path.join(root, relative), { withFileTypes: true })).sort((a,b) => order(a.name,b.name))) {
    const file = `${relative}/${entry.name}`;
    if (entry.isSymbolicLink()) throw new Error(`Symlink is not an immutable package resource: ${file}`);
    if (entry.isDirectory()) result.push(...await walk(root, file));
    else if (entry.isFile()) result.push(file);
  }
  return result;
}

// Match Git's clean text bytes, so Windows autocrlf does not alter the index.
// Explicit -text snapshots and binary assets remain byte-for-byte intact.
export function cleanContent(buffer, textAttribute = 'auto') {
  if (textAttribute === 'unset' || (textAttribute !== 'set' && buffer.subarray(0, 8000).includes(0))) return buffer;
  return Buffer.from(buffer.toString('latin1').replace(/\r\n/g, '\n'), 'latin1');
}

function attributes(root, files) {
  const out = execFileSync('git', ['check-attr', '-z', '--stdin', 'text', 'filter', 'working-tree-encoding'], {
    cwd: root, input: files.join('\0') + '\0', encoding: 'utf8', maxBuffer: 16 * 1024 * 1024,
  }).split('\0');
  const result = new Map();
  for (let i = 0; i + 2 < out.length; i += 3) {
    const [file, attr, value] = out.slice(i, i + 3);
    if (attr !== 'text' && !['unspecified', 'unset'].includes(value)) throw new Error(`Unsupported Git ${attr} conversion on ${file}; cannot promise remote hashes`);
    if (attr === 'text') result.set(file, value);
  }
  return result;
}

export function markdownReferences(text) {
  const refs = [];
  // Fenced examples are not retrieval instructions. Inline code labels remain valid links.
  const prose = text.replace(/^(`{3,}|~{3,})[^\n]*\n[\s\S]*?^\1[^\n]*(?:\n|$)/gm, match => match.replace(/[^\n]/g, ' '));
  const patterns = [ /!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+["'][^\n]*["'])?\s*\)/g, /^\s*\[[^\]\n]+\]:\s*(<[^>]+>|\S+)/gm ];
  for (const pattern of patterns) {
    for (const match of prose.matchAll(pattern)) {
      const target = match[1].replace(/^<|>$/g, '');
      if (!target || target.startsWith('#') || /^(?:[a-z][a-z0-9+.-]*:|\/\/)/i.test(target)) continue;
      refs.push({ target, line: prose.slice(0, match.index).split('\n').length });
    }
  }
  return refs.sort((a,b) => a.line - b.line || order(a.target,b.target));
}

export async function buildIndex(root) {
  const sources = JSON.parse(await readFile(path.join(root, 'sources.json'), 'utf8'));
  if (!Array.isArray(sources)) throw new Error('sources.json must be an array');
  const expected = new Map();
  for (const source of sources) {
    if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(source.category) || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(source.name)) throw new Error('Invalid source category/name');
    const canonical = `skills/${source.category}/${source.name}`;
    if (source.path !== canonical) throw new Error(`Noncanonical source path: ${source.path}`);
    if (expected.has(canonical)) throw new Error(`Duplicate canonical source: ${canonical}`);
    expected.set(canonical, source);
  }
  const discovered = [];
  for (const category of await readdir(path.join(root, 'skills'), { withFileTypes: true })) {
    if (!category.isDirectory()) continue;
    for (const skill of await readdir(path.join(root, 'skills', category.name), { withFileTypes: true })) {
      if (!skill.isDirectory()) continue;
      const packagePath = `skills/${category.name}/${skill.name}`;
      try { if ((await lstat(path.join(root, packagePath, 'SKILL.md'))).isFile()) discovered.push(packagePath); }
      catch (error) { if (error.code !== 'ENOENT') throw error; }
    }
  }
  for (const found of discovered) if (!expected.has(found)) throw new Error(`Unregistered canonical package: ${found}`);
  for (const required of expected.keys()) if (!discovered.includes(required)) throw new Error(`Missing canonical package: ${required}`);
  const packageFiles = new Map();
  for (const packagePath of [...expected.keys()].sort(order)) packageFiles.set(packagePath, await walk(root, packagePath));
  const attrs = attributes(root, [...packageFiles.values()].flat());
  const skills = [], references = [];
  const names = new Set();
  for (const [packagePath, files] of packageFiles) {
    const source = expected.get(packagePath), fileRecords = [];
    const texts = new Map();
    for (const file of files) {
      const content = cleanContent(await readFile(path.join(root, file)), attrs.get(file));
      fileRecords.push({ path: file, sha256: sha256(content), bytes: content.length });
      if (file.endsWith('.md')) texts.set(file, content.toString('utf8'));
    }
    const entrypoint = `${packagePath}/SKILL.md`;
    const native = parseSkill(texts.get(entrypoint), entrypoint);
    if (native.name !== source.name) throw new Error(`${entrypoint}: native name differs from sources.json`);
    if (names.has(native.name)) throw new Error(`Ambiguous duplicate native name: ${native.name}`);
    names.add(native.name);
    const packageRefs = [];
    for (const [file, text] of texts) {
      for (const ref of markdownReferences(text)) {
        let target;
        try { target = decodeURIComponent(ref.target.split(/[?#]/)[0]); }
        catch { target = ref.target; }
        const resolved = path.posix.resolve('/', path.posix.dirname(file), target).slice(1);
        const inside = resolved === packagePath || resolved.startsWith(packagePath + '/');
        let exists = false;
        if (inside) { try { await lstat(path.join(root, resolved)); exists = true; } catch (error) { if (error.code !== 'ENOENT') throw error; } }
        const archived = /\/(?:upstream|original)(?:\/|-)|\/references\/upstream-/i.test(file);
        const record = { skill: `${source.category}/${source.name}`, file, ...ref, resolved_path: resolved, status: !inside ? 'outside-package' : exists ? 'resolved' : 'missing', archived };
        packageRefs.push(record);
        references.push(record);
      }
    }
    const { metadata, ...nativeMetadata } = native;
    skills.push({
      id: `${source.category}/${source.name}`, name: source.name, category: source.category, path: entrypoint,
      description: native.description, native_metadata: nativeMetadata,
      routing_metadata: metadata?.dsi ?? {}, custom_metadata: metadata ?? {}, provenance: source,
      package_sha256: sha256(json(fileRecords)), files: fileRecords,
      resource_status: { missing_local_references: packageRefs.filter(r => r.status !== 'resolved' && !r.archived).length, archived_reference_issues: packageRefs.filter(r => r.status !== 'resolved' && r.archived).length },
    });
  }
  const categories = [...new Set(skills.map(s => s.category))].sort(order);
  const content_sha256 = sha256(json(skills));
  const resources = { schema_version: 1, repository: { owner: 'raiinman', name: 'skill-library', branch: 'main' }, hash_policy: 'sha256 of Git-clean text (CRLF normalized except -text) or original binary bytes; no custom Git filters', content_sha256, count: skills.length, categories, skills };
  const index = { schema_version: 1, repository: resources.repository, content_sha256, count: skills.length, categories, resource_manifest: 'skill-resources.json', provenance_manifest: 'sources.json', skills: skills.map(({ id,name,category,path,description,routing_metadata,resource_status }) => ({ id,name,category,path,description,routing_metadata,resource_status })) };
  const report = { schema_version: 1, content_sha256, scope: 'Markdown inline links and reference definitions outside fenced examples, in canonical packages; archived snapshots reported separately. Runtime capabilities and bare prose/code paths require task-time checking.', counts: { references: references.length, active_issues: references.filter(r => r.status !== 'resolved' && !r.archived).length, archived_issues: references.filter(r => r.status !== 'resolved' && r.archived).length }, references };
  const snapshot = { schema_version: 1, content_sha256, count: skills.length, categories, skills: skills.map(({ id,name,category,path,description,routing_metadata }) => ({ id,name,category,path,description,routing_metadata })) };
  return { index, resources, report, snapshot };
}
