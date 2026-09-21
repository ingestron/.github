"""Check the static public profile without third-party dependencies."""
import json
from pathlib import Path
import struct
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
for name, size in [('hero', (1600, 650)), ('avatar', (512, 512))]:
    path = root / 'profile/assets' / name
    ET.parse(path.with_suffix('.svg'))
    data = path.with_suffix('.png').read_bytes()
    assert data[:8] == b'\x89PNG\r\n\x1a\n'
    assert struct.unpack('>II', data[16:24]) == size
assert json.loads((root / 'profile/assets/provenance.json').read_text())['version'] == '1.1.0'
readme = (root / 'profile/README.md').read_text()
assert 'development preview' in readme.lower()
assert 'https://raw.githubusercontent.com/ingestron/.github/main/profile/assets/hero.png' in readme
for prohibited in ['npm install -g', 'customer data', 'guaranteed savings']:
    assert prohibited not in readme.lower()
print('Profile assets, provenance and release wording checked.')
