# Contributing

This site is maintained by Bardon Scout Leaders using Claude Code, with GitHub Issues as the shared task list. Please read the [code of conduct](CODE_OF_CONDUCT.md) before contributing.

## Setup for New Collaborators

### 1. Install tools

- [Git](https://git-scm.com/downloads)
- [Hugo Extended](https://gohugo.io/installation/) v0.148.2 or later
- [GitHub CLI](https://cli.github.com/) (`gh`)
- [Claude Code](https://claude.com/claude-code)

### 2. Authenticate the GitHub CLI

```sh
gh auth login
```

Choose GitHub.com, HTTPS, and log in with your browser. Check it worked with `gh auth status`.

Your GitHub account must be a collaborator on `bardon-scouts/bardon-scouts-website` so issues can be assigned to you.

### 3. Clone and run the site

```sh
git clone https://github.com/bardon-scouts/bardon-scouts-website.git
cd bardon-scouts-website
git checkout dev
hugo server --buildFuture --buildDrafts --disableFastRender --port 1314
```

Open http://localhost:1314/.

### 4. Open Claude Code in the repository folder

Start Claude Code from the `bardon-scouts-website` folder itself (not a parent folder), so it picks up `CLAUDE.md`, `.claude/instructions.md`, and the slash commands in `.claude/commands/`.

## Workflow

GitHub Issues is the task list. Each person only works on issues assigned to them, which keeps two people (and two Claude Code sessions) from working on the same thing.

1. **Create issues** for anything that needs doing, using the Bug Report or Feature Request template on GitHub, or `/create-bug` and `/create-feature` in Claude Code.
2. **Triage** - agree who takes each issue, then assign it and set a priority label.
3. **Work** - in Claude Code, run `/my-tasks` to see your issues, then `/start-issue <number>`. Or just tell Claude "Work through my assigned GitHub issues".
4. **Complete** - `/complete-issue <number>` commits and pushes to `dev`, then checks the fix actually worked (re-checks the files, then tests the change on the deployed `dev` site, not a local build). It only closes the issue once that's confirmed. If something can't be verified, the issue stays open with the `needs-review` label.
5. **Publish** - every push to `dev` is deployed to https://dev--bardon-scouts-website.netlify.app/ for checking. Merge `dev` into `master` to publish to the live site (https://bardonscouts.org.au/).

### Checking which commit is deployed

Netlify doesn't report build status to GitHub for this repo, so check it one of these ways.

**Netlify CLI.** Log in to the Bardon Scouts Netlify account (`netlify login`, team `bardon-scouts`) and link the folder once with `netlify link --name bardon-scouts-website`. Then:

```sh
netlify api listSiteDeploys --data '{"site_id":"5134019f-f869-4cf3-91f3-a36e2acd8055","per_page":5}'
```

Each deploy shows its `branch`, `commit_ref` and `state`: `ready` means it worked, `error` means it failed (see `error_message`).

**Deploy stamp.** Every page includes a hidden `<meta name="deploy-commit">` tag with the commit it was built from:

```sh
curl -s https://dev--bardon-scouts-website.netlify.app/ | grep -oE 'deploy-commit content="?[0-9a-f]{40}'
```

If it matches `git rev-parse HEAD`, your latest push is live on the dev site.

### Claude Code slash commands

| Command | What it does |
|---|---|
| `/my-tasks` | List my open assigned issues |
| `/create-bug` | Create a bug report interactively |
| `/create-feature` | Create a feature request interactively |
| `/start-issue <number>` | Assign to me, add `in-progress`, comment "Starting work" |
| `/complete-issue <number>` | Commit, push, verify the fix, then close (or mark `needs-review`) |

The full rules Claude follows are in [.claude/instructions.md](.claude/instructions.md).

### Useful `gh` commands

```sh
gh issue list --assignee "@me" --state open      # my tasks
gh issue list --state open                        # everything open
gh issue list --search "no:assignee"             # needs triage
gh issue view 12 --comments                       # read an issue
gh issue edit 12 --add-assignee hamish-username   # assign to someone
```

### Labels

| Group | Labels | Meaning |
|---|---|---|
| Status | `in-progress`, `blocked`, `needs-review`, `ready` | Where the issue is up to |
| Type | `bug`, `enhancement`, `content`, `documentation` | What kind of change |
| Priority | `priority-high`, `priority-medium`, `priority-low` | How urgent |
| Source | `website-feedback`, `complaint`, `discovered` | Where it came from (`discovered` = found while working on something else) |

## Commit Messages

Use a short summary line, include the issue number, and add detail below a blank line if needed:

```
Update Cubs meeting time (#12)

Cubs now meet Tuesday 6:30pm. Updated the section page and homepage schedule.
```

Do not include Claude Code attribution lines. See [.claude/instructions.md](.claude/instructions.md) for content standards.
