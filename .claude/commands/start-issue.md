---
description: Start work on a GitHub issue (assign to me, mark in-progress)
argument-hint: <issue-number>
allowed-tools: Bash(gh issue view:*), Bash(gh issue edit:*), Bash(gh issue comment:*), Bash(git status), Bash(git checkout:*), Bash(git pull:*)
---

Start work on issue #$ARGUMENTS.

1. Run `gh issue view $ARGUMENTS --json number,title,body,state,assignees,labels,comments` and check it:
   - If it is closed, stop and tell the user.
   - If it is assigned to someone other than me, stop and ask the user. Never take over another collaborator's issue without confirmation.
   - If it is labelled `ready-for-review` and the newest comment has no `<!-- claude-code -->` marker, this is a rework: follow the "addressing feedback" rule in `.claude/instructions.md` instead (label `changes-requested`, and acknowledge each feedback point).
   - If it is labelled `ready-for-review` with no new feedback, stop and tell the user it is waiting for their review.
2. Make sure I'm on the `dev` branch and up to date (`git checkout dev`, `git pull`).
3. Update the issue:
   - `gh issue edit $ARGUMENTS --add-assignee "@me" --add-label "in-progress" --remove-label "ready"`
   - `gh issue comment $ARGUMENTS --body "Starting work - *Posted by Claude Code* <!-- claude-code -->"`
4. Summarise the issue for the user and outline the planned approach, then begin the work, following `.claude/instructions.md`.
