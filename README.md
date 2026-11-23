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

This push preserves the repository's private visibility and does not enable a public site or any automatic deployment workflow.

GitHub Pages cannot serve this entire 6 GB collection directly, and Git LFS pointers are not playable video files. For publication, keep the page, figures, paper, and teaser on Pages, and serve complete films from a suitable public media host or public GitHub Release. Configure those media URLs before enabling Pages. Do not place authentication tokens in browser code.

The original offline project-page package remains independent of this repository.
