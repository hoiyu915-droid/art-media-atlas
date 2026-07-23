# Mixed Media v1 Proposal Bundle

This directory is a **non-executable proposal** for using the 75-card Art Media Atlas
inside medical and research-infographic workflows.

## Files

- `MIXED_MEDIA_GUIDELINE_v1.md` — human-readable mixed-media rules.
- `media_role_matrix_v1.csv` — 75-row review table.
- `media_role_matrix_v1.json` — machine-readable copy of the matrix.
- `seed14_default_media_policy.provisional.json` — proposal for the M17 + M22 SEED14 default.

## Source pins

- Art Media Atlas ref: `16fe341270150e7b60f3c547364580cdbef11617`
- Atlas version: `2026.07.23`
- Atlas blob SHA: `ae096ceaf1ff2b0afe9c5c181dab5f51d9e2370c`
- SEED14 binding blob SHA: `80a3373ba206007d93d52843a89cb3de0261664f`

## Safety boundary

The atlas currently exposes 12 reviewed pilot records for automatic selection and
63 low-confidence family defaults requiring manual review. This proposal preserves
that boundary. A row marked `BASE` or `PARTNER` is a workflow recommendation, not
automatic-use authority.

No file in this directory changes `seed-resolver`, Media Atlas eligibility, seed
bindings, or TP02 runtime behavior.
