# Media Atlas pilot validation

Validated on 2026-07-23 (Asia/Hong_Kong).

- Source cards: 75; identifiers M01-M75 complete and unique.
- Card integrity: 75/75 output-card SHA-256 values match `manifest.json`.
- Pilot profiles: 12 YAML files and 12 JSON files.
- Core reference panels: 48 PNG files; all decode successfully.
- Crop geometry: every output panel is at least 400 px wide and 240 px high.
- Crop QA: visual contact-sheet inspection passed after per-card header detection replaced fixed-grid cropping.
- YAML: manifest, profiles, and recipe parse successfully with Ruby YAML.
- CLI: `list`, `show`, `select`, and `recipe` smoke tests passed with the macOS system Python.
- Cache hygiene: no `__pycache__` or `.pyc` files are present in the atlas.

Known limits:

- Crops intentionally retain text and labels that belong inside the panel. Prompts must prohibit copying reference text.
- Profile scores are visual estimates, not measured production benchmarks.
- Medical, chemical, and craft claims shown in the source cards are not validated evidence.
