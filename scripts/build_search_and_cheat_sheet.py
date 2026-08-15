import os

# 1. BUILD FAST SEARCH ENGINE JAVASCRIPT: js/hero-fast-search.js
search_js = """// Instant Client-Side Live Search & Quick Jump Engine for AKTU Results Portal
(function() {
  const searchableIndex = [
    { title: "🎯 UPTAC 2026 AI Choice Filling Order Generator", category: "Tool", desc: "Top 50 college priority list for your JEE rank", url: "/tools/uptac-choice-filling-order-generator.html", keywords: "choice filling uptac jee main rank college priority counselling list 2026" },
    { title: "⚡ AKTU One-View Smart Result Analyzer & 4K Card", category: "Tool", desc: "SGPA, batch percentile & 4K status card", url: "/tools/aktu-one-view-result-analyzer-rank-card.html", keywords: "one view result analyzer rank card sgpa batch percentile aman verma" },
    { title: "📝 AKTU 70-Marks Exam Copy Score Simulator", category: "Tool", desc: "Predict external theory marks & back risk", url: "/tools/aktu-exam-copy-score-simulator.html", keywords: "copy score simulator back risk 70 marks theory exam passing marks 21" },
    { title: "📜 AKTU Percentage & Division Certificate Generator", category: "Tool", desc: "Official (CGPA - 0.75)*10 printable slip", url: "/tools/aktu-cgpa-to-percentage-certificate-generator.html", keywords: "percentage conversion certificate cgpa division distinction tcs infosys" },
    { title: "🎖️ AKTU Honours Degree Eligibility Checker", category: "Tool", desc: "7.5 CGPA, zero back & 20 MOOCs credits", url: "/tools/aktu-honours-degree-eligibility-checker.html", keywords: "honours degree eligibility moocs nptel 7.5 cgpa grace carryover" },
    { title: "📋 AKTU 75% Attendance & Bunk Calculator", category: "Tool", desc: "Find safe bunks and medical leave allowance", url: "/tools/aktu-attendance-bunk-calculator.html", keywords: "attendance bunk 75 percent medical debar rule calculate classes" },
    { title: "🎯 Sessional & Target Marks Planner", category: "Tool", desc: "Calculate required external marks out of 70", url: "/tools/aktu-sessional-endsem-target-planner.html", keywords: "sessional target planner internal ct1 ct2 teacher assessment" },
    { title: "🎁 AKTU Grace Marks & COP Fee Calculator", category: "Tool", desc: "PWG 10-mark rule & Rs 1000/subject COP fee", url: "/tools/aktu-grace-cop-fee-calculator.html", keywords: "grace marks cop carryover fee pwg ordinance rule 10 marks" },
    { title: "💰 UPTAC Scholarship & Fee ROI Calculator", category: "Tool", desc: "Compare 4-year tuition, FW seats & refund", url: "/tools/uptac-scholarship-fee-roi-calculator.html", keywords: "scholarship fee roi calculator up scholarship fw seat fee waiver" },
    { title: "🔍 AKTU Challenge Evaluation ROI Calculator", category: "Tool", desc: "Stage 1 (Rs 300) vs Stage 2 (Rs 2500) refund", url: "/tools/aktu-challenge-evaluation-roi-calculator.html", keywords: "challenge evaluation re-evaluation stage 1 stage 2 copy view refund" },
    { title: "📚 AKTU PYQ & Quantum Notes Hub", category: "Notes", desc: "Previous year papers & handwritten unit notes", url: "/notes/aktu-pyq-notes-quantum-hub.html", keywords: "quantum notes pyq previous year questions pdf unit wise btech" },
    { title: "🏛️ IET Lucknow (Code 052) Profile", category: "College", desc: "Top Govt College - Cutoffs, Fees & Placements", url: "/colleges/profiles/iet-lucknow-profile.html", keywords: "052 iet lucknow institute of engineering technology govt" },
    { title: "🏛️ KNIT Sultanpur (Code 104) Profile", category: "College", desc: "Top Govt Engineering College in UP", url: "/colleges/profiles/knit-sultanpur-profile.html", keywords: "104 knit sultanpur kamla nehru govt" },
    { title: "🏛️ BIET Jhansi (Code 043) Profile", category: "College", desc: "Bundelkhand Institute of Engg & Tech", url: "/colleges/profiles/biet-jhansi-profile.html", keywords: "043 biet jhansi govt bundelkhand" },
    { title: "🏛️ JSS Academy of Tech Education, Noida (Code 091)", category: "College", desc: "Premier Private Engineering Institute", url: "/colleges/profiles/jss-noida-profile.html", keywords: "091 jss noida academy sector 62 pvt" },
    { title: "🏛️ Ajay Kumar Garg Engg College (AKGEC) (Code 027)", category: "College", desc: "Ghaziabad Top Ranked Private College", url: "/colleges/profiles/akgec-ghaziabad-profile.html", keywords: "027 akgec ajay kumar garg ghaziabad" },
    { title: "🏛️ KIET Group of Institutions (Code 029)", category: "College", desc: "Ghaziabad Autonomous NAAC A+ College", url: "/colleges/profiles/kiet-ghaziabad-profile.html", keywords: "029 kiet ghaziabad muradnagar" },
    { title: "🏛️ ABES Engineering College (Code 032)", category: "College", desc: "Ghaziabad Top Placement Institute", url: "/colleges/profiles/abes-ghaziabad-profile.html", keywords: "032 abes engineering college ghaziabad nh 24" },
    { title: "🏛️ Galgotias College of Engg (Code 097)", category: "College", desc: "Greater Noida Knowledge Park II", url: "/colleges/profiles/galgotias-college-greater-noida-profile.html", keywords: "097 galgotias greater noida knowledge park" },
    { title: "🏛️ G.L. Bajaj Institute (Code 192)", category: "College", desc: "Greater Noida Top CSE Placements", url: "/colleges/profiles/gl-bajaj-greater-noida-profile.html", keywords: "192 gl bajaj glbitm greater noida" },
    { title: "🏛️ Pranveer Singh Institute (PSIT) (Code 164)", category: "College", desc: "Kanpur NH-2 80-Acre Campus", url: "/colleges/profiles/psit-kanpur-profile.html", keywords: "164 psit kanpur pranveer singh" },
    { title: "🏛️ NIET Greater Noida (Code 133)", category: "College", desc: "Autonomous Engineering Institute", url: "/colleges/profiles/niet-greater-noida-profile.html", keywords: "133 niet greater noida autonomous" }
  ];

  window.initHeroSearch = function(inputId, resultsId) {
    const input = document.getElementById(inputId);
    const results = document.getElementById(resultsId);
    if (!input || !results) return;

    input.addEventListener('input', function() {
      const q = this.value.trim().toLowerCase();
      if (!q || q.length < 2) {
        results.innerHTML = '';
        results.style.display = 'none';
        return;
      }

      const matches = searchableIndex.filter(item => {
        return item.title.toLowerCase().includes(q) ||
               item.keywords.toLowerCase().includes(q) ||
               item.desc.toLowerCase().includes(q);
      }).slice(0, 6);

      if (!matches.length) {
        results.innerHTML = '<div style="padding:14px; color:#94a3b8; font-size:13px; text-align:center;">No matching tools or colleges found for "' + q + '"</div>';
        results.style.display = 'block';
        return;
      }

      let html = '';
      matches.forEach(item => {
        html += `
          <a href="${item.url}" style="display:flex; align-items:center; justify-content:space-between; padding:12px 16px; border-bottom:1px solid #f1f5f9; text-decoration:none; color:#0f172a; transition:background 0.15s;" onmouseover="this.style.background='#f8fafc'" onmouseout="this.style.background='white'">
            <div>
              <div style="font-weight:700; font-size:14px; color:#1e293b;">${item.title}</div>
              <div style="font-size:12px; color:#64748b; margin-top:2px;">${item.desc}</div>
            </div>
            <span style="font-size:11px; font-weight:700; padding:3px 8px; border-radius:12px; background:#eff6ff; color:#2563eb; text-transform:uppercase;">${item.category}</span>
          </a>
        `;
      });
      results.innerHTML = html;
      results.style.display = 'block';
    });

    document.addEventListener('click', function(e) {
      if (!input.contains(e.target) && !results.contains(e.target)) {
        results.style.display = 'none';
      }
    });
  };
})();
"""

