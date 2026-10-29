#!/usr/bin/env node
// No runtime npm install: the pinned YAML parser is bundled with this package.
import { execFileSync } from 'node:child_process';
import { createHash, randomUUID } from 'node:crypto';
import { isUtf8 } from 'node:buffer';
import { readFileSync, writeFileSync, mkdirSync, existsSync, lstatSync, realpathSync } from 'node:fs';
import { dirname, resolve, relative, isAbsolute } from 'node:path';
import { pathToFileURL, fileURLToPath } from 'node:url';
import { parseDocument } from './vendor/yaml/dist/index.js';

const sha256 = bytes => createHash('sha256').update(bytes).digest('hex');
const defaultOverlayRoot = fileURLToPath(new URL('../resources/maintenance-overlay/', import.meta.url));
const overlayRepository = 'raiinman/skill-library';

export function loadMaintenanceOverlay(root = defaultOverlayRoot) {
  if (!existsSync(resolve(root, 'manifest.json'))) return null;
  const cache = { base: realpathSync(root), stats: new Map() };
  const bytes = snapshotFile(root, 'manifest.json', cache), manifest = JSON.parse(bytes.toString('utf8'));
  if (manifest.schema_version !== 1 || typeof manifest.id !== 'string' || !/^[a-zA-Z0-9._-]+$/.test(manifest.id) ||
      manifest.repository !== overlayRepository || !/^[a-f0-9]{40}$/.test(manifest.base_revision) ||
      !/^[\w.-]+\/[\w.-]+$/.test(manifest.upstream?.repository) || !/^[a-f0-9]{40}$/.test(manifest.upstream?.revision) ||
      !manifest.files || typeof manifest.files !== 'object' || Array.isArray(manifest.files)) throw new Error('Invalid maintenance overlay manifest');
  const resources = new Set();
  for (const [path, entry] of Object.entries(manifest.files)) {
    repositoryPath(path);
    if (!entry || !/^[a-f0-9]{64}$/.test(entry.base_sha256) || !/^[a-f0-9]{64}$/.test(entry.sha256) ||
        !Number.isSafeInteger(entry.bytes) || entry.bytes < 0 ||
        (entry.base_git_blob !== undefined && !/^[a-f0-9]{40}$/.test(entry.base_git_blob))) throw new Error('Invalid maintenance overlay entry');
    repositoryPath(entry.resource_path);
    if (resources.has(entry.resource_path.toLowerCase())) throw new Error('Duplicate maintenance overlay storage path');
    resources.add(entry.resource_path.toLowerCase());
    const replacement = snapshotFile(root, entry.resource_path, cache);
    if (replacement.length !== entry.bytes || sha256(replacement) !== entry.sha256) throw new Error(`Maintenance overlay integrity mismatch: ${path}`);
  }
  return { root, manifest, descriptor: { id: manifest.id, repository: manifest.repository,
    base_revision: manifest.base_revision, manifest_sha256: sha256(bytes) } };
}

function overlaySourceEligible(lock) {
  if (lock.adapter === 'github') return lock.repository?.toLowerCase() === overlayRepository;
  if (lock.adapter === 'git') return /^(?:https:\/\/github\.com\/|git@github\.com:|ssh:\/\/git@github\.com\/)raiinman\/skill-library(?:\.git)?\/?$/i.test(lock.origin ?? '') &&
    git(lock.repository, 'remote', 'get-url', 'origin').toString().trim() === lock.origin;
  return false;
}

function lockedOverlay(lock, overlayRoot) {
  if (!lock.maintenance_overlay) return null;
  if (lock.adapter !== 'snapshot' && !overlaySourceEligible(lock)) throw new Error('Maintenance overlay cannot target this repository');
  const overlay = loadMaintenanceOverlay(overlayRoot);
  if (!overlay || Object.keys(overlay.descriptor).some(key => overlay.descriptor[key] !== lock.maintenance_overlay[key])) throw new Error('Locked maintenance overlay identity or manifest mismatch');
  return overlay;
}

