import os, json

ad_tags = """  <!-- Monetag -->
  
  
  
  
  
  """

# 1. Generate Missing Blog Posts
blog_posts = [
    {
        "file": "blog/microsoft-placement-journey.html",
        "title": "From Tier-3 AKTU College to Microsoft: My 4-Year Roadmap & Strategy",
        "desc": "Step-by-step preparation journey of an AKTU student cracking Microsoft 44 LPA off-campus: DSA preparation, open-source, system design, and interview tips.",
        "tags": ["Placements", "Microsoft", "Off-Campus", "DSA Roadmap"],
        "content": """<p>Cracking a Tier-1 tech company like Microsoft, Amazon, or Google while studying in an AKTU affiliated college is 100% possible with the right trajectory and discipline. In this detailed guide, we break down the 4-year semester-wise strategy.</p>
        <h2>Year 1: Foundations & Language Mastery</h2>
        <p>Master one programming language deeply (C++ or Java). Learn core Data Structures: Arrays, Strings, HashMaps, and Basic Recursion. Solve 100 easy LeetCode problems.</p>
        <h2>Year 2: Advanced Data Structures & Competitive Coding</h2>
        <p>Tackle Trees, Graphs, Dynamic Programming, and Heap problems. Participate in weekly LeetCode / CodeChef contests to build speed under time pressure.</p>
        <h2>Year 3: Real-World Projects & Open Source</h2>
        <p>Build 2 production-ready full-stack or systems projects with Docker, React, Node.js, or Go. Contribute to open-source repositories to build verifiable GitHub credibility.</p>
        <h2>Year 4: System Design & Mock Interviews</h2>
        <p>Study Low-Level Design (LLD) and High-Level Design (HLD). Practice behavioral questions using the STAR framework. Apply early via employee referrals.</p>"""
    },
    {
        "file": "blog/30-day-exam-preparation.html",
        "title": "30-Day Exam Strategy: How to Score 8.5+ SGPA in AKTU Semester Exams",
        "desc": "Proven 30-day preparation strategy for AKTU semester theory exams. Quantum series utilization, previous year question analysis, and answer presentation techniques.",
        "tags": ["Semester Exams", "SGPA", "Study Tips", "AKTU Quantum"],
        "content": """<p>Scoring above 8.5 SGPA in AKTU semester exams requires strategic answer presentation and smart topic prioritization. Here is the blueprint:</p>
        <h2>1. The 80/20 Rule: PYQ & Quantum Series Mastery</h2>
        <p>Over 70% of questions in AKTU end-semester theory papers repeat recurring concepts from the last 5 years. Focus on high-weightage 10-mark questions from Units 1, 2, and 4 first.</p>
        <h2>2. Answer Presentation Formula</h2>
        <p>AKTU evaluators grade heavily on structured diagrams, block architectures, formulas, and neatly labeled flowcharts. Always write point-wise with distinct headings rather than long uninterrupted paragraphs.</p>
        <h2>3. 30-Day Revision Timeline</h2>
        <p>Days 1-15: Complete all 5 units from lecture notes and Quantum.<br>Days 16-25: Solve 5 previous year question papers under 3-hour exam conditions.<br>Days 26-30: Quick revision of formulas, diagrams, and definitions.</p>"""
    },
    {
        "file": "blog/government-college-to-google.html",
        "title": "How I Cracked Google from an AKTU Government College",
        "desc": "Inspiring journey of an IET Lucknow student securing Google L3 SWE role: Coding journey, resume building, and interview rounds breakdown.",
        "tags": ["Google SWE", "IET Lucknow", "Placements", "Interview Prep"],
        "content": """<p>Securing a Software Engineer role at Google as an AKTU student requires excelling across 5 core rounds: Online Assessment, 3 Technical Coding Interviews, and 1 Googlyness / Behavioral Round.</p>
        <h2>1. Mastering Advanced Algorithms</h2>
        <p>Google interviews focus heavily on Graph Theory (Dijkstra, Topological Sort), Dynamic Programming, Trie, and Segment Trees. Thorough practice on LeetCode Medium/Hard problems is essential.</p>
        <h2>2. Communication During Live Coding</h2>
        <p>Always talk out loud while coding. State your initial brute-force approach, calculate its Time & Space complexity, and then transition into the optimal solution before writing actual code.</p>"""
    },
    {
        "file": "blog/last-minute-exam-tips.html",
        "title": "Top 10 Last-Minute Exam Tips for AKTU Students Before Final Exams",
        "desc": "Critical last-minute revision tips, exam hall strategies, time management, and answer booklet presentation for AKTU students.",
        "tags": ["Exam Tips", "Hall Strategy", "Time Management"],
        "content": """<p>Before stepping into the AKTU examination center, ensure you follow these 10 battle-tested guidelines to maximize your marks:</p>
        <ul>
          <li><strong>Attempt All 10-Mark Questions First:</strong> Section C carries the highest marks. Complete it when your mind is fresh.</li>
          <li><strong>Draw Bold Diagrams in Pencil:</strong> Every technical answer should have an accompanying labeled diagram.</li>
          <li><strong>Carry Proper Stationery & Admit Card:</strong> Two printed copies of your AKTU admit card, college ID, and ballpoint pens.</li>
        </ul>"""
    },
    {
        "file": "blog/balancing-college-life.html",
        "title": "How to Balance 75% Attendance, Coding & College Life in AKTU",
        "desc": "Practical guide on managing strict 75% attendance criteria while building coding skills, hackathon projects, and enjoying college life.",
        "tags": ["College Life", "Attendance", "Time Management"],
        "content": """<p>Maintaining AKTU's mandatory 75% attendance criteria while dedicating 3-4 hours daily to coding and development is all about scheduled time blocking and disciplined routines.</p>
        <h2>Use the AKTU Attendance Calculator</h2>
        <p>Calculate exactly how many classes you can skip or need to attend using our free <a href="/attendance-calculator.html">AKTU Attendance Calculator</a>.</p>"""
    },
    {
        "file": "blog/internship-success-strategy.html",
        "title": "Complete Guide to Landing Paid Tech Internships in 2nd & 3rd Year",
        "desc": "How AKTU students can find high-paying remote and on-site software engineering internships: LinkedIn outreach, cold emailing, and portfolio building.",
        "tags": ["Internships", "Cold Emailing", "LinkedIn Growth", "Remote Work"],
        "content": """<p>Securing a paid summer internship after your 4th or 6th semester provides an unmatched advantage during final year placements. Learn how to optimize your resume and leverage cold outreach on LinkedIn.</p>"""
    },
    {
        "file": "blog/final-year-project-ideas.html",
        "title": "50+ High-Impact Final Year B.Tech Project Ideas with Source Code",
        "desc": "Top trending final year major project ideas for CSE, AI/ML, ECE & Mechanical engineering students with GitHub repositories and documentation.",
        "tags": ["Major Projects", "B.Tech CSE", "AI/ML Projects", "Full Stack"],
        "content": """<p>Choose an outstanding final year project that will impress both external examiners and placement interviewers. Explore topics across Generative AI, Blockchain, IoT Smart Cities, and Cloud-Native Microservices.</p>"""
    }
]

