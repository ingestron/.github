"""Check the static public profile without third-party dependencies."""
import hashlib
import json
import re
import struct
import xml.etree.ElementTree as ET
from pathlib import Path

root = Path(__file__).resolve().parents[1]
assets = root / 'profile/assets'
base = 'https://raw.githubusercontent.com/ingestron/.github/main/profile/assets/'


def png_size(path):
    data = path.read_bytes()
    assert data[:8] == b'\x89PNG\r\n\x1a\n', path
    return struct.unpack('>II', data[16:24])


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


# Every image is rendered at device scale 2, so 1600 pixels wide.
for name in ['hero-light.png', 'hero-dark.png']:
    assert png_size(assets / name)[0] == 1600, name
assert png_size(assets / 'avatar.png') == (512, 512)
ET.parse(assets / 'avatar.svg')

provenance = json.loads((assets / 'provenance.json').read_text())
assert provenance['brand'] == 'Ingestron brand (Air + Close-knit)'
for entry in provenance['assets']:
    assert sha256(assets / entry['path']) == entry['sha256'], entry['path']
recorded = {entry['path'] for entry in provenance['assets']}
present = {path.name for path in assets.iterdir() if path.name != 'provenance.json'}
assert recorded == present, sorted(recorded ^ present)

readme = (root / 'profile/README.md').read_text()
assert 'security@ingestron.io' in readme
used = set(re.findall(re.escape(base) + r'([\w.-]+)', readme))
assert {'hero-light.png', 'hero-dark.png'} <= used, used
for name in used:
    assert (assets / name).exists(), name
    assert name in recorded, name
for name in present - used - {'avatar.png', 'avatar.svg'}:
    raise AssertionError(f'{name} is not used by the README')

text = readme.lower()
for prohibited in ['customer data is', 'guaranteed savings',
                   'new zealand', 'auckland', 'otrera', 'pacific/']:
    assert prohibited not in text, prohibited
# Versions belong in the documentation, not the profile.
assert not re.search(r'\b\d+\.\d+\.\d+\b', readme), 'version number in README'
print('Profile assets, provenance and wording checked.')
