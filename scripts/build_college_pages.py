#!/usr/bin/env python3
import os

os.makedirs('colleges/profiles', exist_ok=True)

AD_TAGS = """    <meta name="monetag" content="4b20c6816d7cac00b3d6430a41d4d86f" />
    <script src="https://quge5.com/88/tag.min.js" data-zone="257546" async data-cfasync="false"></script>
    <script async="async" data-cfasync="false" src="https://pl30261454.effectivecpmnetwork.com/1018cdea726c22b2c7ca9bbd11cccba8/invoke.js"></script>
    <script>(function(s){s.dataset.zone='11257064',s.src='https://nap5k.com/tag.min.js'})([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement('script')))</script>"""

COLLEGES = [
    {"slug":"iet-lucknow-profile-2026","code":"052","name":"Institute of Engineering & Technology (IET)","short":"IET Lucknow","city":"Lucknow","district":"Lucknow","type":"Government (AKTU Constituent)","estd":"1984","campus_acres":"110","naac":"A+","nirf_rank":"151-200","address":"Sitapur Road, Lucknow - 226021, Uttar Pradesh","phone":"+91-522-2732183","email":"registrar@ietlucknow.ac.in","website":"https://www.ietlucknow.ac.in","linkedin":"https://www.linkedin.com/school/iet-lucknow/","twitter":"https://twitter.com/ietlucknow","facebook":"https://www.facebook.com/ietlucknow","instagram":"https://www.instagram.com/ietlucknow_official","youtube":"https://www.youtube.com/@IETLucknow","total_intake":750,"highest_pkg":"49 LPA","avg_pkg_cse":"10.5 LPA","placement_pct":94,"top_recruiters":["Amazon","Google","Microsoft","Paytm","Wipro","Infosys","TCS Digital","Capgemini","IBM","Oracle"],"clubs":["Robotics Club","Coding Club SIGMA","NSS IET","IEEE Student Branch","Literary Club","Photography Club","Drama Club Abhinay","Sports Club","E-Cell IET","ACM Student Chapter"],"fee_tuition":85000,"fee_hostel_single":45000,"fee_hostel_double":35000,"fee_mess":36000,"fee_dev":5000,"branches":[{"name":"Computer Science & Engineering (CSE)","intake":180,"hod":"Prof. R.K. Sharma","grade":"A Grade"},{"name":"Electronics & Communication Engineering (ECE)","intake":120,"hod":"Prof. Meera Singh","grade":"A Grade"},{"name":"Mechanical Engineering (ME)","intake":120,"hod":"Prof. A.K. Pandey","grade":"A- Grade"},{"name":"Civil Engineering (CE)","intake":90,"hod":"Prof. S.P. Tiwari","grade":"B+ Grade"},{"name":"Electrical Engineering (EE)","intake":90,"hod":"Prof. Vinod Kumar","grade":"A- Grade"},{"name":"Information Technology (IT)","intake":90,"hod":"Prof. Priya Gupta","grade":"A Grade"}],"about":"Established in 1984, IET Lucknow is one of the oldest government engineering colleges in UP. Spread across 110 acres on Sitapur Road, it holds NAAC A+ accreditation and is a constituent college of AKTU Lucknow. Known for outstanding placements (49 LPA highest package) and research output.","infra":"110-acre green campus with 18 academic buildings, 14 research labs, central library with 1.2 lakh books, 1500-seat auditorium, 8 hostel blocks, sports complex with cricket ground, basketball and badminton courts, indoor stadium, 24/7 WiFi, medical clinic, and canteen."},
    {"slug":"jss-noida-profile-2026","code":"091","name":"JSS Academy of Technical Education","short":"JSS Noida","city":"Noida","district":"Gautam Buddha Nagar","type":"Private (AKTU Affiliated)","estd":"1998","campus_acres":"28","naac":"A","nirf_rank":"101-150","address":"C-20/1, Sector-62, Noida - 201301, Uttar Pradesh","phone":"+91-120-4573842","email":"admission@jssaten.ac.in","website":"https://www.jssaten.ac.in","linkedin":"https://www.linkedin.com/school/jss-academy-of-technical-education/","twitter":"https://twitter.com/JSSNoida","facebook":"https://www.facebook.com/jssaten","instagram":"https://www.instagram.com/jssaten_official","youtube":"https://www.youtube.com/@JSSAcademy","total_intake":1020,"highest_pkg":"57 LPA","avg_pkg_cse":"9.8 LPA","placement_pct":92,"top_recruiters":["Adobe","Amazon","Cisco","TCS Digital","Palo Alto Networks","Commvault","Infosys SP","Wipro Elite","HCL Tech","Persistent Systems"],"clubs":["OWASP JSS Chapter","Coding Club JSS","IEEE JSS Branch","E-Cell JSS","NSS","Sports Committee","Photographic Society","Literary Club","Music Club","Drama Society"],"fee_tuition":138000,"fee_hostel_single":55000,"fee_hostel_double":42000,"fee_mess":42000,"fee_dev":8000,"branches":[{"name":"Computer Science & Engineering (CSE)","intake":240,"hod":"Dr. Sanjeev Sharma","grade":"A+ Grade"},{"name":"CSE (Artificial Intelligence & ML)","intake":120,"hod":"Dr. Anita Rawat","grade":"A+ Grade"},{"name":"Electronics & Communication Engineering (ECE)","intake":180,"hod":"Dr. P.K. Verma","grade":"A Grade"},{"name":"Mechanical Engineering (ME)","intake":120,"hod":"Dr. R.S. Patel","grade":"A Grade"},{"name":"Information Technology (IT)","intake":120,"hod":"Dr. Nidhi Jain","grade":"A+ Grade"},{"name":"Civil Engineering (CE)","intake":120,"hod":"Dr. V.K. Singh","grade":"A- Grade"}],"about":"JSS Academy of Technical Education (JSSATEN), Noida is one of the most reputed AKTU-affiliated private engineering colleges in Delhi-NCR. Founded in 1998 under JSS Mahavidyapeetha, Mysuru. Known for a highest placement of 57 LPA (Palo Alto Networks) and strong NAAC-A accreditation.","infra":"28-acre Sector 62 Noida campus with central library (90,000+ volumes), 12 specialised labs, Cisco Networking Lab, Data Science Centre, Cloud Computing Lab, 1000-seat seminar hall, boys and girls hostel blocks, gymnasium, and round-the-clock security."},
    {"slug":"kiet-ghaziabad-profile-2026","code":"029","name":"KIET Group of Institutions","short":"KIET Ghaziabad","city":"Ghaziabad","district":"Ghaziabad","type":"Autonomous (AKTU Affiliated)","estd":"1998","campus_acres":"18","naac":"A+","nirf_rank":"76-100","address":"13 Km Stone, Delhi-Hapur Bypass Road, Ghaziabad - 201206, UP","phone":"+91-120-2795042","email":"admissions@kiet.edu","website":"https://www.kiet.edu","linkedin":"https://www.linkedin.com/school/kiet-group-of-institutions/","twitter":"https://twitter.com/kietinstitution","facebook":"https://www.facebook.com/kietinstitutions","instagram":"https://www.instagram.com/kiet_institutions","youtube":"https://www.youtube.com/@KIETInstitutions","total_intake":1440,"highest_pkg":"48.5 LPA","avg_pkg_cse":"8.9 LPA","placement_pct":93,"top_recruiters":["Atlassian","Capgemini","Infosys","Wipro","TCS","HCL","Accenture","Tech Mahindra","Cognizant","Oracle"],"clubs":["GDSC KIET","Coding Warriors","IEEE KIET Chapter","NSS KIET","Entrepreneurship Cell","KIET Photography Club","Sports Council","Drama Club","Music Society","KIET Robotics Club"],"fee_tuition":139000,"fee_hostel_single":58000,"fee_hostel_double":44000,"fee_mess":40000,"fee_dev":9000,"branches":[{"name":"Computer Science & Engineering (CSE)","intake":360,"hod":"Dr. A.K. Garg","grade":"A+ Grade"},{"name":"CSE (Data Science)","intake":120,"hod":"Dr. Neha Arora","grade":"A+ Grade"},{"name":"Electronics & Communication Engineering","intake":180,"hod":"Dr. S.K. Dixit","grade":"A Grade"},{"name":"Mechanical Engineering","intake":180,"hod":"Dr. P.K. Jain","grade":"A Grade"},{"name":"Information Technology","intake":180,"hod":"Dr. R. Bhatia","grade":"A Grade"},{"name":"Civil Engineering","intake":120,"hod":"Dr. V. Sharma","grade":"B+ Grade"},{"name":"Biotechnology","intake":60,"hod":"Dr. M. Singh","grade":"B Grade"},{"name":"B.Pharma","intake":60,"hod":"Dr. S. Agarwal","grade":"B Grade"}],"about":"KIET Group of Institutions, Ghaziabad is a NAAC A+ accredited autonomous college affiliated to AKTU. Founded in 1998, KIET consistently ranks NIRF 76-100. Its record 48.5 LPA placement by Atlassian and Microsoft Innovation Centre establish it as one of north India's premier tech institutes.","infra":"18 acres near Delhi-Hapur bypass with 40+ specialized labs, Microsoft Innovation Centre, Industry 4.0 IoT Lab, incubation centre, 3 hostel blocks, food court, swimming pool, cricket ground, and 2000-seat auditorium."},
    {"slug":"akgec-ghaziabad-profile-2026","code":"027","name":"Ajay Kumar Garg Engineering College","short":"AKGEC Ghaziabad","city":"Ghaziabad","district":"Ghaziabad","type":"Autonomous (AKTU Affiliated)","estd":"1998","campus_acres":"40","naac":"A","nirf_rank":"101-150","address":"27th KM Stone, Delhi-Meerut Expressway, Ghaziabad - 201009, UP","phone":"+91-120-2675740","email":"admissions@akgec.ac.in","website":"https://www.akgec.ac.in","linkedin":"https://www.linkedin.com/school/akgec/","twitter":"https://twitter.com/AKGEC_Official","facebook":"https://www.facebook.com/akgec","instagram":"https://www.instagram.com/akgec_official","youtube":"https://www.youtube.com/@AKGECOfficial","total_intake":1260,"highest_pkg":"1.13 CPA (Intl.) / 44 LPA Dom.","avg_pkg_cse":"8.5 LPA","placement_pct":91,"top_recruiters":["Amazon","Microsoft","IBM","Infosys","TCS Digital","Wipro","HCL","Capgemini","Goldman Sachs","JP Morgan"],"clubs":["AKGEC Coding Club","IEEE AKGEC","Robotics Society","Photography Club","Literary Society","NSS","NCC","Sports Council","E-Cell","ACM AKGEC Chapter"],"fee_tuition":141000,"fee_hostel_single":60000,"fee_hostel_double":46000,"fee_mess":42000,"fee_dev":10000,"branches":[{"name":"Computer Science & Engineering (CSE)","intake":300,"hod":"Dr. Pankaj Agarwal","grade":"A Grade"},{"name":"CSE (Artificial Intelligence)","intake":120,"hod":"Dr. Shweta Singh","grade":"A Grade"},{"name":"Electronics & Communication Engineering","intake":180,"hod":"Dr. K.K. Gupta","grade":"A- Grade"},{"name":"Mechanical Engineering","intake":180,"hod":"Dr. Y.P. Singh","grade":"A- Grade"},{"name":"Information Technology","intake":120,"hod":"Dr. Priti Sharma","grade":"A Grade"},{"name":"Civil Engineering","intake":90,"hod":"Dr. A. Verma","grade":"B+ Grade"},{"name":"Electrical Engineering","intake":120,"hod":"Dr. Rakesh Gupta","grade":"B+ Grade"}],"about":"AKGEC Ghaziabad is a NAAC-A accredited autonomous college affiliated to AKTU. Established in 1998, its record international placement of 1.13 CPA and tie-ups with IBM, Microsoft, and AWS make it one of NCR's top engineering colleges. Spread across 40 acres on Delhi-Meerut Expressway.","infra":"40 acres on Delhi-Meerut Expressway with NVIDIA GPU lab, Microsoft Azure Cloud Centre, 5 AC academic blocks, 3 hostel complexes, food court, full-size football ground, basketball courts, and a central library with DELNET and NDL access."},
    {"slug":"gl-bajaj-greater-noida-profile-2026","code":"192","name":"GL Bajaj Institute of Technology & Management","short":"GL Bajaj Gr. Noida","city":"Greater Noida","district":"Gautam Buddha Nagar","type":"Private (AKTU Affiliated)","estd":"2007","campus_acres":"20","naac":"A+","nirf_rank":"76-100","address":"Plot No. 2, Knowledge Park III, Greater Noida - 201306, UP","phone":"+91-120-2323821","email":"info@glbitm.ac.in","website":"https://www.glbitm.ac.in","linkedin":"https://www.linkedin.com/school/gl-bajaj-institute/","twitter":"https://twitter.com/GLBajajInst","facebook":"https://www.facebook.com/glbitm","instagram":"https://www.instagram.com/glbitm_official","youtube":"https://www.youtube.com/@GLBajajInstitute","total_intake":1380,"highest_pkg":"58 LPA","avg_pkg_cse":"8.6 LPA","placement_pct":95,"top_recruiters":["Palo Alto Networks","Commvault","Capgemini","Cognizant","Infosys","TCS","Wipro","Tech Mahindra","Amazon","Mindtree"],"clubs":["GDSC GL Bajaj","CodeChef Chapter","Photography Club","NSS","Entrepreneurship Cell","IEEE Branch","Literary Society","Music & Arts Club","Sports Council","Debate Club"],"fee_tuition":128000,"fee_hostel_single":52000,"fee_hostel_double":40000,"fee_mess":38000,"fee_dev":7500,"branches":[{"name":"Computer Science & Engineering (CSE)","intake":360,"hod":"Dr. Rajesh Kumar","grade":"A+ Grade"},{"name":"CSE (AI & ML)","intake":120,"hod":"Dr. Sanjay Mishra","grade":"A+ Grade"},{"name":"CSE (Data Science)","intake":60,"hod":"Dr. Priya Tiwari","grade":"A Grade"},{"name":"Electronics & Communication Engineering","intake":180,"hod":"Dr. O.P. Singh","grade":"A Grade"},{"name":"Mechanical Engineering","intake":180,"hod":"Dr. S.K. Verma","grade":"A- Grade"},{"name":"Information Technology","intake":180,"hod":"Dr. Anita Singh","grade":"A Grade"},{"name":"Civil Engineering","intake":120,"hod":"Dr. K.L. Gupta","grade":"B+ Grade"},{"name":"MBA","intake":120,"hod":"Dr. Neeraj Agarwal","grade":"B Grade"}],"about":"GL Bajaj Institute of Technology and Management (GLBITM), Greater Noida is a NAAC A+ accredited AKTU-affiliated college with highest placement of 58 LPA by Palo Alto Networks and 95% placement rate — best among private AKTU colleges in the Gr. Noida cluster. Established in 2007, part of GL Bajaj Group.","infra":"20-acre Knowledge Park III campus with 10 academic blocks, 6-storey AC library, Palo Alto Cyber Security Lab, Google Developer Lab, AI & ML research centre, 5 hostel blocks (2000+ capacity), rooftop gardens, and 1500-seat convention centre."},
    {"slug":"knit-sultanpur-profile-2026","code":"104","name":"Kamla Nehru Institute of Technology (KNIT)","short":"KNIT Sultanpur","city":"Sultanpur","district":"Sultanpur","type":"Government Autonomous (AKTU Constituent)","estd":"1962","campus_acres":"95","naac":"A","nirf_rank":"151-200","address":"Chandrapur Road, Sultanpur - 228118, Uttar Pradesh","phone":"+91-5362-240454","email":"registrar@knitnit.ac.in","website":"https://www.knitnit.ac.in","linkedin":"https://www.linkedin.com/school/knit-sultanpur/","twitter":"https://twitter.com/KNIT_Sultanpur","facebook":"https://www.facebook.com/KNITsultanpur","instagram":"https://www.instagram.com/knit_sultanpur","youtube":"https://www.youtube.com/@KNITSultanpur","total_intake":660,"highest_pkg":"45 LPA","avg_pkg_cse":"9.2 LPA","placement_pct":88,"top_recruiters":["Amazon","Samsung","Infosys","TCS","Wipro","L&T Technology","Tata Steel","BHEL","SAIL","ONGC"],"clubs":["Robotics Club KNIT","IEEE Student Branch","NSS","NCC","Coding Society","Photography Club","Literary Club Vyangya","Sports Club","E-Cell KNIT","Drama Society"],"fee_tuition":64350,"fee_hostel_single":38000,"fee_hostel_double":28000,"fee_mess":30000,"fee_dev":3500,"branches":[{"name":"Computer Science & Engineering","intake":120,"hod":"Prof. Dhruv Pandey","grade":"A Grade"},{"name":"Electronics & Communication Engineering","intake":120,"hod":"Prof. R.C. Tiwari","grade":"A- Grade"},{"name":"Mechanical Engineering","intake":120,"hod":"Prof. A.N. Mishra","grade":"A- Grade"},{"name":"Civil Engineering","intake":120,"hod":"Prof. S.P. Srivastava","grade":"B+ Grade"},{"name":"Electrical Engineering","intake":120,"hod":"Prof. V.K. Tiwari","grade":"B+ Grade"},{"name":"Information Technology","intake":60,"hod":"Prof. K.K. Gupta","grade":"A- Grade"}],"about":"KNIT Sultanpur is one of the oldest government engineering colleges in UP, established in 1962. As an AKTU constituent autonomous college on a 95-acre campus, it delivers near-NIT quality education at just Rs 64,350/year. NAAC-A accredited with a 45 LPA highest placement record by Amazon.","infra":"95-acre campus with 12 departments, heritage central library (1 lakh+ volumes), 22 research labs, 8 hostel blocks (boys and girls), cricket ground, indoor stadium, swimming pool, health centre, alumni guest house, and 2000-seat academic auditorium."},
    {"slug":"abes-engineering-ghaziabad-profile-2026","code":"032","name":"ABES Engineering College","short":"ABES EC Ghaziabad","city":"Ghaziabad","district":"Ghaziabad","type":"Autonomous (AKTU Affiliated)","estd":"2000","campus_acres":"23","naac":"A","nirf_rank":"201-300","address":"19th KM Stone, NH-58, Ghaziabad - 201009, Uttar Pradesh","phone":"+91-120-2794580","email":"info@abes.ac.in","website":"https://www.abes.ac.in","linkedin":"https://www.linkedin.com/school/abes-engineering-college/","twitter":"https://twitter.com/ABESCollege","facebook":"https://www.facebook.com/abes.ac.in","instagram":"https://www.instagram.com/abes_engineering","youtube":"https://www.youtube.com/@ABESEngineering","total_intake":1140,"highest_pkg":"50 LPA","avg_pkg_cse":"8.2 LPA","placement_pct":90,"top_recruiters":["Microsoft","Google","Amazon","TCS Digital","Infosys","Wipro","Capgemini","Accenture","Cognizant","HCL"],"clubs":["ABES Coding Club","IEEE ABES","GDSC ABES","Photography Society","NSS Unit","E-Cell","Sports Council","Drama Club","Music Club","ABES Robotics"],"fee_tuition":135000,"fee_hostel_single":55000,"fee_hostel_double":42000,"fee_mess":40000,"fee_dev":8500,"branches":[{"name":"CSE","intake":300,"hod":"Dr. Vikas Saxena","grade":"A Grade"},{"name":"CSE (AI & ML)","intake":120,"hod":"Dr. Anjali Singh","grade":"A Grade"},{"name":"ECE","intake":180,"hod":"Dr. P.K. Gupta","grade":"A- Grade"},{"name":"IT","intake":180,"hod":"Dr. Rahul Agarwal","grade":"A- Grade"},{"name":"ME","intake":180,"hod":"Dr. Sushil Kumar","grade":"B+ Grade"},{"name":"CE","intake":90,"hod":"Dr. Deepak Verma","grade":"B Grade"}],"about":"ABES Engineering College, Ghaziabad is a NAAC-A accredited autonomous college affiliated to AKTU. Founded in 2000, its Google Developer Student Club and Microsoft Learn Student Ambassador chapters make it a tech-first campus. 50 LPA highest package demonstrates strong industry connections.","infra":"23-acre campus near NH-58 with 8 academic blocks, central library, AWS and Google Cloud Labs, incubation centre, 2 hostel blocks, food court, cricket and basketball courts, indoor gym, and 1200-seat auditorium."},
    {"slug":"psit-kanpur-profile-2026","code":"164","name":"Pranveer Singh Institute of Technology","short":"PSIT Kanpur","city":"Kanpur","district":"Kanpur Dehat","type":"Autonomous (AKTU Affiliated)","estd":"2006","campus_acres":"42","naac":"A","nirf_rank":"201-300","address":"Bhauti, NH-25, Kanpur - 209305, Uttar Pradesh","phone":"+91-9839099090","email":"admission@psit.ac.in","website":"https://www.psit.ac.in","linkedin":"https://www.linkedin.com/school/psit-kanpur/","twitter":"https://twitter.com/PSITKanpur","facebook":"https://www.facebook.com/psitkanpur","instagram":"https://www.instagram.com/psit_kanpur","youtube":"https://www.youtube.com/@PSITKanpur","total_intake":1260,"highest_pkg":"40 LPA","avg_pkg_cse":"7.8 LPA","placement_pct":88,"top_recruiters":["TCS","Infosys","Wipro","HCL","Tech Mahindra","Capgemini","Cognizant","Mindtree","Mphasis","L&T Infotech"],"clubs":["PSIT Coding Club","IEEE Chapter","NSS","NCC","Photography Club","E-Cell","Sports Council","Literary Club","Drama Society","Music Club"],"fee_tuition":120000,"fee_hostel_single":50000,"fee_hostel_double":38000,"fee_mess":36000,"fee_dev":7000,"branches":[{"name":"CSE","intake":300,"hod":"Dr. Akash Srivastava","grade":"A- Grade"},{"name":"CSE (AI & ML)","intake":120,"hod":"Dr. Priya Mishra","grade":"A- Grade"},{"name":"ECE","intake":180,"hod":"Dr. R.K. Sharma","grade":"B+ Grade"},{"name":"ME","intake":180,"hod":"Dr. S.K. Verma","grade":"B+ Grade"},{"name":"CE","intake":120,"hod":"Dr. V.K. Tiwari","grade":"B Grade"},{"name":"IT","intake":120,"hod":"Dr. Neha Gupta","grade":"A- Grade"},{"name":"MBA","intake":120,"hod":"Dr. Ashok Pandey","grade":"B Grade"}],"about":"PSIT Kanpur is the top AKTU-affiliated autonomous engineering college in the Kanpur region. NAAC-A accredited, spread across 42 acres on NH-25. Oracle University Centre and IBM SkillsBuild Centre on campus. 40 LPA highest placement. TCS, Infosys, Wipro are anchor recruiters with 88% placement rate.","infra":"42-acre campus with 6 AC academic buildings, 26 advanced labs, Oracle University Centre, IBM SkillsBuild Centre, 4 hostel blocks (1600+ beds), gymnasium, cricket ground, basketball courts, food court, health centre, and 1400-seat convention hall."},
    {"slug":"niet-greater-noida-profile-2026","code":"118","name":"Noida Institute of Engineering & Technology","short":"NIET Gr. Noida","city":"Greater Noida","district":"Gautam Buddha Nagar","type":"Autonomous (AKTU Affiliated)","estd":"2001","campus_acres":"25","naac":"A","nirf_rank":"201-300","address":"19 Knowledge Park II, Greater Noida - 201306, Uttar Pradesh","phone":"+91-120-2323900","email":"admission@niet.co","website":"https://www.niet.co","linkedin":"https://www.linkedin.com/school/niet-greater-noida/","twitter":"https://twitter.com/NIETGreaterNoida","facebook":"https://www.facebook.com/niet.co","instagram":"https://www.instagram.com/niet_greaternodida","youtube":"https://www.youtube.com/@NIETGreaterNoida","total_intake":1320,"highest_pkg":"44 LPA","avg_pkg_cse":"8.0 LPA","placement_pct":91,"top_recruiters":["Samsung R&D","TCS Digital","Infosys","Capgemini","Wipro","HCL","Cognizant","Amazon","Tech Mahindra","Paytm"],"clubs":["NIET Coding Hub","IEEE NIET","GDSC NIET","Photography Society","NSS","E-Cell NIET","Music Club","Drama Society","Sports Council","Literary Circle"],"fee_tuition":130000,"fee_hostel_single":54000,"fee_hostel_double":41000,"fee_mess":39000,"fee_dev":8000,"branches":[{"name":"CSE","intake":360,"hod":"Dr. Sandeep Arora","grade":"A Grade"},{"name":"CSE (Cyber Security)","intake":120,"hod":"Dr. Ritu Gupta","grade":"A Grade"},{"name":"ECE","intake":180,"hod":"Dr. Pankaj Goel","grade":"A- Grade"},{"name":"ME","intake":180,"hod":"Dr. S. Prasad","grade":"B+ Grade"},{"name":"IT","intake":180,"hod":"Dr. Divya Singh","grade":"A Grade"},{"name":"CE","intake":120,"hod":"Dr. Atul Kumar","grade":"B Grade"},{"name":"EEE","intake":60,"hod":"Dr. Meena Tiwari","grade":"B Grade"}],"about":"NIET Greater Noida is a NAAC-A accredited autonomous college affiliated to AKTU. Founded in 2001, it is one of the largest AKTU colleges by intake (1320 seats). Its Cyber Security branch and Samsung R&D partnership make it distinctive. 44 LPA highest package, 91% placement rate.","infra":"25-acre Knowledge Park II campus with 8 academic blocks, Samsung Innovation Lab, Amazon Web Services Academy, 2-storey central library, 35 specialised labs, 5 hostel blocks (2200+ capacity), food court, gymnasium, clinic, and 2400-seat convention centre."},
]

