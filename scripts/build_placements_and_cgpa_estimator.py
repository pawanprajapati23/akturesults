import os

# 1. BUILD PLACEMENT & HIRING TRACKER: placements/aktu-off-campus-hiring-drives-2026.html
placements_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU Off-Campus Hiring & MNC Placement Drive Tracker 2026 (TCS, Infosys, Wipro, Cognizant)</title>
  <meta name="description" content="Live tracker for AKTU B.Tech off-campus placement drives 2026. Eligibility criteria, packages (LPA), exam dates, test patterns, and direct apply links for TCS NQT, Infosys, Wipro, and Accenture.">
  <link rel="canonical" href="https://akturesults.in/placements/aktu-off-campus-hiring-drives-2026.html">
  <meta property="og:title" content="AKTU Off-Campus Hiring & MNC Placement Tracker 2026">
  <meta property="og:description" content="Daily updated off-campus drives, eligibility criteria, and test patterns for AKTU engineering students.">
  <meta property="og:url" content="https://akturesults.in/placements/aktu-off-campus-hiring-drives-2026.html">
  <meta property="og:type" content="article">
  <meta property="og:image" content="https://akturesults.in/images/og-banner.png">
  <meta name="twitter:card" content="summary_large_image">

  <!-- Monetization Ad Tags -->
  <meta name="monetag" content="4b20c6816d7cac00b3d6430a41d4d86f" />
  <script src="https://quge5.com/88/tag.min.js" data-zone="257546" async data-cfasync="false"></script>
  <script async="async" data-cfasync="false" src="https://pl30261454.effectivecpmnetwork.com/1018cdea726c22b2c7ca9bbd11cccba8/invoke.js"></script>
  <script src="https://pl30261457.effectivecpmnetwork.com/5c/91/1d/5c911de89a0e11deb0df88b1aedb08a1.js"></script>
  <script>(function(s){s.dataset.zone='11257064',s.src='https://nap5k.com/tag.min.js'})([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement('script')))</script>

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "AKTU Off-Campus Hiring & MNC Placement Drive Tracker 2026",
    "description": "Live off-campus placement drives and eligibility criteria for AKTU engineering students.",
    "author": { "@type": "Organization", "name": "AKTU Results" },
    "publisher": { "@type": "Organization", "name": "AKTU Results", "url": "https://akturesults.in/" }
  }
  </script>

  <style>
    :root {
      --primary: #0f172a;
      --accent: #2563eb;
      --success: #059669;
      --warning: #d97706;
      --card-bg: #ffffff;
      --text: #1e293b;
      --muted: #64748b;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', system-ui, -apple-system, sans-serif; }
    body { background: #f8fafc; color: var(--text); line-height: 1.6; }
    .container { max-width: 1150px; margin: 0 auto; padding: 20px; }

    header { background: #0f172a; color: white; padding: 18px 0; border-bottom: 3px solid var(--accent); }
    .header-content { display: flex; justify-content: space-between; align-items: center; max-width: 1150px; margin: 0 auto; padding: 0 20px; }
    .logo { font-size: 20px; font-weight: 800; color: white; text-decoration: none; display: flex; align-items: center; gap: 8px; }
    .back-btn { color: #94a3b8; text-decoration: none; font-size: 14px; font-weight: 600; padding: 6px 14px; background: rgba(255,255,255,0.08); border-radius: 8px; }
    .back-btn:hover { color: white; background: rgba(255,255,255,0.15); }

    .hero { text-align: center; padding: 35px 20px 25px; }
    .hero-badge { display: inline-block; padding: 6px 16px; background: #dbeafe; color: #1e40af; border-radius: 30px; font-size: 13px; font-weight: 700; margin-bottom: 12px; }
    .hero h1 { font-size: 30px; font-weight: 800; color: #0f172a; margin-bottom: 10px; }
    .hero p { color: var(--muted); font-size: 16px; max-width: 800px; margin: 0 auto; }

    /* Filters */
    .filter-bar { background: white; padding: 18px 22px; border-radius: 14px; border: 1px solid #e2e8f0; display: flex; gap: 15px; flex-wrap: wrap; align-items: center; justify-content: space-between; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.03); }
    .filter-group { display: flex; align-items: center; gap: 10px; }
    .filter-label { font-size: 13px; font-weight: 700; color: #475569; }
    .filter-select { padding: 8px 12px; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 13px; font-weight: 600; color: #0f172a; outline: none; }

    /* Drive Cards */
    .drive-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 20px; }
    .drive-card { background: white; border-radius: 16px; padding: 24px; border: 1.5px solid #e2e8f0; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.04); transition: transform 0.2s, border-color 0.2s; display: flex; flex-direction: column; justify-content: space-between; }
    .drive-card:hover { transform: translateY(-3px); border-color: var(--accent); }

    .drive-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 14px; }
    .comp-name { font-size: 19px; font-weight: 800; color: #0f172a; }
    .role-badge { font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 20px; background: #eff6ff; color: #1e40af; border: 1px solid #bfdbfe; }
    .pkg-tag { font-size: 18px; font-weight: 900; color: #059669; margin: 4px 0 10px; }

    .req-list { list-style: none; margin: 12px 0 18px; font-size: 13px; color: #475569; }
    .req-list li { display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }
    .req-list li strong { color: #1e293b; }

    .apply-btn { display: block; text-align: center; padding: 12px; background: #0f172a; color: white; text-decoration: none; border-radius: 10px; font-size: 14px; font-weight: 700; transition: all 0.2s; }
    .apply-btn:hover { background: var(--accent); }

    .content-card { background: white; border-radius: 16px; padding: 35px; margin: 30px 0; border: 1px solid #e2e8f0; }
    .content-card h2 { font-size: 22px; font-weight: 800; color: #0f172a; margin: 25px 0 12px; }
    .content-card h2:first-child { margin-top: 0; }
    .content-card p, .content-card li { font-size: 15px; color: #334155; line-height: 1.7; margin-bottom: 12px; }
    .content-card ul { padding-left: 20px; }
  </style>
</head>
<body>

  <header>
    <div class="header-content">
      <a href="/" class="logo">🎓 AKTU Results</a>
      <a href="/calculators.html" class="back-btn">← All Tools</a>
    </div>
  </header>

  <div class="container">
    <div class="hero">
      <span class="hero-badge">💼 2026 OFFICIAL PLACEMENT CELL SUITE</span>
      <h1>🚀 AKTU Off-Campus Hiring &amp; MNC Drive Tracker 2026</h1>
      <p>Verified off-campus recruitment drives, National Qualifier Tests (NQT), eligibility benchmarks, and direct application portals for AKTU affiliated college students.</p>
    </div>

    <!-- Filters -->
    <div class="filter-bar">
      <div class="filter-group">
        <span class="filter-label">Target Batch:</span>
        <select class="filter-select" id="batch-filter" onchange="filterDrives()">
          <option value="all">All Batches (2025 / 2026 / 2027)</option>
          <option value="2026" selected>Batch 2026 (Final Year)</option>
          <option value="2025">Batch 2025 (Freshers)</option>
        </select>
      </div>

      <div class="filter-group">
        <span class="filter-label">Eligibility Criteria:</span>
        <select class="filter-select" id="cgpa-filter" onchange="filterDrives()">
          <option value="all">Any CGPA / %</option>
          <option value="60">60% or 6.0 CGPA (Standard)</option>
          <option value="65">65% or 6.5 CGPA</option>
          <option value="no_crit">No Minimum Percentage</option>
        </select>
      </div>
    </div>

    <!-- Drives Grid -->
    <div class="drive-grid" id="drives-container">
      <!-- TCS NQT -->
      <div class="drive-card" data-batch="2026" data-cgpa="60">
        <div>
          <div class="drive-header">
            <div class="comp-name">Tata Consultancy Services (TCS)</div>
            <span class="role-badge">TCS NQT National Drive</span>
          </div>
          <div class="pkg-tag">₹3.36 LPA (Ninja) to ₹9.0 LPA (Prime)</div>
          <ul class="req-list">
            <li>📌 <strong>Eligibility:</strong> 60% or 6.0 CGPA throughout (10th, 12th, B.Tech)</li>
            <li>📌 <strong>Back Paper Rule:</strong> Max 1 Active Backlog allowed at test time</li>
            <li>📌 <strong>Eligible Branches:</strong> B.Tech All Branches, MCA, M.Tech</li>
            <li>📌 <strong>Exam Pattern:</strong> Numerical Ability, Reasoning, Verbal + Advanced Coding</li>
          </ul>
        </div>
        <a href="https://www.tcs.com/careers" target="_blank" rel="noopener noreferrer" class="apply-btn">Apply on Official Portal →</a>
      </div>

      <!-- Infosys SP & DSE -->
      <div class="drive-card" data-batch="2026" data-cgpa="60">
        <div>
          <div class="drive-header">
            <div class="comp-name">Infosys Limited</div>
            <span class="role-badge">Specialist Programmer (SP)</span>
          </div>
          <div class="pkg-tag">₹6.25 LPA (DSE) / ₹9.5 LPA (SP)</div>
          <ul class="req-list">
            <li>📌 <strong>Eligibility:</strong> 60% or 6.0 CGPA in Graduation</li>
            <li>📌 <strong>Back Paper Rule:</strong> Zero Active Backlogs at joining</li>
            <li>📌 <strong>Eligible Branches:</strong> B.Tech (CSE, IT, ECE, EE, Mechanical)</li>
            <li>📌 <strong>Exam Pattern:</strong> HackWithInfy / InfyTQ Advanced Data Structures &amp; Algorithms</li>
          </ul>
        </div>
        <a href="https://www.infosys.com/careers" target="_blank" rel="noopener noreferrer" class="apply-btn">Apply on Official Portal →</a>
      </div>

      <!-- Wipro Elite -->
      <div class="drive-card" data-batch="2026" data-cgpa="60">
        <div>
          <div class="drive-header">
            <div class="comp-name">Wipro Elite NLTH</div>
            <span class="role-badge">Project Engineer</span>
          </div>
          <div class="pkg-tag">₹3.50 LPA to ₹6.50 LPA (Turbo)</div>
          <ul class="req-list">
            <li>📌 <strong>Eligibility:</strong> 60% (6.0 CGPA) in 10th, 12th &amp; Engineering</li>
            <li>📌 <strong>Back Paper Rule:</strong> 1 active backlog permitted during assessment</li>
            <li>📌 <strong>Eligible Branches:</strong> All Engineering Branches (Circuital &amp; Non-Circuital)</li>
            <li>📌 <strong>Exam Pattern:</strong> English Essay, Aptitude &amp; Coding (Java/Python/C++)</li>
          </ul>
        </div>
        <a href="https://careers.wipro.com" target="_blank" rel="noopener noreferrer" class="apply-btn">Apply on Official Portal →</a>
      </div>

      <!-- Cognizant GenC -->
      <div class="drive-card" data-batch="2026" data-cgpa="60">
        <div>
          <div class="drive-header">
            <div class="comp-name">Cognizant Technology Solutions</div>
            <span class="role-badge">GenC Next / GenC Elevate</span>
          </div>
          <div class="pkg-tag">₹4.0 LPA (GenC) to ₹6.75 LPA (Next)</div>
          <ul class="req-list">
            <li>📌 <strong>Eligibility:</strong> 60% across 10th, 12th &amp; B.Tech aggregate</li>
            <li>📌 <strong>Back Paper Rule:</strong> No active backlogs allowed</li>
            <li>📌 <strong>Eligible Branches:</strong> CSE, IT, ECE, EEE, AI, Data Science</li>
            <li>📌 <strong>Exam Pattern:</strong> Skill-based Coding, SQL Queries &amp; Full Stack MCQ</li>
          </ul>
        </div>
        <a href="https://www.cognizant.com/careers" target="_blank" rel="noopener noreferrer" class="apply-btn">Apply on Official Portal →</a>
      </div>

      <!-- Capgemini Exceller -->
      <div class="drive-card" data-batch="2026" data-cgpa="60">
        <div>
          <div class="drive-header">
            <div class="comp-name">Capgemini</div>
            <span class="role-badge">Exceller Placement Drive</span>
          </div>
          <div class="pkg-tag">₹4.25 LPA to ₹7.50 LPA (Senior Analyst)</div>
          <ul class="req-list">
            <li>📌 <strong>Eligibility:</strong> 60% or 6.0 CGPA in Diploma/Graduation</li>
            <li>📌 <strong>Back Paper Rule:</strong> 0 Backlog at interview round</li>
            <li>📌 <strong>Eligible Branches:</strong> All Engineering Streams</li>
            <li>📌 <strong>Exam Pattern:</strong> Pseudocode, Game-based Aptitude &amp; Behavioral Test</li>
          </ul>
        </div>
        <a href="https://www.capgemini.com/careers" target="_blank" rel="noopener noreferrer" class="apply-btn">Apply on Official Portal →</a>
      </div>

      <!-- Accenture ASE -->
      <div class="drive-card" data-batch="2026" data-cgpa="65">
        <div>
          <div class="drive-header">
            <div class="comp-name">Accenture India</div>
            <span class="role-badge">Associate Software Engineer (ASE)</span>
          </div>
          <div class="pkg-tag">₹4.50 LPA to ₹6.50 LPA (FSE)</div>
          <ul class="req-list">
            <li>📌 <strong>Eligibility:</strong> 65% (6.5 CGPA) or 6.5/10 scale in B.Tech</li>
            <li>📌 <strong>Back Paper Rule:</strong> No active backlogs during onboarding</li>
            <li>📌 <strong>Eligible Branches:</strong> All B.Tech / BE / MCA / M.Tech</li>
            <li>📌 <strong>Exam Pattern:</strong> Cognitive, Technical MCQ + 2 Coding Problems</li>
          </ul>
        </div>
        <a href="https://www.accenture.com/in-en/careers" target="_blank" rel="noopener noreferrer" class="apply-btn">Apply on Official Portal →</a>
      </div>
    </div>

    <div class="content-card">
      <h2>How AKTU Students Can Crack Tier-1 MNC Placement Drives</h2>
      <p>Over 80,000 AKTU engineering students appear for mass IT and product recruitment drives every academic year. The key to securing multiple job offers with packages ranging from ₹4.5 LPA to ₹12 LPA is maintaining strict compliance with recruitment eligibility standards:</p>
      <ul>
        <li><strong>The 60.0% All-Clear Rule:</strong> Over 85% of MNCs (TCS, Infosys, Cognizant, Wipro) filter candidates with an automated threshold of <strong>60.00% aggregate</strong> (which is equivalent to <strong>6.75 CGPA</strong> in AKTU using <code>(CGPA - 0.75) * 10</code> formula). Keep your CGPA above 6.75 to prevent automated ATS resume rejections.</li>
        <li><strong>Clear All Backlogs Before 7th Semester:</strong> While some national drives allow appearing with 1 active back, final onboarding requires submission of a clean provisional degree certificate with zero pending carryovers.</li>
        <li><strong>Practice Core Coding (Data Structures &amp; SQL):</strong> Almost all 2026 hiring assessments feature at least 2 coding problems (Arrays, Strings, HashMaps, Trees) and 5+ SQL query questions.</li>
      </ul>
    </div>
  </div>

  <script>
    function filterDrives() {
      const batch = document.getElementById('batch-filter').value;
      const cgpa = document.getElementById('cgpa-filter').value;
      const cards = document.querySelectorAll('.drive-card');

      cards.forEach(card => {
        let show = true;
        if (batch !== 'all' && card.dataset.batch !== batch) show = false;
        if (cgpa !== 'all') {
          if (cgpa === '60' && parseInt(card.dataset.cgpa) > 60) show = false;
          if (cgpa === '65' && parseInt(card.dataset.cgpa) > 65) show = false;
        }
        card.style.display = show ? 'flex' : 'none';
      });
    }
  </script>
</body>
</html>"""

with open("placements/aktu-off-campus-hiring-drives-2026.html", "w", encoding="utf-8") as f:
    f.write(placements_html)
print("Built placements/aktu-off-campus-hiring-drives-2026.html successfully!")


# 2. BUILD FUTURE CGPA TARGET ESTIMATOR: tools/aktu-cgpa-target-estimator.html
estimator_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU Future CGPA Goal Target Estimator (Semester 1 to 8 SGPA Planner)</title>
  <meta name="description" content="Calculate required SGPA in remaining semesters to achieve your target CGPA (7.5 for Honours, 6.75 for 60% MNC eligibility). Semester 1 to 8 credit-weighted milestone planner.">
  <link rel="canonical" href="https://akturesults.in/tools/aktu-cgpa-target-estimator.html">
  <meta property="og:title" content="AKTU Future CGPA Goal Target Estimator">
  <meta property="og:description" content="Calculate exact required SGPA in upcoming semesters to hit your dream final CGPA & Honours degree.">
  <meta property="og:url" content="https://akturesults.in/tools/aktu-cgpa-target-estimator.html">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://akturesults.in/images/og-banner.png">
  <meta name="twitter:card" content="summary_large_image">

  <!-- Monetization Ad Tags -->
  <meta name="monetag" content="4b20c6816d7cac00b3d6430a41d4d86f" />
  <script src="https://quge5.com/88/tag.min.js" data-zone="257546" async data-cfasync="false"></script>
  <script async="async" data-cfasync="false" src="https://pl30261454.effectivecpmnetwork.com/1018cdea726c22b2c7ca9bbd11cccba8/invoke.js"></script>
  <script src="https://pl30261457.effectivecpmnetwork.com/5c/91/1d/5c911de89a0e11deb0df88b1aedb08a1.js"></script>
  <script>(function(s){s.dataset.zone='11257064',s.src='https://nap5k.com/tag.min.js'})([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement('script')))</script>

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "AKTU Future CGPA Goal Target Estimator",
    "url": "https://akturesults.in/tools/aktu-cgpa-target-estimator.html",
    "description": "Calculates required semester SGPA to achieve target graduation CGPA for AKTU B.Tech.",
    "applicationCategory": "EducationalApplication",
    "operatingSystem": "All"
  }
  </script>

  <style>
    :root {
      --primary: #0f172a;
      --accent: #2563eb;
      --success: #059669;
      --warning: #d97706;
      --danger: #dc2626;
      --text: #1e293b;
      --muted: #64748b;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', system-ui, -apple-system, sans-serif; }
    body { background: #f8fafc; color: var(--text); line-height: 1.6; }
    .container { max-width: 1050px; margin: 0 auto; padding: 20px; }

    header { background: #0f172a; color: white; padding: 18px 0; border-bottom: 3px solid var(--accent); }
    .header-content { display: flex; justify-content: space-between; align-items: center; max-width: 1050px; margin: 0 auto; padding: 0 20px; }
    .logo { font-size: 20px; font-weight: 800; color: white; text-decoration: none; display: flex; align-items: center; gap: 8px; }
    .back-btn { color: #94a3b8; text-decoration: none; font-size: 14px; font-weight: 600; padding: 6px 14px; background: rgba(255,255,255,0.08); border-radius: 8px; }
    .back-btn:hover { color: white; background: rgba(255,255,255,0.15); }

    .hero { text-align: center; padding: 35px 20px 25px; }
    .hero-badge { display: inline-block; padding: 6px 16px; background: #dbeafe; color: #1e40af; border-radius: 30px; font-size: 13px; font-weight: 700; margin-bottom: 12px; }
    .hero h1 { font-size: 28px; font-weight: 800; color: #0f172a; margin-bottom: 10px; }
    .hero p { color: var(--muted); font-size: 16px; max-width: 750px; margin: 0 auto; }

    .grid-2 { display: grid; grid-template-columns: 1.1fr 1fr; gap: 25px; margin: 20px 0 40px; }
    .card { background: white; border-radius: 16px; padding: 25px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; }
    .card-title { font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 18px; display: flex; align-items: center; gap: 10px; border-bottom: 2px solid #f1f5f9; padding-bottom: 10px; }

    .form-group { margin-bottom: 15px; }
    .form-label { display: block; font-size: 13px; font-weight: 700; color: #334155; margin-bottom: 6px; }
    .form-input, .form-select { width: 100%; padding: 10px 12px; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 14px; color: #0f172a; background: white; }
    .form-input:focus, .form-select:focus { border-color: var(--accent); outline: none; }

    .calc-btn { width: 100%; padding: 14px; background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%); color: white; border: none; border-radius: 12px; font-size: 16px; font-weight: 700; cursor: pointer; transition: all 0.2s; box-shadow: 0 4px 12px rgba(37,99,235,0.25); margin-top: 10px; }
    .calc-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(37,99,235,0.35); }

    /* Output Card */
    .target-display { text-align: center; padding: 25px; border-radius: 14px; background: #f8fafc; border: 1.5px solid #e2e8f0; margin-bottom: 20px; }
    .big-target { font-size: 48px; font-weight: 900; color: #1e3a8a; line-height: 1; margin: 10px 0; }
    .feasibility-pill { display: inline-block; padding: 6px 16px; border-radius: 20px; font-size: 13px; font-weight: 800; text-transform: uppercase; }
    .feas-easy { background: #dcfce7; color: #15803d; }
    .feas-mod { background: #dbeafe; color: #1e40af; }
    .feas-hard { background: #fef3c7; color: #b45309; }
    .feas-imp { background: #fee2e2; color: #b91c1c; }

    .breakdown-row { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px dashed #e2e8f0; font-size: 14px; }
    .breakdown-row:last-child { border-bottom: none; }

    .content-card { background: white; border-radius: 16px; padding: 35px; margin: 30px 0; border: 1px solid #e2e8f0; }
    .content-card h2 { font-size: 22px; font-weight: 800; color: #0f172a; margin: 25px 0 12px; }
    .content-card h2:first-child { margin-top: 0; }
    .content-card p, .content-card li { font-size: 15px; color: #334155; line-height: 1.7; margin-bottom: 12px; }
    .content-card ul { padding-left: 20px; }

    @media (max-width: 800px) {
      .grid-2 { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <header>
    <div class="header-content">
      <a href="/" class="logo">🎓 AKTU Results</a>
      <a href="/calculators.html" class="back-btn">← All Tools</a>
    </div>
  </header>

  <div class="container">
    <div class="hero">
      <span class="hero-badge">🎯 ACADEMIC ROADMAP PLANNER</span>
      <h1>📈 AKTU Future CGPA Goal Target Estimator</h1>
      <p>Find out the exact SGPA you must score in each upcoming semester to reach your target final CGPA, B.Tech Honours eligibility (7.50+), or MNC recruitment threshold (6.75+).</p>
    </div>

    <div class="grid-2">
      <!-- Input -->
      <div class="card">
        <div class="card-title">📝 Enter Current Status &amp; Target</div>
        
        <div class="form-group">
          <label class="form-label">Completed Semesters</label>
          <select id="in-comp-sem" class="form-select">
            <option value="1">1 Semester Completed (7 Remaining)</option>
            <option value="2">2 Semesters Completed (6 Remaining)</option>
            <option value="3">3 Semesters Completed (5 Remaining)</option>
            <option value="4" selected>4 Semesters Completed (4 Remaining - 2nd Year End)</option>
            <option value="5">5 Semesters Completed (3 Remaining)</option>
            <option value="6">6 Semesters Completed (2 Remaining - 3rd Year End)</option>
            <option value="7">7 Semesters Completed (1 Remaining - Final Sem)</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label">Current Overall CGPA (Up to Completed Sem)</label>
          <input type="number" id="in-curr-cgpa" class="form-input" value="6.80" step="0.01" min="0" max="10">
        </div>

        <div class="form-group">
          <label class="form-label">Your Target Final Graduation CGPA</label>
          <select id="in-target-cgpa" class="form-select">
            <option value="7.50" selected>7.50 CGPA (B.Tech Honours Degree Threshold)</option>
            <option value="6.75">6.75 CGPA (Equivalent to 60.0% for TCS/Infosys MNC Eligibility)</option>
            <option value="7.00">7.00 CGPA (First Division Standard)</option>
            <option value="8.00">8.00 CGPA (Tier-1 Product Company Cutoff)</option>
            <option value="8.50">8.50 CGPA (University Rank Contender)</option>
          </select>
        </div>

        <button class="calc-btn" onclick="estimateTarget()">
          🚀 Calculate Required Semester SGPA
        </button>
      </div>

      <!-- Output -->
      <div class="card">
        <div class="card-title">📊 Required Semester Performance</div>
        
        <div class="target-display">
          <div style="font-size: 12px; font-weight: 700; color: #64748b; text-transform: uppercase;">Required Average SGPA / Sem</div>
          <div id="out-req-sgpa" class="big-target">8.20</div>
          <div id="out-feas-pill" class="feasibility-pill feas-mod">🎯 HIGHLY ACHIEVABLE (WITH FOCUS)</div>
        </div>

        <div style="margin: 15px 0;">
          <div class="breakdown-row">
            <span style="color:#64748b;">Remaining Semesters:</span>
            <strong id="out-rem-sems" style="color:#0f172a;">4 Semesters (Sem 5 to 8)</strong>
          </div>
          <div class="breakdown-row">
            <span style="color:#64748b;">Current Equivalent %:</span>
            <strong id="out-curr-pct" style="color:#0f172a;">60.50%</strong>
          </div>
          <div class="breakdown-row">
            <span style="color:#64748b;">Target Equivalent %:</span>
            <strong id="out-target-pct" style="color:#059669;">67.50%</strong>
          </div>
          <div class="breakdown-row">
            <span style="color:#64748b;">Required Sessional/CT Average:</span>
            <strong id="out-req-sessional" style="color:#2563eb;">~25-27 / 30 Internal</strong>
          </div>
        </div>

        <div id="out-advice" style="background:#eff6ff; border-left:4px solid #2563eb; padding:12px; border-radius:0 8px 8px 0; font-size:13px; color:#1e40af; margin-top:10px;">
          To reach 7.50 CGPA, maintain an average SGPA of 8.20 across your remaining 4 semesters. Aim for Grade A / A+ in all 4-credit core theory subjects.
        </div>
      </div>
    </div>

    <div class="content-card">
      <h2>How AKTU Cumulative Grade Point Average (CGPA) is Weighted</h2>
      <p>Under the AKTU CBCS Ordinance, CGPA is the cumulative weighted average of all semester grade points divided by total completed credits:</p>
      <p><code>CGPA = Σ(Semester SGPA × Semester Credits) / Total Completed Credits</code></p>
      <p>Since each B.Tech semester carries approximately 20 to 22 credits, early semesters (Sem 1 to 4) represent 50% of your total degree weight. If your early CGPA is lower than desired, scoring 8.0+ in 3rd and 4th year electives and major project work (which carry high credit multipliers) provides the fastest recovery to reach 7.50+ for Honours!</p>
    </div>
  </div>

  <script>
    function estimateTarget() {
      const compSems = parseInt(document.getElementById('in-comp-sem').value);
      const currCgpa = parseFloat(document.getElementById('in-curr-cgpa').value) || 6.5;
      const targetCgpa = parseFloat(document.getElementById('in-target-cgpa').value) || 7.5;

      const totalSems = 8;
      const remSems = totalSems - compSems;

      // Formula: (currCgpa * compSems + reqSgpa * remSems) / totalSems = targetCgpa
      const requiredTotalPoints = targetCgpa * totalSems;
      const currentPoints = currCgpa * compSems;
      const neededPoints = requiredTotalPoints - currentPoints;
      const reqSgpa = neededPoints / remSems;

      const currPct = Math.max(0, (currCgpa - 0.75) * 10);
      const targetPct = Math.max(0, (targetCgpa - 0.75) * 10);

      document.getElementById('out-req-sgpa').innerText = reqSgpa > 10 ? '10.0+ (Maxed)' : (reqSgpa < 0 ? '0.00 (Done)' : reqSgpa.toFixed(2));
      document.getElementById('out-rem-sems').innerText = `${remSems} Semesters (Sem ${compSems + 1} to 8)`;
      document.getElementById('out-curr-pct').innerText = currPct.toFixed(2) + '%';
      document.getElementById('out-target-pct').innerText = targetPct.toFixed(2) + '%';

      const pill = document.getElementById('out-feas-pill');
      const advice = document.getElementById('out-advice');

      if (reqSgpa > 10.0) {
        pill.className = 'feasibility-pill feas-imp';
        pill.innerText = '❌ MATHEMATICALLY IMPOSSIBLE';
        advice.innerHTML = `<strong>Advisory:</strong> Even with a perfect 10.0 SGPA in all remaining ${remSems} semesters, your maximum attainable final CGPA is <strong>${((currentPoints + 10 * remSems) / totalSems).toFixed(2)}</strong>. Try setting a slightly lower target like 7.00.`;
      } else if (reqSgpa >= 8.5) {
        pill.className = 'feasibility-pill feas-hard';
        pill.innerText = '⚠️ CHALLENGING (REQUIRES 8.5+ SGPA)';
        advice.innerHTML = `To hit ${targetCgpa.toFixed(2)} CGPA, you will need consistent <strong>Grade O & A+</strong> in all subjects and high internal sessional marks (27+/30).`;
      } else if (reqSgpa >= 7.5) {
        pill.className = 'feasibility-pill feas-mod';
        pill.innerText = '🎯 HIGHLY ACHIEVABLE (WITH FOCUS)';
        advice.innerHTML = `To reach ${targetCgpa.toFixed(2)} CGPA, maintain an average SGPA of <strong>${reqSgpa.toFixed(2)}</strong> across remaining ${remSems} semesters. Aim for Grade A in all 4-credit subjects.`;
      } else {
        pill.className = 'feasibility-pill feas-easy';
        pill.innerText = '✅ VERY COMFORTABLE TARGET';
        advice.innerHTML = `You are in a great position! You only need an average SGPA of <strong>${reqSgpa.toFixed(2)}</strong> to easily reach your target graduation CGPA.`;
      }
    }

    window.addEventListener('DOMContentLoaded', estimateTarget);
  </script>
</body>
</html>"""

with open("tools/aktu-cgpa-target-estimator.html", "w", encoding="utf-8") as f:
    f.write(estimator_html)
print("Built tools/aktu-cgpa-target-estimator.html successfully!")

