/**
 * Portfolio Timeline - Main JavaScript
 * Handles animations, scrolling effects, and interactions
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize animation on scroll with better performance
    initScrollAnimation();
    
    // Initialize navbar scroll behavior
    initNavbarScroll();
    
    // Initialize smooth scrolling for all anchor links
    initSmoothScroll();
});

/**
 * Initialize animation for elements when they come into view
 * Optimized version with better performance
 */
function initScrollAnimation() {
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    const elementInView = (el, offset = 50) => {
        const elementTop = el.getBoundingClientRect().top;
        return elementTop <= window.innerHeight - offset;
    };

    // Initial check for elements
    const displayElement = (element) => {
        requestAnimationFrame(() => {
            element.classList.add('visible');
            
            // Add index to badges for staggered animation
            if (element.classList.contains('technologies') || element.classList.contains('skills-container')) {
                element.querySelectorAll('.tech-badge, .skill-badge').forEach((badge, index) => {
                    badge.style.setProperty('--badge-index', index);
                });
            }
        });
    };

    // Throttle function to limit scroll event firing
    const throttle = (func, limit = 100) => {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    };

    // Check elements on scroll with throttling
    const handleScroll = throttle(() => {
        animatedElements.forEach(element => {
            if (elementInView(element) && !element.classList.contains('visible')) {
                displayElement(element);
            }
        });
    }, 50);

    // Initial check
    setTimeout(() => {
        handleScroll();
    }, 100);

    // Add scroll listener with passive option for better performance
    window.addEventListener('scroll', handleScroll, { passive: true });
    window.addEventListener('resize', handleScroll, { passive: true });
}

/**
 * Add scroll behavior to the navbar
 */
function initNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    const throttle = (func, limit = 100) => {
        let inThrottle;
        return function() {
            if (!inThrottle) {
                func.apply(this, arguments);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    };

    const handleNavbarScroll = throttle(() => {
        requestAnimationFrame(() => {
            if (window.scrollY > 50) {
                navbar.classList.add('navbar-scrolled');
            } else {
                navbar.classList.remove('navbar-scrolled');
            }
        });
    }, 50);
    
    window.addEventListener('scroll', handleNavbarScroll, { passive: true });
}

/**
 * Initialize smooth scrolling for all anchor links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                
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
