from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "manifest.json"


def family_profile(
    scores: tuple[int, int, int, int, int, int, int, int, int],
    roles: list[str],
    mechanisms: list[str],
    avoid: list[str],
) -> dict:
    keys = (
        "opacity",
        "line_precision",
        "medical_label_legibility",
        "portrait_fit",
        "anatomy_fit",
        "scene_fit",
        "public_health_fit",
        "archive_fit",
        "digital_fit",
    )
    return {
        "capabilities": dict(zip(keys, scores)),
        "recommended_roles": roles,
        "mechanisms": mechanisms,
        "avoid": avoid,
    }


FAMILY_DEFAULTS = {
    "wet_paint": family_profile(
        (3, 2, 3, 5, 3, 5, 3, 2, 2),
        ["base_medium"],
        ["layered_color", "visible_brushwork", "organic_edges"],
        ["uniform_digital_gradient", "plastic_surface"],
    ),
    "fluid_ink": family_profile(
        (3, 2, 2, 4, 2, 5, 3, 2, 3),
        ["base_medium", "texture_accent"],
        ["fluid_bloom", "transparent_overlap", "edge_pooling"],
        ["mechanically_uniform_fill", "perfectly_repeatable_edges"],
    ),
    "sprayed_color": family_profile(
        (4, 3, 4, 3, 3, 4, 5, 2, 4),
        ["base_medium", "texture_accent"],
        ["atomized_color", "soft_masked_edges", "overspray"],
        ["brushstroke_dominance", "unbroken_flat_vector_fill"],
    ),
    "drawing_ink": family_profile(
        (4, 5, 5, 3, 5, 3, 5, 4, 4),
        ["line_medium"],
        ["controlled_line_weight", "hatching", "ink_edge_definition"],
        ["soft_edge_only_rendering", "line_free_airbrushed_surface"],
    ),
    "dry_drawing": family_profile(
        (3, 4, 4, 5, 4, 4, 3, 4, 3),
        ["base_medium", "texture_accent"],
        ["tooth_grain", "layered_strokes", "pressure_variation"],
        ["glass_smooth_fill", "perfectly uniform gradients"],
    ),
    "metalpoint": family_profile(
        (2, 5, 4, 4, 5, 3, 2, 5, 2),
        ["line_medium"],
        ["fine_metallic_line", "toned_ground", "delicate_crosshatching"],
        ["heavy_opaque_fill", "broad saturated brushwork"],
    ),
    "drawing_surface": family_profile(
        (5, 5, 5, 3, 5, 3, 5, 4, 3),
        ["line_medium", "base_medium"],
        ["subtractive_highlight", "high_contrast_line", "dark_ground"],
        ["low_contrast_tonal_mush", "transparent_wash_dominance"],
    ),
    "printmaking": family_profile(
        (5, 4, 4, 3, 4, 4, 5, 5, 3),
        ["base_medium", "texture_accent"],
        ["ink_transfer", "plate_or_block_texture", "limited_color_separation"],
        ["seamless_photorealistic_gradient", "textureless_vector_surface"],
    ),
    "craft_surface": family_profile(
        (5, 3, 3, 3, 3, 4, 4, 5, 2),
        ["texture_accent", "base_medium"],
        ["material_surface", "handmade_irregularity", "layered_construction"],
        ["materialless_flat_rendering", "perfectly uniform repetition"],
    ),
    "wall_surface": family_profile(
        (4, 3, 3, 4, 3, 5, 3, 5, 2),
        ["base_medium", "texture_accent"],
        ["mineral_ground", "matte_pigment", "aged_wall_texture"],
        ["glossy_plastic_finish", "neon_digital_glow"],
    ),
    "wax_medium": family_profile(
        (5, 3, 3, 4, 3, 4, 3, 4, 2),
        ["base_medium", "texture_accent"],
        ["wax_layering", "translucent_depth", "scraped_surface"],
        ["flat_unlayered_fill", "sterile_vector_edges"],
    ),
    "assembled_surface": family_profile(
        (5, 2, 3, 4, 2, 5, 4, 5, 3),
        ["texture_accent", "base_medium"],
        ["assembled_fragments", "layered_edges", "material_contrast"],
        ["single_surface_uniformity", "seamless_airbrush_finish"],
    ),
    "granular_surface": family_profile(
        (5, 2, 2, 3, 2, 4, 4, 5, 2),
        ["texture_accent"],
        ["granular_deposition", "ritual_patterning", "tactile_surface"],
        ["smooth_glossy_fill", "pixel_perfect_micro_edges"],
    ),
    "textile": family_profile(
        (5, 3, 3, 4, 3, 4, 4, 5, 2),
        ["texture_accent", "line_medium"],
        ["thread_direction", "stitched_contour", "fabric_ground"],
        ["threadless_flat_fill", "perfectly smooth gradients"],
    ),
    "marbling": family_profile(
        (4, 1, 2, 3, 1, 5, 3, 4, 2),
        ["texture_accent", "base_medium"],
        ["floating_pigment", "fluid_combing", "nonrepeatable_veining"],
        ["precise_label_linework", "mechanically repeated pattern"],
    ),
    "decorated_paper": family_profile(
        (4, 2, 3, 3, 2, 4, 4, 5, 2),
        ["texture_accent", "output_finish"],
        ["handmade_paper_pattern", "paste_drag", "surface_repeat"],
        ["featureless_white_ground", "photorealistic_depth"],
    ),
    "transfer_texture": family_profile(
        (4, 2, 3, 3, 2, 4, 4, 5, 2),
        ["texture_accent"],
        ["contact_transfer", "found_surface_imprint", "organic_irregularity"],
        ["clean_vector_uniformity", "untextured fill"],
    ),
    "photographic": family_profile(
        (4, 4, 4, 5, 4, 5, 3, 5, 3),
        ["base_medium", "output_finish"],
        ["light_sensitive_process", "tonal_print_surface", "chemical_or_contact_artifact"],
        ["cartoon_outline_dominance", "synthetic_neon_palette"],
    ),
    "digital_output": family_profile(
        (5, 5, 5, 5, 5, 5, 5, 3, 5),
        ["output_finish"],
        ["high_resolution_inkjet_output", "controlled_color_management", "paper_dependent_finish"],
        ["output_method_as_painting_style", "invented_handmade_artifacts"],
    ),
    "digital_creation": family_profile(
        (5, 5, 5, 4, 5, 5, 5, 2, 5),
        ["base_medium", "line_medium", "texture_accent"],
        ["digital_mark_construction", "editable_layers", "resolution_specific_edges"],
        ["unrequested_physical_craft_artifacts", "mixed_resolution_edges"],
    ),
}