def page(c):
    br = "".join([f'<tr><td style="padding:12px 15px; border-bottom:1px solid #e2e8f0; font-weight:600;">{b["name"]}</td><td style="padding:12px 15px; border-bottom:1px solid #e2e8f0; text-align:center;">{b["intake"]}</td><td style="padding:12px 15px; border-bottom:1px solid #e2e8f0;">{b["hod"]}</td><td style="padding:12px 15px; border-bottom:1px solid #e2e8f0; text-align:center;"><span style="background:#e0e7ff; color:#3730a3; padding:3px 10px; border-radius:12px; font-size:12px; font-weight:700;">{b["grade"]}</span></td></tr>' for b in c["branches"]])
    rec = "".join([f'<span style="background:#f1f5f9; color:#475569; padding:5px 12px; border-radius:20px; font-size:13px; font-weight:600; display:inline-block; margin:3px;">{r}</span>' for r in c["top_recruiters"]])
    clu = "".join([f'<li style="padding:5px 0; border-bottom:1px solid #f1f5f9;">{cl}</li>' for cl in c["clubs"]])
    tot = c["fee_tuition"] + c["fee_hostel_double"] + c["fee_mess"] + c["fee_dev"]

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{c["name"]} ({c["code"]}) {c["city"]} | Fees, Placements, Branches & Cutoff | Updated Annually</title>
<meta name="description" content="Complete 2026 guide for {c["short"]} (AKTU Code {c["code"]}). Verified fee structure (Rs {c["fee_tuition"]:,}/yr), hostel charges, branch-wise intake, {c["highest_pkg"]} highest package, NIRF {c["nirf_rank"]}, NAAC {c["naac"]}, top recruiters & campus life." />
<meta name="keywords" content="{c["short"].lower()} fees 2026, {c["short"].lower()} placement, aktu code {c["code"]} cutoff, {c["short"].lower()} hostel fee, {c["short"].lower()} branches, {c["short"].lower()} nirf ranking, {c["short"].lower()} admission 2026, {c["city"].lower()} engineering college aktu" />
<link rel="canonical" href="https://akturesults.in/colleges/profiles/{c["slug"]}.html" />
<meta name="robots" content="index, follow" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet" />
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"EducationalOrganization","name":"{c["name"]}","alternateName":"{c["short"]}","url":"{c["website"]}","description":"{c["about"][:200]}","address":{{"@type":"PostalAddress","streetAddress":"{c["address"]}","addressLocality":"{c["city"]}","addressRegion":"Uttar Pradesh","addressCountry":"IN"}},"telephone":"{c["phone"]}","email":"{c["email"]}"}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://akturesults.in/"}},{{"@type":"ListItem","position":2,"name":"Colleges","item":"https://akturesults.in/colleges/"}},{{"@type":"ListItem","position":3,"name":"{c["short"]}","item":"https://akturesults.in/colleges/profiles/{c["slug"]}.html"}}]}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"What is the fee at {c["short"]} 2026?","acceptedAnswer":{{"@type":"Answer","text":"Tuition fee Rs {c["fee_tuition"]:,}/yr, hostel Rs {c["fee_hostel_double"]:,}/yr, mess Rs {c["fee_mess"]:,}/yr. Total ~Rs {tot:,}/yr."}}}},{{"@type":"Question","name":"Highest package at {c["short"]}?","acceptedAnswer":{{"@type":"Answer","text":"Highest package is {c["highest_pkg"]}. Avg CSE package is {c["avg_pkg_cse"]} with {c["placement_pct"]}% placement."}}}}]}}</script>
{AD_TAGS}
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
<nav class="bc"><div class="wrap"><a href="/">Home</a><span>›</span><a href="/colleges/">Colleges</a><span>›</span><span>{c["short"]}</span></div></nav>

