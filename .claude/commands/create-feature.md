---
description: Interactively create a feature request issue
argument-hint: [short description]
allowed-tools: Bash(gh issue create:*)
---

Create a feature request GitHub issue. Initial description from the user (may be empty): $ARGUMENTS

1. Ask the user for anything missing, following the feature request template in `.github/ISSUE_TEMPLATE/feature_request.md`:
   - Location (page or section affected)
   - Description (what feature or improvement)
   - Why (what problem it solves)
   - Additional instructions (optional)
   - Type: `enhancement` (default), `content` (text/page changes only), or `documentation`
   - Priority: high, medium, or low (optional)
   - Source: `website-feedback`, `complaint`, or none (optional)
   - Assign to me? (default yes)
2. Show the proposed title (prefixed `[FEATURE] `), body, and labels, and confirm before creating.
3. Create it with `gh issue create --title "..." --body "..."` plus the labels, and `--assignee "@me"` if requested.
4. Reply with the issue number and URL.
