import json

from build_master_colleges import all_colleges, ad_tags

# Sort colleges by code numeric / alphanumeric
def get_code_sort_key(c):
    code_str = str(c["code"])
    digits = ''.join(ch for ch in code_str if ch.isdigit())
    return int(digits) if digits else 9999

sorted_colleges = sorted(all_colleges, key=get_code_sort_key)

colleges_json = json.dumps([{
    "code": c["code"],
    "name": c["name"],
    "city": c["city"],
    "type": c["type"],
    "fee": c["fee"],
    "pkg": c["h_pkg"],
    "url": f"/colleges/profiles/{c['slug']}.html"
} for c in sorted_colleges])

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU College Code List (001 to 999) — Complete Master Institute Codes Directory</title>
  <meta name="description" content="Complete Dr. A.P.J. Abdul Kalam Technical University (AKTU) college code directory. Search all affiliated government and private engineering institutes across UP by institute code, city, fee, and branches for UPTAC counseling.">
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
    "description": "Complete reference list of AKTU college codes for UPTAC choice filling and counseling."
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://akturesults.in/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Colleges", "item": "https://akturesults.in/colleges/" }},
      {{ "@type": "ListItem", "position": 3, "name": "College Code List", "item": "https://akturesults.in/colleges/aktu-college-code-list.html" }}
    ]
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
    const colleges = {colleges_json};

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
    f.write(html)

print("Updated colleges/aktu-college-code-list.html successfully!")
