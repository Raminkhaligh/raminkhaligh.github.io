#!/usr/bin/env python3
"""
This script generates a simple sitemap.xml by scanning all HTML files in the
repository.  It should be executed in the root of the project and will output
a `sitemap.xml` file listing each page URL relative to the site base.

To automate sitemap generation on GitHub, add a workflow that calls this
script (see `.github/workflows/generate-sitemap.yml`).
"""
import os
from datetime import datetime, timezone
from urllib.parse import urljoin

# Base URL of the deployed GitHub Pages site.  Update this if the domain changes.
BASE_URL = "https://raminkhaligh.github.io/"

# Directories that hold build artifacts, orphaned drafts, or partials — never
# real indexable pages — plus individual stray files at the repo root.
EXCLUDED_DIRS = {"_site", "includes_", "node_modules"}
EXCLUDED_FILES = {"index1.html", "index3.html"}

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

def generate_sitemap(url_paths: list[str], output_path: str) -> None:
    """Generate a sitemap.xml with the given URL paths."""
    now = datetime.now(timezone.utc).date().isoformat()
    lines = [
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
        "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">",
    ]
    for rel_path in url_paths:
        url = urljoin(BASE_URL, rel_path)
        # Homepages (English + Farsi) are the primary entry points — rank above subpages.
        priority = "1.0" if rel_path in ("index.html", "fa/index.html") else "0.7"
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append(f"    <lastmod>{now}</lastmod>")
        lines.append("    <changefreq>monthly</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    pages = discover_html_files(".")
    generate_sitemap(pages, "sitemap.xml")