---
name: verify
description: Verify a committed change on the Bardon Scouts dev site - confirms the dev site is serving this commit (or a later one containing it) from its deploy stamp, with no Netlify login, then checks the changed pages. Used by submit-for-review before an issue is handed to the owner.
argument-hint: <commit-hash> <what to check>
---

Verify commit $0 on the dev site. Things to check: $ARGUMENTS

- **Dev site:** https://dev--bardon-scouts-website.netlify.app/ (Netlify branch deploy of `dev`, rebuilt on every push)
- **Production:** https://bardonscouts.org.au/ (from `master`; never verify there)
- Never verify with a local Hugo build.

## 1. Confirm this commit deployed

Netlify doesn't post build statuses to GitHub for this repo, so the check uses the dev site's deploy stamp: every page has a `deploy-commit` meta tag with the commit it was built from. It needs no Netlify login, so the account the Netlify CLI is on doesn't matter.

```
python scripts/check_deploy.py $0
```

It passes when the stamp is $0 or a later commit that contains it (`git merge-base --is-ancestor`): a commit pushed together with a later one gets no deploy of its own. It retries for about 5 minutes while the build runs.

If it says **Not verified**, stop: the stamp didn't arrive in time, and the build may have failed. Report it, and say that someone needs to open the Netlify dashboard (site `bardon-scouts-website`, Deploys) to see why.

## 2. Check the change

Check each item on the dev site, using curl (read-only, piped only into grep and similar) or WebFetch:

- **Pages:** each changed page returns 200 (`curl -s -o /dev/null -w "%{http_code}"`) and shows the expected content.
- **Requirements:** apply the "How to check" section of each relevant file in `docs/requirements/` (e.g. an event page must also appear in the events listing, the Events menu, the home page grid and the CMS config). Report each by its test case ID, e.g. EV-1.
- **CMS:** for new or moved pages, the dev site's `/admin/config.yml` includes the file.
- **Styles or templates:** find the stylesheet link on the page (`scss/main.min.<hash>.css`), then confirm the new rules are in it.
- **Sanity-check every search:** make sure it finds something known to exist before trusting a "not found".
- **Browsers and phones:** for each changed page, run the shared browser check. It opens the page in Chromium, Firefox and WebKit and on an emulated iPhone and Android, and checks it loads without errors, has no sideways scroll, fits the phone's width, has readable text, and that buttons react to hover and press and Tab moves a visible focus:

  ```
  python ../lvluplabs_operations/scripts/browser_check.py https://dev--bardon-scouts-website.netlify.app --page <changed page>
  ```

  `<changed page>` is the path, such as `/` or `/events/`. Run it with the PowerShell tool: Git Bash turns a path starting with `/` into a Windows folder, and the check then opens the wrong address. It exits 1 if any check fails; report the failures. Lines marked NOTE, such as tap targets under 44 pixels, are not failures: list them for the reviewer.

## 3. Report

List each check with pass or fail and the evidence (status codes, counts, what the page showed). Any failure means **not verified**. Also list anything that can't be checked this way, such as visual layout, for the reviewer to look at.
