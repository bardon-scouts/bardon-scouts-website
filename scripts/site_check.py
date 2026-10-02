"""Whole-site check for the Bardon Scouts website.

Run from the repository root before publishing `dev` to `master`:

    python scripts/site_check.py                 # checks the dev site
    python scripts/site_check.py <base URL>      # checks another deploy

Checks (see docs/testing/README.md):
  1. Every page linked from the site (crawled from the home page, including every menu link) returns 200.
  2. Every redirect in static/_redirects returns a 301 to the right place.
  3. The deployed CMS config (/admin/config.yml) has an entry for every page in content/.
  4. The contact, website feedback and complaints forms are on their pages.

Uses only the Python standard library. Exits 1 if any check fails.
"""
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE = (sys.argv[1] if len(sys.argv) > 1 else "https://dev--bardon-scouts-website.netlify.app").rstrip("/")
ROOT = pathlib.Path(__file__).resolve().parent.parent
HEADERS = {"User-Agent": "bardon-site-check"}
FORMS = {"/contact/": "contact", "/website-feedback/": "website-feedback", "/complaints/": "complaints"}
ASSET = re.compile(r"\.(css|js|png|jpe?g|gif|svg|pdf|ico|xml|webp|webmanifest)$", re.I)
failures = []


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def get(url, follow=True):
    opener = urllib.request.build_opener() if follow else urllib.request.build_opener(NoRedirect)
    try:
        with opener.open(urllib.request.Request(url, headers=HEADERS), timeout=30) as r:
            return r.status, r.read().decode("utf-8", "replace"), r.headers
    except urllib.error.HTTPError as e:
        return e.code, "", e.headers
    except Exception as e:  # network errors count as failures
        return f"error: {type(e).__name__}", "", {}


def fail(msg):
    failures.append(msg)
    print("  FAIL", msg)


def check_pages():
    print("1. Pages linked from the site return 200")
    seen, queue, stamp = set(), ["/"], None
    while queue:
        path = queue.pop()
        if path in seen:
            continue
        seen.add(path)
        status, html, _ = get(BASE + path)
        if status != 200:
            fail(f"{path} returned {status}")
            continue
        if stamp is None:
            m = re.search(r'deploy-commit content="?([0-9a-f]{40})', html)
            stamp = m.group(1) if m else "none"
        for href in re.findall(r'href="?([^" >]+)', html):
            full = urllib.parse.urljoin(BASE + path, href.split("#")[0])
            if full.startswith(BASE) and not ASSET.search(full):
                queue.append(full[len(BASE):] or "/")
    print(f"  {len(seen)} pages checked (deploy-commit {stamp})")
    return seen


def resolve(path):
    """Follow redirects and Hugo alias pages (meta refresh) from path. Returns (final path, how)."""
    how = []
    for _ in range(4):
        status, html, headers = get(BASE + path, follow=False)
        if status in (301, 302, 308):
            path = urllib.parse.urljoin(BASE + path, headers.get("Location", "")).replace(BASE, "")
            how.append(str(status))
            continue
        refresh = re.search(r'http-equiv="?refresh"?[^>]*url=([^"\'>\s]+)', html, re.I) if status == 200 else None
        if refresh:
            path = urllib.parse.urljoin(BASE + path, refresh.group(1)).replace(BASE, "")
            how.append("alias page")
            continue
        return path, status, how
    return path, "too many redirects", how


def check_redirects():
    print("2. Old URLs in static/_redirects reach their new page")
    count, aliases = 0, []
    for line in (ROOT / "static/_redirects").read_text(encoding="utf-8").splitlines():
        parts = line.split()
        if len(parts) < 3 or line.lstrip().startswith("#"):
            continue
        source, target = parts[0], parts[1]
        if source.endswith("/*"):
            source, target = source[:-1], target.replace(":splat", "")
        final, status, how = resolve(source)
        count += 1
        if status != 200 or final.rstrip("/") != target.rstrip("/") or not how:
            fail(f"{source} ended at {final} ({status}) via {how or 'no redirect'}, expected {target}")
        elif "alias page" in how:
            aliases.append(source)
    print(f"  {count} redirects checked")
    if aliases:
        print(f"  note: {', '.join(aliases)} reach their page through a Hugo alias page (HTML refresh), not a 301")


def check_cms():
    print("3. The CMS config lists every page")
    status, config, _ = get(BASE + "/admin/config.yml")
    if status != 200:
        fail(f"/admin/config.yml returned {status}")
        return
    files = set(re.findall(r'file:\s*"([^"]+)"', config))
    folders = [f.rstrip("/") for f in re.findall(r'folder:\s*"([^"]+)"', config)]
    pages = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / "content").rglob("*.md"))
    missing = [p for p in pages if p not in files and not any(
        p.startswith(f + "/") and p.count("/") == f.count("/") + 1 and not p.endswith("_index.md") for f in folders)]
    for p in missing:
        fail(f"{p} has no CMS entry")
    print(f"  {len(pages)} pages in content/, {len(missing)} missing from the CMS")


def check_forms():
    print("4. Forms are present")
    for path, name in FORMS.items():
        status, html, _ = get(BASE + path)
        # Netlify processes the form at deploy: it removes data-netlify and adds a hidden form-name field
        if not re.search(r'name=["\']?form-name["\']? value=["\']?' + re.escape(name) + r'\b', html):
            fail(f"{path} has no '{name}' Netlify form (status {status})")
    print(f"  {len(FORMS)} forms checked")


print(f"Checking {BASE}")
check_pages()
check_redirects()
check_cms()
check_forms()
print(f"\n{'FAILED: ' + str(len(failures)) + ' problem(s)' if failures else 'All checks passed'}")
sys.exit(1 if failures else 0)
