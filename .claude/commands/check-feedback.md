---
description: Find my issues returned from review and summarise the feedback on each
allowed-tools: Bash(gh issue list:*), Bash(gh issue view:*), Bash(gh api:*)
---

1. List Claude's queue (open, assigned to me, without `needs-review`):

   ```
   gh issue list --assignee "@me" --state open --search "-label:needs-review" --json number,title
   ```

2. For each issue, find when `needs-review` was last added:

   ```
   gh api repos/bardon-scouts/bardon-scouts-website/issues/<number>/timeline --paginate --jq '.[] | select(.event == "labeled" and .label.name == "needs-review") | .created_at'
   ```

   No output means it has never been reviewed. Skip it, because it's new work, not feedback. Otherwise the **last** line is when it was last handed over.

3. For each returned issue, run `gh issue view <number> --comments` and read every comment posted **after** that time. That is the feedback.
4. List the returned issues with a short summary of the feedback on each and what you plan to change. If there are none, say there is no feedback waiting.
5. Unless the user has asked you to go ahead, **stop here** and ask which to work on. When told to proceed, follow rule 4 ("returned from review") in `.claude/instructions.md`, then resubmit with `/submit-for-review <number>`.
