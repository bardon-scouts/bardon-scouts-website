"""Find open issues stuck at a working stage and hand them to the owner.

An issue is stuck when it's at a working stage (Build or Test) and nothing has
happened on it (a comment, commit reference, label, stage or other change) for --days days
(default 7), so nothing in the workflow is moving it (lvlup-labs/lvluplabs_operations#419).
Issues that wait on purpose are left alone: labelled blocked or manual, a recurring task already
labelled overdue (the recurring tasks check told the owner), or with a Start date
after today. Triage, Backlog, Question, Review and Done aren't working stages.

For each stuck issue, once, in this order:
- comment: how long it's been idle, who takes its stage in this project, and what the owner can do
- set its stage to Question, so it's listed for the owner (review-queue)
- add the stuck label

A failure on one issue is reported and the run goes on to the next, then fails, so it's noticed.

A paused project ("paused" in .claude/lvlup-workflow.json, as queue.py reads it) is left alone,
as no work is taken there until it resumes: every project has this automation, paused ones
included (lvlup-labs/lvluplabs_operations#419).

It isn't actioned again while it's in Question. Once the owner moves it on (back to a working
stage, with their answer as feedback), the next run takes the label off, and it's stuck again
only after another --days days with nothing happening.

Stages come from the Stage issue field, or from the labels where the repository has none
(personal accounts, or an organisation where no open issue has a Stage): needs-review is Review (with blocked, Question), triage and backlog
their stages, and no label is Build. Question is set as Stage Question (Review with blocked
where the field has no Question option), or as the needs-review and blocked labels.

The run's token can't list the organisation's fields, so the Stage field's id is passed in
(--field-id, or the STAGE_FIELD_ID environment variable). "Today" is Brisbane time (UTC+10).

Usage: python stuck_issues.py [--days N] [--field-id ID] [--dry-run]
"""

import argparse
import datetime
import json
import os
import subprocess
import sys

STAGE_FIELD = "Stage"
START_DATE_FIELD = "Start date"
STUCK_LABEL = "stuck"
STUCK_COLOUR = "d93f0b"
STUCK_DESCRIPTION = "No activity at a working stage - moved to Question for the owner"
BLOCKED_LABEL = "blocked"
MANUAL_LABEL = "manual"
REVIEW_LABEL = "needs-review"
RECURRING_LABEL = "recurring"
OVERDUE_LABEL = "overdue"
TRIAGE, BACKLOG, BUILD, QUESTION, REVIEW, TEST, DONE = STAGES = [
    "Triage", "Backlog", "Build", "Question", "Review", "Test", "Done"]
WORK_STAGES = [BUILD, TEST]
# As queue.py: an issue still at the old Design stage reads as Build with the design label
OLD_DESIGN_STAGE = "Design"
DESIGN_LABEL = "design"
LABEL_STAGES = {REVIEW_LABEL: REVIEW, "triage": TRIAGE, "backlog": BACKLOG}
# As queue.py: the working stage each role takes (any other role takes Build), and the roles
# that take only their stage's issues with a label
ROLE_STAGES = {"tester": TEST}
ROLE_LABELS = {"designer": DESIGN_LABEL, "test-manager": "testing", "change-manager": "user-docs"}
DEFAULT_ROLES = ["app-builder"]
CONFIG_FILE = os.path.join(".claude", "lvlup-workflow.json")
DEFAULT_DAYS = 7
BRISBANE = datetime.timezone(datetime.timedelta(hours=10))
MARKER = "<!-- lvlup-workflow: stuck issues -->"


