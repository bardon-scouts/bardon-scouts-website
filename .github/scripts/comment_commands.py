"""Set the stage, close or label an issue from a comment (lvlup-labs/lvluplabs_operations#443).

A command is a line of its own in a new comment:
- /build            set Stage to Build (hands it back)
- /backlog          set Stage to Backlog
- /close            close the issue, with Stage Done
- /close-when-done  add the close-when-done label

It counts only in a comment by a person with write access, on an open issue. It never counts on a
pull request, in a comment by Claude's account, in one with a "<!-- lvlup-workflow:" mark (Claude's,
from a PC that uses the owner's account, or an automation's), or in a quote, a code block or a
hidden HTML comment. The plugin's hook also stops Claude posting an unmarked comment.
A re-run never counts: what it says may since have been done another way. Post the command again.

/close-when-done can go with /build or /backlog. Any other mix of commands (such as /build and
/close) is refused: nothing is changed. A comment whose commands were done gets a thumbs up, and one
that was refused a confused face. A failure fails the run, so it's noticed.

Stages are the Stage issue field where its id is given (--field-id, or the STAGE_FIELD_ID
environment variable: the run's token can't list the organisation's fields). Where it's empty the
repository uses the stage labels: triage, backlog and needs-review, and no label is Build.

A change made with a run's own token starts no other workflow, so /close sets Done itself.

Usage: python comment_commands.py [--event FILE] [--field-id ID]
  --event: the issue_comment event (default: GITHUB_EVENT_PATH, set in every run)
"""

import argparse
import json
import os
import re
import subprocess
import sys

BUILD, BACKLOG, CLOSE, CLOSE_WHEN_DONE = COMMANDS = ["build", "backlog", "close", "close-when-done"]
STAGES = {BUILD: "Build", BACKLOG: "Backlog"}
DONE_STAGE = "Done"
CLOSE_LABEL, RECURRING_LABEL = "close-when-done", "recurring"
REVIEW_LABEL, BLOCKED_LABEL, TRIAGE_LABEL, BACKLOG_LABEL = "needs-review", "blocked", "triage", "backlog"
MARK = "<!-- lvlup-workflow:"
CLAUDE_LOGIN = "lvluplabspty"  # the same as queue.py's (lvlup-labs/lvluplabs_operations#463)
WRITE_ACCESS = {"admin", "maintain", "write"}

COMMAND = re.compile(r"^/(build|backlog|close|close-when-done)\s*$", re.IGNORECASE)  # an indented line may be a list's
LIST_MARKER = re.compile(r"^ {0,3}(?:(?:[-*+]|\d{1,9}[.)])\s+)+")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
QUOTE = re.compile(r"^ {0,3}>")
HTML_EDGE = re.compile(r"<!--|-->|</?(?:pre|code|blockquote)\b", re.IGNORECASE)
CODE_SPAN = re.compile(r"(`+)(?!`).*?(?<!`)\1(?!`)")


def find_commands(body):
    """The commands in a comment, in order, each once: lines of their own, outside quotes, code
    and HTML comments. A line straight after a quoted one is still in the quote, as GitHub shows it."""
    found = []
    fence = None
    hidden = quoted = False
    pre = 0
    for line in (body or "").replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        if fence:
            closing = FENCE.match(line)
            if closing and closing.group(1).startswith(fence) and not closing.group(2).strip():
                fence = None
            continue
        if hidden or pre:
            hidden, pre = html_state(line, hidden, pre)
            continue
        if not line.strip():
            quoted = False
            continue
        inner = LIST_MARKER.sub("", line)
        if QUOTE.match(inner):
            quoted = True
            continue
        opening = FENCE.match(inner)
        if opening and not (opening.group(1)[0] == "`" and "`" in opening.group(2)):
            fence, quoted = opening.group(1), False
            continue
        match = COMMAND.match(line)
        if match:
            name = match.group(1).lower()
            if not quoted and name not in found:
                found.append(name)
            continue
        hidden, pre = html_state(line, hidden, pre)
    return found


def html_state(line, hidden, pre):
    """Whether an HTML comment, and how many <pre>, <code> and <blockquote> tags, are open at the
    end of the line."""
    for edge in HTML_EDGE.finditer(CODE_SPAN.sub("", line)):
        text = edge.group(0)
        if text == "<!--":
            hidden = True
        elif text == "-->":
            hidden = False
        elif not hidden:
            pre = max(0, pre - 1) if text.startswith("</") else pre + 1
    return hidden, pre


def conflict(commands):
    """Why the commands can't be done together, or None."""
    moves = [c for c in commands if c != CLOSE_WHEN_DONE]
    if len(moves) > 1:
        return f"{' and '.join('/' + c for c in moves)} can't both be done"
    if CLOSE in commands and CLOSE_WHEN_DONE in commands:
        return "/close and /close-when-done can't both be done"
    return None


