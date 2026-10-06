# Pages and navigation

## What it's for

How ordinary pages (About, Join Us, Leaders, policies and so on) are added, so every page can be found and edited.

## Requirements

- Every new page is added to the CMS, `static/admin/config.yml`, as a file entry with `title`, `description`, hidden `type: page`, and `body`.
- Every new page is added to the navigation menu, `config/_default/menus.toml`, except program pages.
- **Program pages** describe how to run a section's meeting programs, for leaders and adult supporters, e.g. Joey Programs (`/sections/joey-programs/`). They aren't added to the menu. They're added to the footer, `layouts/partials/footer.html`, instead.
- Internal links end with a trailing slash, e.g. `/about/`, because Hugo serves each page as `/about/index.html`.
- Pages with `draft: true` aren't published. Remove it when the page is ready.
- URLs from the old Gatsby site keep working through the redirects in `static/_redirects`. Don't remove them.

## How to check

On the dev site:
- **PN-1:** The new page returns 200 at its URL with a trailing slash.
- **PN-2:** The menu links to it, unless it's a program page.
- **PN-3:** The dev site's `/admin/config.yml` includes its file.
- **PN-4:** A program page isn't in the menu, and the footer links to it.
