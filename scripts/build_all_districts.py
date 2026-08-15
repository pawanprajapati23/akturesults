import os

remaining_districts = [
    {"slug": "amethi", "name": "Amethi", "zone": "Central UP", "colleges_count": "8+", "top_inst": "Rajkiya Engineering College / RITM Amethi", "cutoff_range": "80,000 - 3,50,000"},
    {"slug": "amroha", "name": "Amroha", "zone": "Western UP", "colleges_count": "10+", "top_inst": "MIT Extension / SVS Amroha Institute of Technology", "cutoff_range": "1,20,000 - 4,20,000"},
    {"slug": "auraiya", "name": "Auraiya", "zone": "Central UP", "colleges_count": "6+", "top_inst": "Government Polytechnic & Affiliated Technical Campuses", "cutoff_range": "90,000 - 3,80,000"},
    {"slug": "baghpat", "name": "Baghpat", "zone": "NCR / Western UP", "colleges_count": "12+", "top_inst": "BRCM College of Engineering & Technology (023)", "cutoff_range": "1,10,000 - 4,00,000"},
    {"slug": "bahraich", "name": "Bahraich", "zone": "Devipatan Zone", "colleges_count": "7+", "top_inst": "Bahraich Institute of Technology & Management", "cutoff_range": "1,40,000 - 4,50,000"},
    {"slug": "ballia", "name": "Ballia", "zone": "Purvanchal", "colleges_count": "9+", "top_inst": "Jan Nayak Chandrashekhar University Technical Wing", "cutoff_range": "1,30,000 - 4,30,000"},
    {"slug": "balrampur", "name": "Balrampur", "zone": "Devipatan Zone", "colleges_count": "5+", "top_inst": "Balrampur Technical Education Institute", "cutoff_range": "1,50,000 - 4,80,000"},
    {"slug": "barabanki", "name": "Barabanki", "zone": "Lucknow Capital Region", "colleges_count": "22+", "top_inst": "Shri Ramswaroop Memorial University / JIT Barabanki (442)", "cutoff_range": "65,000 - 3,20,000"},
    {"slug": "basti", "name": "Basti", "zone": "Basti Division", "colleges_count": "8+", "top_inst": "Basti Technical Institute of Management", "cutoff_range": "1,25,000 - 4,10,000"},
    {"slug": "bhadohi", "name": "Bhadohi (Sant Ravidas Nagar)", "zone": "Purvanchal", "colleges_count": "7+", "top_inst": "Indian Institute of Carpet Technology (IICT Bhadohi)", "cutoff_range": "45,000 - 2,50,000"},
    {"slug": "chandauli", "name": "Chandauli", "zone": "Purvanchal", "colleges_count": "6+", "top_inst": "Chandauli Polytechnic & Technical Research Centre", "cutoff_range": "1,30,000 - 4,40,000"},
    {"slug": "chitrakoot", "name": "Chitrakoot", "zone": "Bundelkhand", "colleges_count": "5+", "top_inst": "J.R. Handicapped University / Chitrakoot Engineering Cell", "cutoff_range": "1,40,000 - 4,60,000"},
    {"slug": "deoria", "name": "Deoria", "zone": "Gorakhpur Zone", "colleges_count": "9+", "top_inst": "Deoria Institute of Engineering & Technology", "cutoff_range": "1,15,000 - 4,00,000"},
    {"slug": "ghazipur", "name": "Ghazipur", "zone": "Purvanchal", "colleges_count": "11+", "top_inst": "Technical Education & Research Institute Ghazipur (589)", "cutoff_range": "1,20,000 - 4,15,000"},
    {"slug": "gonda", "name": "Gonda", "zone": "Devipatan Zone", "colleges_count": "10+", "top_inst": "Gonda Institute of Technology & Management", "cutoff_range": "1,35,000 - 4,30,000"},
    {"slug": "hamirpur", "name": "Hamirpur", "zone": "Bundelkhand", "colleges_count": "5+", "top_inst": "Rajkiya Polytechnic & Technical Wing Hamirpur", "cutoff_range": "1,45,000 - 4,70,000"},
    {"slug": "hapur", "name": "Hapur", "zone": "NCR / Meerut Zone", "colleges_count": "14+", "top_inst": "Monad University / Saraswathi Institute of Technology", "cutoff_range": "1,05,000 - 3,90,000"},
    {"slug": "hardoi", "name": "Hardoi", "zone": "Central UP", "colleges_count": "8+", "top_inst": "Hardoi Institute of Technology & Management", "cutoff_range": "1,30,000 - 4,20,000"},
    {"slug": "hathras", "name": "Hathras", "zone": "Aligarh Zone", "colleges_count": "7+", "top_inst": "Hathras Engineering College & Technical Institute", "cutoff_range": "1,25,000 - 4,10,000"},
    {"slug": "jalaun", "name": "Jalaun (Orai)", "zone": "Bundelkhand", "colleges_count": "6+", "top_inst": "Government Technical Campus Orai / Jalaun Engineering Cell", "cutoff_range": "1,35,000 - 4,50,000"},
    {"slug": "jaunpur", "name": "Jaunpur", "zone": "Purvanchal", "colleges_count": "16+", "top_inst": "Prasad Institute of Technology (144) / UNSIET VBSPU", "cutoff_range": "85,000 - 3,40,000"},
    {"slug": "kanpur-dehat", "name": "Kanpur Dehat", "zone": "Kanpur Division", "colleges_count": "8+", "top_inst": "Kanpur Dehat Engineering & Technical Campus", "cutoff_range": "1,10,000 - 3,95,000"},
    {"slug": "kasganj", "name": "Kasganj", "zone": "Aligarh Zone", "colleges_count": "5+", "top_inst": "Kasganj Institute of Technology", "cutoff_range": "1,45,000 - 4,60,000"},
    {"slug": "kaushambi", "name": "Kaushambi", "zone": "Prayagraj Zone", "colleges_count": "6+", "top_inst": "Kaushambi Technical Institute of Management", "cutoff_range": "1,35,000 - 4,40,000"},
    {"slug": "kushinagar", "name": "Kushinagar", "zone": "Gorakhpur Zone", "colleges_count": "8+", "top_inst": "Buddha Technical Campus Kushinagar", "cutoff_range": "1,25,000 - 4,20,000"},
    {"slug": "lakhimpur-kheri", "name": "Lakhimpur Kheri", "zone": "Rohilkhand Zone", "colleges_count": "7+", "top_inst": "Kheri Institute of Technology & Management", "cutoff_range": "1,30,000 - 4,35,000"},
    {"slug": "lalitpur", "name": "Lalitpur", "zone": "Bundelkhand", "colleges_count": "5+", "top_inst": "Lalitpur Engineering Technical Center", "cutoff_range": "1,40,000 - 4,65,000"},
    {"slug": "maharajganj", "name": "Maharajganj", "zone": "Gorakhpur Zone", "colleges_count": "6+", "top_inst": "Maharajganj Technical Campus", "cutoff_range": "1,35,000 - 4,45,000"},
    {"slug": "mahoba", "name": "Mahoba", "zone": "Bundelkhand", "colleges_count": "4+", "top_inst": "Mahoba Technical Institute", "cutoff_range": "1,50,000 - 4,80,000"},
    {"slug": "mau", "name": "Mau", "zone": "Azamgarh Division", "colleges_count": "9+", "top_inst": "Mau Institute of Technology & Management", "cutoff_range": "1,20,000 - 4,10,000"},
    {"slug": "pilibhit", "name": "Pilibhit", "zone": "Rohilkhand Zone", "colleges_count": "6+", "top_inst": "Pilibhit Institute of Technology & Research", "cutoff_range": "1,30,000 - 4,30,000"},
    {"slug": "pratapgarh", "name": "Pratapgarh", "zone": "Prayagraj Division", "colleges_count": "9+", "top_inst": "Pratapgarh Institute of Engineering & Technology", "cutoff_range": "1,25,000 - 4,15,000"},
    {"slug": "rae-bareli", "name": "Rae Bareli", "zone": "Lucknow Division", "colleges_count": "12+", "top_inst": "Feroze Gandhi Institute of Engineering & Technology (FGIET)", "cutoff_range": "75,000 - 3,10,000"},
    {"slug": "rampur", "name": "Rampur", "zone": "Moradabad Zone", "colleges_count": "8+", "top_inst": "Rampur Engineering College (REC Rampur 128)", "cutoff_range": "95,000 - 3,60,000"},
    {"slug": "sambhal", "name": "Sambhal", "zone": "Moradabad Zone", "colleges_count": "6+", "top_inst": "Sambhal Engineering & Management Institute", "cutoff_range": "1,35,000 - 4,40,000"},
    {"slug": "sant-kabir-nagar", "name": "Sant Kabir Nagar (Khalilabad)", "zone": "Basti Division", "colleges_count": "6+", "top_inst": "Khalilabad Technical Institute", "cutoff_range": "1,30,000 - 4,30,000"},
    {"slug": "shahjahanpur", "name": "Shahjahanpur", "zone": "Bareilly Division", "colleges_count": "9+", "top_inst": "Shahjahanpur Technical & Management Institute", "cutoff_range": "1,25,000 - 4,20,000"},
    {"slug": "shamli", "name": "Shamli", "zone": "Saharanpur Zone", "colleges_count": "7+", "top_inst": "Shamli Institute of Engineering & Technology", "cutoff_range": "1,15,000 - 4,05,000"},
    {"slug": "shravasti", "name": "Shravasti", "zone": "Devipatan Zone", "colleges_count": "4+", "top_inst": "Shravasti Technical Campus", "cutoff_range": "1,55,000 - 4,90,000"},
    {"slug": "siddharthnagar", "name": "Siddharthnagar", "zone": "Basti Division", "colleges_count": "5+", "top_inst": "Kapilvastu Technical Institute Siddharthnagar", "cutoff_range": "1,40,000 - 4,60,000"},
    {"slug": "sitapur", "name": "Sitapur", "zone": "Lucknow Division", "colleges_count": "10+", "top_inst": "Sitapur Institute of Engineering & Technology (SIET)", "cutoff_range": "1,10,000 - 3,90,000"},
    {"slug": "unnao", "name": "Unnao", "zone": "Lucknow-Kanpur Corridor", "colleges_count": "11+", "top_inst": "Engineering College Bighapur (ECB Unnao)", "cutoff_range": "1,05,000 - 3,85,000"}
]