MEDIUM_KIND = {
    "photographic": "photographic_process",
    "digital_output": "digital_output_method",
    "digital_creation": "digital_creation_method",
}


def repo_path(relative_media_path: str) -> str:
    return f"Media/{relative_media_path}"


def partner_role(family: str) -> str:
    roles = FAMILY_DEFAULTS[family]["recommended_roles"]
    return roles[0]


def main() -> None:
    source = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    media_by_id = {item["id"]: item for item in source["media"]}
    enriched = []

    for mid in sorted(media_by_id):
        item = media_by_id[mid]
        family = item["family"]
        defaults = FAMILY_DEFAULTS[family]
        profile_path = ROOT / "profiles" / f"{mid}.json"
        pilot = profile_path.exists()
        profile = json.loads(profile_path.read_text(encoding="utf-8")) if pilot else None
        capabilities = profile["scores"] if profile else defaults["capabilities"]
        partner_ids = profile.get("recommended_line_partner", []) if profile else []
        panels = profile.get("reference_panels", []) if profile else []

        partners = []
        for partner_id in partner_ids:
            partner = media_by_id[partner_id]
            partner_is_pilot = (ROOT / "profiles" / f"{partner_id}.json").exists()
            partners.append(
                {
                    "id": partner_id,
                    "role": partner_role(partner["family"]),
                    "automatic_pairing_allowed": partner_is_pilot,
                }
            )

        enriched.append(
            {
                "id": mid,
                "name_zh": item["name_zh"],
                "name_en": item["name_en"],
                "family": family,
                "medium_kind": MEDIUM_KIND.get(family, "physical_visual_medium"),
                "classification_level": item["classification_level"],
                "card": item["card"],
                "source_sha256": item["source_sha256"],
                "profile_status": "pilot" if pilot else "pending",
                "assets": {
                    "card": repo_path(item["card"]),
                    "thumbnail": f"Media/thumbnails/{mid}.jpg",
                    "reference_panels": [repo_path(path) for path in panels],
                },
                "mechanisms": defaults["mechanisms"],
                "capabilities": capabilities,
                "recommended_roles": defaults["recommended_roles"],
                "compatible_partners": partners,
                "avoid": defaults["avoid"],
                "resolver": {
                    "automatic_use_allowed": pilot,
                    "manual_review_required": not pilot,
                    "assessment_basis": "pilot_visual_estimate" if pilot else "family_default_estimate",
                    "confidence": 0.72 if pilot else 0.35,
                },
            }
        )

    atlas = {
        "$schema": "schemas/media-atlas.schema.json",
        "atlas_id": "art-media-atlas",
        "schema_version": "1.0.0",
        "atlas_version": "2026.07.23",
        "repository": "hoiyu915-droid/art-media-atlas",
        "asset_path_base": "repository_root",
        "source_card_count": len(enriched),
        "automatic_candidate_count": sum(
            item["resolver"]["automatic_use_allowed"] for item in enriched
        ),
        "capability_scale": {
            "minimum": 1,
            "maximum": 5,
            "meaning": "1 is weak fit; 5 is strong fit for the named visual task.",
            "fields": [
                "opacity",
                "line_precision",
                "medical_label_legibility",
                "portrait_fit",
                "anatomy_fit",
                "scene_fit",
                "public_health_fit",
                "archive_fit",
                "digital_fit",
            ],
        },
        "resolver_contract": {
            "consumer_inputs": [
                "consumer",
                "lane",
                "card_requirements",
                "current_seed_medium",
                "requested_medium_ids",
            ],
            "decision_actions": ["KEEP_NATIVE", "ADD_PARTNER", "REPLACE_BASE", "BLOCK"],
            "default_candidate_filter": "resolver.automatic_use_allowed == true",
            "exploratory_candidate_filter": "all media; pending entries require manual review",
            "default_fallback_medium": "M01",
            "max_base_media": 1,
            "max_partner_media": 2,
            "full_cards_for_human_selection_only": True,
            "generation_reference_policy": "Send only selected reference_panels, never the complete 3x3 card.",
        },
        "panel_policy": source["panel_policy"],
        "limitations": source["limitations"],
        "media": enriched,
    }
    MANIFEST_PATH.write_text(
        json.dumps(atlas, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"Built {MANIFEST_PATH}: {len(enriched)} media, "
        f"{atlas['automatic_candidate_count']} automatic candidates."
    )


if __name__ == "__main__":
    main()
