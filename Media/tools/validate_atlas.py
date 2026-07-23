from __future__ import annotations

import hashlib
import json
import struct
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def image_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as stream:
        header = stream.read(24)
        if header.startswith(b"\x89PNG\r\n\x1a\n"):
            return struct.unpack(">II", header[16:24])
        if header[:2] != b"\xff\xd8":
            raise AssertionError(f"Unsupported image format: {path}")
        stream.seek(2)
        while True:
            marker_start = stream.read(1)
            if not marker_start:
                break
            if marker_start != b"\xff":
                continue
            marker = stream.read(1)
            while marker == b"\xff":
                marker = stream.read(1)
            if marker in {bytes([value]) for value in range(0xC0, 0xC4)} | {bytes([value]) for value in range(0xC5, 0xC8)} | {bytes([value]) for value in range(0xC9, 0xCC)} | {bytes([value]) for value in range(0xCD, 0xD0)}:
                stream.read(3)
                height, width = struct.unpack(">HH", stream.read(4))
                return width, height
            length_bytes = stream.read(2)
            if len(length_bytes) != 2:
                break
            length = struct.unpack(">H", length_bytes)[0]
            stream.seek(length - 2, 1)
    raise AssertionError(f"Could not read image dimensions: {path}")


def main() -> None:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    media = manifest["media"]
    assert len(media) == 75, f"Expected 75 manifest records, found {len(media)}"
    assert sorted(item["id"] for item in media) == [f"M{i:02d}" for i in range(1, 76)]

    cards = [ROOT / item["card"] for item in media]
    assert len(set(cards)) == 75
    for item, card in zip(media, cards):
        assert card.is_file(), f"Missing card: {card}"
        assert sha256(card) == item["source_sha256"], f"SHA mismatch: {item['id']}"
        assert image_size(card) == (1536, 1024), f"Unexpected card dimensions: {card}"

    panels = sorted((ROOT / "panels").glob("M*/*.png"))
    assert len(panels) == 48, f"Expected 48 pilot panels, found {len(panels)}"
    for panel in panels:
        width, height = image_size(panel)
        assert width >= 400 and height >= 240, f"Implausible crop: {panel} ({width}x{height})"

    profiles = sorted((ROOT / "profiles").glob("M*.json"))
    assert len(profiles) == 12, f"Expected 12 pilot profiles, found {len(profiles)}"
    assert (ROOT / "recipes" / "clinical-soft-precise.yaml").is_file()
    assert (ROOT / "panels" / "crop-calibration.json").is_file()

    print("Media Atlas validation passed: 75 cards, 12 profiles, 48 panels.")


if __name__ == "__main__":
    main()
