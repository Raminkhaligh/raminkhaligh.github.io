(function(){
  // Dark is the default; a saved 'light' preference is the only thing that overrides it.
  function applyTheme(mode){
    document.documentElement.setAttribute('data-theme', mode);
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', mode === 'dark' ? '#0b0d10' : '#ffffff');

    var btn = document.querySelector('[data-theme-toggle]');
    if (btn) {
      var next = mode === 'dark' ? 'Switch to light mode' : 'Switch to dark mode';
      btn.setAttribute('aria-pressed', String(mode === 'dark'));
      btn.setAttribute('aria-label', next);
      btn.title = next;
    }
  }

  // Init
  window.addEventListener('DOMContentLoaded', function(){
    var saved = localStorage.getItem('theme');
    applyTheme(saved === 'light' ? 'light' : 'dark');

    var btn = document.querySelector('[data-theme-toggle]');
    if (btn) btn.addEventListener('click', function(){
      var next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      localStorage.setItem('theme', next);
      applyTheme(next);
    });
  });
})();
