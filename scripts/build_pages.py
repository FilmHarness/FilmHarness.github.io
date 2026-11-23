"""Build the lightweight public site; retain the self-contained source in main."""
from pathlib import Path
import hashlib
import json
import shutil
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '_site'
MEDIA = 'https://media.githubusercontent.com/media/FilmHarness/FilmHarness.github.io/main/'


def build():
    OUT.mkdir(exist_ok=True)
    shutil.copytree(ROOT / 'assets', OUT / 'assets', dirs_exist_ok=True)
    (OUT / '.nojekyll').touch()
    page = (ROOT / 'index.html').read_text()
    original = 'video.src = ours ? "videos/" + id + ".mp4" : "videos/baselines/" + id + "__" + m[0] + ".mp4";'
    replacement = 'video.src = ' + json.dumps(MEDIA) + ' + (ours ? "videos/" + id + ".mp4" : "videos/baselines/" + id + "__" + m[0] + ".mp4");'
    assert page.count(original) == 1, 'Comparison video assignment changed; update the builder.'
    (OUT / 'index.html').write_text(page.replace(original, replacement))
    # Copy a real local teaser or resolve its Git LFS pointer during Actions checkout.
    source = ROOT / 'videos/teaser.mp4'
    target = OUT / 'videos/teaser.mp4'
    target.parent.mkdir(exist_ok=True)
    with source.open('rb') as stream:
        pointer = stream.read(256)
    if pointer.startswith(b'version https://git-lfs.github.com/spec/v1'):
        req = urllib.request.Request(MEDIA + 'videos/teaser.mp4', headers={'User-Agent': 'FilmHarness-Pages-build'})
        with urllib.request.urlopen(req, timeout=120) as response, target.open('wb') as stream:
            shutil.copyfileobj(response, stream)
    else:
        shutil.copy2(source, target)
    manifest = json.loads((ROOT / 'assets/teaser_edit.json').read_text())
    with target.open('rb') as stream:
        actual = hashlib.file_digest(stream, 'sha256').hexdigest()
    assert actual == manifest['output']['sha256'], 'Downloaded teaser does not match the source manifest.'
    total = sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
    assert total < 1_000_000_000, 'Pages artifact exceeds 1 GB.'
    print(f'Pages site prepared: {total / 1_000_000:.1f} MB. Full films use original-quality media URLs.')


if __name__ == '__main__':
    build()
