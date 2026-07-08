import os

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rudy Project Half Marathon 2026</title>
  <link rel="icon" href="//www.rudyproject.com/cdn/shop/files/logo-mobile.svg?v=1752058228&width=47" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,600;0,700;0,800;0,900;1,800;1,900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <style>
    :root {
      /* Dark/Purple Palette from existing site */
      --bg: #030005;
      --bg-card: #0a0510;
      --bg-card-alt: #160a22;
      --text: #ffffff;
      --text-sub: #aaaaaa;
      --primary: #7b2fff;
      --accent: #ff4f00; /* Added Granger orange accent */
      --border: #222222;
      --radius-lg: 32px;
      --radius-md: 24px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    html, body {
      font-family: 'Inter', sans-serif;
      background: var(--bg);
      color: var(--text);
      overflow-x: hidden;
      width: 100%;
      -webkit-font-smoothing: antialiased;
    }

    /* Typography */
    h1, h2, h3, h4, h5, h6, .display-font {
      font-family: 'Barlow', sans-serif;
      text-transform: uppercase;
      font-weight: 800;
      line-height: 1.1;
    }
    a { text-decoration: none; color: inherit; transition: opacity 0.3s; }
    a:hover { opacity: 0.7; }
    img { max-width: 100%; display: block; object-fit: cover; }

    /* Layout Skeleton */
    .layout {
      display: grid;
      grid-template-columns: 80px 1fr;
      min-height: 100vh;
    }

    /* Sidebar Navigation */
    .sidebar {
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 40px 0;
      position: sticky;
      top: 0;
      height: 100vh;
      background: var(--bg);
      z-index: 100;
    }
    .sb-logo img { width: 40px; margin-bottom: 40px; }
    .sb-nav {
      writing-mode: vertical-rl;
      transform: rotate(180deg);
      display: flex;
      gap: 40px;
      align-items: center;
      font-size: 0.85rem;
      letter-spacing: 2px;
      text-transform: uppercase;
      font-weight: 600;
      color: var(--text-sub);
      margin-top: auto;
    }
    .sb-nav a.highlight { color: var(--accent); }
    .sb-nav a.active { color: var(--text); }

    /* Main Content Area */
    .main-content {
      padding: 32px;
      display: flex;
      flex-direction: column;
      gap: 80px; /* Golden ratio spacing */
    }

    /* ── HERO SECTION ── */
    .hero-section {
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 24px;
      height: calc(100vh - 64px);
      min-height: 600px;
    }
    .bento-card {
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      border: 1px solid var(--border);
      overflow: hidden;
      position: relative;
      padding: 32px;
      display: flex;
      flex-direction: column;
    }
    .bento-card.light { background: #ffffff; color: #000000; border: none; }
    .bento-card.accent { background: var(--accent); color: #ffffff; border: none; }
    .bento-card.p-0 { padding: 0; }

    /* Main Hero Image Card */
    .hero-main {
      position: relative;
    }
    .hero-main img {
      position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      opacity: 0.7; z-index: 1;
    }
    .hero-overlay {
      position: relative; z-index: 2;
      height: 100%; display: flex; flex-direction: column; justify-content: flex-end;
      padding: 40px;
    }
    .hero-subtitle {
      font-size: 1.5rem; max-width: 350px; font-weight: 500;
      line-height: 1.3;
    }
    .hero-subtitle span {
      display: block; font-size: 0.9rem; color: #ddd; margin-top: 16px;
      font-weight: 400; font-family: 'Inter', sans-serif;
    }
    
    /* Massive rotated text */
    .hero-giant-text {
      position: absolute;
      right: 0; top: 0;
      height: 100%;
      writing-mode: vertical-rl;
      font-size: clamp(10rem, 18vw, 20rem);
      line-height: 0.8;
      letter-spacing: -5px;
      color: rgba(255,255,255,0.95);
      z-index: 3;
      pointer-events: none;
      display: flex;
      align-items: center;
      mix-blend-mode: overlay;
    }

    /* Hero Side Cards */
    .hero-side {
      display: flex; flex-direction: column; gap: 24px;
    }
    .card-title { font-size: 1.5rem; margin-bottom: 16px; }
    .card-title-lg { font-size: 2.5rem; line-height: 1.1; margin-bottom: 24px; }
    
    .badge {
      display: inline-flex; align-items: center; gap: 8px;
      padding: 6px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600;
      background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2);
      margin-bottom: 24px; width: fit-content;
    }
    .light .badge { background: rgba(0,0,0,0.05); border: 1px solid rgba(0,0,0,0.1); }
    .accent .badge { background: rgba(0,0,0,0.2); border: none; }

    /* ── BENTO GRID SECTION ── */
    .section-title-wrapper {
      display: flex; gap: 24px; align-items: baseline; margin-bottom: 32px;
    }
    .section-title { font-size: clamp(2.5rem, 5vw, 4rem); max-width: 600px; }
    .section-pills { display: flex; gap: 12px; }
    .pill { padding: 8px 16px; border-radius: 30px; border: 1px solid var(--border); font-size: 0.9rem; }

    .bento-grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      grid-auto-rows: 350px;
    }
    .span-2-col { grid-column: span 2; }
    .span-2-row { grid-row: span 2; }

    /* Specific Cards */
    .stat-number { font-size: 5rem; line-height: 1; margin-top: auto; }
    .stat-label { color: var(--text-sub); text-transform: uppercase; letter-spacing: 1px; font-size: 0.8rem; }
    
    /* Hover Effects */
    .hover-scale img { transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1); }
    .bento-card:hover .hover-scale img { transform: scale(1.05); }

    /* Footer */
    .mega-footer {
      padding: 80px 40px;
      background: #000;
      border-top: 1px solid var(--border);
    }
    .footer-top {
      display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 100px;
    }
    .footer-links {
      display: flex; gap: 60px;
    }
    .link-group { display: flex; flex-direction: column; gap: 12px; }
    .link-group h4 { color: var(--text-sub); font-size: 0.9rem; margin-bottom: 8px; }
    .mega-text {
      font-size: clamp(5rem, 15vw, 22rem);
      line-height: 0.8;
      letter-spacing: -5px;
      color: var(--text);
      text-align: center;
      margin: 0 -20px;
      white-space: nowrap;
      overflow: hidden;
    }
    
    .footer-bottom {
      display: flex; justify-content: space-between; margin-top: 40px; color: var(--text-sub); font-size: 0.9rem;
    }

    /* Responsive */
    @media (max-width: 1024px) {
      .layout { grid-template-columns: 1fr; }
      .sidebar {
        height: auto; width: 100%; flex-direction: row; padding: 20px;
        position: relative; border-right: none; border-bottom: 1px solid var(--border);
        justify-content: space-between;
      }
      .sb-logo img { margin-bottom: 0; }
      .sb-nav { writing-mode: horizontal-tb; transform: none; margin-top: 0; gap: 20px; }
      .hero-section { grid-template-columns: 1fr; height: auto; }
      .hero-giant-text { writing-mode: horizontal-tb; position: relative; font-size: 6rem; line-height: 1; padding: 40px; mix-blend-mode: normal; }
      .bento-grid-3 { grid-template-columns: 1fr; grid-auto-rows: auto; }
      .span-2-col { grid-column: span 1; }
      .span-2-row { grid-row: span 1; }
      .footer-top { flex-direction: column; align-items: flex-start; gap: 40px; }
    }
  </style>