function maintenanceResult(overlay, path, bytes) {
  const files = overlay?.manifest.files;
  const entry = files && Object.hasOwn(files, path) ? files[path] : undefined;
  const actual = sha256(bytes);
  if (!entry) return { bytes, source_sha256: actual, match: 'unlisted' };
  if (actual === entry.sha256) return { bytes, source_sha256: actual, match: 'effective' };
  if (actual !== entry.base_sha256) throw new Error(`Maintenance overlay conflict at ${path}: pinned source matches neither base nor effective hash`);
  const effective = snapshotFile(overlay.root, entry.resource_path);
  if (effective.length !== entry.bytes || sha256(effective) !== entry.sha256) throw new Error(`Maintenance overlay integrity mismatch: ${path}`);
  return { bytes: effective, source_sha256: actual, match: 'base' };
}

function applyMaintenanceOverlay(lock, path, bytes, overlayRoot) {
  return maintenanceResult(lockedOverlay(lock, overlayRoot), path, bytes).bytes;
}

export function verifySource({ repository, revision, path, sourceBase64, overlayRoot } = {}) {
  if (repository !== overlayRepository) throw new Error('Expected repository raiinman/skill-library');
  if (typeof revision !== 'string' || revision.length !== 40 || !/^[a-f0-9]{40}$/.test(revision)) throw new Error('Expected a full lowercase commit SHA revision');
  repositoryPath(path);
  if (typeof sourceBase64 !== 'string') throw new Error('Expected canonical base64 source bytes');
  // GitHub may wrap base64 and shell pipelines may append LF or CRLF.
  const encoded = sourceBase64.replace(/\r?\n/g, '');
  if (!/^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$/.test(encoded)) throw new Error('Expected canonical base64 source bytes');
  const source = Buffer.from(encoded, 'base64');
  if (source.toString('base64') !== encoded) throw new Error('Expected canonical base64 source bytes');
  const overlay = loadMaintenanceOverlay(overlayRoot);
  if (!overlay) throw new Error('Maintenance overlay unavailable');
  const result = maintenanceResult(overlay, path, source);
  return { repository, revision, path, source_sha256: result.source_sha256, match: result.match,
    maintenance_overlay: overlay.descriptor, effective_sha256: sha256(result.bytes), bytes: result.bytes.length,
    ...(isUtf8(result.bytes) ? { content: result.bytes.toString('utf8') } : {}),
    content_base64: result.bytes.toString('base64') };
}
const git = (repo, ...args) => execFileSync('git', ['-C', repo, ...args], {
  maxBuffer: 32 * 1024 * 1024, stdio: ['ignore', 'pipe', 'pipe'],
});

function snapshotFile(root, path, cache = { base: realpathSync(root), stats: new Map() }) {
  repositoryPath(path);
  const base = cache.base, target = resolve(base, path);
  const contained = relative(base, target);
  if (contained.startsWith('..') || isAbsolute(contained)) throw new Error('Snapshot path escapes bundle');
  let current = base;
  for (const part of path.split('/')) {
    current = resolve(current, part);
    if (!cache.stats.has(current)) cache.stats.set(current, lstatSync(current));
    if (cache.stats.get(current).isSymbolicLink()) throw new Error('Snapshot symlinks are not allowed');
  }
  if (!cache.stats.get(target).isFile()) throw new Error('Snapshot resource is not a file');
  return readFileSync(target);
}

function snapshotResource(root, manifest, path, cache) {
  repositoryPath(path);
  const entry = manifest.files[path];
  if (!entry) throw new Error(`Resource absent from bundled snapshot: ${path}`);
  const bytes = snapshotFile(root, entry.stored_path, cache);
  if (bytes.length !== entry.bytes || sha256(bytes) !== entry.sha256) throw new Error(`Snapshot resource integrity mismatch: ${path}`);
  return bytes;
}

