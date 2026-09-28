"""Check the static public profile without third-party dependencies."""
import json
import re
from pathlib import Path
import struct
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
assets = root / 'profile/assets'


def png_size(path):
    data = path.read_bytes()
    assert data[:8] == b'\x89PNG\r\n\x1a\n', path
    return struct.unpack('>II', data[16:24])


assert png_size(assets / 'hero-light.png') == (1600, 640)
assert png_size(assets / 'hero-dark.png') == (1600, 640)
assert png_size(assets / 'avatar.png') == (512, 512)
assert png_size(assets / 'how-it-works.png')[0] >= 1600
ET.parse(assets / 'avatar.svg')
assert json.loads((assets / 'provenance.json').read_text())['version'] == '2.0.0'

readme = (root / 'profile/README.md').read_text()
assert 'development preview' in readme.lower()
base = 'https://raw.githubusercontent.com/ingestron/.github/main/profile/assets/'
for name in ['hero-light.png', 'hero-dark.png', 'how-it-works.png']:
    assert base + name in readme, name
for prohibited in ['npm install -g ', 'customer data is', 'guaranteed savings']:
    assert prohibited not in readme.lower(), prohibited
# Versions belong in the documentation, not the profile.
assert not re.search(r'\b\d+\.\d+\.\d+\b', readme), 'version number in README'
print('Profile assets, provenance and wording checked.')
