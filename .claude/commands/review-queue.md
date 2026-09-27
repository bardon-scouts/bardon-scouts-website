---
description: List issues labelled needs-review (waiting on the owner to review, answer or close)
allowed-tools: Bash(gh issue list:*), Bash(gh issue view:*)
---

Run:

```
gh issue list --state open --label needs-review --json number,title,labels,assignees,url
```

For each issue, show:
- the number and title, with its GitHub URL
- who it's assigned to
- whether it's **blocked** (also labelled `blocked`: Claude needs an answer) or **ready to review** (work done and verified on dev)
- from the most recent comment (`gh issue view <number> --comments`): the commit hash, the dev site links, and anything it asks the reviewer to check or answer

Finish with a reminder:
- **Acceptable:** close the issue.
- **Not acceptable, or answering a question:** comment on the issue, then remove the `needs-review` label. That hands it back to Claude.

If the queue is empty, say so. Do not change any issues.
