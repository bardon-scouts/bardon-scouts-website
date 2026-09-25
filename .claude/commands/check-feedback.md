---
description: Find my issues where someone has commented since Claude last acted, and address the feedback
allowed-tools: Bash(gh issue list:*), Bash(gh issue view:*), Bash(gh issue edit:*), Bash(gh issue comment:*)
---

1. Run the feedback check:

   ```
   gh issue list --assignee "@me" --state open --json number,title,labels,comments --jq '.[] | select((.comments | length) > 0 and ((.comments[-1].body | contains("<!-- claude-code -->")) | not)) | "#\(.number) \(.title) | last comment: \(.comments[-1].createdAt)"'
   ```

2. If nothing is returned, say there is no new feedback and stop.
3. For each issue returned, run `gh issue view <number> --comments` and read every comment posted after the newest `<!-- claude-code -->` comment. That is the feedback.
4. List the issues with a short summary of each piece of feedback, and say what you plan to change for each.
5. Unless the user has asked you to go ahead, **stop here** and ask which to work on. When told to proceed, follow the "addressing feedback" rule in `.claude/instructions.md`:
   - `gh issue edit <number> --add-label "changes-requested" --remove-label "ready-for-review"`
   - Comment (with the `<!-- claude-code -->` footer) acknowledging the feedback and what will change. If the feedback is unclear, ask in that comment and stop.
   - Rework, verify on the dev site, then resubmit with `/submit-for-review <number>`.
