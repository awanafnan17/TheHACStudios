/**
 * HAC Studios — Luxury Web & Motion Experience JS
 * Vanilla JS micro-interactions, scroll reveal engine, video hero & modal player
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Sticky Header Animation
  const header = document.querySelector('.site-header');
  if (header) {
    const handleScroll = () => {
      if (window.scrollY > 40) {
        header.classList.add('is-sticky');
      } else {
        header.classList.remove('is-sticky');
      }
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
  }

  // 2. Mobile Drawer Navigation
  const mobileToggle = document.querySelector('.mobile-toggle');
  const mobileDrawer = document.querySelector('.mobile-drawer');
  const drawerBackdrop = document.querySelector('.drawer-backdrop');
  const mobileCloseBtn = document.querySelector('.mobile-close-btn');

  const openDrawer = () => {
    if (mobileDrawer && drawerBackdrop) {
      mobileDrawer.classList.add('is-open');
      drawerBackdrop.classList.add('is-open');
      document.body.style.overflow = 'hidden';
    }
  };

  const closeDrawer = () => {
    if (mobileDrawer && drawerBackdrop) {
      mobileDrawer.classList.remove('is-open');
      drawerBackdrop.classList.remove('is-open');
      document.body.style.overflow = '';
    }
  };

  if (mobileToggle) mobileToggle.addEventListener('click', openDrawer);
  if (drawerBackdrop) drawerBackdrop.addEventListener('click', closeDrawer);
  if (mobileCloseBtn) mobileCloseBtn.addEventListener('click', closeDrawer);

  // Mobile submenu accordion
  document.querySelectorAll('.mobile-has-submenu > a').forEach(toggleLink => {
    toggleLink.addEventListener('click', (e) => {
      e.preventDefault();
      const parent = toggleLink.parentElement;
      const submenu = parent.querySelector('.mobile-submenu');
      if (submenu) {
        submenu.classList.toggle('is-open');
      }
    });
  });

  // 3. Scroll Reveal Engine (IntersectionObserver)
  const revealElements = document.querySelectorAll('.reveal-on-scroll');
  if ('IntersectionObserver' in window && revealElements.length > 0) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-revealed');
          observer.unobserve(entry.target);
        }
      });
    }, {
      root: null,
      threshold: 0.15,
      rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(el => revealObserver.observe(el));
  } else {
    // Fallback if IntersectionObserver unsupported
    revealElements.forEach(el => el.classList.add('is-revealed'));
  }

  // 4. Background Video Autoplay Assurance
  const heroVideo = document.querySelector('.hero-background-video');
  if (heroVideo) {
    heroVideo.muted = true;
    const playPromise = heroVideo.play();
    if (playPromise !== undefined) {
      playPromise.catch(() => {
        // If browser blocks autoplay, poster is displayed seamlessly
      });
    }
  }

  // 5. Video Modal Player
  const videoModal = document.querySelector('.video-modal');
  const playButtons = document.querySelectorAll('.video-play-btn, .hero-play-control');
  const modalCloseBtn = videoModal ? videoModal.querySelector('.modal-close-btn') : null;
  const modalVideo = videoModal ? videoModal.querySelector('video') : null;

  const openVideo = (src) => {
    if (!videoModal || !modalVideo) return;
    const videoSource = modalVideo.querySelector('source');
    if (videoSource) {
      videoSource.src = src || '/assets/videos/wedding-film-1080p.mp4';
      modalVideo.load();
    }
    videoModal.classList.add('is-active');
    document.body.style.overflow = 'hidden';
    modalVideo.play().catch(() => {});
  };

  const closeVideo = () => {
    if (!videoModal || !modalVideo) return;
    modalVideo.pause();
    videoModal.classList.remove('is-active');
    document.body.style.overflow = '';
  };

  playButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const src = btn.getAttribute('data-video-src') || '/assets/videos/wedding-film-1080p.mp4';
      openVideo(src);
    });
  });

  if (modalCloseBtn) modalCloseBtn.addEventListener('click', closeVideo);
  if (videoModal) {
    videoModal.addEventListener('click', (e) => {
      if (e.target === videoModal) closeVideo();
    });
  }

  // Escape key listener for modal
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && videoModal && videoModal.classList.contains('is-active')) {
      closeVideo();
    }
  });

  // 6. Booking Form Interactivity
  const bookingForm = document.getElementById('hac-booking-form');
  if (bookingForm) {
    bookingForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const statusBox = bookingForm.querySelector('.form-status-msg');
      const submitBtn = bookingForm.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerText = 'Previewing Inquiry...';
      }
      setTimeout(() => {
        bookingForm.reset();
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerText = 'Demo Complete';
        }
        if (statusBox) {
          statusBox.innerHTML = '<div style="margin-top: 15px; padding: 12px; background: #e8f5e9; color: #2e7d32; font-size: 14px;">Demo only: no inquiry was sent and no information was stored. Visit the live website to contact HAC Studios.</div>';
        }
      }, 800);
    });
  }
});
