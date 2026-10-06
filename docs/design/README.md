# Bardon Scouts website design

How the site is built and why. The requirements in `docs/requirements/` say what the site must do; this says how it does it. Keep it current: if a change alters something described here, update this file in the same commit, and add a line to the decisions log for any new decision.

## Stack

| Part | What | Where it's set |
|---|---|---|
| Site generator | Hugo 0.128.2 (extended features such as `css.Sass` are used) | `netlify.toml` |
| Styles | Bulma 1.0.2 from the jsDelivr CDN, plus custom SCSS compiled by Hugo Pipes | `layouts/partials/head.html`, `assets/scss/` |
| Script | One small script for the mobile navbar menu | `assets/js/main.js` |
| Content editing | Sveltia CMS at `/admin/`, loaded from unpkg, GitHub backend, editorial workflow (draft, review, ready) | `static/admin/index.html`, `static/admin/config.yml` |
| Hosting | Netlify site `bardon-scouts-website` (team `bardon-scouts`) | `netlify.toml` |
| Forms | Netlify Forms: contact, website feedback, complaints, hire enquiry | `layouts/partials/*-form.html` |

Netlify builds with `hugo --gc --minify` on Node 18.20.0. Branch deploys add `-b $DEPLOY_PRIME_URL` so links work on the dev site.

## Branches and environments

| Branch | Deployed to | Notes |
|---|---|---|
| `dev` | https://dev--bardon-scouts-website.netlify.app/ | All work happens here. Every push deploys. |
| `master` | https://bardonscouts.org.au/ | Production. Published by merging `dev` into `master`. |

Sveltia CMS commits to `master`, not `dev` (`backend.branch` in `static/admin/config.yml`). So leaders' CMS edits reach production without passing through `dev`, and `master` can have content that `dev` doesn't. Pull `master` into `dev` before large content changes. This is tracked as #14.

## Content model

