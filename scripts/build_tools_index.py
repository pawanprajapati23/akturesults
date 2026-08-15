import os

ad_tags = """  <!-- Monetag -->
  
  
  
  
  
  """

tools = [
    {
        "title": "🎁 AKTU Grace & COP Fee Calculator",
        "url": "/tools/aktu-grace-cop-fee-calculator.html",
        "desc": "Calculate rule-based AKTU grace marks eligibility (10-mark annual limit) and COP exam fee breakdown with ERP fee payment guide."
    },
    {
        "title": "💰 UPTAC Scholarship & Fee ROI Calculator",
        "url": "/tools/uptac-scholarship-fee-roi-calculator.html",
        "desc": "Compare 4-year tuition & hostel outlay across top AKTU colleges, calculate UP Scholarship refund (₹56,600 cap), and Fee Waiver savings."
    },
    {
        "title": "🔍 Challenge Evaluation ROI Calculator",
        "url": "/tools/aktu-challenge-evaluation-roi-calculator.html",
        "desc": "Calculate Stage 1 (₹300) vs Stage 2 (₹2,500) revaluation costs, assess risk level, and calculate 15% marks increase threshold for ₹1,800 refund."
    },
    {
        "title": "🎯 UPTAC Choice Filling Predictor",
        "url": "/admissions/uptac-choice-filling-predictor-2026.html",
        "desc": "Predict your admission chances in top AKTU colleges by entering your JEE Main CRL / Category rank with instant college recommendations."
    },
    {
        "title": "📅 Attendance & Bunk Calculator",
        "url": "/tools/aktu-attendance-bunk-calculator.html",
        "desc": "Calculate how many lectures you can safely skip or need to attend to maintain the mandatory 75% attendance threshold."
    },
    {
        "title": "🧮 AKTU Passing Marks Calculator",
        "url": "/tools/aktu-passing-marks-calculator.html",
        "desc": "Check minimum external marks required (30% or 35%) and total combined pass marks based on your internal sessional scores."
    },
    {
        "title": "🔮 Semester Result & Backlog Predictor",
        "url": "/tools/result-predictor.html",
        "desc": "Predict your expected SGPA/CGPA and evaluate backlog clearance probability based on internal marks and credit weights."
    },
    {
        "title": "📊 AKTU Marks & CGPA Analyzer",
        "url": "/tools/aktu-marks-analyzer.html",
        "desc": "Comprehensive analysis of your semester marksheet with grade conversions, credit distribution, and division calculations."
    },
    {
        "title": "🏛️ College Comparison Tool",
        "url": "/tools/college-comparison.html",
        "desc": "Side-by-side comparison of 2 or more AKTU colleges on NIRF rank, NAAC grade, tuition fees, and highest salary packages."
    },
    {
        "title": "⚡ AKTU Master Search Engine",
        "url": "/tools/aktu-master-search-engine-2026.html",
        "desc": "Instant real-time search across syllabus notes, previous year question papers, circulars, and college cutoffs."
    }
]

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU Calculators & Student Tools Hub | Free Academic Utilities</title>
  <meta name="description" content="Access all free AKTU tools: CGPA Calculator, Attendance Planner, Grace Marks & COP Fee Calculator, UPTAC Scholarship ROI, and Challenge Evaluation Predictor.">
  <link rel="canonical" href="https://akturesults.in/tools/">
  <link rel="icon" href="/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
{ad_tags}
  <style>
    * {{ margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans', sans-serif; }}
    body {{ background:#f8fafc; color:#1e293b; line-height:1.7; }}
    .container {{ max-width:1140px; margin:0 auto; padding:0 20px; }}
    nav {{ background:#fff; border-bottom:1px solid #e2e8f0; padding:16px 0; }}
    .nav-inner {{ display:flex; justify-content:space-between; align-items:center; }}
    .logo {{ font-size:22px; font-weight:800; color:#4338ca; text-decoration:none; }}
    .hero {{ background:linear-gradient(135deg, #1e1b4b, #4338ca); color:#fff; padding:55px 0 45px; text-align:center; }}
    .hero h1 {{ font-size:36px; font-weight:900; margin-bottom:12px; }}
    .hero p {{ font-size:16px; opacity:.9; max-width:700px; margin:0 auto; }}
    .tools-grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(340px, 1fr)); gap:22px; margin:40px 0 60px; }}
    .tool-card {{ background:#fff; border:1px solid #e2e8f0; border-radius:14px; padding:24px; box-shadow:0 4px 15px rgba(0,0,0,0.04); display:flex; flex-direction:column; justify-content:space-between; transition:transform .2s, box-shadow .2s; }}
    .tool-card:hover {{ transform:translateY(-3px); box-shadow:0 10px 25px rgba(0,0,0,0.08); border-color:#cbd5e1; }}
    .tool-title {{ font-size:18px; font-weight:800; color:#0f172a; margin-bottom:8px; }}
    .tool-desc {{ font-size:14px; color:#475569; margin-bottom:18px; }}
    .btn-tool {{ background:#4338ca; color:#fff; padding:10px 18px; border-radius:8px; font-weight:700; text-decoration:none; font-size:13px; text-align:center; transition:background .2s; }}
    .btn-tool:hover {{ background:#3730a3; }}
    .footer {{ background:#0f172a; color:#fff; text-align:center; padding:35px 0; font-size:14px; }}
    .footer a {{ color:#06b6d4; text-decoration:none; }}
  </style>
</head>
<body>
  <nav>
    <div class="container nav-inner">
      <a href="/" class="logo">AKTU Results</a>
      <a href="/" style="color:#4338ca; text-decoration:none; font-weight:700; font-size:14px;">← Back to Home</a>
    </div>
  </nav>

  <div class="hero">
    <div class="container">
      <span style="background:rgba(255,255,255,.15); padding:4px 14px; border-radius:20px; font-size:12px; font-weight:700; display:inline-block; margin-bottom:10px;">⚡ Free Student Utilities</span>
      <h1>AKTU Calculators & Student Tools</h1>
      <p>Instant academic calculators for AKTU students — CGPA, Grace marks, COP examination fee, Attendance, and UPTAC admission predictors.</p>
    </div>
  </div>

  <div class="container">
    <div class="tools-grid">
      { "".join([f'''<div class="tool-card">
        <div>
          <h3 class="tool-title">{t["title"]}</h3>
          <p class="tool-desc">{t["desc"]}</p>
        </div>
        <a href="{t["url"]}" class="btn-tool">Open Tool →</a>
      </div>''' for t in tools]) }
    </div>
  </div>

  <footer class="footer">
    <div class="container">
      <p>© 2026 <a href="/">AKTU Results Portal</a> — Built for AKTU & UPTAC Students</p>
    </div>
  </footer>
  <script defer src="/js/community-banner-widget.js"></script>
</body>
</html>"""

with open('tools/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Created tools/index.html hub page!")

# Fix redirects
with open('results/aktu-erp-login-result.html', 'w', encoding='utf-8') as f:
    f.write("""<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url=/results/aktu-erp-login-result-2026.html"><title>Redirecting...</title></head><body><script>window.location.href='/results/aktu-erp-login-result-2026.html';</script></body></html>""")

with open('aktu-result-server-down.html', 'w', encoding='utf-8') as f:
    f.write("""<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url=/results/aktu-result-server-down.html"><title>Redirecting...</title></head><body><script>window.location.href='/results/aktu-result-server-down.html';</script></body></html>""")

with open('aktu-erp-login-guide.html', 'w', encoding='utf-8') as f:
    f.write("""<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url=/results/aktu-erp-login-result-2026.html"><title>Redirecting...</title></head><body><script>window.location.href='/results/aktu-erp-login-result-2026.html';</script></body></html>""")

with open('aktu-one-view-result-2026.html', 'w', encoding='utf-8') as f:
    f.write("""<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url=/results/aktu-one-view-result-2026.html"><title>Redirecting...</title></head><body><script>window.location.href='/results/aktu-one-view-result-2026.html';</script></body></html>""")

print("Cleaned up remaining link targets!")
