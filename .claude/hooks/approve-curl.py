"""PreToolUse hook: auto-approve read-only curl commands.

Approves a Bash command only if it starts with curl and every piped
stage is a read-only text tool. Anything else (redirects, chaining,
command substitution, other programs) gets no decision, so the normal
permission rules apply.
"""
import json
import re
import sys

READ_ONLY = {"curl", "grep", "sort", "uniq", "wc", "head", "tail", "cut", "tr"}
# Characters that could write files or run extra commands
UNSAFE = re.compile(r"[;&<>`]|\$\(")


def strip_quoted(cmd):
    """Remove quoted strings so characters inside patterns aren't flagged."""
    return re.sub(r"'[^']*'|\"[^\"]*\"", "''", cmd)


def is_safe(cmd):
    cmd = cmd.strip()
    if "\n" in cmd:
        return False
    bare = strip_quoted(cmd)
    if UNSAFE.search(bare):
        return False
    stages = [s.strip() for s in bare.split("|")]
    if not stages or stages[0].split()[:1] != ["curl"]:
        return False
    for stage in stages:
        words = stage.split()
        if not words or words[0] not in READ_ONLY:
            return False
    # curl must not write output files or upload data
    curl_args = stages[0].split()[1:]
    for arg in curl_args:
        if arg in ("-o", "--output", "-O", "--remote-name", "-T", "--upload-file",
                   "-d", "--data", "-F", "--form", "-X", "--request", "-K", "--config"):
            # -o /dev/null is harmless and used for status-code checks
            if arg in ("-o", "--output"):
                idx = curl_args.index(arg)
                if idx + 1 < len(curl_args) and curl_args[idx + 1] == "/dev/null":
                    continue
            return False
        # Combined short flags, e.g. -so file or -sd data
        if re.fullmatch(r"-[A-Za-z]{2,}", arg) and set(arg[1:]) & set("oOTdFXK"):
            return False
    return True


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    if data.get("tool_name") != "Bash":
        return
    if is_safe(data.get("tool_input", {}).get("command", "")):
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "allow",
                "permissionDecisionReason": "Read-only curl pre-approved for this project",
            }
        }))


main()
