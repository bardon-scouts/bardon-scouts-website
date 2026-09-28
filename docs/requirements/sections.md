# Scout sections

## What it's for

The Joeys, Cubs, Scouts and Venturers pages, and the section details shown on the home page.

## Requirements

- **`data/sections.yaml` is the single source of truth** for each section's name, slug, age range, meeting day and time, image, description, tagline, activities, leader title and page content. Leaders edit it in the CMS under "Scout Sections".
- The section pages (`/sections/<slug>/`) and the home page's "Our Units" list both read from that file, so a change there updates both. Don't copy meeting times or age ranges into other pages.
- `content/sections/<slug>.md` (`type: sections`) holds extra content for a section page, such as the list of events that section attends. Keep those lists in step with the events each section actually attends.
- Age ranges belong on section pages. They're only banned on event pages.
- Rovers has its own page, `content/sections/rovers.md`, marked as coming soon, and isn't in `data/sections.yaml`.

## How to check

On the dev site:
- Each `/sections/<slug>/` page and the home page "Our Units" list show the same meeting day, time and age range as `data/sections.yaml`.
