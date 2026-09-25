---
description: Commit, push, verify on dev, and submit a GitHub issue for the owner's review (never closes)
argument-hint: <issue-number>
allowed-tools: Bash(gh issue view:*), Bash(gh issue edit:*), Bash(gh issue comment:*), Bash(gh api:*), Bash(git status), Bash(git diff:*), Bash(git add:*), Bash(git commit:*), Bash(git push), Bash(git log:*), Bash(git rev-parse:*), Bash(netlify api:*), Bash(curl:*), Read, Grep, Glob, Write, WebFetch
---

Submit issue #$ARGUMENTS for review, following the rules in `.claude/instructions.md`.

1. Run `gh issue view $ARGUMENTS --json number,title,body,state,assignees,labels,comments` and confirm it is open and assigned to me. If not, stop and ask the user. Note every item, checklist entry, count and "how to verify" step in the issue, and any reviewer feedback in the comments that this round must address.
2. Check `git status`. If there are uncommitted changes for this issue, commit them with the issue number in the summary line (e.g. `Fix broken calendar link (#$ARGUMENTS)`), following the commit format in `.claude/instructions.md` (no attribution lines, message via `git commit -F <file>`). Only stage files related to this issue.
3. Push to `dev` with `git push`, and get the full hash with `git rev-parse HEAD`.
4. **Verify the fix:**
   - Re-run every check the issue needs (searches, counts, checklist items) against the committed files and confirm each one passes. Do not rely on memory of the edits.
   - Double-check for anything missed: other files, `data/`, `layouts/`, other spellings or forms.
   - Confirm the Netlify `dev` deploy for the commit is `ready` and the dev site's `deploy-commit` stamp matches (see "Checking the dev deploy" in `.claude/instructions.md`). Then check the change on the deployed dev site. Never verify with a local build.
   - If feedback was given, confirm each point of it has been addressed.
5. **If everything is verified**, submit for review:
   - `gh issue edit $ARGUMENTS --add-label "ready-for-review" --remove-label "in-progress" --remove-label "changes-requested"`
   - Write the review comment to a scratchpad file and post it with `gh issue comment $ARGUMENTS --body-file <file>`. Include: commit hash(es), what changed, how it was verified with results, links to the affected pages on https://dev--bardon-scouts-website.netlify.app/, how each feedback point was addressed (if any), and anything the reviewer should check themselves. End with the footer:

     ```

     ---
     *Posted by Claude Code* <!-- claude-code -->
     ```
   - **Do not close the issue.** The owner closes it after reviewing.
6. **If anything could not be verified or failed**, do not submit. Mark it `blocked` (remove `in-progress`) and comment (with the footer) with what was done, what is unverified, and why.
7. Reply with the commit hash(es), what was verified, the dev links, and whether the issue is now `ready-for-review` or `blocked`.
