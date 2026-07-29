/* ============================================================
   Blog Enhancements — Ramin Khaligh (blog-post.js)
   Includes: Reading progress bar, lazy image fade-in,
   auto Table of Contents, and active section highlighting
   ============================================================ */

document.addEventListener("DOMContentLoaded", () => {

  /* ===== Reading Progress Bar ===== */
  const progressBar = document.createElement("div");
  progressBar.id = "reading-progress";
  document.body.prepend(progressBar);

  const updateProgress = () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = (scrollTop / docHeight) * 100;
    progressBar.style.width = progress + "%";
    progressBar.classList.toggle("active", scrollTop > 50);
  };
  window.addEventListener("scroll", updateProgress);
  window.addEventListener("resize", updateProgress);
  updateProgress();


  /* ===== Lazy Image Fade-in ===== */
  const lazyImages = document.querySelectorAll('img[loading="lazy"]');
  lazyImages.forEach(img => {
    if (img.complete) img.classList.add("loaded");
    else img.addEventListener("load", () => img.classList.add("loaded"));
  });


  /* ===== Auto Table of Contents ===== */
  const toc = document.querySelector("#table-of-contents ul");
  if (toc) {
    const headers = document.querySelectorAll("article h2, article h3");
    headers.forEach((h, i) => {
      const id = h.id || `section-${i}`;
      h.id = id;
      const li = document.createElement("li");
      li.innerHTML = `<a href="#${id}">${h.textContent}</a>`;
      toc.appendChild(li);
    });

    /* ===== Highlight Active Section on Scroll ===== */
    const tocLinks = toc.querySelectorAll("a");
    const highlightActive = () => {
      let current = "";
      headers.forEach(h => {
        const top = h.offsetTop - 120;
        if (window.scrollY >= top) current = h.id;
      });
      tocLinks.forEach(a => {
        a.classList.toggle("active", a.getAttribute("href") === "#" + current);
      });
    };
    window.addEventListener("scroll", highlightActive);
    highlightActive();
  }


  /* ===== Reading Time ===== */
  const article = document.querySelector("article");
  const readTimeSpan = document.getElementById("read-time");
  if (article && readTimeSpan) {
    const words = (article.innerText || article.textContent).trim().split(/\s+/).length;
    readTimeSpan.textContent = Math.ceil(words / 200) + " min read";
  }


  /* ===== Share Button (native share sheet, clipboard-copy fallback) ===== */
  const shareBtn = document.getElementById("share-btn");
  if (shareBtn) {
    const shareIcon = shareBtn.innerHTML;
    const ogTitle = document.querySelector('meta[property="og:title"]');
    shareBtn.addEventListener("click", () => {
      const shareData = {
        title: document.title,
        text: ogTitle ? ogTitle.content : document.title,
        url: window.location.href
      };
      if (navigator.share) {
        navigator.share(shareData).catch(() => {});
      } else if (navigator.clipboard) {
        navigator.clipboard.writeText(shareData.url).then(() => {
          shareBtn.innerHTML = '<span class="share-copied">Copied!</span>';
          setTimeout(() => { shareBtn.innerHTML = shareIcon; }, 2000);
        });
      }
    });
  }

});
