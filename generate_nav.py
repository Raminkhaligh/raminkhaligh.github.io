#!/usr/bin/env python3
"""
Auto-generate content/nav.json for Ramin Khaligh's portfolio site.

content/nav.seed.json is the hand-maintained base: top-level nav items
(Experience, Skills, About, Blog, FAQ, Contact) plus any Services submenu
entries that are still just in-page anchors on the homepage.

This script scans services/*.html and, for each page, adds or refreshes a
matching submenu entry so new service pages show up in the nav automatically
— no manual JSON editing needed. Each services page should carry:

  <meta name="nav-label" content="Short Nav Label" />
  <meta name="nav-label-fa" content="برچسب کوتاه فارسی" />  (optional)

If nav-label is missing, the part of <title> before " | " is used instead.

If this page replaces one of the anchor-only entries still seeded in
nav.seed.json (a service that only exists as an on-page card so far), add:

  <meta name="nav-replaces" content="svc-growth-marketing" />

using that entry's "anchor" value — the generator upgrades that entry in
place (adds "page", refreshes its label) instead of appending a duplicate.

Run this after adding/removing a page under services/, or let the
generate-nav GitHub Action do it on every push to main.
"""

import re
import json
from pathlib import Path

ROOT = Path(__file__).parent
SERVICES_DIR = ROOT / "services"
SEED_FILE = ROOT / "content" / "nav.seed.json"
OUTPUT_FILE = ROOT / "content" / "nav.json"


def extract_meta_content(html, name):
    m = re.search(rf'<meta[^>]+name=["\']{name}["\'][^>]+content=["\'](.*?)["\']', html, re.I)
    return m.group(1).strip() if m else None


def extract_nav_label(html):
    en = extract_meta_content(html, "nav-label")
    if not en:
        title = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
        raw = title.group(1).strip() if title else "Untitled"
        en = raw.split("|")[0].strip() if "|" in raw else raw
    fa = extract_meta_content(html, "nav-label-fa") or en
    return en, fa


def main():
    seed = json.loads(SEED_FILE.read_text(encoding="utf-8"))
    services_item = next(item for item in seed["items"] if item["id"] == "services")
    submenu = services_item.setdefault("submenu", [])
    existing_by_page = {entry["page"]: entry for entry in submenu if entry.get("page")}

    discovered_urls = set()
    for html_file in sorted(SERVICES_DIR.glob("*.html")):
        if html_file.name == "index.html":
            continue
        html = html_file.read_text(encoding="utf-8", errors="ignore")
        label_en, label_fa = extract_nav_label(html)
        replaces = extract_meta_content(html, "nav-replaces")
        url = f"/services/{html_file.name}"
        discovered_urls.add(url)

        if url in existing_by_page:
            existing_by_page[url]["label"] = {"en": label_en, "fa": label_fa}
            continue

        target = None
        if replaces:
            target = next((e for e in submenu if e.get("anchor") == replaces and not e.get("page")), None)
        if target is not None:
            target["page"] = url
            target["label"] = {"en": label_en, "fa": label_fa}
            existing_by_page[url] = target
        else:
            new_entry = {"page": url, "label": {"en": label_en, "fa": label_fa}}
            submenu.append(new_entry)
            existing_by_page[url] = new_entry

    # Drop auto-added entries whose page no longer exists. Anchor-only
    # entries (no "page" field) are hand-maintained and never removed here.
    services_item["submenu"] = [
        entry for entry in submenu
        if not entry.get("page") or entry["page"] in discovered_urls
    ]

    OUTPUT_FILE.write_text(json.dumps(seed, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Generated {OUTPUT_FILE} with {len(services_item['submenu'])} services submenu entries.")


if __name__ == "__main__":
    main()
