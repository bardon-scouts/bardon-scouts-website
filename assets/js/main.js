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
