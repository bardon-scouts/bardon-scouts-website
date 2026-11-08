# Content standards

## What it's for

Rules for all written content on the site, on top of the lvlup-workflow writing style (no em dashes, hype words or AI filler).

## Requirements

### Section names

Scouts Queensland asked that the site uses the official section names, as on [scoutsqld.au](https://www.scoutsqld.au/) (issue #104).

- Use **Joey Scouts**, **Cub Scouts**, **Scouts**, **Venturer Scouts** and **Rover Scouts**, in page text, titles, menus, the footer, `data/sections.yaml` and CMS labels.
- Never write "Joeys", "Cubs", "Venturers" or "Rovers" on their own. One member is a "Joey Scout", "Cub Scout" and so on.
- Use the full name when the section name describes something: "Cub Scout Leader (Akela)", "Joey Scout program", "Venturer Scout section".
- Leave these as they are: URLs and slugs (`/sections/joeys/`), event names (Joey Jaunt, Cuboree), group words (Joey mob, Cub pack, Rover crew), Scout Shop product names, place names (Cub Hut, Cub Flat) and historical names (Wolf Cubs).
- Rover Scouts is a planned section; refer to it as coming soon.

### Helpful, not blunt

LvlUp Labs' website requirements apply this to every website, including this one (lvlup-labs/lvluplabs_operations#239, issue #115).

- Pages say what we aim for and how we help, rather than promising a result in a few hard words. For example "Scouts aims to help young people develop confidence", not "Scouts develops confidence".
- Avoid outcome promises such as "life-changing", "reach their full potential", "lifelong friends", "the safest possible environment" and "you'll never be alone".
- Facts about how things run aren't promises and can stay direct: "invoices will be sent", "signing in lets us know who is present".

### Headings

- Don't repeat the page title as the first `##` heading. The title is already the page's main heading.

### Financial information

Never publish:
- payment methods or bank account details
- invoice due dates, or the months or schedule of invoicing
- specific payment deadlines
- bank transfer instructions
- payment portal URLs, except Consent2go for events and Bardon Scouts' own Stripe links (see below)

Allowed:
- Bardon Scouts' own Stripe payment links (`buy.stripe.com`) and their QR codes, e.g. the Mango Fundraiser order link
- general fee amounts, e.g. "$344 per six months"
- that invoices will be sent, and to check for them
- "payment details are on your invoice"

### Images

- Images live in `static/img/` and are referenced as `/img/<name>`, so the CMS can manage them.

## How to check

- **CS-1:** Search `content/`, `data/`, `layouts/` and `config/` for "Joey", "Cub", "Venturer" and "Rover" not followed by "Scout". The only matches allowed are the exceptions above (URLs and slugs, event names, group words, product, place and historical names).
- **CS-2:** On the site, the navbar Sections menu, the footer, the home page section list and each section page title show Joey Scouts, Cub Scouts, Scouts and Venturer Scouts, and Rover Scouts as coming soon.
- **CS-3:** Search for bank details, BSB, account numbers, "due", "deadline" and invoice months on any page that mentions fees.
- **CS-4:** Run the plugin's `style-check` on changed content.
- **CS-5:** Read each changed page's text, title and description: no line states an outcome as a bare promise. Search `content/`, `data/` and `layouts/` for "life-changing", "full potential", "lifelong", "guarantee", "ensure", "safest", "never be alone" and "will learn": each match is either a fact about how things run or reworded.
