# Content standards

## What it's for

Rules for all written content on the site, on top of the lvlup-workflow writing style (no em dashes, hype words or AI filler).

## Requirements

### Section names

- Use **Joeys**, **Cubs**, **Scouts** and **Venturers**.
- "Joey Scouts" is allowed only when referring to the formal section name.
- Never write "Cub Scouts" or "Cub Scout". Use "Cubs", or "Cub Leader" rather than "Cub Scout Leader". The only exception is an external product name, such as the Scout Shop's "Cub Scout Uniform" link.
- Rovers is a planned section; refer to it as coming soon.

### Headings

- Don't repeat the page title as the first `##` heading. The title is already the page's main heading.

### Financial information

Never publish:
- payment methods or bank account details
- invoice due dates, or the months or schedule of invoicing
- specific payment deadlines
- bank transfer instructions
- payment portal URLs (Consent2go for events is the only exception)

Allowed:
- general fee amounts, e.g. "$344 per six months"
- that invoices will be sent, and to check for them
- "payment details are on your invoice"

### Images

- Images live in `static/img/` and are referenced as `/img/<name>`, so the CMS can manage them.

## How to check

- Search `content/` and `data/` for "Cub Scout". The only match allowed is the Scout Shop product link.
- Search for bank details, BSB, account numbers, "due", "deadline" and invoice months on any page that mentions fees.
- Run the plugin's `style-check` on changed content.
