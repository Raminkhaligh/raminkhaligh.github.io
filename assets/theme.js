(function(){
  function applyTheme(mode){
    document.documentElement.setAttribute('data-theme', mode);
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', mode === 'dark' ? '#0b0d10' : '#ffffff');

    var btn = document.querySelector('[data-theme-toggle]');
    if (btn) {
      var label = btn.querySelector('.theme-toggle__label');
      // اگر Auto است، برچسب Auto بماند؛ اگر light/dark است، همان را نشان بده
      var saved = localStorage.getItem('theme') || 'auto';
      var show = (saved === 'auto') ? 'Auto' : (mode === 'dark' ? 'Dark' : 'Light');
      if (label) label.textContent = show;
      btn.setAttribute('aria-pressed', String(mode === 'dark'));
      btn.title = (saved === 'auto')
        ? 'Theme: Auto'
        : (mode === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    }
  }

  function resolveAuto(){
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function setThemePreference(pref){ // 'light' | 'dark' | 'auto'
    localStorage.setItem('theme', pref);
    applyTheme(pref === 'auto' ? resolveAuto() : pref);
  }

  function cycleTheme(){
    var saved = localStorage.getItem('theme') || 'auto';
    var next = (saved === 'dark') ? 'light' : (saved === 'light' ? 'auto' : 'dark');
    setThemePreference(next);
  }

  // واکنش به تغییر تم سیستم در حالت Auto
  var mq;
  function attachAutoListener(){
    if (!window.matchMedia) return;
    if (mq) mq.removeEventListener('change', onSystemChange);
    mq = window.matchMedia('(prefers-color-scheme: dark)');
    mq.addEventListener('change', onSystemChange);
  }
  function onSystemChange(){
    var saved = localStorage.getItem('theme') || 'auto';
    if (saved === 'auto') applyTheme(resolveAuto());
  }

  // Init
  window.addEventListener('DOMContentLoaded', function(){
    var saved = localStorage.getItem('theme') || 'auto';
    applyTheme(saved === 'auto' ? resolveAuto() : saved);
    if (saved === 'auto') attachAutoListener();

    var btn = document.querySelector('[data-theme-toggle]');
    if (btn) btn.addEventListener('click', function(){
      cycleTheme();
      var savedNow = localStorage.getItem('theme') || 'auto';
      if (savedNow === 'auto') attachAutoListener();
      else if (mq) { mq.removeEventListener('change', onSystemChange); mq = null; }
    });
  });
})();