def run_gh(args):
    result = subprocess.run(["gh", *args], capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def parse_time(text):
    """An ISO time from the GitHub API ("2026-11-22T22:07:58Z") as an aware datetime."""
    return datetime.datetime.fromisoformat(text.replace("Z", "+00:00"))


class GitHub:
    """The issue actions the script needs, through the gh CLI."""

    def __init__(self, gh=run_gh, dry_run=False):
        self.gh = gh
        self.dry_run = dry_run

    def open_issues(self):
        return json.loads(self.gh(["issue", "list", "--state", "open", "--limit", "1000",
                                   "--json", "number,title,labels,assignees,updatedAt"]) or "[]")

    def field_values(self, number):
        """The issue's fields as {name: value}, or None where the repository has no issue fields
        (HTTP 404). Any other failure is raised, so the issue isn't misread by its labels."""
        try:
            out = self.gh(["api", f"repos/{{owner}}/{{repo}}/issues/{number}/issue-field-values"])
        except RuntimeError as error:
            if "404" in str(error) or "Not Found" in str(error):
                return None
            raise
        values = {}
        for value in json.loads(out or "[]"):
            option = value.get("single_select_option")
            values[value.get("issue_field_name")] = option["name"] if option else value.get("value")
        return values

    def timeline_times(self, number):
        """The time of each event on the issue's timeline (comments, references, commits,
        labels, field changes), as ISO strings."""
        out = self.gh(["api", f"repos/{{owner}}/{{repo}}/issues/{number}/timeline", "--paginate", "--jq",
                       ".[] | (.created_at // .submitted_at // .updated_at // .author.date "
                       "// .committer.date // empty)"])
        return [line.strip() for line in out.splitlines() if line.strip()]

    def change(self, args, summary):
        print(("[dry run] " if self.dry_run else "") + summary)
        if not self.dry_run:
            self.gh(args)


def labels_of(issue):
    return [label["name"] for label in issue.get("labels", [])]


def stage_of(issue, fields):
    """The issue's stage: from the Stage field (fields is None where there are none), or the labels."""
    labels = labels_of(issue)
    if fields is None:
        for label, stage in LABEL_STAGES.items():
            if label in labels:
                return QUESTION if stage == REVIEW and BLOCKED_LABEL in labels else stage
        return BUILD
    stage = fields.get(STAGE_FIELD)
    if stage == REVIEW and BLOCKED_LABEL in labels:
        return QUESTION
    if stage in STAGES:
        return stage
    return BUILD if stage == OLD_DESIGN_STAGE or RECURRING_LABEL in labels else TRIAGE


def old_design_label(fields):
    """The design label, as a list, for an issue still at the old Design stage."""
    return [DESIGN_LABEL] if (fields or {}).get(STAGE_FIELD) == OLD_DESIGN_STAGE else []


def waits_on_purpose(issue, fields, today):
    """Why the issue is left alone at a working stage, or None."""
    labels = labels_of(issue)
    if BLOCKED_LABEL in labels:
        return "blocked"
    if MANUAL_LABEL in labels:
        return "manual"
    if OVERDUE_LABEL in labels and RECURRING_LABEL in labels:
        # The recurring tasks check has told the owner already (lvluplabs_operations#420)
        return "overdue recurring task"
    start = (fields or {}).get(START_DATE_FIELD)
    if start and datetime.date.fromisoformat(start) > today:
        return f"scheduled for {start}"
    return None


def last_activity(issue, times):
    """The latest of the issue's updatedAt and its timeline events."""
    return max(parse_time(t) for t in [issue["updatedAt"], *times])


def project_roles(base):
    """The project's roles from .claude/lvlup-workflow.json, read as queue.py reads them."""
    try:
        with open(os.path.join(base, CONFIG_FILE), encoding="utf-8") as f:
            roles = json.load(f).get("roles")
    except Exception:
        return list(DEFAULT_ROLES)
    if isinstance(roles, str):
        roles = [roles]
    if not isinstance(roles, list):
        return list(DEFAULT_ROLES)
    roles = [{"builder": "app-builder"}.get(r.strip().lower(), r.strip().lower())
             for r in roles if isinstance(r, str) and r.strip()]
    return roles or list(DEFAULT_ROLES)


def project_paused(base):
    """The reason the project is paused, or "" if it isn't. As queue.py: any "paused" value but
    none, null or false pauses it, and a config that can't be read does too; no config doesn't."""
    try:
        with open(os.path.join(base, CONFIG_FILE), encoding="utf-8") as f:
            config = json.load(f)
    except FileNotFoundError:
        return ""
    except Exception:
        config = None
    if not isinstance(config, dict):
        return "the project's config can't be read"
    paused = config.get("paused")
    if paused is None or paused is False:
        return ""
    if isinstance(paused, str) and paused.strip():
        return paused.strip()
    return "no reason given"


def role_for(stage, roles, labels=()):
    """The role that takes an issue at a working stage, by queue.py's rule: a role with its own
    label takes its stage's issues with that label; otherwise the first role whose stage it is,
    else the project's first role."""
    def stage_of_role(role):
        return ROLE_STAGES.get(role, BUILD)
    labelled = next((r for r in roles if r in ROLE_LABELS and ROLE_LABELS[r] in labels
                     and stage_of_role(r) == stage), None)
    if labelled:
        return labelled
    return next((r for r in roles if stage_of_role(r) == stage and r not in ROLE_LABELS), roles[0])


def comment_body(issue, fields, stage, idle_days, since, roles):
    who = ", ".join(a["login"] for a in issue.get("assignees", [])) or "no one"
    labels = labels_of(issue) + old_design_label(fields)
    role = role_for(stage, roles, labels)
    if fields is not None:
        back = (f"set its Stage back to {stage} (and take off `{BLOCKED_LABEL}` if this check added it, which "
                "it does where the Stage field has no Question option)")
    else:
        back = f"remove the `{REVIEW_LABEL}` and `{BLOCKED_LABEL}` labels"
    label = ROLE_LABELS.get(role)
    taken = f"{stage} issues labelled `{label}` are" if label in labels else f"{stage} is"
    role_line = f"In this project, {taken} taken by the {role} role. It's assigned to {who}."
    return "\n".join([
        f"**Stuck:** nothing has happened on this issue for {idle_days} days (last on {since}) while at {stage}, "
        "so it's moved to Question for the Company Director (@anthoneyrimmer) to see.",
        "",
        role_line,
        "",
        "Likely reasons: no session has taken it, timed runs pass over it (a large issue while smaller work is "
        "left, another role's work, or work that needs the owner), or it waits on something no one recorded.",
        "",
        f"To move it on: comment with what should happen (or close it if it's no longer needed), then {back}. "
        f"A `{BLOCKED_LABEL}` label left on means it's waiting on purpose, and it isn't checked again. "
        f"The `{STUCK_LABEL}` label comes off at the next daily check once it has left Question.",
        "",
        MARKER,
    ])


def to_question(number, fields, labels, field_id, github):
    """Set the issue's stage to Question."""
    if fields is None:
        add = [label for label in (REVIEW_LABEL, BLOCKED_LABEL) if label not in labels]
        github.change(["issue", "edit", str(number), "--add-label", ",".join(add)],
                      f"set #{number} to Question (labels {', '.join(add)})")
        return
    try:
        github.change(["api", "-X", "POST", f"repos/{{owner}}/{{repo}}/issues/{number}/issue-field-values",
                       "-F", f"issue_field_values[][field_id]={field_id}",
                       "-f", f"issue_field_values[][value]={QUESTION}"],
                      f"set Stage on #{number} to {QUESTION}")
    except RuntimeError as error:
        if any(code in str(error) for code in ("401", "403", "404")):
            raise
        # The field has no Question option yet: Review with blocked reads as Question
        github.change(["api", "-X", "POST", f"repos/{{owner}}/{{repo}}/issues/{number}/issue-field-values",
                       "-F", f"issue_field_values[][field_id]={field_id}",
                       "-f", f"issue_field_values[][value]={REVIEW}"],
                      f"set Stage on #{number} to {REVIEW} (no Question option)")
        if BLOCKED_LABEL not in labels:
            github.change(["issue", "edit", str(number), "--add-label", BLOCKED_LABEL],
                          f"add {BLOCKED_LABEL} to #{number}")


def handle(issue, fields, times, now, days, roles, field_id, github):
    """Take the action for one issue. times are its timeline event times (only read for an
    issue that could be stuck: pass a function). Returns what was done."""
    number = issue["number"]
    labels = labels_of(issue)
    stage = stage_of(issue, fields)
    if stage not in WORK_STAGES:
        print(f"#{number}: at {stage}, left as it is")
        return "not working"
    if STUCK_LABEL in labels:
        # The owner moved it on from Question: its stuck round is over
        github.change(["issue", "edit", str(number), "--remove-label", STUCK_LABEL],
                      f"take {STUCK_LABEL} off #{number} (back at {stage})")
        return "unlabelled"
    reason = waits_on_purpose(issue, fields, now.astimezone(BRISBANE).date())
    if reason:
        print(f"#{number}: {reason}, left as it is")
        return "waits"
    if now - parse_time(issue["updatedAt"]) < datetime.timedelta(days=days):
        print(f"#{number}: active, left as it is")
        return "active"
    last = last_activity(issue, times(number))
    idle = now - last
    if idle < datetime.timedelta(days=days):
        print(f"#{number}: active, left as it is")
        return "active"
    since = last.astimezone(BRISBANE).date().isoformat()
    for label in old_design_label(fields):
        # Question replaces the stage that marked it as design work: the label first, so a
        # repository without it fails here with nothing lost
        github.change(["issue", "edit", str(number), "--add-label", label], f"add {label} to #{number}")
    # Comment, move, then label: the comment comes before the move so queue.py doesn't read it as
    # the owner's feedback, and the label comes last so `stuck` at a working stage always means
    # the owner has moved it back
    github.change(["issue", "comment", str(number), "--body",
                   comment_body(issue, fields, stage, idle.days, since, roles)],
                  f"comment on #{number} (idle {idle.days} days at {stage})")
    to_question(number, fields, labels, field_id, github)
    github.change(["issue", "edit", str(number), "--add-label", STUCK_LABEL], f"add {STUCK_LABEL} to #{number}")
    return "stuck"


def ensure_label(github):
    """Create the stuck label if the repository doesn't have it yet."""
    try:
        github.gh(["label", "create", STUCK_LABEL, "--color", STUCK_COLOUR, "--description", STUCK_DESCRIPTION])
    except RuntimeError as error:
        if "already exists" not in str(error):
            raise


def main(argv=None, now=None, github=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--days", type=int, default=DEFAULT_DAYS, help="days with no activity before it's stuck")
    parser.add_argument("--field-id", default=os.environ.get("STAGE_FIELD_ID"),
                        help="the Stage field's id (default: STAGE_FIELD_ID)")
    parser.add_argument("--dry-run", action="store_true", help="print the actions without making them")
    args = parser.parse_args(argv)

    paused = project_paused(os.getcwd())
    if paused:
        print(f"The project is paused ({paused}), so no issue is checked.")
        return 0
    github = github or GitHub(dry_run=args.dry_run)
    now = now or datetime.datetime.now(datetime.timezone.utc)
    roles = project_roles(os.getcwd())
    if not github.dry_run:
        ensure_label(github)
    issues = github.open_issues()
    fields, results = {}, {}
    for issue in issues:
        try:
            fields[issue["number"]] = github.field_values(issue["number"])
        except RuntimeError as error:
            # Not read: skipped, rather than read by its labels
            print(f"#{issue['number']}: fields not read, skipped: {error}")
            results["failed"] = results.get("failed", 0) + 1
    # Where no open issue has a Stage, the project uses the stage labels (its organisation has
    # no Stage field, or the run's token can't see it), so every issue is read by its labels
    stage_mode = any(STAGE_FIELD in (f or {}) for f in fields.values())
    if stage_mode and not args.field_id:
        parser.error("the Stage field's id is needed: --field-id or STAGE_FIELD_ID")
    for issue in issues:
        if issue["number"] not in fields:
            continue
        values = fields[issue["number"]] if stage_mode else None
        try:
            result = handle(issue, values, github.timeline_times, now, args.days, roles, args.field_id, github)
        except RuntimeError as error:
            # Reported, and the run goes on; the run then fails so it's noticed
            print(f"#{issue['number']}: failed: {error}")
            result = "failed"
        results[result] = results.get(result, 0) + 1
    print("Totals: " + (", ".join(f"{kind} {n}" for kind, n in sorted(results.items())) or "no open issues"))
    return 1 if results.get("failed") else 0


if __name__ == "__main__":
    sys.exit(main())
