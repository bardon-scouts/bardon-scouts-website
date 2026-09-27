---
description: List my open GitHub issues - returned from review first, then Claude's work, then what's waiting on me
allowed-tools: Bash(gh issue list:*), Bash(gh api:*)
---

1. Run:

   ```
   gh issue list --assignee "@me" --state open --json number,title,labels,updatedAt
   ```

2. For each issue **without** the `needs-review` label, check whether it has been through review before:

   ```
   gh api repos/bardon-scouts/bardon-scouts-website/issues/<number>/timeline --paginate --jq '.[] | select(.event == "labeled" and .label.name == "needs-review") | .created_at'
   ```

   Any output means it was returned from review.

3. Group the results into these sections, in this order, and leave out any empty section:
   1. **Returned from review** - no `needs-review` now, but has had it before. Feedback is waiting.
   2. **In progress** - labelled `in-progress`.
   3. **To do** - everything else without `needs-review`, sorted by priority (`priority-high`, `priority-medium`, `priority-low`, then unlabelled).
   4. **Waiting on you** - labelled `needs-review` (add "blocked" if it's also labelled `blocked`).

   For each issue show the number, title and priority. If there are no open issues, say so.

Do not start work on any issue. Just list them.
