Run the complete index maintenance pipeline: update charts, review README, sync data, review frontend, then push.

## Phase 1: Update Charts

1. Run tracking script to update repo count history and regenerate the chart:
   ```bash
   python3 scripts/update_repo_tracking.py
   ```
2. Verify chart was updated and count is accurate.

## Phase 2: Review README Organization

1. Check alphabetical ordering within each category file in `categories/`. Fix any out-of-order entries.
2. Check for duplicate repos across all category files. Remove duplicates.
3. Review descriptions for consistency (1-2 sentences, clear, professional).
4. Verify every entry has the correct format: `### Name`, badge, description, `---`.
5. Flag overstuffed (>15) or underpopulated (<2) categories.

## Phase 3: Rebuild and Sync Data

1. Run the full build pipeline:
   ```bash
   npm run build
   ```
2. Cross-check that repo counts match across: category files, `data/repos.json`, `data/tagged_repos.json`, and `data/site_state.json`.
3. Verify every repo appears in `data/tagged_repos.json` with valid tags and categories.
4. Spot-check that new repos have pages at https://ai.danielrosehill.com/claude-code/<slug>/ (after the AI site refresh).

## Phase 4: Review Frontend Quality

1. Check `data/tagged_repos.json` for:
   - Repos with missing/generic descriptions
   - Repos with only fallback tags
   - Correct category assignments
2. Review `data/tag_rules.json` — suggest new rules if repos are poorly tagged.
3. Check `data/site_state.json` history for recent changes.

## Phase 5: Commit and Push

1. Stage all changed files:
   ```bash
   git add categories/ data/ charts/ README.md newest.md
   ```
2. Commit with a descriptive message summarizing what was fixed/updated.
3. Push to remote:
   ```bash
   git push
   ```

Report a summary of everything that was checked and any issues found/fixed.
