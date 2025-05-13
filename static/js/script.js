/**
 * Portfolio Timeline - Main JavaScript
 * Handles animations, scrolling effects, and interactions
 */

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize animation on scroll
    initScrollAnimation();
    
    // Initialize navbar scroll behavior
    initNavbarScroll();
    
    // Initialize smooth scrolling for all anchor links
    initSmoothScroll();
});

/**
 * Initialize animation for elements when they come into view
 */
function initScrollAnimation() {
    // Get all elements with animate-on-scroll class
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    
    // Create intersection observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            // Add 'visible' class when element is in view
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Unobserve element after it's animated
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,  // Trigger when 10% of the element is visible
        rootMargin: '0px 0px -50px 0px'  // Adjust trigger point
    });
    
    // Observe each animated element
    animatedElements.forEach(element => {
        observer.observe(element);
    });
    
    // Add visible class to elements already in view on page load
    setTimeout(() => {
        animatedElements.forEach(element => {
            const rect = element.getBoundingClientRect();
            if (rect.top <= window.innerHeight) {
                element.classList.add('visible');
                observer.unobserve(element);
            }
        });
    }, 100);
}

/**
 * Add scroll behavior to the navbar
 */
function initNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        // Add/remove class based on scroll position
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });
}

/**
 * Initialize smooth scrolling for all anchor links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            
            // Skip if it's just '#'
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                // Smooth scroll to the element
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                
                // Update URL without page reload
                history.pushState(null, null, targetId);
            }
        });
    });
}

/**
 * Close the mobile menu when a link is clicked
 */
document.addEventListener('click', function(e) {
    const navbarCollapse = document.querySelector('.navbar-collapse');
    const navbarToggler = document.querySelector('.navbar-toggler');
    
    // If navbar is expanded and user clicks a nav-link, collapse it
    if (navbarCollapse && navbarToggler && 
        navbarCollapse.classList.contains('show') && 
        e.target.classList.contains('nav-link')) {
        navbarToggler.click();
    }
});

/**
 * Add additional animation delay to stagger animations
 */
window.addEventListener('load', function() {
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach((card, index) => {
        card.style.transitionDelay = `${index * 0.1}s`;
    });
    
    const contactOptions = document.querySelectorAll('.contact-option');
    contactOptions.forEach((option, index) => {
        option.style.transitionDelay = `${index * 0.1}s`;
    });
});
