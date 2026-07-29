(function () {
  var ENDPOINT = 'https://api.web3forms.com/submit';
  var ICONS = {
    success: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5" /></svg>',
    error: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9" /><path d="M12 8v5M12 16h.01" /></svg>'
  };

  function setStatus(status, type, message) {
    if (!status) return;
    status.classList.remove('form-status--success', 'form-status--error');
    status.textContent = '';
    if (!message) return;
    status.classList.add('form-status--' + type);
    var icon = document.createElement('span');
    icon.className = 'form-status__icon';
    icon.setAttribute('aria-hidden', 'true');
    icon.innerHTML = ICONS[type];
    var text = document.createElement('span');
    text.textContent = message;
    status.appendChild(icon);
    status.appendChild(text);
  }

  function initContactForm(form) {
    var status = form.querySelector('.form-status');
    var button = form.querySelector('.contact-submit');
    var label = button ? button.querySelector('.contact-submit__label') : null;
    var idleLabel = (label && label.textContent) || 'Send';
    var sendingLabel = form.dataset.sendingLabel || idleLabel;
    var successMessage = form.dataset.successMessage || 'Thanks — your message is on its way.';
    var errorMessage = form.dataset.errorMessage || 'Something went wrong. Please try again.';

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (button) button.disabled = true;
      if (label) label.textContent = sendingLabel;
      setStatus(status, null, '');

      fetch(ENDPOINT, {
        method: 'POST',
        headers: { Accept: 'application/json' },
        body: new FormData(form)
      })
        .then(function (res) {
          return res.json().then(function (data) { return { ok: res.ok, data: data }; });
        })
        .then(function (result) {
          if (result.ok && result.data && result.data.success) {
            form.reset();
            setStatus(status, 'success', successMessage);
          } else {
            setStatus(status, 'error', (result.data && result.data.message) || errorMessage);
          }
        })
        .catch(function () {
          setStatus(status, 'error', errorMessage);
        })
        .then(function () {
          if (button) button.disabled = false;
          if (label) label.textContent = idleLabel;
        });
    });
  }

  document.querySelectorAll('.contact-form').forEach(initContactForm);
})();