<section class="hero"><div class="wrap">
<div class="hero-top">
<div class="logo-box">🏛️</div>
<div><h1>{c["name"]}</h1><div class="hero-meta">📍 {c["address"]}</div></div>
</div>
<div class="badges">
<span class="badge">Code: {c["code"]}</span>
<span class="badge">NAAC {c["naac"]}</span>
<span class="badge">AICTE Approved</span>
<span class="badge">{c["type"]}</span>
<span class="badge">Est. {c["estd"]}</span>
<span class="badge">{c["campus_acres"]} Acre Campus</span>
</div>
<div class="stats">
<div class="stat"><div class="stat-v" style="color:#4ade80;">{c["highest_pkg"]}</div><div class="stat-l">Highest Package</div></div>
<div class="stat"><div class="stat-v">{c["avg_pkg_cse"]}</div><div class="stat-l">Avg CSE Package</div></div>
<div class="stat"><div class="stat-v">{c["placement_pct"]}%</div><div class="stat-l">Placement Rate</div></div>
<div class="stat"><div class="stat-v">{c["total_intake"]:,}</div><div class="stat-l">Total Intake</div></div>
<div class="stat"><div class="stat-v">NIRF</div><div class="stat-l">{c["nirf_rank"]}</div></div>
</div>
</div></section>

