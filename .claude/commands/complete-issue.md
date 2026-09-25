---
description: Commit, push, and close a GitHub issue as completed
argument-hint: <issue-number>
allowed-tools: Bash(gh issue view:*), Bash(gh issue edit:*), Bash(gh issue close:*), Bash(git status), Bash(git diff:*), Bash(git add:*), Bash(git commit:*), Bash(git push), Bash(git log:*), Bash(git rev-parse:*)
---

Complete issue #$ARGUMENTS.

1. Run `gh issue view $ARGUMENTS --json number,title,state,assignees` and confirm it is open and assigned to me. If not, stop and ask the user.
2. Check `git status`. If there are uncommitted changes for this issue, commit them with the issue number in the summary line (e.g. `Fix broken calendar link (#$ARGUMENTS)`), following the commit format in `.claude/instructions.md` (no attribution lines). Only stage files related to this issue.
3. Push to `dev` with `git push`.
4. Get the short hash of the commit(s) for this issue (`git log --oneline`).
5. Close the issue:
   - `gh issue edit $ARGUMENTS --remove-label "in-progress"`
   - `gh issue close $ARGUMENTS --comment "Completed in commit <hash>" --reason completed`

   If there was more than one commit, list all hashes, and add a one or two line summary of what changed.
6. Reply with the commit hash(es) and the closed issue URL.
