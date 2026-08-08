# Art Media Atlas

A standardized visual reference atlas comparing 75 traditional and contemporary art media through a consistent 3 × 3 test-board framework.

## Web gallery

Open [`index.html`](index.html) through GitHub Pages to browse all 75 cards with search, category filters, responsive layout, full-resolution viewing, and shareable card links. Lightweight thumbnails keep the first visit fast; full cards load only when opened.

## Media system

The usable atlas is in [`Media/`](Media/README.md):

- `Media/cards/` — complete M01–M75 cards for human browsing.
- `Media/panels/` — pilot model-reference crops for 12 representative media.
- `Media/profiles/` — structured YAML and JSON profiles.
- `Media/recipes/` — reusable mixed-media prompt recipes.
- `Media/contact-sheets/` — visual QA and browsing sheets.
- `Media/thumbnails/` — lightweight gallery thumbnails.
- `Media/tools/atlas_cli.py` — local selector and query tool.
- `Media/manifest.json` — canonical resolver-ready index shared by the gallery and machine consumers.
- `Media/schemas/media-atlas.schema.json` — JSON Schema for external consumers.
- `Media/manifest.yaml` / `Media/manifest.csv` — legacy convenience snapshots; not resolver truth.

## Quick use

```bash
python3 Media/tools/atlas_cli.py list
python3 Media/tools/atlas_cli.py show M01
python3 Media/tools/atlas_cli.py select clinical_soft --limit 5
python3 Media/tools/atlas_cli.py select anatomy --limit 5
python3 Media/tools/atlas_cli.py select anatomy --limit 5 --include-review
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

## Why this project matters

Art Media Atlas provides a consistent benchmark and machine-readable vocabulary for comparing 75 visual media. Its shared test framework, resolver-ready manifests, schemas, profiles, and cropped reference panels help people and generation pipelines select media intentionally instead of relying on ambiguous style labels.

The repository is actively maintained through pull-request review, manifest and schema validation, asset-integrity checks, gallery maintenance, and release-oriented integration.

## Maintainer workflow and Codex

Codex may assist with repository inspection, pull-request preparation, validation, regression repair, documentation, and release workflows. Maintainers review every change and remain responsible for asset rights, attribution, correctness, and merge decisions.

## Contributing and security

See [`CONTRIBUTING.md`](CONTRIBUTING.md) before adding media profiles, recipes, code, or assets. Report vulnerabilities through the private process in [`SECURITY.md`](SECURITY.md).

## Adoption and impact

The atlas is designed for artists, educators, prompt and rendering-tool authors, and multilingual visual-generation workflows. No unverified traffic, download, or adoption figures are claimed. Public integrations may be recorded through issues or pull requests so impact remains auditable.

## License

Application code, tools, tests, schemas, and validation logic are licensed under Apache-2.0. Original documentation, structured data, recipes, and visual assets are licensed under CC BY 4.0 where rights permit. See [`LICENSE`](LICENSE), [`LICENSE-ASSETS.md`](LICENSE-ASSETS.md), and [`NOTICE.md`](NOTICE.md) for exact boundaries and exclusions.

## Citation

Use [`CITATION.cff`](CITATION.cff) and cite the exact commit or release used.