<div class="wrap" style="margin-top:22px;">

<div class="card">
<h2 class="ctitle">📖 About {c["short"]}</h2>
<p>{c["about"]}</p>
<p style="margin-top:12px;"><strong>Infrastructure:</strong> {c["infra"]}</p>
</div>

<div class="card">
<h2 class="ctitle">🏆 Rankings & Accreditation</h2>
<div class="rg">
<div class="rc"><div class="rv">{c["naac"]}</div><div class="rl">NAAC Grade 2024</div></div>
<div class="rc"><div class="rv">{c["nirf_rank"]}</div><div class="rl">NIRF Engg Band</div></div>
<div class="rc"><div class="rv">✅</div><div class="rl">AICTE Approved 2026</div></div>
<div class="rc"><div class="rv">AKTU</div><div class="rl">University Affiliation</div></div>
</div>
</div>

<div class="card">
<h2 class="ctitle">💰 Complete Fee Structure 2026-27</h2>
<div style="overflow-x:auto;">
<table class="ft">
<thead><tr><th>Fee Component</th><th>Amount / Year</th><th>Notes</th></tr></thead>
<tbody>
<tr><td><strong>B.Tech Tuition Fee</strong></td><td style="color:#16a34a;font-weight:700;">₹{c["fee_tuition"]:,}</td><td>All branches: CSE, ECE, ME, CE, IT</td></tr>
<tr><td><strong>Hostel (Single Room)</strong></td><td>₹{c["fee_hostel_single"]:,}</td><td>Limited seats, first-come basis</td></tr>
<tr><td><strong>Hostel (Double Sharing)</strong></td><td>₹{c["fee_hostel_double"]:,}</td><td>Standard allocation for freshers</td></tr>
<tr><td><strong>Mess / Food Charges</strong></td><td>₹{c["fee_mess"]:,}</td><td>Annual mess (veg + non-veg options)</td></tr>
<tr><td><strong>Development & Exam Fee</strong></td><td>₹{c["fee_dev"]:,}</td><td>AKTU exam + student development</td></tr>
<tr><td><strong>Total (Hostel Student)</strong></td><td>₹{tot:,}</td><td>Per year with double sharing hostel</td></tr>
<tr><td><strong>Total 4-Year B.Tech</strong></td><td>₹{tot*4:,}</td><td>Complete degree estimated cost</td></tr>
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
<tbody>{br}</tbody>
</table>
</div>
</div>

