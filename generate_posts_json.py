#!/usr/bin/env python3
"""
Auto-generate blog/posts.json for Ramin Khaligh’s portfolio site.

Scans all .html files under blog/ and extracts:
 - title from <title>
 - summary from <meta name="description">
 - og:image or default image
 - date/lastmod from each post's own article:published_time /
   article:modified_time meta tags, falling back to git log only if a
   post doesn't have them (git history is a poor proxy for editorial
   publish date — e.g. it goes wrong entirely after a history rewrite
   or a squashed/consolidated commit)
 - auto-detect thumbnail from blog/images/

Outputs blog/posts.json sorted by most recent date.
"""

import os, re, json, subprocess, datetime
from pathlib import Path

ROOT = Path(__file__).parent
BLOG_DIR = ROOT / "blog"
IMG_DIR = BLOG_DIR / "images"
OUTPUT_FILE = BLOG_DIR / "posts.json"
DEFAULT_IMAGE = "/assets/og-cover.webp"
SITE_ORIGIN = "https://raminkhaligh.github.io"

def get_last_commit_date(path):
    try:
        result = subprocess.check_output(
            ["git", "log", "-1", "--format=%ci", str(path)],
            stderr=subprocess.DEVNULL
        )
        return result.decode().strip().split(" ")[0]
    except Exception:
        return datetime.date.today().isoformat()

def extract_meta(html):
    title = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
    desc = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', html, re.I)
    image = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\'](.*?)["\']', html, re.I)
    published = re.search(r'<meta[^>]+property=["\']article:published_time["\'][^>]+content=["\'](.*?)["\']', html, re.I)
    modified = re.search(r'<meta[^>]+property=["\']article:modified_time["\'][^>]+content=["\'](.*?)["\']', html, re.I)
    raw_title = title.group(1).strip() if title else "Untitled"
    # <title> is "Post Title | Site Name" for SEO; strip the site-name suffix
    # so cards/alt text show just the post title, not the full SEO string.
    display_title = raw_title.split("|")[0].strip() if "|" in raw_title else raw_title
    # og:image must be absolute (required by the OG spec for crawlers), but
    # the card/thumbnail render on-page from this same value, so keep it
    # root-relative here — otherwise local/staging previews try to hotlink
    # the live production asset instead of the file being edited.
    img = image.group(1).strip() if image else None
    if img and img.startswith(SITE_ORIGIN):
        img = img[len(SITE_ORIGIN):]
    return {
        "title": display_title,
        "summary": desc.group(1).strip() if desc else "",
        "image": img,
        "published": published.group(1).strip()[:10] if published else None,
        "modified": modified.group(1).strip()[:10] if modified else None,
    }

def detect_thumbnail(html_file):
    base_name = html_file.stem
    for ext in ["jpg", "jpeg", "png", "webp"]:
        candidate = IMG_DIR / f"{base_name}.{ext}"
        if candidate.exists():
            return f"blog/images/{candidate.name}"
    return DEFAULT_IMAGE

def main():
    posts = []
    for html_file in BLOG_DIR.glob("*.html"):
        if html_file.name == "index.html":
            continue

        html = html_file.read_text(encoding="utf-8", errors="ignore")
        meta = extract_meta(html)
        fallback_date = get_last_commit_date(html_file)
        date = meta["published"] or fallback_date
        lastmod = meta["modified"] or date
        image = meta["image"] or detect_thumbnail(html_file)

        posts.append({
            "title": meta["title"],
            "summary": meta["summary"],
            "date": date,
            "lastmod": lastmod,
            "url": f"blog/{html_file.name}",
            "image": image,
            "featured": False
        })

    posts.sort(key=lambda x: x["date"], reverse=True)
    OUTPUT_FILE.write_text(json.dumps(posts, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Generated {OUTPUT_FILE} with {len(posts)} posts.")

if __name__ == "__main__":
    main()
