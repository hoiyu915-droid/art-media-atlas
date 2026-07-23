from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
MEDIA = {item["id"]: item for item in MANIFEST["media"]}

PURPOSES = {
    "clinical_soft": (("portrait_fit", 2), ("scene_fit", 1), ("medical_label_legibility", 1)),
    "anatomy": (("anatomy_fit", 2), ("medical_label_legibility", 1), ("line_precision", 1)),
    "portrait": (("portrait_fit", 2), ("scene_fit", 1)),
    "public_health": (("public_health_fit", 2), ("medical_label_legibility", 1)),
    "archive": (("archive_fit", 2), ("portrait_fit", 1)),
    "digital": (("digital_fit", 2), ("medical_label_legibility", 1)),
}


def cmd_list(_: argparse.Namespace) -> None:
    for item in MANIFEST["media"]:
        resolver = item["resolver"]
        eligibility = "auto" if resolver["automatic_use_allowed"] else "review"
        print(
            f'{item["id"]}  {item["name_zh"]:<12} {item["name_en"]:<28} '
            f'{item["family"]:<18} {eligibility}'
        )


def cmd_show(args: argparse.Namespace) -> None:
    mid = args.id.upper()
    if mid not in MEDIA:
        raise SystemExit(f"Unknown medium: {mid}")
    print(json.dumps(MEDIA[mid], ensure_ascii=False, indent=2))


def cmd_select(args: argparse.Namespace) -> None:
    weights = PURPOSES[args.purpose]
    ranked = []
    for mid, item in MEDIA.items():
        if not args.include_review and not item["resolver"]["automatic_use_allowed"]:
            continue
        scores = item["capabilities"]
        total = sum(scores[key] * weight for key, weight in weights)
        ranked.append((total, mid, item))
    ranked.sort(key=lambda row: (-row[0], row[1]))
    for total, mid, item in ranked[: args.limit]:
        partners = ", ".join(partner["id"] for partner in item["compatible_partners"]) or "-"
        basis = item["resolver"]["assessment_basis"]
        print(
            f'{mid}  score={total:>2}  {item["name_zh"]} / {item["name_en"]}  '
            f'partners={partners}  basis={basis}'
        )


def cmd_recipe(args: argparse.Namespace) -> None:
    path = ROOT / "recipes" / f"{args.name}.yaml"
    if not path.exists():
        raise SystemExit(f"Unknown recipe: {args.name}")
    print(path.read_text(encoding="utf-8"), end="")


def main() -> None:
    parser = argparse.ArgumentParser(description="Query the resolver-ready Media Atlas")
    sub = parser.add_subparsers(required=True)
    p_list = sub.add_parser("list", help="List all 75 media")
    p_list.set_defaults(func=cmd_list)
    p_show = sub.add_parser("show", help="Show one resolver-ready medium record")
    p_show.add_argument("id")
    p_show.set_defaults(func=cmd_show)
    p_select = sub.add_parser("select", help="Rank media for a purpose")
    p_select.add_argument("purpose", choices=sorted(PURPOSES))
    p_select.add_argument("--limit", type=int, default=5)
    p_select.add_argument(
        "--include-review",
        action="store_true",
        help="Include low-confidence family defaults that require manual review",
    )
    p_select.set_defaults(func=cmd_select)
    p_recipe = sub.add_parser("recipe", help="Print a reusable recipe")
    p_recipe.add_argument("name")
    p_recipe.set_defaults(func=cmd_recipe)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
