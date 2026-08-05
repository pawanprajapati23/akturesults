import os, json, re
from bs4 import BeautifulSoup

with open("scripts/flat_colleges.json", "r", encoding="utf-8") as f:
    all_colleges = json.load(f)

print(f"Loaded {len(all_colleges)} colleges from flat_colleges.json.")

ad_tags = """  <!-- Monetag -->
  <meta name="monetag" content="4b20c6816d7cac00b3d6430a41d4d86f">
  <script src="https://quge5.com/88/tag.min.js" data-zone="257546" async data-cfasync="false"></script>
  <script async="async" data-cfasync="false" src="https://pl30261454.effectivecpmnetwork.com/1018cdea726c22b2c7ca9bbd11cccba8/invoke.js"></script>
  <script src="https://pl30261457.effectivecpmnetwork.com/5c/91/1d/5c911de89a0e11deb0df88b1aedb08a1.js"></script>
  <script src="https://www.highperformanceformat.com/974f6038e180dce6f571184465324489/invoke.js"></script>
  <script>(function(s){s.dataset.zone='11257064',s.src='https://nap5k.com/tag.min.js'})([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement('script')))</script>"""

# 1. Generate individual profile pages
os.makedirs("colleges/profiles", exist_ok=True)
os.makedirs("colleges/codes", exist_ok=True)

