# Printed materials

## What it's for

Flyers and other printed material that send people to the site with a QR code, and the pages those codes land on. A printed code can't be changed once it's handed out, so its page has to be right before printing and stay at the same address afterwards. Status: proposed in #84, waiting for approval. Design in `docs/design/promotional-flyer.md`.

## Requirements

### Content

- Follows `docs/principles.md` and `content-standards.md`: section names, no payment details, no leaders' contact details.
- Every fact on it (ages, meeting days and times, address, what's free) matches the site's source for that fact when it goes to print: `data/sections.yaml`, `config/_default/params.toml` or the page it came from.
- Children shown in photos have consent for printed use, or can't be identified.

### Brand

Scouts Queensland's brand rules apply (https://scoutsqld.com.au/brandhome/, which points to the Scouts Australia Brand Book).

- Logos are the official files from the Scouts Australia Brand Centre, unaltered. The Group logo carries the words "Bardon Scout Group" and is at least 30 mm wide, with clear space of 2.5 times the "S" on each side and 1 times above.
- Material for one section uses that section's logo and colours.
- Text is in Nunito Sans (Arial if it can't be used), and colours come from the Brand Book palette.
- Brand assets (logos, Gumtree Graphics) are never redrawn, recoloured or AI-generated. Any drawing of people in uniform shows the correct uniform for their section.
- Before printing, the proof is sent to Scouts Queensland's brand team (brandsupport@scoutsqld.com.au) for approval.

### QR codes

- Each side or panel aimed at a different reader has its own QR code, and the code's URL is printed beside it.
- QR codes are at least 25 mm square, dark on white, with a quiet zone of at least 4 modules.
- A QR code points to an existing page on `https://bardonscouts.org.au/`, with a trailing slash.
- A QR code's page is live on production, with any changes the material relies on, before the material is printed.
- A QR code's URL keeps working while the material could be in use. If its page is retired or moved, add a redirect in `static/_redirects`; never remove one.

### Pages that QR codes land on

- The opening text, the first thing below the page's hero image, tells someone new to Bardon Scouts what the page offers and gives one clear next step, with a link.
- Meeting days, times and ages come from `data/sections.yaml`, not typed into the page.

| Printed material | Page | For | Next step |
|---|---|---|---|
| School flyer (#84), families side | `/join/come-and-try/` | Families with young children | Ask to visit (contact form) |
| School flyer (#84), volunteers side | `/leaders/volunteering/` | Adults who might volunteer | Get in touch (contact form) |

## How to check

Before printing (production, and the print-ready file):
- **PM-1:** Each QR code in the print file decodes to its printed URL, and that URL returns 200 on production.
- **PM-2:** Each fact on the flyer matches its source on production. List each fact, its source and whether they match.
- **PM-3:** Each QR code is at least 25 mm square at print size, measured in the print PDF.
- **PM-4:** A test print scans on at least two phones (one iPhone and one Android), from about 30 cm.
- **PM-5:** The flyer has no fee amounts, payment details, or leaders' names or contact details.
- **PM-10:** The logos are the Brand Centre files. The Group logo is at least 30 mm wide with its clear space, and the text is in Nunito Sans.
- **PM-11:** The QR URLs are listed in the table above, and neither page has been moved without a redirect.
- **PM-12:** Scouts Queensland's brand team has approved the proof (keep the email).

On the dev site, for a page a QR code lands on:
- **PM-6:** The page returns 200 at its path, and the first paragraph below the hero says what the page offers and links to its next step.
- **PM-7:** Any meeting day, time or age range on it matches `data/sections.yaml`.
- **PM-9:** The dev site's `/admin/config.yml` still includes its file.

PM-8 was withdrawn: it checked new QR-only pages, which won't be made.
