# Promotional flyer (#84)

A double-sided A5 flyer for local state schools to send home with prep and early childhood children. One side is for families of young children, the other for adults who might volunteer. Each side has a QR code to a page on the site written for people who have just scanned it.

Status: **proposed, waiting for the owner's approval.** Requirements are in `docs/requirements/printed-materials.md`.

## Audiences and the one message each

| Side | Reader | Message | Next step |
|---|---|---|---|
| Families | A parent with a child in prep or early childhood, who may not know what Scouts is. The child sees the picture. | Joeys at Bardon is fun, local, and you can try it for free. | Scan, then ask to visit |
| Volunteers | Any adult nearby: parents, grandparents, neighbours. | You don't need experience. We'll train you, and any amount of time helps. | Scan, then get in touch |

The two sides work separately. A school may stack flyers either way up, so neither side can depend on the other.

## Facts the flyer uses, and where they come from

Every fact printed must match the site when the flyer goes to print (PM-2).

| Fact | Source |
|---|---|
| Joeys are ages 6 to 8 | `data/sections.yaml` (see open question 1) |
| Joeys meet Tuesday, 6:30 - 7:30pm | `data/sections.yaml` |
| 11 Bee Street, Bardon | `config/_default/params.toml` |
| A free trial visit | `content/join/come-and-try.md` |
| Joey activities: games, crafts, stories, outdoor skills, friends | `data/sections.yaml` (Joeys "What We Do") |
| No experience needed; training is provided | `content/leaders/volunteering.md` |
| Flexible time: weekly, monthly or now and then | `content/leaders/volunteering.md` |
| "Meet the other you" | `content/leaders/volunteering.md` (page heading) |

Never printed: fees, payment details, leaders' names or contact details, or children's names.

## Three concepts

All three use the brand colours (teal `#43a09b`, red `#d9432d`), the Bardon Scouts logo (`static/img/logo.svg`), and the same QR targets. Word counts are body text, not counting the headline or the URL under the QR code. A visual mock-up of all three: https://claude.ai/artifact/Pa1V6awU68jc55UgQfM4ge (private to the owner until shared).

### Concept A: Adventure starts here (photo)

A photo fills the top half of each side, with a teal band below.

**Families side**
- Headline: **Adventure starts here!**
- Body: Joeys at Bardon Scouts. Games, crafts, friends and the outdoors, ages 6 to 8. Tuesdays 6:30 - 7:30pm, 11 Bee Street. Try it free. (23 words)
- QR: `bardonscouts.org.au/try/`, labelled "Scan to visit"

**Volunteers side**
- Headline: **Meet the other you**
- Body: No experience needed: we'll train you. Help weekly, monthly or now and then. Make a difference for young people in Bardon. (21 words)
- QR: `bardonscouts.org.au/volunteer/`, labelled "Scan to find out more"

Strength: it looks like the website, so it's clearly the same group. Weakness: it depends on a good photo with the right consent (open question 3).

### Concept B: Colour me in (illustration)

The families side is a simple line drawing for the child to colour: a tent, a campfire, a kangaroo with a joey and a group of children. A teal strip at the bottom carries the details for parents. The volunteer side is solid teal with white type.

**Families side**
- Headline: **Colour me in! Then come and try Joeys.**
- Body: Ages 6 to 8. Tuesdays 6:30 - 7:30pm at 11 Bee Street, Bardon. Your first visit is free. (17 words)
- QR: `bardonscouts.org.au/try/`

**Volunteers side**
- Headline: **Kids aren't the only ones having fun**
- Body: Volunteer with Bardon Scouts. No experience needed, full training given. A few hours or every week: it all helps. (19 words)
- QR: `bardonscouts.org.au/volunteer/`

Strength: the child keeps it, so it stays on the fridge, and it needs no photos of real children. Weakness: it needs an illustration drawn (or generated and checked), and the volunteer side has no picture.

### Concept C: Big words (type only)

Bold type on solid colour, with no photo: teal for families, red for volunteers. Short lines read like a list of things to do.

**Families side**
- Headline: **Play. Make. Explore. Belong.**
- Body: Joeys at Bardon Scouts, ages 6 to 8. Tuesdays 6:30 - 7:30pm, 11 Bee Street. Try it free. (17 words)
- QR: `bardonscouts.org.au/try/`

**Volunteers side**
- Headline: **Got a few hours? We'll teach you the rest.**
- Body: Volunteer with Bardon Scouts. Training provided, Blue Card help included. (10 words)
- QR: `bardonscouts.org.au/volunteer/`

