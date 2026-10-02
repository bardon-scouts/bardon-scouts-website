# Bardon Scouts website

The Bardon Scout Group website: a Hugo static site with Sveltia CMS, hosted on Netlify. It's maintained by Bardon Scout Leaders, each using Claude Code, with GitHub Issues as the shared task list.

## Where the rules live

- **How we work** (GitHub Issues workflow, testing before review, writing style, commit rules, permissions) comes from the **lvlup-workflow plugin**, loaded at the start of every session. Don't repeat it here.
- **What this project cares about** is in **`docs/`**: `docs/principles.md` is loaded every session; `docs/requirements/` covers content standards, event pages, news posts, pages and navigation, sections and the home page. Read the relevant requirement before changing an area, and update it when a change alters what it describes.
- **How the site is built and why** (stack, content model, templates, decisions log) is in **`docs/design/README.md`**. Update it when a change alters what it describes.
- **How to verify a change** is the **`verify` skill** (`.claude/skills/verify/SKILL.md`): confirm the Netlify dev deploy of the commit, then check the pages on the dev site. **`docs/testing/README.md`** covers the test approach, the test case IDs in the requirements, the whole-site check (`scripts/site_check.py`) and what a person checks.

## Branches and environments

| Branch | Deployed to | Use |
|---|---|---|
| `dev` | https://dev--bardon-scouts-website.netlify.app/ | All work. Every push deploys here. |
| `master` | https://bardonscouts.org.au/ | Production. Publish by merging `dev` into `master`. |

- **Sveltia CMS saves to `master`** (`static/admin/config.yml`, editorial workflow: draft, review, ready). Leaders' CMS edits go to production without passing through `dev`, so `master` can have content changes that `dev` doesn't. Pull `master` into `dev` before large content changes to avoid conflicts.
- Netlify builds with `hugo --gc --minify` on **Hugo 0.128.2** (`netlify.toml`). Don't use Hugo features newer than that.
- Verify on the dev site, never with a local build. Netlify site: `bardon-scouts-website` (team `bardon-scouts`).

## Structure

```
content/            Pages (Markdown). Event pages are content/<slug>.md
  events/_index.md  The Events listing page
  sections/         Joeys, Cubs, Scouts, Venturers, Rovers (coming soon)
  join/ leaders/ skills/ news/ contact/ complaints/ website-feedback/
data/
  sections.yaml     Single source for section details (meeting times, ages, ...)
  features.yaml     Home page features
layouts/            Custom templates (no theme). index.html is the home page
  partials/         navbar, footer, hero, features, sections-list, events-list, forms
assets/scss/        Styles, compiled by Hugo Pipes (main.scss imports the rest)
assets/js/main.js   Navbar menu toggle
config/_default/    config.toml, params.toml (contact details, colours), menus.toml
static/admin/       Sveltia CMS (config.yml defines what leaders can edit)
static/img/         Images, referenced as /img/<name>
static/_redirects   Netlify redirects from the old Gatsby URLs
scripts/site_check.py  Whole-site check, run before publishing dev to master
```

## Notes

- **Styling:** Bulma 1.0.2 from a CDN (`layouts/partials/head.html`), plus custom SCSS. Brand colours are teal `#43a09b` and red `#d9432d`, in `assets/scss/_variables.scss`.
- **Forms** (contact, feedback, complaints) are Netlify forms (`data-netlify="true"`).
- **Deploy stamp:** every page has `<meta name="deploy-commit">` with the commit it was built from (`layouts/partials/head.html`, from Netlify's `COMMIT_REF`). The `verify` skill relies on it.
- The site was converted from Gatsby in July 2026. `CONVERSION-SUMMARY.md` has the history.