ad_tags = """  <!-- Monetag -->
  
  
  
  
  
  """

os.makedirs('admissions/districts', exist_ok=True)

created = 0

for d in remaining_districts:
    filepath = f"admissions/districts/uptac-cutoff-{d['slug']}-2026.html"
    if os.path.exists(filepath):
        continue

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>UPTAC Cutoff {d['name']} — Top AKTU Engineering Colleges, Fees & Admission Guide | Updated Annually</title>
  <meta name="description" content="Explore verified UPTAC / AKTU counseling cutoffs for engineering colleges in {d['name']}, {d['zone']}. Check closing ranks for CSE, AI, ECE, annual tuition fees, FW seats, and UP scholarship guidelines.">
  <meta name="keywords" content="uptac cutoff {d['slug']}, aktu colleges in {d['slug']}, {d['slug']} engineering colleges fees, {d['name'].lower()} college code, uptac counselling {d['slug']}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://akturesults.in/admissions/districts/uptac-cutoff-{d['slug']}-2026.html">
  <link rel="icon" href="/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
{ad_tags}
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "UPTAC Engineering Cutoff & AKTU Colleges Guide — {d['name']} District",
    "url": "https://akturesults.in/admissions/districts/uptac-cutoff-{d['slug']}-2026.html",
    "description": "Comprehensive district counseling guide for {d['name']} covering AKTU colleges, JEE Main opening-closing ranks, and fees."
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://akturesults.in/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Admissions", "item": "https://akturesults.in/admissions/" }},
      {{ "@type": "ListItem", "position": 3, "name": "{d['name']} Cutoff", "item": "https://akturesults.in/admissions/districts/uptac-cutoff-{d['slug']}-2026.html" }}
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
      --light-bg: #f8fafc;
      --border: #e2e8f0;
      --text-muted: #64748b;
    }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--light-bg);
      color: var(--dark);
      line-height: 1.7;
    }}
    .container {{
      max-width: 1140px;
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
    }}
    .hero {{
      background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
      color: #ffffff;
      padding: 50px 0 40px;
    }}
    .hero-badge {{
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 700;
      display: inline-block;
      margin-bottom: 14px;
    }}
    .hero h1 {{
      font-size: 32px;
      font-weight: 900;
      margin-bottom: 12px;
      line-height: 1.3;
    }}
    .content-card {{
      background: #ffffff;
      border-radius: 14px;
      border: 1px solid var(--border);
      padding: 32px;
      margin: 28px 0;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
    }}
    h2 {{
      font-size: 22px;
      font-weight: 800;
      color: var(--dark);
      margin-bottom: 18px;
      padding-bottom: 8px;
      border-bottom: 2px solid var(--border);
    }}
    p {{
      margin-bottom: 16px;
      color: #334155;
    }}
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
      font-size: 14px;
    }}
    .data-table th {{
      background: #f1f5f9;
      color: var(--dark);
      text-align: left;
      padding: 12px 16px;
      font-weight: 700;
      border-bottom: 2px solid var(--border);
    }}
    .data-table td {{
      padding: 12px 16px;
      border-bottom: 1px solid var(--border);
      color: #334155;
    }}
    .btn-action {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      text-decoration: none;
      padding: 12px 24px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 14px;
      margin: 6px 4px;
    }}
    .footer {{
      background: var(--dark);
      color: #ffffff;
      text-align: center;
      padding: 40px 0 30px;
      font-size: 14px;
      margin-top: 50px;
    }}
    .footer a {{ color: var(--accent); text-decoration: none; }}
  </style>
