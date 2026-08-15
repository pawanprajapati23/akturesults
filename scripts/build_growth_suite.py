import os, json

ad_tags = """  <!-- Monetag -->
  
  
  
  
  
  """

os.makedirs("tools", exist_ok=True)
os.makedirs("notes", exist_ok=True)

with open("scripts/flat_colleges.json", "r", encoding="utf-8") as f:
    colleges_list = json.load(f)

colleges_json_str = json.dumps(colleges_list)

compare_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU College Comparison Tool — Compare Fees, Cutoffs, Placements & Hostels Side-by-Side</title>
  <meta name="description" content="Compare any two AKTU affiliated engineering colleges side-by-side. Compare fee structures, highest and average placement packages, NAAC/NIRF rankings, hostel charges, and top recruiters for UPTAC counseling.">
  <meta name="keywords" content="AKTU college comparison, JSS vs AKGEC, KIET vs Galgotias, IET Lucknow vs KNIT Sultanpur, compare AKTU colleges, UPTAC choice filling comparison">
  <link rel="canonical" href="https://akturesults.in/tools/aktu-college-comparison-tool.html">
  <link rel="icon" href="/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
{ad_tags}
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "AKTU College Comparison Tool",
    "url": "https://akturesults.in/tools/aktu-college-comparison-tool.html",
    "applicationCategory": "EducationalApplication",
    "operatingSystem": "All",
    "description": "Side-by-side comparison engine for 355+ AKTU affiliated colleges across fees, placements, and ranking."
  }}
  </script>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', sans-serif; }}
    body {{ background: #f8fafc; color: #1e293b; line-height: 1.6; }}
    .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
    nav {{ background: #ffffff; border-bottom: 1px solid #e2e8f0; padding: 16px 0; position: sticky; top: 0; z-index: 100; }}
    .nav-inner {{ display: flex; justify-content: space-between; align-items: center; }}
    .logo {{ font-size: 22px; font-weight: 800; color: #4338ca; text-decoration: none; display: flex; align-items: center; gap: 8px; }}
    .hero {{ background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%); color: #ffffff; padding: 48px 0 36px; text-align: center; }}
    .hero h1 {{ font-size: 32px; font-weight: 900; margin-bottom: 10px; }}
    .hero p {{ font-size: 16px; opacity: 0.9; max-width: 700px; margin: 0 auto; }}
    .select-card {{ background: #ffffff; border-radius: 16px; border: 1px solid #e2e8f0; padding: 24px; margin: -25px auto 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.06); position: relative; z-index: 10; }}
    .select-grid {{ display: grid; grid-template-columns: 1fr auto 1fr; gap: 20px; align-items: center; }}
    .select-box label {{ display: block; font-size: 13px; font-weight: 800; color: #475569; margin-bottom: 8px; text-transform: uppercase; }}
    .select-control {{ width: 100%; padding: 12px 16px; border-radius: 10px; border: 1.5px solid #cbd5e1; font-size: 15px; font-weight: 700; color: #0f172a; outline: none; background: #f8fafc; transition: all 0.2s; }}
    .select-control:focus {{ border-color: #4338ca; background: #ffffff; box-shadow: 0 0 0 3px rgba(67,56,202,0.15); }}
    .vs-circle {{ width: 44px; height: 44px; border-radius: 50%; background: #4338ca; color: #ffffff; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 14px; box-shadow: 0 4px 12px rgba(67,56,202,0.3); margin: 0 auto; }}
    .compare-table {{ width: 100%; background: #ffffff; border-radius: 14px; border: 1px solid #e2e8f0; border-collapse: separate; border-spacing: 0; overflow: hidden; margin-bottom: 40px; box-shadow: 0 4px 15px rgba(0,0,0,0.03); }}
    .compare-table th, .compare-table td {{ padding: 16px 20px; border-bottom: 1px solid #e2e8f0; }}
    .compare-table th {{ background: #f1f5f9; font-weight: 800; font-size: 16px; width: 40%; }}
    .compare-table th:first-child {{ width: 20%; background: #f8fafc; font-size: 14px; color: #64748b; text-transform: uppercase; }}
    .compare-table td {{ font-size: 15px; font-weight: 600; }}
    .highlight-val {{ font-size: 18px; font-weight: 900; color: #4338ca; }}
    .better-val {{ color: #059669; font-weight: 800; }}
    .badge {{ display: inline-block; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: 800; }}
    .badge-govt {{ background: #dcfce7; color: #15803d; }}
    .badge-pvt {{ background: #e0e7ff; color: #3730a3; }}
    .tags {{ display: flex; flex-wrap: wrap; gap: 6px; }}
    .tag {{ background: #f1f5f9; padding: 3px 8px; border-radius: 4px; font-size: 12px; }}
    .quick-picks {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; padding-top: 14px; border-top: 1px solid #f1f5f9; }}
    .quick-btn {{ background: #f8fafc; border: 1px solid #e2e8f0; padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; cursor: pointer; transition: all 0.2s; }}
    .quick-btn:hover {{ background: #4338ca; color: #ffffff; border-color: #4338ca; }}
    .footer {{ background: #0f172a; color: #ffffff; text-align: center; padding: 40px 0; font-size: 14px; }}
    .footer a {{ color: #06b6d4; text-decoration: none; }}
    @media (max-width: 768px) {{
      .select-grid {{ grid-template-columns: 1fr; gap: 10px; }}
      .vs-circle {{ margin: 6px auto; }}
      .compare-table th:first-child {{ width: 30%; font-size: 12px; }}
      .compare-table th {{ font-size: 14px; }}
    }}
  </style>
</head>
<body>
  <nav>
    <div class="container nav-inner">
      <a href="/" class="logo">🏛️ AKTU Results</a>
      <div>
        <a href="/colleges/aktu-colleges-filter-directory.html" style="color:#4338ca; text-decoration:none; font-weight:700; font-size:14px; margin-right:15px;">🏛️ Directory (355+ Colleges)</a>
        <a href="/admissions/uptac-choice-filling-predictor-2026.html" style="color:#059669; text-decoration:none; font-weight:700; font-size:14px;">🎯 UPTAC Predictor</a>
      </div>
    </div>
  </nav>

  <div class="hero">
    <div class="container">
      <span style="background:rgba(255,255,255,0.15); padding:4px 14px; border-radius:20px; font-size:12px; font-weight:800; display:inline-block; margin-bottom:10px;">⚖️ Head-to-Head Comparison</span>
      <h1>AKTU College Comparison Engine</h1>
      <p>Compare any two colleges across Uttar Pradesh side-by-side to make the best choice during UPTAC counseling.</p>
    </div>
  </div>

  <div class="container">
    <div class="select-card">
      <div class="select-grid">
        <div class="select-box">
          <label>🏛️ Select College 1 (Left)</label>
          <select id="col1Select" class="select-control"></select>
        </div>
        <div class="vs-circle">VS</div>
        <div class="select-box">
          <label>🏛️ Select College 2 (Right)</label>
          <select id="col2Select" class="select-control"></select>
        </div>
      </div>
      <div class="quick-picks">
        <span style="font-size:12px; font-weight:700; color:#64748b; margin-right:6px;">⚡ Popular Battles:</span>
        <button class="quick-btn" onclick="setPair('091', '027')">JSS Noida vs AKGEC Ghaziabad</button>
        <button class="quick-btn" onclick="setPair('029', '097')">KIET Ghaziabad vs Galgotias Gr. Noida</button>
        <button class="quick-btn" onclick="setPair('052', '104')">IET Lucknow vs KNIT Sultanpur</button>
        <button class="quick-btn" onclick="setPair('032', '164')">ABES EC vs PSIT Kanpur</button>
        <button class="quick-btn" onclick="setPair('061', '720')">HBTU Kanpur vs MNNIT Prayagraj</button>
      </div>
    </div>

    <div id="comparisonArea">
      <!-- Comparison Table dynamically generated -->
    </div>
  </div>

  <footer class="footer">
    <div class="container">
      <p>© 2026 <a href="/">AKTU Results Portal</a> — Institutional Comparison Engine for AKTU / UPTAC</p>
    </div>
  </footer>

  <script>
    const colleges = {colleges_json_str};

    function initDropdowns() {{
      const col1 = document.getElementById('col1Select');
      const col2 = document.getElementById('col2Select');

      const sorted = [...colleges].sort((a,b) => a.name.localeCompare(b.name));

      const options = sorted.map(c => `<option value="${{c.code}}">${{c.name}} (${{c.city}}) [Code: ${{c.code}}]</option>`).join('');
      col1.innerHTML = options;
      col2.innerHTML = options;

      col1.addEventListener('change', renderComparison);
      col2.addEventListener('change', renderComparison);
      
      setPair('091', '027');
    }}

    function setPair(code1, code2) {{
      document.getElementById('col1Select').value = code1;
      document.getElementById('col2Select').value = code2;
      renderComparison();
    }}

    function renderComparison() {{
      const code1 = document.getElementById('col1Select').value;
      const code2 = document.getElementById('col2Select').value;

      const c1 = colleges.find(c => c.code === code1) || colleges[0];
      const c2 = colleges.find(c => c.code === code2) || colleges[1];

      const area = document.getElementById('comparisonArea');

      const c1_4yr = (c1.fee + (c1.fee * 0.32) + (c1.fee * 0.30) + (c1.fee * 0.06)) * 4;
      const c2_4yr = (c2.fee + (c2.fee * 0.32) + (c2.fee * 0.30) + (c2.fee * 0.06)) * 4;

      area.innerHTML = `
        <table class="compare-table">
          <thead>
            <tr>
              <th>Metric / Factor</th>
              <th style="color:#4338ca;">${{c1.name}}</th>
              <th style="color:#059669;">${{c2.name}}</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Institute Code & City</td>
              <td><span class="badge badge-pvt">Code ${{c1.code}}</span> 📍 ${{c1.city}}, UP</td>
              <td><span class="badge badge-govt">Code ${{c2.code}}</span> 📍 ${{c2.city}}, UP</td>
            </tr>
            <tr>
              <td>Type & Establishment</td>
              <td>${{c1.type}} (Est. ${{c1.est}})</td>
              <td>${{c2.type}} (Est. ${{c2.est}})</td>
            </tr>
            <tr>
              <td>NAAC & NIRF Ranking</td>
              <td>NAAC <strong>${{c1.naac}}</strong> • NIRF <strong>${{c1.nirf}}</strong></td>
              <td>NAAC <strong>${{c2.naac}}</strong> • NIRF <strong>${{c2.nirf}}</strong></td>
            </tr>
            <tr>
              <td>Annual Tuition Fee</td>
              <td><span class="highlight-val">₹${{(c1.fee / 1000).toFixed(0)}}k / year</span></td>
              <td><span class="highlight-val">₹${{(c2.fee / 1000).toFixed(0)}}k / year</span></td>
            </tr>
            <tr>
              <td>Est. 4-Year Total Outlay</td>
              <td><strong>₹${{(c1_4yr / 100000).toFixed(2)}} Lakh</strong> (incl. hostel & mess)</td>
              <td><strong>₹${{(c2_4yr / 100000).toFixed(2)}} Lakh</strong> (incl. hostel & mess)</td>
            </tr>
            <tr>
              <td>Highest Salary Package</td>
              <td><span class="better-val" style="font-size:18px;">${{c1.h_pkg}} LPA</span></td>
              <td><span class="better-val" style="font-size:18px;">${{c2.h_pkg}} LPA</span></td>
            </tr>
            <tr>
              <td>Avg Branch / CSE Salary</td>
              <td><strong>${{c1.avg_pkg}} LPA</strong></td>
              <td><strong>${{c2.avg_pkg}} LPA</strong></td>
            </tr>
            <tr>
              <td>Placement Percentage</td>
              <td><strong>${{c1.pct}}%</strong> Campus Placement</td>
              <td><strong>${{c2.pct}}%</strong> Campus Placement</td>
            </tr>
            <tr>
              <td>Key Academic Branches</td>
              <td><div class="tags">${{c1.branches.map(b => `<span class="tag">${{b}}</span>`).join('')}}</div></td>
              <td><div class="tags">${{c2.branches.map(b => `<span class="tag">${{b}}</span>`).join('')}}</div></td>
            </tr>
            <tr>
              <td>Top Campus Recruiters</td>
              <td><div class="tags">${{c1.rec.map(r => `<span class="tag">${{r}}</span>`).join('')}}</div></td>
              <td><div class="tags">${{c2.rec.map(r => `<span class="tag">${{r}}</span>`).join('')}}</div></td>
            </tr>
            <tr>
              <td>Action / Detailed Profile</td>
              <td><a href="/colleges/profiles/${{c1.slug}}.html" style="color:#4338ca; font-weight:800; text-decoration:none;">View Full ${{c1.code}} Profile →</a></td>
              <td><a href="/colleges/profiles/${{c2.slug}}.html" style="color:#059669; font-weight:800; text-decoration:none;">View Full ${{c2.code}} Profile →</a></td>
            </tr>
          </tbody>
        </table>
      `;
    }}

    document.addEventListener('DOMContentLoaded', initDropdowns);
  </script>
  <script defer src="/js/community-banner-widget.js"></script>
</body>
</html>"""

with open("tools/aktu-college-comparison-tool.html", "w", encoding="utf-8") as f:
    f.write(compare_html)
print("Created tools/aktu-college-comparison-tool.html")

# 2. Attendance & Bunk Master Calculator
attendance_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU 75% Attendance & Bunk Calculator — Calculate Safe Bunks & Shortage</title>
  <meta name="description" content="Calculate AKTU 75% mandatory attendance and safe bunk limit. Check how many classes you can bunk or how many lectures you must attend to avoid detention and get your semester admit card.">
  <meta name="keywords" content="AKTU attendance calculator, AKTU 75 percent rule, AKTU bunk calculator, AKTU attendance shortage, AKTU admit card detention">
  <link rel="canonical" href="https://akturesults.in/tools/aktu-attendance-bunk-calculator.html">
  <link rel="icon" href="/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
{ad_tags}
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "AKTU 75% Attendance & Bunk Calculator",
    "url": "https://akturesults.in/tools/aktu-attendance-bunk-calculator.html",
    "applicationCategory": "EducationalApplication",
    "operatingSystem": "All",
    "description": "Interactive attendance calculator and safe bunk predictor for AKTU college students."
  }}
  </script>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', sans-serif; }}
    body {{ background: #f8fafc; color: #1e293b; line-height: 1.6; }}
    .container {{ max-width: 960px; margin: 0 auto; padding: 0 20px; }}
    nav {{ background: #ffffff; border-bottom: 1px solid #e2e8f0; padding: 16px 0; position: sticky; top: 0; z-index: 100; }}
    .nav-inner {{ display: flex; justify-content: space-between; align-items: center; }}
    .logo {{ font-size: 22px; font-weight: 800; color: #4338ca; text-decoration: none; }}
    .hero {{ background: linear-gradient(135deg, #1e1b4b, #312e81, #4338ca); color: #ffffff; padding: 45px 0 35px; text-align: center; }}
    .hero h1 {{ font-size: 30px; font-weight: 900; margin-bottom: 8px; }}
    .hero p {{ font-size: 15px; opacity: 0.9; max-width: 650px; margin: 0 auto; }}
    .calc-card {{ background: #ffffff; border-radius: 16px; border: 1px solid #e2e8f0; padding: 30px; margin: -20px auto 35px; box-shadow: 0 10px 30px rgba(0,0,0,0.06); }}
    .input-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 24px; }}
    .input-group label {{ display: block; font-size: 13px; font-weight: 700; color: #475569; margin-bottom: 6px; }}
    .input-ctrl {{ width: 100%; padding: 12px 14px; border-radius: 10px; border: 1.5px solid #cbd5e1; font-size: 15px; font-weight: 700; color: #0f172a; outline: none; background: #f8fafc; transition: all 0.2s; }}
    .input-ctrl:focus {{ border-color: #4338ca; background: #ffffff; box-shadow: 0 0 0 3px rgba(67,56,202,0.15); }}
    .btn-calc {{ width: 100%; background: #4338ca; color: #ffffff; border: none; padding: 14px; border-radius: 10px; font-size: 16px; font-weight: 800; cursor: pointer; transition: background 0.2s; }}
    .btn-calc:hover {{ background: #3730a3; }}
    .result-box {{ margin-top: 24px; padding: 20px; border-radius: 12px; display: none; text-align: center; }}
    .result-safe {{ background: #dcfce7; border: 1px solid #86efac; color: #166534; }}
    .result-warning {{ background: #fee2e2; border: 1px solid #fca5a5; color: #991b1b; }}
    .res-num {{ font-size: 36px; font-weight: 900; margin: 8px 0; }}
    .guide-card {{ background: #ffffff; border-radius: 14px; border: 1px solid #e2e8f0; padding: 26px; margin-bottom: 30px; }}
    .guide-card h2 {{ font-size: 20px; font-weight: 800; color: #0f172a; margin-bottom: 12px; }}
    .footer {{ background: #0f172a; color: #ffffff; text-align: center; padding: 35px 0; font-size: 14px; }}
    .footer a {{ color: #06b6d4; text-decoration: none; }}
  </style>
</head>
<body>
  <nav>
    <div class="container nav-inner">
      <a href="/" class="logo">AKTU Results</a>
      <div>
        <a href="/calculators.html" style="color:#4338ca; text-decoration:none; font-weight:700; font-size:14px; margin-right:15px;">🧮 All Calculators</a>
        <a href="/tools/aktu-college-comparison-tool.html" style="color:#059669; text-decoration:none; font-weight:700; font-size:14px;">⚖️ Compare Colleges</a>
      </div>
    </div>
  </nav>

  <div class="hero">
    <div class="container">
      <span style="background:rgba(255,255,255,0.15); padding:4px 14px; border-radius:20px; font-size:12px; font-weight:800; display:inline-block; margin-bottom:10px;">📋 Official 75% Rule Engine</span>
      <h1>AKTU Attendance & Bunk Calculator</h1>
      <p>Instant calculator to check your exact attendance percentage, how many classes you can safely bunk, or how many lectures you need to avoid detention.</p>
    </div>
  </div>

  <div class="container">
    <div class="calc-card">
      <div class="input-grid">
        <div class="input-group">
          <label>📚 Total Lectures Held</label>
          <input type="number" id="totalClasses" class="input-ctrl" placeholder="e.g. 60" min="1" value="50">
        </div>
        <div class="input-group">
          <label>✅ Lectures Attended</label>
          <input type="number" id="attendedClasses" class="input-ctrl" placeholder="e.g. 42" min="0" value="40">
        </div>
        <div class="input-group">
          <label>🎯 Target Threshold (%)</label>
          <select id="targetPct" class="input-ctrl">
            <option value="75" selected>75% (AKTU Mandatory Normal)</option>
            <option value="60">60% (Medical / Sports Relaxation)</option>
            <option value="80">80% (Safe Buffer Target)</option>
          </select>
        </div>
      </div>
      <button class="btn-calc" onclick="calcAttendance()">⚡ Calculate Attendance & Bunk Limit</button>

      <div id="resultBox" class="result-box">
        <div id="resTitle" style="font-size:14px; font-weight:800; text-transform:uppercase;"></div>
        <div id="resPct" class="res-num"></div>
        <p id="resMsg" style="font-size:15px; font-weight:700;"></p>
      </div>
    </div>

    <div class="guide-card">
      <h2>📜 Official AKTU Attendance Regulations & Medical Concession</h2>
      <ul style="margin-left: 20px; line-height: 1.8; color: #475569; font-size: 15px;">
        <li><strong>75% Mandatory Attendance:</strong> Under AKTU Ordinance clause 3.1, every student is required to attend a minimum of 75% of total classes held in each subject.</li>
        <li><strong>Medical / Special Concession (Up to 15%):</strong> The Director/Principal of the affiliated institution may grant relaxation up to 15% (minimum 60% attendance) on valid medical grounds, hospital certificates, or university-level athletic/cultural representation.</li>
        <li><strong>Admit Card Detention:</strong> Students with attendance below 75% (or 60% with medical proof) will have their ERP admit cards blocked and will receive an <strong>'I' (Incomplete/Detained)</strong> grade in the semester examination.</li>
      </ul>
    </div>
  </div>

  <footer class="footer">
    <div class="container">
      <p>© 2026 <a href="/">AKTU Results Portal</a> — Student Attendance & Academic Tools</p>
    </div>
  </footer>

  <script>
    function calcAttendance() {{
      const total = parseInt(document.getElementById('totalClasses').value);
      const attended = parseInt(document.getElementById('attendedClasses').value);
      const target = parseFloat(document.getElementById('targetPct').value);

      if (isNaN(total) || isNaN(attended) || total <= 0 || attended < 0 || attended > total) {{
        alert("Please enter valid numbers where attended classes do not exceed total lectures held.");
        return;
      }}

      const currentPct = ((attended / total) * 100).toFixed(1);
      const resBox = document.getElementById('resultBox');
      const resTitle = document.getElementById('resTitle');
      const resPct = document.getElementById('resPct');
      const resMsg = document.getElementById('resMsg');

      resBox.style.display = 'block';
      resPct.textContent = `${{currentPct}}%`;

      if (currentPct >= target) {{
        const maxBunk = Math.floor((attended * 100 / target) - total);
        resBox.className = 'result-box result-safe';
        resTitle.textContent = '🎉 You are in the Safe Zone!';
        if (maxBunk > 0) {{
          resMsg.textContent = `You can safely bunk ${{maxBunk}} more consecutive lecture${{maxBunk === 1 ? '' : 's'}} and still remain above ${{target}}%!`;
        }} else {{
          resMsg.textContent = `You are right on the edge of ${{target}}%. Do not bunk any more lectures!`;
        }}
      }} else {{
        const needed = Math.ceil(((target * total) - (100 * attended)) / (100 - target));
        resBox.className = 'result-box result-warning';
        resTitle.textContent = '⚠️ Attendance Shortage Warning!';
        resMsg.textContent = `You need to attend next ${{needed}} consecutive lecture${{needed === 1 ? '' : 's'}} without missing any to reach ${{target}}% attendance!`;
      }}
    }}

    document.addEventListener('DOMContentLoaded', calcAttendance);
  </script>
  <script defer src="/js/community-banner-widget.js"></script>
</body>
</html>"""

with open("tools/aktu-attendance-bunk-calculator.html", "w", encoding="utf-8") as f:
    f.write(attendance_html)
print("Created tools/aktu-attendance-bunk-calculator.html")

# 3. Sessional & End-Sem Target Marks Planner
planner_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU Internal Sessional & End-Sem Target Marks Planner — Calculate Honors & Target CGPA</title>
  <meta name="description" content="Calculate your AKTU internal sessional score (CT-1, CT-2, Teacher Assessment) and calculate required marks in end-semester theory exams to achieve Grade O, A+, A (Honors), or Passing Grade.">
  <meta name="keywords" content="AKTU internal marks calculator, AKTU sessional calculator, AKTU target marks planner, AKTU honors degree marks, AKTU grade calculation formula">
  <link rel="canonical" href="https://akturesults.in/tools/aktu-sessional-endsem-target-planner.html">
  <link rel="icon" href="/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
{ad_tags}
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "AKTU Internal Sessional & End-Sem Target Planner",
    "url": "https://akturesults.in/tools/aktu-sessional-endsem-target-planner.html",
    "applicationCategory": "EducationalApplication",
    "operatingSystem": "All",
    "description": "Internal sessional mark evaluator and end-semester target marks calculator for AKTU engineering students."
  }}
  </script>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', sans-serif; }}
    body {{ background: #f8fafc; color: #1e293b; line-height: 1.6; }}
    .container {{ max-width: 1000px; margin: 0 auto; padding: 0 20px; }}
    nav {{ background: #ffffff; border-bottom: 1px solid #e2e8f0; padding: 16px 0; position: sticky; top: 0; z-index: 100; }}
    .nav-inner {{ display: flex; justify-content: space-between; align-items: center; }}
    .logo {{ font-size: 22px; font-weight: 800; color: #4338ca; text-decoration: none; }}
    .hero {{ background: linear-gradient(135deg, #1e1b4b, #312e81, #4338ca); color: #ffffff; padding: 45px 0 35px; text-align: center; }}
    .hero h1 {{ font-size: 30px; font-weight: 900; margin-bottom: 8px; }}
    .hero p {{ font-size: 15px; opacity: 0.9; max-width: 650px; margin: 0 auto; }}
    .calc-card {{ background: #ffffff; border-radius: 16px; border: 1px solid #e2e8f0; padding: 30px; margin: -20px auto 35px; box-shadow: 0 10px 30px rgba(0,0,0,0.06); }}
    .input-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 24px; }}
    .input-group label {{ display: block; font-size: 12px; font-weight: 700; color: #475569; margin-bottom: 6px; text-transform: uppercase; }}
    .input-ctrl {{ width: 100%; padding: 12px 14px; border-radius: 10px; border: 1.5px solid #cbd5e1; font-size: 15px; font-weight: 700; color: #0f172a; outline: none; background: #f8fafc; transition: all 0.2s; }}
    .input-ctrl:focus {{ border-color: #4338ca; background: #ffffff; box-shadow: 0 0 0 3px rgba(67,56,202,0.15); }}
    .table-target {{ width: 100%; border-collapse: collapse; margin-top: 24px; font-size: 14px; }}
    .table-target th, .table-target td {{ padding: 12px 16px; border: 1px solid #e2e8f0; text-align: left; }}
    .table-target th {{ background: #f1f5f9; font-weight: 800; color: #334155; }}
    .badge-grade {{ font-weight: 900; padding: 4px 10px; border-radius: 6px; display: inline-block; }}
    .footer {{ background: #0f172a; color: #ffffff; text-align: center; padding: 35px 0; font-size: 14px; }}
    .footer a {{ color: #06b6d4; text-decoration: none; }}
  </style>
</head>
<body>
  <nav>
    <div class="container nav-inner">
      <a href="/" class="logo">AKTU Results</a>
      <div>
        <a href="/calculators.html" style="color:#4338ca; text-decoration:none; font-weight:700; font-size:14px; margin-right:15px;">🧮 All Calculators</a>
        <a href="/tools/aktu-attendance-bunk-calculator.html" style="color:#059669; text-decoration:none; font-weight:700; font-size:14px;">📋 Attendance Tool</a>
      </div>
    </div>
  </nav>

  <div class="hero">
    <div class="container">
      <span style="background:rgba(255,255,255,0.15); padding:4px 14px; border-radius:20px; font-size:12px; font-weight:800; display:inline-block; margin-bottom:10px;">🎯 Target Grade Planner</span>
      <h1>AKTU Sessional & End-Sem Target Marks Calculator</h1>
      <p>Enter your internal marks (Class Tests & Teacher Assessment) to find exact marks needed in the 70-mark End Semester University exam.</p>
    </div>
  </div>

  <div class="container">
    <div class="calc-card">
      <div class="input-grid">
        <div class="input-group">
          <label>📝 Class Test 1 (CT-1) [Max: 30]</label>
          <input type="number" id="ct1" class="input-ctrl" min="0" max="30" value="24">
        </div>
        <div class="input-group">
          <label>📝 Class Test 2 (CT-2) [Max: 30]</label>
          <input type="number" id="ct2" class="input-ctrl" min="0" max="30" value="26">
        </div>
        <div class="input-group">
          <label>📊 Teacher Assessment (TA) [Max: 10]</label>
          <input type="number" id="ta" class="input-ctrl" min="0" max="10" value="9">
        </div>
        <div class="input-group">
          <label>📑 Scheme / Total Marks</label>
          <select id="scheme" class="input-ctrl">
            <option value="30_70" selected>30 Internal + 70 External (Standard)</option>
            <option value="50_100">50 Internal + 100 External</option>
          </select>
        </div>
      </div>

      <div style="background:#eef2ff; border:1px solid #c7d2fe; border-radius:10px; padding:16px; display:flex; justify-content:space-between; align-items:center;">
        <div>
          <span style="font-size:13px; font-weight:700; color:#4338ca; text-transform:uppercase;">Calculated Internal Sessional Score:</span>
          <div style="font-size:24px; font-weight:900; color:#1e1b4b;" id="internalTotal">24 / 30</div>
        </div>
        <span style="font-size:13px; font-weight:700; color:#059669;">✅ Sessional Status: Strong</span>
      </div>

      <table class="table-target">
        <thead>
          <tr>
            <th>Target Grade</th>
            <th>Grade Point</th>
            <th>Total % Range</th>
            <th>Required in End-Sem (70 Marks)</th>
            <th>Outcome / Distinction</th>
          </tr>
        </thead>
        <tbody id="targetTableBody">
          <!-- Injected via JS -->
        </tbody>
      </table>
    </div>
  </div>

  <footer class="footer">
    <div class="container">
      <p>© 2026 <a href="/">AKTU Results Portal</a> — Academic Planning Tools</p>
    </div>
  </footer>

  <script>
    function updatePlanner() {{
      const ct1 = parseFloat(document.getElementById('ct1').value) || 0;
      const ct2 = parseFloat(document.getElementById('ct2').value) || 0;
      const ta = parseFloat(document.getElementById('ta').value) || 0;

      const ctAvg = (ct1 + ct2) / 2;
      const ctScaled = (ctAvg / 30) * 20;
      const internalTotal = Math.min(30, Math.round(ctScaled + ta));

      document.getElementById('internalTotal').textContent = `${{internalTotal}} / 30`;

      const grades = [
        {{ grade: 'O (Outstanding)', gp: '10', minTot: 90, desc: 'Top Tier Distinction', bg: '#dcfce7', col: '#15803d' }},
        {{ grade: 'A+ (Excellent)', gp: '9', minTot: 80, desc: 'Eligible for Honors Degree', bg: '#e0e7ff', col: '#3730a3' }},
        {{ grade: 'A (Very Good)', gp: '8', minTot: 70, desc: 'First Division with Distinction', bg: '#f0fdf4', col: '#166534' }},
        {{ grade: 'B+ (Good)', gp: '7', minTot: 60, desc: 'First Division', bg: '#fef3c7', col: '#92400e' }},
        {{ grade: 'B (Above Average)', gp: '6', minTot: 50, desc: 'Second Division', bg: '#f8fafc', col: '#334155' }},
        {{ grade: 'P (Pass Threshold)', gp: '4', minTot: 35, desc: 'Minimum Passing Threshold (30% in End-Sem required)', bg: '#fee2e2', col: '#991b1b' }}
      ];

      const tbody = document.getElementById('targetTableBody');
      tbody.innerHTML = grades.map(g => {{
        const reqTotal = g.minTot;
        let reqExt = reqTotal - internalTotal;
        let extNote = '';

        if (reqExt > 70) {{
          extNote = '<span style="color:#ef4444; font-weight:800;">Not Possible (Exceeds 70)</span>';
        }} else if (reqExt < 21) {{
          extNote = '<strong>21 / 70</strong> (Mandatory 30% min cutoff)';
        }} else {{
          extNote = `<strong>${{reqExt}} / 70</strong> (${{((reqExt/70)*100).toFixed(0)}}%)`;
        }}

        return `
          <tr>
            <td><span class="badge-grade" style="background:${{g.bg}}; color:${{g.col}};">${{g.grade}}</span></td>
            <td><strong>${{g.gp}}</strong></td>
            <td>${{g.minTot}}%+</td>
            <td>${{extNote}}</td>
            <td>${{g.desc}}</td>
          </tr>
        `;
      }}).join('');
    }}

    document.querySelectorAll('.input-ctrl').forEach(el => el.addEventListener('input', updatePlanner));
    document.addEventListener('DOMContentLoaded', updatePlanner);
  </script>
  <script defer src="/js/community-banner-widget.js"></script>
</body>
</html>"""

with open("tools/aktu-sessional-endsem-target-planner.html", "w", encoding="utf-8") as f:
    f.write(planner_html)
print("Created tools/aktu-sessional-endsem-target-planner.html")

# 4. AKTU PYQ & Study Notes / Quantum Hub
notes_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU PYQ & Study Notes Hub — Previous Year Papers, Quantum Series & Unit-Wise Notes</title>
  <meta name="description" content="Download AKTU Previous Year Question Papers (PYQ), Quantum series syllabus guides, important questions, formula sheets, and handwritten lecture notes for B.Tech CSE, IT, ECE, ME, CE, MBA & Pharmacy.">
  <meta name="keywords" content="AKTU PYQ papers, AKTU quantum series pdf, AKTU btech notes, AKTU previous year question papers, AKTU engineering syllabus notes">
  <link rel="canonical" href="https://akturesults.in/notes/aktu-pyq-notes-quantum-hub.html">
  <link rel="icon" href="/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
{ad_tags}
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": "AKTU PYQ & Study Notes Hub",
    "url": "https://akturesults.in/notes/aktu-pyq-notes-quantum-hub.html",
    "description": "Comprehensive digital library of AKTU Previous Year Question Papers and unit-wise notes."
  }}
  </script>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', sans-serif; }}
    body {{ background: #f8fafc; color: #1e293b; line-height: 1.6; }}
    .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
    nav {{ background: #ffffff; border-bottom: 1px solid #e2e8f0; padding: 16px 0; position: sticky; top: 0; z-index: 100; }}
    .nav-inner {{ display: flex; justify-content: space-between; align-items: center; }}
    .logo {{ font-size: 22px; font-weight: 800; color: #4338ca; text-decoration: none; }}
    .hero {{ background: linear-gradient(135deg, #1e1b4b, #312e81, #4338ca); color: #ffffff; padding: 48px 0 36px; text-align: center; }}
    .hero h1 {{ font-size: 32px; font-weight: 900; margin-bottom: 10px; }}
    .hero p {{ font-size: 16px; opacity: 0.9; max-width: 700px; margin: 0 auto; }}
    .filter-card {{ background: #ffffff; border-radius: 16px; border: 1px solid #e2e8f0; padding: 24px; margin: -25px auto 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.06); position: relative; z-index: 10; }}
    .filter-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }}
    .filter-group label {{ display: block; font-size: 12px; font-weight: 700; color: #475569; margin-bottom: 6px; text-transform: uppercase; }}
    .filter-ctrl {{ width: 100%; padding: 10px 14px; border-radius: 8px; border: 1px solid #cbd5e1; font-size: 14px; outline: none; background: #f8fafc; font-weight: 600; color: #1e293b; }}
    .subject-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 20px; margin-bottom: 50px; }}
    .subject-card {{ background: #ffffff; border-radius: 14px; border: 1px solid #e2e8f0; padding: 22px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); display: flex; flex-direction: column; justify-content: space-between; }}
    .subject-code {{ font-size: 12px; font-weight: 800; background: #e0e7ff; color: #3730a3; padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 8px; }}
    .subject-title {{ font-size: 17px; font-weight: 800; color: #0f172a; margin-bottom: 6px; }}
    .subject-meta {{ font-size: 13px; color: #64748b; margin-bottom: 14px; }}
    .resource-links {{ display: flex; flex-direction: column; gap: 8px; }}
    .res-link {{ display: flex; justify-content: space-between; align-items: center; padding: 8px 12px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; font-size: 13px; font-weight: 700; color: #4338ca; text-decoration: none; transition: all 0.2s; }}
    .res-link:hover {{ background: #eef2ff; border-color: #c7d2fe; }}
    .footer {{ background: #0f172a; color: #ffffff; text-align: center; padding: 40px 0; font-size: 14px; }}
    .footer a {{ color: #06b6d4; text-decoration: none; }}
  </style>
</head>
<body>
  <nav>
    <div class="container nav-inner">
      <a href="/" class="logo">📚 AKTU Results</a>
      <div>
        <a href="/syllabus.html" style="color:#4338ca; text-decoration:none; font-weight:700; font-size:14px; margin-right:15px;">📜 Syllabus Hub</a>
        <a href="/calculators.html" style="color:#059669; text-decoration:none; font-weight:700; font-size:14px;">🧮 Calculators</a>
      </div>
    </div>
  </nav>

  <div class="hero">
    <div class="container">
      <span style="background:rgba(255,255,255,0.15); padding:4px 14px; border-radius:20px; font-size:12px; font-weight:800; display:inline-block; margin-bottom:10px;">📖 100% Free Study Material</span>
      <h1>AKTU PYQ, Quantum & Notes Hub</h1>
      <p>Previous year exam papers, unit-wise handwritten notes, important repeated questions, and formula sheets for all branches.</p>
    </div>
  </div>

  <div class="container">
    <div class="filter-card">
      <div class="filter-grid">
        <div class="filter-group">
          <label>🔍 Search Subject / Code</label>
          <input type="text" id="searchSubject" class="filter-ctrl" placeholder="e.g. Data Structures, BCS-301, OS...">
        </div>
        <div class="filter-group">
          <label>🎓 Year / Semester</label>
          <select id="semSelect" class="filter-ctrl">
            <option value="ALL">All Semesters (1st to 8th)</option>
            <option value="1">1st Year (Sem 1 & 2)</option>
            <option value="2">2nd Year (Sem 3 & 4)</option>
            <option value="3">3rd Year (Sem 5 & 6)</option>
            <option value="4">4th Year (Sem 7 & 8)</option>
          </select>
        </div>
        <div class="filter-group">
          <label>💻 Branch</label>
          <select id="branchSelect" class="filter-ctrl">
            <option value="ALL">All Engineering Branches</option>
            <option value="CSE">Computer Science (CSE / IT / AI)</option>
            <option value="ECE">Electronics & Communication (ECE)</option>
            <option value="ME">Mechanical Engineering (ME)</option>
            <option value="CE">Civil Engineering (CE)</option>
            <option value="EE">Electrical Engineering (EE)</option>
          </select>
        </div>
      </div>
    </div>

    <div class="subject-grid" id="subjectsContainer">
      <!-- Injected via JavaScript -->
    </div>
  </div>

  <footer class="footer">
    <div class="container">
      <p>© 2026 <a href="/">AKTU Results Portal</a> — Digital Study Library for AKTU Students</p>
    </div>
  </footer>

  <script>
    const subjects = [
      {{ code: 'BCS-301', name: 'Data Structures & Algorithms', sem: 3, year: 2, branch: 'CSE', units: 5 }},
      {{ code: 'BCS-302', name: 'Computer Organization & Architecture (COA)', sem: 3, year: 2, branch: 'CSE', units: 5 }},
      {{ code: 'BCS-303', name: 'Discrete Mathematics (DM)', sem: 3, year: 2, branch: 'CSE', units: 5 }},
      {{ code: 'BCS-401', name: 'Operating Systems (OS)', sem: 4, year: 2, branch: 'CSE', units: 5 }},
      {{ code: 'BCS-402', name: 'Theory of Computation (TOC / Automata)', sem: 4, year: 2, branch: 'CSE', units: 5 }},
      {{ code: 'BCS-403', name: 'Object Oriented Programming with Java', sem: 4, year: 2, branch: 'CSE', units: 5 }},
      {{ code: 'BCS-501', name: 'Database Management Systems (DBMS)', sem: 5, year: 3, branch: 'CSE', units: 5 }},
      {{ code: 'BCS-502', name: 'Compiler Design (CD)', sem: 5, year: 3, branch: 'CSE', units: 5 }},
      {{ code: 'BCS-503', name: 'Design & Analysis of Algorithms (DAA)', sem: 5, year: 3, branch: 'CSE', units: 5 }},
      {{ code: 'BCS-601', name: 'Software Engineering (SE)', sem: 6, year: 3, branch: 'CSE', units: 5 }},
      {{ code: 'BCS-602', name: 'Computer Networks (CN)', sem: 6, year: 3, branch: 'CSE', units: 5 }},
      {{ code: 'BCS-701', name: 'Artificial Intelligence (AI)', sem: 7, year: 4, branch: 'CSE', units: 5 }},
      {{ code: 'BAS-101', name: 'Engineering Mathematics - I', sem: 1, year: 1, branch: 'ALL', units: 5 }},
      {{ code: 'BAS-102', name: 'Engineering Physics', sem: 1, year: 1, branch: 'ALL', units: 5 }},
      {{ code: 'BAS-103', name: 'Engineering Chemistry', sem: 1, year: 1, branch: 'ALL', units: 5 }},
      {{ code: 'BEE-101', name: 'Basic Electrical Engineering (BEE)', sem: 1, year: 1, branch: 'ALL', units: 5 }},
      {{ code: 'BEC-301', name: 'Electronic Devices & Circuits (EDC)', sem: 3, year: 2, branch: 'ECE', units: 5 }},
      {{ code: 'BEC-302', name: 'Digital System Design (DSD)', sem: 3, year: 2, branch: 'ECE', units: 5 }},
      {{ code: 'BME-301', name: 'Thermodynamics', sem: 3, year: 2, branch: 'ME', units: 5 }},
      {{ code: 'BME-401', name: 'Applied Thermodynamics', sem: 4, year: 2, branch: 'ME', units: 5 }},
      {{ code: 'BCE-301', name: 'Building Materials & Construction', sem: 3, year: 2, branch: 'CE', units: 5 }},
      {{ code: 'BCE-401', name: 'Hydraulics & Hydraulic Machines', sem: 4, year: 2, branch: 'CE', units: 5 }}
    ];

    function renderSubjects(data) {{
      const container = document.getElementById('subjectsContainer');
      if (data.length === 0) {{
        container.innerHTML = '<div style="grid-column:1/-1; text-align:center; padding:40px; background:#fff; border-radius:12px; color:#64748b;">No subjects matching your search filter.</div>';
        return;
      }}

      container.innerHTML = data.map(s => `
        <div class="subject-card">
          <div>
            <span class="subject-code">${{s.code}}</span>
            <h2 class="subject-title">${{s.name}}</h2>
            <div class="subject-meta">Sem ${{s.sem}} • Year ${{s.year}} • ${{s.branch}} Branch • ${{s.units}} Units</div>
          </div>
          <div class="resource-links">
            <a href="/syllabus/subjects/subject-${{s.code.toLowerCase().replace(/[^a-z0-9]/g, '-')}}-syllabus.html" class="res-link">
              <span>📖 Complete Syllabus & Units</span>
              <span>→</span>
            </a>
            <a href="/syllabus/aktu-btech-cse-${{s.sem}}th-semester-syllabus-2026.html" class="res-link" style="color:#059669;">
              <span>📑 Previous Year Papers (PYQ)</span>
              <span>Download ↓</span>
            </a>
            <a href="/calculators.html" class="res-link" style="color:#6366f1;">
              <span>💡 Important Repeated Questions</span>
              <span>View</span>
            </a>
          </div>
        </div>
      `).join('');
    }}

    function filterSubjects() {{
      const q = document.getElementById('searchSubject').value.toLowerCase().trim();
      const sem = document.getElementById('semSelect').value;
      const branch = document.getElementById('branchSelect').value;

      const filtered = subjects.filter(s => {{
        if (q && !s.name.toLowerCase().includes(q) && !s.code.toLowerCase().includes(q)) return false;
        if (sem !== 'ALL' && s.year !== parseInt(sem)) return false;
        if (branch !== 'ALL' && s.branch !== 'ALL' && s.branch !== branch) return false;
        return true;
      }});

      renderSubjects(filtered);
    }}

    document.getElementById('searchSubject').addEventListener('input', filterSubjects);
    document.getElementById('semSelect').addEventListener('change', filterSubjects);
    document.getElementById('branchSelect').addEventListener('change', filterSubjects);

    document.addEventListener('DOMContentLoaded', () => renderSubjects(subjects));
  </script>
  <script defer src="/js/community-banner-widget.js"></script>
</body>
</html>"""

with open("notes/aktu-pyq-notes-quantum-hub.html", "w", encoding="utf-8") as f:
    f.write(notes_html)
print("Created notes/aktu-pyq-notes-quantum-hub.html")