</head>
<body>

<div class="layout">
  
  <!-- SIDEBAR -->
  <aside class="sidebar">
    <a href="#" class="sb-logo">
      <img src="//www.rudyproject.com/cdn/shop/files/logo-mobile.svg?v=1752058228&width=47" alt="Logo">
    </a>
    <nav class="sb-nav">
      <a href="#">About</a>
      <a href="#">Events</a>
      <a href="#">Product</a>
      <a href="#" class="highlight">Program</a>
      <a href="#">Get in Touch</a>
    </nav>
  </aside>

  <!-- MAIN CONTENT -->
  <main class="main-content">
    
    <!-- 1. HERO -->
    <section class="hero-section">
      <div class="bento-card p-0 hero-main hover-scale">
        <img src="https://images.unsplash.com/photo-1552674605-db6ffd4facb5?q=80&w=2070&auto=format&fit=crop" alt="Runner">
        <div class="hero-giant-text display-font">RPHM 26</div>
        <div class="hero-overlay">
          <div class="hero-subtitle">
            A new era of performance running.
            <span>Improve your health — performance well</span>
          </div>
        </div>
      </div>
      <div class="hero-side">
        <div class="bento-card light" style="flex: 1;">
          <div class="badge">EST - 2026</div>
          <h2 class="card-title">Explore our flexible activity.</h2>
          <p style="color: #666; font-size: 0.9rem; line-height: 1.5;">Smart features designed to move with you — fast, flexible, and built for everyday action.</p>
        </div>
        <div class="bento-card" style="flex: 1;">
          <div class="badge">🏆 Premium Race</div>
          <h2 class="card-title">Visionary Precision Play</h2>
          <a href="#" style="margin-top: auto; display: inline-block; padding: 12px 24px; background: var(--accent); color: white; border-radius: 30px; font-weight: 600; width: fit-content;">Join Now →</a>
        </div>
      </div>
    </section>

    <!-- 2. BENTO FEATURES -->
    <section>
      <div class="section-title-wrapper">
        <h2 class="section-title">Elevate your experience with handpicked featured.</h2>
        <div class="section-pills">
          <div class="pill">Virtual Challenges</div>
          <div class="pill">Community Tournaments</div>
        </div>
      </div>

      <div class="bento-grid-3">
        <!-- Stat Card -->
        <div class="bento-card light">
          <h3 class="card-title">Upcoming Events</h3>
          <div class="stat-number display-font">03<span style="font-size: 2rem; color: #888;">/26</span></div>
          <div class="stat-label">Main Races</div>
        </div>
        
        <!-- Dark Text Card -->
        <div class="bento-card">
          <h3 class="card-title-lg">The coach experts and simple software for better sportainment.</h3>
          <div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center;">
            <div class="badge" style="margin: 0;">((•)) Live</div>
            <a href="#">rudyprojectrun.com</a>
          </div>
        </div>

        <!-- Image Card -->
        <div class="bento-card p-0 hover-scale span-2-row">
          <img src="https://images.unsplash.com/photo-1530549387789-4c1017266635?q=80&w=2070&auto=format&fit=crop" alt="Swimming/Running" style="width: 100%; height: 100%;">
          <div style="position: absolute; bottom: 30px; left: 30px; z-index: 2;">
            <h3 style="font-size: 2rem; font-family: 'Barlow'; text-transform: uppercase;">Chemistry<br>Sports Partner</h3>
            <p style="font-size: 0.8rem; color: #ccc; margin-top: 8px;">BSD CITY, TANGERANG</p>
          </div>
        </div>

        <!-- Orange Accent Card -->
        <div class="bento-card accent span-2-col" style="display: flex; flex-direction: row; align-items: center; justify-content: space-between;">
          <div>
            <div class="badge">Performance</div>
            <h3 class="card-title-lg" style="margin-bottom: 0;">Youth Sports Camp — 20yo</h3>
          </div>
          <div style="display: flex; gap: 20px; font-weight: 500;">
            <div>Obstacle Course Race</div>
            <div>Sport x Game Day</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. MOTIVATION & TRACKING -->
    <section>
      <div class="bento-grid-3">
        <div class="bento-card span-2-col light" style="display: flex; flex-direction: row; gap: 40px; padding: 40px;">
          <div style="flex: 1; display: flex; flex-direction: column; justify-content: center;">
            <div class="badge" style="color: var(--accent); background: rgba(255,79,0,0.1);">Featured Features</div>
            <h2 class="card-title-lg">Stay motivated with activity tracking.</h2>
            <p style="color: #666; font-weight: 500;">Record activities to boost your performance.</p>
            <p style="font-weight: 800; font-family: 'Barlow'; margin-top: 10px;">WITH IZT RACE 4.0</p>
          </div>
          <div style="flex: 1; background: #f5f5f5; border-radius: 20px; padding: 20px; display: flex; align-items: center; justify-content: center;">
            <!-- Placeholder for chart -->
            <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070&auto=format&fit=crop" alt="Data" style="border-radius: 12px;">
          </div>
        </div>
        
        <div class="bento-card">
          <h2 class="card-title-lg" style="line-height: 1;">To win over sports-minded consumers with technology and excellent.</h2>
          <div style="margin-top: auto; color: var(--text-sub);">Online Fitness Challenge</div>
        </div>
      </div>
    </section>

  </main>
