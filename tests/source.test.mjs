import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, writeFileSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { execFileSync } from 'node:child_process';
import { begin, read, repositoryPath } from '../plugins/dsi-skill-library/skills/dsi-library-router/scripts/source.mjs';

test('real Git update preserves task revision, worktree, binary resources and explicit refresh', async t => {
  const root = mkdtempSync(join(tmpdir(), 'dsi-source-'));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  const origin = join(root, 'origin');
  const repo = join(root, 'repo');
  const lock = join(root, 'task.json');
  const git = (cwd, ...args) => execFileSync('git', ['-C', cwd, ...args], { stdio: 'pipe' }).toString().trim();
  mkdirSync(origin);
  git(origin, 'init', '-b', 'main');
  git(origin, 'config', 'user.name', 'DSI Test');
  git(origin, 'config', 'user.email', 'dsi@example.invalid');
  git(origin, 'config', 'core.autocrlf', 'false');
  writeFileSync(join(origin, 'skill-index.json'), JSON.stringify({ schema_version: 1, skills: [{ name: 'fixture' }] }));
  writeFileSync(join(origin, 'SKILL.md'), 'accepted version one');
  writeFileSync(join(origin, 'asset.bin'), Buffer.from([0, 255, 13, 10]));
  git(origin, 'add', '.');
  git(origin, 'commit', '-m', 'first accepted fixture');
  execFileSync('git', ['clone', origin, repo], { stdio: 'pipe' });
  writeFileSync(join(repo, 'SKILL.md'), 'unrelated uncommitted edit');
  const first = await begin({ repo, lock });
  assert.equal((await read({ lock, path: 'SKILL.md' })).content, 'accepted version one');
  writeFileSync(join(origin, 'SKILL.md'), 'accepted version two');
  git(origin, 'add', '.');
  git(origin, 'commit', '-m', 'controlled accepted update');
  assert.equal((await read({ lock, path: 'SKILL.md' })).content, 'accepted version one');
  await assert.rejects(begin({ repo, lock }), /lock exists/);
  const second = await begin({ repo, lock, refresh: true });
  assert.notEqual(first.source.revision, second.source.revision);
  assert.equal((await read({ lock, path: 'SKILL.md' })).content, 'accepted version two');
  assert.equal(readFileSync(join(repo, 'SKILL.md'), 'utf8'), 'unrelated uncommitted edit');
  const output = join(root, 'asset.bin');
  await read({ lock, path: 'asset.bin', out: output });
  assert.deepEqual(readFileSync(output), Buffer.from([0, 255, 13, 10]));
  await assert.rejects(read({ lock, path: 'asset.bin', out: output }), /EEXIST/);
  await assert.rejects(read({ lock, path: 'missing.md' }));
  const lockedBeforeFailure = readFileSync(lock, 'utf8');
  await assert.rejects(begin({ repo, lock, branch: 'nonexistent', refresh: true }));
  assert.equal(readFileSync(lock, 'utf8'), lockedBeforeFailure);
});

test('unsafe resource paths and invalid source locks fail closed', async t => {
  for (const value of ['../secret', '/absolute', 'a/../b', 'C:/x', 'a\\b', 'a?x', 'a//b']) {
    assert.throws(() => repositoryPath(value));
  }
  assert.equal(repositoryPath('skills/category/name/SKILL.md'), 'skills/category/name/SKILL.md');
  await assert.rejects(begin({ repo: '.', github: 'a/b', lock: 'unused' }), /exactly one/);
  await assert.rejects(begin({ github: 'a/b', branch: '--help', lock: 'unused' }), /Invalid branch/);
});
