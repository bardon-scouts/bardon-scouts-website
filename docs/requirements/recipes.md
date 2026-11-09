# Recipes

## What it's for

A shared collection of camp recipes that leaders keep in Sveltia CMS, and that anyone can pick from and print as their own cookbook for a camp (#117). Scaling recipes to the number of people is planned in #118.

## Requirements

### Content

- One file per recipe, `content/recipes/<slug>.md`, edited in the CMS's **Recipes** collection (`static/admin/config.yml`), which saves to `master` through the editorial workflow like other content.
- Front matter: `title`, `description` (optional, one line), `tags` (free-form list), `servings`, `prepTime`, `cookTime`, `methods` (Cooked on: a fixed list in the CMS), `dietary` (free-form list), `image` (optional) and `ingredients`. The method is the Markdown body.
- Each ingredient has `quantity` (number, optional), `unit` (optional, from the CMS's fixed list: tsp, tbsp, cup, ml, L, g, kg, pinch, handful, can, packet, jar, bunch, clove, slice), `name` (singular), `plural` (optional, only where it isn't the name plus "s"), `note` (optional) and `group` (optional heading such as "Sauce"; rows in a group sit next to each other). These fields are what scaling (#118) will use, so don't replace them with one line of text.
- Ingredients are shown as written: halves, quarters, thirds and three-quarters as fractions (0.5 as ½), the unit made plural where it reads that way (2 cups, 3 cans), whole items made plural (2 onions, or the plural name), and the note after a comma. An ingredient with no amount ("salt and pepper, to taste") is shown with no number.
- The method is written without amounts ("add the stock"), so it still reads right once recipes can be scaled. The leaders' guide is `docs/training/entering-recipes.md`.
- Recipes are public, so they follow `docs/principles.md` and `content-standards.md`: no leaders' names or contact details, and no photos where children can be identified. Dietary notes are general information, and the Recipes page says to check allergies for your own group.
- Tags are free-form, so new kinds of recipe (such as fundraiser recipes) need no code change. Nothing in the layouts or URLs says "camp".
- No recipe may have the slug `print`, which is the cookbook page's address. The build stops with an error if one does (`layouts/recipes/list.html`), so the live site keeps its last good version until the recipe is renamed.

### Recipes page and recipe pages

- `/recipes/` (`content/recipes/_index.md`, `layouts/recipes/list.html`) lists every recipe by title, each with an "Add to cookbook" checkbox, its serves, times, cooking methods, dietary notes and tags.
- A tag filter shows only the recipes with a tag. It runs in the browser, because tag pages are turned off (`disableKinds`, #67) and stay off. "Select all shown" adds the recipes currently shown to the cookbook.
- Each recipe page, `/recipes/<slug>/` (`layouts/recipes/single.html`), shows the recipe and an "Add to cookbook" button that becomes "Remove from cookbook" once added.
- The picked recipes are kept in the browser's `localStorage` (key `bardon-cookbook`), so nothing is sent to a server.
- The Recipes page is in the menu under Skills.

### Cookbook print page

- `/recipes/print/` (`content/recipes-print.md`, `layouts/_default/cookbook.html`) shows the picked recipes, in the order they were picked, read from `/recipes/index.json` (`layouts/recipes/list.json`). It has a "Print / Save as PDF" button and a short note on choosing "Save as PDF" in the print dialog.
- With no recipes picked it shows a message saying how to pick some, not a blank page.
- The PDF comes from the browser's print dialog. JS PDF libraries aren't used, as they cut pages at arbitrary points.
- Printing (`assets/scss/_print.scss`, shared with any later printable collection such as an activities catalogue): A4 with margins, no navbar or footer, each recipe kept on one page where it fits so short recipes share pages, headings kept with what follows, and images no wider than the page.
- A recipe taller than one printed page gets the `long` class (`assets/js/recipes.js`, measured at the printed width) and flows across pages instead of leaving a gap.
- The printout carries "Bardon Scouts cookbook" and `bardonscouts.org.au/recipes/` in its heading, and Chrome also prints the name and address at the foot of each page. No logos are added, so the brand rules in `printed-materials.md` don't apply. If a logo is ever added, they do.

## How to check

On the dev site:
- **RC-1:** `/recipes/` returns 200 and lists every file in `content/recipes/` except `_index.md`, each with a checkbox. The menu's Skills dropdown links to it.
- **RC-2:** Each recipe page returns 200 and shows its serves, times, methods, dietary notes, ingredients as written (groups as headings, fractions, plurals, no number for an ingredient with no amount) and method.
- **RC-3:** `/recipes/index.json` returns 200, is valid JSON, and has one entry per recipe with its structured ingredients, each with a `text` line matching the recipe page.
- **RC-4:** On `/recipes/`, choosing a tag shows only recipes with that tag; "Select all shown" picks only those; the cookbook count matches. "Add to cookbook" on a recipe page adds it, and the count on the list agrees.
- **RC-5:** `/recipes/print/` with nothing picked shows the empty message and a disabled Print button. With recipes picked it shows them in order.
- **RC-6:** A print to PDF of the cookbook (A4) has no navbar or footer, keeps each short recipe on one page with short recipes sharing pages, and lets a recipe taller than a page (`.long`) flow across pages. Images fit the page width.
- **RC-7:** The dev site's `/admin/config.yml` has the Recipes folder collection with the fields above, and file entries for `content/recipes/_index.md` and `content/recipes-print.md`.

For a person (the reviewer):
- **RC-8:** Open the Recipes collection in the CMS on the dev site: the fields load, and adding an ingredient row is quick. Don't publish a test recipe: the CMS saves to `master`, so it would reach the live site.
- **RC-9:** Print preview of a cookbook of three or more recipes in Chrome, Safari and a phone browser: short recipes share pages, long ones break cleanly.