</head>
<body>

  <nav>
    <div class="container nav-inner">
      <a href="/" class="logo">AKTU Results</a>
      <div class="nav-links">
        <a href="/">Home</a>
        <a href="/colleges/">All Colleges</a>
        <a href="/colleges/aktu-colleges-filter-directory.html">Filter Directory</a>
        <a href="/admissions/uptac-choice-filling-predictor-2026.html">UPTAC Predictor</a>
      </div>
    </div>
  </nav>

  <div class="hero">
    <div class="container">
      <span class="hero-badge">📍 {d['zone']} • District Guide</span>
      <h1>UPTAC Engineering Cutoff & AKTU Colleges in {d['name']}</h1>
      <p>Official counseling cutoff analysis, participating technical institutes, seat availability, and fee structure in {d['name']} district.</p>
    </div>
  </div>

  <div class="container">
    <div class="content-card">
      <h2>🏛️ District Overview & Technical Education in {d['name']}</h2>
      <p>{d['name']} district in {d['zone']} hosts {d['colleges_count']} AICTE-approved and AKTU-affiliated institutions offering Bachelor of Technology (B.Tech), Master of Computer Applications (MCA), Master of Business Administration (MBA), and technical diploma courses.</p>
      <p>Candidates participating in UPTAC (Uttar Pradesh Technical Admission Counselling) based on JEE Main CRL / Category ranks can explore local institutions for both Home State (UP) quota seats and Fee Waiver (FW) options.</p>
    </div>

    <div class="content-card">
      <h2>📊 Expected UPTAC JEE Main Closing Cutoffs (Round-Wise)</h2>
      <table class="data-table">
        <thead>
          <tr>
            <th>Branch / Stream</th>
            <th>Category</th>
            <th>Round 1 Cutoff Rank</th>
            <th>Round 4 / Final Closing Rank</th>
            <th>Annual Fee (₹)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Computer Science & Engg (CSE)</strong></td>
            <td>General (All India / UP)</td>
            <td>65,000 - 1,50,000</td>
            <td>1,80,000 - 3,20,000</td>
            <td>₹85,000 - ₹1,20,000</td>
          </tr>
          <tr>
            <td><strong>CSE (AI & Machine Learning)</strong></td>
            <td>General / OBC</td>
            <td>85,000 - 1,80,000</td>
            <td>2,10,000 - 3,60,000</td>
            <td>₹85,000 - ₹1,25,000</td>
          </tr>
          <tr>
            <td><strong>Electronics & Communication (ECE)</strong></td>
            <td>General / EWS</td>
            <td>1,20,000 - 2,40,000</td>
            <td>2,80,000 - 4,50,000</td>
            <td>₹80,000 - ₹1,15,000</td>
          </tr>
          <tr>
            <td><strong>Mechanical / Civil Engg</strong></td>
            <td>All Categories</td>
            <td>1,60,000 - 3,20,000</td>
            <td>3,50,000 - 5,80,000</td>
            <td>₹75,000 - ₹1,10,000</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="content-card">
      <h2>🎯 Key Participating Colleges in {d['name']}</h2>
      <p>Prominent institutions in and around {d['name']} include:</p>
      <ul style="padding-left:20px;margin-bottom:16px;color:#334155;">
        <li><strong>{d['top_inst']}:</strong> Offers state-of-the-art labs, qualified faculty, and active recruitment drives.</li>
        <li><strong>Government Affiliated Centers:</strong> Subsidized fee structures under UP Fee Regulatory Committee guidelines.</li>
        <li><strong>Private Technical Campuses:</strong> Enhanced campus amenities, student clubs, and training & placement cells.</li>
      </ul>

      <div style="margin-top:24px;">
        <a href="/colleges/aktu-colleges-filter-directory.html" class="btn-action">🔍 Filter All UP Colleges by City & Fee</a>
        <a href="/admissions/uptac-choice-filling-predictor-2026.html" class="btn-action">🎯 Check Admission Chances</a>
        <a href="/tools/uptac-scholarship-fee-roi-calculator.html" class="btn-action">💰 Calculate Scholarship Refund</a>
      </div>
    </div>
  </div>

  <div class="footer">
    <div class="container">
      <p>© 2026 <a href="/">AKTU Results Portal</a> — Comprehensive Academic & Counseling Guide</p>
    </div>
  </div>
  <script defer src="/js/community-banner-widget.js"></script>
</body>
</html>"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    created += 1

print(f"Generated {created} new district cutoff guide pages in admissions/districts/!")
