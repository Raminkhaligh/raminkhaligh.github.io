#!/usr/bin/env python3
"""
This script generates a simple sitemap.xml by scanning all HTML files in the
repository.  It should be executed in the root of the project and will output
a `sitemap.xml` file listing each page URL relative to the site base.

To automate sitemap generation on GitHub, add a workflow that calls this
script (see `.github/workflows/generate-sitemap.yml`).
"""
import os
from datetime import datetime
from urllib.parse import urljoin

# Base URL of the deployed GitHub Pages site.  Update this if the domain changes.
BASE_URL = "https://raminkhaligh.github.io/"

def discover_html_files(root_dir: str) -> list[str]:
    """Return a list of relative paths for all .html files under root_dir."""
    html_paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".html"):
                rel_path = os.path.relpath(os.path.join(dirpath, filename), root_dir)
                # Skip files in node_modules or hidden directories if present
                if rel_path.startswith(".") or "node_modules" in rel_path:
                    continue
                html_paths.append(rel_path)
    return sorted(html_paths)

def generate_sitemap(url_paths: list[str], output_path: str) -> None:
    """Generate a sitemap.xml with the given URL paths."""
    now = datetime.utcnow().date().isoformat()
    lines = [
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>",
        "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">",
    ]
    for rel_path in url_paths:
        url = urljoin(BASE_URL, rel_path)
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append(f"    <lastmod>{now}</lastmod>")
        lines.append("    <changefreq>monthly</changefreq>")
        lines.append("    <priority>0.7</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    pages = discover_html_files(".")
    generate_sitemap(pages, "sitemap.xml")