---
description: List my assigned open GitHub issues
allowed-tools: Bash(gh issue list:*)
---

Run:

```
gh issue list --assignee "@me" --state open --json number,title,labels,updatedAt
```

Show the results as a short table sorted by priority (`priority-high`, `priority-medium`, `priority-low`, then unlabelled). Include number, title, status label (`in-progress`, `blocked`, `needs-review`, `ready`) and priority. If there are no issues, say so.

Do not start work on any issue. Just list them.