Strength: the cheapest to make and the easiest to read from a distance. Weakness: it's the least appealing to a 5 year old.

**Recommendation:** Concept A for the volunteers side and Concept B for the families side. The colouring side gives a child a reason to keep the flyer, and the photo side lets the volunteer message look like the website. If photo consent can't be confirmed, use Concept C's volunteer side instead.

## QR codes and where they land

Each side has its own QR code, so families and volunteers each land on a page written for them. The URL is printed under each code, so people without a camera can type it in.

| Side | Printed URL | Lands on |
|---|---|---|
| Families | `https://bardonscouts.org.au/try/` | A new short page, "Try Joeys" |
| Volunteers | `https://bardonscouts.org.au/volunteer/` | A new short page, "Volunteer with Us" |

Why new pages rather than the existing ones:
- **Short, permanent URLs.** A printed code can't be changed, so its URL must never move. `/try/` and `/volunteer/` say what they're for, are easy to type, and don't depend on where the Join and Leaders pages sit in the menu.
- **Clarity for someone new.** Come and Try and How to Join are written for families who already know about Scouts. Volunteering runs to about 600 words. Someone arriving from a flyer needs the answer and one next step.

### Try Joeys (`/try/`)

For a parent who has just scanned the flyer. Short: under 200 words. In this order:
1. One sentence on what Joeys is, and the ages (from `data/sections.yaml`).
2. When and where: Tuesday 6:30 - 7:30pm, 11 Bee Street, Bardon (from `data/sections.yaml` and `params.toml`, not typed in).
3. How to come and try, in three steps: send us a message (meetings are sometimes away from the Den, so ask at least a day ahead); fill in Form F6 and bring it; come along.
4. One button: **Ask to visit**, to the contact form.
5. Links for more: the Joeys page, Fees, Play On! vouchers, and Our Sections for older brothers and sisters.

### Volunteer with Us (`/volunteer/`)

For any adult who has just scanned the flyer. Under 200 words. In this order:
1. "Meet the other you", and one sentence on why.
2. What you could do, in one line each: help at a section, help at events now and then, join the committee, share a skill.
3. What you need: a Blue Card (we help you apply) and to be willing to learn. Training is provided.
4. One button: **Get in touch**, to the contact form.
5. A link to the full Volunteering page.

### The contact form

Both pages send people to the contact form, but its "child's name" field is required (`docs/requirements/forms.md`). A volunteer without a child at the group can't send it without making something up. The design proposes:
- making `child_names` optional, labelled "Your child's name (if any)", and
- adding a required `enquiry` list (Joining or a visit, Volunteering, Something else), set from the page the visitor came from, so leaders see where interest comes from.

This changes `forms.md`, so it needs the owner's agreement (open question 4).

### Navigation

The two pages are for people arriving from print, like program pages are for leaders. Proposed: they aren't in the menu. Come and Try links to `/try/`, and Volunteering links to `/volunteer/`. This is a new exception to `pages-and-navigation.md`, written in `printed-materials.md`.

## Print spec

- A5 portrait, 148 x 210 mm, double-sided, with 3 mm bleed and a 5 mm safe area.
- Images at 300 dpi at print size. Final file as a print PDF from Canva.
- QR codes at least 25 mm square, dark on a white square with a quiet zone of at least 4 modules, and error correction level M or higher.
- Body text at least 11 pt, and the headline at least 28 pt.

## Open questions for the owner

1. **Ages.** Queensland prep children are about 5, but the site says Joeys are ages 6 to 8. Should the flyer target prep at all? If Joeys take 5 year olds, `data/sections.yaml` needs correcting first. If not, should the flyer say "from age 6" or "for Year 1 to Year 3"?
2. **The fair flyer.** It couldn't be opened, because Canva isn't connected (lvlup-labs/lvluplabs_operations#62). Which of its wording, pictures or layout must the new flyer keep?
3. **Photos.** Concept A needs a photo of children. Is there one with consent for printed use, or should it use children who can't be identified, or an illustration?
4. **Contact form.** Agree to `child_names` becoming optional and the new `enquiry` list?
5. **Landing pages.** New `/try/` and `/volunteer/` pages (proposed), or send the codes to Come and Try and Volunteering?
6. **Schools.** Does each school need to approve the flyer first, and how many copies does each one need? This sets the print run.
7. **Scouts Queensland branding.** Do Scouts Queensland's brand rules apply to printed material, such as logo use or wording?
