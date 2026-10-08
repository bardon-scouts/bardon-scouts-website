# Promotional flyer (#84)

A double-sided A5 flyer for local state schools to send home with prep and early childhood children. One side is for families of young children, the other for adults who might volunteer. Each side has a QR code to an existing page on the site, updated so it works for someone who has just scanned it.

Status: **proposed, waiting for the owner to choose a concept.** Requirements are in `docs/requirements/printed-materials.md`. Mock-up: https://claude.ai/artifact/Pa1V6awU68jc55UgQfM4ge (private to the owner until shared).

## Settled with the owner (#84, 9 Oct 2026)

| Question | Answer |
|---|---|
| Ages | Joeys take ages 5 to 8. The site's "6 to 8" is wrong and is being fixed separately. |
| The fair flyer | Nothing has to carry over, but its photos can be used for now. |
| Contact form | "Child's name" becomes optional. |
| QR pages | Use the existing pages and update them. No new pages. |
| Schools | The owner is arranging this with the principals, including numbers. |
| Branding | Scouts Queensland's brand rules apply: https://scoutsqld.com.au/brandhome/ |

## The fair flyer in Canva

The fair flyer is two single-page A4 designs in Canva: "Bardon Scouts Youth Recruitment" (four activity photos) and "Bardon Scouts Leader Recruitment" (a leader fitting a Joey's climbing harness). The A5 copy is one two-page design, **"Bardon Scouts School Flyer A5 (#84)"**: page 1 is the youth side, page 2 the leader side, resized by Canva to 1118 x 1588 px (A5 at twice Canva's 96 dpi). The originals are unchanged. Build starts from this copy or from the Scouts Queensland template.

What the copy shows for Build (checked 9 Oct 2026):

| Item | Finding | What Build does |
|---|---|---|
| Photos (5) | 615 to 880 dpi at A5 | Usable as they are |
| Group logo (`Bardon-Hori-Full.png`) | 263 x 99 px, about 94 dpi at 71 mm wide | Replace with the Brand Centre file (PM-10) |
| Heading images ("Change lives", the page 1 header) | About 243 and 252 dpi | Rebuild as Nunito Sans text, which the brand rules need anyway |
| Other text | Mostly images of text in other fonts, plus maroon `#681e35` panels | Rebuild in Nunito Sans and brand colours |
| QR codes | Both go to `https://bardonscouts.org.au/` (the home page), error correction H, about 62 mm. The photo above and the page edge leave almost no quiet zone, and a "TQRCG" mark covers one corner. OpenCV couldn't read them; zxing could | Replace with new codes for the two pages below, with a full quiet zone (PM-1, PM-3, PM-4) |

The leader photo shows a Joey in uniform, so it also suits the families side.

## Brand rules that shape the flyer

From the Scouts Australia Brand Book (August 2026), which the Scouts Queensland brand page points to, and from that page itself:

- **Logo:** use the official files from the Scouts Australia Brand Centre (members log in with their membership number), never redrawn or AI-generated. A Scout Group uses the logo with its name: "Bardon" in Nunito Sans Black and "Scout Group" in Nunito Sans Regular. Keep clear space of 2.5 times the "S" on each side and 1 times above. The logo with its words must be at least 30 mm wide. Use full colour with black lettering on light backgrounds, and full colour with white lettering (or white only) on dark ones. Don't place it on a busy part of a photo.
- **Section material:** material for one section uses that section's logo and colours. The families side is about Joeys, so it uses the Joey Scouts logo and the Joeys colours.
- **Typeface:** Nunito Sans. Headings in Black, body in Regular or Bold, mostly left aligned. Arial if Nunito Sans isn't available.
- **Colours:** the flyer uses brand colours, not the website's teal and red:

  | Use | Colour | Hex | Print |
  |---|---|---|---|
  | Families side panels | Scouts Joeys (dark) | `#973d20` | PMS 1675c |
  | Families side accent | Scouts Joeys Brown | `#ba6228` | PMS 471c, C21 M76 Y100 K10 |
  | Volunteers side panels | Australian Navy Blue | `#28265c` | PMS 280c, C100 M98 Y28 K24 |
  | Volunteers side accent | Scouts Teal | `#008f88` | PMS 7714c, C95 M16 Y53 K0 |
  | Text on white | Dark Grey | `#575756` | K80 |

  White text goes on the darker shades, which read clearly; Joeys Brown and Scouts Teal are too light for small white text. The website's red (`#d9432d`) is close to the Rovers colour, so it's left off.
