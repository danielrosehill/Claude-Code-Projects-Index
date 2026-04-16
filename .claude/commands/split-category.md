Add a category file to `data/split_pages.json` so it renders as a standalone page with a teaser in the README.

## When to split a category

Consider splitting when a category exceeds ~100 README lines or ~12 repos — at that point, the README becomes tedious to scroll and the table of contents loses its value. Typical candidates: `10-misc.md`, `03-research.md`, `08-plugins.md`, `01-systems-administration.md`.

Don't split tiny categories (<6 repos) — the indirection costs more than it saves.

## Steps

1. **Confirm the target category**. If the user didn't name one, list current category files with their repo counts (`wc -l categories/*.md`) and ask which one.

2. **Pick an output filename**. The convention is the category topic in lowercase, e.g. `misc.md`, `research.md`, `plugins.md`, `systems-admin.md`. Ask the user if the derived name isn't obvious.

3. **Edit `data/split_pages.json`**. Add an entry under `splits`:
   ```json
   {
     "category_file": "NN-your-category.md",
     "output": "your-output.md"
   }
   ```
   If the file already has the entry, tell the user and stop.

4. **Rebuild the site**:
   ```bash
   npm run build
   ```
   This emits `<output>.md` at the repo root and replaces the category's full section in the README with a teaser (title + image + intro paragraph + "see dedicated page" link).

5. **Verify** the standalone page renders and the README teaser reads naturally. If the category file has no intro paragraph before the first `###`, the teaser will be thin — suggest the user add a one-sentence intro to the category file.

6. **Commit** with a message like `Split <category> into dedicated page`.

## How the split system works

- `scripts/build_site.py` reads `data/split_pages.json` at the start of each build.
- For each listed category, it writes the full content to `<output>.md` at the repo root (with a "GENERATED" banner).
- In the concatenated README, the category's section is replaced with everything up to the first `###` entry, plus a link to the standalone page.
- The category file in `categories/` stays the single source of truth — both outputs regenerate on every build.

## Reversing a split

Remove the entry from `data/split_pages.json`, delete the standalone `<output>.md` at repo root, and rebuild. The README will go back to including the full category inline.

## Plugins are a special case

`categories/08-plugins.md` is regenerated on every build from `data/marketplace.json` (which is synced live from the Claude-Code-Plugins marketplace repo by `scripts/sync_marketplace.py`). Don't hand-edit that file. If the user wants to adjust plugin grouping, edit `data/plugin_group_map.json` instead.
