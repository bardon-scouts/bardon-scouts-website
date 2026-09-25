# Claude Instructions for Bardon Scouts Website

## Project Context

This is a collaborative project between two Bardon Scout Leaders who are both using Claude Code:
- You (current user)
- Hamish (fellow Scout Leader)

These instructions are shared via Git, so any changes here will be synchronized between collaborators.

## Git Commit Message Format

**IMPORTANT: DO NOT include attribution in commit messages.**

When creating git commits:
- ❌ DO NOT include "🤖 Generated with [Claude Code]" lines
- ❌ DO NOT include "Co-Authored-By: Claude <noreply@anthropic.com>" lines
- ✅ DO use clear, descriptive commit messages
- ✅ DO use standard git commit format (short summary, blank line, detailed description if needed)

### Example of CORRECT commit format:

```
Add Code of Conduct and Phone Use Policy pages

Created two new policy pages under About section:
- Code of Conduct with sections for parents and scouts
- Phone Use Policy explaining no-phone rules during meetings

Both pages added to navigation menu and Sveltia CMS.
```

### Example of INCORRECT commit format (DO NOT USE):

```
Add Code of Conduct and Phone Use Policy pages

Created two new policy pages under About section.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

## Website-Specific Guidelines

### Content Standards

1. **Section Terminology** - Use these short names consistently:
   - Joey Scouts → **Joeys** (unless specifically referring to "Joey Scouts" as the formal section name)
   - Cub Scouts → **Cubs** (never "Cub Scouts")
   - Scouts → **Scouts** (correct as-is)
   - Venturers → **Venturers** (correct as-is)

   **Examples:**
   - ✅ "Cubs participate in..."
   - ✅ "Joey Scouts and Cubs attend..."
   - ❌ "Cub Scouts participate in..."

2. **No Age Ranges on Event Pages** - Event pages should NOT include age ranges (e.g., "6-8 years", "Cub Scouts (8-11)"). Use section names only (e.g., "Joey Scouts", "Cubs").

3. **No Redundant Headings** - Avoid repeating the page title in the first ## heading. Let the page title serve as the H1, and start content immediately or with a different heading.

4. **Event Images** - Use `scouts_logo.jpg` as placeholder for event images when creating new event pages.

5. **No Em Dashes** - NEVER use em dashes (—) in content. Always use regular hyphens (-) instead. Em dashes are not appropriate for this website's style.

6. **Security & Privacy - Financial Information** - NEVER include the following on the website to protect against fraud and scams:
   - Payment methods or bank account details
   - Invoice due dates or billing months/schedule
   - Specific payment deadlines
   - Bank transfer instructions
   - Payment portal URLs (except Consent2go for events)

   **Rationale:** Preventing fraudulent emails that impersonate Bardon Scouts by timing scam emails to coincide with actual invoicing periods. Financial details are communicated privately via invoice only.

   **What IS allowed:**
   - General fee amounts (e.g., "$344 per six months")
   - General statement that invoices will be sent
   - Instruction to check for invoices
   - Reference to "payment details on invoice"

### Hugo & Sveltia CMS

- This is a Hugo Extended v0.148.2 static site
- Content managed through Sveltia CMS (successor to Netlify CMS)
- When adding new pages, remember to add them to both:
  - Navigation menu (`config/_default/menus.toml`)
  - CMS configuration (`static/admin/config.yml`)

### Development Workflow

- Work on the `dev` branch
- Hugo server runs with: `hugo server --buildFuture --buildDrafts --disableFastRender --port 1314`
- Auto-commit and push changes after completing tasks

## GitHub Issues Workflow

GitHub Issues is the task list for this project. Both collaborators use Claude Code independently, so the workflow is assignment-based to avoid conflicts. Use the GitHub CLI (`gh`) for all issue operations - do not set up or use GitHub MCP servers.

`@me` always resolves to whoever is authenticated with `gh` on the current machine, so the same rules work for both collaborators.

### Issue lifecycle

```
new/ready -> in-progress -> ready-for-review -> (owner closes)            = done
                                             -> (owner comments)
                                                  -> changes-requested -> in-progress -> ready-for-review ...
