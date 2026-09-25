---
description: Commit, push, verify, and close a GitHub issue as completed
argument-hint: <issue-number>
allowed-tools: Bash(gh issue view:*), Bash(gh issue edit:*), Bash(gh issue close:*), Bash(gh issue comment:*), Bash(gh api:*), Bash(git status), Bash(git diff:*), Bash(git add:*), Bash(git commit:*), Bash(git push), Bash(git log:*), Bash(git rev-parse:*), Read, Grep, Glob, WebFetch
---

Complete issue #$ARGUMENTS, following the verification rules in `.claude/instructions.md`.

1. Run `gh issue view $ARGUMENTS --json number,title,body,state,assignees,comments` and confirm it is open and assigned to me. If not, stop and ask the user. Note every item, checklist entry, count and "how to verify" step in the issue.
2. Check `git status`. If there are uncommitted changes for this issue, commit them with the issue number in the summary line (e.g. `Fix broken calendar link (#$ARGUMENTS)`), following the commit format in `.claude/instructions.md` (no attribution lines). Only stage files related to this issue.
3. Push to `dev` with `git push`, and get the short hash of the commit(s) for this issue (`git log --oneline`).
4. **Verify the fix** against the committed files:
   - Re-run every check the issue needs (searches, counts, checklist items) and confirm each one passes. Do not rely on memory of the edits.
   - Double-check for anything missed: other files, `data/`, `layouts/`, other spellings or forms.
   - Once Netlify has deployed the commit to the `dev` branch deploy, confirm the deploy succeeded and check the change on the deployed `dev` site (e.g. with WebFetch). Do not build or run the site locally. Only the deployed `dev` site counts.
5. **If everything is verified**, close the issue:
   - `gh issue edit $ARGUMENTS --remove-label "in-progress"`
   - `gh issue close $ARGUMENTS --comment "Completed in commit <hash>. Verified by: <what was checked and the results>" --reason completed`

   If there was more than one commit, list all hashes, and add a one or two line summary of what changed.
6. **If anything could not be verified or failed**, do not close. Run `gh issue edit $ARGUMENTS --remove-label "in-progress" --add-label "needs-review"` and comment with what was done, what is still unverified, and why.
7. Reply with the commit hash(es), what was verified, and whether the issue was closed or left for review.
