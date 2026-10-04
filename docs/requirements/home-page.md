# Home page

## What it's for

The first page parents see: what Bardon Scouts is, why to join, the sections and when they meet, and the events.

## Requirements

Sections, in this order (`layouts/index.html`):

1. **Hero**: image, heading and subheading from `content/_index.md`
2. **Why Join Scouts?**: the main pitch from `content/_index.md`
3. **Contact call to action**
4. **Features**: from `data/features.yaml`
5. **Contact call to action**
6. **Our Units**: each section's name, age range and meeting time, from `data/sections.yaml`, with the den's address
7. **Our Events**: every event in the Events menu as a link, in a four-column grid, with a "See all events" button to `/events/`

All home page text is editable in the CMS (Homepage, Homepage Features, Scout Sections). The events grid follows the Events menu automatically.

## How to check

On the dev site's home page:
- **HP-1:** The sections appear in the order above.
- **HP-2:** "Our Events" lists the same events as the Events menu, and every link returns 200.
