# Testing

How changes to the site are tested, and what has to be checked by a person.

## Testing a change

Every change is tested on the dev site after it deploys, never with a local build.

1. **Netlify dev deploy.** Every push to `dev` builds and deploys to https://dev--bardon-scouts-website.netlify.app/. A failed build shows in the Netlify dashboard's deploy list with an error message, which needs a Netlify login. Nothing else in testing does.
2. **Deploy stamp.** Every page has `<meta name="deploy-commit" content="...">`, the commit it was built from. A check only counts once the dev site shows the hash of the commit being tested, or of a later commit that contains it (a commit pushed together with a later one gets no deploy of its own). `scripts/check_deploy.py <commit>` waits up to about 5 minutes for this, with no Netlify login.
3. **`verify` skill** (`.claude/skills/verify/SKILL.md`). Claude uses it before handing an issue over: it confirms the dev site is serving the commit (with `scripts/check_deploy.py`), then checks the changed pages, the relevant test cases and the shared browser check (see "What a person checks").
4. **`style-check`** (lvlup-workflow plugin). Run on any changed prose. It must report 0 errors.

## Test cases

Test cases live in the requirements, not here. Each file in `docs/requirements/` ends with a "How to check" section, and each item has an ID so issues and test reports can refer to it:

| Prefix | File |
|---|---|
| CS | `content-standards.md` |
| EV | `event-pages.md` |
| FM | `forms.md` |
| HP | `home-page.md` |
| NP | `news-posts.md` |
| PN | `pages-and-navigation.md` |
| PM | `printed-materials.md` |
| RC | `recipes.md` |
| SE | `sections.md` |

When a requirement changes, update its test cases in the same commit. Give new test cases the next number and don't reuse old ones.

## Whole-site check

Run before publishing `dev` to `master`. Leaders' CMS edits go straight to `master` without passing through `dev`, so this catches problems a single change's tests wouldn't.

```
python scripts/site_check.py
```

It checks the dev site by default; pass another base URL to check a different deploy. It uses only the Python standard library and exits 1 if anything fails. It checks that:

1. every page linked from the site, starting at the home page and including every menu link, returns 200 and links to `/ask-to-join/` and `/privacy/` (PN-5)
2. every old URL in `static/_redirects` reaches its new page
3. the deployed CMS config (`/admin/config.yml`) has an entry for every page in `content/`
4. the contact, trial visit, website feedback, complaints and hire enquiry forms are on their pages

## What a person checks

The `verify` skill runs the shared browser check (`../lvluplabs_operations/scripts/browser_check.py`, from the lvluplabs_operations repository) on each changed page. It covers Chromium, Firefox, WebKit and emulated iPhone and Android screens: errors, sideways scroll, fitting the phone's width, text size, hover and press on buttons, and keyboard focus. It lists tap targets under 44 pixels as a note, not a failure, as no size is set yet (lvlup-labs/lvluplabs_operations#261).

What it can't test, the reviewer of the issue (the owner) checks on the dev site when a change affects it.

| What | How |
|---|---|
| Visual layout | The browser check covers emulated phones. For a big visual change (a new page design, a style change across the site), also open the changed pages on a real phone and a desktop. Check headings, images, menus and spacing look right. |
| Editing in Sveltia CMS | Log in at `/admin/` on the dev site and open the changed entry. Check its fields load and the preview looks right. Don't publish a test edit: the CMS saves to `master`, so it would reach the live site. |
| Form submissions | Submit the changed form on the dev site with a name such as "Test", then check it appears in the Netlify site's Forms list and delete it there. |
