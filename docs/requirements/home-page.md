# Home page

## What it's for

The first page parents see: what Bardon Scouts is, why to join, the sections and when they meet, and the events.

## Requirements

Sections, in this order (`layouts/index.html`):

1. **Hero**: image, heading and subheading from `content/_index.md`
2. **Main pitch**: a heading and text about the adventure of Scouting, then a "who we are" line saying we are Bardon Scouts, part of Scouts Australia and Scouts Queensland, with a link to [Scouts Queensland](https://www.scoutsqld.au/) (`mainPitch` in `content/_index.md`)
3. **Contact call to action**: the only "Contact us" button on the page
4. **Features**: the "Get ready for adventure" heading and the four images and blurbs from `data/features.yaml`
5. **Our Units**: each section's name, age range and meeting time, from `data/sections.yaml`, with the den's address
6. **Events**: a parent-focused heading about outdoor adventures ("Outdoor adventures all year", `eventsSection` in `content/_index.md`), then every event in the Events menu as a link, in a four-column grid, with a "See all events" button to `/events/`

All home page text is editable in the CMS (Homepage, Homepage Features, Scout Sections). The events grid follows the Events menu automatically.

## How to check

On the dev site's home page:
- **HP-1:** The sections appear in the order above.
- **HP-2:** The events grid lists the same events as the Events menu, and every link returns 200.
- **HP-3:** The page says we are part of Scouts Australia and Scouts Queensland, and the Scouts Queensland link returns 200.
- **HP-4:** The page has exactly one "Contact us" button, and four feature images under "Get ready for adventure".
