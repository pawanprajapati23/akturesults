// ============================================
// AKTU Results - Main JavaScript
// ============================================

// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const navLinks = document.querySelector('.nav-links');
  
  if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', function() {
      navLinks.classList.toggle('active');
      this.textContent = navLinks.classList.contains('active') ? '✕' : '☰';
    });
    
    // Close menu when clicking on a link
    document.querySelectorAll('.nav-links a').forEach(link => {
      link.addEventListener('click', function() {
        navLinks.classList.remove('active');
        mobileMenuBtn.textContent = '☰';
      });
    });
  }
  
  // Result Popup
  const modal = document.getElementById('resultModal');
  if (modal) {
    setTimeout(function() {
      modal.classList.add('show');
    }, 4000);
    
    const modalClose = document.querySelector('.modal-close');
    if (modalClose) {
      modalClose.addEventListener('click', function() {
        modal.classList.remove('show');
      });
    }
    
    modal.addEventListener('click', function(e) {
      if (e.target === modal) {
        modal.classList.remove('show');
      }
    });
  }
  
  // FAQ Toggle
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    item.addEventListener('click', function() {
      this.classList.toggle('active');
    });
  });
  
  // Search Functionality
  const searchBtn = document.querySelector('.search-box button');
  if (searchBtn) {
    searchBtn.addEventListener('click', function(e) {
      e.preventDefault();
      const searchInput = document.querySelector('.search-box input');
      const query = searchInput.value.toLowerCase();
      
      if (query) {
        // Redirect to relevant pages based on keywords
        if (query.includes('result')) {
          window.location.href = 'aktu-result-2026.html';
        } else if (query.includes('calculator') || query.includes('cgpa')) {
          window.location.href = 'sgpa-cgpa-calculator.html';
        } else if (query.includes('syllabus')) {
          window.location.href = 'syllabus.html';
        } else if (query.includes('paper') || query.includes('pyq')) {
          window.location.href = 'previous-papers.html';
        } else if (query.includes('admit')) {
          window.location.href = 'admit-card.html';
        } else if (query.includes('erp')) {
          window.location.href = 'erp-login.html';
        } else {
          alert('No exact match found. Try: result, calculator, syllabus, papers, admit card, erp');
        }
      }
    });
    
    // Search on Enter key
    const searchInput = document.querySelector('.search-box input');
    if (searchInput) {
      searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
          searchBtn.click();
        }
      });
    }
  }
  
  // Smooth Scroll
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
  
  // Share Buttons
  const whatsappBtn = document.querySelector('.share-btn.whatsapp');
  if (whatsappBtn) {
    whatsappBtn.addEventListener('click', function(e) {
      e.preventDefault();
      const url = encodeURIComponent(window.location.href);
      const text = encodeURIComponent('Check AKTU Results & Updates on akturesults.in');
      window.open(`https://wa.me/?text=${text}%20${url}`, '_blank');
    });
  }
  
  const telegramBtn = document.querySelector('.share-btn.telegram');
  if (telegramBtn) {
    telegramBtn.addEventListener('click', function(e) {
      e.preventDefault();
      const url = encodeURIComponent(window.location.href);
      const text = encodeURIComponent('Check AKTU Results & Updates');
      window.open(`https://t.me/share/url?url=${url}&text=${text}`, '_blank');
    });
  }
  
  // Add animation on scroll
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animation = 'fadeInUp 0.6s ease-out forwards';
      }
    });
  }, observerOptions);
  
  document.querySelectorAll('.card, .content-block').forEach(el => {
    observer.observe(el);
  });
  
  // Scroll to Top Button
  const scrollToTopBtn = document.getElementById('scrollToTop');
  if (scrollToTopBtn) {
    window.addEventListener('scroll', function() {
      if (window.pageYOffset > 300) {
        scrollToTopBtn.classList.add('show');
      } else {
        scrollToTopBtn.classList.remove('show');
      }
    });
    
    scrollToTopBtn.addEventListener('click', function() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }
});

// Smooth Scroll Behavior
document.documentElement.style.scrollBehavior = 'smooth';

// Structured Data for SEO
function addStructuredData(data) {
  const script = document.createElement('script');
  script.type = 'application/ld+json';
  script.text = JSON.stringify(data);
  document.head.appendChild(script);
}

// Page-specific structured data will be added inline in each HTML file
