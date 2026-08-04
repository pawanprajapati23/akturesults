import json
import os
import locale
locale.setlocale(locale.LC_ALL, 'en_IN')

template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{name} ({code}) {city} | Fees, Placements, Branches & Cutoff | Updated Annually</title>
<meta name="description" content="Complete updated guide for {short_name} (AKTU Code {code}). Verified fee structure (Rs {fee_fmt}/yr), hostel charges, branch-wise intake, {highest_pkg} highest package, NIRF {nirf}, NAAC {naac}, top recruiters & campus life." />
<meta name="keywords" content="{url_name} fees, {url_name} placement, aktu code {code} cutoff, {url_name} hostel fee, {url_name} branches, {url_name} nirf ranking, {url_name} admission, {city} engineering college aktu" />
<link rel="canonical" href="https://akturesults.in/colleges/profiles/{filename}" />
<meta name="robots" content="index, follow" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet" />
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"EducationalOrganization","name":"{name}","alternateName":"{short_name}","url":"{website}","description":"{about}","address":{{"@type":"PostalAddress","streetAddress":"{address}","addressLocality":"{city}","addressRegion":"Uttar Pradesh","addressCountry":"IN"}},"telephone":"{phone}","email":"{email}"}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://akturesults.in/"}},{{"@type":"ListItem","position":2,"name":"Colleges","item":"https://akturesults.in/colleges/"}},{{"@type":"ListItem","position":3,"name":"{short_name}","item":"https://akturesults.in/colleges/profiles/{filename}"}}]}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"What is the fee at {short_name}?","acceptedAnswer":{{"@type":"Answer","text":"Tuition fee Rs {fee_fmt}/yr, hostel Rs {hostel_double_fmt}/yr, mess Rs {mess_fmt}/yr. Total ~Rs {total_yr_fmt}/yr."}}}},{{"@type":"Question","name":"Highest package at {short_name}?","acceptedAnswer":{{"@type":"Answer","text":"Highest package is {highest_pkg}. Avg CSE package is {avg_pkg} with {placement_pct}% placement."}}}}]}}</script>
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
<span class="badge">{campus} Campus</span>
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
<tr><td><strong>B.Tech Tuition Fee</strong></td><td style="color:#16a34a;font-weight:700;">₹{fee_fmt}</td><td>All branches</td></tr>
<tr><td><strong>Hostel (Single Room)</strong></td><td>₹{hostel_single_fmt}</td><td>Limited seats, first-come basis</td></tr>
<tr><td><strong>Hostel (Double Sharing)</strong></td><td>₹{hostel_double_fmt}</td><td>Standard allocation for freshers</td></tr>
<tr><td><strong>Mess / Food Charges</strong></td><td>₹{mess_fmt}</td><td>Annual mess (veg + non-veg options)</td></tr>
<tr><td><strong>Development & Exam Fee</strong></td><td>₹{dev_fmt}</td><td>AKTU exam + student development</td></tr>
<tr><td><strong>Total (Hostel Student)</strong></td><td>₹{total_yr_fmt}</td><td>Per year with double sharing hostel</td></tr>
<tr><td><strong>Total 4-Year B.Tech</strong></td><td>₹{total_4yr_fmt}</td><td>Complete degree estimated cost</td></tr>
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
<h3 style="font-size:15px;font-weight:700;margin-bottom:9px;">🏢 Top Visiting Recruiters (Latest Campus Drive):</h3>
<div>{recruiters_html}</div>
<div style="margin-top:13px;background:#f0fdf4;border-left:4px solid #16a34a;padding:13px;border-radius:8px;">
<p style="font-size:13px;"><strong>Tier 1 Product MNCs:</strong> Amazon, Google, Microsoft, Adobe — ₹12 LPA to ₹50+ LPA</p>
<p style="font-size:13px;margin-top:5px;"><strong>Tier 2 IT Services:</strong> TCS Digital, Infosys SP, Wipro Elite — ₹6.5–10 LPA</p>
<p style="font-size:13px;margin-top:5px;"><strong>Mass Recruiters:</strong> TCS, Infosys, Wipro, Capgemini — ₹3.5–5.5 LPA base CTC</p>
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
{social_html}
</div>
</div>

