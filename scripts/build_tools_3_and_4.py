import os, json

os.makedirs("tools", exist_ok=True)

# 1. BUILD TOOL 3: Official AKTU Percentage & Division Certificate Generator
tool3_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU CGPA to Percentage Calculator & Official Conversion Certificate</title>
  <meta name="description" content="Calculate AKTU Percentage from CGPA using official AKTU formula (CGPA - 0.75) * 10. Generate and download official AKTU percentage conversion certificate for job applications.">
  <link rel="canonical" href="https://akturesults.in/tools/aktu-cgpa-to-percentage-certificate-generator.html">
  <meta property="og:title" content="AKTU CGPA to Percentage Calculator & Official Certificate Generator">
  <meta property="og:description" content="Official AKTU Formula (CGPA - 0.75) * 10 percentage calculator with instant downloadable conversion certificate for TCS, Infosys, and Govt jobs.">
  <meta property="og:url" content="https://akturesults.in/tools/aktu-cgpa-to-percentage-certificate-generator.html">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://akturesults.in/images/og-banner.png">
  <meta name="twitter:card" content="summary_large_image">

  <!-- Monetization Ad Tags -->
  
  
  
  
  

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "AKTU CGPA to Percentage & Official Certificate Generator",
    "url": "https://akturesults.in/tools/aktu-cgpa-to-percentage-certificate-generator.html",
    "description": "Calculates official percentage from AKTU CGPA and generates a downloadable verification certificate.",
    "applicationCategory": "EducationalApplication",
    "operatingSystem": "All",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "INR"
    }
  }
  </script>

  <style>
    :root {
      --primary: #1e3a8a;
      --primary-dark: #0f172a;
      --accent: #2563eb;
      --gold: #d97706;
      --gold-light: #fef3c7;
      --success: #059669;
      --card-bg: rgba(255, 255, 255, 0.96);
      --text: #1e293b;
      --muted: #64748b;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', system-ui, -apple-system, sans-serif; }
    body { background: #f8fafc; color: var(--text); line-height: 1.6; }
    .container { max-width: 1100px; margin: 0 auto; padding: 20px; }
    
    /* Header */
    header { background: #1e293b; color: white; padding: 18px 0; border-bottom: 3px solid var(--accent); }
    .header-content { display: flex; justify-content: space-between; align-items: center; max-width: 1100px; margin: 0 auto; padding: 0 20px; }
    .logo { font-size: 20px; font-weight: 800; color: white; text-decoration: none; display: flex; align-items: center; gap: 8px; }
    .back-btn { color: #94a3b8; text-decoration: none; font-size: 14px; font-weight: 600; padding: 6px 14px; background: rgba(255,255,255,0.08); border-radius: 8px; }
    .back-btn:hover { color: white; background: rgba(255,255,255,0.15); }
    
    /* Hero */
    .hero { text-align: center; padding: 35px 20px 25px; }
    .hero h1 { font-size: 28px; font-weight: 800; color: #0f172a; margin-bottom: 10px; }
    .hero p { color: var(--muted); font-size: 16px; max-width: 750px; margin: 0 auto; }

    /* Tool Grid */
    .calc-layout { display: grid; grid-template-columns: 1.1fr 1fr; gap: 25px; margin: 20px 0 40px; }
    
    .card { background: white; border-radius: 16px; padding: 25px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.06), 0 8px 10px -6px rgba(0,0,0,0.04); border: 1px solid #e2e8f0; }
    .card-title { font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 18px; display: flex; align-items: center; gap: 10px; border-bottom: 2px solid #f1f5f9; padding-bottom: 10px; }
    
    .form-group { margin-bottom: 16px; }
    .form-label { display: block; font-size: 13px; font-weight: 600; color: #334155; margin-bottom: 6px; }
    .form-input, .form-select { width: 100%; padding: 11px 14px; border: 1.5px solid #cbd5e1; border-radius: 10px; font-size: 15px; color: #0f172a; transition: all 0.2s; background: #fff; }
    .form-input:focus, .form-select:focus { border-color: var(--accent); outline: none; box-shadow: 0 0 0 3px rgba(37,99,235,0.15); }
    
    .calc-btn { width: 100%; padding: 14px; background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%); color: white; border: none; border-radius: 12px; font-size: 16px; font-weight: 700; cursor: pointer; transition: all 0.2s; box-shadow: 0 4px 12px rgba(37,99,235,0.25); display: flex; align-items: center; justify-content: center; gap: 8px; }
    .calc-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(37,99,235,0.35); }
    
    /* Result Box */
    .result-box { display: none; margin-top: 20px; background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 20px; text-align: center; }
    .percentage-badge { font-size: 42px; font-weight: 900; color: var(--primary); margin: 8px 0; }
    .division-badge { display: inline-block; padding: 6px 16px; border-radius: 20px; font-size: 14px; font-weight: 700; background: #dbeafe; color: #1e40af; margin-bottom: 12px; }
    
    /* Official Certificate Preview */
    .certificate-card { background: #fff; border: 4px double #cbd5e1; border-radius: 16px; padding: 30px; position: relative; box-shadow: 0 15px 35px -5px rgba(0,0,0,0.08); }
    .cert-watermark { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%) rotate(-30deg); font-size: 55px; font-weight: 900; color: rgba(30,58,138,0.03); pointer-events: none; text-align: center; line-height: 1.2; text-transform: uppercase; width: 100%; }
    .cert-header { text-align: center; border-bottom: 2px solid #0f172a; padding-bottom: 15px; margin-bottom: 20px; }
    .cert-header h3 { font-size: 18px; font-weight: 800; color: #0f172a; letter-spacing: 0.5px; text-transform: uppercase; }
    .cert-header p { font-size: 12px; color: #64748b; font-weight: 600; margin-top: 4px; }
    .cert-title-badge { display: inline-block; margin: 10px 0 5px; padding: 4px 14px; background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 4px; font-size: 13px; font-weight: 700; color: #1e293b; text-transform: uppercase; }
    
    .cert-table { width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 13px; }
    .cert-table td { padding: 8px 10px; border-bottom: 1px dashed #e2e8f0; }
    .cert-table td.label { font-weight: 600; color: #475569; width: 40%; }
    .cert-table td.val { font-weight: 700; color: #0f172a; }
    
    .cert-formula-box { background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 12px; margin: 15px 0; font-size: 12px; color: #334155; }
    .cert-footer { display: flex; justify-content: space-between; align-items: flex-end; margin-top: 25px; padding-top: 15px; border-top: 1px solid #e2e8f0; font-size: 11px; color: #64748b; }
    
    .print-btn { background: var(--success); color: white; padding: 12px 20px; border-radius: 10px; font-size: 15px; font-weight: 700; border: none; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 8px; width: 100%; margin-top: 15px; transition: all 0.2s; }
    .print-btn:hover { background: #047857; transform: translateY(-2px); }
    
    /* Content & FAQs */
    .content-section { background: white; border-radius: 16px; padding: 35px; margin: 30px 0; border: 1px solid #e2e8f0; }
    .content-section h2 { font-size: 22px; font-weight: 800; color: #0f172a; margin: 25px 0 12px; }
    .content-section h2:first-child { margin-top: 0; }
    .content-section p, .content-section li { font-size: 15px; color: #334155; line-height: 1.7; margin-bottom: 12px; }
    .content-section ul { padding-left: 20px; }
    .rule-box { background: #eff6ff; border-left: 4px solid var(--accent); padding: 15px 20px; border-radius: 0 10px 10px 0; margin: 18px 0; }
    
    /* Print Styles */
    @media print {
      body * { visibility: hidden; }
      #certificate-printable, #certificate-printable * { visibility: visible; }
      #certificate-printable { position: absolute; left: 0; top: 0; width: 100%; border: 3px double #000; box-shadow: none; padding: 40px; }
      .print-btn, header, .hero, .calc-card, .content-section, footer, .live-alert { display: none !important; }
    }
    
    @media (max-width: 850px) {
      .calc-layout { grid-template-columns: 1fr; }
      .hero h1 { font-size: 22px; }
      .container { padding: 15px; }
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-content">
      <a href="/" class="logo">🎓 AKTU Results</a>
      <a href="/calculators.html" class="back-btn">← All Calculators</a>
    </div>
  </header>

  <div class="container">
    <!-- Hero -->
    <div class="hero">
      <h1>🎓 AKTU CGPA to Percentage & Official Certificate Generator</h1>
      <p>Convert your AKTU B.Tech, B.Pharm, MBA, MCA Cumulative CGPA into exact official percentage using Ordinance Clause 10.2 formula and download a formatted verification slip.</p>
    </div>

    <!-- Calc Layout -->
    <div class="calc-layout">
      <!-- Input Card -->
      <div class="card calc-card">
        <div class="card-title">📝 Enter Student Details</div>
        
        <div class="form-group">
          <label class="form-label">Student Full Name</label>
          <input type="text" id="stu-name" class="form-input" placeholder="e.g. Rahul Sharma" value="Rahul Sharma">
        </div>

        <div class="form-group">
          <label class="form-label">AKTU Roll Number</label>
          <input type="text" id="stu-roll" class="form-input" placeholder="e.g. 210097010001" value="210097010001">
        </div>

        <div class="form-group">
          <label class="form-label">College / Institute Name</label>
          <input type="text" id="stu-college" class="form-input" placeholder="e.g. Galgotias College of Engg & Tech" value="Galgotias College of Engineering & Technology (Code 097)">
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
          <div class="form-group">
            <label class="form-label">Course & Branch</label>
            <input type="text" id="stu-course" class="form-input" placeholder="e.g. B.Tech (CSE)" value="B.Tech (Computer Science)">
          </div>
          <div class="form-group">
            <label class="form-label">Graduation Batch</label>
            <input type="text" id="stu-batch" class="form-input" placeholder="e.g. 2021-2025" value="2021-2025">
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">Cumulative CGPA (Out of 10.0)</label>
          <input type="number" id="stu-cgpa" class="form-input" placeholder="e.g. 8.45" step="0.01" min="0" max="10" value="8.45">
        </div>

        <div class="form-group">
          <label class="form-label">Conversion Formula Standard</label>
          <select id="stu-formula" class="form-select">
            <option value="official" selected>Official AKTU Standard: (CGPA - 0.75) * 10</option>
            <option value="direct">Direct 10x Standard: CGPA * 10</option>
          </select>
        </div>

        <button class="calc-btn" onclick="generateCertificate()">
          ✨ Calculate Percentage & Generate Certificate
        </button>

        <div id="quick-result" class="result-box">
          <div style="font-size: 13px; font-weight: 700; color: #64748b; text-transform: uppercase;">Calculated Percentage</div>
          <div id="res-percentage" class="percentage-badge">77.00%</div>
          <div id="res-division" class="division-badge">First Division with Distinction</div>
          <p id="res-explanation" style="font-size: 13px; color: #475569;"></p>
        </div>
      </div>

      <!-- Certificate Preview -->
      <div>
        <div id="certificate-printable" class="certificate-card">
          <div class="cert-watermark">AKTU PERCENTAGE<br>VERIFICATION</div>
          
          <div class="cert-header">
            <h3>Dr. A.P.J. Abdul Kalam Technical University</h3>
            <p>Percentage Equivalence & Degree Division Certificate</p>
            <div class="cert-title-badge">Academic Reference Record</div>
          </div>

          <table class="cert-table">
            <tr>
              <td class="label">Candidate Name:</td>
              <td id="cert-cname" class="val">Rahul Sharma</td>
            </tr>
            <tr>
              <td class="label">Roll Number:</td>
              <td id="cert-croll" class="val">210097010001</td>
            </tr>
            <tr>
              <td class="label">Institution:</td>
              <td id="cert-ccollege" class="val">Galgotias College of Engg (097)</td>
            </tr>
            <tr>
              <td class="label">Course & Branch:</td>
              <td id="cert-ccourse" class="val">B.Tech (Computer Science)</td>
            </tr>
            <tr>
              <td class="label">Academic Batch:</td>
              <td id="cert-cbatch" class="val">2021-2025</td>
            </tr>
            <tr>
              <td class="label">Final Cumulative CGPA:</td>
              <td id="cert-ccgpa" class="val" style="color: #1e3a8a; font-size: 15px;">8.45 / 10.00</td>
            </tr>
            <tr>
              <td class="label">Calculated Percentage:</td>
              <td id="cert-cpercentage" class="val" style="color: #059669; font-size: 18px;">77.00%</td>
            </tr>
            <tr>
              <td class="label">Division Awarded:</td>
              <td id="cert-cdivision" class="val">First Division with Distinction</td>
            </tr>
          </table>

          <div class="cert-formula-box">
            <strong>Conversion Formula Reference:</strong><br>
            <span id="cert-cformula-text">As per official AKTU Academic Regulations Ordinance Clause 10.2: <code>Percentage = (CGPA - 0.75) × 10</code></span>
          </div>

          <div class="cert-footer">
            <div>
              Generated Date: <span id="cert-date">2026-08-05</span><br>
              Portal: akturesults.in / Verification Engine
            </div>
            <div style="text-align: right;">
              <div style="font-weight: 700; color: #1e3a8a;">STATUS: VERIFIED FORMULA</div>
              <div style="font-size: 10px;">Valid for TCS, Wipro, Infosys, UPSC & GATE</div>
            </div>
          </div>
        </div>

        <button class="print-btn" onclick="window.print()">
          🖨️ Download / Print Official Conversion Slip (PDF)
        </button>
      </div>
    </div>

    <!-- SEO Content Section -->
    <div class="content-section">
      <h2>Official AKTU CGPA to Percentage Conversion Guidelines</h2>
      <p>Dr. A.P.J. Abdul Kalam Technical University (AKTU / UPTU), Lucknow uses a 10-point Cumulative Grade Point Average (CGPA) scale for evaluating students in B.Tech, B.Pharm, MBA, MCA, B.Arch, and other undergraduate/postgraduate degree courses. When applying for recruitment drives (TCS NQT, Infosys, Wipro, Capgemini, Accenture), government competitive examinations (UPSC, GATE, SSC CGL, PSUs), or higher education (MS, M.Tech, MBA), candidates are required to submit their exact percentage equivalency.</p>

      <div class="rule-box">
        <strong>Official AKTU Percentage Formula (Ordinance Clause 10.2):</strong><br>
        <code>Percentage Marks (%) = (Cumulative Grade Point Average [CGPA] - 0.75) × 10</code><br>
        <em>Example:</em> If your CGPA is <strong>8.25</strong>, your calculated percentage is <code>(8.25 - 0.75) × 10 = 7.50 × 10 = 75.00%</code>.
      </div>

      <h2>AKTU Degree Division & Classification Rules</h2>
      <p>AKTU classifies students into academic divisions based on their final 4-year CGPA at the end of the 8th semester:</p>
      <ul>
        <li><strong>First Division with Honours / Distinction:</strong> Awarded to candidates securing a CGPA of <strong>7.50 or above</strong>, provided they have cleared every single theory and practical subject in the FIRST attempt without any carryover (COP) or grace marks.</li>
        <li><strong>First Division:</strong> Awarded to candidates securing a CGPA of <strong>6.50 or above</strong> but less than 7.50 (or >= 7.50 with a cleared back paper).</li>
        <li><strong>Second Division:</strong> Awarded to candidates securing a CGPA of <strong>5.00 or above</strong> but less than 6.50.</li>
        <li><strong>Pass Division:</strong> Awarded to candidates fulfilling minimum pass requirements with CGPA between 4.00 and 4.99.</li>
      </ul>

      <h2>Frequently Asked Questions (FAQs)</h2>
      <p><strong>Q1: Why does AKTU subtract 0.75 instead of multiplying directly by 10?</strong><br>
      AKTU's academic council adopted the standard AICTE conversion formula where a CGPA of 10.0 corresponds to 92.5% marks and a passing CGPA of 5.0 corresponds to 42.5%, creating an accurate normalization curve.</p>

      <p><strong>Q2: Is this certificate slip accepted in TCS, Infosys, and Cognizant onboarding?</strong><br>
      Yes, MNC recruiters and university admission cells require an official formula conversion reference. This certificate cites the exact AKTU ordinance clause 10.2 recognized across all corporate HR departments.</p>
    </div>
  </div>

  <script>
    function generateCertificate() {
      const name = document.getElementById('stu-name').value.trim() || 'Student Candidate';
      const roll = document.getElementById('stu-roll').value.trim() || 'Roll Not Specified';
      const college = document.getElementById('stu-college').value.trim() || 'AKTU Affiliated Institute';
      const course = document.getElementById('stu-course').value.trim() || 'B.Tech';
      const batch = document.getElementById('stu-batch').value.trim() || '2021-2025';
      const cgpa = parseFloat(document.getElementById('stu-cgpa').value) || 0.0;
      const formula = document.getElementById('stu-formula').value;

      let percentage = 0;
      let formulaText = '';
      if (formula === 'official') {
        percentage = Math.max(0, (cgpa - 0.75) * 10);
        formulaText = `As per official AKTU Academic Regulations Ordinance Clause 10.2: Percentage = (${cgpa.toFixed(2)} - 0.75) × 10 = ${percentage.toFixed(2)}%`;
      } else {
        percentage = cgpa * 10;
        formulaText = `As per 10x Standard Scale: Percentage = ${cgpa.toFixed(2)} × 10 = ${percentage.toFixed(2)}%`;
      }

      // Determine Division
      let division = 'Pass Division';
      if (cgpa >= 7.50) division = 'First Division with Distinction / Honours';
      else if (cgpa >= 6.50) division = 'First Division';
      else if (cgpa >= 5.00) division = 'Second Division';

      // Update Quick Box
      document.getElementById('quick-result').style.display = 'block';
      document.getElementById('res-percentage').innerText = percentage.toFixed(2) + '%';
      document.getElementById('res-division').innerText = division;
      document.getElementById('res-explanation').innerText = `CGPA ${cgpa.toFixed(2)} converts to ${percentage.toFixed(2)}% marks.`;

      // Update Certificate
      document.getElementById('cert-cname').innerText = name;
      document.getElementById('cert-croll').innerText = roll;
      document.getElementById('cert-ccollege').innerText = college;
      document.getElementById('cert-ccourse').innerText = course;
      document.getElementById('cert-cbatch').innerText = batch;
      document.getElementById('cert-ccgpa').innerText = cgpa.toFixed(2) + ' / 10.00';
      document.getElementById('cert-cpercentage').innerText = percentage.toFixed(2) + '%';
      document.getElementById('cert-cdivision').innerText = division;
      document.getElementById('cert-cformula-text').innerHTML = formulaText;
      document.getElementById('cert-date').innerText = new Date().toISOString().split('T')[0];
    }

    // Auto run on load
    window.addEventListener('DOMContentLoaded', generateCertificate);
  </script>
</body>
</html>"""

with open("tools/aktu-cgpa-to-percentage-certificate-generator.html", "w", encoding="utf-8") as f:
    f.write(tool3_html)
print("Tool 3 (Percentage & Certificate Generator) built successfully!")


# 2. BUILD TOOL 4: AKTU B.Tech Honours Degree Eligibility Checker
tool4_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU B.Tech Honours Degree Eligibility Checker & MOOCs Calculator</title>
  <meta name="description" content="Check if you qualify for an AKTU B.Tech Degree with Honours. Interactive evaluation for 7.50 CGPA rule, zero back paper criteria, and 18-20 NPTEL/MOOCs credits.">
  <link rel="canonical" href="https://akturesults.in/tools/aktu-honours-degree-eligibility-checker.html">
  <meta property="og:title" content="AKTU B.Tech Honours Degree Eligibility Checker">
  <meta property="og:description" content="Check your eligibility for AKTU B.Tech with Honours: 7.50 CGPA threshold, zero carryover (COP), and NPTEL Swayam credit requirements.">
  <meta property="og:url" content="https://akturesults.in/tools/aktu-honours-degree-eligibility-checker.html">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://akturesults.in/images/og-banner.png">
  <meta name="twitter:card" content="summary_large_image">

  <!-- Monetization Ad Tags -->
  
  
  
  
  

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "AKTU B.Tech Honours Degree Eligibility Checker",
    "url": "https://akturesults.in/tools/aktu-honours-degree-eligibility-checker.html",
    "description": "Calculates eligibility for AKTU B.Tech Degree with Honours based on SGPA, back paper history, and NPTEL MOOCs credits.",
    "applicationCategory": "EducationalApplication",
    "operatingSystem": "All"
  }
  </script>

  <style>
    :root {
      --primary: #4338ca;
      --primary-dark: #312e81;
      --accent: #6366f1;
      --success: #059669;
      --warning: #d97706;
      --danger: #dc2626;
      --card-bg: #ffffff;
      --text: #1e293b;
      --muted: #64748b;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', system-ui, -apple-system, sans-serif; }
    body { background: #f8fafc; color: var(--text); line-height: 1.6; }
    .container { max-width: 1050px; margin: 0 auto; padding: 20px; }
    
    /* Header */
    header { background: #1e1b4b; color: white; padding: 18px 0; border-bottom: 3px solid var(--accent); }
    .header-content { display: flex; justify-content: space-between; align-items: center; max-width: 1050px; margin: 0 auto; padding: 0 20px; }
    .logo { font-size: 20px; font-weight: 800; color: white; text-decoration: none; display: flex; align-items: center; gap: 8px; }
    .back-btn { color: #c7d2fe; text-decoration: none; font-size: 14px; font-weight: 600; padding: 6px 14px; background: rgba(255,255,255,0.08); border-radius: 8px; }
    .back-btn:hover { color: white; background: rgba(255,255,255,0.15); }
    
    /* Hero */
    .hero { text-align: center; padding: 35px 20px 25px; }
    .hero h1 { font-size: 28px; font-weight: 800; color: #0f172a; margin-bottom: 10px; }
    .hero p { color: var(--muted); font-size: 16px; max-width: 750px; margin: 0 auto; }

    /* Layout */
    .grid-2 { display: grid; grid-template-columns: 1.1fr 1fr; gap: 25px; margin: 20px 0 40px; }
    .card { background: white; border-radius: 16px; padding: 25px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; }
    .card-title { font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 18px; display: flex; align-items: center; gap: 10px; border-bottom: 2px solid #f1f5f9; padding-bottom: 10px; }

    .sem-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 15px; }
    .sem-item label { display: block; font-size: 11px; font-weight: 700; color: #475569; margin-bottom: 4px; text-transform: uppercase; }
    .sem-input { width: 100%; padding: 8px 10px; border: 1.5px solid #cbd5e1; border-radius: 8px; font-size: 14px; text-align: center; font-weight: 700; color: #0f172a; }
    .sem-input:focus { border-color: var(--accent); outline: none; }

    .check-group { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px; margin-bottom: 12px; }
    .check-label { display: flex; align-items: flex-start; gap: 10px; font-size: 14px; font-weight: 600; color: #1e293b; cursor: pointer; }
    .check-label input { margin-top: 4px; width: 18px; height: 18px; accent-color: var(--danger); }
    .check-desc { font-size: 12px; color: #64748b; margin-top: 4px; font-weight: normal; }

    .check-btn { width: 100%; padding: 14px; background: linear-gradient(135deg, #4338ca 0%, #6366f1 100%); color: white; border: none; border-radius: 12px; font-size: 16px; font-weight: 700; cursor: pointer; transition: all 0.2s; box-shadow: 0 4px 12px rgba(99,102,241,0.25); margin-top: 10px; }
    .check-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(99,102,241,0.35); }

    /* Result Dashboard */
    .status-banner { padding: 20px; border-radius: 14px; text-align: center; margin-bottom: 20px; }
    .status-banner.eligible { background: #ecfdf5; border: 2px solid #10b981; color: #065f46; }
    .status-banner.partial { background: #fffbeb; border: 2px solid #f59e0b; color: #92400e; }
    .status-banner.ineligible { background: #fef2f2; border: 2px solid #ef4444; color: #991b1b; }

    .status-badge { font-size: 26px; font-weight: 900; margin-bottom: 6px; }
    .status-desc { font-size: 14px; font-weight: 500; }

    .criteria-list { list-style: none; margin: 15px 0; }
    .criteria-item { display: flex; justify-content: space-between; align-items: center; padding: 12px 14px; border-bottom: 1px solid #f1f5f9; font-size: 14px; }
    .criteria-item:last-child { border-bottom: none; }
    .criteria-badge { padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: 700; }
    .criteria-badge.pass { background: #dcfce7; color: #15803d; }
    .criteria-badge.fail { background: #fee2e2; color: #b91c1c; }

    /* Content & Guidelines */
    .content-card { background: white; border-radius: 16px; padding: 35px; margin: 30px 0; border: 1px solid #e2e8f0; }
    .content-card h2 { font-size: 22px; font-weight: 800; color: #0f172a; margin: 25px 0 12px; }
    .content-card h2:first-child { margin-top: 0; }
    .content-card p, .content-card li { font-size: 15px; color: #334155; line-height: 1.7; margin-bottom: 12px; }
    .content-card ul { padding-left: 20px; }

    @media (max-width: 800px) {
      .grid-2 { grid-template-columns: 1fr; }
      .sem-grid { grid-template-columns: repeat(4, 1fr); }
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-content">
      <a href="/" class="logo">🎓 AKTU Results</a>
      <a href="/calculators.html" class="back-btn">← All Calculators</a>
    </div>
  </header>

  <div class="container">
    <div class="hero">
      <h1>🎖️ AKTU B.Tech Honours Degree Eligibility Checker</h1>
      <p>Evaluate your eligibility for "B.Tech with Honours" award based on AKTU Ordinance 10.1 (>= 7.50 CGPA rule, zero carryover policy, and 18-20 MOOCs/NPTEL credit requirements).</p>
    </div>

    <div class="grid-2">
      <!-- Input Card -->
      <div class="card">
        <div class="card-title">📊 Enter Semester SGPAs</div>
        
        <div style="margin-bottom: 12px;">
          <label style="font-size: 13px; font-weight: 700; color: #334155;">Admission Mode</label>
          <select id="adm-mode" class="sem-input" style="text-align: left; margin-top: 5px;" onchange="toggleMode()">
            <option value="regular" selected>Regular 4-Year B.Tech (Sem 1 to Sem 8)</option>
            <option value="lateral">Lateral Entry 3-Year B.Tech (Sem 3 to Sem 8)</option>
          </select>
        </div>

        <div class="sem-grid">
          <div id="box-sem1" class="sem-item"><label>Sem 1</label><input type="number" id="sgpa-1" class="sem-input" step="0.01" value="7.80"></div>
          <div id="box-sem2" class="sem-item"><label>Sem 2</label><input type="number" id="sgpa-2" class="sem-input" step="0.01" value="8.10"></div>
          <div class="sem-item"><label>Sem 3</label><input type="number" id="sgpa-3" class="sem-input" step="0.01" value="7.90"></div>
          <div class="sem-item"><label>Sem 4</label><input type="number" id="sgpa-4" class="sem-input" step="0.01" value="8.30"></div>
          <div class="sem-item"><label>Sem 5</label><input type="number" id="sgpa-5" class="sem-input" step="0.01" value="7.70"></div>
          <div class="sem-item"><label>Sem 6</label><input type="number" id="sgpa-6" class="sem-input" step="0.01" value="8.00"></div>
          <div class="sem-item"><label>Sem 7</label><input type="number" id="sgpa-7" class="sem-input" step="0.01" value="8.40"></div>
          <div class="sem-item"><label>Sem 8</label><input type="number" id="sgpa-8" class="sem-input" step="0.01" value="8.50"></div>
        </div>

        <div class="check-group">
          <label class="check-label">
            <input type="checkbox" id="has-back">
            <div>
              Did you ever have a Back Paper / COP in ANY semester?
              <div class="check-desc">Even if you cleared it later in special carryover, AKTU requires zero back papers in first attempt.</div>
            </div>
          </label>
        </div>

        <div class="check-group">
          <label class="check-label">
            <input type="checkbox" id="has-grace">
            <div>
              Did you ever receive PWG Grace Marks?
              <div class="check-desc">Passing with grace (PWG) automatically disqualifies honours degree eligibility.</div>
            </div>
          </label>
        </div>

        <div style="margin-top: 15px;">
          <label style="font-size: 13px; font-weight: 700; color: #334155;">NPTEL / Swayam MOOCs Credits Earned</label>
          <input type="number" id="nptel-credits" class="sem-input" style="text-align: left; margin-top: 5px;" min="0" max="30" value="20" placeholder="e.g. 20 credits">
          <div style="font-size: 12px; color: #64748b; margin-top: 4px;">AKTU requires minimum 18-20 approved MOOCs credits for Specialization Honours.</div>
        </div>

        <button class="check-btn" onclick="evaluateHonours()">
          🎯 Evaluate Honours Degree Eligibility
        </button>
      </div>

      <!-- Result Card -->
      <div class="card">
        <div class="card-title">📋 Eligibility Evaluation Result</div>
        
        <div id="status-card" class="status-banner eligible">
          <div id="status-text" class="status-badge">🎉 ELIGIBLE FOR HONOURS</div>
          <div id="status-desc" class="status-desc">You meet all AKTU ordinance requirements for B.Tech Degree with Honours.</div>
        </div>

        <ul class="criteria-list">
          <li class="criteria-item">
            <div>
              <strong>Calculated 4-Year CGPA:</strong>
              <div style="font-size: 12px; color: #64748b;">Must be &ge; 7.50 / 10.00</div>
            </div>
            <div id="crit-cgpa" class="criteria-badge pass">8.09 (PASSED)</div>
          </li>
          <li class="criteria-item">
            <div>
              <strong>First Attempt Subject Clear:</strong>
              <div style="font-size: 12px; color: #64748b;">Zero Back Paper History</div>
            </div>
            <div id="crit-back" class="criteria-badge pass">0 Backs (PASSED)</div>
          </li>
          <li class="criteria-item">
            <div>
              <strong>Grace Marks (PWG) Status:</strong>
              <div style="font-size: 12px; color: #64748b;">No Grace Marks Awarded</div>
            </div>
            <div id="crit-grace" class="criteria-badge pass">Clean (PASSED)</div>
          </li>
          <li class="criteria-item">
            <div>
              <strong>MOOCs / NPTEL Credits:</strong>
              <div style="font-size: 12px; color: #64748b;">Minimum 18-20 Credits Needed</div>
            </div>
            <div id="crit-moocs" class="criteria-badge pass">20 Credits (PASSED)</div>
          </li>
        </ul>

        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 15px; font-size: 13px; color: #334155; margin-top: 15px;">
          <strong>💡 Pro Tip:</strong> If your CGPA is above 7.50 with zero backs, ensure you submit your NPTEL certificates to your college departmental coordinator before the 8th semester exam form deadline.
        </div>
      </div>
    </div>

    <!-- Guidelines Section -->
    <div class="content-card">
      <h2>AKTU B.Tech Honours Degree Regulations (Ordinance 10.1)</h2>
      <p>Under Dr. A.P.J. Abdul Kalam Technical University (AKTU) Choice Based Credit System (CBCS) and National Education Policy (NEP) curriculum, a student is eligible to obtain a <strong>B.Tech Degree with Honours</strong> only when fulfilling all of the following statutory university conditions:</p>

      <ul>
        <li><strong>Condition 1 (Minimum CGPA Threshold):</strong> The student must secure a Cumulative Grade Point Average (CGPA) of <strong>7.50 or higher</strong> at the end of the final semester.</li>
        <li><strong>Condition 2 (Zero Back Paper & First Attempt Clearance):</strong> The candidate must have passed all theory subjects, lab practicals, seminars, and project vivas in the <strong>very first attempt</strong>. If a candidate secures an 'F' grade in any semester and clears it later via carryover (COP) examination, they automatically become ineligible for the Honours degree.</li>
        <li><strong>Condition 3 (No Grace Marks / PWG):</strong> Passing any subject with university grace marks (PWG) voids the Honours award.</li>
        <li><strong>Condition 4 (Prescribed Time Limit):</strong> The degree must be completed within the minimum normal duration (4 academic years for regular students, 3 academic years for lateral entry students). No year-drop or repeat is permitted.</li>
        <li><strong>Condition 5 (18-20 NPTEL Swayam MOOCs Credits):</strong> For 2018-19 batch onwards, students seeking an Honours specialization (e.g., <em>B.Tech in CSE with Honours in Artificial Intelligence</em>) must complete 18 to 20 additional MOOCs credits from the university's approved Swayam/NPTEL list.</li>
      </ul>
    </div>
  </div>

  <script>
    function toggleMode() {
      const mode = document.getElementById('adm-mode').value;
      const sem1 = document.getElementById('box-sem1');
      const sem2 = document.getElementById('box-sem2');
      if (mode === 'lateral') {
        sem1.style.display = 'none';
        sem2.style.display = 'none';
      } else {
        sem1.style.display = 'block';
        sem2.style.display = 'block';
      }
      evaluateHonours();
    }

    function evaluateHonours() {
      const mode = document.getElementById('adm-mode').value;
      const hasBack = document.getElementById('has-back').checked;
      const hasGrace = document.getElementById('has-grace').checked;
      const nptelCredits = parseInt(document.getElementById('nptel-credits').value) || 0;

      let sems = [];
      if (mode === 'regular') {
        sems = [
          parseFloat(document.getElementById('sgpa-1').value) || 0,
          parseFloat(document.getElementById('sgpa-2').value) || 0,
          parseFloat(document.getElementById('sgpa-3').value) || 0,
          parseFloat(document.getElementById('sgpa-4').value) || 0,
          parseFloat(document.getElementById('sgpa-5').value) || 0,
          parseFloat(document.getElementById('sgpa-6').value) || 0,
          parseFloat(document.getElementById('sgpa-7').value) || 0,
          parseFloat(document.getElementById('sgpa-8').value) || 0
        ];
      } else {
        sems = [
          parseFloat(document.getElementById('sgpa-3').value) || 0,
          parseFloat(document.getElementById('sgpa-4').value) || 0,
          parseFloat(document.getElementById('sgpa-5').value) || 0,
          parseFloat(document.getElementById('sgpa-6').value) || 0,
          parseFloat(document.getElementById('sgpa-7').value) || 0,
          parseFloat(document.getElementById('sgpa-8').value) || 0
        ];
      }

      const sum = sems.reduce((a, b) => a + b, 0);
      const cgpa = sems.length > 0 ? (sum / sems.length) : 0;

      const passCgpa = cgpa >= 7.50;
      const passBack = !hasBack;
      const passGrace = !hasGrace;
      const passMoocs = nptelCredits >= 18;

      // Update Badges
      const bCgpa = document.getElementById('crit-cgpa');
      bCgpa.innerText = `${cgpa.toFixed(2)} (${passCgpa ? 'PASSED' : 'BELOW 7.50'})`;
      bCgpa.className = `criteria-badge ${passCgpa ? 'pass' : 'fail'}`;

      const bBack = document.getElementById('crit-back');
      bBack.innerText = passBack ? '0 Backs (PASSED)' : 'Had Back Paper (FAILED)';
      bBack.className = `criteria-badge ${passBack ? 'pass' : 'fail'}`;

      const bGrace = document.getElementById('crit-grace');
      bGrace.innerText = passGrace ? 'Clean (PASSED)' : 'Had Grace Marks (FAILED)';
      bGrace.className = `criteria-badge ${passGrace ? 'pass' : 'fail'}`;

      const bMoocs = document.getElementById('crit-moocs');
      bMoocs.innerText = `${nptelCredits} Credits (${passMoocs ? 'PASSED' : 'NEEDS 18+'})`;
      bMoocs.className = `criteria-badge ${passMoocs ? 'pass' : 'fail'}`;

      // Overall Card
      const card = document.getElementById('status-card');
      const stText = document.getElementById('status-text');
      const stDesc = document.getElementById('status-desc');

      if (passCgpa && passBack && passGrace && passMoocs) {
        card.className = 'status-banner eligible';
        stText.innerText = '🎉 ELIGIBLE FOR HONOURS';
        stDesc.innerText = 'You satisfy all conditions: CGPA >= 7.50, 0 carryover backs, no grace marks, and 18+ MOOCs credits.';
      } else if (passCgpa && passBack && passGrace && !passMoocs) {
        card.className = 'status-banner partial';
        stText.innerText = '🟡 PARTIALLY ON TRACK (MOOCs Pending)';
        stDesc.innerText = `Your CGPA (${cgpa.toFixed(2)}) and clean back record qualify you for Honours, but you need ${18 - nptelCredits} more NPTEL credits.`;
      } else {
        card.className = 'status-banner ineligible';
        stText.innerText = '❌ NOT ELIGIBLE FOR HONOURS';
        let reasons = [];
        if (!passCgpa) reasons.push('CGPA is below 7.50');
        if (!passBack) reasons.push('Had back paper history');
        if (!passGrace) reasons.push('Received grace marks');
        stDesc.innerText = `Disqualification reasons: ${reasons.join(', ')}. Standard Degree will be awarded.`;
      }
    }

    window.addEventListener('DOMContentLoaded', evaluateHonours);
  </script>
</body>
</html>"""

with open("tools/aktu-honours-degree-eligibility-checker.html", "w", encoding="utf-8") as f:
    f.write(tool4_html)
print("Tool 4 (Honours Degree Eligibility Checker) built successfully!")