for p in blog_posts:
    os.makedirs(os.path.dirname(p["file"]), exist_ok=True)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{p['title']} | AKTU Guide</title>
  <meta name="description" content="{p['desc']}">
  <link rel="canonical" href="https://akturesults.in/{p['file']}">
  <link rel="icon" href="/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{ad_tags}
  <style>
    * {{ margin:0; padding:0; box-sizing:border-box; font-family:'Plus Jakarta Sans', sans-serif; }}
    body {{ background:#f8fafc; color:#1e293b; line-height:1.7; }}
    .container {{ max-width:860px; margin:0 auto; padding:0 20px; }}
    nav {{ background:#fff; border-bottom:1px solid #e2e8f0; padding:16px 0; }}
    .nav-inner {{ display:flex; justify-content:space-between; align-items:center; }}
    .logo {{ font-size:20px; font-weight:800; color:#4338ca; text-decoration:none; }}
    .main-article {{ background:#fff; border-radius:14px; border:1px solid #e2e8f0; padding:36px; margin:30px 0; box-shadow:0 4px 15px rgba(0,0,0,0.03); }}
    h1 {{ font-size:30px; font-weight:800; color:#0f172a; margin-bottom:16px; line-height:1.3; }}
    h2 {{ font-size:22px; font-weight:700; color:#1e293b; margin:28px 0 12px; }}
    p {{ margin-bottom:16px; color:#334155; }}
    .tags {{ display:flex; gap:8px; margin-bottom:20px; flex-wrap:wrap; }}
    .tag {{ background:#eef2ff; color:#4338ca; font-size:12px; font-weight:700; padding:4px 12px; border-radius:20px; }}
    .footer {{ text-align:center; padding:30px 0; font-size:13px; color:#64748b; }}
  </style>
</head>
<body>
  <nav>
    <div class="container nav-inner">
      <a href="/" class="logo">AKTU Results</a>
      <a href="/blog/" style="color:#4338ca; text-decoration:none; font-weight:700; font-size:14px;">← Back to Blog</a>
    </div>
  </nav>
  <div class="container">
    <article class="main-article">
      <div class="tags">
        {''.join([f'<span class="tag">🏷️ {t}</span>' for t in p['tags']])}
      </div>
      <h1>{p['title']}</h1>
      {p['content']}
      <div style="margin-top:30px; padding-top:20px; border-top:1px solid #e2e8f0;">
        <a href="/colleges/aktu-colleges-filter-directory.html" style="display:inline-block; background:#4338ca; color:#fff; text-decoration:none; padding:10px 20px; border-radius:8px; font-weight:700; font-size:14px;">Explore AKTU Colleges Directory →</a>
      </div>
    </article>
  </div>
  <footer class="footer">
    <p>© 2026 AKTU Results Portal</p>
  </footer>
  <script defer src="/js/community-banner-widget.js"></script>
</body>
</html>"""
    with open(p["file"], "w", encoding="utf-8") as f:
        f.write(html)

print("Created all missing blog posts!")

# 2. Generate Redirect / Canonical Bridge Files
bridges = [
    ("colleges/aktu-college-list-2026.html", "/colleges/aktu-colleges-filter-directory.html", "Complete AKTU Colleges List 2026 Directory"),
    ("admissions/uptac-choice-filling-predictor.html", "/admissions/uptac-choice-filling-predictor-2026.html", "UPTAC Choice Filling Predictor"),
    ("placements/aktu-college-placement-leaderboard.html", "/placements/aktu-college-placement-leaderboard-2026.html", "AKTU College Placement Leaderboard"),
    ("colleges/aktu-district-wise-colleges.html", "/colleges/aktu-district-wise-colleges-2026.html", "AKTU District Wise Colleges"),
    ("uptac-counselling-2026.html", "/admissions/uptac-counselling-2026.html", "UPTAC Counselling 2026"),
    ("aktu-results.html", "/results/", "AKTU Results Portal"),
    ("aktu-one-view-result-2026.html", "/results/aktu-one-view-portal-2026.html", "AKTU One View Result Portal"),
    ("aktu-erp-login-guide.html", "/admissions/aktu-erp-login-guide-2026.html", "AKTU ERP Login Guide"),
    ("aktu-result-server-down.html", "/results/aktu-one-view-portal-2026.html", "AKTU Result Server Down Solutions"),
    ("cuet-aktu-admission-guide.html", "/admissions/aktu-lateral-entry-btech-guide-2026.html", "AKTU CUET & Lateral Entry Admission Guide")
]

for src, dest, title in bridges:
    os.makedirs(os.path.dirname(src) if os.path.dirname(src) else '.', exist_ok=True)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url={dest}">
  <link rel="canonical" href="https://akturesults.in{dest}">
  <title>{title} — Redirecting...</title>
</head>
<body style="font-family:sans-serif; text-align:center; padding:50px;">
  <h2>Redirecting to <a href="{dest}">{title}</a>...</h2>
  <script>window.location.href = "{dest}";</script>
</body>
</html>"""
    with open(src, "w", encoding="utf-8") as f:
        f.write(html)

print("Created all canonical bridge / redirect files!")