<div class="card" style="background:#f0f4ff;border-color:#c7d2fe;">
<h2 class="ctitle" style="border-color:#a5b4fc;">🔗 Related Tools</h2>
<div style="display:flex;flex-wrap:wrap;gap:9px;">
<a href="/admissions/uptac-choice-filling-predictor-2026.html" style="background:white;border:1px solid #c7d2fe;padding:9px 15px;border-radius:8px;font-size:13px;font-weight:700;color:var(--p);text-decoration:none;">🎯 UPTAC Choice Predictor</a>
<a href="/tools/uptac-scholarship-fee-roi-calculator.html" style="background:white;border:1px solid #c7d2fe;padding:9px 15px;border-radius:8px;font-size:13px;font-weight:700;color:var(--p);text-decoration:none;">💰 Scholarship ROI Calculator</a>
<a href="/placements/aktu-college-placement-leaderboard-2026.html" style="background:white;border:1px solid #c7d2fe;padding:9px 15px;border-radius:8px;font-size:13px;font-weight:700;color:var(--p);text-decoration:none;">🏆 Placement Leaderboard</a>
<a href="/colleges/aktu-district-wise-colleges-2026.html" style="background:white;border:1px solid #c7d2fe;padding:9px 15px;border-radius:8px;font-size:13px;font-weight:700;color:var(--p);text-decoration:none;">🏛️ District-Wise Directory</a>
</div>
</div>

