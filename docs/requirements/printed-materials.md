# Printed materials

## What it's for

Flyers and other printed material that point people to the site with a QR code, and the pages those codes land on. A printed code can't be changed once it's handed out, so its page has to be right before printing and stay at the same address afterwards. Status: proposed in #84, waiting for approval. Design in `docs/design/promotional-flyer.md`.

## Requirements

### The printed material

- Follows `docs/principles.md` and `content-standards.md`: section names, no payment details, no leaders' contact details.
- Every fact on it (ages, meeting days and times, address, what's free) matches the site's source for that fact when it goes to print: `data/sections.yaml`, `config/_default/params.toml` or the page it came from.
- Each side or panel aimed at a different reader has its own QR code, and the code's URL is printed beside it.
- QR codes are at least 25 mm square, dark on white, with a quiet zone of at least 4 modules.
- Children shown in photos have consent for printed use, or can't be identified.

### QR codes

- A QR code points to a page on `https://bardonscouts.org.au/`, with a short path ending in a trailing slash, e.g. `/try/`.
- A QR code's page is live on production before the material is printed.
- A QR code's URL keeps working for as long as the printed material could be in use. If its page is retired or moved, add a redirect in `static/_redirects`; never remove one.

### QR landing pages

- A landing page is written for someone who knew nothing about Bardon Scouts before scanning: what it is, who it's for, when and where, and one clear next step.
- It's under 200 words, with one call to action.
- Meeting days, times and ages come from `data/sections.yaml`, not typed into the page.
- Like every page, it's in the CMS (`pages-and-navigation.md`). Unlike other pages, it isn't on the menu. A related page links to it: Come and Try to `/try/`, Volunteering to `/volunteer/`.

| Page | Path | For | Call to action |
|---|---|---|---|
| Try Joeys | `/try/` | Families with children starting school | Ask to visit (contact form) |
| Volunteer with Us | `/volunteer/` | Adults who might volunteer | Get in touch (contact form) |

## How to check

Before printing (production, and the print-ready file):
- **PM-1:** Each QR code in the print file decodes to its printed URL, and that URL returns 200 on production.
- **PM-2:** Each fact on the flyer matches its source on production. List each fact, its source and whether they match.
- **PM-3:** Each QR code is at least 25 mm square at print size, measured in the print PDF.
- **PM-4:** A test print scans on at least two phones (one iPhone and one Android), from about 30 cm.
- **PM-5:** The flyer has no fee amounts, payment details, or leaders' names or contact details.

On the dev site, for a landing page:
- **PM-6:** The page returns 200 at its path, has under 200 words of body text, and has one call to action linking to `/contact/`.
- **PM-7:** Its meeting day, time and age range match `data/sections.yaml`.
- **PM-8:** It isn't on the menu, and its related page links to it.
- **PM-9:** The dev site's `/admin/config.yml` includes its file.