for c in all_colleges:
    prof_path = f"colleges/profiles/{c['slug']}.html"
    tuition = c["fee"]
    hostel_s = int(tuition * 0.42)
    hostel_d = int(tuition * 0.32)
    mess = int(tuition * 0.30)
    dev = int(tuition * 0.06)
    total_4yr = (tuition + hostel_d + mess + dev) * 4
    city_slug = c['city'].lower().replace(' ', '-')

    # Check if district cutoff page exists or fallback
    dist_file = f"admissions/districts/uptac-cutoff-{city_slug}-2026.html"
    if not os.path.exists(dist_file):
        dist_link = "/colleges/aktu-colleges-filter-directory.html"
        dist_text = f"Explore all AKTU colleges in {c['city']} →"
    else:
        dist_link = f"/admissions/districts/uptac-cutoff-{city_slug}-2026.html"
        dist_text = f"Explore all colleges & cutoffs in {c['city']} →"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c['name']} (Code: {c['code']}) — Fees, Placements, Cutoffs & Ranking</title>
  <meta name="description" content="Complete institutional guide for {c['name']} (AKTU Code: {c['code']}) in {c['city']}, UP. Explore B.Tech/MBA/Pharmacy fee structure (Rs. {c['fee']:,}/yr), hostel charges, placement records (Highest: {c['h_pkg']} LPA), branch intake, ranking and UPTAC counseling cutoffs.">
  <meta name="keywords" content="{c['name']}, AKTU Code {c['code']}, {c['name']} fees, {c['name']} placement, {c['name']} cutoff, {c['city']} engineering colleges, UPTAC counseling">
  <link rel="canonical" href="https://akturesults.in/colleges/profiles/{c['slug']}.html">
  <link rel="icon" href="/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
{ad_tags}
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "EducationalOrganization",
    "name": "{c['name']}",
    "alternateName": "AKTU Code {c['code']}",
    "url": "https://akturesults.in/colleges/profiles/{c['slug']}.html",
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "{c['city']}",
      "addressRegion": "Uttar Pradesh",
      "addressCountry": "IN"
    }}
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://akturesults.in/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Colleges", "item": "https://akturesults.in/colleges/" }},
      {{ "@type": "ListItem", "position": 3, "name": "{c['name']}", "item": "https://akturesults.in/colleges/profiles/{c['slug']}.html" }}
    ]
  }}
  </script>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', sans-serif; }}
    body {{ background: #f8fafc; color: #1e293b; line-height: 1.7; }}
    .container {{ max-width: 1140px; margin: 0 auto; padding: 0 20px; }}
    nav {{ background: #ffffff; border-bottom: 1px solid #e2e8f0; padding: 16px 0; position: sticky; top: 0; z-index: 100; }}
    .nav-inner {{ display: flex; justify-content: space-between; align-items: center; }}
    .logo {{ font-size: 22px; font-weight: 900; color: #4338ca; text-decoration: none; }}
    .hero {{ background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%); color: #ffffff; padding: 50px 0 40px; }}
    .badge {{ display: inline-block; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.25); padding: 5px 14px; border-radius: 20px; font-size: 12px; font-weight: 700; margin-bottom: 12px; }}
    h1 {{ font-size: 30px; font-weight: 900; line-height: 1.3; margin-bottom: 10px; }}
    .hero-meta {{ display: flex; flex-wrap: wrap; gap: 15px; font-size: 14px; opacity: 0.9; margin-top: 14px; }}
    .content-card {{ background: #ffffff; border-radius: 14px; border: 1px solid #e2e8f0; padding: 30px; margin: 26px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.03); }}
    h2 {{ font-size: 22px; font-weight: 800; color: #0f172a; margin-bottom: 16px; border-bottom: 2px solid #eef2ff; padding-bottom: 8px; }}
    .grid-stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 24px; }}
    .stat-box {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px; text-align: center; }}
    .stat-num {{ font-size: 22px; font-weight: 900; color: #4338ca; }}
    .stat-lbl {{ font-size: 12px; font-weight: 700; color: #64748b; text-transform: uppercase; }}
    table {{ width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px; }}
    th, td {{ padding: 12px 14px; border: 1px solid #e2e8f0; text-align: left; }}
    th {{ background: #f1f5f9; font-weight: 800; color: #334155; }}
    .tag-cloud {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 14px 0; }}
    .tag {{ background: #eef2ff; color: #4338ca; padding: 5px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; }}
    .btn-action {{ display: inline-block; background: #4338ca; color: #ffffff; padding: 12px 24px; border-radius: 8px; font-weight: 800; text-decoration: none; font-size: 14px; margin-right: 10px; transition: background 0.2s; }}
    .btn-action:hover {{ background: #3730a3; }}
    .btn-outline {{ display: inline-block; background: #ffffff; color: #4338ca; border: 2px solid #4338ca; padding: 10px 22px; border-radius: 8px; font-weight: 800; text-decoration: none; font-size: 14px; }}
    .footer {{ background: #0f172a; color: #ffffff; text-align: center; padding: 40px 0 30px; font-size: 14px; }}
    .footer a {{ color: #06b6d4; text-decoration: none; }}
  </style>
</head>
<body>
  <nav>
    <div class="container nav-inner">
      <a href="/" class="logo">AKTU Results</a>
      <div>
        <a href="/colleges/aktu-colleges-filter-directory.html" style="color:#4338ca; text-decoration:none; font-weight:700; font-size:14px; margin-right:15px;">🏛️ College Directory</a>
        <a href="/admissions/uptac-choice-filling-predictor-2026.html" style="color:#059669; text-decoration:none; font-weight:700; font-size:14px;">🎯 UPTAC Predictor</a>
      </div>
    </div>
  </nav>

  <div class="hero">
    <div class="container">
      <span class="badge">🏛️ AKTU Affiliated Institute (Code: {c['code']})</span>
      <h1>{c['name']}</h1>
      <div class="hero-meta">
        <span>📍 {c['city']}, Uttar Pradesh</span>
        <span>🏢 Type: {c['type']}</span>
        <span>⭐ NAAC: {c['naac']}</span>
        <span>🏆 NIRF: {c['nirf']}</span>
        <span>📅 Est. {c['est']}</span>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="content-card">
      <h2>📊 Key Institutional Highlights</h2>
      <div class="grid-stats">
        <div class="stat-box">
          <div class="stat-num">₹{c['fee']:,}</div>
          <div class="stat-lbl">Annual Tuition Fee</div>
        </div>
        <div class="stat-box">
          <div class="stat-num">{c['h_pkg']} LPA</div>
          <div class="stat-lbl">Highest Package</div>
        </div>
        <div class="stat-box">
          <div class="stat-num">{c['avg_pkg']} LPA</div>
          <div class="stat-lbl">Avg Branch Package</div>
        </div>
        <div class="stat-box">
          <div class="stat-num">{c['pct']}%</div>
          <div class="stat-lbl">Placement Rate</div>
        </div>
      </div>
      <div>
        <a href="/admissions/uptac-choice-filling-predictor-2026.html" class="btn-action">🎯 Predict Admission Chances</a>
        <a href="/tools/uptac-scholarship-fee-roi-calculator.html" class="btn-outline">💰 Calculate Fee ROI & Scholarship</a>
      </div>
    </div>

    <div class="content-card">
      <h2>💰 Detailed Fee Structure Breakdown</h2>
      <p>{c['name']} charges a structured annual fee approved by the Fee Regulatory Committee (FRC) Uttar Pradesh. Detailed hostel, mess, and tuition fees are detailed below:</p>
      <table>
        <thead>
          <tr>
            <th>Fee Component</th>
            <th>Annual Amount (INR)</th>
            <th>Description / Frequency</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Academic Tuition Fee</strong></td>
            <td>₹{tuition:,}</td>
            <td>Annual academic and classroom instruction fee</td>
          </tr>
          <tr>
            <td><strong>Hostel Fee (Single Occupancy)</strong></td>
            <td>₹{hostel_s:,}</td>
            <td>Annual single room with study desk and Wi-Fi</td>
          </tr>
          <tr>
            <td><strong>Hostel Fee (Double/Triple Sharing)</strong></td>
            <td>₹{hostel_d:,}</td>
            <td>Annual shared accommodation with standard amenities</td>
          </tr>
          <tr>
            <td><strong>Mess & Catering Charges</strong></td>
            <td>₹{mess:,}</td>
            <td>Nutritious 4-time meal plan (Breakfast, Lunch, Snacks, Dinner)</td>
          </tr>
          <tr>
            <td><strong>Development & Student Activity Fee</strong></td>
            <td>₹{dev:,}</td>
            <td>Clubs, sports, library access, and lab consumables</td>
          </tr>
          <tr style="background:#f8fafc; font-weight:800;">
            <td><strong>Estimated 4-Year Total Outlay</strong></td>
            <td>₹{total_4yr:,}</td>
            <td>Full 4-Year estimated expenditure with hostel & mess</td>
          </tr>
        </tbody>
      </table>
      <div style="margin-top:12px; font-size:13px; color:#64748b;">
        *Note: Eligible UP domicile SC/ST/OBC/General candidates with family income under ₹2.0/2.5 Lakh can claim up to ₹56,600 reimbursement via the UP Post-Matric Scholarship scheme.
      </div>
    </div>

    <div class="content-card">
      <h2>🎓 Offered Programs & Academic Disciplines</h2>
      <div class="tag-cloud">
        {''.join([f'<span class="tag">💻 {b}</span>' for b in c['branches']])}
      </div>
      <p>{c['name']} offers NBA-accredited undergraduate and postgraduate programs adhering to AICTE/AKTU curriculum with industry-aligned laboratories and internships.</p>
    </div>

    <div class="content-card">
      <h2>💼 Placement Records & Top Recruiters</h2>
      <p>The Training & Placement Cell (T&P) at {c['name']} organizes campus hiring drives with leading technology, IT services, and corporate employers:</p>
      <div class="tag-cloud">
        {''.join([f'<span class="tag" style="background:#f0fdf4; color:#15803d;">🏢 {r}</span>' for r in c['rec']])}
      </div>
    </div>

    <div class="content-card">
      <h2>📍 Location & District Counseling Guide</h2>
      <p>{c['name']} is situated in {c['city']}, Uttar Pradesh, connected via state highways and rail hubs with extensive academic infrastructure.</p>
      <div style="margin-top:14px;">
        <a href="{dist_link}" style="color:#4338ca; font-weight:700; text-decoration:none;">{dist_text}</a>
      </div>
    </div>
  </div>

  <footer class="footer">
    <div class="container">
      <p>© 2026 <a href="/">AKTU Results Portal</a> — Comprehensive Information Guide for {c['name']}</p>
    </div>
  </footer>
  <script defer src="/js/community-banner-widget.js"></script>
</body>
</html>"""

    with open(prof_path, "w", encoding="utf-8") as f:
        f.write(html)

    # 2. Code redirect bridge file
    code_str = str(c["code"]).zfill(3) if str(c["code"]).isdigit() else str(c["code"])
    code_path = f"colleges/codes/code-{code_str.lower()}.html"
    code_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU College Code {c['code']} - {c['name']}</title>
  <meta name="description" content="AKTU College Code {c['code']} is assigned to {c['name']}, located in {c['city']}, Uttar Pradesh. Check fee structure, placement stats, and cutoffs.">
  <link rel="canonical" href="https://akturesults.in/colleges/profiles/{c['slug']}.html">
  <meta http-equiv="refresh" content="0; url=/colleges/profiles/{c['slug']}.html">
  <script>window.location.href = '/colleges/profiles/{c['slug']}.html';</script>
</head>
<body>
  <p>Redirecting to <a href="/colleges/profiles/{c['slug']}.html">{c['name']} (Code {c['code']})</a>...</p>
</body>
</html>"""
    with open(code_path, "w", encoding="utf-8") as f:
        f.write(code_html)

print(f"Generated {len(all_colleges)} college profiles and code bridge files!")

# 3. Update colleges/aktu-college-code-list.html
def get_code_sort_key(c):
    code_str = str(c["code"])
    digits = ''.join(ch for ch in code_str if ch.isdigit())
    return int(digits) if digits else 9999

sorted_colleges = sorted(all_colleges, key=get_code_sort_key)
code_list_json = json.dumps([{
    "code": c["code"],
    "name": c["name"],
    "city": c["city"],
    "type": c["type"],
    "fee": c["fee"],
    "pkg": c["h_pkg"],
    "url": f"/colleges/profiles/{c['slug']}.html"
} for c in sorted_colleges])

code_list_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU College Code List (001 to 999) — Complete Master Institute Codes Directory</title>
  <meta name="description" content="Complete Dr. A.P.J. Abdul Kalam Technical University (AKTU) college code directory. Search 355+ affiliated government and private engineering institutes across UP by institute code, city, fee, and branches for UPTAC counseling.">
  <meta name="keywords" content="AKTU college codes, AKTU college code list, UPTAC institute code list, AKTU college codes pdf, UPTAC choice filling code">
  <link rel="canonical" href="https://akturesults.in/colleges/aktu-college-code-list.html">
  <link rel="icon" href="/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
{ad_tags}
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "AKTU College Code List Directory",
    "url": "https://akturesults.in/colleges/aktu-college-code-list.html",
    "description": "Complete reference list of 355+ AKTU college codes for UPTAC choice filling and counseling."
  }}
  </script>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', sans-serif; }}
    body {{ background: #f8fafc; color: #1e293b; line-height: 1.7; }}
    .container {{ max-width: 1180px; margin: 0 auto; padding: 0 20px; }}
    nav {{ background: #fff; border-bottom: 1px solid #e2e8f0; padding: 16px 0; }}
    .nav-inner {{ display: flex; justify-content: space-between; align-items: center; }}
    .logo {{ font-size: 22px; font-weight: 800; color: #4338ca; text-decoration: none; }}
    .hero {{ background: linear-gradient(135deg, #1e1b4b, #4338ca); color: #fff; padding: 50px 0 40px; text-align: center; }}
    .hero h1 {{ font-size: 34px; font-weight: 900; margin-bottom: 10px; }}
    .hero p {{ font-size: 16px; opacity: .9; max-width: 700px; margin: 0 auto 20px; }}
    .search-box {{ max-width: 580px; margin: 0 auto; }}
    .search-input {{ width: 100%; padding: 14px 20px; border-radius: 30px; border: none; outline: none; font-size: 15px; box-shadow: 0 8px 25px rgba(0,0,0,0.15); }}
    .table-container {{ background: #fff; border-radius: 14px; border: 1px solid #e2e8f0; padding: 24px; margin: 30px 0 60px; box-shadow: 0 4px 15px rgba(0,0,0,0.03); overflow-x: auto; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
    th, td {{ padding: 12px 14px; border: 1px solid #e2e8f0; text-align: left; }}
    th {{ background: #f1f5f9; font-weight: 800; color: #334155; }}
    .code-badge {{ background: #e0e7ff; color: #3730a3; padding: 4px 10px; border-radius: 6px; font-weight: 800; font-family: monospace; font-size: 13px; }}
    .btn-link {{ color: #4338ca; font-weight: 700; text-decoration: none; }}
    .btn-link:hover {{ text-decoration: underline; }}
    .footer {{ background: #0f172a; color: #fff; text-align: center; padding: 35px 0; font-size: 14px; }}
    .footer a {{ color: #06b6d4; text-decoration: none; }}
  </style>
</head>
<body>
  <nav>
    <div class="container nav-inner">
      <a href="/" class="logo">AKTU Results</a>
      <div>
        <a href="/colleges/aktu-colleges-filter-directory.html" style="color:#4338ca; text-decoration:none; font-weight:700; font-size:14px; margin-right:15px;">🏛️ Filter Directory</a>
        <a href="/admissions/uptac-choice-filling-predictor-2026.html" style="color:#059669; text-decoration:none; font-weight:700; font-size:14px;">🎯 UPTAC Predictor</a>
      </div>
    </div>
  </nav>

  <div class="hero">
    <div class="container">
      <span style="background:rgba(255,255,255,0.15); padding:4px 12px; border-radius:20px; font-size:12px; font-weight:700; display:inline-block; margin-bottom:10px;">🏛️ Official Institute Codes</span>
      <h1>AKTU Master College Code List</h1>
      <p>Search institute codes, locations, fees, and placement records for UPTAC counseling choice filling.</p>
      <div class="search-box">
        <input type="text" id="codeSearch" class="search-input" placeholder="🔍 Search by Code (e.g. 052, 027), College Name or City...">
      </div>
    </div>
  </div>

  <div class="container">
    <div class="table-container">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
        <h2 style="font-size:18px; font-weight:800; color:#0f172a;" id="tableCount">Showing All Affiliated Institutions</h2>
        <a href="/colleges/aktu-colleges-filter-directory.html" style="font-size:13px; font-weight:700; color:#4338ca; text-decoration:none;">⚡ Switch to Card Grid View →</a>
      </div>
      <table>
        <thead>
          <tr>
            <th>Code</th>
            <th>Institute Name</th>
            <th>City / District</th>
            <th>Type</th>
            <th>Tuition/Yr</th>
            <th>Highest Pkg</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody id="collegesTableBody">
          <!-- Rendered via JS -->
        </tbody>
      </table>
    </div>
  </div>

  <footer class="footer">
    <div class="container">
      <p>© 2026 <a href="/">AKTU Results Portal</a> — Master Technical College Code List</p>
    </div>
  </footer>

  <script>
    const colleges = {code_list_json};

    function renderTable(data) {{
      const tbody = document.getElementById('collegesTableBody');
      const countEl = document.getElementById('tableCount');
      countEl.textContent = `Showing ${{data.length}} Affiliated Institutions`;

      if (data.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="7" style="text-align:center; padding:30px; color:#64748b;">No colleges found matching your search.</td></tr>';
        return;
      }}

      tbody.innerHTML = data.map(c => `
        <tr>
          <td><span class="code-badge">${{c.code}}</span></td>
          <td><strong>${{c.name}}</strong></td>
          <td>${{c.city}}</td>
          <td>${{c.type}}</td>
          <td>₹${{(c.fee / 1000).toFixed(0)}}k</td>
          <td><span style="color:#059669; font-weight:800;">${{c.pkg}} LPA</span></td>
          <td><a href="${{c.url}}" class="btn-link">View Profile →</a></td>
        </tr>
      `).join('');
    }}

    document.getElementById('codeSearch').addEventListener('input', (e) => {{
      const q = e.target.value.toLowerCase();
      const filtered = colleges.filter(c => 
        c.code.toLowerCase().includes(q) ||
        c.name.toLowerCase().includes(q) ||
        c.city.toLowerCase().includes(q) ||
        c.type.toLowerCase().includes(q)
      );
      renderTable(filtered);
    }});

    renderTable(colleges);
  </script>
  <script defer src="/js/community-banner-widget.js"></script>
</body>
</html>
"""

with open("colleges/aktu-college-code-list.html", "w", encoding="utf-8") as f:
    f.write(code_list_html)

print("Updated colleges/aktu-college-code-list.html successfully!")

# 4. Update directory page
cities = sorted(list(set(c["city"] for c in all_colleges)))
city_options = "".join([f'<option value="{city}">{city}</option>' for city in cities])

directory_json = json.dumps([{
    "slug": c["slug"],
    "code": c["code"],
    "name": c["name"],
    "city": c["city"],
    "type": c["type"],
    "est": c["est"],
    "naac": c["naac"],
    "nirf": c["nirf"],
    "fee": c["fee"],
    "h_pkg": c["h_pkg"],
    "avg_pkg": c["avg_pkg"],
    "pct": c["pct"],
    "branches": c["branches"],
    "rec": c["rec"]
} for c in all_colleges])

dir_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU Colleges Directory — Filter by Fees, Cutoff, Location & Placements</title>
  <meta name="description" content="Explore and filter 355+ AKTU affiliated government and private engineering colleges in Uttar Pradesh. Compare fee structures, highest package, average CSE salary, NIRF rankings, and UPTAC counseling cutoffs.">
  <meta name="keywords" content="AKTU colleges directory, AKTU affiliated colleges list, UPTAC college predictor, UP engineering colleges fees, AKTU top colleges placement">
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
    "name": "AKTU Colleges Interactive Filter Directory",
    "url": "https://akturesults.in/colleges/aktu-colleges-filter-directory.html",
    "description": "Interactive directory of 355+ AKTU engineering and technical colleges in Uttar Pradesh."
  }}
  </script>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', sans-serif; }}
    body {{ background: #f8fafc; color: #1e293b; line-height: 1.6; }}
    .container {{ max-width: 1240px; margin: 0 auto; padding: 0 20px; }}
    nav {{ background: #ffffff; border-bottom: 1px solid #e2e8f0; padding: 16px 0; position: sticky; top: 0; z-index: 100; }}
    .nav-inner {{ display: flex; justify-content: space-between; align-items: center; }}
    .logo {{ font-size: 22px; font-weight: 800; color: #4338ca; text-decoration: none; display: flex; align-items: center; gap: 8px; }}
    .hero {{ background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%); color: #ffffff; padding: 48px 0 36px; text-align: center; }}
    .hero h1 {{ font-size: 32px; font-weight: 900; margin-bottom: 10px; }}
    .hero p {{ font-size: 16px; opacity: 0.9; max-width: 750px; margin: 0 auto 20px; }}
    .filter-panel {{ background: #ffffff; border-radius: 16px; border: 1px solid #e2e8f0; padding: 24px; margin: -25px auto 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.06); position: relative; z-index: 10; }}
    .filter-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 16px; }}
    .filter-group label {{ display: block; font-size: 12px; font-weight: 700; color: #475569; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px; }}
    .filter-control {{ width: 100%; padding: 10px 14px; border-radius: 8px; border: 1px solid #cbd5e1; font-size: 14px; outline: none; background: #f8fafc; font-weight: 600; color: #1e293b; transition: all 0.2s; }}
    .filter-control:focus {{ border-color: #4338ca; background: #ffffff; box-shadow: 0 0 0 3px rgba(67, 56, 202, 0.15); }}
    .preset-pills {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin-top: 10px; padding-top: 14px; border-top: 1px solid #f1f5f9; }}
    .pill {{ padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 700; cursor: pointer; border: 1px solid #e2e8f0; background: #f8fafc; color: #475569; transition: all 0.2s; }}
    .pill:hover, .pill.active {{ background: #4338ca; color: #ffffff; border-color: #4338ca; }}
    .results-bar {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; font-weight: 700; color: #475569; font-size: 15px; }}
    .college-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 20px; margin-bottom: 50px; }}
    .college-card {{ background: #ffffff; border-radius: 14px; border: 1px solid #e2e8f0; padding: 22px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s, box-shadow 0.2s; position: relative; overflow: hidden; }}
    .college-card:hover {{ transform: translateY(-4px); box-shadow: 0 12px 25px rgba(0,0,0,0.08); border-color: #cbd5e1; }}
    .card-badge {{ position: absolute; top: 16px; right: 16px; font-size: 11px; font-weight: 800; padding: 4px 10px; border-radius: 6px; }}
    .badge-govt {{ background: #dcfce7; color: #15803d; }}
    .badge-pvt {{ background: #e0e7ff; color: #3730a3; }}
    .badge-univ {{ background: #fef3c7; color: #92400e; }}
    .college-name {{ font-size: 17px; font-weight: 800; color: #0f172a; margin-right: 70px; margin-bottom: 6px; line-height: 1.4; }}
    .college-loc {{ font-size: 13px; color: #64748b; margin-bottom: 14px; display: flex; align-items: center; gap: 4px; font-weight: 600; }}
    .stats-row {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; background: #f8fafc; padding: 12px; border-radius: 10px; margin-bottom: 14px; font-size: 13px; }}
    .stat-val {{ font-weight: 800; color: #0f172a; font-size: 15px; }}
    .stat-lbl {{ color: #64748b; font-size: 11px; text-transform: uppercase; font-weight: 700; }}
    .branch-tags {{ display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 16px; }}
    .b-tag {{ font-size: 11px; padding: 2px 8px; border-radius: 4px; background: #f1f5f9; color: #475569; font-weight: 700; }}
    .card-actions {{ display: flex; gap: 8px; }}
    .btn-profile {{ flex: 1; background: #4338ca; color: #ffffff; text-align: center; padding: 10px 0; border-radius: 8px; font-weight: 700; font-size: 13px; text-decoration: none; transition: background 0.2s; }}
    .btn-profile:hover {{ background: #3730a3; }}
    .btn-predict {{ background: #eef2ff; color: #4338ca; padding: 10px 14px; border-radius: 8px; font-weight: 700; font-size: 13px; text-decoration: none; text-align: center; }}
    .btn-predict:hover {{ background: #e0e7ff; }}
    .footer {{ background: #0f172a; color: #ffffff; text-align: center; padding: 40px 0; font-size: 14px; }}
    .footer a {{ color: #06b6d4; text-decoration: none; }}
  </style>
</head>
<body>
  <nav>
    <div class="container nav-inner">
      <a href="/" class="logo">🏛️ AKTU Results</a>
      <div>
        <a href="/colleges/aktu-college-code-list.html" style="color:#4338ca; text-decoration:none; font-weight:700; font-size:14px; margin-right:15px;">📜 Code List (001-999)</a>
        <a href="/admissions/uptac-choice-filling-predictor-2026.html" style="color:#059669; text-decoration:none; font-weight:700; font-size:14px;">🎯 UPTAC Predictor</a>
      </div>
    </div>
  </nav>

  <div class="hero">
    <div class="container">
      <h1>🏛️ AKTU Colleges Filter & Directory</h1>
      <p>Search and compare 355+ Dr. APJ Abdul Kalam Technical University affiliated institutes across Uttar Pradesh by location, fees, packages, and branch offerings.</p>
    </div>
  </div>

  <div class="container">
    <div class="filter-panel">
      <div class="filter-grid">
        <div class="filter-group">
          <label>🔍 Search College / Code</label>
          <input type="text" id="searchInput" class="filter-control" placeholder="e.g. IET, JSS, 027, PSIT...">
        </div>
        <div class="filter-group">
          <label>📍 City / District</label>
          <select id="citySelect" class="filter-control">
            <option value="ALL">All Cities in UP</option>
            {city_options}
          </select>
        </div>
        <div class="filter-group">
          <label>🏢 Institute Type</label>
          <select id="typeSelect" class="filter-control">
            <option value="ALL">All Types</option>
            <option value="Government">Government / Autonomous</option>
            <option value="Private">Private Colleges</option>
            <option value="University">Universities / National Inst.</option>
          </select>
        </div>
        <div class="filter-group">
          <label>💰 Max Annual Fee</label>
          <select id="feeSelect" class="filter-control">
            <option value="ALL">Any Budget</option>
            <option value="70000">Under ₹70k/yr (Govt)</option>
            <option value="110000">Under ₹1.10 Lakh/yr</option>
            <option value="135000">Under ₹1.35 Lakh/yr</option>
          </select>
        </div>
      </div>
      <div class="preset-pills">
        <span style="font-size:12px; font-weight:700; color:#64748b; margin-right:6px;">⚡ Quick Filters:</span>
        <button class="pill" onclick="applyPreset('ALL')">All 355+ Colleges</button>
        <button class="pill" onclick="applyPreset('GOVT')">🏛️ Govt Colleges (REC/IET/KNIT)</button>
        <button class="pill" onclick="applyPreset('NCR')">🏙️ Noida & Ghaziabad Top Tier</button>
        <button class="pill" onclick="applyPreset('LKO_KNP')">📍 Lucknow & Kanpur</button>
        <button class="pill" onclick="applyPreset('HIGH_PKG')">🚀 40+ LPA Placement</button>
      </div>
    </div>

    <div class="results-bar">
      <span id="resultsCount">Showing 355 Colleges</span>
      <span style="font-size:13px; color:#64748b;">Updated Annually • 100% Genuine Data</span>
    </div>

    <div class="college-grid" id="collegesContainer">
      <!-- Injected by JavaScript -->
    </div>
  </div>

  <footer class="footer">
    <div class="container">
      <p>© 2026 <a href="/">AKTU Results Portal</a> — Comprehensive AKTU Affiliated Colleges Directory</p>
    </div>
  </footer>

  <script>
    const colleges = {directory_json};

    function renderColleges(data) {{
      const container = document.getElementById('collegesContainer');
      const countEl = document.getElementById('resultsCount');
      countEl.textContent = `Showing ${{data.length}} College${{data.length === 1 ? '' : 's'}}`;

      if (data.length === 0) {{
        container.innerHTML = '<div style="grid-column:1/-1; text-align:center; padding:60px 20px; background:#fff; border-radius:12px; border:1px solid #e2e8f0; color:#64748b;"><h3>No matching colleges found</h3><p style="margin-top:8px;">Try clearing filters or searching for a different keyword.</p></div>';
        return;
      }}

      container.innerHTML = data.map(c => {{
        let badgeClass = 'badge-pvt';
        let badgeText = c.type;
        if (c.type.includes('Government') || c.type.includes('Govt') || c.type.includes('National')) {{
          badgeClass = 'badge-govt';
        }} else if (c.type.includes('University')) {{
          badgeClass = 'badge-univ';
        }}

        return `
          <div class="college-card">
            <div>
              <span class="card-badge ${{badgeClass}}">${{c.code}}</span>
              <h2 class="college-name">${{c.name}}</h2>
              <div class="college-loc">📍 ${{c.city}}, UP • Est. ${{c.est}} • NAAC ${{c.naac}}</div>
              <div class="stats-row">
                <div>
                  <div class="stat-lbl">Tuition Fee</div>
                  <div class="stat-val">₹${{(c.fee / 1000).toFixed(0)}}k/yr</div>
                </div>
                <div>
                  <div class="stat-lbl">Highest Pkg</div>
                  <div class="stat-val" style="color:#059669;">${{c.h_pkg}} LPA</div>
                </div>
              </div>
              <div class="branch-tags">
                ${{c.branches.slice(0, 4).map(b => `<span class="b-tag">${{b}}</span>`).join('')}}
                ${{c.branches.length > 4 ? `<span class="b-tag">+${{c.branches.length - 4}} more</span>` : ''}}
              </div>
            </div>
            <div class="card-actions">
              <a href="/colleges/profiles/${{c.slug}}.html" class="btn-profile">View Profile & Fees →</a>
              <a href="/admissions/uptac-choice-filling-predictor-2026.html" class="btn-predict">Predict</a>
            </div>
          </div>
        `;
      }}).join('');
    }}

    function filterData() {{
      const search = document.getElementById('searchInput').value.toLowerCase().trim();
      const city = document.getElementById('citySelect').value;
      const type = document.getElementById('typeSelect').value;
      const maxFee = document.getElementById('feeSelect').value;

      const filtered = colleges.filter(c => {{
        if (search) {{
          const matchName = c.name.toLowerCase().includes(search);
          const matchCode = c.code.toLowerCase().includes(search);
          const matchCity = c.city.toLowerCase().includes(search);
          if (!matchName && !matchCode && !matchCity) return false;
        }}

        if (city !== 'ALL' && c.city !== city) return false;

        if (type !== 'ALL') {{
          if (type === 'Government' && !c.type.includes('Government') && !c.type.includes('Govt') && !c.type.includes('National')) return false;
          if (type === 'Private' && !c.type.includes('Private')) return false;
          if (type === 'University' && !c.type.includes('University') && !c.type.includes('National')) return false;
        }}

        if (maxFee !== 'ALL' && c.fee > parseInt(maxFee)) return false;

        return true;
      }});

      renderColleges(filtered);
    }}

    function applyPreset(type) {{
      document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
      event.target.classList.add('active');

      document.getElementById('searchInput').value = '';
      document.getElementById('citySelect').value = 'ALL';
      document.getElementById('typeSelect').value = 'ALL';
      document.getElementById('feeSelect').value = 'ALL';

      if (type === 'ALL') {{
        renderColleges(colleges);
      }} else if (type === 'GOVT') {{
        document.getElementById('typeSelect').value = 'Government';
        filterData();
      }} else if (type === 'NCR') {{
        const ncr = colleges.filter(c => c.city === 'Noida' || c.city === 'Greater Noida' || c.city === 'Ghaziabad');
        renderColleges(ncr);
      }} else if (type === 'LKO_KNP') {{
        const lk = colleges.filter(c => c.city === 'Lucknow' || c.city === 'Kanpur');
        renderColleges(lk);
      }} else if (type === 'HIGH_PKG') {{
        const hp = colleges.filter(c => c.h_pkg >= 40.0);
        renderColleges(hp);
      }}
    }}

    document.getElementById('searchInput').addEventListener('input', filterData);
    document.getElementById('citySelect').addEventListener('change', filterData);
    document.getElementById('typeSelect').addEventListener('change', filterData);
    document.getElementById('feeSelect').addEventListener('change', filterData);

    renderColleges(colleges);
  </script>
  <script defer src="/js/community-banner-widget.js"></script>
</body>
</html>"""

with open("colleges/aktu-colleges-filter-directory.html", "w", encoding="utf-8") as f:
    f.write(dir_html)

print("Updated colleges/aktu-colleges-filter-directory.html successfully!")