<div class="card">
<h2 class="ctitle">💼 Latest Placements — Companies & Packages</h2>
<div class="rg" style="margin-bottom:16px;">
<div class="rc"><div class="rv" style="color:#16a34a;">{c["highest_pkg"]}</div><div class="rl">Highest Package</div></div>
<div class="rc"><div class="rv">{c["avg_pkg_cse"]}</div><div class="rl">Avg CSE Package</div></div>
<div class="rc"><div class="rv">{c["placement_pct"]}%</div><div class="rl">Students Placed</div></div>
</div>
<h3 style="font-size:15px;font-weight:700;margin-bottom:9px;">🏢 Top Visiting Recruiters (Latest Campus Drive):</h3>
<div>{rec}</div>
<div style="margin-top:13px;background:#f0fdf4;border-left:4px solid #16a34a;padding:13px;border-radius:8px;">
<p style="font-size:13px;"><strong>Tier 1 Product MNCs:</strong> Amazon, Google, Microsoft, Adobe — ₹12 LPA to ₹50+ LPA</p>
<p style="font-size:13px;margin-top:5px;"><strong>Tier 2 IT Services:</strong> TCS Digital, Infosys SP, Wipro Elite — ₹6.5–10 LPA</p>
<p style="font-size:13px;margin-top:5px;"><strong>Mass Recruiters:</strong> TCS, Infosys, Wipro, Capgemini — ₹3.5–5.5 LPA base CTC</p>
</div>
</div>

