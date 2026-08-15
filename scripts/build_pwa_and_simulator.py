import os

# 1. BUILD PWA INSTALL WIDGET SCRIPT: js/pwa-install-widget.js
pwa_script = """// AKTU Results PWA Smart Install Prompt Widget
(function() {
  let deferredPrompt;
  
  // Create styles
  const style = document.createElement('style');
  style.textContent = `
    .pwa-install-banner {
      position: fixed;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%) translateY(120px);
      width: calc(100% - 30px);
      max-width: 480px;
      background: #0f172a;
      color: white;
      border: 1.5px solid #334155;
      border-radius: 16px;
      padding: 16px 20px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.5), 0 0 20px rgba(37,99,235,0.2);
      z-index: 999999;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      font-family: 'Inter', system-ui, sans-serif;
    }
    .pwa-install-banner.show {
      transform: translateX(-50%) translateY(0);
    }
    .pwa-icon-box {
      width: 46px;
      height: 46px;
      border-radius: 12px;
      background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      flex-shrink: 0;
      box-shadow: 0 4px 10px rgba(37,99,235,0.4);
    }
    .pwa-info {
      flex: 1;
    }
    .pwa-title {
      font-size: 14px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 2px;
    }
    .pwa-desc {
      font-size: 11px;
      color: #94a3b8;
      line-height: 1.3;
    }
    .pwa-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .pwa-btn-install {
      background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
      color: white;
      border: none;
      padding: 9px 16px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      white-space: nowrap;
      box-shadow: 0 4px 10px rgba(37,99,235,0.3);
    }
    .pwa-btn-close {
      background: transparent;
      color: #64748b;
      border: none;
      font-size: 18px;
      cursor: pointer;
      padding: 4px;
      line-height: 1;
    }
    .pwa-btn-close:hover {
      color: #cbd5e1;
    }
  `;
  document.head.appendChild(style);

  // Register service worker if supported
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/service-worker.js').catch(err => console.log('SW reg error:', err));
    });
  }

  // Create Banner Element
  const banner = document.createElement('div');
  banner.className = 'pwa-install-banner';
  banner.innerHTML = `
    <div class="pwa-icon-box">🎓</div>
    <div class="pwa-info">
      <div class="pwa-title">Install AKTU Portal App</div>
      <div class="pwa-desc">Fast 1-click results & offline calculators on your home screen</div>
    </div>
    <div class="pwa-actions">
      <button class="pwa-btn-install" id="pwa-install-btn">Install</button>
      <button class="pwa-btn-close" id="pwa-close-btn">&times;</button>
    </div>
  `;
  document.body.appendChild(banner);

  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    if (!localStorage.getItem('pwa_banner_dismissed')) {
      setTimeout(() => {
        banner.classList.add('show');
      }, 3000);
    }
  });

  document.getElementById('pwa-install-btn').addEventListener('click', async () => {
    if (deferredPrompt) {
      deferredPrompt.prompt();
      const { outcome } = await deferredPrompt.userChoice;
      if (outcome === 'accepted') {
        banner.classList.remove('show');
      }
      deferredPrompt = null;
    } else {
      alert('To install, tap the Share/Menu icon in your browser and select "Add to Home Screen"');
    }
  });

  document.getElementById('pwa-close-btn').addEventListener('click', () => {
    banner.classList.remove('show');
    localStorage.setItem('pwa_banner_dismissed', 'true');
  });
})();
"""

os.makedirs("js", exist_ok=True)
with open("js/pwa-install-widget.js", "w", encoding="utf-8") as f:
    f.write(pwa_script)
print("Built js/pwa-install-widget.js!")