**Pages** are Markdown files with YAML front matter in `content/`. Most pages use `type: page` and the `_default/single.html` template. Event pages are `content/<slug>.md`; the other areas have their own folders (`join/`, `leaders/`, `sections/`, `skills/`, `news/`, `contact/`, `complaints/`, `website-feedback/`, and `hire-the-den/` for its form's thanks page). A folder's `_index.md` is its landing page.

Common front matter:
- `title`, `description` (used for the page title, meta description and share preview)
- `type` (`page`, or `sections` for section page extras)
- `image` (the page's hero and share image; falls back to the Scouts logo)
- `aliases` (old URLs that redirect to this page)
- form flags such as `showForm`, `showFeedbackForm`, `showComplaintsForm`, `showHireForm`

**Data files** in `data/`:
- `sections.yaml` is the single source for each section's name, age range, meeting day and time, colour, image, description, tagline, leader title and page content. The section pages (`layouts/sections/single.html`), the Sections page and the home page "Our Units" list (`partials/sections-list.html`) all read it. Don't copy these details into pages.
- `features.yaml` holds the four home page feature blurbs (`partials/features.html`).

`content/sections/<slug>.md` adds extra content to a section page, such as the list of events that section attends.

**Menus** are in `config/_default/menus.toml` (the `main` menu, with dropdowns set by `parent`). The home page "Our Events" grid is built from the Events dropdown (`partials/events-list.html`), so adding an event to the Events menu also adds it to the home page. The footer (`partials/footer.html`) is a hand-written list and must be updated separately. Program pages (how to run a section's meeting programs, e.g. Joey Programs) are in the footer but not the menu (`docs/requirements/pages-and-navigation.md`).

**Site settings** are in `config/_default/`: `config.toml` (base URL, Markdown rendering with HTML allowed, tags and categories taxonomies, with taxonomy pages turned off), `params.toml` (description, brand colours, address, Facebook link).

**The CMS** (`static/admin/config.yml`) has a file entry for each page and data file, plus folder collections for news. Every page must have an entry so leaders can edit it (`docs/principles.md`). The `events` folder collection is unused (#13).

## Templates

There's no theme; all templates are in `layouts/`:
- `_default/baseof.html`: the page shell (head, navbar, main block, footer, script)
- `index.html`: the home page (hero, main pitch, features, events grid, sections list, contact call to action)
- `_default/single.html`: ordinary pages
- `sections/list.html` and `sections/single.html`: the Sections page and each section page
- `news/`, `events/`, `join/`, `leaders/`, `skills/` list templates for those folders' landing pages
- `404.html`
- `partials/`: `head`, `navbar`, `footer`, `hero`, `features`, `sections-list`, `events-list`, `contact-cta`, and the four forms

Brand colours are teal `#43a09b` and red `#d9432d`, in `assets/scss/_variables.scss` and `params.toml`.

### Deploy stamp

`partials/head.html` writes `<meta name="deploy-commit" content="...">` on every page, from Netlify's `COMMIT_REF` (allowed in `config.toml` under `security.funcs`). It shows which commit a page was built from, so a change can be checked on the dev site after it deploys. The `verify` skill relies on it.

### Redirects

URLs from the old Gatsby site keep working through `static/_redirects` (true 301s from Netlify): `/products/` to `/sections/`, `/contactus/` to `/contact/`, `/thanks/` to `/contact/thanks/`, and two old contact sub-pages. `/join/fairplay-voucher/` redirects to `/join/play-on-voucher/` since FairPlay vouchers were replaced by Play On! (#36). Some pages also have Hugo `aliases`.

## Decisions log

Add new decisions at the bottom: date, decision, and why. Where the reason wasn't recorded at the time, say so rather than guess.

| Date | Decision | Why |
|---|---|---|
| 19 Jul 2026 | Replace Gatsby v4 (from a Netlify CMS starter template) with Hugo (ea5ea57) | Simpler content model with no GraphQL or React, direct Markdown editing, and much faster builds (about 100ms against 30-60 seconds). Plan in `HUGO-CONVERSION-PLAN.md`. |
| 19 Jul 2026 | Build a custom theme on Bulma rather than use an off-the-shelf Hugo theme | Keep the existing design and branding, and limit migration risk. |
| 19 Jul 2026 | Use Netlify's `_redirects` for old URLs, not only Hugo aliases | True 301 redirects, which search engines follow better. |
| 19 Jul 2026 | Rename the blog to News | Fits a Scout group better than "blog". |
| 19 Jul 2026 | Pin Hugo 0.128.2 (750c69f) | The planned 0.148.2 might not have been available on Netlify's build image; 0.128.2 was known to work and has the features the site needs. |
| 19 Jul 2026 | Keep section details in `data/sections.yaml` | One place for meeting times and ages, so the section pages and home page can't disagree. Recorded in `docs/requirements/sections.md`. |
| 25 Jul 2026 | Replace Decap CMS with Sveltia CMS (f33e945) | A drop-in replacement using the same `config.yml`, with better performance, media library and search, and active development. |
| 28 Jul 2026 | The CMS saves to `master` (affb09f) | It had pointed at the conversion branch; it was moved to `master` when that branch was merged. The reason for choosing `master` over `dev` wasn't recorded. See #14. |
| 25 Sep 2026 | Stamp every build with its commit (02b7f08, #11) | Netlify doesn't report builds to GitHub for this repo, so the stamp is how a change is confirmed on the dev site. |
| 28 Sep 2026 | Move working rules to the lvlup-workflow plugin and project rules to `docs/` (99fefd8) | One set of workflow rules shared across projects; Bardon-specific principles and requirements kept in this repo. |
| 4 Oct 2026 | Turn off tag and category pages (`disableKinds`, #67) | The site has no template for them, so the sitemap listed 15 addresses that returned 404. News posts still show their tags as text. The unused `sections` taxonomy was removed too: Hugo had been building the Our Sections page (`/sections/`) as that taxonomy's list page, so turning taxonomy pages off would have removed it. |
| 6 Oct 2026 | Program pages go in the footer, not the menu (#81) | The site has outgrown putting every page on the menu. Program pages are for leaders and adult supporters, so they stay out of the menu but can still be found from the footer. |
