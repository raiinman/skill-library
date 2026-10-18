"""Run pinned upstream recipes in a fresh Blender process, with Windows path-safe substitutions."""
import argparse
import json
from pathlib import Path
import sys
import types
import bpy

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source',type=Path,required=True)
parser.add_argument('--out',type=Path,required=True)
args=parser.parse_args(sys.argv[sys.argv.index('--')+1:])
if bpy.data.filepath:
    raise ValueError('Run only with factory startup, without loading a user blend')
if args.out.exists():
    raise FileExistsError(args.out)
source=args.source.resolve()/'tests/core_recipe_regressions.py'
text=source.read_text(encoding='utf-8')
# The upstream test inserts filesystem paths into quoted Python code strings.
text=text.replace('str(path)','path.as_posix()').replace("str(out/'fixture.hdr')","(out/'fixture.hdr').as_posix()")
module=types.ModuleType('pinned_blender_core_tests')
module.__file__=str(source)
exec(compile(text,str(source),'exec'),module.__dict__)
report=module.run_suite(args.source.resolve(),args.out.resolve())
failed=[row for row in report['tests'] if row['status']!='PASS']
print('BLENDER_RECIPE_RESULTS',len(report['tests']),json.dumps(failed))
if failed:
    raise RuntimeError('Recipe regression failures, see core-tests.json')
