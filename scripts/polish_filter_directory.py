import json

from build_all_aktu_colleges import colleges_master

directory_items = []
for c in colleges_master:
    directory_items.append({
        "name": c["name"],
        "code": c["code"],
        "city": c["city"],
        "type": c["type"],
        "est": c["est"],
        "naac": c["naac"],
        "nirf": c["nirf"],
        "fee": c["fee"],
        "highest_pkg": c["h_pkg"],
        "avg_pkg": c["avg_pkg"],
        "placement_pct": c["pct"],
        "branches": c["branches"],
        "recruiters": c["rec"],
        "url": f"/colleges/profiles/{c['slug']}.html"
    })

ad_tags = """  <!-- Monetag -->
  <meta name="monetag" content="4b20c6816d7cac00b3d6430a41d4d86f">
  <script src="https://quge5.com/88/tag.min.js" data-zone="257546" async data-cfasync="false"></script>
  <script async="async" data-cfasync="false" src="https://pl30261454.effectivecpmnetwork.com/1018cdea726c22b2c7ca9bbd11cccba8/invoke.js"></script>
  <script src="https://pl30261457.effectivecpmnetwork.com/5c/91/1d/5c911de89a0e11deb0df88b1aedb08a1.js"></script>
  <script src="https://www.highperformanceformat.com/974f6038e180dce6f571184465324489/invoke.js"></script>
  <script>(function(s){s.dataset.zone='11257064',s.src='https://nap5k.com/tag.min.js'})([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement('script')))</script>"""

