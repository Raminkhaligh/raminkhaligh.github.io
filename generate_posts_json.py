#!/usr/bin/env python3
"""
Auto-generate blog/posts.json for Ramin Khaligh’s portfolio site.

Scans all .html files under blog/ and extracts:
 - title from <title>
 - summary from <meta name="description">
 - og:image or default image
 - date and lastmod from git log
 - auto-detect thumbnail from blog/images/

Outputs blog/posts.json sorted by most recent date.
"""

import os, re, json, subprocess, datetime
from pathlib import Path

ROOT = Path(__file__).parent
BLOG_DIR = ROOT / "blog"
IMG_DIR = BLOG_DIR / "images"
OUTPUT_FILE = BLOG_DIR / "posts.json"
DEFAULT_IMAGE = "/assets/og-cover.png"

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
    return {
        "title": title.group(1).strip() if title else "Untitled",
        "summary": desc.group(1).strip() if desc else "",
        "image": image.group(1).strip() if image else None
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
        date = get_last_commit_date(html_file)
        image = meta["image"] or detect_thumbnail(html_file)

        posts.append({
            "title": meta["title"],
            "summary": meta["summary"],
            "date": date,
            "lastmod": date,
            "url": f"blog/{html_file.name}",
            "image": image,
            "featured": False
        })

    posts.sort(key=lambda x: x["date"], reverse=True)
    OUTPUT_FILE.write_text(json.dumps(posts, indent=2, ensure_ascii=False))
    print(f"✅ Generated {OUTPUT_FILE} with {len(posts)} posts.")

if __name__ == "__main__":
    main()
