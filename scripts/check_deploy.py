"""Check that a commit has reached the Bardon Scouts dev site.

Every page carries <meta name="deploy-commit"> with the commit it was built
from. A commit passes when the stamp is that commit, or a later commit that
contains it (a commit pushed together with a later one gets no deploy of its
own). Needs no Netlify login.

Usage: python scripts/check_deploy.py <commit> [--timeout SECONDS]

Exits 0 when deployed, 1 when not verified (the stamp didn't arrive in time:
the build may have failed, so look at the Netlify dashboard).
"""

import argparse
import re
import subprocess
import sys
import time
import urllib.request

DEV_SITE = "https://dev--bardon-scouts-website.netlify.app/"
STAMP = re.compile(r'name="?deploy-commit"? content="?([0-9a-f]{40})')
INTERVAL = 20


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True)


def read_stamp():
    request = urllib.request.Request(
        DEV_SITE + "?nocache=" + str(int(time.time())),
        headers={"Cache-Control": "no-cache", "User-Agent": "check_deploy"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            html = response.read().decode("utf-8", "replace")
    except OSError as error:
        print(f"Couldn't read the dev site: {error}")
        return None
    match = STAMP.search(html)
    return match.group(1) if match else None


def contains(stamp, commit):
    """True when the stamp is the commit or a later commit containing it."""
    if stamp == commit:
        return True
    if git("cat-file", "-e", stamp + "^{commit}").returncode != 0:
        git("fetch", "--quiet", "origin", "dev")
    return git("merge-base", "--is-ancestor", commit, stamp).returncode == 0


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("commit")
    parser.add_argument("--timeout", type=int, default=300,
                        help="seconds to wait for the stamp (default 300)")
    args = parser.parse_args()

    resolved = git("rev-parse", "--verify", "--quiet", args.commit + "^{commit}")
    if resolved.returncode != 0:
        git("fetch", "--quiet", "origin", "dev")
        resolved = git("rev-parse", "--verify", "--quiet", args.commit + "^{commit}")
    if resolved.returncode != 0:
        print(f"Not verified: {args.commit} isn't a known commit.")
        return 1
    commit = resolved.stdout.strip()

    deadline = time.time() + args.timeout
    stamp = None
    while True:
        stamp = read_stamp() or stamp
        if stamp and contains(stamp, commit):
            how = "the same commit" if stamp == commit else "a later commit that contains it"
            print(f"Deployed: the dev site's stamp is {stamp} ({how}).")
            return 0
        if time.time() >= deadline:
            break
        time.sleep(INTERVAL)

    print(f"Not verified: after {args.timeout} seconds the dev site's stamp is "
          f"{stamp or 'missing'}, which doesn't contain {commit}. The build may "
          "have failed: open the Netlify dashboard (Deploys) to see why.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
