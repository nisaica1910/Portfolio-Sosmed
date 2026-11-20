(function () {
  var root = document.documentElement;

  // Bahasa ID / EN
  function setLang(l) {
    root.lang = l;
    try { localStorage.setItem('lang', l); } catch (e) {}
  }
  var saved = null;
  try { saved = localStorage.getItem('lang'); } catch (e) {}
  if (saved === 'en' || saved === 'id') root.lang = saved;
  document.getElementById('lang').addEventListener('click', function () {
    setLang(root.lang === 'id' ? 'en' : 'id');
  });

  // Filter karya
  document.querySelectorAll('.filter').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('.filter').forEach(function (x) { x.classList.remove('on'); });
      b.classList.add('on');
      document.querySelectorAll('.card').forEach(function (c) {
        c.hidden = !(b.dataset.f === 'all' || c.dataset.cat === b.dataset.f);
      });
    });
  });

  // Tombol kembali ke atas
  var top = document.getElementById('totop');
  function toggleTop() { top.classList.toggle('show', window.scrollY > 500); }
  window.addEventListener('scroll', toggleTop, { passive: true });
  toggleTop();
})();

(function () {
  var grid = document.querySelector('#karya .grid');
  var btn = document.getElementById('more');
  if (!grid || !btn) return;
  var cards = Array.prototype.slice.call(grid.querySelectorAll('.card'));
  var expanded = false;

  function cols() {
    return getComputedStyle(grid).gridTemplateColumns.split(' ').length;
  }
  function apply() {
    var limit = cols() * 2;
    cards.forEach(function (c, i) { c.classList.toggle('extra', !expanded && i >= limit); });
    btn.hidden = cards.length <= limit;
    btn.classList.toggle('open', expanded);
    btn.setAttribute('aria-expanded', expanded);
  }
  btn.addEventListener('click', function () {
    expanded = !expanded;
    apply();
    if (!expanded) document.getElementById('karya').scrollIntoView({ behavior: 'smooth' });
  });
  window.addEventListener('resize', apply);
  apply();
})();