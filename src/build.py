#!/usr/bin/env python3
"""
HAC Studios — Authoritative Static Site Compiler (V2 High-Fidelity Esthetic Motion Rebuild)
Compiles all 15 clean routes with content-hashed assets, SEO tags, sitemap, and robots.txt.
Matches Esthetic reference motion, background video, keyframes, typography, and section flow.
"""

import json
import hashlib
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
DATA_FILE = SRC / "data" / "media-selection.json"

# Load media catalog
media_data = json.loads(DATA_FILE.read_text(encoding='utf-8'))

CANONICAL_DOMAIN = "https://thehacstudios.com"
BRAND_NAME = "HAC Studios"
TAGLINE = "Luxury Wedding Photography & Cinematography"

# Calculate Asset Hashes dynamically from fresh file contents
css_content = (SRC / "assets" / "css" / "style.css").read_bytes()
js_content = (SRC / "assets" / "js" / "main.js").read_bytes()

CSS_HASH = hashlib.sha256(css_content).hexdigest()[:8]
JS_HASH = hashlib.sha256(js_content).hexdigest()[:8]

CSS_FILENAME = f"style.{CSS_HASH}.css"
JS_FILENAME = f"main.{JS_HASH}.js"

def get_head(title: str, description: str, canonical_path: str, og_image: str = "/assets/images/portfolio/c01-01-large.webp") -> str:
    full_title = f"{title} | {BRAND_NAME}" if title != BRAND_NAME else f"{BRAND_NAME} | {TAGLINE}"
    canonical_url = f"{CANONICAL_DOMAIN}{canonical_path}"
    full_og_image = f"{CANONICAL_DOMAIN}{og_image}" if og_image.startswith("/") else og_image

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{full_title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical_url}">
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{full_og_image}">
  <meta property="og:site_name" content="{BRAND_NAME}">
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{full_title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{full_og_image}">
  
  <!-- Favicons -->
  <link rel="icon" type="image/x-icon" href="/assets/images/favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/images/favicon.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/images/apple-touch-icon.png">
  
  <!-- Core Content-Hashed Stylesheet -->
  <link rel="stylesheet" href="/assets/css/{CSS_FILENAME}">
</head>
<body>
"""

def get_header(active_route: str = "/", is_solid: bool = False) -> str:
    header_class = "site-header solid-header" if is_solid else "site-header"
    
    return f"""  <!-- Site Header (Single Navigation, Esthetic Alignment) -->
  <header class="{header_class}">
    <div class="container">
      <div class="header-inner">
        <a href="/" class="brand-logo" aria-label="{BRAND_NAME} Home">
          <img src="/assets/images/logo-light.png" alt="{BRAND_NAME}" class="logo-light" width="160" height="42">
          <img src="/assets/images/logo-dark.png" alt="{BRAND_NAME}" class="logo-dark" width="160" height="42">
        </a>

        <nav class="nav-menu" aria-label="Main Navigation">
          <div class="nav-item {'active' if active_route in ['/', '/home-2/'] else ''}">
            <a href="/" class="nav-link">Home <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor"><path d="M1 1L5 5L9 1"/></svg></a>
            <div class="dropdown-menu">
              <a href="/" class="dropdown-link">Home Layout 1</a>
              <a href="/home-2/" class="dropdown-link">Home Layout 2 (Films)</a>
            </div>
          </div>

          <div class="nav-item {'active' if active_route == '/about/' else ''}">
            <a href="/about/" class="nav-link">About</a>
          </div>

          <div class="nav-item {'active' if active_route in ['/portfolio/', '/portfolio-2/', '/portfolio-story/'] else ''}">
            <a href="/portfolio/" class="nav-link">Portfolio <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor"><path d="M1 1L5 5L9 1"/></svg></a>
            <div class="dropdown-menu">
              <a href="/portfolio/" class="dropdown-link">Portfolio Style 1</a>
              <a href="/portfolio-2/" class="dropdown-link">Portfolio Style 2</a>
              <a href="/portfolio-story/" class="dropdown-link">Single Story</a>
            </div>
          </div>

          <div class="nav-item {'active' if active_route in ['/services/', '/our-team/', '/pricing/', '/faq/'] else ''}">
            <a href="/services/" class="nav-link">Pages <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor"><path d="M1 1L5 5L9 1"/></svg></a>
            <div class="dropdown-menu">
              <a href="/services/" class="dropdown-link">Services</a>
              <a href="/our-team/" class="dropdown-link">Our Team</a>
              <a href="/pricing/" class="dropdown-link">Pricing & Packages</a>
              <a href="/faq/" class="dropdown-link">FAQ</a>
            </div>
          </div>

          <div class="nav-item {'active' if active_route in ['/stories/', '/story/'] else ''}">
            <a href="/stories/" class="nav-link">Stories <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor"><path d="M1 1L5 5L9 1"/></svg></a>
            <div class="dropdown-menu">
              <a href="/stories/" class="dropdown-link">Stories & Journal</a>
              <a href="/story/" class="dropdown-link">Featured Story</a>
            </div>
          </div>

          <div class="nav-item {'active' if active_route == '/contact/' else ''}">
            <a href="/contact/" class="nav-link">Contact</a>
          </div>
        </nav>

        <div class="header-actions">
          <a href="/contact/" class="btn header-btn">Book Now</a>
          <button class="mobile-toggle" aria-label="Toggle Mobile Navigation">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Mobile Off-canvas Drawer -->
  <div class="drawer-backdrop"></div>
  <aside class="mobile-drawer" aria-label="Mobile Navigation">
    <div class="mobile-drawer-header">
      <a href="/" class="brand-logo" aria-label="{BRAND_NAME}">
        <img src="/assets/images/logo-light.png" alt="{BRAND_NAME}" width="140" height="36">
      </a>
      <span class="mobile-close-btn">&times;</span>
    </div>

    <ul class="mobile-nav-list">
      <li class="mobile-nav-item mobile-has-submenu">
        <a href="/" class="mobile-nav-link">Home <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor"><path d="M1 1L5 5L9 1"/></svg></a>
        <div class="mobile-submenu">
          <a href="/" class="mobile-sublink">Home Layout 1</a>
          <a href="/home-2/" class="mobile-sublink">Home Layout 2 (Films)</a>
        </div>
      </li>
      <li class="mobile-nav-item"><a href="/about/" class="mobile-nav-link">About</a></li>
      <li class="mobile-nav-item mobile-has-submenu">
        <a href="/portfolio/" class="mobile-nav-link">Portfolio <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor"><path d="M1 1L5 5L9 1"/></svg></a>
        <div class="mobile-submenu">
          <a href="/portfolio/" class="mobile-sublink">Portfolio Style 1</a>
          <a href="/portfolio-2/" class="mobile-sublink">Portfolio Style 2</a>
          <a href="/portfolio-story/" class="mobile-sublink">Single Story</a>
        </div>
      </li>
      <li class="mobile-nav-item mobile-has-submenu">
        <a href="/services/" class="mobile-nav-link">Pages <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor"><path d="M1 1L5 5L9 1"/></svg></a>
        <div class="mobile-submenu">
          <a href="/services/" class="mobile-sublink">Services</a>
          <a href="/our-team/" class="mobile-sublink">Our Team</a>
          <a href="/pricing/" class="mobile-sublink">Pricing</a>
          <a href="/faq/" class="mobile-sublink">FAQ</a>
        </div>
      </li>
      <li class="mobile-nav-item mobile-has-submenu">
        <a href="/stories/" class="mobile-nav-link">Stories <svg width="10" height="6" viewBox="0 0 10 6" fill="currentColor"><path d="M1 1L5 5L9 1"/></svg></a>
        <div class="mobile-submenu">
          <a href="/stories/" class="mobile-sublink">Journal Grid</a>
          <a href="/story/" class="mobile-sublink">Featured Story</a>
        </div>
      </li>
      <li class="mobile-nav-item"><a href="/contact/" class="mobile-nav-link">Contact</a></li>
    </ul>

    <div class="mobile-drawer-footer">
      <a href="/contact/" class="btn btn-primary" style="width: 100%; text-align: center;">Inquire Date</a>
    </div>
  </aside>
"""

def get_footer() -> str:
    footer_thumbs = [
        "/assets/images/portfolio/c01-01-thumb.webp",
        "/assets/images/portfolio/fe-0480-thumb.webp",
        "/assets/images/portfolio/fe-0528-thumb.webp",
        "/assets/images/portfolio/c01-07-thumb.webp",
        "/assets/images/portfolio/fe-0682-thumb.webp",
        "/assets/images/portfolio/fe-0777-thumb.webp"
    ]
    thumbs_html = "".join([
        f"""            <a href="/portfolio-story/" class="footer-thumb">
              <img src="{src}" alt="HAC Studios Wedding Moment" loading="lazy" width="90" height="90">
            </a>\n""" for src in footer_thumbs
    ])

    return f"""  <!-- Site Footer (Esthetic Luxury Dark Footer) -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-top-grid reveal-on-scroll">
        <div class="footer-brand">
          <a href="/" aria-label="{BRAND_NAME}">
            <img src="/assets/images/logo-light.png" alt="{BRAND_NAME}" width="150" height="38">
          </a>
          <p>Documenting luxury wedding narratives, authentic emotion, and timeless heirlooms across Pakistan and destination celebrations worldwide.</p>
        </div>

        <div class="footer-col">
          <h4 class="footer-heading">Other Pages</h4>
          <div class="footer-links">
            <a href="/" class="footer-link">Home</a>
            <a href="/about/" class="footer-link">About Us</a>
            <a href="/services/" class="footer-link">Services</a>
            <a href="/portfolio/" class="footer-link">Portfolio</a>
            <a href="/stories/" class="footer-link">Blog & Stories</a>
            <a href="/contact/" class="footer-link">Contact Us</a>
          </div>
        </div>

        <div class="footer-col">
          <h4 class="footer-heading">Experience</h4>
          <div class="footer-links">
            <a href="/pricing/" class="footer-link">Pricing Packages</a>
            <a href="/our-team/" class="footer-link">Our Creative Team</a>
            <a href="/faq/" class="footer-link">FAQ</a>
            <a href="/portfolio-2/" class="footer-link">Filterable Gallery</a>
            <a href="/privacy-policy/" class="footer-link">Privacy Policy</a>
            <a href="/terms/" class="footer-link">Terms & Conditions</a>
          </div>
        </div>

        <div class="footer-col">
          <h4 class="footer-heading">Selected Frames</h4>
          <div class="footer-gallery-grid">
{thumbs_html}          </div>
        </div>
      </div>

      <div class="footer-bottom-bar">
        <p>&copy; 2026 {BRAND_NAME}. Luxury Wedding Photography & Cinematography. All rights reserved.</p>
        <div class="footer-legal-links">
          <a href="/privacy-policy/">Privacy Policy</a> &bull; 
          <a href="/terms/">Terms of Service</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Video Player Modal -->
  <div class="video-modal modal-backdrop" role="dialog" aria-modal="true" aria-label="Cinematic Film Player">
    <span class="modal-close-btn" aria-label="Close Video Player">&times;</span>
    <div class="modal-container">
      <video controls playsinline preload="metadata">
        <source src="/assets/videos/wedding-film-1080p.mp4" type="video/mp4">
      </video>
    </div>
  </div>

  <!-- Content-Hashed Main JavaScript -->
  <script src="/assets/js/{JS_FILENAME}"></script>
</body>
</html>
"""

# ==============================================================================
# HOMEPAGE BUILDER (Layout 1: High-Fidelity Esthetic Rebuild)
# ==============================================================================

def build_home() -> str:
    # 4 curated portfolio cards for homepage
    home_portfolio_items = media_data["portfolio_items"][:4]
    portfolio_cards_html = ""
    for item in home_portfolio_items:
        portfolio_cards_html += f"""        <div class="portfolio-card-item reveal-on-scroll">
          <div class="portfolio-card-img-wrap">
            <img src="{item['image']}" alt="{item['alt']}" loading="lazy">
          </div>
          <div class="portfolio-card-info">
            <span class="portfolio-card-cat">{item['category']}</span>
            <h3 class="portfolio-card-title"><a href="{item['url']}">{item['title']}</a></h3>
            <a href="{item['url']}" class="btn-link">View Story &rarr;</a>
          </div>
        </div>\n"""

    # 3 stories cards for homepage
    journal_cards_html = ""
    for story in media_data["stories"][:3]:
        journal_cards_html += f"""        <div class="story-card-item reveal-on-scroll">
          <div class="story-card-media">
            <img src="{story['image']}" alt="{story['title']}" loading="lazy">
          </div>
          <div class="story-card-content">
            <span class="story-card-date">{story['date']}</span>
            <h3 class="story-card-title"><a href="{story['url']}">{story['title']}</a></h3>
            <p class="story-card-excerpt">{story['excerpt']}</p>
            <a href="{story['url']}" class="btn-link">Read Story &rarr;</a>
          </div>
        </div>\n"""

    return f"""{get_head("Timeless Wedding Photography & Films", "HAC Studios documents luxury weddings and cinematic films with an editorial, timeless approach.", "/", "/assets/images/portfolio/c01-01-large.webp")}
{get_header("/", is_solid=False)}

  <!-- 01 Hero Section (Esthetic Motion Architecture) -->
  <section class="hero">
    <div class="hero-media-wrapper">
      <video autoplay muted loop playsinline preload="metadata" poster="/assets/images/hero-video-poster.webp" class="hero-background-video">
        <source src="/assets/videos/hero-background-loop.mp4" type="video/mp4">
      </video>
      <div class="hero-overlay"></div>
      <div class="hero-grid-overlay"></div>
    </div>

    <!-- Left Social Rail -->
    <div class="hero-social-rail motion-fade-in delay-100">
      <a href="https://instagram.com/" target="_blank" rel="noopener noreferrer" class="hero-social-link" aria-label="Instagram">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
      </a>
      <a href="https://vimeo.com/" target="_blank" rel="noopener noreferrer" class="hero-social-link" aria-label="Vimeo">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
      </a>
    </div>

    <!-- Right Play Control -->
    <div class="hero-play-control motion-fade-in delay-500" data-video-src="/assets/videos/wedding-film-1080p.mp4">
      <div class="hero-play-btn">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
      </div>
      <span class="hero-play-label">Play</span>
    </div>

    <div class="container hero-content">
      <span class="hero-tag motion-fade-in">Wedding Photography & Cinematography</span>
      <h1 class="display-title hero-primary-title motion-fade-down delay-100">Make Your Wedding Story<br>Timeless</h1>
      <div class="hero-script-layer motion-fade-up delay-300">Wedding<br>Photography</div>
      <div class="hero-cta motion-fade-up delay-700">
        <a href="/portfolio/" class="btn btn-hero">View Portfolio</a>
      </div>
    </div>
  </section>

  <!-- 02 Floating Wedding Videography Teaser Card -->
  <div class="container teaser-card-wrapper reveal-on-scroll">
    <div class="teaser-card">
      <div class="teaser-card-left">
        <span class="section-subtitle">Wedding Videography</span>
        <h5>Cinematic Wedding Films That Immortalize Emotion</h5>
      </div>
      <div class="teaser-card-right">
        <p>Every frame is recorded with 4K clarity, authentic color science, and cinematic motion that captures the unspoken emotion of your celebration.</p>
        <button class="btn-link video-play-btn" data-video-src="/assets/videos/wedding-film-1080p.mp4">Watch Highlight Reel &rarr;</button>
      </div>
    </div>
  </div>

  <!-- 03 & 04 About Introduction & Service Blocks -->
  <section class="section bg-white" style="padding-top: 20px;">
    <div class="container">
      <div class="about-service-grid reveal-on-scroll">
        <div class="about-intro-col">
          <span class="section-subtitle">About Us</span>
          <h2>I’m Hassan, Lead Storyteller at HAC Studios</h2>
          <p class="lead-p">We believe that real luxury lies in authentic, unposed connection. For over a decade, our studio has captured timeless love stories, framing history with refined elegance and editorial sophistication.</p>
          <a href="/about/" class="btn btn-primary">Discover More</a>
        </div>

        <div class="about-services-col">
          <div class="service-block-card">
            <span class="section-subtitle">01 / Service</span>
            <h5>Wedding Photography</h5>
            <p>Editorial documentary coverage capturing grand ceremonies, quiet embraces, and heirloom portraits that remain timeless for generations.</p>
            <a href="/services/" class="btn-link">Read More &rarr;</a>
          </div>

          <div class="service-block-card">
            <span class="section-subtitle">02 / Service</span>
            <h5>Photo Retouching & Heirloom Editing</h5>
            <p>Artisanal fine-art post-production and true-to-life skin tones that celebrate natural light and authentic elegance.</p>
            <a href="/services/" class="btn-link">Read More &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 05 Large Editorial Image Treatment Banner -->
  <section class="editorial-banner-section reveal-on-scroll">
    <div class="editorial-banner-bg">
      <img src="{media_data['roles']['about_main']['image']}" alt="HAC Studios Editorial Feature" loading="lazy">
    </div>
    <div class="editorial-banner-content">
      <span class="section-subtitle text-light">Capturing The Moment</span>
      <h2>Creating Timeless Visual Poetry For Modern Romantics</h2>
      <a href="/portfolio-story/" class="btn btn-outline-light" style="margin-top: 10px;">Explore Story</a>
    </div>
  </section>

  <!-- 06 Portfolio / Projects Showcase Grid -->
  <section class="section bg-white">
    <div class="container">
      <div class="text-center reveal-on-scroll" style="max-width: 650px; margin: 0 auto 50px;">
        <span class="section-subtitle">Curated Works</span>
        <h2 class="section-title">Selected Wedding Stories</h2>
        <p class="lead-p">Explore recent bridal portraits, ceremony highlights, and editorial narratives captured across exquisite locations.</p>
      </div>

      <div class="portfolio-grid-layout">
{portfolio_cards_html}      </div>

      <div class="text-center reveal-on-scroll" style="margin-top: 50px;">
        <a href="/portfolio/" class="btn btn-outline">View All Projects</a>
      </div>
    </div>
  </section>

  <!-- 07 Testimonial / Story Area -->
  <section class="section testimonial-section">
    <div class="container">
      <div class="testimonial-card-centered reveal-on-scroll">
        <div class="testimonial-quote-icon">&ldquo;</div>
        <p class="testimonial-quote-text">Wow, we are both completely blown away. These photos and cinematic film are beyond breathtaking. Thank you HAC Studios for capturing the soul of our day so perfectly.</p>
        <h4 class="testimonial-author-name">Abdulrehman & Zainish</h4>
        <span class="testimonial-author-role">Bride & Groom &bull; Lahore</span>
      </div>
    </div>
  </section>

  <!-- 08 Partner / Collaboration Presentation -->
  <div class="partners-section">
    <div class="container">
      <div class="partners-grid reveal-on-scroll">
        <span class="partner-logo-item">Vogue Weddings</span>
        <span class="partner-logo-item">Harper's Bazaar</span>
        <span class="partner-logo-item">Bridal Couture</span>
        <span class="partner-logo-item">The Heritage Club</span>
        <span class="partner-logo-item">Luxe Destinations</span>
      </div>
    </div>
  </div>

  <!-- 09 Pricing Packages -->
  <section class="section bg-white" id="pricing">
    <div class="container">
      <div class="text-center reveal-on-scroll" style="max-width: 650px; margin: 0 auto;">
        <span class="section-subtitle">Pricing</span>
        <h2 class="section-title">Choose Your Packages</h2>
        <p class="lead-p">Bespoke photography and cinematography collections tailored to your wedding itinerary.</p>
      </div>

      <div class="pricing-cards-grid reveal-on-scroll">
        <!-- Essential -->
        <div class="pricing-card-box">
          <h3 class="pricing-card-name">Essential</h3>
          <p class="pricing-card-desc">Intimate Celebrations & Nikkah Events</p>
          <div class="pricing-card-price">Custom Quote</div>
          <ul class="pricing-features-list">
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> 1 Lead Wedding Photographer</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Up to 6 Hours Coverage</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> 200+ Master Edited Photos</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Online Heirloom Gallery</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> High-Resolution Digital Delivery</li>
          </ul>
          <a href="/contact/" class="btn btn-outline" style="width: 100%;">Inquire Now</a>
        </div>

        <!-- Signature (Featured) -->
        <div class="pricing-card-box featured">
          <h3 class="pricing-card-name">Signature</h3>
          <p class="pricing-card-desc">Complete Photo & 4K Cinema Film</p>
          <div class="pricing-card-price">Custom Quote</div>
          <ul class="pricing-features-list">
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> 2 Lead Photographers & 1 Cinematographer</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Full Day Coverage (Up to 10 Hours)</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> 4K Cinematic Highlight Film</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Bridal Editorial Session Included</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Fine-Art Handcrafted Album Proof</li>
          </ul>
          <a href="/contact/" class="btn btn-hero" style="width: 100%;">Inquire Signature</a>
        </div>

        <!-- Royal Heirloom -->
        <div class="pricing-card-box">
          <h3 class="pricing-card-name">Royal Heirloom</h3>
          <p class="pricing-card-desc">Multi-Day Grand Celebration Production</p>
          <div class="pricing-card-price">Custom Quote</div>
          <ul class="pricing-features-list">
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Full Creative Crew (Photo + Cinema)</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Multi-Day Complete Coverage</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Feature-Length Film + Teaser Reels</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Drone Aerial Cinematography</li>
            <li><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Bespoke Italian Leather Album</li>
          </ul>
          <a href="/contact/" class="btn btn-outline" style="width: 100%;">Inquire Royal</a>
        </div>
      </div>
    </div>
  </section>

  <!-- 10 Booking & Inquire CTA -->
  <section class="section booking-section-wrapper" id="booking">
    <div class="container">
      <div class="booking-split-grid reveal-on-scroll">
        <div class="booking-info-box">
          <span class="section-subtitle">Get In Touch</span>
          <h2>Are you ready to immortalize your story?</h2>
          <p class="lead-p">Dates for upcoming wedding seasons fill quickly. Tell us about your celebration, venue, and vision, and our creative directors will connect with you.</p>
          <div style="margin-top: 20px;">
            <p style="font-family: var(--font-serif); font-size: 18px; font-weight: 700; color: var(--color-text-dark);">HAC Studios Creative Headquarters</p>
            <p style="color: var(--color-text-muted); font-size: 14px;">Lahore &bull; Islamabad &bull; Worldwide Travel</p>
          </div>
        </div>

        <div class="booking-form-card">
          <form id="hac-booking-form">
            <div class="form-grid-2">
              <div class="form-field">
                <label class="form-label" for="book-name">Your Name *</label>
                <input type="text" id="book-name" class="form-input" placeholder="e.g. Sarah & David" required>
              </div>

              <div class="form-field">
                <label class="form-label" for="book-email">Email Address *</label>
                <input type="email" id="book-email" class="form-input" placeholder="name@domain.com" required>
              </div>

              <div class="form-field">
                <label class="form-label" for="book-phone">Phone Number</label>
                <input type="tel" id="book-phone" class="form-input" placeholder="+92 300 0000000">
              </div>

              <div class="form-field">
                <label class="form-label" for="book-date">Wedding Date</label>
                <input type="date" id="book-date" class="form-input">
              </div>

              <div class="form-field form-group-full">
                <label class="form-label" for="book-service">Service Required</label>
                <select id="book-service" class="form-select">
                  <option value="both">Photography & Cinematography (Recommended)</option>
                  <option value="photo">Wedding Photography Only</option>
                  <option value="film">Wedding Cinematography Only</option>
                  <option value="bridal">Bridal Portrait Session</option>
                </select>
              </div>

              <div class="form-field form-group-full">
                <label class="form-label" for="book-message">Wedding Vision & Details *</label>
                <textarea id="book-message" class="form-textarea" placeholder="Share your venue, celebration style, and special moments..." required></textarea>
              </div>

              <div class="form-field form-group-full">
                <button type="submit" class="btn btn-primary" style="width: 100%; padding: 14px;">Send Booking Inquiry</button>
              </div>
            </div>
            <div class="form-status-msg" role="status" aria-live="polite"></div>
          </form>
        </div>
      </div>
    </div>
  </section>

  <!-- 11 Stories & Articles Grid -->
  <section class="section bg-secondary">
    <div class="container">
      <div class="text-center reveal-on-scroll" style="max-width: 650px; margin: 0 auto 30px;">
        <span class="section-subtitle">Our Blog</span>
        <h2 class="section-title">Latest Blog & Articles</h2>
        <p class="lead-p">Insights into wedding photography, lighting artistry, and cinematic film craft.</p>
      </div>

      <div class="stories-grid-3">
{journal_cards_html}      </div>
    </div>
  </section>

{get_footer()}
"""

# ==============================================================================
# HOME 2 BUILDER (Layout 2: Moving Cinematic Films & Full Motion)
# ==============================================================================

def build_home_2() -> str:
    return f"""{get_head("Home Layout 2 (Cinematic Films)", "Cinematic wedding films and moving narratives by HAC Studios.", "/home-2/", "/assets/images/portfolio/fe-0771-large.webp")}
{get_header("/home-2/", is_solid=False)}

  <!-- Home 2 Full-Viewport Cinematic Motion Hero -->
  <section class="hero">
    <div class="hero-media-wrapper">
      <video autoplay muted loop playsinline preload="metadata" poster="/assets/images/hero-video-poster.webp" class="hero-background-video">
        <source src="/assets/videos/hero-background-loop.mp4" type="video/mp4">
      </video>
      <div class="hero-overlay"></div>
      <div class="hero-grid-overlay"></div>
    </div>

    <!-- Left Social Rail -->
    <div class="hero-social-rail motion-fade-in delay-100">
      <a href="https://instagram.com/" target="_blank" rel="noopener noreferrer" class="hero-social-link" aria-label="Instagram">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
      </a>
      <a href="https://vimeo.com/" target="_blank" rel="noopener noreferrer" class="hero-social-link" aria-label="Vimeo">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
      </a>
    </div>

    <!-- Right Play Control -->
    <div class="hero-play-control motion-fade-in delay-500" data-video-src="/assets/videos/wedding-film-1080p.mp4">
      <div class="hero-play-btn">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
      </div>
      <span class="hero-play-label">Play</span>
    </div>

    <div class="container hero-content">
      <span class="hero-tag motion-fade-in">Cinematic Motion Picture</span>
      <h1 class="display-title hero-primary-title motion-fade-down delay-100">Make Your Wedding Story<br>Timeless</h1>
      <div class="hero-script-layer motion-fade-up delay-300">Wedding<br>Cinema</div>
      <div class="hero-cta motion-fade-up delay-700">
        <button class="btn btn-hero video-play-btn" data-video-src="/assets/videos/wedding-film-1080p.mp4">Watch Featured Film</button>
      </div>
    </div>
  </section>

{get_footer()}
"""

# ==============================================================================
# INNER PAGES
# ==============================================================================

def build_about() -> str:
    return f"""{get_head("About Studio & Vision", "Learn about HAC Studios' philosophy of luxury wedding photography and storytelling.", "/about/", "/assets/images/portfolio/fe-0466-large.webp")}
{get_header("/about/", is_solid=True)}

  <section class="section bg-white" style="padding-top: 60px;">
    <div class="container">
      <div class="about-service-grid reveal-on-scroll">
        <div class="about-intro-col">
          <span class="section-subtitle">About Studio</span>
          <h2>Capturing Moments, Framing Memories Across Generations</h2>
          <p class="lead-p">HAC Studios was founded on a singular conviction: that wedding photography should transcend trends to become timeless heirloom art.</p>
          <p style="color: var(--color-text-muted); margin-bottom: 24px;">With mastery in natural lighting, refined editorial composition, and organic storytelling, our team preserves the true grandeur and genuine heart of your day.</p>
          <a href="/contact/" class="btn btn-primary">Book Consultation</a>
        </div>
        <div>
          <img src="{media_data['roles']['about_main']['image']}" alt="About HAC Studios" style="box-shadow: var(--shadow-hover);">
        </div>
      </div>
    </div>
  </section>

{get_footer()}
"""

def build_portfolio() -> str:
    items_html = ""
    for item in media_data["portfolio_items"]:
        items_html += f"""        <div class="portfolio-card-item reveal-on-scroll">
          <div class="portfolio-card-img-wrap">
            <img src="{item['image']}" alt="{item['alt']}" loading="lazy">
          </div>
          <div class="portfolio-card-info">
            <span class="portfolio-card-cat">{item['category']}</span>
            <h3 class="portfolio-card-title"><a href="{item['url']}">{item['title']}</a></h3>
            <a href="{item['url']}" class="btn-link">View Story &rarr;</a>
          </div>
        </div>\n"""

    return f"""{get_head("Portfolio Style 1", "Explore HAC Studios luxury wedding photography and cinematic portfolios.", "/portfolio/", "/assets/images/portfolio/c01-01-large.webp")}
{get_header("/portfolio/", is_solid=True)}

  <section class="section bg-white" style="padding-top: 60px;">
    <div class="container">
      <div class="text-center reveal-on-scroll" style="max-width: 650px; margin: 0 auto 50px;">
        <span class="section-subtitle">Portfolio Style 1</span>
        <h2 class="section-title">Curated Wedding Stories</h2>
        <p class="lead-p">A gallery of fine-art photography and cinematic highlights from celebrations worldwide.</p>
      </div>

      <div class="portfolio-grid-layout">
{items_html}      </div>
    </div>
  </section>

{get_footer()}
"""

def build_portfolio_2() -> str:
    items_html = ""
    for item in media_data["portfolio_items"]:
        items_html += f"""        <div class="portfolio-card-item reveal-on-scroll" data-category="{item['category_slug']}">
          <div class="portfolio-card-img-wrap">
            <img src="{item['image']}" alt="{item['alt']}" loading="lazy">
          </div>
          <div class="portfolio-card-info">
            <span class="portfolio-card-cat">{item['category']}</span>
            <h3 class="portfolio-card-title"><a href="{item['url']}">{item['title']}</a></h3>
            <a href="{item['url']}" class="btn-link">View Story &rarr;</a>
          </div>
        </div>\n"""

    return f"""{get_head("Portfolio Style 2", "Filterable wedding photography and cinematography collections by HAC Studios.", "/portfolio-2/", "/assets/images/portfolio/fe-0480-large.webp")}
{get_header("/portfolio-2/", is_solid=True)}

  <section class="section bg-white" style="padding-top: 60px;">
    <div class="container">
      <div class="text-center reveal-on-scroll" style="max-width: 650px; margin: 0 auto 40px;">
        <span class="section-subtitle">Portfolio Style 2</span>
        <h2 class="section-title">Filterable Wedding Gallery</h2>
      </div>

      <div class="portfolio-grid-layout">
{items_html}      </div>
    </div>
  </section>

{get_footer()}
"""

def build_portfolio_story() -> str:
    return f"""{get_head("Abdulrehman & Zainish Wedding Story", "Complete wedding story and cinematic film for Abdulrehman & Zainish by HAC Studios.", "/portfolio-story/", "/assets/images/portfolio/c01-01-large.webp")}
{get_header("/portfolio-story/", is_solid=True)}

  <section class="section bg-white" style="padding-top: 60px;">
    <div class="container" style="max-width: 900px;">
      <div class="reveal-on-scroll">
        <span class="section-subtitle text-center">Featured Story</span>
        <h1 class="section-title text-center" style="font-size: 42px; margin-bottom: 20px;">Abdulrehman & Zainish: A Timeless Celebration</h1>
        <p class="lead-p text-center" style="margin-bottom: 40px;">An unforgettable wedding weekend documented with fine-art precision and heartfelt cinematic motion.</p>
        
        <div style="margin-bottom: 40px;">
          <img src="{media_data['roles']['hero_desktop']['image']}" alt="Abdulrehman & Zainish Shoot" style="width: 100%;">
        </div>

        <div class="text-center" style="margin-bottom: 50px;">
          <button class="btn btn-primary video-play-btn" data-video-src="/assets/videos/wedding-film-1080p.mp4">Watch 4K Cinematic Highlight Film</button>
        </div>
      </div>
    </div>
  </section>

{get_footer()}
"""

def build_services() -> str:
    return f"""{get_head("Our Services", "Wedding photography, cinematography, bridal sessions, and photo retouching services by HAC Studios.", "/services/", "/assets/images/portfolio/fe-0500-large.webp")}
{get_header("/services/", is_solid=True)}

  <section class="section bg-white" style="padding-top: 60px;">
    <div class="container">
      <div class="text-center reveal-on-scroll" style="max-width: 650px; margin: 0 auto 50px;">
        <span class="section-subtitle">What We Offer</span>
        <h2 class="section-title">Our Creative Services</h2>
        <p class="lead-p">From intimate rituals to grand multi-day celebrations, we provide complete visual coverage.</p>
      </div>

      <div class="pricing-cards-grid reveal-on-scroll">
        <div class="service-block-card">
          <span class="section-subtitle">Service 01</span>
          <h5>Wedding Photography</h5>
          <p>Full-day fine-art documentary photography capturing the emotional essence and grandeur of your wedding.</p>
        </div>
        <div class="service-block-card">
          <span class="section-subtitle">Service 02</span>
          <h5>Wedding Cinematography</h5>
          <p>4K master films, audio storytelling, and drone perspectives that turn your day into a cinematic motion picture.</p>
        </div>
        <div class="service-block-card">
          <span class="section-subtitle">Service 03</span>
          <h5>Bridal & Couple Portraits</h5>
          <p>Dedicated editorial portraiture sessions focused on natural light, high-fashion styling, and heirloom beauty.</p>
        </div>
      </div>
    </div>
  </section>

{get_footer()}
"""

def build_team() -> str:
    return f"""{get_head("Our Creative Team", "Meet the directors, photographers, and cinematographers of HAC Studios.", "/our-team/", "/assets/images/portfolio/c01-03-large.webp")}
{get_header("/our-team/", is_solid=True)}

  <section class="section bg-white" style="padding-top: 60px;">
    <div class="container">
      <div class="text-center reveal-on-scroll" style="max-width: 650px; margin: 0 auto 50px;">
        <span class="section-subtitle">Our Team</span>
        <h2 class="section-title">The HAC Studios Creative Team</h2>
        <p class="lead-p">A passionate collective of visual artists, directors, and master editors dedicated to heirloom wedding storytelling.</p>
      </div>

      <div class="portfolio-grid-layout reveal-on-scroll">
        <div class="service-block-card text-center">
          <h5>Principal Creative Directors</h5>
          <p>Leading each celebration with creative vision, editorial framing, and personal guidance.</p>
        </div>
        <div class="service-block-card text-center">
          <h5>Master Cinematographers</h5>
          <p>Specialists in 4K optics, sound design, and fluid camera movement that immortalize raw emotion.</p>
        </div>
      </div>
    </div>
  </section>

{get_footer()}
"""

def build_pricing() -> str:
    return f"""{get_head("Pricing & Packages", "Explore comprehensive wedding coverage options by HAC Studios.", "/pricing/", "/assets/images/portfolio/c01-08-large.webp")}
{get_header("/pricing/", is_solid=True)}

  <section class="section bg-white" style="padding-top: 60px;">
    <div class="container">
      <div class="text-center reveal-on-scroll" style="max-width: 650px; margin: 0 auto 50px;">
        <span class="section-subtitle">Pricing</span>
        <h2 class="section-title">Choose Your Packages</h2>
        <p class="lead-p">Every love story is unique. We provide tailored photography and film packages designed around your itinerary.</p>
      </div>

      <div class="pricing-cards-grid reveal-on-scroll">
        <div class="pricing-card-box">
          <h3 class="pricing-card-name">Essential</h3>
          <div class="pricing-card-price">Custom Quote</div>
          <ul class="pricing-features-list">
            <li>1 Lead Photographer</li>
            <li>Up to 6 Hours Coverage</li>
            <li>200+ Master Edited Photos</li>
            <li>Online Gallery</li>
          </ul>
          <a href="/contact/" class="btn btn-outline" style="width: 100%;">Inquire</a>
        </div>

        <div class="pricing-card-box featured">
          <h3 class="pricing-card-name">Signature</h3>
          <div class="pricing-card-price">Custom Quote</div>
          <ul class="pricing-features-list">
            <li>2 Photographers & Cinematographer</li>
            <li>Full Day Coverage</li>
            <li>4K Highlight Film</li>
            <li>Bridal Portrait Session</li>
          </ul>
          <a href="/contact/" class="btn btn-hero" style="width: 100%;">Inquire</a>
        </div>

        <div class="pricing-card-box">
          <h3 class="pricing-card-name">Royal Heirloom</h3>
          <div class="pricing-card-price">Custom Quote</div>
          <ul class="pricing-features-list">
            <li>Full Photo & Cinema Crew</li>
            <li>Multi-Day Coverage</li>
            <li>Feature Film & Drone</li>
            <li>Handcrafted Leather Album</li>
          </ul>
          <a href="/contact/" class="btn btn-outline" style="width: 100%;">Inquire</a>
        </div>
      </div>
    </div>
  </section>

{get_footer()}
"""

def build_faq() -> str:
    return f"""{get_head("Frequently Asked Questions", "Answers to common questions about booking HAC Studios for your wedding.", "/faq/", "/assets/images/portfolio/c01-11-large.webp")}
{get_header("/faq/", is_solid=True)}

  <section class="section bg-white" style="padding-top: 60px;">
    <div class="container" style="max-width: 800px;">
      <div class="text-center reveal-on-scroll" style="margin-bottom: 50px;">
        <span class="section-subtitle">FAQ</span>
        <h2 class="section-title">Frequently Asked Questions</h2>
      </div>

      <div class="reveal-on-scroll" style="display: flex; flex-direction: column; gap: 24px;">
        <div class="service-block-card">
          <h5>How far in advance should we book?</h5>
          <p>We recommend booking 6 to 12 months in advance, especially for autumn and winter peak wedding dates.</p>
        </div>
        <div class="service-block-card">
          <h5>Do you travel for destination weddings?</h5>
          <p>Yes, HAC Studios documents celebrations across Pakistan (Lahore, Islamabad, Karachi) and international destination locations.</p>
        </div>
        <div class="service-block-card">
          <h5>When will our photos and films be delivered?</h5>
          <p>A curated preview gallery is delivered within 10 days of your event. Final high-resolution galleries and 4K films are delivered within 6 to 8 weeks.</p>
        </div>
      </div>
    </div>
  </section>

{get_footer()}
"""

def build_stories() -> str:
    cards_html = ""
    for story in media_data["stories"]:
        cards_html += f"""        <div class="story-card-item reveal-on-scroll">
          <div class="story-card-media">
            <img src="{story['image']}" alt="{story['title']}" loading="lazy">
          </div>
          <div class="story-card-content">
            <span class="story-card-date">{story['date']}</span>
            <h3 class="story-card-title"><a href="{story['url']}">{story['title']}</a></h3>
            <p class="story-card-excerpt">{story['excerpt']}</p>
            <a href="{story['url']}" class="btn-link">Read Story &rarr;</a>
          </div>
        </div>\n"""

    return f"""{get_head("Stories & Journal", "Wedding journal, articles, and celebration spotlights by HAC Studios.", "/stories/", "/assets/images/portfolio/c01-01-card.webp")}
{get_header("/stories/", is_solid=True)}

  <section class="section bg-white" style="padding-top: 60px;">
    <div class="container">
      <div class="text-center reveal-on-scroll" style="max-width: 650px; margin: 0 auto 50px;">
        <span class="section-subtitle">Our Blog</span>
        <h2 class="section-title">Stories & Journal Articles</h2>
      </div>

      <div class="stories-grid-3">
{cards_html}      </div>
    </div>
  </section>

{get_footer()}
"""

def build_story() -> str:
    return f"""{get_head("Featured Story", "Featured wedding narrative and editorial article by HAC Studios.", "/story/", "/assets/images/portfolio/fe-0480-large.webp")}
{get_header("/story/", is_solid=True)}

  <section class="section bg-white" style="padding-top: 60px;">
    <div class="container" style="max-width: 800px;">
      <div class="reveal-on-scroll">
        <span class="section-subtitle text-center">Featured Article</span>
        <h1 class="section-title text-center" style="font-size: 38px; margin-bottom: 20px;">The Art of Natural Light in Bridal Portraiture</h1>
        <p class="lead-p text-center" style="margin-bottom: 30px;">How HAC Studios approaches bridal portrait sessions with an editorial eye, capturing effortless beauty and authentic emotion.</p>
        
        <div style="margin-bottom: 30px;">
          <img src="/assets/images/portfolio/fe-0480-large.webp" alt="Bridal Editorial" style="width: 100%;">
        </div>

        <p class="lead-p">Light is the defining brushstroke of wedding imagery. When framing a bride during her morning preparation or sunset portraits, understanding the interplay of gentle window light and subtle shadow brings dimension and grace to every photograph.</p>
      </div>
    </div>
  </section>

{get_footer()}
"""

def build_contact() -> str:
    return f"""{get_head("Contact & Booking", "Get in touch with HAC Studios to reserve your wedding date and check availability.", "/contact/", "/assets/images/portfolio/fe-0777-large.webp")}
{get_header("/contact/", is_solid=True)}

  <section class="section booking-section-wrapper" style="padding-top: 60px;">
    <div class="container">
      <div class="booking-split-grid reveal-on-scroll">
        <div class="booking-info-box">
          <span class="section-subtitle">Get In Touch</span>
          <h2>Let’s Immortalize Your Celebration</h2>
          <p class="lead-p">Dates fill quickly for upcoming seasons. Please complete the inquiry form and our creative team will provide detailed coverage proposals.</p>
          <div style="margin-top: 20px;">
            <p style="font-family: var(--font-serif); font-size: 18px; font-weight: 700; color: var(--color-text-dark);">HAC Studios Creative Headquarters</p>
            <p style="color: var(--color-text-muted); font-size: 14px;">Lahore &bull; Islamabad &bull; Worldwide Travel</p>
          </div>
        </div>

        <div class="booking-form-card">
          <form id="hac-booking-form">
            <div class="form-grid-2">
              <div class="form-field">
                <label class="form-label" for="c-name">Your Name *</label>
                <input type="text" id="c-name" class="form-input" placeholder="e.g. Sarah & David" required>
              </div>

              <div class="form-field">
                <label class="form-label" for="c-email">Email Address *</label>
                <input type="email" id="c-email" class="form-input" placeholder="name@domain.com" required>
              </div>

              <div class="form-field">
                <label class="form-label" for="c-phone">Phone Number</label>
                <input type="tel" id="c-phone" class="form-input" placeholder="+92 300 0000000">
              </div>

              <div class="form-field">
                <label class="form-label" for="c-date">Wedding Date</label>
                <input type="date" id="c-date" class="form-input">
              </div>

              <div class="form-field form-group-full">
                <label class="form-label" for="c-service">Service Required</label>
                <select id="c-service" class="form-select">
                  <option value="both">Photography & Cinematography (Recommended)</option>
                  <option value="photo">Wedding Photography Only</option>
                  <option value="film">Wedding Cinematography Only</option>
                  <option value="bridal">Bridal Portrait Session</option>
                </select>
              </div>

              <div class="form-field form-group-full">
                <label class="form-label" for="c-message">Tell Us About Your Celebration *</label>
                <textarea id="c-message" class="form-textarea" placeholder="Share your venue, timeline, and celebration style..." required></textarea>
              </div>

              <div class="form-field form-group-full">
                <button type="submit" class="btn btn-primary" style="width: 100%; padding: 14px;">Send Booking Inquiry</button>
              </div>
            </div>
            <div class="form-status-msg" role="status" aria-live="polite"></div>
          </form>
        </div>
      </div>
    </div>
  </section>

{get_footer()}
"""

def build_privacy() -> str:
    return f"""{get_head("Privacy Policy", "Privacy policy and client data protection practices for HAC Studios.", "/privacy-policy/")}
{get_header("/privacy-policy/", is_solid=True)}

  <section class="section bg-white" style="padding-top: 60px;">
    <div class="container" style="max-width: 800px;">
      <span class="section-subtitle">Legal Information</span>
      <h1 class="section-title">Privacy Policy</h1>
      <p class="lead-p" style="margin-bottom: 20px;">HAC Studios values the privacy and confidentiality of our clients and wedding guests. This policy explains how we collect and safeguard information when you inquire or work with our studio.</p>
      <h3 style="margin: 20px 0 10px;">1. Client Information</h3>
      <p style="color: var(--color-text-muted); margin-bottom: 16px;">We collect information you submit via booking inquiries (name, email, phone number, wedding details) exclusively for the purpose of communicating and providing photography/videography services.</p>
    </div>
  </section>

{get_footer()}
"""

def build_terms() -> str:
    return f"""{get_head("Terms & Conditions", "Terms and conditions of service for HAC Studios.", "/terms/")}
{get_header("/terms/", is_solid=True)}

  <section class="section bg-white" style="padding-top: 60px;">
    <div class="container" style="max-width: 800px;">
      <span class="section-subtitle">Legal Information</span>
      <h1 class="section-title">Terms & Conditions</h1>
      <p class="lead-p" style="margin-bottom: 20px;">All wedding photography and cinematography services provided by HAC Studios are governed by our bespoke client service agreements and these terms.</p>
    </div>
  </section>

{get_footer()}
"""

# ==============================================================================
# MAIN COMPILER EXECUTION
# ==============================================================================

def main():
    print("=== Starting HAC Studios V2 Motion Build ===")
    print(f"Content-Hashed CSS: {CSS_FILENAME}")
    print(f"Content-Hashed JS:  {JS_FILENAME}")

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)

    # Copy all static assets from SRC to DIST
    assets_src = SRC / "assets"
    assets_dist = DIST / "assets"
    shutil.copytree(assets_src, assets_dist)

    # Write hashed CSS and JS
    (assets_dist / "css" / CSS_FILENAME).write_bytes(css_content)
    (assets_dist / "js" / JS_FILENAME).write_bytes(js_content)

    # Routes to build
    routes = {
        "/": build_home(),
        "/home-2/": build_home_2(),
        "/about/": build_about(),
        "/portfolio/": build_portfolio(),
        "/portfolio-2/": build_portfolio_2(),
        "/portfolio-story/": build_portfolio_story(),
        "/services/": build_services(),
        "/our-team/": build_team(),
        "/pricing/": build_pricing(),
        "/faq/": build_faq(),
        "/stories/": build_stories(),
        "/story/": build_story(),
        "/contact/": build_contact(),
        "/privacy-policy/": build_privacy(),
        "/terms/": build_terms(),
    }

    sitemap_entries = []

    for route_path, html_content in routes.items():
        if route_path == "/":
            dest = DIST / "index.html"
        else:
            folder = DIST / route_path.strip("/")
            folder.mkdir(parents=True, exist_ok=True)
            dest = folder / "index.html"

        dest.write_text(html_content, encoding="utf-8")
        print(f"✓ Generated: {route_path} -> {dest.relative_to(ROOT)} ({len(html_content)} bytes)")
        sitemap_entries.append(f"{CANONICAL_DOMAIN}{route_path}")

    # Generate sitemap.xml
    sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in sitemap_entries:
        sitemap_xml.append("  <url>")
        sitemap_xml.append(f"    <loc>{url}</loc>")
        sitemap_xml.append("    <changefreq>weekly</changefreq>")
        sitemap_xml.append("    <priority>0.8</priority>")
        sitemap_xml.append("  </url>")
    sitemap_xml.append("</urlset>")
    (DIST / "sitemap.xml").write_text("\n".join(sitemap_xml), encoding="utf-8")
    print("✓ Generated: sitemap.xml")

    # Generate robots.txt
    robots_txt = f"""User-agent: *
Allow: /
Sitemap: {CANONICAL_DOMAIN}/sitemap.xml
"""
    (DIST / "robots.txt").write_text(robots_txt, encoding="utf-8")
    print("✓ Generated: robots.txt")

    print("\n✓ Motion build successfully completed in dist/!")

if __name__ == "__main__":
    main()
