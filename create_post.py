#!/usr/bin/env python3
"""
Create a new blog post from a template.
Usage: python create_post.py "Post Title" "Post Summary" "Content" "image.webp"
"""

import sys
import os
from datetime import datetime
from pathlib import Path

# Get arguments
if len(sys.argv) < 4:
    print("Usage: python create_post.py \"Title\" \"Summary\" \"Content\" [image.webp]")
    print("Example: python create_post.py \"My New Post\" \"Summary here\" \"<p>Content...</p>\" \"my-post.webp\"")
    sys.exit(1)

title = sys.argv[1]
summary = sys.argv[2]
content = sys.argv[3]
image = sys.argv[4] if len(sys.argv) > 4 else "/assets/og-cover.webp"

# Generate filename from title
filename = title.lower().replace(" ", "-").replace(",", "").replace(":", "").replace("'", "").replace("(", "").replace(")", "").replace("/", "-") + ".html"

# Generate date
date_str = datetime.now().strftime("%Y-%m-%d")

# Read template
template_path = Path("blog_template.html")
if not template_path.exists():
    print("Error: blog_template.html not found!")
    sys.exit(1)

template = template_path.read_text(encoding="utf-8")

# Replace placeholders
post_html = template.replace("{{TITLE}}", title)
post_html = post_html.replace("{{SUMMARY}}", summary)
post_html = post_html.replace("{{CONTENT}}", content)
post_html = post_html.replace("{{IMAGE}}", image)
post_html = post_html.replace("{{FILENAME}}", filename)
post_html = post_html.replace("{{PUBLISHED_DATE}}", date_str)

# Save to blog directory
output_path = Path("blog") / filename
output_path.write_text(post_html, encoding="utf-8")

print(f"✓ Blog post created: {output_path}")
print(f"  URL: https://raminkhaligh.ir/blog/{filename}")
print(f"  Title: {title}")