export function verifySnapshot(snapshot, { all = true, overlayRoot } = {}) {
  const cache = { base: realpathSync(snapshot), stats: new Map() };
  const bytes = snapshotFile(snapshot, 'snapshot-manifest.json', cache);
  const manifest = JSON.parse(bytes.toString('utf8'));
  if (manifest.schema_version !== 1 || !/^[\w.-]+\/[\w.-]+$/.test(manifest.repository) ||
      !/^[a-f0-9]{40}$/.test(manifest.revision) || typeof manifest.branch !== 'string' ||
      !manifest.files || typeof manifest.files !== 'object' || Array.isArray(manifest.files) ||
      manifest.index_path !== 'skill-index.json') throw new Error('Invalid snapshot manifest');
  const stored = new Set();
  for (const [path, entry] of Object.entries(manifest.files)) {
    repositoryPath(path);
    if (!entry || typeof entry !== 'object' || !/^[a-f0-9]{64}$/.test(entry.sha256) ||
        !Number.isSafeInteger(entry.bytes) || entry.bytes < 0) throw new Error('Invalid snapshot resource record');
    repositoryPath(entry.stored_path);
    if (stored.has(entry.stored_path)) throw new Error('Duplicate snapshot storage path');
    stored.add(entry.stored_path);
    if (all) snapshotResource(snapshot, manifest, path, cache);
  }
  const indexBytes = snapshotResource(snapshot, manifest, manifest.index_path, cache);
  const index = JSON.parse(indexBytes.toString('utf8'));
  if (index.schema_version !== 1 || index.revision !== manifest.revision || !Array.isArray(index.skills) ||
      !index.skills.length || index.count !== index.skills.length) throw new Error('Invalid bundled index or revision');
  const ids = new Set(), names = new Set();
  for (const skill of index.skills) {
    repositoryPath(skill.path);
    if (!/^skills\/[a-z0-9-]+\/[a-z0-9-]+\/SKILL\.md$/.test(skill.path) ||
        skill.id !== skill.path.split('/').slice(1, 3).join('/') ||
        skill.name !== skill.path.split('/')[2] || typeof skill.description !== 'string' || !skill.description.trim() ||
        ids.has(skill.id) || names.has(skill.name) || !manifest.files[skill.path] ||
        !manifest.files[skill.path.replace(/SKILL\.md$/, 'SOURCE.md')]) throw new Error('Invalid bundled primary or provenance');
    ids.add(skill.id); names.add(skill.name);
  }
  if (manifest.maintenance_overlay) {
    if (manifest.repository !== overlayRepository) throw new Error('Snapshot maintenance overlay repository mismatch');
    const overlay = lockedOverlay({ adapter: 'snapshot', maintenance_overlay: manifest.maintenance_overlay }, overlayRoot);
    if (manifest.revision !== overlay.manifest.base_revision) throw new Error('Snapshot maintenance overlay base revision mismatch');
    for (const [path, entry] of Object.entries(overlay.manifest.files)) {
      if (manifest.files[path]?.sha256 !== entry.sha256 || manifest.files[path]?.bytes !== entry.bytes) throw new Error(`Snapshot maintenance overlay not materialized: ${path}`);
    }
  }
  return { manifest, index, manifest_sha256: sha256(bytes) };
}

