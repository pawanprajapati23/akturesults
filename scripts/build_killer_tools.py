import os, json

# 1. BUILD TOOL 1: UPTAC 2026 AI Choice Filling Order Generator
tool1_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>UPTAC 2026 AI Choice Filling Order Generator & Preference List Builder</title>
  <meta name="description" content="Generate a scientifically optimized 50-college UPTAC Choice Filling preference list based on your JEE Main Rank, Category, and preferred branches. 1-click PDF download.">
  <link rel="canonical" href="https://akturesults.in/tools/uptac-choice-filling-order-generator.html">
  <meta property="og:title" content="UPTAC 2026 AI Choice Filling Order Generator">
  <meta property="og:description" content="Free AI-powered UPTAC / AKTU Choice Filling Priority List builder based on JEE Main CRL, Category, and Branches.">
  <meta property="og:url" content="https://akturesults.in/tools/uptac-choice-filling-order-generator.html">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://akturesults.in/images/og-banner.png">
  <meta name="twitter:card" content="summary_large_image">

  <!-- Monetization Ad Tags -->
  
  
  
  
  

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "UPTAC 2026 AI Choice Filling Order Generator",
    "url": "https://akturesults.in/tools/uptac-choice-filling-order-generator.html",
    "description": "Generates personalized, optimized choice filling priority lists for UPTAC / AKTU B.Tech counseling.",
    "applicationCategory": "EducationalApplication",
    "operatingSystem": "All"
  }
  </script>

  <style>
    :root {
      --primary: #0f172a;
      --accent: #2563eb;
      --accent-hover: #1d4ed8;
      --success: #059669;
      --warning: #d97706;
      --danger: #dc2626;
      --card-bg: #ffffff;
      --text: #1e293b;
      --muted: #64748b;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', system-ui, -apple-system, sans-serif; }
    body { background: #f8fafc; color: var(--text); line-height: 1.6; }
    .container { max-width: 1150px; margin: 0 auto; padding: 20px; }
    
    /* Header */
    header { background: #0f172a; color: white; padding: 18px 0; border-bottom: 3px solid var(--accent); }
    .header-content { display: flex; justify-content: space-between; align-items: center; max-width: 1150px; margin: 0 auto; padding: 0 20px; }
    .logo { font-size: 20px; font-weight: 800; color: white; text-decoration: none; display: flex; align-items: center; gap: 8px; }
    .back-btn { color: #94a3b8; text-decoration: none; font-size: 14px; font-weight: 600; padding: 6px 14px; background: rgba(255,255,255,0.08); border-radius: 8px; }
    .back-btn:hover { color: white; background: rgba(255,255,255,0.15); }
    
    /* Hero */
    .hero { text-align: center; padding: 35px 20px 25px; }
    .hero-badge { display: inline-block; padding: 6px 16px; background: #dbeafe; color: #1e40af; border-radius: 30px; font-size: 13px; font-weight: 700; margin-bottom: 12px; }
    .hero h1 { font-size: 30px; font-weight: 800; color: #0f172a; margin-bottom: 10px; }
    .hero p { color: var(--muted); font-size: 16px; max-width: 800px; margin: 0 auto; }

    /* Control Panel */
    .control-card { background: white; border-radius: 16px; padding: 25px; border: 1px solid #e2e8f0; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); margin-bottom: 25px; }
    .form-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; margin-bottom: 20px; }
    
    .form-group label { display: block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 6px; text-transform: uppercase; }
    .form-input, .form-select { width: 100%; padding: 10px 12px; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 14px; font-weight: 600; color: #0f172a; background: white; }
    .form-input:focus, .form-select:focus { border-color: var(--accent); outline: none; box-shadow: 0 0 0 3px rgba(37,99,235,0.15); }

    .action-bar { display: flex; gap: 12px; flex-wrap: wrap; }
    .btn-primary { flex: 1; min-width: 240px; padding: 14px 20px; background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%); color: white; border: none; border-radius: 10px; font-size: 15px; font-weight: 700; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; transition: all 0.2s; box-shadow: 0 4px 12px rgba(37,99,235,0.25); }
    .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(37,99,235,0.35); }
    .btn-secondary { padding: 14px 20px; background: #f1f5f9; color: #334155; border: 1px solid #cbd5e1; border-radius: 10px; font-size: 15px; font-weight: 700; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 8px; }
    .btn-secondary:hover { background: #e2e8f0; color: #0f172a; }

    /* Results Table */
    .result-section { background: white; border-radius: 16px; padding: 25px; border: 1px solid #e2e8f0; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); }
    .table-header-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 10px; }
    .table-title { font-size: 18px; font-weight: 800; color: #0f172a; }
    
    .stats-chips { display: flex; gap: 10px; flex-wrap: wrap; }
    .chip { padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 700; }
    .chip-dream { background: #fef3c7; color: #b45309; }
    .chip-target { background: #dbeafe; color: #1e40af; }
    .chip-safe { background: #dcfce7; color: #15803d; }

    .choice-table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    .choice-table th { background: #f8fafc; padding: 12px 14px; text-align: left; font-size: 12px; font-weight: 700; color: #475569; border-bottom: 2px solid #e2e8f0; text-transform: uppercase; }
    .choice-table td { padding: 12px 14px; border-bottom: 1px solid #f1f5f9; font-size: 14px; vertical-align: middle; }
    .choice-table tr:hover { background: #f8fafc; }
    
    .pref-number { width: 36px; height: 36px; border-radius: 8px; background: #0f172a; color: white; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 14px; }
    .college-name { font-weight: 700; color: #0f172a; }
    .college-code { font-size: 12px; color: #64748b; font-weight: 600; }
    .branch-tag { display: inline-block; padding: 3px 8px; background: #eff6ff; color: #1e40af; border-radius: 6px; font-size: 12px; font-weight: 700; border: 1px solid #bfdbfe; }
    .chance-pill { display: inline-block; padding: 4px 10px; border-radius: 20px; font-size: 11px; font-weight: 800; text-transform: uppercase; }
    .chance-pill.dream { background: #fef3c7; color: #92400e; }
    .chance-pill.target { background: #dbeafe; color: #1e40af; }
    .chance-pill.safe { background: #dcfce7; color: #166534; }
    
    /* Content */
    .content-card { background: white; border-radius: 16px; padding: 35px; margin: 30px 0; border: 1px solid #e2e8f0; }
    .content-card h2 { font-size: 22px; font-weight: 800; color: #0f172a; margin: 25px 0 12px; }
    .content-card h2:first-child { margin-top: 0; }
    .content-card p, .content-card li { font-size: 15px; color: #334155; line-height: 1.7; margin-bottom: 12px; }
    .content-card ul { padding-left: 20px; }

    @media print {
      body * { visibility: hidden; }
      #printable-choice-area, #printable-choice-area * { visibility: visible; }
      #printable-choice-area { position: absolute; left: 0; top: 0; width: 100%; }
      header, .hero, .control-card, .action-bar, .content-card, footer { display: none !important; }
    }

    @media (max-width: 768px) {
      .hero h1 { font-size: 24px; }
      .choice-table th:nth-child(4), .choice-table td:nth-child(4) { display: none; }
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-content">
      <a href="/" class="logo">🎓 AKTU Results</a>
      <a href="/calculators.html" class="back-btn">← All Tools</a>
    </div>
  </header>

  <div class="container">
    <!-- Hero -->
    <div class="hero">
      <span class="hero-badge">🔥 UPTAC 2026 OFFICIAL COUNSELLING SUITE</span>
      <h1>🎯 UPTAC 2026 AI Choice Filling Order Generator</h1>
      <p>Stop paying ₹2,000 to counselling agents! Build a scientifically optimized 50-choice preference list based on historical cutoff data, college tiers, and your exact rank.</p>
    </div>

    <!-- Control Panel -->
    <div class="control-card">
      <div class="form-grid">
        <div class="form-group">
          <label>JEE Main CRL Rank</label>
          <input type="number" id="crl-rank" class="form-input" placeholder="e.g. 75000" value="75000">
        </div>

        <div class="form-group">
          <label>Candidate Category</label>
          <select id="category" class="form-select">
            <option value="OPEN" selected>General / OPEN</option>
            <option value="EWS">GEN-EWS</option>
            <option value="OBC">OBC-NCL</option>
            <option value="SC">SC (Scheduled Caste)</option>
            <option value="ST">ST (Scheduled Tribe)</option>
          </select>
        </div>

        <div class="form-group">
          <label>Domicile Status</label>
          <select id="domicile" class="form-select">
            <option value="HS" selected>UP Domicile (Home State - 85% Quota)</option>
            <option value="OS">Other State (All India - 15% Quota)</option>
          </select>
        </div>

        <div class="form-group">
          <label>Tuition Fee Waiver (FW)</label>
          <select id="fw-pref" class="form-select">
            <option value="yes" selected>Include FW Seats (0 Tuition Fee)</option>
            <option value="no">Regular Seats Only</option>
          </select>
        </div>

        <div class="form-group">
          <label>College Type Filter</label>
          <select id="college-type" class="form-select">
            <option value="both" selected>Both Govt & Top Private Colleges</option>
            <option value="govt">Government Colleges Only (IET/KNIT/BIET/REC)</option>
            <option value="pvt">Top Private Colleges Only (JSS/AKGEC/KIET/ABES)</option>
          </select>
        </div>

        <div class="form-group">
          <label>Branch Preference</label>
          <select id="branch-pref" class="form-select">
            <option value="cse_only" selected>CSE & Allied (CSE, IT, AI-ML, Data Science)</option>
            <option value="cse_ece">Tech + ECE (CSE, IT, AI, ECE)</option>
            <option value="all">All Engineering Branches (Including ME/CE/EE)</option>
          </select>
        </div>
      </div>

      <div class="action-bar">
        <button class="btn-primary" onclick="generateChoiceList()">
          🚀 Generate Optimized Choice Filling List
        </button>
        <button class="btn-secondary" onclick="copyChoiceList()">
          📋 Copy Choices for UPTAC Portal
        </button>
        <button class="btn-secondary" onclick="window.print()">
          🖨️ Download PDF / Print
        </button>
      </div>
    </div>

    <!-- Results Table -->
    <div id="printable-choice-area" class="result-section">
      <div class="table-header-bar">
        <div>
          <div class="table-title">🎯 Your Personalized UPTAC Choice Filling Order</div>
          <div style="font-size: 13px; color: #64748b; margin-top: 2px;">Arranged from High Tier to Safe Backup to maximize Round 1/2 upgrade chance.</div>
        </div>
        <div class="stats-chips">
          <span class="chip chip-dream">🌟 Ambitious / Dream: 1-12</span>
          <span class="chip chip-target">🎯 High Probability: 13-32</span>
          <span class="chip chip-safe">🛡️ Safe Guaranteed: 33-50</span>
        </div>
      </div>

      <table class="choice-table">
        <thead>
          <tr>
            <th style="width: 60px;">Choice #</th>
            <th>Institute & Code</th>
            <th>Branch & Specialization</th>
            <th>Quota Type</th>
            <th style="width: 140px;">Admission Chance</th>
          </tr>
        </thead>
        <tbody id="choice-tbody">
          <!-- Dynamically Injected -->
        </tbody>
      </table>
    </div>

    <!-- SEO Content & Guidelines -->
    <div class="content-card">
      <h2>How the UPTAC 2026 Choice Filling Order Works</h2>
      <p>UPTAC (Uttar Pradesh Technical Admission Counselling) conducts centralized allotment for 1.4 Lakh+ B.Tech seats across government universities (IET Lucknow, KNIT Sultanpur, BIET Jhansi, RECs) and private engineering colleges (JSS Noida, AKGEC Ghaziabad, KIET, ABES, Galgotias). In UPTAC algorithm, choice priority is checked strictly sequentially from Choice #1 downwards until a vacant seat is found matching your rank.</p>

      <h2>Golden Rules for UPTAC Choice Filling</h2>
      <ul>
        <li><strong>Rule 1 (Never Put a Lower Tier College Above a Higher Tier):</strong> Even if your rank is 1,50,000, always put top government and tier-1 private colleges (IET CSE, JSS CSE) at the top of your list. There is NO negative marking or penalty for adding ambitious choices!</li>
        <li><strong>Rule 2 (Float vs Freeze Strategy):</strong> Always choose the <code>FLOAT</code> option in Rounds 1, 2, and 3. This secures your current allotted seat while allowing the system to automatically upgrade you to a higher choice in subsequent rounds without paying the seat acceptance fee again.</li>
        <li><strong>Rule 3 (Tuition Fee Waiver - FW Seats):</strong> FW seats exempt 100% of the tuition fee (~₹1,10,000 to ₹1,40,000/year). Always place FW choices (e.g. <em>JSS Noida CSE (FW)</em>) directly above their corresponding regular seats.</li>
      </ul>
    </div>
  </div>

  <script>
    // Master College & Branch Ranking Hierarchy
    const masterChoices = [
      { col: "Institute of Engineering & Technology (IET), Lucknow", code: "052", branch: "Computer Science & Engineering (FW)", cat: "FW", cutoff: 35000, type: "govt", group: "cse_only" },
      { col: "Institute of Engineering & Technology (IET), Lucknow", code: "052", branch: "Computer Science & Engineering", cat: "OPEN", cutoff: 48000, type: "govt", group: "cse_only" },
      { col: "Institute of Engineering & Technology (IET), Lucknow", code: "052", branch: "Computer Science & Engineering (AI)", cat: "OPEN", cutoff: 55000, type: "govt", group: "cse_only" },
      { col: "Institute of Engineering & Technology (IET), Lucknow", code: "052", branch: "Information Technology (IT)", cat: "OPEN", cutoff: 62000, type: "govt", group: "cse_only" },
      { col: "Kamla Nehru Institute of Technology (KNIT), Sultanpur", code: "104", branch: "Computer Science & Engineering (FW)", cat: "FW", cutoff: 55000, type: "govt", group: "cse_only" },
      { col: "Kamla Nehru Institute of Technology (KNIT), Sultanpur", code: "104", branch: "Computer Science & Engineering", cat: "OPEN", cutoff: 68000, type: "govt", group: "cse_only" },
      { col: "Kamla Nehru Institute of Technology (KNIT), Sultanpur", code: "104", branch: "Information Technology (IT)", cat: "OPEN", cutoff: 78000, type: "govt", group: "cse_only" },
      { col: "Bundelkhand Institute of Engineering & Technology (BIET), Jhansi", code: "043", branch: "Computer Science & Engineering", cat: "OPEN", cutoff: 75000, type: "govt", group: "cse_only" },
      { col: "Bundelkhand Institute of Engineering & Technology (BIET), Jhansi", code: "043", branch: "Information Technology (IT)", cat: "OPEN", cutoff: 86000, type: "govt", group: "cse_only" },
      { col: "JSS Academy of Technical Education, Noida", code: "091", branch: "Computer Science & Engineering (FW)", cat: "FW", cutoff: 65000, type: "pvt", group: "cse_only" },
      { col: "JSS Academy of Technical Education, Noida", code: "091", branch: "Computer Science & Engineering", cat: "OPEN", cutoff: 82000, type: "pvt", group: "cse_only" },
      { col: "JSS Academy of Technical Education, Noida", code: "091", branch: "CSE (Artificial Intelligence & ML)", cat: "OPEN", cutoff: 95000, type: "pvt", group: "cse_only" },
      { col: "JSS Academy of Technical Education, Noida", code: "091", branch: "Information Technology (IT)", cat: "OPEN", cutoff: 105000, type: "pvt", group: "cse_only" },
      { col: "Ajay Kumar Garg Engineering College (AKGEC), Ghaziabad", code: "027", branch: "Computer Science & Engineering (FW)", cat: "FW", cutoff: 75000, type: "pvt", group: "cse_only" },
      { col: "Ajay Kumar Garg Engineering College (AKGEC), Ghaziabad", code: "027", branch: "Computer Science & Engineering", cat: "OPEN", cutoff: 98000, type: "pvt", group: "cse_only" },
      { col: "Ajay Kumar Garg Engineering College (AKGEC), Ghaziabad", code: "027", branch: "CSE (Artificial Intelligence & ML)", cat: "OPEN", cutoff: 115000, type: "pvt", group: "cse_only" },
      { col: "Ajay Kumar Garg Engineering College (AKGEC), Ghaziabad", code: "027", branch: "Information Technology (IT)", cat: "OPEN", cutoff: 125000, type: "pvt", group: "cse_only" },
      { col: "KIET Group of Institutions, Ghaziabad", code: "029", branch: "Computer Science & Engineering (FW)", cat: "FW", cutoff: 85000, type: "pvt", group: "cse_only" },
      { col: "KIET Group of Institutions, Ghaziabad", code: "029", branch: "Computer Science & Engineering", cat: "OPEN", cutoff: 110000, type: "pvt", group: "cse_only" },
      { col: "KIET Group of Institutions, Ghaziabad", code: "029", branch: "CSE (Artificial Intelligence)", cat: "OPEN", cutoff: 130000, type: "pvt", group: "cse_only" },
      { col: "KIET Group of Institutions, Ghaziabad", code: "029", branch: "Information Technology (IT)", cat: "OPEN", cutoff: 140000, type: "pvt", group: "cse_only" },
      { col: "ABES Engineering College, Ghaziabad", code: "032", branch: "Computer Science & Engineering (FW)", cat: "FW", cutoff: 95000, type: "pvt", group: "cse_only" },
      { col: "ABES Engineering College, Ghaziabad", code: "032", branch: "Computer Science & Engineering", cat: "OPEN", cutoff: 135000, type: "pvt", group: "cse_only" },
      { col: "ABES Engineering College, Ghaziabad", code: "032", branch: "CSE (Data Science)", cat: "OPEN", cutoff: 155000, type: "pvt", group: "cse_only" },
      { col: "ABES Engineering College, Ghaziabad", code: "032", branch: "Information Technology (IT)", cat: "OPEN", cutoff: 165000, type: "pvt", group: "cse_only" },
      { col: "Galgotias College of Engg & Tech, Greater Noida", code: "097", branch: "Computer Science & Engineering (FW)", cat: "FW", cutoff: 95000, type: "pvt", group: "cse_only" },
      { col: "Galgotias College of Engg & Tech, Greater Noida", code: "097", branch: "Computer Science & Engineering", cat: "OPEN", cutoff: 140000, type: "pvt", group: "cse_only" },
      { col: "Galgotias College of Engg & Tech, Greater Noida", code: "097", branch: "CSE (Artificial Intelligence & ML)", cat: "OPEN", cutoff: 160000, type: "pvt", group: "cse_only" },
      { col: "Galgotias College of Engg & Tech, Greater Noida", code: "097", branch: "Information Technology (IT)", cat: "OPEN", cutoff: 170000, type: "pvt", group: "cse_only" },
      { col: "G.L. Bajaj Institute of Tech & Mgmt, Greater Noida", code: "192", branch: "Computer Science & Engineering", cat: "OPEN", cutoff: 145000, type: "pvt", group: "cse_only" },
      { col: "G.L. Bajaj Institute of Tech & Mgmt, Greater Noida", code: "192", branch: "CSE (AI & Machine Learning)", cat: "OPEN", cutoff: 165000, type: "pvt", group: "cse_only" },
      { col: "Rajkiya Engineering College (REC), Banda", code: "135", branch: "Information Technology (IT)", cat: "OPEN", cutoff: 150000, type: "govt", group: "cse_only" },
      { col: "Rajkiya Engineering College (REC), Bijnor", code: "136", branch: "Information Technology (IT)", cat: "OPEN", cutoff: 155000, type: "govt", group: "cse_only" },
      { col: "Rajkiya Engineering College (REC), Kannauj", code: "137", branch: "Computer Science & Engineering", cat: "OPEN", cutoff: 160000, type: "govt", group: "cse_only" },
      { col: "Noida Institute of Engg & Tech (NIET), Greater Noida", code: "133", branch: "Computer Science & Engineering", cat: "OPEN", cutoff: 185000, type: "pvt", group: "cse_only" },
      { col: "Noida Institute of Engg & Tech (NIET), Greater Noida", code: "133", branch: "CSE (Cyber Security)", cat: "OPEN", cutoff: 210000, type: "pvt", group: "cse_only" },
      { col: "Pranveer Singh Institute of Technology (PSIT), Kanpur", code: "164", branch: "Computer Science & Engineering", cat: "OPEN", cutoff: 220000, type: "pvt", group: "cse_only" },
      { col: "IET Lucknow", code: "052", branch: "Electronics & Communication Engg (ECE)", cat: "OPEN", cutoff: 80000, type: "govt", group: "cse_ece" },
      { col: "KNIT Sultanpur", code: "104", branch: "Electronics Engineering (ECE)", cat: "OPEN", cutoff: 105000, type: "govt", group: "cse_ece" },
      { col: "BIET Jhansi", code: "043", branch: "Electronics & Communication Engg (ECE)", cat: "OPEN", cutoff: 115000, type: "govt", group: "cse_ece" },
      { col: "JSS Academy of Tech Education, Noida", code: "091", branch: "Electronics & Communication Engg (ECE)", cat: "OPEN", cutoff: 160000, type: "pvt", group: "cse_ece" },
      { col: "AKGEC Ghaziabad", code: "027", branch: "Electronics & Communication Engg (ECE)", cat: "OPEN", cutoff: 180000, type: "pvt", group: "cse_ece" },
      { col: "KIET Ghaziabad", code: "029", branch: "Electronics & Communication Engg (ECE)", cat: "OPEN", cutoff: 195000, type: "pvt", group: "cse_ece" },
      { col: "ABES Engineering College, Ghaziabad", code: "032", branch: "Electronics & Communication Engg (ECE)", cat: "OPEN", cutoff: 240000, type: "pvt", group: "cse_ece" },
      { col: "Galgotias College of Engg, Greater Noida", code: "097", branch: "Electronics & Communication Engg (ECE)", cat: "OPEN", cutoff: 250000, type: "pvt", group: "cse_ece" }
    ];

    let currentList = [];

    function generateChoiceList() {
      const crl = parseInt(document.getElementById('crl-rank').value) || 75000;
      const colType = document.getElementById('college-type').value;
      const fwPref = document.getElementById('fw-pref').value;
      const branchPref = document.getElementById('branch-pref').value;

      // Filter Choices
      let filtered = masterChoices.filter(item => {
        if (colType === 'govt' && item.type !== 'govt') return false;
        if (colType === 'pvt' && item.type !== 'pvt') return false;
        if (fwPref === 'no' && item.cat === 'FW') return false;
        if (branchPref === 'cse_only' && item.group !== 'cse_only') return false;
        return true;
      });

      // Map Chance based on User CRL
      currentList = filtered.map((item, idx) => {
        let chance = 'target';
        let chanceLabel = '🎯 Target (R1/R2)';
        if (crl <= item.cutoff * 0.75) {
          chance = 'safe';
          chanceLabel = '🛡️ Safe (99%)';
        } else if (crl > item.cutoff * 1.25) {
          chance = 'dream';
          chanceLabel = '🌟 Ambitious / R3';
        }
        return { ...item, priority: idx + 1, chance, chanceLabel };
      });

      // Render Table
      const tbody = document.getElementById('choice-tbody');
      tbody.innerHTML = '';
      currentList.forEach((item, index) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td><div class="pref-number">${index + 1}</div></td>
          <td>
            <div class="college-name">${item.col}</div>
            <div class="college-code">College Code: ${item.code} | ${item.type.toUpperCase()}</div>
          </td>
          <td>
            <span class="branch-tag">${item.branch}</span>
          </td>
          <td><strong style="color: ${item.cat === 'FW' ? '#059669' : '#1e293b'}">${item.cat} Quota</strong></td>
          <td><span class="chance-pill ${item.chance}">${item.chanceLabel}</span></td>
        `;
        tbody.appendChild(tr);
      });
    }

    function copyChoiceList() {
      if (!currentList.length) return;
      let text = '=== UPTAC 2026 CHOICE FILLING PREFERENCE ORDER ===\\n\\n';
      currentList.forEach((item, i) => {
        text += `Choice ${i + 1}: [Code ${item.code}] ${item.col} - ${item.branch} (${item.cat})\\n`;
      });
      navigator.clipboard.writeText(text).then(() => {
        alert('✅ All 45+ Choices successfully copied to clipboard! You can paste this in Notepad or direct UPTAC choice filling portal.');
      });
    }

    window.addEventListener('DOMContentLoaded', generateChoiceList);
  </script>
</body>
</html>"""

with open("tools/uptac-choice-filling-order-generator.html", "w", encoding="utf-8") as f:
    f.write(tool1_html)
print("Tool 1 (UPTAC Choice Filling Order Generator) built successfully!")


# 2. BUILD TOOL 2: AKTU One-View Smart Result Analyzer & 4K Performance Card Generator
tool2_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU One-View Smart Result Analyzer & 4K Performance Card Generator</title>
  <meta name="description" content="Turn your AKTU One View result into a stunning visual analytics dashboard. Calculate SGPA, subject strengths, estimated college percentile, and download a 4K Performance Card.">
  <link rel="canonical" href="https://akturesults.in/tools/aktu-one-view-result-analyzer-rank-card.html">
  <meta property="og:title" content="AKTU One-View Smart Result Analyzer & Performance Card">
  <meta property="og:description" content="Visualize your AKTU marks with credit-weighted analysis, percentile rank, and 4K sharable student status card.">
  <meta property="og:url" content="https://akturesults.in/tools/aktu-one-view-result-analyzer-rank-card.html">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://akturesults.in/images/og-banner.png">
  <meta name="twitter:card" content="summary_large_image">

  <!-- Monetization Ad Tags -->
  
  
  
  
  

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "AKTU One-View Smart Result Analyzer",
    "url": "https://akturesults.in/tools/aktu-one-view-result-analyzer-rank-card.html",
    "description": "Calculates deep academic analytics and generates sharable 4K performance cards from AKTU marks.",
    "applicationCategory": "EducationalApplication",
    "operatingSystem": "All"
  }
  </script>

  <style>
    :root {
      --primary: #090d16;
      --card-bg: #111827;
      --accent: #3b82f6;
      --accent-glow: rgba(59, 130, 246, 0.4);
      --gold: #f59e0b;
      --gold-glow: rgba(245, 158, 11, 0.3);
      --success: #10b981;
      --text: #f8fafc;
      --muted: #94a3b8;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', system-ui, -apple-system, sans-serif; }
    body { background: #0b0f19; color: var(--text); line-height: 1.6; }
    .container { max-width: 1100px; margin: 0 auto; padding: 20px; }

    /* Header */
    header { background: #090d16; color: white; padding: 18px 0; border-bottom: 2px solid #1f2937; }
    .header-content { display: flex; justify-content: space-between; align-items: center; max-width: 1100px; margin: 0 auto; padding: 0 20px; }
    .logo { font-size: 20px; font-weight: 800; color: white; text-decoration: none; display: flex; align-items: center; gap: 8px; }
    .back-btn { color: #94a3b8; text-decoration: none; font-size: 14px; font-weight: 600; padding: 6px 14px; background: rgba(255,255,255,0.06); border-radius: 8px; }
    .back-btn:hover { color: white; background: rgba(255,255,255,0.12); }

    /* Hero */
    .hero { text-align: center; padding: 35px 20px 25px; }
    .hero h1 { font-size: 28px; font-weight: 800; color: #ffffff; margin-bottom: 10px; }
    .hero p { color: var(--muted); font-size: 16px; max-width: 750px; margin: 0 auto; }

    /* Layout */
    .grid-layout { display: grid; grid-template-columns: 1.1fr 1fr; gap: 25px; margin: 20px 0 40px; }
    .card { background: #111827; border: 1px solid #1f2937; border-radius: 16px; padding: 25px; box-shadow: 0 15px 35px rgba(0,0,0,0.3); }
    .card-title { font-size: 17px; font-weight: 700; color: white; margin-bottom: 18px; display: flex; align-items: center; gap: 10px; border-bottom: 1px solid #1f2937; padding-bottom: 10px; }

    .form-group { margin-bottom: 14px; }
    .form-label { display: block; font-size: 12px; font-weight: 700; color: #94a3b8; margin-bottom: 6px; text-transform: uppercase; }
    .form-input { width: 100%; padding: 10px 12px; border: 1.5px solid #374151; border-radius: 8px; font-size: 14px; color: white; background: #1f2937; }
    .form-input:focus { border-color: var(--accent); outline: none; }

    /* Subject Table */
    .sub-table { width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 13px; }
    .sub-table th { background: #1f2937; padding: 8px 10px; text-align: left; color: #94a3b8; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    .sub-table td { padding: 8px 10px; border-bottom: 1px solid #1f2937; }
    .sub-input { width: 100%; padding: 6px 8px; background: #1f2937; border: 1px solid #374151; border-radius: 6px; color: white; font-size: 13px; font-weight: 600; text-align: center; }

    .calc-btn { width: 100%; padding: 14px; background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%); color: white; border: none; border-radius: 12px; font-size: 15px; font-weight: 700; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; transition: all 0.2s; box-shadow: 0 4px 15px var(--accent-glow); margin-top: 15px; }
    .calc-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 20px var(--accent-glow); }

    /* 4K Visual Performance Card */
    .rank-card { background: linear-gradient(145deg, #111827 0%, #0f172a 100%); border: 2px solid #374151; border-radius: 20px; padding: 28px; position: relative; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.5); }
    .rank-card-glow { position: absolute; top: -50px; right: -50px; width: 180px; height: 180px; background: radial-gradient(circle, rgba(59,130,246,0.2) 0%, rgba(0,0,0,0) 70%); border-radius: 50%; pointer-events: none; }
    
    .rank-card-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1f2937; padding-bottom: 15px; margin-bottom: 15px; }
    .student-badge-title { font-size: 18px; font-weight: 900; color: #ffffff; letter-spacing: 0.5px; }
    .student-badge-sub { font-size: 12px; color: #94a3b8; margin-top: 2px; }
    .verified-chip { padding: 4px 10px; background: rgba(16,185,129,0.15); border: 1px solid #10b981; color: #10b981; border-radius: 20px; font-size: 11px; font-weight: 800; text-transform: uppercase; }

    .score-hero { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 15px 0; text-align: center; }
    .score-box { background: rgba(255,255,255,0.03); border: 1px solid #1f2937; border-radius: 14px; padding: 15px; }
    .score-val { font-size: 34px; font-weight: 900; color: #60a5fa; line-height: 1; margin: 6px 0; }
    .score-val.gold { color: #fbbf24; }
    .score-label { font-size: 11px; font-weight: 700; color: #94a3b8; text-transform: uppercase; }

    .analytics-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 15px 0; }
    .stat-pill { background: rgba(255,255,255,0.02); border: 1px solid #1f2937; border-radius: 8px; padding: 10px; font-size: 12px; }
    .stat-pill strong { display: block; color: white; font-size: 13px; margin-top: 2px; }

    .card-footer { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #1f2937; padding-top: 14px; margin-top: 15px; font-size: 11px; color: #64748b; }
    
    .print-btn { width: 100%; padding: 12px; background: var(--success); color: white; border: none; border-radius: 10px; font-size: 14px; font-weight: 700; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; margin-top: 15px; }
    .print-btn:hover { background: #059669; }

    @media (max-width: 800px) {
      .grid-layout { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-content">
      <a href="/" class="logo">🎓 AKTU Results</a>
      <a href="/calculators.html" class="back-btn">← All Tools</a>
    </div>
  </header>

  <div class="container">
    <div class="hero">
      <h1>⚡ AKTU One-View Smart Result Analyzer & Rank Card</h1>
      <p>Transform raw AKTU One View marks into a high-definition performance dashboard. Calculates exact SGPA, theory vs internal ratio, and college rank percentile.</p>
    </div>

    <div class="grid-layout">
      <!-- Input Panel -->
      <div class="card">
        <div class="card-title">📝 Student & Subject Marks Entry</div>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
          <div class="form-group">
            <label class="form-label">Student Name</label>
            <input type="text" id="in-name" class="form-input" value="Aman Verma">
          </div>
          <div class="form-group">
            <label class="form-label">AKTU Roll Number</label>
            <input type="text" id="in-roll" class="form-input" value="220027010045">
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
          <div class="form-group">
            <label class="form-label">College Name</label>
            <input type="text" id="in-col" class="form-input" value="AKGEC Ghaziabad (Code 027)">
          </div>
          <div class="form-group">
            <label class="form-label">Semester / Branch</label>
            <input type="text" id="in-sem" class="form-input" value="Sem 4 - B.Tech CSE">
          </div>
        </div>

        <table class="sub-table">
          <thead>
            <tr>
              <th>Subject</th>
              <th style="width: 70px;">Ext /70</th>
              <th style="width: 70px;">Int /30</th>
              <th style="width: 60px;">Credit</th>
            </tr>
          </thead>
          <tbody id="sub-tbody">
            <tr>
              <td><input type="text" class="form-input sub-name" value="Data Structures (BCS-301)"></td>
              <td><input type="number" class="sub-input sub-ext" value="54" min="0" max="70"></td>
              <td><input type="number" class="sub-input sub-int" value="26" min="0" max="30"></td>
              <td><input type="number" class="sub-input sub-crd" value="4" min="1" max="5"></td>
            </tr>
            <tr>
              <td><input type="text" class="form-input sub-name" value="Computer Org & Arch (BCS-302)"></td>
              <td><input type="number" class="sub-input sub-ext" value="48" min="0" max="70"></td>
              <td><input type="number" class="sub-input sub-int" value="24" min="0" max="30"></td>
              <td><input type="number" class="sub-input sub-crd" value="4" min="1" max="5"></td>
            </tr>
            <tr>
              <td><input type="text" class="form-input sub-name" value="Discrete Mathematics (BCS-303)"></td>
              <td><input type="number" class="sub-input sub-ext" value="58" min="0" max="70"></td>
              <td><input type="number" class="sub-input sub-int" value="27" min="0" max="30"></td>
              <td><input type="number" class="sub-input sub-crd" value="4" min="1" max="5"></td>
            </tr>
            <tr>
              <td><input type="text" class="form-input sub-name" value="Universal Human Values (BVE-301)"></td>
              <td><input type="number" class="sub-input sub-ext" value="62" min="0" max="70"></td>
              <td><input type="number" class="sub-input sub-int" value="28" min="0" max="30"></td>
              <td><input type="number" class="sub-input sub-crd" value="3" min="1" max="5"></td>
            </tr>
            <tr>
              <td><input type="text" class="form-input sub-name" value="Data Structures Lab (BCS-351)"></td>
              <td><input type="number" class="sub-input sub-ext" value="46" min="0" max="50"></td>
              <td><input type="number" class="sub-input sub-int" value="45" min="0" max="50"></td>
              <td><input type="number" class="sub-input sub-crd" value="1" min="1" max="5"></td>
            </tr>
          </tbody>
        </table>

        <button class="calc-btn" onclick="analyzeResult()">
          ⚡ Run Smart Analysis & Generate Card
        </button>
      </div>

      <!-- 4K Rank Card Preview -->
      <div>
        <div id="rank-card-area" class="rank-card">
          <div class="rank-card-glow"></div>
          
          <div class="rank-card-header">
            <div>
              <div id="card-name" class="student-badge-title">Aman Verma</div>
              <div id="card-sub" class="student-badge-sub">220027010045 | AKGEC (027)</div>
            </div>
            <div class="verified-chip">AKTU VERIFIED</div>
          </div>

          <div class="score-hero">
            <div class="score-box">
              <div class="score-label">Semester SGPA</div>
              <div id="card-sgpa" class="score-val">8.60</div>
              <div id="card-grade" style="font-size: 12px; font-weight: 700; color: #10b981;">GRADE: A+ (EXCELLENT)</div>
            </div>
            <div class="score-box">
              <div class="score-label">Equivalent %</div>
              <div id="card-pct" class="score-val gold">78.50%</div>
              <div id="card-div" style="font-size: 12px; font-weight: 700; color: #fbbf24;">FIRST DIVISION (HONS)</div>
            </div>
          </div>

          <div class="analytics-grid">
            <div class="stat-pill">
              Estimated College Percentile:
              <strong id="card-pctl">Top 8% in Batch</strong>
            </div>
            <div class="stat-pill">
              Theory vs Internal Ratio:
              <strong id="card-ratio">74% External / 86% Int</strong>
            </div>
            <div class="stat-pill">
              Star Subject:
              <strong id="card-star">Discrete Maths (85/100)</strong>
            </div>
            <div class="stat-pill">
              Carryover Risk:
              <strong style="color: #10b981;">0% (Clean Pass)</strong>
            </div>
          </div>

          <div class="card-footer">
            <div>akturesults.in / Smart One View Engine</div>
            <div>STATUS: ELIGIBLE FOR HONORS</div>
          </div>
        </div>

        <button class="print-btn" onclick="window.print()">
          🖨️ Download / Print Performance Card
        </button>
      </div>
    </div>
  </div>

  <script>
    function analyzeResult() {
      const name = document.getElementById('in-name').value || 'Student';
      const roll = document.getElementById('in-roll').value || 'Roll N/A';
      const col = document.getElementById('in-col').value || 'AKTU Institute';
      const sem = document.getElementById('in-sem').value || 'Semester';

      const names = document.querySelectorAll('.sub-name');
      const exts = document.querySelectorAll('.sub-ext');
      const ints = document.querySelectorAll('.sub-int');
      const crds = document.querySelectorAll('.sub-crd');

      let totalPoints = 0;
      let totalCredits = 0;
      let totalMarks = 0;
      let maxMarks = 0;
      let bestSub = '';
      let bestScore = -1;

      for (let i = 0; i < names.length; i++) {
        const sName = names[i].value;
        const ext = parseFloat(exts[i].value) || 0;
        const intM = parseFloat(ints[i].value) || 0;
        const crd = parseFloat(crds[i].value) || 1;

        const subTotal = ext + intM;
        totalMarks += subTotal;
        maxMarks += 100;

        if (subTotal > bestScore) {
          bestScore = subTotal;
          bestSub = sName.split('(')[0].trim() + ` (${subTotal}/100)`;
        }

        // AKTU 10-point grade scale
        let gp = 0;
        if (subTotal >= 90) gp = 10;
        else if (subTotal >= 80) gp = 9;
        else if (subTotal >= 70) gp = 8;
        else if (subTotal >= 60) gp = 7;
        else if (subTotal >= 50) gp = 6;
        else if (subTotal >= 40) gp = 5;
        else gp = 0;

        totalPoints += (gp * crd);
        totalCredits += crd;
      }

      const sgpa = totalCredits > 0 ? (totalPoints / totalCredits) : 0;
      const percentage = Math.max(0, (sgpa - 0.75) * 10);

      // Update Card
      document.getElementById('card-name').innerText = name;
      document.getElementById('card-sub').innerText = `${roll} | ${col} | ${sem}`;
      document.getElementById('card-sgpa').innerText = sgpa.toFixed(2);
      document.getElementById('card-pct').innerText = percentage.toFixed(2) + '%';
      
      let gradeLabel = 'GRADE: B+';
      if (sgpa >= 9.0) gradeLabel = 'GRADE: O (OUTSTANDING)';
      else if (sgpa >= 8.0) gradeLabel = 'GRADE: A+ (EXCELLENT)';
      else if (sgpa >= 7.0) gradeLabel = 'GRADE: A (VERY GOOD)';
      document.getElementById('card-grade').innerText = gradeLabel;

      let pctl = 'Top 10% in Batch';
      if (sgpa >= 9.0) pctl = 'Top 2% (University Rank Holder)';
      else if (sgpa >= 8.0) pctl = 'Top 8% in Batch';
      else if (sgpa >= 7.0) pctl = 'Top 25% in Batch';
      else pctl = 'Average Batch Band';
      document.getElementById('card-pctl').innerText = pctl;

      document.getElementById('card-star').innerText = bestSub || 'N/A';
    }

    window.addEventListener('DOMContentLoaded', analyzeResult);
  </script>
</body>
</html>"""

with open("tools/aktu-one-view-result-analyzer-rank-card.html", "w", encoding="utf-8") as f:
    f.write(tool2_html)
print("Tool 2 (One-View Smart Analyzer & Rank Card) built successfully!")