- **Gumtree Graphics:** the brand's gum bark pattern can be used as a border or background, cropped but never redrawn, recoloured or used in greyscale. No text over the figures in it. The Joey Scouts version goes on the families side.
- **Photos:** Scouting in action, usually young people outdoors, or the view from a participant's point of view.
- **AI images:** allowed only to support ideas. They must never stand in for brand assets, and must never show wrong uniforms, scarves or badges.
- **Tone:** short, sharp, positive sentences that speak as "we".
- **Approval:** new artwork goes to the Branch before production. For Queensland, send the proof to brandsupport@scoutsqld.com.au.
- **Templates:** Scouts Queensland has an editable Canva poster template (on its Printable Resources page) and the Brand Centre has more. Build can start from one of these, resized to A5, which keeps the logo and fonts right.

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
| Joeys are ages 5 to 8 | `data/sections.yaml` (it says 6 to 8 until the fix is published) |
| Joeys meet Tuesday, 6:30 - 7:30pm | `data/sections.yaml` |
| 11 Bee Street, Bardon | `config/_default/params.toml` |
| A free trial visit | `content/join/come-and-try.md` |
| Joey activities: games, crafts, stories, outdoor skills, friends | `data/sections.yaml` (Joeys "What We Do") |
| No experience needed; training is provided | `content/leaders/volunteering.md` |
| Flexible time: weekly, monthly or now and then | `content/leaders/volunteering.md` |
| "Meet the other you" | `content/leaders/volunteering.md` (page heading) |

Never printed: fees, payment details, leaders' names or contact details, or children's names.

## Three concepts

All three use Nunito Sans, the brand colours above, the Bardon Scout Group logo, and the same QR targets. The families side also carries the Joey Scouts logo. Word counts are body text, not counting the headline or the URL under the QR code.

### Concept A: Adventure starts here (photo)

A photo from the fair flyer fills the top half of each side, with a colour panel below.

**Families side** (Joeys dark panel)
- Headline: **Adventure starts here!**
- Body: Joeys at Bardon Scouts. Games, crafts, friends and the outdoors, ages 5 to 8. Tuesdays 6:30 - 7:30pm, 11 Bee Street. Try it free. (23 words)
- QR: `bardonscouts.org.au/join/come-and-try/`, labelled "Scan to visit"

**Volunteers side** (Navy panel)
- Headline: **Meet the other you**
- Body: No experience needed: we'll train you. Help weekly, monthly or now and then. Make a difference for young people in Bardon. (21 words)
- QR: `bardonscouts.org.au/leaders/volunteering/`, labelled "Scan to find out more"

Strength: real Bardon photos, ready to use now. Weakness: the logo needs a quiet part of the photo or the panel, and the photos may be replaced later.

### Concept B: Colour me in (illustration)

The families side is a simple line drawing for the child to colour: a tent, a campfire, gum trees and a kangaroo with a joey. A Joeys dark strip at the bottom carries the details for parents. The volunteers side is Navy, with a strip of the Gumtree Graphics.

**Families side**
- Headline: **Colour me in! Then come and try Joeys.**
- Body: Ages 5 to 8. Tuesdays 6:30 - 7:30pm at 11 Bee Street, Bardon. Your first visit is free. (17 words)
- QR: `bardonscouts.org.au/join/come-and-try/`

**Volunteers side**
- Headline: **Kids aren't the only ones having fun**
- Body: Volunteer with Bardon Scouts. No experience needed, full training given. A few hours or every week: it all helps. (19 words)
- QR: `bardonscouts.org.au/leaders/volunteering/`

Strength: the child keeps it, so it stays on the fridge, and it needs no photos. Weakness: the drawing is new artwork. If it shows people in uniform, the uniforms must be correct, and the brand team should see it before printing.

### Concept C: Big words (type only)

Bold Nunito Sans Black on solid colour, with a strip of Gumtree Graphics at the foot. Families side Joeys dark, volunteers side Navy.

**Families side**
- Headline: **Play. Make. Explore. Belong.**
- Body: Joeys at Bardon Scouts, ages 5 to 8. Tuesdays 6:30 - 7:30pm, 11 Bee Street. Try it free. (17 words)
- QR: `bardonscouts.org.au/join/come-and-try/`

**Volunteers side**
- Headline: **Got a few hours? We'll teach you the rest.**
- Body: Volunteer with Bardon Scouts. Training provided, Blue Card help included. (10 words)
- QR: `bardonscouts.org.au/leaders/volunteering/`

Strength: the simplest to build within the brand rules, and the easiest to read from across a room. Weakness: it's the least appealing to a 5 year old.

**Recommendation:** the Concept B families side, with the Concept A volunteers side. The colouring side gives a child a reason to keep the flyer, and the fair photos make the volunteers side look like a real local group. Concept C is the fallback if the illustration can't be made in time.

