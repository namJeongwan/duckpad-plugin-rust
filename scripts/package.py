#!/usr/bin/env python3
"""Verify the signed definition and build a deterministic installable ZIP."""
from pathlib import Path
import hashlib, json, subprocess, zipfile
root = Path(__file__).resolve().parents[1]
packages = list(root.glob('*.duckpad-plugin'))
assert len(packages) == 1, 'Expected exactly one plugin package'
package = packages[0]
expected = {'plugin.json', 'SHA256SUMS', 'SIGNATURE.ed25519'}
assert {p.name for p in package.iterdir()} == expected
assert all(p.is_file() and not p.is_symlink() for p in package.iterdir())
manifest = (package / 'plugin.json').read_bytes()
metadata = json.loads(manifest)
assert package.name == metadata['id'] + '.duckpad-plugin'
inventory = (hashlib.sha256(manifest).hexdigest() + '  plugin.json\n').encode()
assert (package / 'SHA256SUMS').read_bytes() == inventory
public = (root / 'publisher.public').read_text().strip()
subprocess.run(['swift', str(root / 'scripts/verify.swift'), str(package / 'SHA256SUMS'),
                str(package / 'SIGNATURE.ed25519'), public], check=True)
version = '.'.join(str(metadata['version'][key]) for key in ['major', 'minor', 'patch'])
name = metadata['id'].rsplit('.', 1)[1].capitalize()
out = root / 'dist' / ('Duckpad-' + name + '-' + version + '.zip')
out.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
    for filename in sorted(expected):
        info = zipfile.ZipInfo(package.name + '/' + filename, (2026, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, (package / filename).read_bytes())
with zipfile.ZipFile(out) as archive:
    assert archive.testzip() is None
print(hashlib.sha256(out.read_bytes()).hexdigest(), out.name)