</div>

<!-- MEGA FOOTER -->
<footer class="mega-footer">
  <div class="wrap" style="max-width: 100%; padding: 0 40px;">
    <div class="footer-top">
      <div>
        <h2 style="font-size: 2rem; max-width: 400px; line-height: 1.2;">We're doing everything for future healthiness.</h2>
        <div class="badge" style="margin-top: 24px;">Trainer & Coach Access</div>
      </div>
      <div class="footer-links">
        <div class="link-group">
          <h4>Navigate</h4>
          <a href="#">Program</a>
          <a href="#">Product</a>
          <a href="#">Event</a>
          <a href="#">About</a>
        </div>
        <div class="link-group">
          <h4>Social</h4>
          <a href="#">X (Twitter)</a>
          <a href="#">Instagram</a>
          <a href="#">LinkedIn</a>
        </div>
        <div class="link-group">
          <h4>Legal</h4>
          <a href="#">Privacy Policy</a>
          <a href="#">Terms & Conditions</a>
        </div>
      </div>
    </div>
    
    <div class="mega-text">rudy project</div>
    
    <div class="footer-bottom">
      <div>© 2026 PT. Arras Protama Sejahtera. All Right Reserved.</div>
      <div>Designed for Rudy Project Indonesia</div>
    </div>
  </div>
</footer>

</body>
</html>
"""

with open("index_new.html", "w") as f:
    f.write(html_content)

print("Generated index_new.html")
