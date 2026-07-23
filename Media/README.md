# Media Atlas M01-M75

This reference system turns the 75 complete cards into selectable, cropped, reusable visual references and a machine-readable resolver feed.

## Canonical resolver feed

`manifest.json` is the canonical machine-readable source for the gallery and external consumers such as `seed-resolver`. It contains all 75 media records, repository-relative assets, mechanisms, capability scores, recommended roles, partner metadata, avoid rules, confidence, and automatic-use eligibility.

- The 12 cropped pilot media are eligible for automatic selection.
- The remaining 63 records expose low-confidence family defaults and require manual review.
- `schemas/media-atlas.schema.json` defines the interchange contract.
- `tools/build_resolver_manifest.py` rebuilds the enriched JSON deterministically from the card index and reviewed pilot profiles.

Consumers should pin `atlas_version` plus the fetched blob SHA. They should send only the selected records and cropped reference panels to an image generator, never the complete 75-record payload or full 3 × 3 cards.

## Quick use

From the `Media/` directory:

```bash
python3 tools/atlas_cli.py list
python3 tools/atlas_cli.py show M01
python3 tools/atlas_cli.py select clinical_soft --limit 5
python3 tools/atlas_cli.py select anatomy --limit 5
python3 tools/atlas_cli.py select anatomy --limit 5 --include-review
python3 tools/atlas_cli.py recipe clinical-soft-precise
python3 tools/validate_atlas.py
```

The first pilot profiles are M01, M02, M06, M17, M22, M39, M40, M43, M50, M69, M73, and M74. Each has four reference-ready crops: 02 fingerprint, 05 portrait, 06 anatomy, and 09 micro-technique.

## Safe operating rule

- Humans browse the full card in `cards/`.
- Image generation receives only the relevant files in `panels/`.
- Reference panels control visual medium only. They are not medical evidence and their text must not be copied.
- Keep source validation and post-render number/text inspection in the rendering workflow.

## Crop geometry

All source cards were verified at 1536 x 1024, but their panel boundaries drift. The build process detected each dark-teal `Mxx-nn` header badge, derived per-card panel boundaries, and stored the result in `panels/crop-calibration.json`. Reference crops start below the badge and stop before the next detected panel, reducing header and neighboring-panel contamination.

## Assessment status

Pilot profile scores are practical visual estimates. Family-default scores are explicitly lower confidence and are excluded from automatic selection. Run controlled smoke tests before promoting additional media to automatic-use status.
