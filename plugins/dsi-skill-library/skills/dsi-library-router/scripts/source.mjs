#!/usr/bin/env node
// No npm dependencies: this reader also runs from an installed skill package.
import { execFileSync } from 'node:child_process';
import { createHash, randomUUID } from 'node:crypto';
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const sha256 = bytes => createHash('sha256').update(bytes).digest('hex');
const git = (repo, ...args) => execFileSync('git', ['-C', repo, ...args], {
  maxBuffer: 32 * 1024 * 1024, stdio: ['ignore', 'pipe', 'pipe'],
});

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
  if (!response.ok) throw new Error(`Source unavailable: HTTP ${response.status} (${url})`);
  return json ? response.json() : Buffer.from(await response.arrayBuffer());
}

async function pinnedBytes(lock, path) {
  repositoryPath(path);
  if (!/^[a-f0-9]{40}$/.test(lock.revision)) throw new Error('Invalid locked commit SHA');
  if (lock.adapter === 'git') return git(lock.repository, 'show', `${lock.revision}:${path}`);
  if (lock.adapter !== 'github' || !/^[\w.-]+\/[\w.-]+$/.test(lock.repository)) {
    throw new Error('Invalid source adapter or repository');
  }
  return httpsRead(`https://raw.githubusercontent.com/${lock.repository}/${lock.revision}/${path.split('/').map(encodeURIComponent).join('/')}`);
}

export async function begin({ repo, github, branch = 'main', lock: lockPath, refresh = false }) {
  if (!lockPath) throw new Error('--lock is required');
  if (Boolean(repo) === Boolean(github)) throw new Error('Choose exactly one of --repo or --github');
  if (existsSync(lockPath) && !refresh) throw new Error('Task lock exists; reuse it or explicitly --refresh');
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
  const bytes = await pinnedBytes(lock, 'skill-index.json');
  const index = JSON.parse(bytes.toString('utf8'));
  if (index.schema_version !== 1 || !Array.isArray(index.skills)) throw new Error('Unsupported skill index');
  lock.index_sha256 = sha256(bytes);
  mkdirSync(dirname(resolve(lockPath)), { recursive: true });
  writeFileSync(lockPath, JSON.stringify(lock, null, 2) + '\n', { flag: refresh ? 'w' : 'wx' });
  return { source: lock, index };
}

export async function read({ lock: lockPath, path, out }) {
  const lock = JSON.parse(readFileSync(lockPath, 'utf8'));
  const bytes = await pinnedBytes(lock, path);
  if (path === 'skill-index.json' && sha256(bytes) !== lock.index_sha256) {
    throw new Error('Locked index integrity mismatch');
  }
  if (out) {
    mkdirSync(dirname(resolve(out)), { recursive: true });
    writeFileSync(out, bytes, { flag: 'wx' });
  }
  return { revision: lock.revision, path, sha256: sha256(bytes), bytes: bytes.length,
    ...(out ? { output: resolve(out) } : { content: bytes.toString('utf8') }) };
}

function options(args) {
  const result = {};
  for (let i = 0; i < args.length; i++) {
    const key = args[i];
    if (!['--repo', '--github', '--branch', '--lock', '--path', '--out', '--refresh'].includes(key)) {
      throw new Error(`Unknown option: ${key}`);
    }
    if (key === '--refresh') result.refresh = true;
    else {
      const value = args[++i];
      if (!value || value.startsWith('--')) throw new Error(`Missing value for ${key}`);
      result[key.slice(2)] = value;
    }
  }
  return result;
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  try {
    const [command, ...args] = process.argv.slice(2);
    if (!['begin', 'read'].includes(command)) throw new Error('Usage: source.mjs begin|read --lock PATH [options]');
    const result = await (command === 'begin' ? begin : read)(options(args));
    process.stdout.write(JSON.stringify(result, null, 2) + '\n');
  } catch (error) {
    process.stderr.write(`DSI source error: ${error.message}\n`);
    process.exitCode = 1;
  }
}
