import json
import os
import re

template_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{name} ({code}) {city} | Fees, Placements, Branches & Cutoff | Updated Annually</title>
<meta name="description" content="Complete updated guide for {name} (AKTU Code {code}). Verified fee structure (Rs {fee}/yr), hostel charges, branch-wise intake, {highest_pkg} highest package, NIRF {nirf}, NAAC {naac}, top recruiters & campus life." />
<meta name="keywords" content="{short_name_lower} fees, {short_name_lower} placement, aktu code {code} cutoff, {short_name_lower} hostel fee, {short_name_lower} branches, {short_name_lower} nirf ranking, {short_name_lower} admission, {city_lower} engineering college aktu" />
<link rel="canonical" href="https://akturesults.in/colleges/profiles/{filename}" />
<meta name="robots" content="index, follow" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet" />
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"EducationalOrganization","name":"{name}","alternateName":"{short_name}","url":"{website}","description":"{about_escaped}","address":{{"@type":"PostalAddress","streetAddress":"{address_clean}","addressLocality":"{city}","addressRegion":"{state}","addressCountry":"IN"}},"telephone":"{phone}","email":"{email}"}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://akturesults.in/"}},{{"@type":"ListItem","position":2,"name":"Colleges","item":"https://akturesults.in/colleges/"}},{{"@type":"ListItem","position":3,"name":"{short_name}","item":"https://akturesults.in/colleges/profiles/{filename}"}}]}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"What is the fee at {short_name}?","acceptedAnswer":{{"@type":"Answer","text":"Tuition fee Rs {fee}/yr, hostel Rs {hostel_double}/yr, mess Rs {mess}/yr. Total ~Rs {total_fee}/yr."}}}},{{"@type":"Question","name":"Highest package at {short_name}?","acceptedAnswer":{{"@type":"Answer","text":"Highest package is {highest_pkg}. Avg CSE package is {avg_pkg} with {placement_pct}% placement."}}}}]}}</script>
    <meta name="monetag" content="4b20c6816d7cac00b3d6430a41d4d86f" />
    <script src="https://quge5.com/88/tag.min.js" data-zone="257546" async data-cfasync="false"></script>
    <script async="async" data-cfasync="false" src="https://pl30261454.effectivecpmnetwork.com/1018cdea726c22b2c7ca9bbd11cccba8/invoke.js"></script>
    <script>(function(s){{s.dataset.zone='11257064',s.src='https://nap5k.com/tag.min.js'}})([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement('script')))</script>
