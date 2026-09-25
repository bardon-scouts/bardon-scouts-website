---
description: List my open GitHub issues, with feedback to address first
allowed-tools: Bash(gh issue list:*)
---

Run:

```
gh issue list --assignee "@me" --state open --json number,title,labels,comments,updatedAt
```

Group the results into these sections, in this order, and leave out any empty section:

1. **Feedback to address** - issues whose newest comment does **not** contain `<!-- claude-code -->`. A person has commented since Claude last acted. Show a one-line summary of that comment.
2. **In progress / changes requested** - labelled `in-progress` or `changes-requested`.
3. **Waiting for your review** - labelled `ready-for-review` (and not in section 1).
4. **Blocked** - labelled `blocked`.
5. **To do** - everything else, sorted by priority (`priority-high`, `priority-medium`, `priority-low`, then unlabelled).

For each issue show the number, title and priority. If there are no open issues, say so.

Do not start work on any issue. Just list them.
