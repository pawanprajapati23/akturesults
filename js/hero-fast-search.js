// Instant Client-Side Live Search & Quick Jump Engine for AKTU Results Portal
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