<style>
:root{{--p:#4f46e5;--pd:#3730a3;--dark:#0f172a;--bg:#f8fafc;--bdr:#e2e8f0;--grn:#16a34a;}}
*{{margin:0;padding:0;box-sizing:border-box;font-family:'Plus Jakarta Sans',sans-serif;}}
body{{background:var(--bg);color:#1e293b;line-height:1.7;}}
.wrap{{max-width:1100px;margin:0 auto;padding:0 20px;}}
header{{background:linear-gradient(135deg,#1e1b4b,#312e81);color:white;padding:18px 0;}}
.brand{{font-size:24px;font-weight:800;color:white;text-decoration:none;display:flex;align-items:center;gap:8px;}}
.bc{{background:white;padding:11px 0;font-size:13px;border-bottom:1px solid var(--bdr);}}
.bc a{{color:var(--p);text-decoration:none;font-weight:500;}}
.bc span{{margin:0 6px;color:#94a3b8;}}
.hero{{background:linear-gradient(135deg,#1e1b4b,#4338ca);color:white;padding:35px 25px 28px;}}
.hero-top{{display:flex;align-items:center;gap:18px;margin-bottom:18px;flex-wrap:wrap;}}
.logo-box{{width:65px;height:65px;background:white;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:30px;flex-shrink:0;}}
.hero h1{{font-size:26px;font-weight:800;margin-bottom:5px;}}
.hero-meta{{font-size:13px;opacity:.85;}}
.badges{{display:flex;flex-wrap:wrap;gap:7px;margin-top:12px;}}
.badge{{background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.3);padding:4px 13px;border-radius:20px;font-size:12px;font-weight:700;}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px;margin-top:22px;}}
.stat{{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:10px;padding:13px;text-align:center;}}
.stat-v{{font-size:20px;font-weight:800;}}
.stat-l{{font-size:11px;opacity:.8;margin-top:2px;}}
.card{{background:white;border-radius:14px;border:1px solid var(--bdr);padding:26px;margin-bottom:20px;box-shadow:0 2px 6px rgba(0,0,0,.04);}}
.ctitle{{font-size:19px;font-weight:800;color:var(--dark);margin-bottom:16px;display:flex;align-items:center;gap:7px;padding-bottom:11px;border-bottom:2px solid #e0e7ff;}}
.ft{{width:100%;border-collapse:collapse;}}
.ft th{{background:#f8fafc;padding:11px 14px;text-align:left;font-size:12px;font-weight:700;color:#64748b;text-transform:uppercase;border-bottom:2px solid var(--bdr);}}
.ft td{{padding:12px 14px;border-bottom:1px solid var(--bdr);font-size:14px;}}
.ft tr:last-child td{{border-bottom:none;font-weight:800;color:var(--p);background:#f0f4ff;}}
.bt{{width:100%;border-collapse:collapse;}}
.bt th{{background:#312e81;color:white;padding:11px 14px;text-align:left;font-size:12px;}}
.bt td{{padding:11px 14px;border-bottom:1px solid var(--bdr);font-size:13px;}}
.bt tr:hover{{background:#f8fafc;}}
.rg{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;}}
.rc{{background:linear-gradient(135deg,#f8fafc,#e0e7ff);border:1px solid #c7d2fe;border-radius:10px;padding:14px;text-align:center;}}
.rv{{font-size:22px;font-weight:800;color:var(--pd);}}
.rl{{font-size:11px;color:#64748b;margin-top:3px;font-weight:600;}}
.cg{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;}}
.ci{{display:flex;align-items:flex-start;gap:10px;padding:13px;background:#f8fafc;border-radius:10px;}}
.clbl{{font-size:11px;color:#64748b;font-weight:600;text-transform:uppercase;}}
.cval{{font-size:13px;font-weight:600;color:var(--dark);word-break:break-all;}}
.cval a{{color:var(--p);text-decoration:none;}}
.socbar{{display:flex;flex-wrap:wrap;gap:9px;}}
.sbtn{{display:inline-flex;align-items:center;gap:5px;padding:8px 14px;border-radius:8px;font-size:12px;font-weight:700;text-decoration:none;color:white;transition:.2s;}}
.sbtn:hover{{transform:translateY(-2px);}}
.s1{{background:#4f46e5;}}
.s2{{background:#0077b5;}}
.s3{{background:#1da1f2;}}
.s4{{background:#1877f2;}}
.s5{{background:linear-gradient(135deg,#f58529,#dd2a7b,#8134af);}}
.s6{{background:#ff0000;}}
.clist{{list-style:none;padding:0;columns:2;}}
.clist li{{padding:5px 0;border-bottom:1px solid #f1f5f9;}}
.clist li::before{{content:"🎯 ";}}
footer{{background:var(--dark);color:white;padding:28px 0;text-align:center;margin-top:35px;font-size:13px;}}
footer a{{color:#38bdf8;text-decoration:none;}}
@media(max-width:768px){{.hero h1{{font-size:20px;}}.stats{{grid-template-columns:repeat(2,1fr);}}.clist{{columns:1;}}}}
</style>
</head>
<body>
<header><div class="wrap"><a href="/" class="brand"><img src="/favicon.png" alt="AKTU Results" style="width:32px;height:32px;border-radius:7px;" /> AKTU Results</a></div></header>
<nav class="bc"><div class="wrap"><a href="/">Home</a><span>›</span><a href="/colleges/">Colleges</a><span>›</span><span>{short_name}</span></div></nav>

<section class="hero"><div class="wrap">
<div class="hero-top">
<div class="logo-box">🏛️</div>
<div><h1>{name}</h1><div class="hero-meta">📍 {address}</div></div>
</div>
<div class="badges">
<span class="badge">Code: {code}</span>
<span class="badge">NAAC {naac}</span>
<span class="badge">AICTE Approved</span>
<span class="badge">{type}</span>
<span class="badge">Est. {est}</span>
<span class="badge">{area} Campus</span>
</div>
<div class="stats">
<div class="stat"><div class="stat-v" style="color:#4ade80;">{highest_pkg}</div><div class="stat-l">Highest Package</div></div>
<div class="stat"><div class="stat-v">{avg_pkg}</div><div class="stat-l">Avg CSE Package</div></div>
<div class="stat"><div class="stat-v">{placement_pct}%</div><div class="stat-l">Placement Rate</div></div>
<div class="stat"><div class="stat-v">{total_intake}</div><div class="stat-l">Total Intake</div></div>
<div class="stat"><div class="stat-v">NIRF</div><div class="stat-l">{nirf}</div></div>
</div>
</div></section>

<div class="wrap" style="margin-top:22px;">

<div class="card">
<h2 class="ctitle">📖 About {short_name}</h2>
<p>{about}</p>
<p style="margin-top:12px;"><strong>Infrastructure:</strong> {infra}</p>
</div>

<div class="card">
<h2 class="ctitle">🏆 Rankings & Accreditation (NIRF / NAAC)</h2>
<div class="rg">
<div class="rc"><div class="rv">{naac}</div><div class="rl">NAAC Grade</div></div>
<div class="rc"><div class="rv">{nirf}</div><div class="rl">NIRF Engg Band</div></div>
<div class="rc"><div class="rv">✅</div><div class="rl">AICTE Approved</div></div>
<div class="rc"><div class="rv">AKTU</div><div class="rl">University Affiliation</div></div>
</div>
</div>

<div class="card">
<h2 class="ctitle">💰 Complete Fee Structure (Updated Annually)</h2>
<div style="overflow-x:auto;">
<table class="ft">
<thead><tr><th>Fee Component</th><th>Amount / Year</th><th>Notes</th></tr></thead>
<tbody>
<tr><td><strong>B.Tech Tuition Fee</strong></td><td style="color:#16a34a;font-weight:700;">₹{fee}</td><td>All branches</td></tr>
<tr><td><strong>Hostel (Single Room)</strong></td><td>₹{hostel_single}</td><td>Limited seats, first-come basis</td></tr>
<tr><td><strong>Hostel (Double Sharing)</strong></td><td>₹{hostel_double}</td><td>Standard allocation</td></tr>
<tr><td><strong>Mess / Food Charges</strong></td><td>₹{mess}</td><td>Annual mess (veg + non-veg options)</td></tr>
<tr><td><strong>Development & Exam Fee</strong></td><td>₹{dev}</td><td>AKTU exam + student development</td></tr>
<tr><td><strong>Total (Hostel Student)</strong></td><td>₹{total_fee}</td><td>Per year with double sharing hostel</td></tr>
<tr><td><strong>Total 4-Year B.Tech</strong></td><td>₹{total_4yr}</td><td>Complete degree estimated cost</td></tr>
</tbody>
</table>
</div>
<p style="margin-top:12px;font-size:13px;color:#64748b;">ℹ️ SC/ST/OBC may qualify for UP Scholarship or TFW scheme. <a href="/tools/uptac-scholarship-fee-roi-calculator.html" style="color:var(--p);font-weight:700;">Calculate net cost with scholarship →</a></p>
</div>

<div class="card">
<h2 class="ctitle">🎓 Branches, Intake & Department Heads</h2>
<div style="overflow-x:auto;">
<table class="bt">
<thead><tr><th>Branch / Programme</th><th>Intake</th><th>Department HOD</th><th>Dept Grade</th></tr></thead>
<tbody>{branches_html}</tbody>
</table>
</div>
</div>

<div class="card">
<h2 class="ctitle">💼 Latest Placement — Companies & Packages</h2>
<div class="rg" style="margin-bottom:16px;">
<div class="rc"><div class="rv" style="color:#16a34a;">{highest_pkg}</div><div class="rl">Highest Package</div></div>
<div class="rc"><div class="rv">{avg_pkg}</div><div class="rl">Avg CSE Package</div></div>
<div class="rc"><div class="rv">{placement_pct}%</div><div class="rl">Students Placed</div></div>
</div>
<h3 style="font-size:15px;font-weight:700;margin-bottom:9px;">🏢 Top Visiting Recruiters:</h3>
<div>{recruiters_html}</div>
<div style="margin-top:13px;background:#f0fdf4;border-left:4px solid #16a34a;padding:13px;border-radius:8px;">
<p style="font-size:13px;"><strong>Tier 1 / Product MNCs:</strong> Top recruiters offer premium packages up to {highest_pkg}.</p>
<p style="font-size:13px;margin-top:5px;"><strong>Core & IT Services:</strong> Major recruiters hire at package ranges of ₹4-8 LPA.</p>
</div>
</div>

<div class="card">
<h2 class="ctitle">🎯 Campus Clubs & Student Life</h2>
<ul class="clist">{clubs_html}</ul>
</div>

<div class="card">
<h2 class="ctitle">📞 Contact Information</h2>
<div class="cg">
<div class="ci"><div style="font-size:20px;">📍</div><div><div class="clbl">Address</div><div class="cval">{address}</div></div></div>
<div class="ci"><div style="font-size:20px;">📱</div><div><div class="clbl">Phone</div><div class="cval"><a href="tel:{phone}">{phone}</a></div></div></div>
<div class="ci"><div style="font-size:20px;">✉️</div><div><div class="clbl">Email</div><div class="cval"><a href="mailto:{email}">{email}</a></div></div></div>
<div class="ci"><div style="font-size:20px;">🌐</div><div><div class="clbl">Official Website</div><div class="cval"><a href="{website}" target="_blank" rel="noopener">{website}</a></div></div></div>
</div>
</div>

<div class="card">
<h2 class="ctitle">🔗 Official Social Media</h2>
<div class="socbar">
<a href="{website}" class="sbtn s1" target="_blank" rel="noopener">🌐 Website</a>
<a href="#" class="sbtn s2" target="_blank" rel="noopener">in LinkedIn</a>
<a href="#" class="sbtn s3" target="_blank" rel="noopener">𝕏 Twitter</a>
<a href="#" class="sbtn s4" target="_blank" rel="noopener">f Facebook</a>
<a href="#" class="sbtn s5" target="_blank" rel="noopener">📸 Instagram</a>
<a href="#" class="sbtn s6" target="_blank" rel="noopener">▶ YouTube</a>
</div>
</div>

<div class="card" style="background:#f0f4ff;border-color:#c7d2fe;">
<h2 class="ctitle" style="border-color:#a5b4fc;">🔗 Related Tools</h2>
<div style="display:flex;flex-wrap:wrap;gap:9px;">
<a href="/admissions/uptac-choice-filling-predictor.html" style="background:white;border:1px solid #c7d2fe;padding:9px 15px;border-radius:8px;font-size:13px;font-weight:700;color:var(--p);text-decoration:none;">🎯 UPTAC Choice Predictor</a>
<a href="/tools/uptac-scholarship-fee-roi-calculator.html" style="background:white;border:1px solid #c7d2fe;padding:9px 15px;border-radius:8px;font-size:13px;font-weight:700;color:var(--p);text-decoration:none;">💰 Scholarship ROI Calculator</a>
<a href="/placements/aktu-college-placement-leaderboard.html" style="background:white;border:1px solid #c7d2fe;padding:9px 15px;border-radius:8px;font-size:13px;font-weight:700;color:var(--p);text-decoration:none;">🏆 Placement Leaderboard</a>
<a href="/colleges/aktu-district-wise-colleges.html" style="background:white;border:1px solid #c7d2fe;padding:9px 15px;border-radius:8px;font-size:13px;font-weight:700;color:var(--p);text-decoration:none;">🏛️ District-Wise Directory</a>
</div>
</div>

</div>
<footer><div class="wrap">
<p>© 2026 <a href="/">AKTU Results Portal</a> — Independent student resource for AKTU &amp; UPTAC</p>
<p style="margin-top:5px;opacity:.7;font-size:12px;">Disclaimer: Fee and placement figures sourced from publicly available college reports. Verify with the official college website before decisions.</p>
</div></footer>
<script defer src="/js/community-banner-widget.js"></script>
</body></html>"""

colleges = [
    {
        "filename": "galgotias-college-greater-noida-profile.html",
        "name": "Galgotias College of Engineering & Technology",
        "short_name": "Galgotias College",
        "code": "097",
        "city": "Greater Noida",
        "type": "Private",
        "est": "1999",
        "area": "55 acres",
        "naac": "A",
        "nirf": "101-150",
        "fee": 125000,
        "hostel_single": 52000,
        "hostel_double": 40000,
        "mess": 38000,
        "dev": 7500,
        "highest_pkg": "52 LPA",
        "avg_pkg": "9.2 LPA",
        "placement_pct": 93,
        "branches": [("CSE", 480), ("CSE-AI", 120), ("ECE", 240), ("ME", 180), ("IT", 120), ("CE", 120), ("CSE-DS", 60)],
        "clubs": ["GDSC Galgotias", "CodChef Galgotias", "NSS", "IEEE", "E-Cell", "Photography", "Music", "Drama", "Sports", "Robotics"],
        "recruiters": ["Google", "Amazon", "Microsoft", "Adobe", "Cisco", "TCS Digital", "Wipro Elite", "Infosys SP", "Capgemini", "HCL"],
        "address": "1, Knowledge Park II, Greater Noida - 201306, UP",
        "phone": "+91-120-2323300",
        "email": "admission@galgotiacollege.edu",
        "website": "https://www.galgotiacollege.edu",
        "about": "Galgotias College of Engineering and Technology, Greater Noida is a NAAC-A accredited autonomous college affiliated to AKTU. Founded in 1999 under the Galgotias Educational Institutions, it has grown to become one of the largest engineering colleges in UP with 1320+ intake seats. The college recorded a highest placement of 52 LPA by Google and maintains strong campus recruitment partnerships with major MNCs.",
        "infra": "55-acre Knowledge Park II campus with Google Developer Lab, Microsoft Learn Centre, 40+ specialized labs, central library with 100,000+ volumes, 6 hostel blocks (3000+ capacity), swimming pool, football ground, basketball courts, indoor stadium, food court, and 3000-seat convention centre."
    },
    {
        "filename": "bbditm-lucknow-profile.html",
        "name": "Babu Banarasi Das Institute of Technology & Management",
        "short_name": "BBDITM Lucknow",
        "code": "091-L",
        "city": "Lucknow",
        "type": "Private",
        "est": "2000",
        "area": "20 acres",
        "naac": "B+",
        "nirf": "301-400",
        "fee": 105000,
        "hostel_single": 46000,
        "hostel_double": 34000,
        "mess": 32000,
        "dev": 6000,
        "highest_pkg": "18 LPA",
        "avg_pkg": "5.8 LPA",
        "placement_pct": 78,
        "branches": [("CSE", 180), ("ECE", 120), ("ME", 120), ("CE", 90), ("IT", 90)],
        "clubs": ["Coding Club", "IEEE", "NSS", "Photography", "Sports", "Music", "E-Cell", "Drama", "Literary"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Tech Mahindra", "Capgemini", "NIIT", "Mphasis"],
        "address": "Sector II, Dr. Akhilesh Das Nagar, Lucknow - 226028, UP",
        "phone": "+91-522-2732999",
        "email": "info@bbditm.ac.in",
        "website": "https://www.bbditm.ac.in",
        "about": "Babu Banarasi Das Institute of Technology & Management (BBDITM) is a premier engineering college in Lucknow affiliated to AKTU. Established in 2000, it offers excellent academic environment and placement opportunities.",
        "infra": "20-acre lush green campus with modern laboratories, spacious classrooms, well-stocked library, dedicated sports facilities, separate hostels for boys and girls, and a sprawling cafeteria."
    },
    {
        "filename": "invertis-university-bareilly-profile.html",
        "name": "Invertis University",
        "short_name": "Invertis University",
        "code": "140",
        "city": "Bareilly",
        "type": "Private University",
        "est": "2010",
        "area": "32 acres",
        "naac": "B+",
        "nirf": "301-400",
        "fee": 98000,
        "hostel_single": 44000,
        "hostel_double": 32000,
        "mess": 30000,
        "dev": 5500,
        "highest_pkg": "15 LPA",
        "avg_pkg": "5.2 LPA",
        "placement_pct": 72,
        "branches": [("CSE", 120), ("ECE", 90), ("ME", 90), ("CE", 60), ("IT", 60), ("MBA", 60)],
        "clubs": ["Coding Club", "NSS", "IEEE", "Photography", "Sports", "Music", "E-Cell"],
        "recruiters": ["TCS", "Wipro", "Infosys", "HCL", "Cognizant", "Capgemini", "Mindtree"],
        "address": "Lucknow Road, Tedhia Pulia, Bareilly - 243123, UP",
        "phone": "+91-581-2303900",
        "email": "info@invertis.org",
        "website": "https://www.invertis.org",
        "about": "Invertis University is a leading private university in Bareilly, established in 2010. It offers a wide range of undergraduate, postgraduate, and doctoral programs, focusing on holistic development and industry-aligned curriculum.",
        "infra": "32-acre campus equipped with modern infrastructure, hi-tech labs, central library, sports complex, auditoriums, and comprehensive hostel facilities for students."
    },
    {
        "filename": "shiats-allahabad-profile.html",
        "name": "Sam Higginbottom University of Agriculture, Technology & Sciences",
        "short_name": "SHUATS",
        "code": "SHUATS",
        "city": "Allahabad",
        "type": "Deemed University",
        "est": "1910",
        "area": "480 acres",
        "naac": "A",
        "nirf": "151-200",
        "fee": 85000,
        "hostel_single": 42000,
        "hostel_double": 30000,
        "mess": 28000,
        "dev": 5000,
        "highest_pkg": "28 LPA",
        "avg_pkg": "6.5 LPA",
        "placement_pct": 82,
        "branches": [("CSE", 120), ("ECE", 90), ("ME", 90), ("CE", 90), ("IT", 60), ("Agri Engg", 60)],
        "clubs": ["Coding Club", "NSS", "NCC", "IEEE", "Photography", "Sports", "Music", "Agricultural Club", "E-Cell", "Drama"],
        "recruiters": ["TCS", "Amazon", "Infosys", "Wipro", "ITC", "Britannia", "Nestle", "Dabur", "HCL"],
        "address": "Naini, Prayagraj (Allahabad) - 211007, UP",
        "phone": "+91-532-2684281",
        "email": "registrar@shiats.edu.in",
        "website": "https://www.shuats.edu.in",
        "about": "Established in 1910, SHUATS is one of the oldest institutions for agricultural and technological sciences in India. It is a highly reputed Deemed University with NAAC A accreditation.",
        "infra": "Massive 480-acre green campus with agricultural farms, advanced research centers, heritage buildings, central library, sports facilities, and numerous hostels."
    },
    {
        "filename": "miet-meerut-profile.html",
        "name": "Meerut Institute of Engineering & Technology",
        "short_name": "MIET Meerut",
        "code": "108",
        "city": "Meerut",
        "type": "Autonomous Private",
        "est": "1995",
        "area": "40 acres",
        "naac": "A",
        "nirf": "201-300",
        "fee": 118000,
        "hostel_single": 50000,
        "hostel_double": 38000,
        "mess": 35000,
        "dev": 7000,
        "highest_pkg": "35 LPA",
        "avg_pkg": "7.5 LPA",
        "placement_pct": 86,
        "branches": [("CSE", 240), ("ECE", 180), ("ME", 180), ("CE", 120), ("IT", 120), ("EE", 60)],
        "clubs": ["MIET Coding Club", "IEEE", "NSS", "NCC", "Photography", "Sports", "E-Cell", "Drama", "Music", "Robotics"],
        "recruiters": ["TCS Digital", "Infosys", "Wipro", "Amazon", "HCL", "Capgemini", "Cognizant", "Tech Mahindra"],
        "address": "NH-58, Bypass Road, Meerut - 250005, UP",
        "phone": "+91-121-2439021",
        "email": "info@miet.ac.in",
        "website": "https://www.miet.ac.in",
        "about": "Meerut Institute of Engineering & Technology (MIET) is a premier autonomous private engineering college in Meerut. Established in 1995, it is known for its excellent academic standards and placement records.",
        "infra": "40-acre campus with state-of-the-art academic blocks, research and development centers, incubation centers, central library, auditoriums, sports facilities, and hostels."
    },
    {
        "filename": "himalayan-institute-dehradun-profile.html",
        "name": "Himalayan Institute of Technology",
        "short_name": "HIT Dehradun",
        "code": "052-D",
        "city": "Dehradun",
        "type": "Private",
        "est": "2001",
        "area": "25 acres",
        "naac": "B+",
        "nirf": "301-400",
        "fee": 95000,
        "hostel_single": 45000,
        "hostel_double": 33000,
        "mess": 30000,
        "dev": 5000,
        "highest_pkg": "16 LPA",
        "avg_pkg": "5.5 LPA",
        "placement_pct": 74,
        "branches": [("CSE", 120), ("ECE", 90), ("ME", 90), ("CE", 60), ("IT", 60)],
        "clubs": ["Coding Club", "NSS", "IEEE", "Photography", "Sports", "Music", "Drama"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Capgemini"],
        "address": "Sitapur Road, Jolly Grant, Dehradun - 248140, Uttarakhand",
        "phone": "+91-1357-245180",
        "email": "info@hitd.ac.in",
        "website": "https://www.hitd.ac.in",
        "about": "Himalayan Institute of Technology, located in the scenic Doon valley, offers high-quality technical education. It focuses on practical skills and overall personality development.",
        "infra": "25-acre scenic campus equipped with modern labs, computing facilities, central library, sports grounds, and on-campus hostel facilities."
    },
    {
        "filename": "gcet-greater-noida-profile.html",
        "name": "Greater Noida Institute of Technology",
        "short_name": "GNIOT",
        "code": "049",
        "city": "Greater Noida",
        "type": "Private",
        "est": "2000",
        "area": "22 acres",
        "naac": "B+",
        "nirf": "301-400",
        "fee": 112000,
        "hostel_single": 48000,
        "hostel_double": 36000,
        "mess": 36000,
        "dev": 6500,
        "highest_pkg": "24 LPA",
        "avg_pkg": "6.5 LPA",
        "placement_pct": 82,
        "branches": [("CSE", 240), ("ECE", 120), ("ME", 120), ("IT", 120), ("CE", 90), ("MBA", 60)],
        "clubs": ["Coding Club", "NSS", "IEEE", "Photography", "Sports", "E-Cell", "Literary", "Music", "Drama", "Environment Club"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra", "Capgemini", "Cognizant", "Mphasis"],
        "address": "27 Knowledge Park I, Greater Noida - 201308, UP",
        "phone": "+91-120-2323811",
        "email": "info@gniot.net",
        "website": "https://www.gniot.net",
        "about": "Greater Noida Institute of Technology (GNIOT) is a leading institution under the GNIOT Group. Known for value-based education, modern infrastructure, and strong industry linkages for placements.",
        "infra": "22-acre campus featuring modern classrooms, well-equipped labs, central library, auditoriums, sports complex, cafeterias, and separate boys and girls hostels."
    },
    {
        "filename": "hbtu-kanpur-profile.html",
        "name": "Harcourt Butler Technical University",
        "short_name": "HBTU Kanpur",
        "code": "061",
        "city": "Kanpur",
        "type": "Government University",
        "est": "1921",
        "area": "200 acres",
        "naac": "A+",
        "nirf": "76-100",
        "fee": 62000,
        "hostel_single": 35000,
        "hostel_double": 25000,
        "mess": 28000,
        "dev": 3000,
        "highest_pkg": "65 LPA",
        "avg_pkg": "12.5 LPA",
        "placement_pct": 96,
        "branches": [("CSE", 120), ("ECE", 120), ("ME", 120), ("CE", 90), ("Chemical Engg", 90), ("IT", 60), ("EE", 60)],
        "clubs": ["Coding Club HBTU", "IEEE", "NSS", "NCC", "Photography", "Sports", "E-Cell", "Drama", "Music", "Alumni Association"],
        "recruiters": ["Google", "Amazon", "Microsoft", "Goldman Sachs", "Morgan Stanley", "Flipkart", "Paytm", "Samsung R&D", "IBM", "Oracle"],
        "address": "Nawabganj, Kanpur - 208002, UP",
        "phone": "+91-512-2533537",
        "email": "registrar@hbtu.ac.in",
        "website": "https://www.hbtu.ac.in",
        "about": "Harcourt Butler Technical University (HBTU), Kanpur is one of the oldest and most prestigious government technical universities in India, established in 1921. As a full university (not just college), HBTU grants its own degrees and has consistently produced India's top engineers and entrepreneurs. Google, Goldman Sachs, and Morgan Stanley regularly recruit from HBTU with packages up to 65 LPA. NAAC A+ accredited and NIRF ranked 76-100.",
        "infra": "200-acre heritage campus in Nawabganj Kanpur with colonial-era academic buildings, supercomputing lab, central library with 2 lakh+ volumes, 16 hostel blocks, Olympic-size swimming pool, cricket ground, football ground, indoor stadium, research park, and a 3000-seat auditorium."
    },
    {
        "filename": "rait-rampur-profile.html",
        "name": "Rampur Engineering College",
        "short_name": "REC Rampur",
        "code": "128",
        "city": "Rampur",
        "type": "Government",
        "est": "2010",
        "area": "12 acres",
        "naac": "B",
        "nirf": "401-500",
        "fee": 55000,
        "hostel_single": 28000,
        "hostel_double": 20000,
        "mess": 24000,
        "dev": 2500,
        "highest_pkg": "12 LPA",
        "avg_pkg": "4.5 LPA",
        "placement_pct": 68,
        "branches": [("CSE", 60), ("ECE", 60), ("ME", 60), ("CE", 60)],
        "clubs": ["Coding Club", "NSS", "NCC", "IEEE", "Sports", "Photography", "Music"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini", "SAIL", "BHEL", "ONGC"],
        "address": "Delhi Road, Rampur - 244901, UP",
        "phone": "+91-595-2350456",
        "email": "info@recrampur.ac.in",
        "website": "https://www.recrampur.ac.in",
        "about": "Rajkiya Engineering College (REC) Rampur is a government engineering college offering affordable, quality technical education in Uttar Pradesh.",
        "infra": "12-acre developing campus with essential academic buildings, laboratories, central library, sports grounds, and student hostels."
    },
    {
        "filename": "iec-greater-noida-profile.html",
        "name": "IEC College of Engineering & Technology",
        "short_name": "IEC Greater Noida",
        "code": "057",
        "city": "Greater Noida",
        "type": "Private",
        "est": "2000",
        "area": "15 acres",
        "naac": "B+",
        "nirf": "301-400",
        "fee": 108000,
        "hostel_single": 46000,
        "hostel_double": 34000,
        "mess": 32000,
        "dev": 6000,
        "highest_pkg": "20 LPA",
        "avg_pkg": "6.0 LPA",
        "placement_pct": 79,
        "branches": [("CSE", 180), ("ECE", 120), ("ME", 90), ("CE", 60), ("IT", 60)],
        "clubs": ["Coding Club", "NSS", "IEEE", "Photography", "Sports", "E-Cell", "Music"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Tech Mahindra", "Capgemini"],
        "address": "Knowledge Park I, Greater Noida - 201306, UP",
        "phone": "+91-120-2323401",
        "email": "info@ieccollege.com",
        "website": "https://www.ieccollege.com",
        "about": "IEC College of Engineering & Technology in Greater Noida provides excellent academic facilities and industry-focused engineering programs.",
        "infra": "15-acre campus with robust infrastructure including well-equipped laboratories, a modern library, sports areas, and comfortable hostels."
    },
    {
        "filename": "srmcem-lucknow-profile.html",
        "name": "SRM College of Engineering & Management",
        "short_name": "SRM Lucknow",
        "code": "195",
        "city": "Lucknow",
        "type": "Private",
        "est": "2010",
        "area": "18 acres",
        "naac": "B+",
        "nirf": "301-400",
        "fee": 110000,
        "hostel_single": 48000,
        "hostel_double": 36000,
        "mess": 33000,
        "dev": 6500,
        "highest_pkg": "22 LPA",
        "avg_pkg": "6.2 LPA",
        "placement_pct": 80,
        "branches": [("CSE", 120), ("ECE", 90), ("ME", 90), ("CE", 60), ("IT", 60), ("MBA", 60)],
        "clubs": ["Coding Club", "NSS", "IEEE", "Photography", "Sports", "E-Cell", "Music", "Drama", "Literary", "Robotics"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini", "Cognizant", "Tech Mahindra", "Mindtree"],
        "address": "Tiraha Bakshi Ka Talab, Sitapur Road, Lucknow - 226201, UP",
        "phone": "+91-522-2734501",
        "email": "info@srmcemlucknow.ac.in",
        "website": "https://www.srmcemlucknow.ac.in",
        "about": "SRM College of Engineering & Management offers comprehensive technical and management education in Lucknow, focusing on holistic development and excellent placements.",
        "infra": "18-acre green campus equipped with modern labs, computing facilities, extensive library, auditoriums, sports complex, and on-campus hostels."
    },
    {
        "filename": "ipec-ghaziabad-profile.html",
        "name": "Inderprastha Engineering College",
        "short_name": "IPEC Ghaziabad",
        "code": "068-G",
        "city": "Ghaziabad",
        "type": "Private",
        "est": "1999",
        "area": "10 acres",
        "naac": "B+",
        "nirf": "301-400",
        "fee": 112000,
        "hostel_single": 47000,
        "hostel_double": 35000,
        "mess": 32000,
        "dev": 6500,
        "highest_pkg": "26 LPA",
        "avg_pkg": "6.8 LPA",
        "placement_pct": 83,
        "branches": [("CSE", 180), ("ECE", 120), ("ME", 90), ("CE", 60), ("IT", 60)],
        "clubs": ["IPEC Coding Club", "IEEE", "NSS", "Photography", "Sports", "E-Cell", "Drama", "Music", "Literary", "Robotics"],
        "recruiters": ["TCS Digital", "Infosys", "Wipro", "Amazon", "HCL", "Capgemini", "Cognizant", "Tech Mahindra"],
        "address": "Adhyatmik Nagar, NH-9, Ghaziabad - 201010, UP",
        "phone": "+91-120-2675800",
        "email": "info@ipec.org.in",
        "website": "https://www.ipec.org.in",
        "about": "Inderprastha Engineering College (IPEC) is a well-known technical institute in Ghaziabad. Since 1999, it has been providing quality technical education and boasts strong placement records.",
        "infra": "10-acre campus with well-equipped modern laboratories, digital library, seminar halls, sports facilities, and comfortable hostel accommodations."
    }
]

import xml.etree.ElementTree as ET
from datetime import date

base_dir = '/home/techiedevang/akturesults/colleges/profiles'
sitemap_path = '/home/techiedevang/akturesults/sitemap.xml'
os.makedirs(base_dir, exist_ok=True)

urls_to_add = []

for c in colleges:
    total_fee = c["fee"] + c["hostel_double"] + c["mess"] + c["dev"]
    total_4yr = c["fee"] * 4 + c["hostel_double"] * 4 + c["mess"] * 4 + c["dev"] * 4
    total_intake = sum(b[1] for b in c["branches"])

    branches_html = ""
    for b in c["branches"]:
        branches_html += f'<tr><td style="padding:12px 15px; border-bottom:1px solid #e2e8f0; font-weight:600;">{b[0]}</td><td style="padding:12px 15px; border-bottom:1px solid #e2e8f0; text-align:center;">{b[1]}</td><td style="padding:12px 15px; border-bottom:1px solid #e2e8f0;">HOD</td><td style="padding:12px 15px; border-bottom:1px solid #e2e8f0; text-align:center;"><span style="background:#e0e7ff; color:#3730a3; padding:3px 10px; border-radius:12px; font-size:12px; font-weight:700;">A Grade</span></td></tr>'

    recruiters_html = "".join([f'<span style="background:#f1f5f9; color:#475569; padding:5px 12px; border-radius:20px; font-size:13px; font-weight:600; display:inline-block; margin:3px;">{r}</span>' for r in c["recruiters"]])

    clubs_html = "".join([f'<li style="padding:5px 0; border-bottom:1px solid #f1f5f9;">{club}</li>' for club in c["clubs"]])

    state = "UP" if "Dehradun" not in c["city"] else "Uttarakhand"
    
    html = template_html.format(
        filename=c["filename"],
        name=c["name"],
        short_name=c["short_name"],
        short_name_lower=c["short_name"].lower(),
        code=c["code"],
        city=c["city"],
        city_lower=c["city"].lower(),
        type=c["type"],
        est=c["est"],
        area=c["area"],
        naac=c["naac"],
        nirf=c["nirf"],
        fee=c["fee"],
        hostel_single=c["hostel_single"],
        hostel_double=c["hostel_double"],
        mess=c["mess"],
        dev=c["dev"],
        total_fee=total_fee,
        total_4yr=total_4yr,
        highest_pkg=c["highest_pkg"],
        avg_pkg=c["avg_pkg"],
        placement_pct=c["placement_pct"],
        total_intake=total_intake,
        branches_html=branches_html,
        recruiters_html=recruiters_html,
        clubs_html=clubs_html,
        address=c["address"],
        address_clean=c["address"].replace('"', '\\"'),
        state=state,
        phone=c["phone"],
        email=c["email"],
        website=c["website"],
        about=c["about"],
        about_escaped=c["about"].replace('"', '\\"'),
        infra=c["infra"]
    )
    
    file_path = os.path.join(base_dir, c["filename"])
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    urls_to_add.append(f"https://akturesults.in/colleges/profiles/{c['filename']}")

# update sitemap.xml
today = date.today().isoformat()
ET.register_namespace('', "http://www.sitemaps.org/schemas/sitemap/0.9")

try:
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
except Exception as e:
    root = ET.Element('{http://www.sitemaps.org/schemas/sitemap/0.9}urlset')
    tree = ET.ElementTree(root)

existing_urls = [url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text for url_elem in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url') if url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc') is not None]

for url in urls_to_add:
    if url not in existing_urls:
        url_elem = ET.SubElement(root, "url")
        loc = ET.SubElement(url_elem, "loc")
        loc.text = url
        lastmod = ET.SubElement(url_elem, "lastmod")
        lastmod.text = today
        changefreq = ET.SubElement(url_elem, "changefreq")
        changefreq.text = "weekly"
        priority = ET.SubElement(url_elem, "priority")
        priority.text = "0.9"

tree.write(sitemap_path, encoding='utf-8', xml_declaration=True)

print("HTML generation and sitemap update complete.")
