# Contributing

This site is maintained by Bardon Scout Leaders using Claude Code, with GitHub Issues as the shared task list. Please read the [code of conduct](CODE_OF_CONDUCT.md) before contributing.

## How we work

The process (GitHub Issues, testing before review, writing style, commit rules) comes from the **lvlup-workflow** Claude Code plugin, which this project enables in `.claude/settings.json`. Its README, in [lvlup-labs/lvlup-workflow](https://github.com/lvlup-labs/lvlup-workflow), explains the process and the commands in full.

In short:

1. **Create an issue** for anything that needs doing (GitHub's Bug Report or Feature Request template, or `/create-bug` / `/create-feature` in Claude Code), and assign it.
2. **Claude works on it:** ask Claude to "work through my issues", or run `/start-issue <number>`. Claude tests the result on the dev site, posts a summary on the issue, and adds the **`needs-review`** label.
3. **You review it** on the dev site:
   - **Acceptable:** close the issue.
   - **Not acceptable:** comment with what needs to change, then **remove `needs-review`** to hand it back to Claude.

Claude never closes issues. To see what's waiting on you, use [open issues labelled `needs-review`](https://github.com/bardon-scouts/bardon-scouts-website/issues?q=is%3Aopen+label%3Aneeds-review) or `/review-queue`.

## Setup for new collaborators

1. **Access.** You need write access to this repository, and read access to the private plugin repository `lvlup-labs/lvlup-workflow`. Ask Anthoney for both.
2. **Install:** [Git](https://git-scm.com/downloads), [GitHub CLI](https://cli.github.com/), [Claude Code](https://claude.com/claude-code) and Python 3. On Windows, Git for Windows provides the Git Bash that Claude Code's hooks need.
3. **Log in to GitHub** so Claude Code can download the private plugin:

   ```sh
   gh auth login
   gh auth setup-git
   ```

4. **Clone** and switch to `dev`:

   ```sh
   git clone https://github.com/bardon-scouts/bardon-scouts-website.git
   git -C bardon-scouts-website checkout dev
   ```

5. **Open Claude Code in the `bardon-scouts-website` folder itself**, not a parent folder, so it finds this project's settings and docs. The plugin installs in the background. **Reload once** (VS Code: Developer: Reload Window; terminal: restart), and it's active.
6. **Optional, for checking deploys:** the [Netlify CLI](https://docs.netlify.com/cli/get-started/), logged in to the Bardon Scouts Netlify team, with `netlify link --name bardon-scouts-website` run once in the folder.

## This project

- **Docs:** `docs/principles.md` (what matters on this site) and `docs/requirements/` (content standards, event pages, pages and navigation, sections, home page). Claude reads these; please keep them current when things change.
- **Branches:** work on `dev`, which deploys to https://dev--bardon-scouts-website.netlify.app/. Merging `dev` into `master` publishes to https://bardonscouts.org.au/. The CMS currently saves straight to `master` (see [#14](https://github.com/bardon-scouts/bardon-scouts-website/issues/14)).
- **Checking a change:** Claude uses the `verify` skill (`.claude/skills/verify/SKILL.md`), which confirms the Netlify deploy of a commit and then checks the pages on the dev site.
- **Extra labels** on top of the plugin's standard ones: `content` (text or page changes), `website-feedback` and `complaint` (where an issue came from).