export function repositoryPath(value) {
  if (typeof value !== 'string' || !value || value.startsWith('/') ||
      value.includes('\\') || /[\x00-\x1f:#?]/.test(value) ||
      value.split('/').some(part => !part || part === '..' || part === '.')) {
    throw new Error('Expected a contained repository-relative path');
  }
  return value;
}

async function httpsRead(url, json = false) {
  const response = await fetch(url, {
    headers: { Accept: json ? 'application/vnd.github+json' : 'application/octet-stream' },
    signal: AbortSignal.timeout(30000), redirect: 'error',
  });
  if (!response.ok) {
    const error = new Error(`Source unavailable: HTTP ${response.status} (${url})`);
    error.status = response.status;
    throw error;
  }
  return json ? response.json() : Buffer.from(await response.arrayBuffer());
}

async function optionalIndex(lock, overlayRoot) {
  try { return await pinnedBytes(lock, 'skill-index.json', overlayRoot); }
  catch (error) {
    // Only an absent path permits compatibility discovery. Authentication, transport,
    // invalid revisions and malformed JSON must never silently switch discovery modes.
    if (lock.adapter === 'github' && error.status === 404) return null;
    if (lock.adapter === 'git' && /fatal: path 'skill-index\.json' (?:does not exist in|exists on disk, but not in)/.test(error.stderr?.toString() ?? '')) return null;
    throw error;
  }
}

function nativeSkill(path, bytes) {
  const frontmatter = bytes.toString('utf8').replace(/^\uFEFF/, '').match(/^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/);
  if (!frontmatter) throw new Error(`${path}: missing native YAML frontmatter`);
  const document = parseDocument(frontmatter[1], { uniqueKeys: true });
  if (document.errors.length) throw new Error(`${path}: invalid native YAML: ${document.errors.map(e => e.message).join('; ')}`);
  const native = document.toJS({ maxAliasCount: 100 }), [, category, name] = path.split('/');
  if (!native || native.name !== name || typeof native.description !== 'string' || !native.description.trim()) throw new Error(`${path}: invalid native name or description`);
  return { id: `${category}/${name}`, name, category, path, description: native.description, routing_metadata: native.metadata?.dsi ?? {} };
}

export async function discoverIndex(lock, { overlayRoot } = {}) {
  const published = await optionalIndex(lock, overlayRoot);
  if (published) {
    const index = JSON.parse(published.toString('utf8'));
    if (index.schema_version !== 1 || !Array.isArray(index.skills)) throw new Error('Unsupported skill index');
    const overlay = lockedOverlay(lock, overlayRoot), inputs = { 'skill-index.json': sha256(published) };
    if (!overlay) return { index, bytes: published, mode: 'published-index', inputs };
    for (let i = 0; i < index.skills.length; i++) {
      const skill = index.skills[i];
      if (!overlay.manifest.files[skill.path] || !skill.path?.endsWith('/SKILL.md')) continue;
      const body = await pinnedBytes(lock, skill.path, overlayRoot);
      index.skills[i] = { ...skill, ...nativeSkill(skill.path, body) }; inputs[skill.path] = sha256(body);
    }
    return { index, bytes: Buffer.from(JSON.stringify(index, null, 2) + '\n'), mode: 'maintenance-overlay-index', inputs };
  }
  const catalog = await pinnedBytes(lock, 'CATALOG.md', overlayRoot);
  const paths = [...catalog.toString('utf8').matchAll(/\]\((skills\/[a-z0-9-]+\/[a-z0-9-]+\/SKILL\.md)\)/g)].map(match => match[1]);
  if (!paths.length || new Set(paths).size !== paths.length) throw new Error('Catalog has no canonical skills or contains duplicates');
  const inputs = { 'CATALOG.md': sha256(catalog) }, skills = [], names = new Set();
  // Bounded parallel reads keep the full live catalog practical on HTTPS hosts.
  for (let offset = 0; offset < paths.length; offset += 12) {
    const batch = await Promise.all(paths.slice(offset, offset + 12).map(async path => {
      const bytes = await pinnedBytes(lock, path, overlayRoot);
      return { hash: sha256(bytes), skill: nativeSkill(path, bytes) };
    }));
    for (let i = 0; i < batch.length; i++) {
      const { skill, hash } = batch[i];
      if (names.has(skill.name)) throw new Error(`Ambiguous duplicate native name: ${skill.name}`);
      names.add(skill.name);
      inputs[paths[offset + i]] = hash;
      skills.push(skill);
    }
  }
  const index = { schema_version: 1, discovery: 'derived-from-pinned-catalog', revision: lock.revision,
    count: skills.length, categories: [...new Set(skills.map(s => s.category))].sort(), skills };
  return { index, bytes: Buffer.from(JSON.stringify(index, null, 2) + '\n'), mode: 'derived-from-pinned-catalog', inputs };
}

async function pinnedBytes(lock, path, overlayRoot) {
  repositoryPath(path);
  if (!/^[a-f0-9]{40}$/.test(lock.revision)) throw new Error('Invalid locked commit SHA');
  if (lock.adapter === 'snapshot') {
    const verified = verifySnapshot(lock.snapshot_root, { all: false, overlayRoot });
    if (verified.manifest_sha256 !== lock.snapshot_manifest_sha256 ||
        verified.manifest.revision !== lock.revision || verified.manifest.repository !== lock.repository ||
        verified.manifest.branch !== lock.branch) throw new Error('Locked snapshot identity or manifest mismatch');
    lockedOverlay(lock, overlayRoot);
    return snapshotResource(lock.snapshot_root, verified.manifest, path);
  }
  if (lock.adapter === 'git') return applyMaintenanceOverlay(lock, path, git(lock.repository, 'show', `${lock.revision}:${path}`), overlayRoot);
  if (lock.adapter !== 'github' || !/^[\w.-]+\/[\w.-]+$/.test(lock.repository)) {
    throw new Error('Invalid source adapter or repository');
  }
  return applyMaintenanceOverlay(lock, path, await httpsRead(`https://raw.githubusercontent.com/${lock.repository}/${lock.revision}/${path.split('/').map(encodeURIComponent).join('/')}`), overlayRoot);
}

