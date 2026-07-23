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
    assert manifest["$schema"] == "schemas/media-atlas.schema.json"
    assert manifest["atlas_id"] == "art-media-atlas"
    assert manifest["schema_version"] == "1.0.0"
    assert manifest["repository"] == "hoiyu915-droid/art-media-atlas"
    assert manifest["resolver_contract"]["decision_actions"] == [
        "KEEP_NATIVE",
        "ADD_PARTNER",
        "REPLACE_BASE",
        "BLOCK",
    ]
    media = manifest["media"]
    assert len(media) == 75, f"Expected 75 manifest records, found {len(media)}"
    assert sorted(item["id"] for item in media) == [f"M{i:02d}" for i in range(1, 76)]

    score_fields = set(manifest["capability_scale"]["fields"])
    automatic = [item for item in media if item["resolver"]["automatic_use_allowed"]]
    assert len(automatic) == manifest["automatic_candidate_count"] == 12
    for item in media:
        assert set(item["capabilities"]) == score_fields, f"Capability fields drift: {item['id']}"
        assert all(1 <= value <= 5 for value in item["capabilities"].values())
        assert item["mechanisms"], f"Missing mechanisms: {item['id']}"
        assert item["recommended_roles"], f"Missing roles: {item['id']}"
        assert item["avoid"], f"Missing avoid rules: {item['id']}"
        resolver = item["resolver"]
        assert resolver["automatic_use_allowed"] != resolver["manual_review_required"]
        if resolver["automatic_use_allowed"]:
            assert resolver["assessment_basis"] == "pilot_visual_estimate"
            assert len(item["assets"]["reference_panels"]) == 4
        else:
            assert resolver["assessment_basis"] == "family_default_estimate"
            assert item["assets"]["reference_panels"] == []

        for asset_name in ("card", "thumbnail"):
            asset = ROOT.parent / item["assets"][asset_name]
            assert asset.is_file(), f"Missing {asset_name}: {asset}"
        for panel_path in item["assets"]["reference_panels"]:
            panel = ROOT.parent / panel_path
            assert panel.is_file(), f"Missing reference panel: {panel}"

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
    thumbnails = sorted((ROOT / "thumbnails").glob("M*.jpg"))
    assert len(thumbnails) == 75, f"Expected 75 gallery thumbnails, found {len(thumbnails)}"
    for thumbnail in thumbnails:
        assert image_size(thumbnail) == (600, 400), f"Unexpected thumbnail size: {thumbnail}"
    assert image_size(ROOT / "social-preview.jpg") == (1200, 630)
    schema = ROOT / "schemas" / "media-atlas.schema.json"
    assert schema.is_file(), "Missing resolver JSON Schema"
    schema_data = json.loads(schema.read_text(encoding="utf-8"))
    assert schema_data["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    index = ROOT.parent / "index.html"
    assert index.is_file(), "Missing root index.html"
    index_text = index.read_text(encoding="utf-8")
    assert 'fetch("Media/manifest.json")' in index_text
    assert "Media/thumbnails/M01.jpg" in index_text
    assert (ROOT / "recipes" / "clinical-soft-precise.yaml").is_file()
    assert (ROOT / "panels" / "crop-calibration.json").is_file()

    print(
        "Media Atlas validation passed: 75 resolver records, 75 cards, "
        "75 thumbnails, 12 automatic candidates, 48 reference panels."
    )


if __name__ == "__main__":
    main()