## QR codes and where they land

Each side has its own QR code, so families and volunteers land on pages meant for them. The URL is printed under each code, so people without a camera can type it in.

| Side | Printed URL | Lands on |
|---|---|---|
| Families | `https://bardonscouts.org.au/join/come-and-try/` | Come and Try, updated |
| Volunteers | `https://bardonscouts.org.au/leaders/volunteering/` | Volunteering, updated |

A printed code can't be changed, so these two URLs must keep working while flyers are in use. If either page ever moves, add a redirect (PM-11).

Every page opens with a hero image up to 400 px tall, so on a phone the first lines of text are what a new visitor reads first. Both pages need to answer their reader's questions in those lines.

### Come and Try (`/join/come-and-try/`)

Today the page assumes the reader knows what Scouts is, and doesn't say who it's for, when, or where. Proposed wording, under 200 words:

> Your child can come to a Bardon Scouts meeting for free before you decide to join.
>
> *[Section table: section, ages, meeting day and time, from `data/sections.yaml`]*
>
> We meet at the Scout Den, 11 Bee Street, Bardon.
>
> ## How to come and try
>
> 1. **Send us a message** at least a day before. Meetings are sometimes held away from the Den, so we'll confirm where to go. **[Ask to visit](/contact/)**
> 2. **Fill in Form F6** and bring it with you: [Non-Member Activity Indemnity and Release (PDF)](/img/F6-Non-Member-Activity-Indemnity-and-Release.pdf)
> 3. **Come along** to the meeting.
>
> ## After your visit
>
> If your child would like to join, [How to Join](/join/how-to-join/) has the steps.
>
> ## Help with costs
>
> Queensland children aged 5 to 17 can get a [Play On! Sports Voucher](/join/play-on-voucher/) of up to $200 towards membership fees.

The section table can't be typed into the page, because times and ages come only from `data/sections.yaml` (`sections.md`). Proposed: a front matter flag, `showSectionTimes: true`, that makes the page template show the table, in the same way the `showForm` flags add forms. Leaders can switch it on or off in the CMS. The "Your First Night" link moves to How to Join, where it already is.

### Volunteering (`/leaders/volunteering/`)

Today the page runs to about 600 words, and the "Contact us" link is at the bottom. Proposed: a short opening that answers the scan, then the existing detail below it.

> ## Meet the Other You
>
> Volunteering with Bardon Scouts is a chance to learn new skills, get outdoors and make a difference for young people. No experience needed: we'll train you.
>
> - **Help in the way that suits you:** with a section each week, at events now and then, on the committee, or with a skill such as IT or first aid.
> - **What you need:** a Blue Card (we'll help you apply) and a willingness to learn.
>
> **[Get in touch](/contact/)** to find out more.

Below this, the existing sections stay (Why Volunteer, Roles, Time Commitment, What We Provide, Requirements). Two removals avoid saying things twice: the old opening paragraph, and the closing "Ready to Meet the Other You?" section, which the new opening replaces. The Learn More links stay.

### Contact form

`child_names` is no longer required, and its label becomes "Child's name(s), if any". The contact page already asks "Would you like to get involved?", so volunteers fit there without other changes. `docs/requirements/forms.md` is updated to match.

## Print spec

- A5 portrait, 148 x 210 mm, double-sided, with 3 mm bleed and a 5 mm safe area.
- CMYK, using the brand's CMYK values. Images at 300 dpi at print size. Final file as a print PDF from Canva.
- QR codes at least 25 mm square, dark on a white square with a quiet zone of at least 4 modules, and error correction level M or higher.
- Body text at least 11 pt, and headlines at least 28 pt, in Nunito Sans.
- The Group logo with its words at least 30 mm wide, with its clear space.

## Build steps, once a concept is chosen

1. Fix the Joeys ages on the site, then update Come and Try, Volunteering and the contact form. Publish them to production before printing (PM-1).
2. Get the Bardon Scout Group logo (the fair flyer's copy is too low resolution to print), the Joey Scouts logo and the Gumtree Graphics from the Brand Centre (needs a leader's membership login).
3. Build the flyer in Canva at A5, starting from the Scouts Queensland template if it fits.
4. Make the QR codes for the two production URLs.
5. Check against `printed-materials.md` (PM-1 to PM-5, PM-10 to PM-12), then send the proof to brandsupport@scoutsqld.com.au.
6. Order a test print and scan it (PM-4) before the full run.

## Still open

- **Which concept**: the owner is deciding.
- **Brand Centre files**: someone with a membership login needs to download the Group logo, the Joey Scouts logo and the Gumtree Graphics.