export async function begin({ repo, github, snapshot, branch = 'main', lock: lockPath, refresh = false, overlayRoot }) {
  if (!lockPath) throw new Error('--lock is required');
  if ([repo, github, snapshot].filter(Boolean).length !== 1) throw new Error('Choose exactly one of --repo, --github or --snapshot');
  if (existsSync(lockPath) && !refresh) throw new Error('Task lock exists; reuse it or explicitly --refresh');
  if (snapshot) {
    const verified = verifySnapshot(snapshot, { overlayRoot });
    const manifest = verified.manifest;
    const source = { schema_version: 1, adapter: 'snapshot', source_kind: 'bundled-snapshot',
      repository: manifest.repository, branch: manifest.branch, revision: manifest.revision,
      freshness: 'immutable packaged revision; not a live branch check', snapshot_root: resolve(snapshot),
      snapshot_manifest_sha256: verified.manifest_sha256, discovery_mode: 'bundled-snapshot',
      index_sha256: manifest.files[manifest.index_path].sha256,
      ...(manifest.maintenance_overlay ? { maintenance_overlay: manifest.maintenance_overlay } : {}) };
    lockedOverlay(source, overlayRoot);
    mkdirSync(dirname(resolve(lockPath)), { recursive: true });
    writeFileSync(lockPath, JSON.stringify(source, null, 2) + '\n', { flag: refresh ? 'w' : 'wx' });
    return { source, index: verified.index };
  }
  if (!branch || branch.startsWith('-') || /[\x00-\x20~^:?*\[\\]/.test(branch) || branch.includes('..')) {
    throw new Error('Invalid branch');
  }
  const lock = { schema_version: 1, adapter: repo ? 'git' : 'github',
    repository: repo ? resolve(repo) : github, branch };
  if (repo) {
    git(lock.repository, 'check-ref-format', `refs/heads/${branch}`);
    lock.origin = git(lock.repository, 'remote', 'get-url', 'origin').toString().trim();
    // A unique temporary ref avoids FETCH_HEAD races between concurrent tasks.
    const taskRef = `refs/dsi-tasks/${randomUUID()}`;
    try {
      git(lock.repository, 'fetch', '--no-tags', '--no-write-fetch-head', 'origin', `refs/heads/${branch}:${taskRef}`);
      lock.revision = git(lock.repository, 'rev-parse', '--verify', `${taskRef}^{commit}`).toString().trim();
    } finally {
      git(lock.repository, 'update-ref', '-d', taskRef);
    }
  } else {
    if (!/^[\w.-]+\/[\w.-]+$/.test(github)) throw new Error('Expected owner/repository');
    const commit = await httpsRead(`https://api.github.com/repos/${github}/commits/${encodeURIComponent(branch)}`, true);
    lock.revision = commit.sha;
  }
  let discovered;
  try {
    if (overlaySourceEligible(lock)) {
      const overlay = loadMaintenanceOverlay(overlayRoot);
      if (overlay) lock.maintenance_overlay = overlay.descriptor;
    }
    discovered = await discoverIndex(lock, { overlayRoot });
  } catch (error) {
    // Discovery may fail after branch resolution. Expose that pin for connector
    // recovery without writing a lock that would imply successful discovery.
    error.source = { adapter: lock.adapter, repository: lock.repository,
      branch: lock.branch, revision: lock.revision };
    throw error;
  }
  const { index, bytes, mode, inputs } = discovered;
  lock.discovery_mode = mode;
  lock.discovery_inputs = inputs;
  if (mode === 'derived-from-pinned-catalog' || mode === 'maintenance-overlay-index') lock.derived_index = index;
  lock.index_sha256 = sha256(bytes);
  mkdirSync(dirname(resolve(lockPath)), { recursive: true });
  writeFileSync(lockPath, JSON.stringify(lock, null, 2) + '\n', { flag: refresh ? 'w' : 'wx' });
  const { derived_index, ...source } = lock;
  return { source, index };
}

export async function read({ lock: lockPath, snapshot, path, out, overlayRoot }) {
  if (Boolean(lockPath) === Boolean(snapshot)) throw new Error('Choose exactly one of --lock or --snapshot');
  let lock;
  if (snapshot) {
    const verified = verifySnapshot(snapshot, { overlayRoot });
    lock = { adapter: 'snapshot', snapshot_root: resolve(snapshot), repository: verified.manifest.repository,
      branch: verified.manifest.branch, revision: verified.manifest.revision,
      snapshot_manifest_sha256: verified.manifest_sha256, discovery_mode: 'bundled-snapshot',
      index_sha256: verified.manifest.files[verified.manifest.index_path].sha256,
      ...(verified.manifest.maintenance_overlay ? { maintenance_overlay: verified.manifest.maintenance_overlay } : {}) };
  } else lock = JSON.parse(readFileSync(lockPath, 'utf8'));
  repositoryPath(path);
  if (!/^[a-f0-9]{40}$/.test(lock.revision)) throw new Error('Invalid locked commit SHA');
  lockedOverlay(lock, overlayRoot);
  const virtual = path === 'skill-index.json' && ['derived-from-pinned-catalog', 'maintenance-overlay-index'].includes(lock.discovery_mode);
  const bytes = virtual
    ? Buffer.from(JSON.stringify(lock.derived_index, null, 2) + '\n') : await pinnedBytes(lock, path, overlayRoot);
  if (path === 'skill-index.json' && sha256(bytes) !== lock.index_sha256) {
    throw new Error('Locked index integrity mismatch');
  }
  if (!virtual && lock.discovery_inputs?.[path] && sha256(bytes) !== lock.discovery_inputs[path]) throw new Error('Locked discovery resource integrity mismatch');
  if (out) {
    mkdirSync(dirname(resolve(out)), { recursive: true });
    writeFileSync(out, bytes, { flag: 'wx' });
  }
  return { revision: lock.revision, path, sha256: sha256(bytes), bytes: bytes.length,
    ...(lock.maintenance_overlay ? { maintenance_overlay: lock.maintenance_overlay,
      effective_source: 'pinned-source-plus-maintenance-overlay' } : {}),
    ...(lock.adapter === 'snapshot' ? { source_kind: 'bundled-snapshot', freshness: 'immutable packaged revision; not a live branch check' } : {}),
    ...(virtual ? { virtual: true, discovery_mode: lock.discovery_mode } : {}),
    ...(out ? { output: resolve(out) } : { content: bytes.toString('utf8') }) };
}

function options(args, strict = false) {
  const result = {};
  for (let i = 0; i < args.length; i++) {
    const key = args[i];
    if (!['--repo', '--github', '--snapshot', '--branch', '--lock', '--path', '--out', '--refresh', '--repository', '--revision', '--source-base64'].includes(key)) {
      throw new Error(`Unknown option: ${key}`);
    }
    if (key === '--refresh') result.refresh = true;
    else {
      const value = args[++i];
      if (!value || value.startsWith('--')) throw new Error(`Missing value for ${key}`);
      const name = key === '--source-base64' ? 'sourceBase64' : key.slice(2);
      if (strict && Object.hasOwn(result, name)) throw new Error(`Duplicate option: ${key}`);
      result[name] = value;
    }
  }
  return result;
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  try {
    const [command, ...args] = process.argv.slice(2);
    if (!['begin', 'read', 'verify', 'verify-source'].includes(command)) throw new Error('Usage: source.mjs begin|read|verify|verify-source [options]');
    const parsed = options(args, command === 'verify-source');
    let result;
    if (command === 'verify-source') {
      if (Object.keys(parsed).some(key => !['repository', 'revision', 'path', 'sourceBase64'].includes(key))) throw new Error('verify-source accepts only --repository, --revision, --path and --source-base64');
      if (parsed.sourceBase64 === '-') parsed.sourceBase64 = readFileSync(0, 'utf8');
      result = verifySource(parsed);
    } else if (command === 'verify') {
      if (!parsed.snapshot || Object.keys(parsed).some(k => k !== 'snapshot')) throw new Error('verify requires only --snapshot PATH');
      const verified = verifySnapshot(parsed.snapshot);
      result = { source_kind: 'bundled-snapshot', repository: verified.manifest.repository,
        revision: verified.manifest.revision, manifest_sha256: verified.manifest_sha256,
        ...(verified.manifest.maintenance_overlay ? { maintenance_overlay: verified.manifest.maintenance_overlay } : {}),
        files: Object.keys(verified.manifest.files).length, skills: verified.index.count,
        freshness: 'immutable packaged revision; not a live branch check' };
    } else result = await (command === 'begin' ? begin : read)(parsed);
    process.stdout.write(JSON.stringify(result, null, 2) + '\n');
  } catch (error) {
    process.stderr.write(`DSI source error: ${error.message}\n`);
    if (error.source) process.stderr.write(JSON.stringify({ type: 'dsi-source-error',
      message: error.message, source: error.source }) + '\n');
    process.exitCode = 1;
  }
}
