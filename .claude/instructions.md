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

### Rules

1. **Only work on issues assigned to `@me`.** Never start, edit, or close an issue assigned to someone else. If an unassigned issue is requested, assign it to `@me` first. If it is assigned to someone else, stop and ask the user.
2. **When starting work** on an issue:
   - Assign to self: `gh issue edit <number> --add-assignee "@me"`
   - Add the in-progress label: `gh issue edit <number> --add-label "in-progress" --remove-label "ready"`
   - Comment: `gh issue comment <number> --body "Starting work"`
3. **During work**, add a short progress comment at meaningful milestones (e.g. approach decided, main change done, blocked on a question).
4. **If blocked**, add the `blocked` label, remove `in-progress`, and comment explaining what is needed.
5. **When completing** an issue:
   - Commit with the issue number in the summary line, e.g. `Update Cubs meeting time (#12)`, and push to `dev`
   - **Verify before closing** (see rule 6). Never close an issue on the strength of having made the change.
   - Close with the commit reference and a summary of how it was verified: `gh issue close <number> --comment "Completed in commit <hash>. Verified by: ..." --reason completed`
   - Remove the `in-progress` label
6. **Verify the fix actually worked.** An issue is not done until the result has been confirmed and tested, and your own working has been double-checked:
   - **Re-check after committing.** Re-run the checks against the committed files, not your memory of the edits. For example, if the issue is to remove every em dash, search the whole site again after the commit and confirm zero remain. If the issue lists items (a checklist, a count, file and line numbers), confirm every one and state the final count in the closing comment.
   - **Check the build.** Once the build for the commit has finished, confirm it succeeded and the change appears correctly on the built site (local `hugo` build and/or the Netlify `dev` branch deploy). Template, layout, style or config changes must always be checked on a build.
   - **Double-check your working.** Look for places the first pass could have missed: other files, `data/`, `layouts/`, other spellings or forms of the same thing. Re-check any numbers you report.
   - **If you can't verify** (for example no build is available), do not close the issue. Add the `needs-review` label, remove `in-progress`, and comment with what was done, what still needs checking, and why.
7. **When discovering bugs or unrelated problems** while working, do not fix them silently. Create a new issue with the `discovered` label plus a type label, and assign it to `@me`:
   `gh issue create --title "..." --body "..." --label bug --label discovered --assignee "@me"`

### Command Reference

| Action | Command |
|---|---|
| Check my tasks | `gh issue list --assignee "@me" --state open` |
| View an issue | `gh issue view <number> --comments` |
| Create issue | `gh issue create --title "..." --body "..." --label bug --assignee "@me"` |
| Update issue | `gh issue edit <number> --add-label "in-progress"` |
| Add comment | `gh issue comment <number> --body "..."` |
| Close issue | `gh issue close <number> --comment "Completed in commit <hash>" --reason completed` |

### Slash Commands

Defined in `.claude/commands/`:

- `/my-tasks` - List my assigned open issues
- `/create-bug` - Interactively create a bug issue
- `/create-feature` - Interactively create a feature request
- `/start-issue <number>` - Assign to me, add in-progress label, comment "Starting work"
- `/complete-issue <number>` - Commit, push, verify the fix, then close (or mark `needs-review` if it can't be verified)

### Labels

- **Status:** `in-progress`, `blocked`, `needs-review`, `ready`
- **Type:** `bug`, `enhancement`, `content`, `documentation`
- **Priority:** `priority-high`, `priority-medium`, `priority-low`
- **Source:** `website-feedback`, `complaint`, `discovered`

When working through "my assigned issues", take them in priority order (high, medium, low, then unlabelled) and skip anything labelled `blocked`.

## Additional Notes

If you have questions or need clarification on these instructions, ask the user before proceeding.
