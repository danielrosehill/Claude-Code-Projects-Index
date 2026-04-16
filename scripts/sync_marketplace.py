#!/usr/bin/env python3
"""Sync the Claude Code Plugins marketplace manifest into local data.

Fetches .claude-plugin/marketplace.json from danielrosehill/Claude-Code-Plugins
via the gh CLI and caches it at data/marketplace.json. If the fetch fails
(e.g. offline), the existing cached copy is kept.

Also regenerates categories/08-plugins.md from the manifest so the data
pipeline sees the full, authoritative plugin list on the next build.

Run: python3 scripts/sync_marketplace.py
"""

import base64
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DATA_DIR = REPO_ROOT / "data"
CATEGORIES_DIR = REPO_ROOT / "categories"
MARKETPLACE_CACHE = DATA_DIR / "marketplace.json"
GROUP_MAP_PATH = DATA_DIR / "plugin_group_map.json"
PLUGINS_CATEGORY_FILE = CATEGORIES_DIR / "08-plugins.md"

MARKETPLACE_REPO = "danielrosehill/Claude-Code-Plugins"
MANIFEST_PATH = ".claude-plugin/marketplace.json"

GENERATED_BANNER = "<!-- GENERATED FROM data/marketplace.json — do not edit by hand. Run scripts/sync_marketplace.py or npm run build. -->"


def fetch_manifest() -> dict | None:
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{MARKETPLACE_REPO}/contents/{MANIFEST_PATH}", "--jq", ".content"],
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError) as e:
        print(f"  warning: could not fetch marketplace manifest ({e})")
        return None

    try:
        decoded = base64.b64decode(result.stdout.strip()).decode("utf-8")
        return json.loads(decoded)
    except (ValueError, json.JSONDecodeError) as e:
        print(f"  warning: could not decode marketplace manifest ({e})")
        return None


def load_cached_manifest() -> dict | None:
    if MARKETPLACE_CACHE.exists():
        return json.loads(MARKETPLACE_CACHE.read_text(encoding="utf-8"))
    return None


def load_group_map() -> tuple[dict, dict]:
    """Return (group_map, name_overrides) from the config file."""
    if not GROUP_MAP_PATH.exists():
        return {}, {}
    data = json.loads(GROUP_MAP_PATH.read_text(encoding="utf-8"))
    overrides = data.pop("name_overrides", {}) or {}
    data = {k: v for k, v in data.items() if not k.startswith("_comment")}
    return data, overrides


ACRONYMS = {"ai": "AI", "mcp": "MCP", "seo": "SEO", "qa": "QA", "md": "MD", "lan": "LAN"}


def format_display_name(slug: str) -> str:
    parts = slug.replace("_", "-").split("-")
    words = [ACRONYMS.get(p.lower(), p.capitalize()) for p in parts if p]
    return " ".join(words)


def github_url_from_source(source: dict) -> str:
    repo = source.get("repo", "")
    if not repo:
        return ""
    return f"https://github.com/{repo}"


def render_plugins_markdown(manifest: dict, group_map: dict, name_overrides: dict) -> str:
    plugins = manifest.get("plugins", [])
    groups: dict[str, list[dict]] = {}
    for p in plugins:
        tags = p.get("tags") or []
        raw_group = tags[0] if tags else "other"
        group = group_map.get(raw_group, {"label": format_display_name(raw_group), "order": 999})
        key = (group["order"], group["label"])
        groups.setdefault(key, []).append(p)

    lines = [GENERATED_BANNER, "", "# Plugins", "", "![Plugins](images/plugins.png)", ""]
    lines.append(
        "All plugins registered in the [danielrosehill marketplace](https://github.com/danielrosehill/Claude-Code-Plugins). "
        "Install any of these with `/plugin install <name>@danielrosehill`."
    )
    lines.append("")

    for (_, label), group_plugins in sorted(groups.items()):
        lines.append(f"## {label}")
        lines.append("")
        for p in sorted(group_plugins, key=lambda x: x.get("name", "").lower()):
            slug = p.get("name", "")
            display = name_overrides.get(slug) or format_display_name(slug)
            url = github_url_from_source(p.get("source", {}))
            desc = p.get("description", "").strip()
            lines.append(f"### {display}")
            lines.append(
                f"[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)]({url}) "
                "![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)"
            )
            lines.append("")
            if desc:
                lines.append(desc)
                lines.append("")
            lines.append("---")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def sync() -> bool:
    DATA_DIR.mkdir(exist_ok=True)
    manifest = fetch_manifest()
    if manifest:
        MARKETPLACE_CACHE.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        print(f"  fetched {len(manifest.get('plugins', []))} plugins from {MARKETPLACE_REPO}")
    else:
        manifest = load_cached_manifest()
        if not manifest:
            print("  error: no marketplace manifest available (fetch failed and no cache)")
            return False
        print(f"  using cached manifest ({len(manifest.get('plugins', []))} plugins)")

    group_map, name_overrides = load_group_map()
    markdown = render_plugins_markdown(manifest, group_map, name_overrides)
    PLUGINS_CATEGORY_FILE.write_text(markdown, encoding="utf-8")
    print(f"  regenerated {PLUGINS_CATEGORY_FILE.relative_to(REPO_ROOT)}")
    return True


if __name__ == "__main__":
    print("Syncing marketplace manifest...")
    if not sync():
        sys.exit(1)
