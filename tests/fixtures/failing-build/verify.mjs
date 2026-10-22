import { spawnSync } from 'node:child_process';
import assert from 'node:assert/strict';

const result = spawnSync(process.execPath, ['src/index.mjs'], { encoding: 'utf8' });
assert.equal(result.status, 0, result.stderr);
assert.equal(result.stdout.trim(), 'total=42');
console.log('PASS: application builds and produces the expected total');
