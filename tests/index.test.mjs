import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, mkdir, writeFile, rm, readFile } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildIndex, parseSkill, cleanContent, markdownReferences } from '../scripts/lib/index.mjs';

const repo = fileURLToPath(new URL('../', import.meta.url));
const source = { category: 'example', name: 'sample', path: 'skills/example/sample', repo: 'owner/original', commit: 'a'.repeat(40), license: 'MIT', license_files: ['LICENSE'] };
async function fixture(t) {
  const root = await mkdtemp(path.join(tmpdir(), 'dsi-index-'));
  t.after(() => rm(root, { recursive: true, force: true }));
  execFileSync('git', ['init', '-q'], { cwd: root });
  async function put(file, text) { await mkdir(path.dirname(path.join(root,file)), { recursive: true }); await writeFile(path.join(root,file), text); }
  await put('.gitattributes', '* text=auto\n**/references/upstream-skill.md -text\n');
  await put('sources.json', JSON.stringify([source]));
  await put(source.path + '/LICENSE', 'MIT fixture\n');
  await put(source.path + '/SKILL.md', '---\nname: sample\ndescription: >-\n  Design an example.\n  Use for example work.\nmetadata:\n  dsi:\n    excludes: ordinary conversation\n---\n[Guide](references/guide.md)\n[Missing](references/missing.md)\n[External package](../other/SKILL.md)\n');
  await put(source.path + '/references/guide.md', '# Fixture guide\n');
  await put(source.path + '/references/upstream-skill.md', '[Unavailable historical file](old.md)\r\n');
  return { root, put };
}

test('canonical source inventory uses true YAML, preserves provenance, and excludes duplicate snapshots', async t => {
  const { root, put } = await fixture(t);
  await put('collections/copied/sample/SKILL.md', 'not even YAML');
  await put(source.path + '/archive/nested/SKILL.md', '# Archived entrypoint, never separately registered');
  const { index, resources, snapshot, report } = await buildIndex(root);
  assert.equal(index.count, 1);
  assert.equal(index.skills[0].description, 'Design an example. Use for example work.');
  assert.deepEqual(resources.skills[0].provenance, source);
  assert.deepEqual(index.skills[0].routing_metadata, { excludes: 'ordinary conversation' });
  assert.equal(resources.skills[0].native_metadata.metadata, undefined);
  assert.ok(resources.skills[0].files.some(f => f.path.endsWith('/archive/nested/SKILL.md')));
  assert.equal(snapshot.skills[0].files, undefined);
  assert.equal(snapshot.content_sha256, index.content_sha256);
  assert.equal(report.counts.active_issues, 2);
  assert.equal(report.counts.archived_issues, 1);
  assert.ok(report.references.some(r => r.status === 'outside-package'));
});

test('duplicate, absent, and unregistered canonical entries fail', async t => {
  const { root, put } = await fixture(t);
  await put('sources.json', JSON.stringify([source,source]));
  await assert.rejects(buildIndex(root), /Duplicate canonical source/);
  await put('sources.json', JSON.stringify([{ ...source, name: 'absent', path: 'skills/example/absent' },source]));
  await assert.rejects(buildIndex(root), /Missing canonical package/);
  await put('sources.json', JSON.stringify([]));
  await assert.rejects(buildIndex(root), /Unregistered canonical package/);
});

test('resource edits and source metadata edits change the content identity, repeat builds are identical', async t => {
  const { root, put } = await fixture(t);
  const a = await buildIndex(root), b = await buildIndex(root);
  assert.deepEqual(a,b);
  await put(source.path + '/references/guide.md', 'Changed instruction\n');
  const c = await buildIndex(root);
  assert.notEqual(c.index.content_sha256,a.index.content_sha256);
  assert.notEqual(c.resources.skills[0].package_sha256,a.resources.skills[0].package_sha256);
  await put('sources.json', JSON.stringify([{ ...source, adaptations: ['preserve approved customization'] }]));
  const d = await buildIndex(root);
  assert.notEqual(d.index.content_sha256,c.index.content_sha256);
  assert.equal(d.resources.skills[0].package_sha256,c.resources.skills[0].package_sha256);
  const entrypoint = await readFile(path.join(root,source.path,'SKILL.md'),'utf8');
  await put(source.path + '/SKILL.md', entrypoint.replace('Design an example.', 'Design a changed example.'));
  const e = await buildIndex(root);
  assert.notEqual(e.index.content_sha256,d.index.content_sha256);
  assert.match(e.index.skills[0].description,/changed example/);
});

test('Windows text checkout normalization matches LF while explicit binary snapshots retain bytes', () => {
  assert.deepEqual(cleanContent(Buffer.from('a\r\nb\r\n'), 'auto'), Buffer.from('a\nb\n'));
  assert.deepEqual(cleanContent(Buffer.from('a\r\n'), 'unset'), Buffer.from('a\r\n'));
  const binary = Buffer.from([0,13,10,255]);
  assert.deepEqual(cleanContent(binary,'auto'),binary);
});

test('malformed YAML and duplicate keys fail instead of silently inventing activation metadata', () => {
  assert.throws(() => parseSkill('---\nname: sample\ndescription: [broken\n---\n'), /flow sequence/i);
  assert.throws(() => parseSkill('---\nname: sample\nname: second\ndescription: Example\n---\n'), /unique/);
  assert.throws(() => parseSkill('---\nname: sample\ndescription: null\n---\n'), /description must be/);
});

test('reference audit separates retrieval links from URLs, anchors, and fenced demonstrations', () => {
  const refs = markdownReferences('[A](references/a.md#section)\n[A][guide]\n[guide]: references/guide.md\n[Web](https://example.com)\n[Same](#anchor)\n```md\n[Example](missing.md)\n```\n');
  assert.deepEqual(refs.map(r => r.target), ['references/a.md#section','references/guide.md']);
});

test('checked-in generated inventory covers each canonical source exactly once and preserves key specialized workflows', async () => {
  const sources = JSON.parse(await readFile(path.join(repo,'sources.json'),'utf8'));
  const index = JSON.parse(await readFile(path.join(repo,'skill-index.json'),'utf8'));
  const resources = JSON.parse(await readFile(path.join(repo,'skill-resources.json'),'utf8'));
  assert.equal(index.count,sources.length);
  assert.equal(new Set(index.skills.map(s => s.path)).size,sources.length);
  assert.deepEqual(index.skills.map(s => s.path).sort(),sources.map(s => `${s.path}/SKILL.md`).sort());
  for (const name of ['using-agent-skills','arcads-media-router','reverse-skill-router','blender','uefn-toolbelt']) {
    const matches = index.skills.filter(s => s.name === name);
    assert.equal(matches.length,1,`${name} must be registered once`);
    assert.ok(resources.skills.find(s => s.id === matches[0].id).files.some(f => f.path === matches[0].path));
  }
});
