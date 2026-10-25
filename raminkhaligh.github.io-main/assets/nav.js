(function () {
  var NAV_DATA_URL = '/content/nav.json';

  function buildHref(item, ctx) {
    // A dedicated page always wins, even on the homepage — submenu items
    // should navigate to their real landing page, not just scroll in-page.
    if (item.page) return item.page;
    return (ctx.isHome ? '#' : ctx.homePath + '#') + item.anchor;
  }

  function buildSubmenuAriaLabel(label, lang) {
    return lang === 'fa' ? 'نمایش زیرمنوی ' + label : 'Show ' + label + ' submenu';
  }

  function renderNavList(navList, items, ctx) {
    var html = items.map(function (item, index) {
      var label = item.label[ctx.lang] || item.label.en;
      var href = buildHref(item, ctx);

      if (item.submenu && item.submenu.length) {
        var submenuId = 'nav-submenu-' + item.id;
        var subHtml = item.submenu.map(function (sub) {
          var subLabel = sub.label[ctx.lang] || sub.label.en;
          return '<li><a href="' + buildHref(sub, ctx) + '">' + subLabel + '</a></li>';
        }).join('');
        return (
          '<li class="nav-item has-submenu">' +
            '<div class="nav-item__row">' +
              '<a href="' + href + '" class="nav-link">' + label + '</a>' +
              '<button type="button" class="submenu-toggle" aria-expanded="false" aria-controls="' + submenuId + '" aria-label="' + buildSubmenuAriaLabel(label, ctx.lang) + '">' +
                '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="m19 9-7 7-7-7" /></svg>' +
              '</button>' +
            '</div>' +
            '<ul class="submenu" id="' + submenuId + '">' + subHtml + '</ul>' +
          '</li>'
        );
      }
      return '<li class="nav-item"><a href="' + href + '" class="nav-link">' + label + '</a></li>';
    }).join('');

    navList.innerHTML = html;
  }

  function markActiveLinks(header) {
    var currentPath = window.location.pathname;
    if (currentPath.length > 1 && currentPath.endsWith('/')) {
      currentPath = currentPath.slice(0, -1);
    }
    header.querySelectorAll('.nav-link, .submenu a').forEach(function (link) {
      link.removeAttribute('aria-current');
      var href = link.getAttribute('href');
      // In-page anchors (#services) are never a distinct "current page" —
      // without this check every anchor link would match on the homepage.
      if (!href || href.charAt(0) === '#') return;
      var linkPath = new URL(href, window.location.origin).pathname;
      if (linkPath.length > 1 && linkPath.endsWith('/')) linkPath = linkPath.slice(0, -1);
      if (linkPath === currentPath) link.setAttribute('aria-current', 'page');
    });
  }

  // Scroll-spy: as the visitor scrolls a one-page layout (home/fa home),
  // highlight the section's nav-link, update the browser tab title, and
  // reflect it in the URL hash — all read straight off whatever nav-links
  // are actually in the DOM, so it works whether they came from the static
  // markup or the data-driven render above.
  function initScrollSpy(header) {
    if (!('IntersectionObserver' in window)) return;

    var lang = header.dataset.lang || 'en';
    var homePath = lang === 'fa' ? '/fa/' : '/';
    var defaultTitle = document.title;
    var titleSuffix = lang === 'fa' ? ' – رامین خلیق' : ' | Ramin Khaligh';

    var sections = [];
    header.querySelectorAll('.nav-link').forEach(function (link) {
      var href = link.getAttribute('href') || '';
      if (href.charAt(0) !== '#') return; // only true in-page anchors apply
      var el = document.getElementById(href.slice(1));
      if (el) sections.push({ id: href.slice(1), label: link.textContent.trim(), el: el, link: link });
    });
    if (!sections.length) return; // not a one-page layout (blog, services subpage, ...)

    var heroEl = document.getElementById('top');
    if (heroEl && !sections.some(function (s) { return s.el === heroEl; })) {
      sections.unshift({ id: 'top', label: null, el: heroEl, link: null });
    }

    var current;
    function setActive(section) {
      if (current === section) return;
      current = section;
      sections.forEach(function (s) { if (s.link) s.link.removeAttribute('aria-current'); });
      if (section && section.link) section.link.setAttribute('aria-current', 'page');
      document.title = (section && section.label) ? section.label + titleSuffix : defaultTitle;
      history.replaceState(null, '', (section && section.label) ? '#' + section.id : homePath);
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var match = sections.filter(function (s) { return s.el === entry.target; })[0];
        if (match) setActive(match);
      });
    }, { rootMargin: '-45% 0px -45% 0px', threshold: 0 });

    sections.forEach(function (s) { observer.observe(s.el); });
  }

  function wireSubmenuToggles(header, closeMenu) {
    header.querySelectorAll('.submenu-toggle').forEach(function (toggle) {
      toggle.addEventListener('click', function (e) {
        e.stopPropagation();
        var expanded = toggle.getAttribute('aria-expanded') === 'true';
        header.querySelectorAll('.submenu-toggle').forEach(function (t) {
          t.setAttribute('aria-expanded', 'false');
          var item = t.closest('.nav-item');
          if (item) item.classList.remove('submenu-open');
        });
        if (!expanded) {
          toggle.setAttribute('aria-expanded', 'true');
          var parentItem = toggle.closest('.nav-item');
          if (parentItem) parentItem.classList.add('submenu-open');
        }
      });
    });
    header.querySelectorAll('.nav-link, .submenu a').forEach(function (link) {
      link.addEventListener('click', closeMenu);
    });
  }

  function initNav(header) {
    var toggle = header.querySelector('[data-nav-toggle]');
    var nav = header.querySelector('.primary-nav');
    var navList = header.querySelector('.nav-list');
    if (!toggle || !nav) return;

    function closeSubmenus() {
      header.querySelectorAll('.submenu-toggle[aria-expanded="true"]').forEach(function (t) {
        t.setAttribute('aria-expanded', 'false');
        var item = t.closest('.nav-item');
        if (item) item.classList.remove('submenu-open');
      });
    }
    function closeMenu() {
      header.classList.remove('nav-open');
      toggle.setAttribute('aria-expanded', 'false');
      closeSubmenus();
    }
    function openMenu() {
      header.classList.add('nav-open');
      toggle.setAttribute('aria-expanded', 'true');
    }

    toggle.addEventListener('click', function () {
      var isOpen = header.classList.contains('nav-open');
      if (isOpen) closeMenu(); else openMenu();
    });
    document.addEventListener('click', function (e) {
      if (!header.contains(e.target)) closeMenu();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && header.classList.contains('nav-open')) {
        closeMenu();
        toggle.focus();
      }
    });
    window.matchMedia('(min-width: 901px)').addEventListener('change', function (e) {
      if (e.matches) closeMenu();
    });

    wireSubmenuToggles(header, closeMenu);
    markActiveLinks(header);

    // Data-driven nav: rebuild the link list from a single shared source so
    // adding/renaming a page only means editing content/nav.json, not every
    // page's header. If the fetch fails, the static markup above keeps working.
    if (navList) {
      var ctx = {
        lang: header.dataset.lang || 'en',
        isHome: header.dataset.home === 'true',
        homePath: header.dataset.lang === 'fa' ? '/fa/' : '/'
      };
      fetch(NAV_DATA_URL)
        .then(function (res) { return res.ok ? res.json() : null; })
        .then(function (data) {
          if (!data || !Array.isArray(data.items)) return;
          renderNavList(navList, data.items, ctx);
          wireSubmenuToggles(header, closeMenu);
          markActiveLinks(header);
        })
        .catch(function () { /* keep the static nav-list already in the page */ })
        .then(function () { initScrollSpy(header); });
    } else {
      initScrollSpy(header);
    }
  }

  var headers = document.querySelectorAll('.site-nav');
  for (var k = 0; k < headers.length; k++) initNav(headers[k]);
})();
