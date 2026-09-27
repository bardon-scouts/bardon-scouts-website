---
description: Start work on a GitHub issue (assign to me, mark in-progress)
argument-hint: <issue-number>
allowed-tools: Bash(gh issue view:*), Bash(gh issue edit:*), Bash(gh issue comment:*), Bash(gh api:*), Bash(git status), Bash(git checkout:*), Bash(git pull:*)
---

Start work on issue #$ARGUMENTS.

1. Run `gh issue view $ARGUMENTS --json number,title,body,state,assignees,labels,comments` and check it:
   - If it is closed, stop and tell the user.
   - If it is assigned to someone other than me, stop and ask the user. Never take over another collaborator's issue without confirmation.
   - If it is labelled `needs-review`, stop and tell the user it is waiting on them. Only they remove that label.
   - Check whether it was returned from review: `gh api repos/bardon-scouts/bardon-scouts-website/issues/$ARGUMENTS/timeline --paginate --jq '.[] | select(.event == "labeled" and .label.name == "needs-review") | .created_at'`. If there's any output, follow rule 4 ("returned from review") in `.claude/instructions.md`: the feedback is every comment after the last time shown.
2. Make sure I'm on the `dev` branch and up to date (`git checkout dev`, `git pull`).
3. Update the issue:
   - `gh issue edit $ARGUMENTS --add-assignee "@me" --add-label "in-progress" --remove-label "ready"`
   - `gh issue comment $ARGUMENTS --body "Starting work"`
4. Summarise the issue for the user and outline the planned approach, then begin the work, following `.claude/instructions.md`.
