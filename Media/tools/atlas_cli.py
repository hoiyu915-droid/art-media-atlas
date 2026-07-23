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


def read_profile(mid: str) -> dict | None:
    path = ROOT / "profiles" / f"{mid}.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def cmd_list(_: argparse.Namespace) -> None:
    for item in MANIFEST["media"]:
        print(f'{item["id"]}  {item["name_zh"]:<12} {item["name_en"]:<28} {item["family"]:<18} {item["profile_status"]}')


def cmd_show(args: argparse.Namespace) -> None:
    mid = args.id.upper()
    if mid not in MEDIA:
        raise SystemExit(f"Unknown medium: {mid}")
    profile = read_profile(mid)
    print(json.dumps({"manifest": MEDIA[mid], "profile": profile}, ensure_ascii=False, indent=2))


def cmd_select(args: argparse.Namespace) -> None:
    weights = PURPOSES[args.purpose]
    ranked = []
    for mid, item in MEDIA.items():
        profile = read_profile(mid)
        if not profile:
            continue
        scores = profile["scores"]
        total = sum(scores[key] * weight for key, weight in weights)
        ranked.append((total, mid, item, profile))
    ranked.sort(key=lambda row: (-row[0], row[1]))
    for total, mid, item, profile in ranked[: args.limit]:
        partners = ", ".join(profile["recommended_line_partner"])
        print(f'{mid}  score={total:>2}  {item["name_zh"]} / {item["name_en"]}  partners={partners}')


def cmd_recipe(args: argparse.Namespace) -> None:
    path = ROOT / "recipes" / f"{args.name}.yaml"
    if not path.exists():
        raise SystemExit(f"Unknown recipe: {args.name}")
    print(path.read_text(encoding="utf-8"), end="")


def main() -> None:
    parser = argparse.ArgumentParser(description="Query the Media Atlas pilot")
    sub = parser.add_subparsers(required=True)
    p_list = sub.add_parser("list", help="List all 75 media")
    p_list.set_defaults(func=cmd_list)
    p_show = sub.add_parser("show", help="Show one medium and its pilot profile")
    p_show.add_argument("id")
    p_show.set_defaults(func=cmd_show)
    p_select = sub.add_parser("select", help="Rank the 12 pilot media for a purpose")
    p_select.add_argument("purpose", choices=sorted(PURPOSES))
    p_select.add_argument("--limit", type=int, default=5)
    p_select.set_defaults(func=cmd_select)
    p_recipe = sub.add_parser("recipe", help="Print a reusable recipe")
    p_recipe.add_argument("name")
    p_recipe.set_defaults(func=cmd_recipe)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
