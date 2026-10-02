#!/usr/bin/env python3
"""Generate square PNG logo/icon assets without external dependencies.

Draws a rounded blue tile with a white upward "career ladder" glyph.
"""
from __future__ import annotations

import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "assets"
BRAND = (0x1D, 0x4E, 0xD8)
WHITE = (0xFF, 0xFF, 0xFF)


def write_png(path: Path, size: int, pixels: list[list[tuple[int, int, int, int]]]) -> None:
    raw = bytearray()
    for row in pixels:
        raw.append(0)
        for r, g, b, a in row:
            raw.extend((r, g, b, a))

    def chunk(kind: bytes, data: bytes) -> bytes:
        body = kind + data
        return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body) & 0xFFFFFFFF)

    header = struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header) + chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b"")
    path.write_bytes(png)


def inside_rounded_square(x: float, y: float, size: int, radius: float) -> bool:
    inner = size - radius
    cx = min(max(x, radius), inner)
    cy = min(max(y, radius), inner)
    return (x - cx) ** 2 + (y - cy) ** 2 <= radius**2


def inside_glyph(x: float, y: float, size: int) -> bool:
    """Three ascending bars (a simple 'growth' mark) centered in the tile."""
    unit = size / 16
    bar_width = 2.6 * unit
    gap = 0.9 * unit
    total = 3 * bar_width + 2 * gap
    left = (size - total) / 2
    baseline = size * 0.74
    heights = [4 * unit, 6.5 * unit, 9 * unit]
    for index, height in enumerate(heights):
        x0 = left + index * (bar_width + gap)
        if x0 <= x <= x0 + bar_width and baseline - height <= y <= baseline:
            return True
    return False


def render(size: int) -> list[list[tuple[int, int, int, int]]]:
    radius = size * 0.22
    rows = []
    for py in range(size):
        row = []
        for px in range(size):
            x, y = px + 0.5, py + 0.5
            if not inside_rounded_square(x, y, size, radius):
                row.append((0, 0, 0, 0))
            elif inside_glyph(x, y, size):
                row.append((*WHITE, 255))
            else:
                row.append((*BRAND, 255))
        rows.append(row)
    return rows


def main() -> None:
    ROOT.mkdir(exist_ok=True)
    write_png(ROOT / "logo.png", 512, render(512))
    write_png(ROOT / "icon.png", 128, render(128))
    print("wrote assets/logo.png (512) and assets/icon.png (128)")


if __name__ == "__main__":
    main()
