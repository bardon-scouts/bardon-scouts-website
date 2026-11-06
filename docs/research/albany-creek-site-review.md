# Albany Creek Scout Group website review

## The question

What can the Bardon Scouts website learn from the [Albany Creek Scout Group site](https://albanycreekscouts.weebly.com/), and which ideas should we bring across? The owner decides. Parents of current and prospective members are the readers that matter.

- **Issue:** #110. It says to take no action until approved, so this report changes nothing on the site and raises no follow-up issues yet.
- **Date:** 6 November 2026
- **Effort:** a short study of one site, compared with ours

## Short answer

Bardon's site is already ahead on most things a parent needs: joining steps, first night, fees, uniforms, a single source for section details and an Ask to join button on every page. Albany Creek is ahead in four places, and all four are content rather than new features:

1. Three simple joining steps on the home page.
2. A set of plain answers to the questions new families ask.
3. Real stories of things its sections did, on the section pages.
4. Facts and prices for hiring the hall.

I recommend the first three, with the fourth once the committee can supply the facts. A photo gallery is worth having only after the photo consent rules (#23, #54) are settled. Most of the rest of the site should not be copied, because it conflicts with `docs/principles.md`.

## Findings

All Albany Creek pages were read on 6 November 2026: every page in its navigation, plus the [Committee](https://albanycreekscouts.weebly.com/committee.html) page linked from the home page. The PDFs linked from its FAQ were read too: the group FAQ, the start of the Joey Scouts FAQ and the start of the [Parent Information Pack](https://albanycreekscouts.weebly.com/uploads/5/3/8/3/53834961/parent-info-pack-march-2026v1.pdf). The Cub Scouts, Scouts and Venturers FAQ sheets were downloaded and sized, not read. Not checked: the gallery photos (counted, not viewed) and the Matterport tours (embeds seen, not opened).

### Where Albany Creek does something we don't

**Three joining steps on the home page.** The [home page](https://albanycreekscouts.weebly.com/) opens with "Step 1: Find your age group", "Step 2: Come for a free trial", "Step 3: Join the adventure", followed straight away by the five sections with their ages. Our home page has one Contact us button and lists the sections further down (`docs/requirements/home-page.md`). Backlog issue #69 ("New here?" panel) is close, but differs: it asks for three links (Come and Try, How to Join, Your First Night), not steps.

**Plain answers for new families.** Its [FAQ](https://albanycreekscouts.weebly.com/faq.html) answers six questions: can my child try first, what ages, do I need to stay, how much does it cost, what will my child do, and is Scouting safe. Our `content/join/faqs.md` answers two (parent expectations and lost property) and has a hidden TODO for more. The gap is already noted in #38. We have most of the answers on other pages: Come and Try, Fees, Your First Night ("You're welcome to stay for the meeting, but you don't have to"). "Blue Card" appears on five of our pages, but none of them answers a new parent asking whether Scouting is safe. #38's own list of missing questions overlaps with these six but isn't the same: it also has first night clothes, uniforms and camps.

**Stories of real activities.** Its [Scouts page](https://albanycreekscouts.weebly.com/scouts.html) describes a canoe journey up the Noosa River with an overnight camp at Fig Tree Point, and a first aid night organised by an Assistant Patrol Leader. Its [Cubs page](https://albanycreekscouts.weebly.com/cubs.html) describes a day of flying and model planes at Archerfield. Both list outings with the month they happen in, such as Raftarama (March) and Skillorama (September). Our section pages (`data/sections.yaml`) have general bullets such as "Fun and Games" and "Team Challenges", an empty "Program & Activities" heading on the Cub Scouts, Scouts and Venturer Scouts pages (#38; the Joey Scouts page doesn't have it), and an alphabetical list of event links. Our links are more useful for finding details, and its stories are more convincing.

**Hire facts on the page.** Its [Hall Hire page](https://albanycreekscouts.weebly.com/hall-hire.html) gives hourly rates ($30 casual, $25 regular, $10 downstairs), capacity (about 100), equipment, and a condition about licensed security. Our Hire the Den page (`content/hire-the-den.md`) gives the address and parking, then says we'll tell people the facilities, conditions and cost after they enquire.

**A gallery and a virtual tour.** Its [Gallery](https://albanycreekscouts.weebly.com/gallery.html) ("Our Adventures") has 34 images on the page, and its [Virtual Tour](https://albanycreekscouts.weebly.com/virtual-tour.html) embeds two Matterport tours of the hall, linked from Hall Hire. We have neither.

**Writing directly to teenagers.** Its [Venturers page](https://albanycreekscouts.weebly.com/venturers.html) uses questions a teenager would ask ("Won't the Leaders tell us what to do? NO!!!") and says no prior experience is needed. Our Venturer Scouts page has its own bullets and its join text speaks to teenagers ("If you're 14-18"), but the rest is a general list and it doesn't say experience isn't needed.

### Where Bardon is already ahead

- **Joining path:** Ask to join is on every page (#111), and Come and Try, How to Join, Your First Night, Fees, Uniforms and the Play On! voucher each have a page. Albany Creek's "Join the adventure" links straight to the [Scouts Queensland membership form](https://scoutsqld.com.au/membershipform/), past the free trial it has just offered.
- **Consistent facts:** ours come from one file, `data/sections.yaml`. Albany Creek's differ between pages: Scouts are 11 to 14 on the home page and 11 to 15 on the [Scouts page](https://albanycreekscouts.weebly.com/scouts.html), and Venturer Scouts are 14 to 18 on the home page and 15 to 18 on the [Venturers page](https://albanycreekscouts.weebly.com/venturers.html).
- **Section names:** we use the Scouts Queensland names throughout. Its navigation uses "Joeys" and "Cubs".
- **Events:** we have a page for each event, with a listing and a menu. It has lists on section pages only.
- **Program pages, policies and forms:** Joey Scout Programs, a Privacy Policy, Complaints and Website Feedback have no equivalent in its navigation.
- **Committee:** both pages say what the committee does and when it meets. Our "Information coming soon" role entries are the weak spot (#38), and its page doesn't help there.

## Options

Each option can be approved on its own. Effort is my estimate. Each needs a person to supply or vouch for the facts, as "Accurate, not impressive" requires.

| # | Option | Effort | What it fixes | Risk or condition |
|---|---|---|---|---|
| 1 | Three joining steps on the home page, in our order: find your section, ask to join (the request for a free trial), come along and decide. This would change #69 from three links to three steps | Small | A new parent sees how joining works straight away | Changes the order in `home-page.md`. Ask to join must come before the visit, because we confirm where to meet and families bring Form F6 (`content/join/come-and-try.md`). The steps must not lead to the Scouts Queensland form |
| 2 | Use its questions as a checklist for the FAQs, alongside #38's list, with answers in our own words that link to existing pages | Small to medium | Answers common new family questions in one place | A leader must vouch for the answers on staying and safety. Safety gets an answer only if it's specific to us, as "Short and specific" rules out generic safety text. Ages link to the section pages rather than being copied (`sections.md`). Cost answers must not give payment methods or timing |
| 3 | Real activity stories on section pages: two or three short ones each, filling or replacing the empty heading where there is one, plus the month beside recurring events | Medium | Section pages say what this group actually does | Needs leaders to supply stories. Photos and names need the consent rules (#23). Months are safer than dates, which go stale (#33) |
| 4 | Hire the Den facts: capacity, equipment, conditions and, if the committee agrees, rates | Small | Fewer enquiries that go nowhere, and fewer repeat questions for the committee | Needs committee approval. Rates need keeping current |
| 5 | Photo gallery of Bardon Scouts adventures | Medium | Shows real young people on real adventures, and helps #39 | Wait for #23 and #54. Must be editable in the CMS |
| 6 | Venturer Scouts page written partly for teenagers, saying no experience is needed | Small | Gives a 14 year old a reason to come | The join text already speaks to teenagers, so this goes further the same way. How far is the owner's call under "Parents first" |
| 7 | Virtual tour of the Den | Unknown | Helps hirers and nervous families see the space | Needs a capture and hosting. Matterport's price not checked |
| 8 | Do nothing | None | Nothing: the FAQ and section page gaps stay as #38 describes | None |

### What not to copy

- **Promise, Law, Scout history, "Famous Scouts" and national videos** ([home](https://albanycreekscouts.weebly.com/), [About](https://albanycreekscouts.weebly.com/about.html)): the three YouTube videos are Scouts Australia's. "Short and specific" rules out generic sections that could appear on any Scout site.
- **The Group Leader's email address** ([About](https://albanycreekscouts.weebly.com/about.html), [Contact](https://albanycreekscouts.weebly.com/contact.html)): "Don't publish leaders' contact details" rules this out.
- **PDF FAQ sheets for each section** ([FAQ](https://albanycreekscouts.weebly.com/faq.html)): PDFs can't be edited in the CMS, so they'd fail "Leaders can maintain it". What they hold also conflicts with our principles: the [group FAQ](https://albanycreekscouts.weebly.com/uploads/5/3/8/3/53834961/faqs_group.pdf) gives the invoice timing (four weeks to pay), which "Protect families from scams" rules out, and a leader's email, and the [Joey Scouts FAQ](https://albanycreekscouts.weebly.com/uploads/5/3/8/3/53834961/faqs_joey_scouts.pdf) names its leaders.
- **An enquiry form on each section page:** our one Ask to Join form, with a button on each section page, keeps one place to maintain.

## Recommendation

Approve options 1 and 2 now. They're small, need little new content and close gaps already on our backlog. Approving them means moving #69 out of Backlog with its links changed to these steps (or keeping #69's links if you prefer), and doing the FAQ part of #38 with both lists of questions.

Approve option 3 next, starting with one section, if a leader can supply two or three stories. It's the option most specific to Bardon: general bullets could be on any group's site, and these stories couldn't.

Ask the committee about option 4. Leave option 5 until #23 and #54 are settled. Decide option 6 as a question of who the Venturer Scouts page is for. Skip option 7 unless a hirer or parent asks for it: it's the option with the least evidence behind it.

**What would change this:** enquiries showing parents don't ask about these things would lower option 2, and leaders being unable to supply stories would drop option 3. A decision that the site should also speak to teenagers would raise option 6.
