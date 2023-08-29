// Get the current URL path
const currentPath = window.location.pathname;

// Get all navigation links
const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

// Loop through each navigation link and add the active-link class if the href matches the current path
navLinks.forEach(link => {
    if (link.getAttribute('href') === currentPath) {
        link.classList.add('active-link');
    }
});