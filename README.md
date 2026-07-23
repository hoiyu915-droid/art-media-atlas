# Art Media Atlas

A standardized visual reference atlas comparing 75 traditional and contemporary art media through a consistent 3 × 3 test-board framework.

## Media system

The usable atlas is in [`Media/`](Media/README.md):

- `Media/cards/` — complete M01–M75 cards for human browsing.
- `Media/panels/` — pilot model-reference crops for 12 representative media.
- `Media/profiles/` — structured YAML and JSON profiles.
- `Media/recipes/` — reusable mixed-media prompt recipes.
- `Media/contact-sheets/` — visual QA and browsing sheets.
- `Media/tools/atlas_cli.py` — local selector and query tool.
- `Media/manifest.yaml` / `Media/manifest.json` / `Media/manifest.csv` — canonical index.

## Quick use

```bash
python3 Media/tools/atlas_cli.py list
python3 Media/tools/atlas_cli.py show M01
python3 Media/tools/atlas_cli.py select clinical_soft --limit 5
python3 Media/tools/atlas_cli.py select anatomy --limit 5
python3 Media/tools/atlas_cli.py recipe clinical-soft-precise
python3 Media/tools/validate_atlas.py
```

## Standard test framework

Each full card uses the same nine subjects and panel roles to compare opacity, edge behavior, layering, texture, portrait rendering, medical illustration, narrative scenes, infographic layout, and technique steps.

Full cards are intended for human selection. Image-generation workflows should use only the relevant cropped panels so the model is less likely to reproduce the 3 × 3 grid, labels, or fixed test motifs.

## Naming convention

Cards use `M##__english_medium_name.ext`. Panel paths use `Media/panels/M##/NN__panel-role.png`.

## Scope and limitations

This repository is a visual-reference and benchmark system. Generated card text is not authoritative medical, craft, chemical-safety, or historical evidence. Digital entries M72–M75 are classified separately from traditional physical media in the manifest.
