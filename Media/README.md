# Media Atlas M01-M75 (pilot)

This local reference system turns the 75 complete cards into selectable, cropped, reusable visual references.

## Quick use

From the `Media/` directory:

```bash
python3 tools/atlas_cli.py list
python3 tools/atlas_cli.py show M01
python3 tools/atlas_cli.py select clinical_soft --limit 5
python3 tools/atlas_cli.py select anatomy --limit 5
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

## Status

Profile scores are pilot visual estimates. Run controlled smoke tests before promoting them to production defaults.
