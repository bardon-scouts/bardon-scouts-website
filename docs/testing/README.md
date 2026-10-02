# Testing

How changes to the site are tested, and what has to be checked by a person.

## Testing a change

Every change is tested on the dev site after it deploys, never with a local build.

1. **Netlify dev deploy.** Every push to `dev` builds and deploys to https://dev--bardon-scouts-website.netlify.app/. A failed build shows in the Netlify deploy list with an error message.
2. **Deploy stamp.** Every page has `<meta name="deploy-commit" content="...">`, the commit it was built from. A check only counts once the dev site shows the hash of the commit being tested.
3. **`verify` skill** (`.claude/skills/verify/SKILL.md`). Claude uses it before handing an issue over: it confirms the deploy of the exact commit, then checks the changed pages and the relevant test cases.
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
| SE | `sections.md` |

When a requirement changes, update its test cases in the same commit. Give new test cases the next number and don't reuse old ones.

## Whole-site check

Run before publishing `dev` to `master`. Leaders' CMS edits go straight to `master` without passing through `dev`, so this catches problems a single change's tests wouldn't.

```
python scripts/site_check.py
```

It checks the dev site by default; pass another base URL to check a different deploy. It uses only the Python standard library and exits 1 if anything fails. It checks that:

1. every page linked from the site, starting at the home page and including every menu link, returns 200
2. every old URL in `static/_redirects` reaches its new page
3. the deployed CMS config (`/admin/config.yml`) has an entry for every page in `content/`
4. the contact, website feedback and complaints forms are on their pages

## What a person checks

These can't be tested automatically. The reviewer of the issue (the owner) checks them on the dev site when a change affects them.

| What | How |
|---|---|
| Visual layout | Open the changed pages on a phone and a desktop. Check headings, images, menus and spacing look right. |
| Editing in Sveltia CMS | Log in at `/admin/` on the dev site and open the changed entry. Check its fields load and the preview looks right. Don't publish a test edit: the CMS saves to `master`, so it would reach the live site. |
| Form submissions | Submit the changed form on the dev site with a name such as "Test", then check it appears in the Netlify site's Forms list and delete it there. |
