import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync, spawnSync } from 'node:child_process';
import { mkdtempSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
const reader = join(root, 'plugins/dsi-skill-library/skills/dsi-library-router/scripts/source.mjs');

test('packaged CLI retrieves the real debugging workflow and provenance at one commit', t => {
  const temporary = mkdtempSync(join(tmpdir(), 'dsi-plugin-smoke-'));
  t.after(() => rmSync(temporary, { recursive: true, force: true }));
  const git = (...args) => execFileSync('git', ['-C', root, ...args], { encoding: 'utf8' }).trim();
  const revision = git('rev-parse', 'HEAD');
  const origin = join(temporary, 'origin.git');
  const checkout = join(temporary, 'checkout');
  // A local clone of the real committed library: no fabricated index or network dependency.
  // Give detached CI checkouts a named source branch without changing the user's refs.
  execFileSync('git', ['clone', '--bare', '--shared', root, origin], { stdio: 'pipe' });
  execFileSync('git', ['-C', origin, 'update-ref', 'refs/heads/dsi-smoke-source', revision], { stdio: 'pipe' });
  execFileSync('git', ['clone', '--shared', '--no-checkout', origin, checkout], { stdio: 'pipe' });
  const lock = join(temporary, 'task.json');
  const cli = (...args) => spawnSync(process.execPath, [reader, ...args], {
    encoding: 'utf8', maxBuffer: 4 * 1024 * 1024,
  });
  const started = cli('begin', '--repo', checkout, '--branch', 'dsi-smoke-source', '--lock', lock);
  assert.equal(started.status, 0, started.stderr);
  const { source, index } = JSON.parse(started.stdout);
  assert.equal(source.revision, revision);
  const selected = index.skills.find(s => s.id === 'coding-workflow/debugging-and-error-recovery');
  assert(selected, 'The debugging workflow must be discoverable');
  const contents = [];
  for (const path of [selected.path, selected.path.replace(/SKILL\.md$/, 'SOURCE.md')]) {
    const result = cli('read', '--lock', lock, '--path', path);
    assert.equal(result.status, 0, result.stderr);
    const resource = JSON.parse(result.stdout);
    assert.equal(resource.revision, revision);
    assert.equal(resource.content, execFileSync('git', ['-C', root, 'show', `${revision}:${path}`], { encoding: 'utf8' }));
    contents.push(resource.content);
  }
  assert.match(contents[0], /builds break/);
  const retained = readFileSync(lock, 'utf8');
  const missing = cli('read', '--lock', lock, '--path', 'missing-skill/SKILL.md');
  assert.notEqual(missing.status, 0);
  assert.match(missing.stderr, /DSI source error:/);
  assert.equal(readFileSync(lock, 'utf8'), retained);
  const invalid = cli('begin', '--lock', lock, '--unknown-option');
  assert.notEqual(invalid.status, 0);
  assert.match(invalid.stderr, /Unknown option/);
});

test('fresh-chat debugging fixture reproduces its intentional module failure', () => {
  const result = spawnSync(process.execPath, ['src/index.mjs'], {
    cwd: join(root, 'tests/fixtures/failing-build'), encoding: 'utf8',
  });
  assert.notEqual(result.status, 0, 'The fixture must remain broken for a fresh host trial');
  assert.match(result.stderr, /does not provide an export named 'sum'/);
});
