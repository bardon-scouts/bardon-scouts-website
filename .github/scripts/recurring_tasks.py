"""Open or reopen issues for recurring tasks that are due today.

Reads .github/recurring-tasks.yml. For each task due today (Brisbane time):
- no issue yet: create one with the task's labels plus `recurring`
- issue closed: reopen it, reset its labels (and its Stage to Build, where it has one) and
  comment that it's due again
- issue open: leave it, so a missed occurrence is only done once

Usage: python recurring_tasks.py [--dry-run] [--date YYYY-MM-DD] [--tasks FILE]

Shared by the lvlup-workflow plugin, which keeps each project's copy up to date.
Change it in the plugin, not in a project.
"""

import argparse
import calendar
import datetime
import json
import subprocess
import sys

BRISBANE = datetime.timezone(datetime.timedelta(hours=10))  # no daylight saving
LABEL = "recurring"
RESET_LABELS = ("needs-review", "blocked")
STAGE_FIELD = "Stage"
WORK_STAGE = "Build"
WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
QUARTER_MONTHS = (1, 4, 7, 10)


def marker(task_id):
    return f"<!-- recurring-task: {task_id} -->"


def is_due(task, day):
    """True if the task falls due on `day` (a datetime.date)."""
    every = task["every"]
    if every == "daily":
        return True
    if "day" not in task:
        raise ValueError(f"task {task['id']}: '{every}' needs a 'day'")
    if every == "weekly":
        return day.weekday() == WEEKDAYS.index(str(task["day"]).lower())
    if every in ("monthly", "quarterly"):
        if every == "quarterly" and day.month not in QUARTER_MONTHS:
            return False
        # A day past the end of the month (e.g. 31 in April) falls on its last day.
        last = calendar.monthrange(day.year, day.month)[1]
        return day.day == min(int(task["day"]), last)
    raise ValueError(f"task {task['id']}: unknown 'every' value {every!r}")


def run_gh(args):
    result = subprocess.run(["gh", *args], capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


class GitHub:
    """The issue actions the script needs, through the gh CLI."""

    def __init__(self, gh=run_gh, dry_run=False):
        self.gh = gh
        self.dry_run = dry_run

    def recurring_issues(self):
        out = self.gh(["issue", "list", "--state", "all", "--label", LABEL, "--limit", "1000",
                       "--json", "number,state,body,labels"])
        return json.loads(out)

    def change(self, args, summary):
        print(("[dry run] " if self.dry_run else "") + summary)
        if not self.dry_run:
            self.gh(args)

    def stage(self, number):
        """(field id, stage) for the issue's Stage, or None if it has none.

        The run's token can't list the organisation's fields, so the field's id comes from the
        issue. Repositories without issue fields (personal accounts) return 404: no Stage.
        """
        try:
            out = self.gh(["api", f"repos/{{owner}}/{{repo}}/issues/{number}/issue-field-values"])
        except RuntimeError:
            return None
        for value in json.loads(out or "[]"):
            if value.get("issue_field_name") == STAGE_FIELD:
                option = value.get("single_select_option") or {}
                return value["issue_field_id"], option.get("name")
        return None

    def ensure_label(self):
        self.change(["label", "create", LABEL, "--color", "0E8A16", "--force",
                     "--description", "Opened by the recurring tasks workflow"],
                    f"ensure label '{LABEL}' exists")


def find_issue(issues, task_id):
    for issue in issues:
        if marker(task_id) in (issue.get("body") or ""):
            return issue
    return None


def handle(task, day, issues, github):
    """Take the action for one task. Returns what was done."""
    if not is_due(task, day):
        return "not due"
    labels = list(task.get("labels", [])) + [LABEL]
    issue = find_issue(issues, task["id"])
    if issue is None:
        body = f"{task.get('body', '').rstrip()}\n\n{marker(task['id'])}\n"
        args = ["issue", "create", "--title", task["title"], "--body", body]
        for label in labels:
            args += ["--label", label]
        github.change(args, f"create issue for '{task['id']}'")
        return "created"
    number = str(issue["number"])
    if issue["state"] == "OPEN":
        print(f"'{task['id']}' is still open (#{number}), left as it is")
        return "still open"
    github.change(["issue", "reopen", number], f"reopen #{number} for '{task['id']}'")
    current = {label["name"] for label in issue.get("labels", [])}
    edit = ["issue", "edit", number]
    for label in RESET_LABELS:
        if label in current:
            edit += ["--remove-label", label]
    for label in labels:
        if label not in current:
            edit += ["--add-label", label]
    if len(edit) > 3:
        github.change(edit, f"reset labels on #{number}")
    stage = github.stage(number)
    if stage and stage[1] != WORK_STAGE:
        github.change(["api", "-X", "POST", f"repos/{{owner}}/{{repo}}/issues/{number}/issue-field-values",
                       "-F", f"issue_field_values[][field_id]={stage[0]}",
                       "-f", f"issue_field_values[][value]={WORK_STAGE}"],
                      f"set Stage on #{number} to {WORK_STAGE} (was {stage[1]})")
    github.change(["issue", "comment", number, "--body", f"Due again on {day.isoformat()}."],
                  f"comment on #{number}")
    return "reopened"


def load_tasks(path):
    import yaml  # only needed when reading the real list

    with open(path, encoding="utf-8") as f:
        tasks = (yaml.safe_load(f) or {}).get("tasks") or []
    ids = [task["id"] for task in tasks]
    if len(ids) != len(set(ids)):
        raise ValueError("task ids must be unique")
    return tasks


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true", help="print the actions without making them")
    parser.add_argument("--date", help="treat this date (YYYY-MM-DD) as today")
    parser.add_argument("--tasks", default=".github/recurring-tasks.yml")
    args = parser.parse_args(argv)

    day = (datetime.date.fromisoformat(args.date) if args.date
           else datetime.datetime.now(BRISBANE).date())
    tasks = load_tasks(args.tasks)
    github = GitHub(dry_run=args.dry_run)
    print(f"{len(tasks)} recurring task(s), today is {day.isoformat()} (Brisbane)")
    due = [task for task in tasks if is_due(task, day)]
    if not due:
        print("nothing due")
        return 0
    github.ensure_label()
    issues = github.recurring_issues()
    for task in tasks:
        handle(task, day, issues, github)
    return 0


if __name__ == "__main__":
    sys.exit(main())
