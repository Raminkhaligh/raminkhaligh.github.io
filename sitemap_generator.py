#!/usr/bin/env python3
"""
This script generates a simple sitemap.xml by scanning all HTML files in the
repository.  It should be executed in the root of the project and will output
a `sitemap.xml` file listing each page URL relative to the site base.

To automate sitemap generation on GitHub, add a workflow that calls this
script (see `.github/workflows/generate-sitemap.yml`).
"""
import json
import os
import subprocess
from datetime import datetime, timezone
from urllib.parse import urljoin

# Canonical origin of the deployed site (must match CNAME and each page's
# <link rel="canonical">).  Update this if the domain changes.
BASE_URL = "https://raminkhaligh.ir/"

# Directories that hold build artifacts, orphaned drafts, or partials — never
# real indexable pages — plus individual stray files at the repo root.
EXCLUDED_DIRS = {"_site", "includes_", "node_modules"}
EXCLUDED_FILES = {"index1.html", "index3.html", "404.html"}

def discover_html_files(root_dir: str) -> list[str]:
    """Return a list of relative paths for all real, indexable .html files under root_dir."""
    html_paths = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS and not d.startswith(".")]
        for filename in filenames:
            if not filename.endswith(".html"):
                continue
            if filename in EXCLUDED_FILES or filename.startswith("google"):
                continue
            rel_path = os.path.relpath(os.path.join(dirpath, filename), root_dir)
            if rel_path.startswith("."):
                continue
            html_paths.append(rel_path.replace(os.sep, "/"))
    return sorted(html_paths)

def git_last_commit_date(rel_path: str) -> str | None:
    """ISO date of the last commit that touched rel_path, or None outside a repo."""
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", rel_path],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        return out[:10] if out else None
    except (subprocess.CalledProcessError, OSError):
        return None

def posts_json_lastmod() -> dict[str, str]:
    """Map blog post URL paths to their lastmod dates from blog/posts.json."""
    mapping = {}
    try:
        with open("blog/posts.json", encoding="utf-8") as f:
            for post in json.load(f):
                url = post.get("url", "")
                lastmod = post.get("lastmod") or post.get("date")
                if url and lastmod:
                    mapping[url.lstrip("/")] = lastmod[:10]
    except (OSError, ValueError):
        pass
    return mapping

def generate_sitemap(url_paths: list[str], output_path: str) -> None:
    """Generate a sitemap.xml with the given URL paths."""
    today = datetime.now(timezone.utc).date().isoformat()
    post_dates = posts_json_lastmod()
    # lastmod must reflect real content changes — a constant "generated today"
    # stamp is noise Google learns to ignore.  Prefer the last git commit,
    # then the curated date in posts.json, then today.
    lines = [
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
        "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">",
    ]
    for rel_path in url_paths:
        # index.html canonicalizes to its directory with a trailing slash
        # (matches each page's own <link rel="canonical">) rather than the
        # literal /index.html path — keeps the sitemap from splitting
        # ranking signal across two URLs for the same page.
        if os.path.basename(rel_path) == "index.html":
            dir_part = rel_path[: -len("index.html")]
            url = urljoin(BASE_URL, dir_part)
        else:
            url = urljoin(BASE_URL, rel_path)
        lastmod = git_last_commit_date(rel_path) or post_dates.get(rel_path) or today
        # Homepages (English + Farsi) are the primary entry points — rank above subpages.
        priority = "1.0" if rel_path in ("index.html", "fa/index.html") else "0.7"
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append(f"    <changefreq>monthly</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    pages = discover_html_files(".")
    generate_sitemap(pages, "sitemap.xml")
