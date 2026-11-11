# Pages and navigation

## What it's for

How ordinary pages (About, Join Us, Leaders, policies and so on) are added, so every page can be found and edited.

## Requirements

- Every new page is added to the CMS, `static/admin/config.yml`, as a file entry with `title`, `description`, hidden `type: page`, and `body`.
- Every new page is added to the navigation menu, `config/_default/menus.toml`, except program pages and the Privacy Policy.
- **Program pages** describe how to run a section's meeting programs, for leaders and adult supporters, e.g. Joey Scout Programs (`/sections/joey-programs/`). They aren't added to the menu. They're added to the footer, `layouts/partials/footer.html`, instead.
- **Every page leads to asking to join.** The navbar has a "Join" button linking to `/ask-to-join/` (`layouts/partials/navbar.html`), visible without opening the menu on phones too, and the footer's Join Us column links to it, so every page offers the site's main action (#111).
- **Every page links to the Privacy Policy.** The footer's bottom row links to `/privacy/` (`content/privacy.md`). The Privacy Policy names the fields every form collects (see `docs/requirements/forms.md`), how they're used, where they're stored, and how to ask to see, correct or delete them, and links to the Scouts Queensland Privacy Policy for the rest. A committee member or leader approves its wording before it's published (#111).
- Internal links end with a trailing slash, e.g. `/about/`, because Hugo serves each page as `/about/index.html`.
- Pages with `draft: true` aren't published. Remove it when the page is ready.
- URLs from the old Gatsby site keep working through the redirects in `static/_redirects`. Don't remove them.

## How to check

On the dev site:
- **PN-1:** The new page returns 200 at its URL with a trailing slash.
- **PN-2:** The menu links to it, unless it's a program page or the Privacy Policy.
- **PN-3:** The dev site's `/admin/config.yml` includes its file.
- **PN-4:** A program page isn't in the menu, and the footer links to it.
- **PN-5:** Every page links to `/ask-to-join/` and to `/privacy/`. The whole-site check (`scripts/site_check.py`) checks every page it crawls.
- **PN-6:** `/privacy/` returns 200 and names the fields of every form in the `docs/requirements/forms.md` table.
