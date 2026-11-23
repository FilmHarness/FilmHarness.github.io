# FilmHarness

Project page for **FilmHarness: An Agentic Framework for Autonomous Film Generation**.

Yiyun Zhou, Jingwei Shi, Ruijie Quan, Jingyuan Chen, and Bo An.

Nanyang Technological University · Zhejiang University · Hong Kong Polytechnic University.

## Local preview

Install Git LFS before cloning, then retrieve the full media files:

```bash
git lfs install
git clone git@github.com:FilmHarness/FilmHarness.github.io.git
cd FilmHarness.github.io
git lfs pull
python3 serve.py
```

Open the localhost address printed by the preview server. No build step is required. The server supports byte-range requests for video seeking and concurrent playback.

## Contents

- `index.html`: complete project page with authors, paper, method, quantitative results, and interactive video comparisons.
- `assets/paper/FilmHarness.pdf`: supplied nonanonymous paper.
- `videos/teaser.mp4`: high-quality one-minute edit, with genre and backbone annotations in the top left.
- `videos/`: 56 complete films across four synopses, two video backbones, FilmHarness, and six baselines.
- `assets/media_manifest.json`: dimensions, frame rates, file hashes, and verification that original encoded video streams are preserved.
- Code will be released at https://github.com/FilmHarness/FilmHarness.

All MP4 files are tracked with Git LFS. The complete media collection is approximately 6 GB. FilmHarness appears last in the comparison gallery.

## Publication

The public site is built and deployed by `.github/workflows/pages.yml`. In repository **Settings → Pages**, select **GitHub Actions** as the source to enable deployment. Pushes to `main` then update the site automatically.

`scripts/build_pages.py` prepares a lightweight Pages artifact containing the page, images, paper, and an actual playable teaser. It resolves the teaser's Git LFS pointer and verifies its SHA-256. Complete films load directly from the public Git LFS media endpoint, retaining their original encoded video streams. The `main` source page continues to work offline after `git lfs pull`.

The complete 6 GB collection is not bundled into the Pages artifact. Public media downloads consume the repository owner's Git LFS bandwidth allowance. For substantial traffic, migrate complete-film URLs to a dedicated media host or public Release.

The original offline project-page package remains independent of this repository.
