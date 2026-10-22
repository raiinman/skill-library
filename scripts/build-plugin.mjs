#!/usr/bin/env node
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildIndex, json } from './lib/index.mjs';

const root = fileURLToPath(new URL('../', import.meta.url));
const check = process.argv.includes('--check');
if (process.argv.slice(2).some(arg => arg !== '--check')) throw new Error('Usage: node scripts/build-plugin.mjs [--check]');
const { index, resources, report, snapshot } = await buildIndex(root);
const outputs = {
  'skill-index.json': index,
  'skill-resources.json': resources,
  'resource-report.json': report,
  'plugins/dsi-skill-library/skills/dsi-library-router/references/skill-snapshot.json': snapshot,
};
for (const [file, data] of Object.entries(outputs)) {
  const target = path.join(root, file), expected = json(data);
  if (check) {
    let actual;
    try { actual = (await readFile(target, 'utf8')).replace(/\r\n/g, '\n'); } catch (error) { if (error.code !== 'ENOENT') throw error; }
    if (actual !== expected) throw new Error(`${file} is stale; run npm run build`);
  } else {
    await mkdir(path.dirname(target), { recursive: true });
    await writeFile(target, expected);
  }
}
console.log(`${check ? 'Verified' : 'Generated'} ${index.count} canonical skills across ${index.categories.length} categories; ${report.counts.active_issues} active and ${report.counts.archived_issues} archived reference issues are recorded in resource-report.json.`);