def run_gh(args):
    result = subprocess.run(["gh", *args], capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


class GitHub:
    """The issue actions the script needs, through the gh CLI."""

    def __init__(self, gh=run_gh):
        self.gh = gh

    def has_write_access(self, user):
        """True if the user can write to the repository. Someone with no access at all is a 404."""
        try:
            access = json.loads(self.gh(["api", f"repos/{{owner}}/{{repo}}/collaborators/{user}/permission"]))
        except RuntimeError as error:
            if "404" in str(error):
                return False
            raise
        return access.get("permission") in WRITE_ACCESS

    def issue(self, number):
        """(open, labels) as they are now: the event's copy can be behind."""
        data = json.loads(self.gh(["issue", "view", str(number), "--json", "state,labels"]))
        return data["state"] == "OPEN", [label["name"] for label in data["labels"]]

    def set_stage(self, number, field_id, stage):
        self.gh(["api", "-X", "POST", f"repos/{{owner}}/{{repo}}/issues/{number}/issue-field-values",
                 "-F", f"issue_field_values[][field_id]={field_id}",
                 "-f", f"issue_field_values[][value]={stage}"])

    def edit_labels(self, number, add=(), remove=()):
        args = ["issue", "edit", str(number)]
        if add:
            args += ["--add-label", ",".join(add)]
        if remove:
            args += ["--remove-label", ",".join(remove)]
        if add or remove:
            self.gh(args)

    def close(self, number):
        self.gh(["issue", "close", str(number), "--reason", "completed"])

    def react(self, comment_id, content):
        self.gh(["api", "-X", "POST", f"repos/{{owner}}/{{repo}}/issues/comments/{comment_id}/reactions",
                 "-f", f"content={content}", "--silent"])


def move_with_labels(number, command, labels, github):
    """Set the stage in a repository that uses the stage labels. blocked goes only where it's half
    of Question (needs-review with blocked); on its own it means the issue waits on other work."""
    drop = [label for label in (REVIEW_LABEL, TRIAGE_LABEL, BACKLOG_LABEL) if label in labels]
    if REVIEW_LABEL in labels and BLOCKED_LABEL in labels:
        drop.append(BLOCKED_LABEL)
    add = []
    if command == BACKLOG:
        drop = [label for label in drop if label != BACKLOG_LABEL]
        add = [BACKLOG_LABEL] if BACKLOG_LABEL not in labels else []
    github.edit_labels(number, add, drop)


def do(command, number, labels, field_id, github):
    if command == CLOSE_WHEN_DONE:
        # One left from an earlier round is taken off first: queue.py close needs it added since the
        # last hand-over. On a recurring task it's standing, and stays.
        if CLOSE_LABEL in labels and RECURRING_LABEL not in labels:
            github.edit_labels(number, remove=[CLOSE_LABEL])
        github.edit_labels(number, add=[CLOSE_LABEL])
    elif command == CLOSE:
        # Done first: if closing fails, the issue is open, so the command can be posted again
        if field_id:
            github.set_stage(number, field_id, DONE_STAGE)
        github.close(number)
    elif field_id:
        github.set_stage(number, field_id, STAGES[command])
    else:
        move_with_labels(number, command, labels, github)
    print(f"#{number}: /{command} done")


def handle(event, field_id, github, attempt="1"):
    """Do the commands in an issue_comment event. Returns what was done."""
    comment, issue = event["comment"], event["issue"]
    number, user = issue["number"], comment["user"]
    body = comment.get("body") or ""
    if attempt != "1":
        return ignored(number, "a re-run (post the command again)")
    if event.get("action") != "created":
        return ignored(number, "not a new comment")
    if issue.get("pull_request"):
        return ignored(number, "a pull request")
    if user.get("type") != "User":
        return ignored(number, "not a person's comment")
    if MARK in body or user["login"].lower() == CLAUDE_LOGIN:
        return ignored(number, "Claude's or an automation's comment")
    commands = find_commands(body)
    if not commands:
        return ignored(number, "no command on a line of its own")
    if not github.has_write_access(user["login"]):
        return ignored(number, f"{user['login']} has no write access")
    is_open, labels = github.issue(number)
    refusal = conflict(commands) or (None if is_open else "the issue is closed")
    if refusal:
        print(f"#{number}: refused: {refusal}")
        github.react(comment["id"], "confused")
        return "refused"
    # The label first: queue.py close reads it as part of the feedback the issue comes back with
    for command in sorted(commands, key=lambda c: c != CLOSE_WHEN_DONE):
        do(command, number, labels, field_id, github)
    github.react(comment["id"], "+1")
    return "done"


def ignored(number, why):
    print(f"#{number}: ignored: {why}")
    return "ignored"


def main(argv=None, github=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--event", default=os.environ.get("GITHUB_EVENT_PATH"), help="the event's JSON file")
    parser.add_argument("--field-id", default=os.environ.get("STAGE_FIELD_ID", ""),
                        help="the Stage field's id (default: STAGE_FIELD_ID; empty: the stage labels)")
    args = parser.parse_args(argv)
    if not args.event:
        parser.error("the event is needed: --event or GITHUB_EVENT_PATH")
    with open(args.event, encoding="utf-8") as f:
        event = json.load(f)
    handle(event, args.field_id, github or GitHub(), os.environ.get("GITHUB_RUN_ATTEMPT", "1"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
