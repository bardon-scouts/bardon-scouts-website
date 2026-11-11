// Navbar burger toggle
document.addEventListener('DOMContentLoaded', () => {
  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Add a click event on each of them
  $navbarBurgers.forEach( el => {
    el.addEventListener('click', () => {
      // Get the target from the "data-target" attribute
      const target = el.dataset.target;
      const $target = document.getElementById(target);

      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      el.classList.toggle('is-active');
      $target.classList.toggle('is-active');
    });
  });

  // Navbar dropdown toggle for mobile
  const dropdowns = document.querySelectorAll('.navbar-item.has-dropdown');

  dropdowns.forEach(dropdown => {
    const link = dropdown.querySelector('.navbar-link');

    link.addEventListener('click', (e) => {
      // Only prevent default on mobile (< 1024px)
      const isMobile = window.matchMedia('(max-width: 1023px)').matches;

      if (isMobile) {
        e.preventDefault();

        // Toggle this dropdown
        dropdown.classList.toggle('is-active');

        // Close other dropdowns
        dropdowns.forEach(other => {
          if (other !== dropdown) {
            other.classList.remove('is-active');
          }
        });
      }
    });
  });
});

// Home page carousel (#122). The slides stack without JavaScript; this adds
// tabs, previous and next arrows, and a slow auto-advance that pauses on
// hover or focus, stops once someone uses the controls, and is off for
// people who turn off motion.
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-carousel]').forEach((carousel, n) => {
    const slides = Array.from(carousel.querySelectorAll('[data-carousel-slide]'));
    const controls = carousel.querySelector('.carousel-controls');
    const tablist = carousel.querySelector('.carousel-tabs');
    if (slides.length < 2 || !controls || !tablist) return;

    const tabs = slides.map((slide, i) => {
      const tab = document.createElement('button');
      tab.type = 'button';
      tab.className = 'carousel-tab';
      tab.textContent = slide.dataset.label || 'Slide ' + (i + 1);
      tab.setAttribute('role', 'tab');
      tab.id = 'carousel-' + n + '-tab-' + i;
      tab.setAttribute('aria-controls', slide.id);
      slide.setAttribute('role', 'tabpanel');
      slide.setAttribute('aria-labelledby', tab.id);
      tab.addEventListener('click', () => { stop(); show(i); });
      tab.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
          e.preventDefault();
          stop();
          show(current + (e.key === 'ArrowRight' ? 1 : -1));
          tabs[current].focus();
        }
      });
      tablist.appendChild(tab);
      return tab;
    });

    let current = 0;
    function show(i) {
      current = (i + slides.length) % slides.length;
      slides.forEach((slide, j) => {
        const active = j === current;
        slide.hidden = !active;
        slide.classList.toggle('is-active', active);
        tabs[j].setAttribute('aria-selected', active ? 'true' : 'false');
        tabs[j].tabIndex = active ? 0 : -1;
      });
    }

    let timer = null;
    let stopped = false;
    let paused = false;
    const interval = parseInt(carousel.dataset.interval, 10) || 9000;
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function stop() {
      stopped = true;
      clearInterval(timer);
    }
    if (!reduceMotion) {
      timer = setInterval(() => {
        if (!stopped && !paused && !document.hidden) show(current + 1);
      }, interval);
    }
    carousel.addEventListener('mouseenter', () => { paused = true; });
    carousel.addEventListener('mouseleave', () => { paused = false; });
    carousel.addEventListener('focusin', () => { paused = true; });
    carousel.addEventListener('focusout', () => { paused = false; });

    carousel.querySelector('[data-carousel-prev]').addEventListener('click', () => { stop(); show(current - 1); });
    carousel.querySelector('[data-carousel-next]').addEventListener('click', () => { stop(); show(current + 1); });

    controls.hidden = false;
    carousel.classList.add('is-enhanced');
    show(0);
  });
});
