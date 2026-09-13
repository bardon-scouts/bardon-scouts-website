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

1. **No Age Ranges on Event Pages** - Event pages should NOT include age ranges (e.g., "6-8 years", "Cub Scouts (8-11)"). Use section names only (e.g., "Joey Scouts", "Cub Scouts").

2. **No Redundant Headings** - Avoid repeating the page title in the first ## heading. Let the page title serve as the H1, and start content immediately or with a different heading.

3. **Event Images** - Use `scouts_logo.jpg` as placeholder for event images when creating new event pages.

4. **No Em Dashes** - NEVER use em dashes (—) in content. Always use regular hyphens (-) instead. Em dashes are not appropriate for this website's style.

5. **Security & Privacy - Financial Information** - NEVER include the following on the website to protect against fraud and scams:
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

## Additional Notes

If you have questions or need clarification on these instructions, ask the user before proceeding.
