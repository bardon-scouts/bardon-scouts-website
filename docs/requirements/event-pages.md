# Event pages

## What it's for

One page per event Bardon Scouts runs or takes part in (e.g. Group Camp, Cuboree, ANZAC Day March), so parents can see what it is, when it happens and who can go.

## Requirements

### The page

- Lives at `content/<slug>.md` and is served at `/<slug>/`.
- Front matter: `title`, `description`, `type: page`, and `image`. New events use the placeholder `/img/scouts_logo.jpg` until a real photo is available.
- Has an **Event Details** section near the top with at least **When:** and **Who:** lines. Add **Where:** and **Duration:** when known.
- **Who** uses section names only (Joeys, Cubs, Scouts, Venturers). **No age ranges** on event pages.
- Details that aren't confirmed are marked as such (e.g. "dates to be announced"), not guessed.

### Everywhere the event must appear

A new event is only complete when it's in all of these:

1. **Events listing**, `content/events/_index.md`: an entry with the event name linked to its page, **When:**, **Who:**, a one or two sentence summary, and a "Learn more" link.
2. **Events menu**, `config/_default/menus.toml`: an entry with `parent = "events"`.
3. **CMS**, `static/admin/config.yml`: a file entry for `content/<slug>.md`, alongside the other event pages, so leaders can edit it.
4. **Home page**: the "Our Events" grid is built from the Events menu, so it appears there automatically once step 2 is done.

## How to check

On the dev site:
- `/<slug>/` returns 200 and shows the title, When and Who.
- `/events/` links to the page (heading and "Learn more"), and the Events menu links to it.
- The home page "Our Events" grid links to it.
- The dev site's `/admin/config.yml` includes `content/<slug>.md`.
