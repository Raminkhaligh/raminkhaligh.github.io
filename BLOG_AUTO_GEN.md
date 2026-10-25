# Blog Auto-Generate Feature

This system allows you to easily create new blog posts that are automatically added to the posts.json file and displayed on your website.

## How It Works

1. **Template System**: Uses a template file (`blog_template.html`) with placeholders for dynamic content
2. **Auto-Generation**: When you create a new post, the system generates the HTML file and updates `posts.json`
3. **GitHub Actions**: Automatically runs when you push changes to the repository

## Usage

### Creating a New Blog Post

Run the create script with these arguments:
```bash
python create_post.py "Post Title" "Post Summary" "HTML Content" [image.webp]
```

**Example:**
```bash
python create_post.py "My New Blog Post" "This is the summary of my blog post" "<p>This is the content...</p>" "my-post.webp"
```

**Arguments:**
- `Title` (required): The title of your blog post
- `Summary` (required): A brief summary of the post
- `Content` (required): The HTML content of your post
- `image.webp` (optional): Image filename (default: `og-cover.webp`)

### Example HTML Content

```html
<h2>Introduction</h2>
<p>Your introduction goes here...</p>

<h2>Main Point</h2>
<p>Your main point goes here...</p>

<h2>Key Takeaway</h2>
<p>Your conclusion goes here...</p>
```

## What Gets Generated

When you run `create_post.py`:

1. **HTML File**: Creates a new file in the `blog/` directory
   - Filename is automatically generated from the title
   - Contains proper meta tags, Open Graph data, and structured data

2. **posts.json**: Automatically updated with:
   - Title
   - Summary
   - Date (today's date)
   - URL (blog/filename.html)
   - Image path

3. **Homepage Cards**: Automatically updated on:
   - `index.html` (English homepage)
   - `fa/index.html` (Persian homepage)
   - `blog/index.html` (Blog hub page)

## Image Handling

Place your image files in the `blog/images/` directory:

```
blog/
├── images/
│   ├── my-post.webp
│   └── another-post.jpg
├── my-new-blog-post.html
└── posts.json
```

If no image is provided, the default `/assets/og-cover.webp` will be used.

## GitHub Actions

The workflow already runs automatically when you push to the `main` branch:

```yaml
# .github/workflows/generate-posts.yml
name: Generate and Commit Blog Posts JSON

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 2 * * 0'

jobs:
  update-posts:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Generate posts.json
        run: python3 generate_posts_json.py
      - name: Commit and push updated posts.json
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add blog/posts.json
          git commit -m "Auto-update posts.json" || echo "No changes to commit"
          git push
```

## Manual Workflow

If you need to manually update posts.json:

```bash
python generate_posts_json.py
```

This scans all HTML files in the `blog/` directory and updates `posts.json` accordingly.

## Notes

- The template already includes:
  - Proper SEO meta tags
  - Open Graph and Twitter Card data
  - Schema.org structured data (JSON-LD)
  - Table of contents sidebar
  - Reading time calculation
  - Share button functionality
- Images should be in the blog/images/ directory
- The system automatically detects Persian content for proper homepage ordering