colleges_json = json.dumps(directory_items)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU Affiliated Colleges Directory | Filter by City, Fees, Branch & NAAC Grade</title>
  <meta name="description" content="Explore and filter 800+ AKTU colleges by city (Noida, Lucknow, Ghaziabad, Kanpur, Meerut), annual fee bracket, engineering branches (CSE, AI, ECE), NAAC grades and highest placement packages. Interactive college directory updated annually.">
  <meta name="keywords" content="aktu college filter, aktu colleges list, aktu fees list, top aktu colleges cse, best aktu government colleges, uptac college predictor">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://akturesults.in/colleges/aktu-colleges-filter-directory.html">
  <link rel="icon" href="/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
{ad_tags}
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "AKTU Affiliated Colleges Directory & Interactive Filter",
    "url": "https://akturesults.in/colleges/aktu-colleges-filter-directory.html",
    "description": "Interactive college directory for AKTU affiliated institutions across Uttar Pradesh with instant filtering by city, fee range, branches, and placement records."
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://akturesults.in/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Colleges", "item": "https://akturesults.in/colleges/" }},
      {{ "@type": "ListItem", "position": 3, "name": "Filter Directory", "item": "https://akturesults.in/colleges/aktu-colleges-filter-directory.html" }}
    ]
  }}
  </script>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    :root {{
      --primary: #4338ca;
      --primary-light: #6366f1;
      --accent: #06b6d4;
      --dark: #0f172a;
      --card-bg: #ffffff;
      --light-bg: #f8fafc;
      --border: #e2e8f0;
      --text-muted: #64748b;
    }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--light-bg);
      color: var(--dark);
      line-height: 1.6;
    }}
    .container {{
      max-width: 1260px;
      margin: 0 auto;
      padding: 0 20px;
    }}
    nav {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 16px 0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .nav-inner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .logo {{
      font-size: 22px;
      font-weight: 900;
      background: linear-gradient(135deg, var(--primary), var(--primary-light));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-decoration: none;
    }}
    .nav-links a {{
      color: var(--dark);
      text-decoration: none;
      font-weight: 600;
      font-size: 14px;
      margin-left: 20px;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{
      color: var(--primary);
    }}
    .hero {{
      background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
      color: #ffffff;
      padding: 55px 0 45px;
      text-align: center;
    }}
    .hero-badge {{
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 700;
      display: inline-block;
      margin-bottom: 14px;
      backdrop-filter: blur(8px);
    }}
    .hero h1 {{
      font-size: 38px;
      font-weight: 900;
      margin-bottom: 12px;
      line-height: 1.25;
      letter-spacing: -0.02em;
    }}
    .hero p {{
      font-size: 16px;
      opacity: 0.9;
      max-width: 760px;
      margin: 0 auto 24px;
    }}
    .search-box-wrapper {{
      max-width: 680px;
      margin: 0 auto;
      position: relative;
    }}
    .search-input {{
      width: 100%;
      padding: 16px 24px;
      font-size: 16px;
      border-radius: 50px;
      border: 2px solid transparent;
      outline: none;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
      font-family: inherit;
    }}
    .search-input:focus {{
      border-color: var(--accent);
    }}

    /* Filter Controls Section */
    .filter-section {{
      background: #ffffff;
      border-radius: 16px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
      padding: 24px 28px;
      margin: -25px auto 32px;
      position: relative;
      z-index: 10;
      border: 1px solid var(--border);
    }}
    .filter-header-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border);
    }}
    .filter-header-title {{
      font-size: 16px;
      font-weight: 800;
      color: var(--dark);
    }}
    .btn-reset {{
      background: #f1f5f9;
      color: #475569;
      border: 1px solid #cbd5e1;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .btn-reset:hover {{
      background: #e2e8f0;
      color: #0f172a;
    }}

    .presets-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 18px;
      align-items: center;
    }}
    .preset-pill {{
      background: #eef2ff;
      border: 1px solid #c7d2fe;
      color: var(--primary);
      padding: 6px 12px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .preset-pill:hover {{
      background: var(--primary);
      color: #fff;
    }}

    .filter-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
      margin-bottom: 14px;
    }}
    .filter-row:last-child {{
      margin-bottom: 0;
    }}
    .filter-label {{
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      min-width: 90px;
    }}
    .pill-group {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      flex: 1;
    }}
    .filter-pill {{
      background: #f1f5f9;
      border: 1px solid #e2e8f0;
      color: #334155;
      padding: 5px 12px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      user-select: none;
    }}
    .filter-pill:hover {{
      background: #e2e8f0;
      border-color: #cbd5e1;
    }}
    .filter-pill.active {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 2px 8px rgba(67, 56, 202, 0.3);
    }}

    /* Results Header & Grid */
    .results-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 22px;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .results-count {{
      font-size: 15px;
      font-weight: 800;
      color: var(--dark);
    }}
    .sort-wrapper {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .sort-select {{
      padding: 8px 14px;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: #ffffff;
      font-size: 13px;
      font-weight: 700;
      outline: none;
      font-family: inherit;
    }}

    .college-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 22px;
      margin-bottom: 50px;
    }}
    .college-card {{
      background: #ffffff;
      border-radius: 14px;
      border: 1px solid var(--border);
      padding: 22px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.25s ease, box-shadow 0.25s ease;
    }}
    .college-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.1);
      border-color: #cbd5e1;
    }}
    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 10px;
      gap: 8px;
    }}
    .badge-city {{
      background: #eff6ff;
      color: #1d4ed8;
      font-size: 11px;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 12px;
      text-transform: uppercase;
    }}
    .badge-naac {{
      background: #ecfdf5;
      color: #047857;
      font-size: 11px;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 12px;
    }}
    .badge-govt {{
      background: #fef3c7;
      color: #b45309;
      font-size: 11px;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 12px;
    }}
    .card-title {{
      font-size: 17px;
      font-weight: 800;
      color: var(--dark);
      margin-bottom: 6px;
      line-height: 1.35;
    }}
    .card-code {{
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 12px;
    }}
    .card-stats {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 6px;
      background: #f8fafc;
      border-radius: 10px;
      padding: 10px 8px;
      text-align: center;
      margin-bottom: 14px;
    }}
    .stat-val {{
      font-size: 15px;
      font-weight: 900;
      color: var(--primary);
    }}
    .stat-lbl {{
      font-size: 10px;
      color: var(--text-muted);
      margin-top: 2px;
      font-weight: 700;
      text-transform: uppercase;
    }}
    .branch-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
      margin-bottom: 12px;
    }}
    .branch-tag {{
      background: #f1f5f9;
      color: #475569;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 5px;
    }}
    .recruiters-list {{
      font-size: 12px;
      color: #334155;
      margin-bottom: 16px;
      line-height: 1.4;
    }}
    .card-actions {{
      display: flex;
      gap: 8px;
    }}
    .card-btn {{
      flex: 1;
      text-align: center;
      background: var(--primary);
      color: #ffffff;
      text-decoration: none;
      padding: 10px 0;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      transition: background 0.2s;
    }}
    .card-btn:hover {{
      background: var(--primary-light);
    }}
    .card-btn-secondary {{
      background: #f1f5f9;
      color: #334155;
      padding: 10px 14px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      text-decoration: none;
      transition: background 0.2s;
    }}
    .card-btn-secondary:hover {{
      background: #e2e8f0;
      color: #0f172a;
    }}
    .empty-state {{
      grid-column: 1 / -1;
      text-align: center;
      padding: 60px 20px;
      background: #ffffff;
      border-radius: 14px;
      border: 1px dashed var(--border);
    }}
    .empty-state h3 {{
      font-size: 20px;
      font-weight: 800;
      margin-bottom: 8px;
    }}
    .footer {{
      background: var(--dark);
      color: #ffffff;
      text-align: center;
      padding: 40px 0 30px;
      font-size: 14px;
    }}
    .footer a {{
      color: var(--accent);
      text-decoration: none;
    }}
    @media(max-width: 768px) {{
      .hero h1 {{ font-size: 26px; }}
      .filter-section {{ padding: 18px; margin-top: -15px; }}
      .filter-row {{ flex-direction: column; align-items: flex-start; gap: 6px; }}
      .college-grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>

  <nav>
    <div class="container nav-inner">
      <a href="/" class="logo">AKTU Results</a>
      <div class="nav-links">
        <a href="/">Home</a>
        <a href="/colleges/">All Colleges</a>
        <a href="/placements/aktu-college-placement-leaderboard-2026.html">Placements</a>
        <a href="/admissions/uptac-choice-filling-predictor-2026.html">UPTAC Predictor</a>
      </div>
    </div>
  </nav>

  <div class="hero">
    <div class="container">
      <span class="hero-badge">🏛️ Complete UP Technical Directory</span>
      <h1>Find Your Best AKTU College</h1>
      <p>Instant filter by City, Fees, Branches, NAAC Accreditation, and Highest Placements across Dr. A.P.J. Abdul Kalam Technical University.</p>
      <div class="search-box-wrapper">
        <input type="text" id="searchInput" class="search-input" placeholder="🔍 Search college by name, city, or branch (e.g. IET, KIET, Noida, CSE, 027)...">
      </div>
    </div>
  </div>

  <div class="container">
    <!-- Filter Controls -->
    <div class="filter-section">
      <div class="filter-header-bar">
        <div class="filter-header-title">⚡ Interactive Filter Engine</div>
        <button id="resetFiltersBtn" class="btn-reset">🔄 Reset All Filters</button>
      </div>

      <!-- Preset Shortcuts -->
      <div class="presets-row">
        <span style="font-size:12px;font-weight:800;color:var(--text-muted);">Quick Presets:</span>
        <span class="preset-pill" onclick="applyPreset('govt')">🏛️ Top Govt Colleges</span>
        <span class="preset-pill" onclick="applyPreset('ncr')">🏙️ Top NCR Colleges</span>
        <span class="preset-pill" onclick="applyPreset('high_pkg')">💼 Highest Packages (>40 LPA)</span>
        <span class="preset-pill" onclick="applyPreset('budget')">💰 Under ₹1 Lakh Budget</span>
      </div>

      <!-- City Filter -->
      <div class="filter-row">
        <div class="filter-label">🏙️ City:</div>
        <div class="pill-group" id="cityGroup">
          <span class="filter-pill active" data-filter="city" data-val="all">All Cities</span>
          <span class="filter-pill" data-filter="city" data-val="Lucknow">Lucknow</span>
          <span class="filter-pill" data-filter="city" data-val="Noida">Noida</span>
          <span class="filter-pill" data-filter="city" data-val="Greater Noida">Gr. Noida</span>
          <span class="filter-pill" data-filter="city" data-val="Ghaziabad">Ghaziabad</span>
          <span class="filter-pill" data-filter="city" data-val="Kanpur">Kanpur</span>
          <span class="filter-pill" data-filter="city" data-val="Meerut">Meerut</span>
          <span class="filter-pill" data-filter="city" data-val="Prayagraj">Prayagraj</span>
          <span class="filter-pill" data-filter="city" data-val="Varanasi">Varanasi</span>
          <span class="filter-pill" data-filter="city" data-val="Gorakhpur">Gorakhpur</span>
          <span class="filter-pill" data-filter="city" data-val="Jhansi">Jhansi</span>
          <span class="filter-pill" data-filter="city" data-val="Bareilly">Bareilly</span>
          <span class="filter-pill" data-filter="city" data-val="Moradabad">Moradabad</span>
          <span class="filter-pill" data-filter="city" data-val="Agra">Agra</span>
          <span class="filter-pill" data-filter="city" data-val="Mathura">Mathura</span>
          <span class="filter-pill" data-filter="city" data-val="Aligarh">Aligarh</span>
        </div>
      </div>

      <!-- Fee Filter -->
      <div class="filter-row">
        <div class="filter-label">💰 Fee / Yr:</div>
        <div class="pill-group" id="feeGroup">
          <span class="filter-pill active" data-filter="fee" data-val="all">All Budgets</span>
          <span class="filter-pill" data-filter="fee" data-val="govt">Under ₹70,000 (Govt/Subsidized)</span>
          <span class="filter-pill" data-filter="fee" data-val="budget">₹70,000 - ₹1,00,000</span>
          <span class="filter-pill" data-filter="fee" data-val="mid">₹1,00,000 - ₹1,30,000</span>
          <span class="filter-pill" data-filter="fee" data-val="premium">Above ₹1,30,000</span>
        </div>
      </div>

      <!-- Branch Filter -->
      <div class="filter-row">
        <div class="filter-label">🎓 Branch:</div>
        <div class="pill-group" id="branchGroup">
          <span class="filter-pill active" data-filter="branch" data-val="all">All Branches</span>
          <span class="filter-pill" data-filter="branch" data-val="CSE">CSE Core</span>
          <span class="filter-pill" data-filter="branch" data-val="CSE-AI">CSE (AI/ML)</span>
          <span class="filter-pill" data-filter="branch" data-val="CSE-DS">CSE (Data Science)</span>
          <span class="filter-pill" data-filter="branch" data-val="ECE">ECE</span>
          <span class="filter-pill" data-filter="branch" data-val="ME">Mechanical</span>
          <span class="filter-pill" data-filter="branch" data-val="CE">Civil</span>
          <span class="filter-pill" data-filter="branch" data-val="EE">Electrical</span>
        </div>
      </div>

      <!-- NAAC / Type Filter -->
      <div class="filter-row">
        <div class="filter-label">⭐ Grade:</div>
        <div class="pill-group" id="naacGroup">
          <span class="filter-pill active" data-filter="naac" data-val="all">All Grades</span>
          <span class="filter-pill" data-filter="naac" data-val="A+">NAAC A+ Accredited</span>
          <span class="filter-pill" data-filter="naac" data-val="A">NAAC A Accredited</span>
          <span class="filter-pill" data-filter="naac" data-val="B+">NAAC B+</span>
          <span class="filter-pill" data-filter="type" data-val="govt_only">🏛️ Govt Colleges Only</span>
        </div>
      </div>
    </div>

    <!-- Results Header -->
    <div class="results-bar">
      <div class="results-count" id="resultsCount">Loading Verified Colleges...</div>
      <div class="sort-wrapper">
        <label for="sortSelect" style="font-size:13px;font-weight:700;color:var(--text-muted);">Sort By:</label>
        <select id="sortSelect" class="sort-select">
          <option value="pkg_desc">Highest Package (High to Low)</option>
          <option value="placement_desc">Placement Rate (High to Low)</option>
          <option value="fee_asc">Annual Fee (Low to High)</option>
          <option value="nirf_asc">NIRF / Seniority Rank</option>
        </select>
      </div>
    </div>

    <!-- Colleges Grid -->
    <div class="college-grid" id="collegeGrid">
      <!-- Populated dynamically -->
    </div>
  </div>

  <div class="footer">
    <div class="container">
      <p>© 2026 <a href="/">AKTU Results Portal</a> — Comprehensive AKTU Academic & Placement Directory</p>
      <p style="margin-top:6px;opacity:.7;font-size:13px;">All figures sourced from verified college prospectuses and official AKTU counseling cutoffs. Updated annually.</p>
    </div>
  </div>

  <script>
    const collegesData = {colleges_json};

    let currentFilters = {{
      search: '',
      city: 'all',
      fee: 'all',
      branch: 'all',
      naac: 'all',
      type: 'all',
      sort: 'pkg_desc'
    }};

    function resetFilters() {{
      currentFilters = {{
        search: '',
        city: 'all',
        fee: 'all',
        branch: 'all',
        naac: 'all',
        type: 'all',
        sort: 'pkg_desc'
      }};
      document.getElementById('searchInput').value = '';
      document.getElementById('sortSelect').value = 'pkg_desc';
      document.querySelectorAll('.filter-pill').forEach(p => {{
        if (p.dataset.val === 'all') p.classList.add('active');
        else p.classList.remove('active');
      }});
      renderColleges();
    }}

    function applyPreset(type) {{
      resetFilters();
      if (type === 'govt') {{
        currentFilters.type = 'govt_only';
        document.querySelector('[data-filter="type"][data-val="govt_only"]').classList.add('active');
        document.querySelector('#naacGroup .filter-pill[data-val="all"]').classList.remove('active');
      }} else if (type === 'ncr') {{
        currentFilters.city = 'Noida';
        renderColleges();
      }} else if (type === 'high_pkg') {{
        currentFilters.sort = 'pkg_desc';
      }} else if (type === 'budget') {{
        currentFilters.fee = 'budget';
        document.querySelector('[data-filter="fee"][data-val="budget"]').classList.add('active');
        document.querySelector('#feeGroup .filter-pill[data-val="all"]').classList.remove('active');
      }}
      renderColleges();
    }}

    function renderColleges() {{
      const grid = document.getElementById('collegeGrid');
      const countEl = document.getElementById('resultsCount');
      
      let filtered = collegesData.filter(c => {{
        if (currentFilters.search) {{
          const q = currentFilters.search.toLowerCase();
          const matchName = c.name.toLowerCase().includes(q);
          const matchCity = c.city.toLowerCase().includes(q);
          const matchCode = c.code.toLowerCase().includes(q);
          const matchBranch = c.branches.some(b => b.toLowerCase().includes(q));
          if (!matchName && !matchCity && !matchCode && !matchBranch) return false;
        }}

        if (currentFilters.city !== 'all' && c.city.toLowerCase() !== currentFilters.city.toLowerCase()) {{
          return false;
        }}

        if (currentFilters.fee !== 'all') {{
          if (currentFilters.fee === 'govt' && c.fee > 70000) return false;
          if (currentFilters.fee === 'budget' && (c.fee < 70000 || c.fee > 100000)) return false;
          if (currentFilters.fee === 'mid' && (c.fee < 100000 || c.fee > 130000)) return false;
          if (currentFilters.fee === 'premium' && c.fee <= 130000) return false;
        }}

        if (currentFilters.branch !== 'all' && !c.branches.includes(currentFilters.branch)) {{
          return false;
        }}

        if (currentFilters.naac !== 'all' && c.naac !== currentFilters.naac) {{
          return false;
        }}

        if (currentFilters.type === 'govt_only' && !c.type.toLowerCase().includes('government')) {{
          return false;
        }}

        return true;
      }});

      filtered.sort((a, b) => {{
        if (currentFilters.sort === 'pkg_desc') return b.highest_pkg - a.highest_pkg;
        if (currentFilters.sort === 'placement_desc') return b.placement_pct - a.placement_pct;
        if (currentFilters.sort === 'fee_asc') return a.fee - b.fee;
        if (currentFilters.sort === 'nirf_asc') return a.est - b.est;
        return 0;
      }});

      countEl.textContent = `Showing ${{filtered.length}} of ${{collegesData.length}} Verified Colleges`;

      if (filtered.length === 0) {{
        grid.innerHTML = `
          <div class="empty-state">
            <h3>No Colleges Found</h3>
            <p style="color:var(--text-muted);margin-bottom:14px;">Try adjusting your search criteria or reset filters to view all colleges.</p>
            <button onclick="resetFilters()" class="btn-reset">Reset Filters</button>
          </div>
        `;
        return;
      }}

      grid.innerHTML = filtered.map(c => `
        <div class="college-card">
          <div>
            <div class="card-top">
              <span class="badge-city">${{c.city}}</span>
              <div>
                ${{c.type.includes('Government') ? '<span class="badge-govt">🏛️ Govt</span> ' : ''}}
                <span class="badge-naac">NAAC ${{c.naac}}</span>
              </div>
            </div>
            <h3 class="card-title">${{c.name}}</h3>
            <div class="card-code">Code: ${{c.code}} • Est. ${{c.est}} • NIRF: ${{c.nirf}}</div>
            
            <div class="card-stats">
              <div>
                <div class="stat-val">₹${{(c.fee / 1000).toFixed(0)}}k</div>
                <div class="stat-lbl">Tuition/Yr</div>
              </div>
              <div>
                <div class="stat-val">${{c.highest_pkg}} LPA</div>
                <div class="stat-lbl">Highest Pkg</div>
              </div>
              <div>
                <div class="stat-val">${{c.placement_pct}}%</div>
                <div class="stat-lbl">Placement</div>
              </div>
            </div>

            <div style="font-size:12px;font-weight:700;color:var(--text-muted);margin-bottom:6px;">Offered Branches:</div>
            <div class="branch-tags">
              ${{c.branches.map(b => `<span class="branch-tag">${{b}}</span>`).join('')}}
            </div>

            <div class="recruiters-list">
              <strong>🏢 Top Recruiters:</strong> ${{c.recruiters.slice(0, 4).join(', ')}}
            </div>
          </div>

          <div class="card-actions">
            <a href="${{c.url}}" class="card-btn">Full Profile & Fees →</a>
            <a href="/admissions/uptac-choice-filling-predictor-2026.html" class="card-btn-secondary" title="Check Cutoffs">🎯 Predict</a>
          </div>
        </div>
      `).join('');
    }}

    document.getElementById('resetFiltersBtn').addEventListener('click', resetFilters);

    document.getElementById('searchInput').addEventListener('input', (e) => {{
      currentFilters.search = e.target.value;
      renderColleges();
    }});

    document.querySelectorAll('.filter-pill').forEach(pill => {{
      pill.addEventListener('click', function() {{
        const group = this.parentElement;
        group.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
        this.classList.add('active');

        const filterType = this.dataset.filter;
        const val = this.dataset.val;

        if (filterType === 'city') currentFilters.city = val;
        if (filterType === 'fee') currentFilters.fee = val;
        if (filterType === 'branch') currentFilters.branch = val;
        if (filterType === 'naac') {{
          currentFilters.naac = val;
          currentFilters.type = 'all';
        }}
        if (filterType === 'type') {{
          currentFilters.type = val;
          currentFilters.naac = 'all';
        }}

        renderColleges();
      }});
    }});

    document.getElementById('sortSelect').addEventListener('change', (e) => {{
      currentFilters.sort = e.target.value;
      renderColleges();
    }});

    renderColleges();
  </script>
  <script defer src="/js/community-banner-widget.js"></script>
</body>
</html>"""

with open('colleges/aktu-colleges-filter-directory.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Polished colleges/aktu-colleges-filter-directory.html successfully!')
