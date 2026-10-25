#!/usr/bin/env python3
import pathlib

template_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{{TITLE}} | Ramin Khaligh</title>
  <meta name="description" content="{{SUMMARY}}" />
  <meta name="keywords" content="{{KEYWORDS}}" />
  <meta name="language" content="en" />
  <meta name="author" content="Ramin Khaligh" />
  <link rel="canonical" href="https://raminkhaligh.ir/blog/{{FILENAME}}" />
  <meta name="robots" content="index,follow" />
  <meta property="og:title" content="{{TITLE}}" />
  <meta property="og:description" content="{{SUMMARY}}" />
  <meta property="og:type" content="article" />
  <meta property="og:image" content="https://raminkhaligh.ir{{IMAGE}}" />
  <meta property="og:url" content="https://raminkhaligh.ir/blog/{{FILENAME}}" />
  <meta property="article:published_time" content="{{PUBLISHED_DATE}}T00:00:00+00:00" />
  <meta property="article:modified_time" content="{{PUBLISHED_DATE}}T00:00:00+00:00" />
  <meta property="article:author" content="https://raminkhaligh.ir/" />
  <meta property="og:site_name" content="Ramin Khaligh Blog" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{{TITLE}}" />
  <meta name="twitter:description" content="{{SUMMARY}}" />
  <meta name="twitter:image" content="https://raminkhaligh.ir{{IMAGE}}" />
  <link rel="stylesheet" href="/assets/style.css" />
  <link rel="stylesheet" href="/assets/blog-post.css" />
</head>
<body>
  <header class="header" role="banner">
    <div class="container">
      <a href="/">Ramin Khaligh</a>
    </div>
  </header>
  <main class="container two-column">
    <div class="content-wrapper">
      <article class="card">
        <header class="post-header">
          <h1>{{TITLE}}</h1>
          <p>{{SUMMARY}}</p>
          <p>Published on <time datetime="{{PUBLISHED_DATE}}">{{PUBLISHED_DATE}}</time></p>
        </header>
        {{CONTENT}}
      </article>
    </div>
    <aside class="sidebar">
      <nav id="table-of-contents">
        <strong>On this page</strong>
        <ul></ul>
      </nav>
    </aside>
  </main>
  <footer class="footer">
    <p>© 2026 Ramin Khaligh</p>
  </footer>
  <script src="/assets/theme.js" defer></script>
  <script src="/assets/nav.js" defer></script>
  <script src="/assets/blog-post.js" defer></script>
</body>
</html>'''

pathlib.Path('blog_template.html').write_text(template_content, encoding='utf-8')
print('Template created successfully!')
