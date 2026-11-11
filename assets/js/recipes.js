// Recipes and the printable cookbook (#117).
// The picked recipes are a list of slugs in localStorage, shared by the Recipes
// list (layouts/recipes/list.html), each recipe page (layouts/recipes/single.html)
// and the cookbook print page (layouts/_default/cookbook.html), which fetches
// /recipes/index.json and renders the picked recipes for printing.
(function () {
  'use strict';

  var KEY = 'bardon-cookbook';

  function load() {
    try {
      var list = JSON.parse(localStorage.getItem(KEY) || '[]');
      return Array.isArray(list) ? list.filter(function (s) { return typeof s === 'string'; }) : [];
    } catch (e) {
      return [];
    }
  }

  function save(list) {
    try {
      localStorage.setItem(KEY, JSON.stringify(list));
    } catch (e) {
      // Storage blocked (private browsing in some browsers): the page still works until it's left
    }
    refresh(list);
  }

  function add(list, slug) {
    if (list.indexOf(slug) === -1) list.push(slug);
    return list;
  }

  function remove(list, slug) {
    return list.filter(function (s) { return s !== slug; });
  }

  function all(selector) {
    return Array.prototype.slice.call(document.querySelectorAll(selector));
  }

  // Show the current selection on checkboxes, add/remove buttons and counts
  function refresh(list) {
    all('[data-cookbook-check]').forEach(function (box) {
      box.checked = list.indexOf(box.getAttribute('data-cookbook-check')) !== -1;
    });
    all('[data-cookbook-toggle]').forEach(function (btn) {
      var inBook = list.indexOf(btn.getAttribute('data-cookbook-toggle')) !== -1;
      btn.textContent = inBook ? 'Remove from cookbook' : 'Add to cookbook';
      btn.setAttribute('aria-pressed', inBook ? 'true' : 'false');
    });
    all('[data-cookbook-count]').forEach(function (el) {
      el.textContent = String(list.length);
    });
  }

  // ---- Recipes list and recipe pages ----

  function setUpPicking() {
    all('[data-cookbook-check]').forEach(function (box) {
      box.addEventListener('change', function () {
        var slug = box.getAttribute('data-cookbook-check');
        save(box.checked ? add(load(), slug) : remove(load(), slug));
      });
    });

    all('[data-cookbook-toggle]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var slug = btn.getAttribute('data-cookbook-toggle');
        var list = load();
        save(list.indexOf(slug) === -1 ? add(list, slug) : remove(list, slug));
      });
    });

    all('[data-cookbook-select-shown]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var list = load();
        all('.recipe-card').forEach(function (card) {
          if (card.hidden) return;
          var box = card.querySelector('[data-cookbook-check]');
          if (box) add(list, box.getAttribute('data-cookbook-check'));
        });
        save(list);
      });
    });

    all('[data-cookbook-clear]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        save([]);
        if (document.getElementById('cookbook')) renderCookbook();
      });
    });
  }

  function setUpTagFilter() {
    var buttons = all('[data-recipe-tag]');
    if (!buttons.length) return;
    var none = document.querySelector('.recipe-none-shown');

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var tag = btn.getAttribute('data-recipe-tag');
        buttons.forEach(function (b) {
          var on = b === btn;
          b.setAttribute('aria-pressed', on ? 'true' : 'false');
          b.classList.toggle('is-primary', on);
        });
        var shown = 0;
        all('.recipe-card').forEach(function (card) {
          var tags = (card.getAttribute('data-recipe-tags') || '').split('|');
          card.hidden = tag !== '' && tags.indexOf(tag) === -1;
          if (!card.hidden) shown++;
        });
        if (none) none.hidden = shown > 0;
      });
    });
  }

  // ---- Cookbook print page ----

  function escapeHtml(text) {
    return String(text == null ? '' : text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function facts(recipe) {
    var rows = [];
    if (recipe.servings) rows.push(['Serves', recipe.servings]);
    if (recipe.prepTime) rows.push(['Prep', recipe.prepTime]);
    if (recipe.cookTime) rows.push(['Cook', recipe.cookTime]);
    if (recipe.methods && recipe.methods.length) rows.push(['Cooked on', recipe.methods.join(', ')]);
    if (recipe.dietary && recipe.dietary.length) rows.push(['Dietary', recipe.dietary.join('; ')]);
    if (!rows.length) return '';
    return '<dl class="recipe-facts">' + rows.map(function (r) {
      return '<div><dt>' + escapeHtml(r[0]) + '</dt><dd>' + escapeHtml(r[1]) + '</dd></div>';
    }).join('') + '</dl>';
  }

  function ingredients(recipe) {
    var html = '';
    var group = null;
    (recipe.ingredients || []).forEach(function (ing) {
      var g = ing.group || '';
      if (group === null || g !== group) {
        if (group !== null) html += '</ul>';
        if (g) html += '<h3 class="recipe-group">' + escapeHtml(g) + '</h3>';
        html += '<ul class="recipe-ingredients">';
        group = g;
      }
      html += '<li>' + escapeHtml(ing.text || ing.name) + '</li>';
    });
    if (group !== null) html += '</ul>';
    return html;
  }

  function renderRecipe(recipe) {
    var html = '<article class="recipe print-item" data-recipe="' + escapeHtml(recipe.slug) + '">';
    html += '<h2 class="recipe-title">' + escapeHtml(recipe.title) + '</h2>';
    if (recipe.description) html += '<p class="recipe-description">' + escapeHtml(recipe.description) + '</p>';
    html += facts(recipe);
    if (recipe.image) {
      html += '<figure class="image recipe-image"><img src="' + escapeHtml(recipe.image) + '" alt=""></figure>';
    }
    html += '<h3>Ingredients</h3>' + ingredients(recipe);
    // The method is the recipe's own HTML, built by Hugo from the CMS Markdown
    html += '<h3>Method</h3><div class="recipe-method">' + (recipe.content || '') + '</div>';
    html += '</article>';
    return html;
  }

  // The height of one printed page's content area, in CSS pixels. Matches the
  // @page size and margins in assets/scss/_print.scss (A4, 15mm top, 20mm bottom)
  function pageHeight() {
    var probe = document.createElement('div');
    probe.style.cssText = 'position:absolute;visibility:hidden;height:262mm;width:1px;';
    document.body.appendChild(probe);
    var h = probe.offsetHeight;
    document.body.removeChild(probe);
    return h;
  }

  // A recipe taller than a page can't be kept on one page, so let it flow across
  // pages instead of jumping to a new page and leaving a gap
  function markLong() {
    var book = document.getElementById('cookbook');
    if (!book || book.hidden) return;
    var limit = pageHeight();
    // Measure at the printed width (A4 less the margins), not the screen's,
    // which is narrower on a phone and would make recipes look longer
    book.classList.add('cookbook--measure');
    all('#cookbook .recipe').forEach(function (el) {
      el.classList.toggle('long', el.getBoundingClientRect().height > limit);
    });
    book.classList.remove('cookbook--measure');
  }

  function renderCookbook() {
    var book = document.getElementById('cookbook');
    var target = book.querySelector('[data-cookbook-recipes]');
    var empty = document.querySelector('[data-cookbook-empty]');
    var error = document.querySelector('[data-cookbook-error]');
    var printBtn = document.querySelector('[data-cookbook-print]');
    var list = load();

    function show(state) {
      book.hidden = state !== 'book';
      empty.hidden = state !== 'empty';
      error.hidden = state !== 'error';
      if (printBtn) printBtn.disabled = state !== 'book';
    }

    if (!list.length) {
      target.innerHTML = '';
      show('empty');
      return;
    }

    fetch(book.getAttribute('data-cookbook-json'))
      .then(function (res) {
        if (!res.ok) throw new Error('HTTP ' + res.status);
        return res.json();
      })
      .then(function (data) {
        var bySlug = {};
        (data.recipes || []).forEach(function (r) { bySlug[r.slug] = r; });
        var picked = list.filter(function (slug) { return bySlug[slug]; });
        if (picked.length !== list.length) save(picked); // drop recipes that no longer exist
        if (!picked.length) {
          target.innerHTML = '';
          show('empty');
          return;
        }
        target.innerHTML = picked.map(function (slug) { return renderRecipe(bySlug[slug]); }).join('');
        show('book');
        markLong();
        // Images change a recipe's height once they load
        all('#cookbook img').forEach(function (img) {
          if (!img.complete) img.addEventListener('load', markLong);
        });
      })
      .catch(function () {
        show('error');
      });
  }

  function setUpCookbook() {
    if (!document.getElementById('cookbook')) return;
    renderCookbook();
    var printBtn = document.querySelector('[data-cookbook-print]');
    if (printBtn) printBtn.addEventListener('click', function () { window.print(); });
    window.addEventListener('beforeprint', markLong);
  }

  function start() {
    refresh(load());
    setUpPicking();
    setUpTagFilter();
    setUpCookbook();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
})();
