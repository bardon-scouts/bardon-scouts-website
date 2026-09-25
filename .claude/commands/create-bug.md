---
description: Interactively create a bug report issue
argument-hint: [short description]
allowed-tools: Bash(gh issue create:*)
---

Create a bug report GitHub issue. Initial description from the user (may be empty): $ARGUMENTS

1. Ask the user for anything missing, following the bug report template in `.github/ISSUE_TEMPLATE/bug_report.md`:
   - Location of problem (page or section of the website)
   - Description of problem (what is wrong, what was expected)
   - Additional instructions (optional)
   - Priority: high, medium, or low (optional)
   - Source: `website-feedback`, `complaint`, or none (optional)
   - Assign to me? (default yes)
2. Show the proposed title (prefixed `[BUG] `), body, and labels, and confirm before creating.
3. Create it with `gh issue create --title "..." --body "..." --label bug` plus any priority/source labels, and `--assignee "@me"` if requested.
4. Reply with the issue number and URL.