with open("js/hero-fast-search.js", "w", encoding="utf-8") as f:
    f.write(search_js)
print("Built js/hero-fast-search.js successfully!")


# 2. BUILD QUANTUM 1-NIGHT REVISION HUB: notes/aktu-last-night-pass-revision-sheets.html
cheat_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU 1-Night "Pass Guarantee" Quantum Revision Cheat-Sheet Hub</title>
  <meta name="description" content="Top 15 most repeated AKTU 10-mark questions, unit-wise formula summaries, block diagrams, and 3-hour last night exam cram sheet for B.Tech semester exams.">
  <link rel="canonical" href="https://akturesults.in/notes/aktu-last-night-pass-revision-sheets.html">
  <meta property="og:title" content="AKTU 1-Night Pass Guarantee Revision Cheat-Sheets">
  <meta property="og:description" content="High-yield 1-page revision summaries and top repeated PYQs for AKTU B.Tech exams. Free PDF download.">
  <meta property="og:url" content="https://akturesults.in/notes/aktu-last-night-pass-revision-sheets.html">
  <meta property="og:type" content="article">
  <meta property="og:image" content="https://akturesults.in/images/og-banner.png">
  <meta name="twitter:card" content="summary_large_image">

  <!-- Monetization Ad Tags -->
  
  
  
  
  

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "AKTU 1-Night Pass Guarantee Quantum Revision Cheat-Sheet Hub",
    "description": "High-yield formulas, repeated derivations, and exam cram sheets for AKTU B.Tech.",
    "author": { "@type": "Organization", "name": "AKTU Results" },
    "publisher": { "@type": "Organization", "name": "AKTU Results", "url": "https://akturesults.in/" }
  }
  </script>

  <style>
    :root {
      --primary: #0f172a;
      --accent: #dc2626;
      --accent-hover: #b91c1c;
      --blue: #2563eb;
      --text: #1e293b;
      --muted: #64748b;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', system-ui, -apple-system, sans-serif; }
    body { background: #f8fafc; color: var(--text); line-height: 1.6; }
    .container { max-width: 1100px; margin: 0 auto; padding: 20px; }

    header { background: #0f172a; color: white; padding: 18px 0; border-bottom: 3px solid var(--accent); }
    .header-content { display: flex; justify-content: space-between; align-items: center; max-width: 1100px; margin: 0 auto; padding: 0 20px; }
    .logo { font-size: 20px; font-weight: 800; color: white; text-decoration: none; display: flex; align-items: center; gap: 8px; }
    .back-btn { color: #94a3b8; text-decoration: none; font-size: 14px; font-weight: 600; padding: 6px 14px; background: rgba(255,255,255,0.08); border-radius: 8px; }
    .back-btn:hover { color: white; background: rgba(255,255,255,0.15); }

    .hero { text-align: center; padding: 35px 20px 25px; }
    .hero-badge { display: inline-block; padding: 6px 16px; background: #fee2e2; color: #991b1b; border-radius: 30px; font-size: 13px; font-weight: 700; margin-bottom: 12px; }
    .hero h1 { font-size: 30px; font-weight: 800; color: #0f172a; margin-bottom: 10px; }
    .hero p { color: var(--muted); font-size: 16px; max-width: 800px; margin: 0 auto; }

    .subject-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; margin: 30px 0; }
    .sheet-card { background: white; border-radius: 16px; padding: 25px; border: 1.5px solid #e2e8f0; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); transition: transform 0.2s; }
    .sheet-card:hover { transform: translateY(-4px); border-color: var(--blue); }
    .sheet-sem { font-size: 11px; font-weight: 800; text-transform: uppercase; color: var(--blue); margin-bottom: 6px; }
    .sheet-title { font-size: 18px; font-weight: 800; color: #0f172a; margin-bottom: 8px; }
    .sheet-code { font-size: 12px; color: #64748b; font-weight: 600; margin-bottom: 15px; }

    .sheet-points { list-style: none; margin: 15px 0; font-size: 13px; color: #475569; }
    .sheet-points li { display: flex; align-items: flex-start; gap: 8px; margin-bottom: 8px; }
    .sheet-points li::before { content: "🔥"; font-size: 12px; }

    .sheet-btn { display: block; width: 100%; text-align: center; padding: 10px; background: #0f172a; color: white; text-decoration: none; border-radius: 8px; font-size: 13px; font-weight: 700; transition: background 0.2s; }
    .sheet-btn:hover { background: var(--blue); }

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
      <a href="/notes/aktu-pyq-notes-quantum-hub.html" class="back-btn">← All Notes</a>
    </div>
  </header>

  <div class="container">
    <div class="hero">
      <span class="hero-badge">⚡ 3-HOUR LAST NIGHT CRAM PROTOCOL</span>
      <h1>📚 AKTU 1-Night "Pass Guarantee" Revision Cheat-Sheets</h1>
      <p>Short on time? Master the top 15 most repeated university questions, essential block diagrams, and unit formula summaries to comfortably clear your 21/70 theory passing cutoff!</p>
    </div>

    <div class="subject-grid">
      <!-- Data Structures -->
      <div class="sheet-card">
        <div class="sheet-sem">Semester 3 / 4 — B.Tech CSE & IT</div>
        <div class="sheet-title">Data Structures (BCS-301)</div>
        <div class="sheet-code">Code: BCS-301 / KCS-301</div>
        <ul class="sheet-points">
          <li><strong>Unit 1:</strong> Array operations, Sparse Matrix, Infix to Postfix conversion using Stack.</li>
          <li><strong>Unit 2:</strong> Circular Queue, Singly vs Doubly Linked List deletion/insertion algorithm.</li>
          <li><strong>Unit 3:</strong> Binary Tree Traversals (Inorder/Preorder/Postorder), AVL Tree Rotations (LL, RR, LR, RL).</li>
          <li><strong>Unit 4:</strong> Dijkstra Shortest Path algorithm &amp; Minimum Spanning Tree (Prim's &amp; Kruskal's).</li>
          <li><strong>Unit 5:</strong> Quick Sort vs Merge Sort time complexity derivation &amp; Hashing collision techniques.</li>
        </ul>
        <a href="/notes/aktu-pyq-notes-quantum-hub.html" class="sheet-btn">Download 1-Page Revision PDF →</a>
      </div>

      <!-- COA -->
      <div class="sheet-card">
        <div class="sheet-sem">Semester 3 / 4 — B.Tech CSE & IT</div>
        <div class="sheet-title">Computer Org &amp; Arch (BCS-302)</div>
        <div class="sheet-code">Code: BCS-302 / KCS-302</div>
        <ul class="sheet-points">
          <li><strong>Unit 1:</strong> Booth Multiplication Algorithm flowchart &amp; IEEE 754 Floating Point Representation.</li>
          <li><strong>Unit 2:</strong> Hardwired vs Microprogrammed Control Unit block diagrams.</li>
          <li><strong>Unit 3:</strong> Memory Hierarchy, Cache Mapping (Direct, Associative, Set-Associative).</li>
          <li><strong>Unit 4:</strong> Pipelining hazards (Data, Structural, Control) &amp; Speedup formula.</li>
          <li><strong>Unit 5:</strong> DMA Controller architecture &amp; Interrupt handling mechanism.</li>
        </ul>
        <a href="/notes/aktu-pyq-notes-quantum-hub.html" class="sheet-btn">Download 1-Page Revision PDF →</a>
      </div>

      <!-- Discrete Mathematics -->
      <div class="sheet-card">
        <div class="sheet-sem">Semester 3 / 4 — B.Tech CSE & IT</div>
        <div class="sheet-title">Discrete Mathematics (BCS-303)</div>
        <div class="sheet-code">Code: BCS-303 / KCS-303</div>
        <ul class="sheet-points">
          <li><strong>Unit 1:</strong> Principle of Mathematical Induction &amp; Pigeonhole Principle proofs.</li>
          <li><strong>Unit 2:</strong> Poset, Hasse Diagrams, Lattices, and Boolean Algebra laws.</li>
          <li><strong>Unit 3:</strong> Group Theory: Subgroups, Cyclic Groups, Lagrange's Theorem proof.</li>
          <li><strong>Unit 4:</strong> Generating Functions &amp; Homogeneous Recurrence Relations solution.</li>
          <li><strong>Unit 5:</strong> Graph Theory: Euler Graph, Hamiltonian Path, Planar Graphs (Euler's formula: V - E + F = 2).</li>
        </ul>
        <a href="/notes/aktu-pyq-notes-quantum-hub.html" class="sheet-btn">Download 1-Page Revision PDF →</a>
      </div>

      <!-- Engineering Mathematics-II -->
      <div class="sheet-card">
        <div class="sheet-sem">Semester 2 — All B.Tech Branches</div>
        <div class="sheet-title">Engineering Maths-II (BAS-203)</div>
        <div class="sheet-code">Code: BAS-203 / KAS-203</div>
        <ul class="sheet-points">
          <li><strong>Unit 1:</strong> Ordinary Differential Equations with constant coefficients &amp; Cauchy-Euler equations.</li>
          <li><strong>Unit 2:</strong> Method of Variation of Parameters &amp; Simultaneous linear differential equations.</li>
          <li><strong>Unit 3:</strong> Partial Differential Equations: Lagrange's linear PDE &amp; Charpit's Method.</li>
          <li><strong>Unit 4:</strong> Fourier Series of periodic functions &amp; Half-range sine/cosine series.</li>
          <li><strong>Unit 5:</strong> Laplace Transforms of standard functions, First/Second Shifting theorems &amp; Inverse Laplace.</li>
        </ul>
        <a href="/notes/aktu-pyq-notes-quantum-hub.html" class="sheet-btn">Download 1-Page Revision PDF →</a>
      </div>
    </div>

    <div class="content-card">
      <h2>The 3-Hour AKTU Last Night Exam Strategy</h2>
      <p>If you have less than 12 hours before entering the exam center, follow this time-tested preparation routine:</p>
      <ul>
        <li><strong>Hour 1 (Master 5 Core Diagrams):</strong> Draw and practice the 5 key architectural diagrams of your subject (e.g. Memory Hierarchy in COA, AVL Rotations in DS, Charpit's flowchart in Maths). Diagrams fetch instant step marks.</li>
        <li><strong>Hour 2 (Memorize Section A 2-Mark Definitions):</strong> Review 20 short definitions. Scoring 14-16 marks in Section A covers 75% of your passing cutoff requirement!</li>
        <li><strong>Hour 3 (Practice 2 High-Weightage Derivations):</strong> Solve one standard 7-mark numerical/derivation from Unit 1 and Unit 5.</li>
      </ul>
    </div>
  </div>

</body>
</html>"""

with open("notes/aktu-last-night-pass-revision-sheets.html", "w", encoding="utf-8") as f:
    f.write(cheat_html)
print("Built notes/aktu-last-night-pass-revision-sheets.html successfully!")

