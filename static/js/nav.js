const links = document.querySelectorAll(".nav__links a");

function updateActiveLink() {
  let current = null;
  links.forEach((link) => {
    const target = document.querySelector(link.getAttribute("href"));
    if (target && target.getBoundingClientRect().top <= 120) {
      current = link;
    }
  });
  links.forEach((link) => {
    if (link === current) {
      link.setAttribute("aria-current", "true");
    } else {
      link.removeAttribute("aria-current");
    }
  });
}

window.addEventListener("scroll", updateActiveLink, { passive: true });
updateActiveLink();