# Contributing

This site is maintained by Bardon Scout Leaders using Claude Code, with GitHub Issues as the shared task list. Please read the [code of conduct](CODE_OF_CONDUCT.md) before contributing.

## How we work

The process (creating and approving issues, Claude's work and testing, your review, writing style, commit rules) comes from the **lvlup-workflow** Claude Code plugin, which this project enables in `.claude/settings.json`. Its README, in [lvlup-labs/lvlup-workflow](https://github.com/lvlup-labs/lvlup-workflow), explains the process, the commands and the one-time setup for each computer.

## Setup for new collaborators

1. **Access.** You need write access to this repository, and read access to the private plugin repository `lvlup-labs/lvlup-workflow`. Ask Anthoney for both.
2. **Set up your computer** as described in the plugin README ("One-time setup per machine"), and install [Claude Code](https://claude.com/claude-code).
3. **Clone** and switch to `dev`:

   ```sh
   git clone https://github.com/bardon-scouts/bardon-scouts-website.git
   git -C bardon-scouts-website checkout dev
   ```

4. **Open Claude Code in the `bardon-scouts-website` folder itself**, not a parent folder, so it finds this project's settings and docs. The plugin installs in the background; reload once and it's active.
5. **Optional, for checking deploys:** the [Netlify CLI](https://docs.netlify.com/cli/get-started/), logged in to the Bardon Scouts Netlify team, with `netlify link --name bardon-scouts-website` run once in the folder.

## This project

- **Docs:** `docs/principles.md` (what matters on this site) and `docs/requirements/` (content standards, event pages, pages and navigation, sections, home page). Claude reads these; please keep them current when things change.
- **Branches:** work on `dev`, which deploys to https://dev--bardon-scouts-website.netlify.app/. Merging `dev` into `master` publishes to https://bardonscouts.org.au/. The CMS currently saves straight to `master` (see [#14](https://github.com/bardon-scouts/bardon-scouts-website/issues/14)).
- **Checking a change:** Claude uses the `verify` skill (`.claude/skills/verify/SKILL.md`), which confirms the Netlify deploy of a commit and then checks the pages on the dev site.
- **Extra labels** on top of the plugin's standard ones: `content` (text or page changes), `website-feedback` and `complaint` (where an issue came from).
- **Issues waiting on you:** [open issues labelled `needs-review`](https://github.com/bardon-scouts/bardon-scouts-website/issues?q=is%3Aopen+label%3Aneeds-review).