<div class="card">
<h2 class="ctitle">🎯 Campus Clubs & Student Life</h2>
<ul class="clist">{clu}</ul>
</div>

<div class="card">
<h2 class="ctitle">📞 Contact Information</h2>
<div class="cg">
<div class="ci"><div style="font-size:20px;">📍</div><div><div class="clbl">Address</div><div class="cval">{c["address"]}</div></div></div>
<div class="ci"><div style="font-size:20px;">📱</div><div><div class="clbl">Phone</div><div class="cval"><a href="tel:{c["phone"]}">{c["phone"]}</a></div></div></div>
<div class="ci"><div style="font-size:20px;">✉️</div><div><div class="clbl">Email</div><div class="cval"><a href="mailto:{c["email"]}">{c["email"]}</a></div></div></div>
<div class="ci"><div style="font-size:20px;">🌐</div><div><div class="clbl">Official Website</div><div class="cval"><a href="{c["website"]}" target="_blank" rel="noopener">{c["website"]}</a></div></div></div>
</div>
</div>

<div class="card">
<h2 class="ctitle">🔗 Official Social Media</h2>
<div class="socbar">
<a href="{c["website"]}" class="sbtn s1" target="_blank" rel="noopener">🌐 Website</a>
<a href="{c["linkedin"]}" class="sbtn s2" target="_blank" rel="noopener">in LinkedIn</a>
<a href="{c["twitter"]}" class="sbtn s3" target="_blank" rel="noopener">𝕏 Twitter</a>
<a href="{c["facebook"]}" class="sbtn s4" target="_blank" rel="noopener">f Facebook</a>
<a href="{c["instagram"]}" class="sbtn s5" target="_blank" rel="noopener">📸 Instagram</a>
<a href="{c["youtube"]}" class="sbtn s6" target="_blank" rel="noopener">▶ YouTube</a>
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
<p>© 2026 <a href="/">AKTU Results Portal</a> — Independent student resource for AKTU &amp; UPTAC 2026</p>
<p style="margin-top:5px;opacity:.7;font-size:12px;">Disclaimer: Fee and placement figures sourced from publicly available college reports. Verify with the official college website before decisions.</p>
</div></footer>
<script defer src="/js/community-banner-widget.js"></script>
</body></html>"""

created = 0
for c in COLLEGES:
    fp = f'colleges/profiles/{c["slug"]}.html'
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(page(c))
    created += 1
    print(f"  Created: {fp}")

print(f"\nTotal: {created} profiles generated!")
