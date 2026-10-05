---
name: verify
description: Verify a committed change on the Bardon Scouts dev site - checks the Netlify CLI is on the Bardon account, confirms the Netlify dev deploy of this exact commit succeeded, then checks the changed pages. Used by submit-for-review before an issue is handed to the owner.
argument-hint: <commit-hash> <what to check>
---

Verify commit $0 on the dev site. Things to check: $ARGUMENTS

- **Dev site:** https://dev--bardon-scouts-website.netlify.app/ (Netlify branch deploy of `dev`, rebuilt on every push)
- **Production:** https://bardonscouts.org.au/ (from `master`; never verify there)
- Never verify with a local Hugo build.

## 1. Check the Netlify account

The Netlify CLI can hold several accounts on one machine, with one active at a time. The person at the machine switches accounts when they change project; this skill only checks (see "Tool accounts" in `CLAUDE.md`).

1. Run `netlify status` and read the output, not the exit code: it exits with an error outside a linked folder even when logged in.
2. The "Teams" list must include `bardon-scouts`.
3. If it doesn't, or no user is logged in, stop: **not verified** (not a failed deploy). Tell the person to run `netlify switch` and pick the Bardon Scouts account, or `netlify login --new` with that account the first time on a machine, then run verify again. Don't switch accounts yourself.

## 2. Confirm this commit deployed

Netlify doesn't post build statuses to GitHub for this repo. Use the Netlify CLI and the deploy stamp.

1. Deploy state for the commit:

   ```
   netlify api listSiteDeploys --data '{"site_id":"5134019f-f869-4cf3-91f3-a36e2acd8055","per_page":5}'
   ```

   Find the entry whose `commit_ref` starts with $0 and `branch` is `dev`. `state` is `ready` (deployed), `building`/`enqueued` (wait and re-check, up to about 5 minutes), or `error` (failed: read `error_message`).
2. Once it's `ready`, confirm the dev site is serving it. Every page has a `deploy-commit` meta tag, and the HTML is minified, so the quotes may be missing:

   ```
   curl -s https://dev--bardon-scouts-website.netlify.app/ | grep -oE 'deploy-commit content="?[0-9a-f]{40}'
   ```

   The hash must be the full hash of $0.
3. If the deploy failed, or isn't live after about 5 minutes, stop: **not verified**. Report the error.

## 3. Check the change

Check each item on the dev site, using curl (read-only, piped only into grep and similar) or WebFetch:

- **Pages:** each changed page returns 200 (`curl -s -o /dev/null -w "%{http_code}"`) and shows the expected content.
- **Requirements:** apply the "How to check" section of each relevant file in `docs/requirements/` (e.g. an event page must also appear in the events listing, the Events menu, the home page grid and the CMS config). Report each by its test case ID, e.g. EV-1.
- **CMS:** for new or moved pages, the dev site's `/admin/config.yml` includes the file.
- **Styles or templates:** find the stylesheet link on the page (`scss/main.min.<hash>.css`), then confirm the new rules are in it.
- **Sanity-check every search:** make sure it finds something known to exist before trusting a "not found".

## 4. Report

List each check with pass or fail and the evidence (status codes, counts, what the page showed). Any failure means **not verified**. Also list anything that can't be checked this way, such as visual layout, for the reviewer to look at.