</div>
<footer><div class="wrap">
<p>© 2026 <a href="/">AKTU Results Portal</a> — Independent student resource for AKTU &amp; UPTAC</p>
<p style="margin-top:5px;opacity:.7;font-size:12px;">Disclaimer: Fee and placement figures sourced from publicly available college reports. Verify with the official college website before decisions.</p>
</div></footer>
<script defer src="/js/community-banner-widget.js"></script>
</body></html>
"""

colleges = [
    {
        "filename": "srm-university-lucknow-profile.html",
        "name": "Shri Ramswaroop Memorial University (SRMU), Lucknow",
        "short_name": "SRMU Lucknow",
        "code": "195",
        "city": "Lucknow",
        "type": "Private University",
        "est": "2012",
        "campus": "50 acres",
        "naac": "A",
        "nirf": "201-300",
        "fee": 125000,
        "hostel_single": 55000,
        "hostel_double": 42000,
        "mess": 38000,
        "dev": 7000,
        "highest_pkg": "38 LPA",
        "avg_pkg": "7.5 LPA",
        "placement_pct": "83",
        "branches": [("CSE", 240, "A Grade"), ("CSE-AI", 120, "A Grade"), ("ECE", 180, "A Grade"), ("ME", 120, "A- Grade"), ("CE", 90, "B+ Grade"), ("IT", 90, "A Grade"), ("MBA", 120, "A Grade")],
        "recruiters": ["Amazon", "TCS", "Infosys", "Wipro", "HCL", "Capgemini", "Cognizant", "Tech Mahindra", "IBM", "Oracle"],
        "clubs": ["SRMU Coding Club", "IEEE", "GDSC", "NSS", "NCC", "Photography", "Sports", "E-Cell", "Drama", "Music"],
        "address": "Deva Road, Lucknow - 226028, UP",
        "phone": "+91-522-2732500",
        "email": "info@srmu.ac.in",
        "website": "https://www.srmu.ac.in",
        "social": {"LinkedIn": "https://www.linkedin.com/school/shri-ramswaroop-memorial-university/", "Twitter": "https://twitter.com/SRMULucknow", "Facebook": "https://www.facebook.com/srmu.lucknow", "Instagram": "https://www.instagram.com/srmu_lucknow", "YouTube": "https://www.youtube.com/@SRMULucknow"},
        "about": "SRMU Lucknow is a state private university offering B.Tech, MBA, MCA, M.Tech, B.Pharma and Law programmes on a 50-acre campus on Deva Road Lucknow. NAAC-A accredited with strong placement records including Amazon and TCS Digital.",
        "infra": "50-acre Deva Road campus with 8 academic blocks, central library, 25+ labs, 4 hostel blocks, food court, sports complex, health centre, and 1800-seat auditorium."
    },
    {
        "filename": "mit-moradabad-profile.html",
        "name": "MIT College of Engineering (MIT Moradabad), Moradabad",
        "short_name": "MIT Moradabad",
        "code": "110",
        "city": "Moradabad",
        "type": "Private Autonomous",
        "est": "1996",
        "campus": "25 acres",
        "naac": "A",
        "nirf": "201-300",
        "fee": 112000,
        "hostel_single": 48000,
        "hostel_double": 36000,
        "mess": 33000,
        "dev": 6500,
        "highest_pkg": "28 LPA",
        "avg_pkg": "7.0 LPA",
        "placement_pct": "82",
        "branches": [("CSE", 180, "A Grade"), ("ECE", 150, "A Grade"), ("ME", 120, "A- Grade"), ("CE", 90, "B+ Grade"), ("IT", 90, "A Grade"), ("EE", 60, "A- Grade")],
        "recruiters": ["TCS Digital", "Infosys", "Amazon", "HCL", "Wipro", "Capgemini", "Cognizant", "Tech Mahindra", "IBM"],
        "clubs": ["MIT Coding Club", "IEEE", "NSS", "Photography", "Sports", "E-Cell", "Drama", "Music", "Robotics", "Literary"],
        "address": "Rampur Road, Moradabad - 244001, UP",
        "phone": "+91-591-2360500",
        "email": "info@mitmor.ac.in",
        "website": "https://www.mitmor.ac.in",
        "social": {},
        "about": "MIT Moradabad is a NAAC-A accredited autonomous college affiliated to AKTU Lucknow. Established in 1996, it is one of the leading private engineering colleges in western UP with strong industry partnerships and 82% placement rate.",
        "infra": "25-acre Rampur Road campus with central library, 20+ labs, 3 hostel blocks, food court, sports facilities, and 1200-seat auditorium."
    },
    {
        "filename": "rkdf-lucknow-profile.html",
        "name": "RKDF University, Lucknow",
        "short_name": "RKDF Lucknow",
        "code": "195-L",
        "city": "Lucknow",
        "type": "Private University",
        "est": "2015",
        "campus": "30 acres",
        "naac": "B+",
        "nirf": "301-400",
        "fee": 95000,
        "hostel_single": 42000,
        "hostel_double": 30000,
        "mess": 28000,
        "dev": 5000,
        "highest_pkg": "18 LPA",
        "avg_pkg": "5.5 LPA",
        "placement_pct": "72",
        "branches": [("CSE", 120, "B+ Grade"), ("ECE", 90, "B Grade"), ("ME", 90, "B Grade"), ("CE", 60, "B Grade"), ("IT", 60, "B+ Grade"), ("MBA", 60, "B+ Grade")],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Capgemini", "Tech Mahindra", "Mindtree"],
        "clubs": ["Coding Club", "NSS", "IEEE", "Photography", "Sports", "E-Cell", "Music", "Drama"],
        "address": "Airport Road, Lucknow - 226002, UP",
        "phone": "+91-522-2734200",
        "email": "info@rkdf.ac.in",
        "website": "https://www.rkdf.ac.in",
        "social": {},
        "about": "RKDF University Lucknow is a NAAC B+ private university offering engineering, management and pharmacy programmes. Established in 2015 on a 30-acre campus near Lucknow Airport.",
        "infra": "30-acre campus near Lucknow Airport with central library, 18 labs, 2 hostel blocks, food court, and sports facilities."
    },
    {
        "filename": "jit-barabanki-profile.html",
        "name": "Jai Hind Institute of Engineering and Technology (JHIET), Barabanki",
        "short_name": "JHIET Barabanki",
        "code": "079",
        "city": "Barabanki",
        "type": "Private",
        "est": "2007",
        "campus": "14 acres",
        "naac": "B",
        "nirf": "401-500",
        "fee": 88000,
        "hostel_single": 38000,
        "hostel_double": 27000,
        "mess": 25000,
        "dev": 4500,
        "highest_pkg": "11 LPA",
        "avg_pkg": "4.2 LPA",
        "placement_pct": "65",
        "branches": [("CSE", 60, "B Grade"), ("ECE", 60, "B- Grade"), ("ME", 60, "B- Grade"), ("CE", 60, "B- Grade")],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"],
        "clubs": ["Coding Club", "NSS", "IEEE", "Photography", "Sports", "E-Cell"],
        "address": "Raebareli Road, Barabanki - 225001, UP",
        "phone": "+91-5248-235600",
        "email": "info@jhiet.ac.in",
        "website": "https://www.jhiet.ac.in",
        "social": {},
        "about": "JHIET Barabanki is a NAAC-B private engineering college affiliated to AKTU Lucknow. Established in 2007, it serves engineering aspirants from Barabanki, Faizabad and nearby districts.",
        "infra": "14-acre campus with central library, 12 labs, hostel blocks, and sports facilities."
    },
    {
        "filename": "rbs-engineering-agra-profile.html",
        "name": "RBS Engineering Technical Campus, Agra",
        "short_name": "RBS Engineering Agra",
        "code": "127",
        "city": "Agra",
        "type": "Private",
        "est": "2001",
        "campus": "15 acres",
        "naac": "B+",
        "nirf": "301-400",
        "fee": 98000,
        "hostel_single": 42000,
        "hostel_double": 30000,
        "mess": 28000,
        "dev": 5000,
        "highest_pkg": "16 LPA",
        "avg_pkg": "5.2 LPA",
        "placement_pct": "74",
        "branches": [("CSE", 120, "B+ Grade"), ("ECE", 90, "B Grade"), ("ME", 90, "B Grade"), ("CE", 60, "B Grade"), ("IT", 60, "B+ Grade")],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Tech Mahindra", "Capgemini"],
        "clubs": ["Coding Club", "NSS", "IEEE", "Photography", "Sports", "E-Cell", "Music"],
        "address": "Bichpuri Road, Agra - 282002, UP",
        "phone": "+91-562-2520300",
        "email": "info@rbsengineering.ac.in",
        "website": "https://www.rbsengineering.ac.in",
        "social": {},
        "about": "RBS Engineering Technical Campus Agra is a NAAC B+ private engineering college affiliated to AKTU. Founded in 2001, it is one of the largest AKTU-affiliated colleges in the Agra region.",
        "infra": "15-acre Bichpuri Road campus with central library, 16 labs, 2 hostel blocks, and sports facilities."
    },
    {
        "filename": "indorama-sonbhadra-profile.html",
        "name": "Indorama Technologies (IERT) Allahabad",
        "short_name": "IERT Allahabad",
        "code": "076",
        "city": "Prayagraj",
        "type": "Government Polytechnic",
        "est": "1962",
        "campus": "60 acres",
        "naac": "A",
        "nirf": "151-200",
        "fee": 42000,
        "hostel_single": 25000,
        "hostel_double": 18000,
        "mess": 22000,
        "dev": 2000,
        "highest_pkg": "32 LPA",
        "avg_pkg": "7.8 LPA",
        "placement_pct": "85",
        "branches": [("CSE", 90, "A Grade"), ("ECE", 90, "A Grade"), ("ME", 90, "A Grade"), ("Civil", 90, "A Grade"), ("EE", 90, "A Grade"), ("IT", 60, "A Grade")],
        "recruiters": ["TCS", "L&T", "BHEL", "NTPC", "ONGC", "Samsung", "IBM", "Infosys", "Wipro"],
        "clubs": ["Robotics Club", "NSS", "NCC", "IEEE", "Photography", "Sports", "E-Cell", "Cultural Club"],
        "address": "Jhunsi, Prayagraj - 211015, UP",
        "phone": "+91-532-2684000",
        "email": "registrar@iert.ac.in",
        "website": "https://www.iert.ac.in",
        "social": {},
        "about": "Institute of Engineering and Rural Technology (IERT) Allahabad is a government institution established in 1962 in Jhunsi, Prayagraj. One of UP's finest government technical institutes with 60-acre campus, NAAC-A accreditation, and consistent PSU placements at BHEL, NTPC and L&T.",
        "infra": "60-acre Jhunsi campus with 12 departments, research labs, central library, 8 hostel blocks, sports complex, health centre, and auditorium."
    },
    {
        "filename": "gitm-lucknow-profile.html",
        "name": "Goel Institute of Technology & Management (GITM), Lucknow",
        "short_name": "GITM Lucknow",
        "code": "054",
        "city": "Lucknow",
        "type": "Private",
        "est": "2004",
        "campus": "12 acres",
        "naac": "B+",
        "nirf": "301-400",
        "fee": 100000,
        "hostel_single": 44000,
        "hostel_double": 32000,
        "mess": 30000,
        "dev": 5500,
        "highest_pkg": "20 LPA",
        "avg_pkg": "6.0 LPA",
        "placement_pct": "77",
        "branches": [("CSE", 120, "B+ Grade"), ("ECE", 90, "B Grade"), ("ME", 90, "B Grade"), ("CE", 60, "B Grade"), ("IT", 60, "B+ Grade")],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Capgemini", "Tech Mahindra"],
        "clubs": ["Coding Club", "NSS", "IEEE", "Photography", "Sports", "E-Cell", "Drama", "Music"],
        "address": "Faizabad Road, Lucknow - 226028, UP",
        "phone": "+91-522-2732600",
        "email": "info@gitm.ac.in",
        "website": "https://www.gitm.ac.in",
        "social": {},
        "about": "GITM Lucknow is a NAAC B+ private engineering college affiliated to AKTU. Founded in 2004 on Faizabad Road, it offers B.Tech in 5 branches with good placement support.",
        "infra": "12-acre Faizabad Road campus with central library, 14 labs, hostel blocks, food court, and sports facilities."
    },
    {
        "filename": "iec-engineering-greater-noida-profile.html",
        "name": "IEC College of Engineering and Technology, Greater Noida",
        "short_name": "IEC Greater Noida",
        "code": "057",
        "city": "Greater Noida",
        "type": "Private",
        "est": "2001",
        "campus": "18 acres",
        "naac": "B+",
        "nirf": "301-400",
        "fee": 108000,
        "hostel_single": 46000,
        "hostel_double": 35000,
        "mess": 32000,
        "dev": 6000,
        "highest_pkg": "21 LPA",
        "avg_pkg": "6.1 LPA",
        "placement_pct": "79",
        "branches": [("CSE", 180, "B+ Grade"), ("ECE", 120, "B Grade"), ("ME", 90, "B Grade"), ("CE", 60, "B Grade"), ("IT", 60, "B+ Grade"), ("MBA", 60, "B+ Grade")],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Tech Mahindra", "Capgemini", "Mindtree"],
        "clubs": ["Coding Club", "NSS", "IEEE", "Photography", "Sports", "E-Cell", "Drama", "Music", "Literary", "Robotics"],
        "address": "Knowledge Park I, Greater Noida - 201306, UP",
        "phone": "+91-120-2323402",
        "email": "info@iecollege.ac.in",
        "website": "https://www.iecollege.ac.in",
        "social": {},
        "about": "IEC College of Engineering and Technology is a NAAC B+ private college affiliated to AKTU. Established in 2001 in Knowledge Park I, Greater Noida. Known for strong TCS and Infosys mass placement drives.",
        "infra": "18-acre Knowledge Park campus with central library, 18 labs, 3 hostel blocks, food court, sports grounds, and 1000-seat auditorium."
    },
    {
        "filename": "swami-vivekanand-meerut-profile.html",
        "name": "Swami Vivekanand Subharti University (SVSU), Meerut",
        "short_name": "SVSU Meerut",
        "code": "115",
        "city": "Meerut",
        "type": "Private University",
        "est": "2008",
        "campus": "70 acres",
        "naac": "A",
        "nirf": "201-300",
        "fee": 108000,
        "hostel_single": 48000,
        "hostel_double": 36000,
        "mess": 32000,
        "dev": 6500,
        "highest_pkg": "28 LPA",
        "avg_pkg": "6.8 LPA",
        "placement_pct": "80",
        "branches": [("CSE", 180, "A Grade"), ("ECE", 150, "A Grade"), ("ME", 120, "A- Grade"), ("CE", 90, "B+ Grade"), ("IT", 90, "A Grade"), ("MBA", 120, "A Grade"), ("LLB", 60, "A Grade")],
        "recruiters": ["TCS", "Amazon", "Infosys", "Wipro", "HCL", "Capgemini", "Cognizant", "IBM", "Tech Mahindra"],
        "clubs": ["SVSU Coding Club", "IEEE", "NSS", "NCC", "Photography", "Sports", "E-Cell", "Drama", "Music", "Legal Aid Club"],
        "address": "NH-58, Meerut-Hapur Bypass, Meerut - 250005, UP",
        "phone": "+91-121-2439500",
        "email": "admission@subhartiuniversity.edu.in",
        "website": "https://www.subhartiuniversity.edu.in",
        "social": {},
        "about": "Swami Vivekanand Subharti University (SVSU), Meerut is a NAAC-A accredited private university offering engineering, management, law, medical and pharmacy on a 70-acre campus on NH-58. Established in 2008, SVSU has developed strong placement partnerships with TCS, Amazon and IBM.",
        "infra": "70-acre NH-58 campus with 10 academic schools, central library, 35 labs, medical college, law school, 6 hostel blocks, sports complex, swimming pool, and 2000-seat convention centre."
    },
    {
        "filename": "siet-sitapur-profile.html",
        "name": "Shambhunath Institute of Engineering and Technology (SIET), Allahabad",
        "short_name": "SIET Allahabad",
        "code": "135",
        "city": "Prayagraj",
        "type": "Private",
        "est": "2004",
        "campus": "16 acres",
        "naac": "B+",
        "nirf": "301-400",
        "fee": 95000,
        "hostel_single": 41000,
        "hostel_double": 29000,
        "mess": 27000,
        "dev": 5000,
        "highest_pkg": "14 LPA",
        "avg_pkg": "4.8 LPA",
        "placement_pct": "70",
        "branches": [("CSE", 90, "B+ Grade"), ("ECE", 60, "B Grade"), ("ME", 60, "B Grade"), ("CE", 60, "B Grade"), ("IT", 60, "B+ Grade")],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Capgemini"],
        "clubs": ["Coding Club", "NSS", "IEEE", "Photography", "Sports", "E-Cell"],
        "address": "Jhalwa, Prayagraj - 211012, UP",
        "phone": "+91-532-2684100",
        "email": "info@siet.ac.in",
        "website": "https://www.siet.ac.in",
        "social": {},
        "about": "SIET Allahabad is a NAAC B+ private engineering college affiliated to AKTU. Founded in 2004 in Jhalwa, it serves Allahabad and surrounding districts.",
        "infra": "16-acre Jhalwa campus with central library, 14 labs, hostel blocks, and sports facilities."
    },
    {
        "filename": "kmclu-lucknow-profile.html",
        "name": "Khwaja Moinuddin Chishti Language University, Lucknow",
        "short_name": "KMCLU Lucknow",
        "code": "086",
        "city": "Lucknow",
        "type": "Government University",
        "est": "2010",
        "campus": "22 acres",
        "naac": "B+",
        "nirf": "301-400",
        "fee": 65000,
        "hostel_single": 30000,
        "hostel_double": 22000,
        "mess": 24000,
        "dev": 3000,
        "highest_pkg": "12 LPA",
        "avg_pkg": "4.0 LPA",
        "placement_pct": "62",
        "branches": [("CSE", 60, "B+ Grade"), ("IT", 60, "B+ Grade"), ("MBA", 60, "B+ Grade"), ("BA", 120, "B Grade"), ("MA", 60, "B Grade")],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"],
        "clubs": ["Coding Club", "NSS", "NCC", "Photography", "Sports", "Cultural Club", "Literary Club", "Language Club", "Drama"],
        "address": "Sitapur Road, Lucknow - 226013, UP",
        "phone": "+91-522-2732700",
        "email": "info@kmclu.ac.in",
        "website": "https://www.kmclu.ac.in",
        "social": {},
        "about": "KMCLU is a government university in Lucknow offering liberal arts, language, and technology programmes. Established in 2010 on a 22-acre Sitapur Road campus.",
        "infra": "22-acre Sitapur Road campus with library, labs, hostel blocks, and sports facilities."
    },
    {
        "filename": "ecb-unnao-profile.html",
        "name": "Engineering College Bikru (ECB), Unnao",
        "short_name": "ECB Unnao",
        "code": "048",
        "city": "Unnao",
        "type": "Government",
        "est": "2010",
        "campus": "10 acres",
        "naac": "B",
        "nirf": "401-500",
        "fee": 55000,
        "hostel_single": 28000,
        "hostel_double": 20000,
        "mess": 23000,
        "dev": 2500,
        "highest_pkg": "10 LPA",
        "avg_pkg": "3.8 LPA",
        "placement_pct": "62",
        "branches": [("CSE", 60, "B Grade"), ("ECE", 60, "B- Grade"), ("ME", 60, "B- Grade"), ("CE", 60, "B- Grade")],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "BHEL"],
        "clubs": ["Coding Club", "NSS", "NCC", "IEEE", "Sports", "Photography"],
        "address": "Bikru, Unnao - 209801, UP",
        "phone": "+91-515-2340100",
        "email": "info@ecbunnao.ac.in",
        "website": "https://www.ecbunnao.ac.in",
        "social": {},
        "about": "Engineering College Bikru (ECB) is a government engineering college in Unnao established in 2010. Affiliated to AKTU, it offers B.Tech in 4 branches serving students from Unnao, Kanpur, and Lucknow districts.",
        "infra": "10-acre Bikru campus with library, 10 labs, hostel blocks, and sports facilities."
    },
    {
        "filename": "coer-roorkee-profile.html",
        "name": "College of Engineering Roorkee (COER), Roorkee",
        "short_name": "COER Roorkee",
        "code": "038",
        "city": "Roorkee",
        "type": "Private",
        "est": "2004",
        "campus": "20 acres",
        "naac": "B+",
        "nirf": "301-400",
        "fee": 105000,
        "hostel_single": 46000,
        "hostel_double": 34000,
        "mess": 30000,
        "dev": 6000,
        "highest_pkg": "22 LPA",
        "avg_pkg": "6.2 LPA",
        "placement_pct": "78",
        "branches": [("CSE", 120, "B+ Grade"), ("ECE", 90, "B Grade"), ("ME", 90, "B Grade"), ("CE", 60, "B Grade"), ("IT", 60, "B+ Grade")],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Tech Mahindra", "Capgemini"],
        "clubs": ["Coding Club", "NSS", "IEEE", "Photography", "Sports", "E-Cell", "Drama", "Music"],
        "address": "Roorkee-Haridwar Highway, Roorkee - 247667, Uttarakhand",
        "phone": "+91-1332-276200",
        "email": "info@coer.ac.in",
        "website": "https://www.coer.ac.in",
        "social": {},
        "about": "COER Roorkee is a NAAC B+ private engineering college on the Roorkee-Haridwar Highway. Founded in 2004, it benefits from proximity to IIT Roorkee and the Roorkee tech ecosystem.",
        "infra": "20-acre campus with central library, 18 labs, 3 hostel blocks, food court, sports facilities, and 1000-seat auditorium."
    },
    {
        "filename": "sbs-college-mathura-profile.html",
        "name": "SBS College of Engineering & Technology, Mathura",
        "short_name": "SBS Mathura",
        "code": "133",
        "city": "Mathura",
        "type": "Private",
        "est": "2003",
        "campus": "12 acres",
        "naac": "B",
        "nirf": "401-500",
        "fee": 90000,
        "hostel_single": 40000,
        "hostel_double": 28000,
        "mess": 26000,
        "dev": 4500,
        "highest_pkg": "12 LPA",
        "avg_pkg": "4.2 LPA",
        "placement_pct": "66",
        "branches": [("CSE", 90, "B Grade"), ("ECE", 60, "B- Grade"), ("ME", 60, "B- Grade"), ("CE", 60, "B- Grade"), ("IT", 60, "B Grade")],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"],
        "clubs": ["Coding Club", "NSS", "IEEE", "Photography", "Sports", "E-Cell", "Music"],
        "address": "Mathura-Delhi Highway, Mathura - 281001, UP",
        "phone": "+91-565-2420100",
        "email": "info@sbsmathura.ac.in",
        "website": "https://www.sbsmathura.ac.in",
        "social": {},
        "about": "SBS College of Engineering & Technology Mathura is a NAAC-B private engineering college affiliated to AKTU. Founded in 2003 on the Mathura-Delhi Highway, it serves engineering aspirants from Mathura, Agra, and Vrindavan.",
        "infra": "12-acre highway campus with library, 12 labs, hostel blocks, and sports facilities."
    },
    {
        "filename": "brcm-baghpat-profile.html",
        "name": "BRCM College of Engineering & Technology, Baghpat",
        "short_name": "BRCM Baghpat",
        "code": "023",
        "city": "Baghpat",
        "type": "Private",
        "est": "2002",
        "campus": "15 acres",
        "naac": "B",
        "nirf": "401-500",
        "fee": 92000,
        "hostel_single": 40000,
        "hostel_double": 28000,
        "mess": 26000,
        "dev": 4800,
        "highest_pkg": "13 LPA",
        "avg_pkg": "4.5 LPA",
        "placement_pct": "67",
        "branches": [("CSE", 90, "B Grade"), ("ECE", 60, "B- Grade"), ("ME", 60, "B- Grade"), ("CE", 60, "B- Grade"), ("IT", 60, "B Grade")],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Capgemini"],
        "clubs": ["Coding Club", "NSS", "IEEE", "Photography", "Sports", "E-Cell", "Music", "Drama"],
        "address": "Diwana Road, Baghpat - 250609, UP",
        "phone": "+91-1232-241000",
        "email": "info@brcmcet.ac.in",
        "website": "https://www.brcmcet.ac.in",
        "social": {},
        "about": "BRCM College Baghpat is a NAAC-B private engineering college affiliated to AKTU. Founded in 2002 on Diwana Road, it serves students from Baghpat, Meerut, and the western UP belt.",
        "infra": "15-acre campus with library, 12 labs, hostel blocks, and sports facilities."
    }
]

sitemap_entries = []
out_dir = "/home/techiedevang/akturesults/colleges/profiles"
os.makedirs(out_dir, exist_ok=True)

for col in colleges:
    url_name = col['short_name'].lower().replace(" ", "-")
    total_yr = col['fee'] + col['hostel_double'] + col['mess'] + col['dev']
    total_4yr = total_yr * 4
    total_intake = sum(c[1] for c in col['branches'])
    
    branches_html = ""
    for i, (branch_name, intake, grade) in enumerate(col['branches']):
        if branch_name.startswith("CS"):
            full_b = "Computer Science & Engineering"
            if branch_name == "CSE-AI": full_b = "Computer Science & Engineering (AI)"
        elif branch_name == "ECE": full_b = "Electronics & Communication Engineering"
        elif branch_name == "ME": full_b = "Mechanical Engineering"
        elif branch_name == "CE" or branch_name == "Civil": full_b = "Civil Engineering"
        elif branch_name == "EE": full_b = "Electrical Engineering"
        elif branch_name == "IT": full_b = "Information Technology"
        elif branch_name == "MBA": full_b = "Master of Business Administration (MBA)"
        elif branch_name == "BA": full_b = "Bachelor of Arts (BA)"
        elif branch_name == "MA": full_b = "Master of Arts (MA)"
        elif branch_name == "LLB": full_b = "Bachelor of Laws (LLB)"
        else: full_b = branch_name
        
        branches_html += f'<tr><td style="padding:12px 15px; border-bottom:1px solid #e2e8f0; font-weight:600;">{full_b} ({branch_name})</td><td style="padding:12px 15px; border-bottom:1px solid #e2e8f0; text-align:center;">{intake}</td><td style="padding:12px 15px; border-bottom:1px solid #e2e8f0;">Prof. Head</td><td style="padding:12px 15px; border-bottom:1px solid #e2e8f0; text-align:center;"><span style="background:#e0e7ff; color:#3730a3; padding:3px 10px; border-radius:12px; font-size:12px; font-weight:700;">{grade}</span></td></tr>'
        
    recruiters_html = "".join([f'<span style="background:#f1f5f9; color:#475569; padding:5px 12px; border-radius:20px; font-size:13px; font-weight:600; display:inline-block; margin:3px;">{r}</span>' for r in col['recruiters']])
    
    clubs_html = "".join([f'<li style="padding:5px 0; border-bottom:1px solid #f1f5f9;">{c}</li>' for c in col['clubs']])
    
    social_links = col['social']
    social_html = ""
    for k, v in social_links.items():
        if k == "LinkedIn": social_html += f'\\n<a href="{v}" class="sbtn s2" target="_blank" rel="noopener">in LinkedIn</a>'
        elif k == "Twitter": social_html += f'\\n<a href="{v}" class="sbtn s3" target="_blank" rel="noopener">𝕏 Twitter</a>'
        elif k == "Facebook": social_html += f'\\n<a href="{v}" class="sbtn s4" target="_blank" rel="noopener">f Facebook</a>'
        elif k == "Instagram": social_html += f'\\n<a href="{v}" class="sbtn s5" target="_blank" rel="noopener">📸 Instagram</a>'
        elif k == "YouTube": social_html += f'\\n<a href="{v}" class="sbtn s6" target="_blank" rel="noopener">▶ YouTube</a>'
        
    html = template.format(
        name=col['name'],
        short_name=col['short_name'],
        url_name=url_name,
        code=col['code'],
        city=col['city'],
        type=col['type'],
        est=col['est'],
        campus=col['campus'],
        naac=col['naac'],
        nirf=col['nirf'],
        fee=col['fee'],
        fee_fmt=f"{col['fee']:,}",
        hostel_single=col['hostel_single'],
        hostel_single_fmt=f"{col['hostel_single']:,}",
        hostel_double=col['hostel_double'],
        hostel_double_fmt=f"{col['hostel_double']:,}",
        mess=col['mess'],
        mess_fmt=f"{col['mess']:,}",
        dev=col['dev'],
        dev_fmt=f"{col['dev']:,}",
        total_yr=total_yr,
        total_yr_fmt=f"{total_yr:,}",
        total_4yr=total_4yr,
        total_4yr_fmt=f"{total_4yr:,}",
        highest_pkg=col['highest_pkg'],
        avg_pkg=col['avg_pkg'],
        placement_pct=col['placement_pct'],
        total_intake=total_intake,
        about=col['about'],
        infra=col['infra'],
        address=col['address'],
        phone=col['phone'],
        email=col['email'],
        website=col['website'],
        filename=col['filename'],
        branches_html=branches_html,
        recruiters_html=recruiters_html,
        clubs_html=clubs_html,
        social_html=social_html
    )
    
    file_path = os.path.join(out_dir, col['filename'])
    with open(file_path, "w") as f:
        f.write(html)
        
    sitemap_entries.append(f'  <url>\\n    <loc>https://akturesults.in/colleges/profiles/{col["filename"]}</loc>\\n    <lastmod>2026-08-04</lastmod>\\n    <changefreq>monthly</changefreq>\\n    <priority>0.8</priority>\\n  </url>')

sitemap_path = "/home/techiedevang/akturesults/sitemap.xml"
if os.path.exists(sitemap_path):
    with open(sitemap_path, "r") as f:
        sitemap = f.read()
    
    entries_str = "\\n".join(sitemap_entries)
    sitemap = sitemap.replace('</urlset>', f'{entries_str}\\n</urlset>')
    
    with open(sitemap_path, "w") as f:
        f.write(sitemap)
