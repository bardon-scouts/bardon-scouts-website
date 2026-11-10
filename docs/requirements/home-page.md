# Home page

## What it's for

The first page parents see: what Bardon Scouts is, why to join, the sections and when they meet, and the events.

## Requirements

Sections, in this order (`layouts/index.html`):

1. **Hero**: image, heading and subheading from `content/_index.md`
2. **Main pitch**: a heading and text about the adventure of Scouting, written about the child and family: what Scouts gives a young person and how (the site's offer, #111), then a "who we are" line saying we are Bardon Scouts, part of Scouts Australia and Scouts Queensland, with a link to [Scouts Queensland](https://www.scoutsqld.au/) (`mainPitch` in `content/_index.md`). The main pitch text is the same size as the "who we are" line, and sits close under the hero (#122)
3. **Features**: the four images and blurbs from `data/features.yaml`, with no heading, close under the main pitch (#122)
4. **Our Units**: each section's name, age range and meeting time, from `data/sections.yaml`, with the den's address
5. **Events**: a parent-focused heading about outdoor adventures ("Outdoor adventures all year", `eventsSection` in `content/_index.md`), then every event in the Events menu as a link, in a four-column grid, with a "See all events" button to `/events/`

All home page text is editable in the CMS (Homepage, Homepage Features, Scout Sections). The events grid follows the Events menu automatically.

The page has no "Contact us" button: the navbar's "Join" button, on every page, is its call to action (#122, `pages-and-navigation.md`). The CMS's "Show Contact Button" toggle (`contactCTA`) is off.

## How to check

On the dev site's home page:
- **HP-1:** The sections appear in the order above.
- **HP-2:** The events grid lists the same events as the Events menu, and every link returns 200.
- **HP-3:** The page says we are part of Scouts Australia and Scouts Queensland, and the Scouts Queensland link returns 200.
- **HP-4:** The page has no "Contact us" button, has the navbar's "Join" button linking to `/ask-to-join/`, and has four feature images, with no "Get ready for adventure" heading above them.
- **HP-5:** The main pitch says what Scouts gives a young person and how (for example: they plan their own adventures, build skills outdoors and grow in confidence).