```

**Claude never closes issues.** Claude takes an issue as far as `ready-for-review`. The owner reviews it and either closes it (accepted) or comments with what needs to change.

### Marking Claude's comments

Claude posts to GitHub through the owner's account, so the comment author can't tell a person's comment from Claude's. **Every comment Claude posts must end with this footer**, exactly:

```

---
*Posted by Claude Code* <!-- claude-code -->
```

This applies to all comments, including "Starting work", progress notes, review requests and comments added with `gh issue reopen --comment` or `gh issue create --body`. For multi-line comments, write the body to a file in the scratchpad and use `--body-file`.

Short one-line comments can use the inline form instead, keeping the command on one line:

```
gh issue comment <number> --body "Starting work - *Posted by Claude Code* <!-- claude-code -->"
```

Detection relies only on the `<!-- claude-code -->` marker, so never leave it out and never paraphrase it.

**Detecting feedback:** if the newest comment on an open issue does **not** contain `<!-- claude-code -->`, a person has commented since Claude last acted, and that comment must be treated as feedback to act on. Issues with no comments at all are new work, not feedback.

### Rules

1. **Only work on issues assigned to `@me`.** Never start or edit an issue assigned to someone else. If an unassigned issue is requested, assign it to `@me` first. If it is assigned to someone else, stop and ask the user.
2. **Check for feedback first.** Before starting any new issue, run the feedback check (see Command Reference). Issues with unanswered feedback come before new work.
3. **When starting work** on an issue:
   - Assign to self: `gh issue edit <number> --add-assignee "@me"`
   - Add the in-progress label: `gh issue edit <number> --add-label "in-progress" --remove-label "ready"`
   - Comment "Starting work" (with the footer)
4. **When addressing feedback** on an issue:
   - `gh issue edit <number> --add-label "changes-requested" --remove-label "ready-for-review"`, then add `in-progress` when you begin
   - Comment (with the footer) acknowledging the feedback in your own words and saying what you will change. If the feedback is unclear, ask in the comment and stop. Don't guess.
   - Do the rework, then follow rules 7 and 8 as normal. Remove `changes-requested` when resubmitting.
5. **During work**, add a short progress comment (with the footer) at meaningful milestones (e.g. approach decided, main change done, blocked on a question).
6. **If blocked**, add the `blocked` label, remove `in-progress`, and comment (with the footer) explaining what is needed.
7. **Verify the fix actually worked.** An issue is not ready for review until the result has been confirmed and tested, and your own working has been double-checked:
   - **Re-check after committing.** Re-run the checks against the committed files, not your memory of the edits. For example, if the issue is to remove every em dash, search the whole site again after the commit and confirm zero remain. If the issue lists items (a checklist, a count, file and line numbers), confirm every one and state the final count in the review comment.
   - **Test on the deployed `dev` site, not locally.** Once Netlify has finished deploying the commit to the `dev` branch deploy, confirm the deploy succeeded and check the change on the live `dev` site (e.g. with curl or WebFetch). Do not build or run the site locally to verify. A local build doesn't count as verification. Every change must be checked on the deployed `dev` site, including content-only changes.
   - **Double-check your working.** Look for places the first pass could have missed: other files, `data/`, `layouts/`, other spellings or forms of the same thing. Re-check any numbers you report.
   - **If you can't verify** (for example the `dev` deploy failed), don't submit for review. Mark the issue `blocked` (rule 6) instead.
8. **Submit for review** once verified:
   - Commit with the issue number in the summary line, e.g. `Update Cubs meeting time (#12)`, and push to `dev` (this happens before verification, of course)
   - `gh issue edit <number> --add-label "ready-for-review" --remove-label "in-progress" --remove-label "changes-requested"`
   - Post a review comment (with the footer) containing: the commit hash(es), what changed, how it was verified on the dev site with results, links to the affected dev pages, and anything the reviewer should look at themselves (e.g. visual layout Claude can't judge).
   - **Do not close the issue.**
9. **When discovering bugs or unrelated problems** while working, do not fix them silently. Create a new issue with the `discovered` label plus a type label, and assign it to `@me`:
   `gh issue create --title "..." --body-file <file> --label bug --label discovered --assignee "@me"` (body ends with the footer)

### Checking the dev deploy

- **Dev site:** https://dev--bardon-scouts-website.netlify.app/ (Netlify branch deploy of `dev`, rebuilt on every push)
- **Production:** https://bardonscouts.org.au/ (deployed from `master`)

Netlify does not post build statuses to GitHub for this repo. Use the Netlify CLI and the deploy stamp instead.

**Netlify CLI** (must be logged in to the Bardon Scouts Netlify account, team `bardon-scouts`; check with `netlify status`. The repo folder is linked with `netlify link --name bardon-scouts-website`, site ID `5134019f-f869-4cf3-91f3-a36e2acd8055`):

- Deploy state per commit: `netlify api listSiteDeploys --data '{"site_id":"5134019f-f869-4cf3-91f3-a36e2acd8055","per_page":5}'`. Each deploy has `branch`, `commit_ref`, `state` (`ready` = success, `error` = failed, `building`/`enqueued` = in progress) and `error_message`.

**Deploy stamp:** every page has `<meta name="deploy-commit" content="<full commit hash>">`, set from Netlify's `COMMIT_REF`. The HTML is minified, so the quotes around attribute values may be dropped. Search with a pattern that allows for that.

1. Get the full hash of the pushed commit: `git rev-parse HEAD`
2. Check the deploy state for that commit with `netlify api listSiteDeploys` (above). If it's `error`, read `error_message`, mark the issue `blocked`, and fix the build before anything else.
3. Once it's `ready`, confirm the dev site is serving it: `curl -s https://dev--bardon-scouts-website.netlify.app/ | grep -oE 'deploy-commit content="?[0-9a-f]{40}'` should show the same hash.
4. Only once the hash matches, check the actual change on the dev site (curl or WebFetch the affected pages).

### Command Reference

| Action | Command |
|---|---|
| Check my tasks | `gh issue list --assignee "@me" --state open` |
| Check for feedback | see the command below the table |
| Ready for review | `gh issue list --state open --label ready-for-review` |
| View an issue | `gh issue view <number> --comments` |
| Create issue | `gh issue create --title "..." --body-file <file> --label bug --assignee "@me"` |
| Update issue | `gh issue edit <number> --add-label "in-progress"` |
| Add comment | `gh issue comment <number> --body-file <file>` (body ends with the footer) |

**Feedback check.** This lists open issues assigned to me whose newest comment wasn't posted by Claude:

```sh
gh issue list --assignee "@me" --state open --json number,title,labels,comments --jq '.[] | select((.comments | length) > 0 and ((.comments[-1].body | contains("<!-- claude-code -->")) | not)) | "#\(.number) \(.title) | last comment: \(.comments[-1].createdAt)"'
```

### Slash Commands

Defined in `.claude/commands/`:

- `/my-tasks` - List my open issues, with feedback to address shown first
- `/review-queue` - List issues ready for the owner to review and close
- `/check-feedback` - Find issues where someone has commented since Claude last acted, and address them
- `/create-bug` - Interactively create a bug issue
- `/create-feature` - Interactively create a feature request
- `/start-issue <number>` - Assign to me, add in-progress label, comment "Starting work"
- `/submit-for-review <number>` - Commit, push, verify on dev, then label `ready-for-review` with a review comment (never closes)

### Labels

- **Status:** `ready`, `in-progress`, `blocked`, `ready-for-review` (verified on dev, waiting for the owner), `changes-requested` (owner commented, needs rework)
- **Type:** `bug`, `enhancement`, `content`, `documentation`
- **Priority:** `priority-high`, `priority-medium`, `priority-low`
- **Source:** `website-feedback`, `complaint`, `discovered`

When working through "my assigned issues": first address any issues with feedback (see rule 2), then take the rest in priority order (high, medium, low, then unlabelled). Skip anything labelled `blocked` or `ready-for-review`, which is waiting on a person.

## Additional Notes

If you have questions or need clarification on these instructions, ask the user before proceeding.
