---
description: List issues that are verified on dev and waiting for the owner to review and close
allowed-tools: Bash(gh issue list:*)
---

Run:

```
gh issue list --state open --label ready-for-review --json number,title,assignees,comments,url
```

For each issue, show:
- the number and title, with its GitHub URL
- who it's assigned to
- from the latest comment containing `<!-- claude-code -->` (the review comment): the commit hash, the dev site links, and anything it asks the reviewer to check themselves

Flag any issue whose newest comment has **no** `<!-- claude-code -->` marker as "you've already commented, waiting for Claude to rework".

Finish with a reminder: close an issue if it's acceptable, or comment on it with what needs to change. Claude will pick up the comment next time it checks for feedback.

If the queue is empty, say so. Do not change any issues.
