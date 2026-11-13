Review how the index is displayed on its web home, https://ai.danielrosehill.com/claude-code, and whether the categories are well organised.

The site itself lives in the monorepo `danielrosehill/danielrosehilldotcom` (`site-ai/`, loader
`shared/data/claude-index.ts`); this repo only supplies `data/tagged_repos.json` and `data/categories.json`.
claude.danielrosehill.com was retired on 2026-11-13 and only redirects.

## Steps

1. **Rebuild the data**: `npm run build`.
2. **Check `data/tagged_repos.json`**: count repos per category and per tag; flag missing or generic descriptions
   and repos with only the fallback tag.
3. **Review `data/categories.json`**: does the group/category hierarchy still make sense, does every category file
   have an entry, should anything be regrouped?
4. **Check `data/tag_rules.json` coverage**: suggest keyword rules for poorly tagged repos.
5. **Check the live site**: the listing at https://ai.danielrosehill.com/claude-code (all three views: Newest, A–Z,
   By category) and 3–5 recent `https://ai.danielrosehill.com/claude-code/<slug>/` pages. If the live data is
   behind this repo, run Step 9 of `sync-index`.
6. Report findings and fix what belongs to this repo; for display problems, fix them in the monorepo.
