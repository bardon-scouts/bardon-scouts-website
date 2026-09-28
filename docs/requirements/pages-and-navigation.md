# Pages and navigation

## What it's for

How ordinary pages (About, Join Us, Leaders, policies and so on) are added, so every page can be found and edited.

## Requirements

- Every new page is added to **both**:
  - the navigation menu, `config/_default/menus.toml`
  - the CMS, `static/admin/config.yml`, as a file entry with `title`, `description`, hidden `type: page`, and `body`
- Internal links end with a trailing slash, e.g. `/about/`, because Hugo serves each page as `/about/index.html`.
- Pages with `draft: true` aren't published. Remove it when the page is ready.
- URLs from the old Gatsby site keep working through the redirects in `static/_redirects`. Don't remove them.

## How to check

On the dev site:
- The new page returns 200 at its URL with a trailing slash.
- The menu links to it.
- The dev site's `/admin/config.yml` includes its file.