# 2. BUILD TOOL: AKTU 70-Marks Exam Copy Score Simulator & Back Risk Predictor
tool_sim_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU Copy Checker & 70-Marks Exam Score Simulator (Back Risk Calculator)</title>
  <meta name="description" content="Simulate your AKTU external theory score out of 70. Enter pages written, diagrams drawn, Section A/B/C attempt rate, and evaluate back paper risk and expected letter grade.">
  <link rel="canonical" href="https://akturesults.in/tools/aktu-exam-copy-score-simulator.html">
  <meta property="og:title" content="AKTU 70-Marks Exam Copy Score Simulator & Back Risk Checker">
  <meta property="og:description" content="Calculate your expected AKTU theory exam marks out of 70 based on page count, diagrams, question attempts, and examiner marking patterns.">
  <meta property="og:url" content="https://akturesults.in/tools/aktu-exam-copy-score-simulator.html">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://akturesults.in/images/og-banner.png">
  <meta name="twitter:card" content="summary_large_image">

  <!-- Monetization Ad Tags -->
  
  
  
  
  

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "AKTU 70-Marks Exam Copy Score Simulator",
    "url": "https://akturesults.in/tools/aktu-exam-copy-score-simulator.html",
    "description": "Simulates AKTU external theory paper scores based on examiner step marking rules.",
    "applicationCategory": "EducationalApplication",
    "operatingSystem": "All"
  }
  </script>

  <style>
    :root {
      --primary: #1e1b4b;
      --accent: #4f46e5;
      --success: #059669;
      --warning: #d97706;
      --danger: #dc2626;
      --text: #1e293b;
      --muted: #64748b;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', system-ui, -apple-system, sans-serif; }
    body { background: #f8fafc; color: var(--text); line-height: 1.6; }
    .container { max-width: 1050px; margin: 0 auto; padding: 20px; }

    /* Header */
    header { background: #0f172a; color: white; padding: 18px 0; border-bottom: 3px solid var(--accent); }
    .header-content { display: flex; justify-content: space-between; align-items: center; max-width: 1050px; margin: 0 auto; padding: 0 20px; }
    .logo { font-size: 20px; font-weight: 800; color: white; text-decoration: none; display: flex; align-items: center; gap: 8px; }
    .back-btn { color: #94a3b8; text-decoration: none; font-size: 14px; font-weight: 600; padding: 6px 14px; background: rgba(255,255,255,0.08); border-radius: 8px; }
    .back-btn:hover { color: white; background: rgba(255,255,255,0.15); }

    /* Hero */
    .hero { text-align: center; padding: 35px 20px 25px; }
    .hero h1 { font-size: 28px; font-weight: 800; color: #0f172a; margin-bottom: 10px; }
    .hero p { color: var(--muted); font-size: 16px; max-width: 750px; margin: 0 auto; }

    /* Grid */
    .grid-2 { display: grid; grid-template-columns: 1.1fr 1fr; gap: 25px; margin: 20px 0 40px; }
    .card { background: white; border-radius: 16px; padding: 25px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; }
    .card-title { font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 18px; display: flex; align-items: center; gap: 10px; border-bottom: 2px solid #f1f5f9; padding-bottom: 10px; }

    .form-group { margin-bottom: 15px; }
    .form-label { display: block; font-size: 13px; font-weight: 700; color: #334155; margin-bottom: 6px; }
    .form-input, .form-select { width: 100%; padding: 10px 12px; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 14px; color: #0f172a; background: white; }
    .form-input:focus, .form-select:focus { border-color: var(--accent); outline: none; }

    .range-wrap { display: flex; align-items: center; gap: 15px; }
    .range-slider { flex: 1; accent-color: var(--accent); height: 6px; }
    .range-val { font-weight: 800; color: var(--accent); font-size: 16px; min-width: 45px; }

    .sim-btn { width: 100%; padding: 14px; background: linear-gradient(135deg, #1e1b4b 0%, #4f46e5 100%); color: white; border: none; border-radius: 12px; font-size: 16px; font-weight: 700; cursor: pointer; transition: all 0.2s; box-shadow: 0 4px 12px rgba(79,70,229,0.25); margin-top: 10px; }
    .sim-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(79,70,229,0.35); }

    /* Result Engine */
    .score-display { text-align: center; padding: 25px; border-radius: 14px; background: #f8fafc; border: 1.5px solid #e2e8f0; margin-bottom: 20px; }
    .big-score { font-size: 48px; font-weight: 900; color: #1e1b4b; line-height: 1; margin: 10px 0; }
    .score-status { display: inline-block; padding: 6px 16px; border-radius: 20px; font-size: 13px; font-weight: 800; text-transform: uppercase; }
    .status-safe { background: #dcfce7; color: #15803d; }
    .status-border { background: #fef3c7; color: #b45309; }
    .status-danger { background: #fee2e2; color: #b91c1c; }

    .breakdown-row { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px dashed #e2e8f0; font-size: 14px; }
    .breakdown-row:last-child { border-bottom: none; }
    .breakdown-label { color: #475569; }
    .breakdown-val { font-weight: 700; color: #0f172a; }

    .advice-box { background: #eff6ff; border-left: 4px solid var(--accent); padding: 14px; border-radius: 0 8px 8px 0; font-size: 13px; color: #1e40af; margin-top: 15px; }

    /* Content */
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

  <!-- Header -->
  <header>
    <div class="header-content">
      <a href="/" class="logo">🎓 AKTU Results</a>
      <a href="/calculators.html" class="back-btn">← All Tools</a>
    </div>
  </header>

  <div class="container">
    <div class="hero">
      <h1>📝 AKTU 70-Marks Exam Copy Score Simulator</h1>
      <p>Estimate your external theory score out of 70 based on total pages written, diagrams drawn, section attempt completeness, and AKTU step-marking rubrics.</p>
    </div>

    <div class="grid-2">
      <!-- Input Card -->
      <div class="card">
        <div class="card-title">🔍 Enter Your Exam Attempt Details</div>
        
        <div class="form-group">
          <label class="form-label">Total Answer Booklet Pages Written (Out of 32)</label>
          <div class="range-wrap">
            <input type="range" id="in-pages" class="range-slider" min="5" max="32" value="24" oninput="updateVal('in-pages', 'val-pages')">
            <span id="val-pages" class="range-val">24</span>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">Section A (2-Mark Short Questions Attempted)</label>
          <select id="in-sec-a" class="form-select">
            <option value="10">All 10 Questions Attempted (20 Marks)</option>
            <option value="8" selected>8-9 Questions Attempted (~16-18 Marks)</option>
            <option value="6">6-7 Questions Attempted (~12-14 Marks)</option>
            <option value="4">4-5 Questions Attempted (~8-10 Marks)</option>
            <option value="2">Less than 4 Questions (< 8 Marks)</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label">Section B & C (7-Mark Long Questions Attempted)</label>
          <select id="in-sec-bc" class="form-select">
            <option value="5" selected>All 5 Long Questions Attempted (35 Marks pool)</option>
            <option value="4">4 Long Questions Attempted (28 Marks pool)</option>
            <option value="3">3 Long Questions Attempted (21 Marks pool)</option>
            <option value="2">2 Long Questions Attempted (14 Marks pool)</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label">Block Diagrams, Flowcharts & Circuit Sketches Drawn</label>
          <div class="range-wrap">
            <input type="range" id="in-diagrams" class="range-slider" min="0" max="15" value="5" oninput="updateVal('in-diagrams', 'val-diagrams')">
            <span id="val-diagrams" class="range-val">5</span>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">Content Depth & Keyword Accuracy</label>
          <select id="in-quality" class="form-select">
            <option value="high" selected>High (Clear headings, bullet points, correct definitions)</option>
            <option value="medium">Medium (Moderate explanation, some technical terms)</option>
            <option value="low">Low (Story writing / generic filler text)</option>
          </select>
        </div>

        <button class="sim-btn" onclick="simulateScore()">
          🚀 Calculate Predicted Score & Back Risk
        </button>
      </div>

      <!-- Result Card -->
      <div class="card">
        <div class="card-title">📊 Simulated Examiner Score Card</div>
        
        <div class="score-display">
          <div style="font-size: 12px; font-weight: 700; color: #64748b; text-transform: uppercase;">Predicted External Theory Score</div>
          <div id="sim-score" class="big-score">51 / 70</div>
          <div id="sim-status" class="score-status status-safe">🛡️ SAFE ZONE (GRADE A+)</div>
        </div>

        <div style="margin: 15px 0;">
          <div class="breakdown-row">
            <span class="breakdown-label">Section A (2-Mark Pool):</span>
            <span id="b-sec-a" class="breakdown-val">15.0 / 20</span>
          </div>
          <div class="breakdown-row">
            <span class="breakdown-label">Section B & C Long Answers:</span>
            <span id="b-sec-bc" class="breakdown-val">26.5 / 35</span>
          </div>
          <div class="breakdown-row">
            <span class="breakdown-label">Diagram & Flowchart Bonus:</span>
            <span id="b-diag" class="breakdown-val">+6.5 Marks</span>
          </div>
          <div class="breakdown-row">
            <span class="breakdown-label">Page Volume Weighting:</span>
            <span id="b-page" class="breakdown-val">+3.0 Marks</span>
          </div>
          <div class="breakdown-row">
            <span class="breakdown-label">Mandatory 30% Theory Cutoff (21/70):</span>
            <span id="b-cutoff" class="breakdown-val" style="color: #059669;">PASSED (Cutoff: 21)</span>
          </div>
        </div>

        <div id="sim-advice" class="advice-box">
          <strong>Examiner Assessment:</strong> High chance of securing Grade A / A+. Your diagram density and page count comfortably exceed the safe evaluation threshold.
        </div>
      </div>
    </div>

    <!-- Content Card -->
    <div class="content-card">
      <h2>How AKTU University Exam Copies Are Evaluated</h2>
      <p>Under AKTU valuation center guidelines, external theory answer booklets (typically 32 pages) are graded according to step-marking criteria. Examiners are assigned bundles of 30 to 40 answer sheets per day. The key factors that directly determine your final score out of 70 include:</p>

      <ul>
        <li><strong>Mandatory 30% Theory Passing Cutoff (21 Marks out of 70):</strong> Regardless of how high your internal sessional marks are (e.g. 28/30), you MUST score at least <strong>21 marks out of 70</strong> in the external theory exam to clear the subject.</li>
        <li><strong>Diagram & Visual Presentation:</strong> In engineering subjects (COA, DBMS, Mechanics, Electronics, Heat Transfer), examiners scan for neat block diagrams, flowcharts, or algorithmic pseudo-code before reading text blocks. Clear diagrams typically add 1 to 2 bonus marks per long question.</li>
        <li><strong>Section A Precision:</strong> Section A contains 10 compulsory 2-mark questions. Writing crisp, 2-to-3 line definitions with relevant formula gives high scoring efficiency.</li>
      </ul>
    </div>
  </div>

  <script>
    function updateVal(sliderId, labelId) {
      document.getElementById(labelId).innerText = document.getElementById(sliderId).value;
    }

    function simulateScore() {
      const pages = parseInt(document.getElementById('in-pages').value) || 20;
      const secA = parseInt(document.getElementById('in-sec-a').value) || 8;
      const secBC = parseInt(document.getElementById('in-sec-bc').value) || 4;
      const diag = parseInt(document.getElementById('in-diagrams').value) || 3;
      const quality = document.getElementById('in-quality').value;

      // Calculate Section A
      let scoreA = (secA * 1.7);
      if (quality === 'low') scoreA *= 0.6;
      else if (quality === 'medium') scoreA *= 0.85;

      // Calculate Section BC
      let maxBC = secBC * 7;
      let qFactor = quality === 'high' ? 0.78 : (quality === 'medium' ? 0.60 : 0.40);
      let scoreBC = maxBC * qFactor;

      // Diagram bonus
      let scoreDiag = Math.min(8, diag * 1.2);

      // Page bonus
      let scorePage = 0;
      if (pages >= 25) scorePage = 3.5;
      else if (pages >= 18) scorePage = 2.0;
      else if (pages >= 12) scorePage = 1.0;

      let total = Math.min(70, Math.round(scoreA + scoreBC + scoreDiag + scorePage));

      // Update UI
      document.getElementById('sim-score').innerText = `${total} / 70`;
      document.getElementById('b-sec-a').innerText = `${scoreA.toFixed(1)} / 20`;
      document.getElementById('b-sec-bc').innerText = `${scoreBC.toFixed(1)} / 35`;
      document.getElementById('b-diag').innerText = `+${scoreDiag.toFixed(1)} Marks`;
      document.getElementById('b-page').innerText = `+${scorePage.toFixed(1)} Marks`;

      const status = document.getElementById('sim-status');
      const cutoff = document.getElementById('b-cutoff');
      const advice = document.getElementById('sim-advice');

      if (total >= 21) {
        cutoff.innerText = 'PASSED (Cutoff: 21)';
        cutoff.style.color = '#059669';
      } else {
        cutoff.innerText = 'BELOW CUTOFF (Back Risk)';
        cutoff.style.color = '#dc2626';
      }

      if (total >= 50) {
        status.className = 'score-status status-safe';
        status.innerText = '🛡️ SAFE ZONE (GRADE A+)';
        advice.innerHTML = '<strong>Examiner Assessment:</strong> High chance of securing Grade A / A+. Your diagram density and page count comfortably exceed the safe evaluation threshold.';
      } else if (total >= 32) {
        status.className = 'score-status status-safe';
        status.innerText = '✅ CLEAN PASS (GRADE B / B+)';
        advice.innerHTML = '<strong>Examiner Assessment:</strong> You are safely above the passing cutoff. Internal marks will push your overall grade to B+ or A.';
      } else if (total >= 21) {
        status.className = 'score-status status-border';
        status.innerText = '⚠️ BORDERLINE PASS (GRADE C / P)';
        advice.innerHTML = '<strong>Examiner Assessment:</strong> Borderline clear! If external marks fall below 21, you might need 3-5 marks PWG Grace or Challenge Evaluation Stage 1 copy review.';
      } else {
        status.className = 'score-status status-danger';
        status.innerText = '❌ HIGH BACK RISK (GRADE F)';
        advice.innerHTML = '<strong>Examiner Assessment:</strong> Predicted score is below 21 marks cutoff. Recommended to prepare for Carryover (COP) exam or apply for Challenge Evaluation if you attempted more pages.';
      }
    }

    window.addEventListener('DOMContentLoaded', simulateScore);
  </script>
</body>
</html>"""

with open("tools/aktu-exam-copy-score-simulator.html", "w", encoding="utf-8") as f:
    f.write(tool_sim_html)
print("Built tools/aktu-exam-copy-score-simulator.html!")

