# Image prompts

Prompts for an image generator (such as Leonardo) for every page that shows the Scouts Australia logo as its hero image. Written for #59.

## How to use them

1. Add the **shared style** below to the end of each prompt.
2. Generate the image at 3:1 landscape, at least 2400 x 800 pixels.
3. Save it as JPG under the filename given, in `static/img/` (or upload it through the CMS with that name).
4. For pages marked **set the image**, also change the page's `image:` to the new file, in the CMS or by an issue. Event pages already point at their filename, so saving over the old file is enough.

## Adding an image

Tested with Clean Up Australia Day (#59).

1. **Check the shape.** The hero needs a 3:1 image. If the generator gives a square or other shape (Leonardo's default is 1024 x 1024), crop it to 3:1 around the subject, keeping the subject on the left or centre. Otherwise the page shows only the top of the image.
2. **Check the right-hand third.** The page title covers it. If the subject is on the right, mirror the image (only if it has no text).
3. **Add it,** either way:
   - **Ask Claude:** attach the image to an issue comment and say which page it's for. Claude crops it if needed, saves it and checks it on the dev site.
   - **In the CMS:** open the page, choose its image and upload the file. For event pages, use the filename given below so it replaces the old file. CMS changes go straight to the live site (see `CLAUDE.md`), so crop the image first.

**Shared style:** *Natural light, South East Queensland bush or suburban setting, realistic colours. Keep the main subject in the left and centre and leave the right third simple and uncluttered. No text, no words, no logos, no badges, no uniforms, no recognisable faces.*

**Why the shape and the right-hand space:** the hero is cropped from the top left to at most 400 pixels tall across the full page width, and the page title sits over the right-hand side.

**Why no faces or uniforms:** there's no requirement yet on AI images (#54). Until it's decided, these prompts avoid anything that could pass for a photo of Bardon members. People appear only as hands or distant figures seen from behind. Where a real photo would be more honest (the Den, the group's history, our leaders, uniforms), the entry says so.

## Events

All the event pages below now have their own image (#59). To change one, save the new image over its file.

### ANZAC Day March - `/anzac-day-march/`
File: `/img/anzac-day-march.jpg`. Done (#59).

> A wreath of red poppies and rosemary resting at the base of a sandstone war memorial at dawn, soft pink sky, dew on the grass.

### Annual Report Presentation - `/annual-report-presentation/`
File: `/img/annual-report-presentation.jpg`. Done (#59).

> Rows of folding chairs in a timber community hall in the evening, a trestle table at the front with a stack of printed reports and a tray of tea cups, warm lights.

### Clean Up Australia Day - `/clean-up-australia-day/`
File: `/img/clean-up-australia-day.jpg`. Done (#59).

> Gloved hands dropping a plastic bottle into a rubbish bag beside a creek bank lined with gum trees, morning light.

### Cuboree - `/cuboree/`
File: `/img/cuboree.jpg`. Done (#59), using the official Cuboree 2026 logo.

> A large open camp field filled with rows of tents and colourful flags on poles at dusk, campfire smoke drifting, distant figures seen from behind.

### District Camps - `/district-camps/`
File: `/img/district-camps.jpg`. Done (#59).

> A cluster of tents among tall eucalyptus trees, a camp kitchen table with billies and enamel mugs in the foreground, late afternoon light.

### District Swimming - `/district-swimming/`
File: `/img/district-swimming.jpg`. Done (#59).

> An outdoor swimming pool from the end of the lanes, lane ropes and starting blocks, kickboards stacked on the edge, bright sunny day.

### KnightMoves - `/knightmoves/`
File: `/img/knightmoves.jpg`. Done (#59).

> At night, a compass and a paper map lit by a head torch on the grass, distant city lights on the horizon.

### Operation NightHawk - `/operation-nighthawk/`
File: `/img/operation-nighthawk.jpg`. Done (#59), using the official Operation NightHawk logo.

> A line of small head torch lights winding across dark rolling farmland on the Darling Downs under a starry sky.

### Pizza and Paddle - `/pizza-and-paddle/`
File: `/img/pizza-and-paddle.jpg`. Done (#59).

> Canoes pulled up on a grassy riverbank at sunset with paddles and life jackets beside them, pizza boxes on a picnic table in the foreground.

### Rock Climbing - `/rock-climbing/`
File: `/img/rock-climbing.jpg`. Done (#59).

> An indoor climbing wall with colourful holds seen from below, a rope running up the wall and a chalk bag hanging in the foreground.

### Skillorama - `/skillorama/`
File: `/img/skillorama.jpg`. Done (#59).

> A showground on a sunny day set up with activity bases: small marquees, a low rope bridge, hay bales and buckets, distant figures seen from behind.

### Air Activities - `/air-activities/`
File: `/img/air-activities.jpg`. Done (#59).

> A small glider sitting on a grass airfield in the early morning, windsock in the background, clear blue sky.

### Fishing - `/fishing/`
File: `/img/fishing.jpg`. Done (#59).

> Two fishing rods leaning on a timber jetty railing over calm water at sunrise, an open tackle box and a bucket on the boards.

### Group Camp - `/group-camp/`
File: `/img/group-camp.jpg`. Done (#59).

> A bush campsite in spring with several tents around a campfire circle of logs, jacaranda and gum trees, golden evening light.

## Join Us

### Join Us - `/join/`
File: `/img/join.jpg`, **set the image** (this page has no `image:` yet)

> A pair of hiking boots and a water bottle on the timber step of a hall, a bush track leading away in the background.

### Welcome Pack - `/welcome/`
File: `/img/welcome.jpg`, **set the image**

> Top-down view of a wooden table with a day pack, a folded map, a compass, a torch and a water bottle laid out neatly.

### Your First Night - `/join/first-night/`
File: `/img/first-night.jpg`, **set the image**

> A pair of closed-in shoes, a water bottle and a folded jumper by the open door of a timber hall at dusk, warm light inside.

### How to Join - `/join/how-to-join/`
File: `/img/how-to-join.jpg`, **set the image**

> A winding bush track with stepping stones leading toward a sunlit clearing.

### Fees & Costs - `/join/fees/`
File: `/img/fees.jpg`, **set the image**

> A small glass jar of coins beside a compass and a folded map on a wooden table.

### Uniforms - `/join/uniforms/`
File: `/img/uniforms.jpg`, **set the image**. A real photo of a Bardon uniform would be better: generators get Scout uniforms wrong.

> A wide-brimmed hat, a coiled rope and a day pack hanging on wooden pegs in a hall.

### Come and Try - `/join/come-and-try/`
File: `/img/come-and-try.jpg`, **set the image**

> The open double doors of a timber hall at dusk with warm light spilling onto the path, gum trees around it.

### Play On! Voucher - `/join/play-on-voucher/`
File: `/img/play-on-voucher.jpg`, **set the image**

> A pair of hiking boots and a small backpack on the grass at the start of a bush trail, morning light.

### New Family FAQs - `/join/faqs/`
File: `/img/faqs.jpg`, **set the image**

> A wooden signpost in the bush with blank arrows pointing in several directions.

### Taking a Break or Finishing Up - `/join/taking-a-break/`
File: `/img/taking-a-break.jpg`, **set the image**

> An empty hammock strung between two gum trees in soft afternoon light.

## About

### About - `/about/`
File: `/img/about.jpg`, **set the image**

> A campfire in a bush clearing at dusk, logs arranged around it, tall eucalyptus trees against an orange sky.

### Our History - `/history/`
File: `/img/history.jpg`, **set the image**. An old photo of the group would be better, if one can be found.

> A sepia-toned photograph of an old canvas tent with wooden poles and pegs in a paddock, in the style of the 1920s.

### Group Structure - `/group-structure/`
File: `/img/group-structure.jpg`, **set the image**

> A tall pioneering tower made of timber poles and rope lashings against a blue sky.

### Hire the Den - `/hire-the-den/`
File: `/img/hire-the-den.jpg`, **set the image**. A real photo of the Den would be better, since people hiring it need to see the actual hall.

> The inside of an empty community hall with a polished timber floor, stacked chairs and folding tables, daylight through the windows.

### Calendar - `/calendar/`
File: `/img/calendar.jpg`, **set the image**

> A paper planner open at blank pages with a pencil and a compass on a wooden table, a window with gum trees behind.

### Committee - `/committee/`
File: `/img/committee.jpg`, **set the image**

> A meeting table with notebooks, pens and mugs of tea under warm evening light.

### Consent2go - `/consent2go/`
File: `/img/consent2go.jpg`, **set the image**

> A tablet with a softly glowing blank screen on a picnic table beside a day pack, outdoors.

### Sign In and Out - `/sign-in-out/`
File: `/img/sign-in-out.jpg`, **set the image**

> A clipboard with a blank sheet and a pen on a string hanging beside the door of a hall at dusk.

### Code of Conduct - `/code-of-conduct/`
File: `/img/code-of-conduct.jpg`, **set the image**

> Hands of adults and children stacked together in the middle of a circle, seen from above, on grass.

### Phone Use Policy - `/phone-use/`
File: `/img/phone-use.jpg`, **set the image**

> A basket of mobile phones lying face down on a table, with a blurred campfire glowing in the background.

### Communication - `/communication/`
File: `/img/communication.jpg`, **set the image**

> A mobile phone with a blank screen on a camp table beside an enamel mug and a torch.

### Terrain - `/terrain/`
File: `/img/terrain.jpg`, **set the image**

> A topographic map with contour lines, a compass and a pencil marking a route, on a groundsheet in the bush.

## Help Us!

### Help Us! - `/leaders/`
File: `/img/help-us.jpg`, **set the image** (this page has no `image:` yet)

> Many hands gripping a thick rope together, pulling in the same direction, on grass.

### Our Leaders - `/leaders/our-leaders/`
File: `/img/our-leaders.jpg`, **set the image**. A real group photo of the leaders (with their permission) would be better.

> A lit lantern on a camp table at dusk with tents in the background.

### Volunteering - `/leaders/volunteering/`
File: `/img/volunteering.jpg`, **set the image**

> Close-up of an adult's hands showing a child's hands how to tie a knot in a rope.

### Parent Roster - `/leaders/parent-roster/`
File: `/img/parent-roster.jpg`, **set the image**

> A trestle table in a hall set with a tea urn, cups and a plate of biscuits, ready for a meeting.

### Adult Supporters - `/leaders/adult-supporters/`
File: `/img/adult-supporters.jpg`, **set the image**

> Adult hands lashing two timber poles together with rope.

### Friends of Bardon Scouts - `/leaders/friends/`
File: `/img/friends.jpg`, **set the image**

> Timber benches around a campfire in the evening, smoke rising into the trees.

### Containers for Change - `/containers-for-change/`
File: `/img/containers-for-change.jpg`, **set the image**

> Plastic crates full of empty aluminium cans and plastic drink bottles, sorted and ready for recycling.

## Skills

### Scouting Skills - `/skills/`
File: `/img/skills.jpg`, **set the image**

> Flat lay on a groundsheet of a compass, coiled rope, first aid kit, map and a canoe paddle.

### Bushwalking - `/skills/bushwalking/`
File: `/img/skills-bushwalking.jpg`, **set the image**

> A narrow walking track through Queensland eucalypt forest, dappled sunlight, hiking boots on the track in the foreground.

### Campcraft - `/skills/campcraft/`
File: `/img/skills-campcraft.jpg`, **set the image**

> A small tent pitched in a bush clearing with a billy hanging over a small campfire.

### First Aid - `/skills/first-aid/`
File: `/img/skills-first-aid.jpg`, **set the image**

> An open first aid kit on a groundsheet outdoors with bandages, a triangular bandage and a water bottle.

### Pioneering - `/skills/pioneering/`
File: `/img/skills-pioneering.jpg`, **set the image**

> Close-up of a square lashing joining two timber poles with natural rope.

### Water Activities - `/skills/water-activities/`
File: `/img/skills-water-activities.jpg`, **set the image**

> Canoes on a calm river with paddles across them and life jackets on the bank, morning mist.

## Other pages

### News & Updates - `/news/`
File: `/img/news.jpg`, **set the image** (this page has no `image:` yet)

> A cork noticeboard with blank photo prints and pins, in a timber hall.

### Rovers - `/sections/rovers/`
File: `/img/rovers.jpg`, **set the image** (this page has no `image:` yet)

> Two young adults with large hiking packs walking along a mountain ridge at sunrise, seen from behind at a distance.

### Contact Us - `/contact/`
File: `/img/contact.jpg`, **set the image**

> A timber letterbox on a post at a gate, gum trees behind it, afternoon light.

### Complaints - `/complaints/`
File: `/img/complaints.jpg`, **set the image**

> A notebook and pen beside a cup of tea on a table by a window, calm morning light.

### Website Feedback - `/website-feedback/`
File: `/img/website-feedback.jpg`, **set the image**

> A laptop on a wooden table with a blank web page on the screen and a compass beside it.

### Thank-you pages - `/contact/thanks/`, `/complaints/thanks/`, `/website-feedback/thanks/`, `/hire-the-den/thanks/`
File: `/img/thank-you.jpg`, **set the image** on all four

> A single tent in a bush campsite under a warm sunset.
