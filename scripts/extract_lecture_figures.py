"""Extract figure images from the course PDF slide decks.

Lectures 3, 8 and 12 were issued as beamer PDFs rather than as Quarto HTML, so
their plots exist only as slide content. This script rasterises the pages that
carry a figure, trims the beamer furniture (the navigation band at the top, the
frame title, the caption and the page number) and writes one PNG per figure into
``lectures/figures-reconstructed/``.

Rasterising the page is deliberate. Several plots are vector drawings produced by
R, so ``pdfimages`` never sees them, and every embedded raster carries a paired
soft mask, so extracting the raster alone gives the wrong transparency.

Usage:
    .venv/bin/python scripts/extract_lecture_figures.py            # every figure
    .venv/bin/python scripts/extract_lecture_figures.py 8          # one lecture
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "lectures" / "figures-reconstructed"
PDF_DIR = Path.home() / "Downloads"
DPI = 200


@dataclass(frozen=True)
class Figure:
    """One figure to lift out of a slide.

    ``page`` is the physical PDF page, one-based, which is not the frame number:
    beamer overlays make several pages share a frame. ``top`` and ``bottom`` are
    the fractions of page height to discard before the white margins are trimmed,
    which is how the frame title above the plot and the caption below it are
    removed. ``left`` and ``right`` do the same horizontally, for the two-column
    frames whose diagram sits beside a block of bullets.
    """

    page: int
    name: str
    top: float = 0.13
    bottom: float = 0.04
    left: float = 0.0
    right: float = 0.0


DECKS: dict[str, tuple[str, tuple[Figure, ...]]] = {
    "3": (
        "Lecture-3.pdf",
        (
            Figure(8, "scaling-laws", top=0.38, bottom=0.26),
            Figure(9, "intelligence-age", top=0.15, bottom=0.28),
            Figure(13, "fashion-mnist-samples", top=0.48, bottom=0.10),
            Figure(14, "fashion-mnist-pca", top=0.26, bottom=0.20),
            Figure(18, "fashion-mnist-autoencoder", top=0.16, bottom=0.03),
            Figure(19, "representation-to-prediction", top=0.42, bottom=0.38),
            Figure(21, "cnn-layers-1-2", top=0.44, bottom=0.05),
            Figure(22, "cnn-layer-5", top=0.28, bottom=0.03),
            Figure(24, "single-layer-fnn", top=0.17, bottom=0.06, left=0.52),
            Figure(25, "deep-fnn", top=0.17, bottom=0.05, left=0.48),
            Figure(26, "fnn-generalises-glm", top=0.17, bottom=0.30, left=0.50),
            Figure(32, "cnn-convolution", top=0.17, bottom=0.04),
            Figure(36, "rnn-diagram", top=0.17, bottom=0.06),
            Figure(37, "lstm-cell", top=0.28, bottom=0.16),
            Figure(38, "gru-cell", top=0.28, bottom=0.20),
            Figure(41, "autoencoder", top=0.17, bottom=0.05, left=0.48),
            Figure(46, "cann-implementation", top=0.17, bottom=0.30),
        ),
    ),
    "8": (
        "Lecture-8.pdf",
        (
            Figure(11, "ridge-vs-lasso-penalisation", top=0.05, bottom=0.02),
            Figure(14, "feasible-set-of-solutions", top=0.05, bottom=0.02),
            Figure(33, "icenet-pdp", top=0.16, bottom=0.15),
            Figure(34, "icenet-ice-plots", top=0.16, bottom=0.15),
            Figure(35, "icenet-pdp-constraint-parameters", top=0.16, bottom=0.15),
        ),
    ),
    "12": (
        "Lecture-12.pdf",
        (
            Figure(25, "icl-ct-architecture", top=0.17, bottom=0.30),
            Figure(27, "context-retrieval", top=0.12, bottom=0.27, left=0.56),
            Figure(38, "pca-cls-tokens", top=0.13, bottom=0.05),
            Figure(39, "pca-training-phases", top=0.13, bottom=0.05),
        ),
    ),
}


def render_page(pdf: Path, page: int, workdir: Path) -> Image.Image:
    """Rasterise one PDF page to a PIL image."""
    prefix = workdir / f"page{page}"
    subprocess.run(
        ["pdftoppm", "-r", str(DPI), "-f", str(page), "-l", str(page), "-png",
         str(pdf), str(prefix)],
        check=True,
    )
    rendered = sorted(workdir.glob(f"page{page}-*.png"))
    if not rendered:
        raise FileNotFoundError(f"pdftoppm produced nothing for {pdf.name} page {page}")
    return Image.open(rendered[0]).convert("RGB")


def mask_page_number(image: Image.Image) -> Image.Image:
    """Whiten the beamer page counter in the bottom-left corner.

    Left in place it survives the margin trim as a stray "10/36" beside the
    plot, because it is ink like any other.
    """
    masked = image.copy()
    width, height = masked.size
    box = (0, int(height * 0.92), int(width * 0.12), height)
    masked.paste((255, 255, 255), box)
    return masked


def trim_white(image: Image.Image, pad: int = 12) -> Image.Image:
    """Crop to the bounding box of everything that is not the white page ground."""
    pixels = np.asarray(image)
    ink = (pixels < 245).any(axis=2)
    rows = np.flatnonzero(ink.any(axis=1))
    cols = np.flatnonzero(ink.any(axis=0))
    if rows.size == 0 or cols.size == 0:
        return image
    top, bottom = rows[0], rows[-1]
    left, right = cols[0], cols[-1]
    height, width = ink.shape
    return image.crop((
        max(left - pad, 0),
        max(top - pad, 0),
        min(right + 1 + pad, width),
        min(bottom + 1 + pad, height),
    ))


def extract(lecture: str) -> list[Path]:
    pdf_name, figures = DECKS[lecture]
    pdf = PDF_DIR / pdf_name
    if not pdf.exists():
        raise SystemExit(
            f"{pdf} not found. The decks live in the vault rather than this repo; "
            "place the PDF in ~/Downloads or edit PDF_DIR."
        )
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written = []
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        for figure in figures:
            page = mask_page_number(render_page(pdf, figure.page, workdir))
            height = page.height
            body = page.crop((
                int(page.width * figure.left),
                int(height * figure.top),
                int(page.width * (1 - figure.right)),
                int(height * (1 - figure.bottom)),
            ))
            out = OUT_DIR / f"lecture{int(lecture):02d}-{figure.name}.png"
            trim_white(body).save(out, optimize=True)
            written.append(out)
            print(f"{out.relative_to(REPO)}  ({out.stat().st_size // 1024} KB)")
    return written


def main() -> None:
    wanted = sys.argv[1:] or sorted(DECKS)
    for lecture in wanted:
        if lecture not in DECKS:
            raise SystemExit(f"no figure table for lecture {lecture}")
        extract(lecture)


if __name__ == "__main__":
    main()
