import os

dept_pages = [
    {
        'filename': 'jss-noida-cse-department.html',
        'college_name': 'JSS Academy of Technical Education, Noida',
        'short_name': 'JSS Noida',
        'dept_name': 'Computer Science & Engineering (CSE)',
        'hod_name': 'Dr. Sanjeev Sharma',
        'intake': '240 Seats + 120 AI/ML',
        'highest_pkg': '57 LPA',
        'avg_pkg': '9.8 LPA',
        'placed_pct': '92%',
        'recruiters': 'Adobe, Amazon, Cisco, TCS Digital, Palo Alto Networks, Commvault, Infosys SP, Wipro Elite',
        'hod_quote': 'Our Department of Computer Science & Engineering is committed to nurturing industry-ready software engineers and innovators through cutting-edge research, hands-on lab projects, and active tech chapters including OWASP and IEEE.',
        'faculty': [
            ('Dr. Sanjeev Sharma', 'Professor & HOD', 'Cloud Computing & Distributed Systems', 'Ph.D. (IIT Roorkee)'),
            ('Dr. Anita Rawat', 'Professor', 'Artificial Intelligence & Deep Learning', 'Ph.D. (AKTU)'),
            ('Dr. P.K. Verma', 'Associate Professor', 'Network Security & Cryptography', 'Ph.D. (MNIT)'),
            ('Dr. Nidhi Jain', 'Associate Professor', 'Data Science & Big Data Analytics', 'Ph.D. (DTU)'),
            ('Dr. Rajesh Mishra', 'Associate Professor', 'Computer Vision & NLP', 'Ph.D. (AKTU)'),
            ('Prof. Saurabh Gupta', 'Assistant Professor', 'Software Engineering & Agile', 'M.Tech (IIT Delhi)'),
            ('Prof. Pooja Sharma', 'Assistant Professor', 'Database Systems & SQL Optimization', 'M.Tech (NIT Kurukshetra)'),
            ('Prof. Vikas Tiwari', 'Assistant Professor', 'Full-Stack Web & Mobile Architecture', 'M.Tech (AKTU)')
        ],
        'labs': [
            ('Palo Alto Cybersecurity Lab', 'Equipped with enterprise firewall appliances and cyber range simulations for practical intrusion detection training.'),
            ('AI & Deep Learning Computing Centre', 'NVIDIA GPU-accelerated workstations powering LLM, Computer Vision, and Neural Network research.'),
            ('Cloud Computing & DevOps Lab', 'AWS Academy & Microsoft Azure environment for Docker, Kubernetes, and serverless architectures.'),
            ('Advanced Algorithms & Competitive Coding Hub', 'Dedicated arena for CodeChef, LeetCode, and ICPC contest training with high-speed fibre intranet.'),
            ('IoT & Embedded Systems Lab', 'Raspberry Pi 4, Arduino, ESP32, and sensor arrays for edge computing and smart systems projects.'),
            ('Open Source & OWASP Security Cell', 'Hub for OWASP Student Chapter projects, vulnerability assessment, and open-source contributions.')
        ],
        'curriculum': [
            ('Sem 1', 'Engineering Mathematics I, Engineering Physics, Programming for Problem Solving (C), Basic Electrical Engg'),
            ('Sem 2', 'Engineering Mathematics II, Engineering Chemistry, Data Structures in C/C++, Digital Electronics'),
            ('Sem 3', 'Discrete Mathematics, Data Structures & Algorithms, Computer Organization & Architecture, OOP with Java'),
            ('Sem 4', 'Operating Systems, Database Management Systems, Theory of Computation (Automata), Python Programming'),
            ('Sem 5', 'Design & Analysis of Algorithms, Software Engineering, Computer Networks, Web Technologies (MERN)'),
            ('Sem 6', 'Compiler Design, Cloud Computing, Artificial Intelligence & Machine Learning, Department Elective I'),
            ('Sem 7', 'Information & Cyber Security, Big Data Analytics, Open Elective I, Capstone Project Stage I'),
            ('Sem 8', 'Deep Learning & NLP, Industrial Internship, Open Elective II, Capstone Project Stage II & Defense')
        ]
    },
    {
        'filename': 'abes-ghaziabad-cse-department.html',
        'college_name': 'ABES Engineering College, Ghaziabad',
        'short_name': 'ABES EC Ghaziabad',
        'dept_name': 'Computer Science & Engineering (CSE)',
        'hod_name': 'Dr. Vikas Saxena',
        'intake': '300 Seats + 120 AI/ML',
        'highest_pkg': '50 LPA',
        'avg_pkg': '8.2 LPA',
        'placed_pct': '90%',
        'recruiters': 'Microsoft, Google, Amazon, TCS Digital, Infosys, Wipro, Capgemini, Accenture, Cognizant, HCL',
        'hod_quote': 'At ABES CSE, we empower students through intense coding culture, hackathons, and Google Developer Student Clubs to solve real-world industry engineering challenges.',
        'faculty': [
            ('Dr. Vikas Saxena', 'Professor & HOD', 'Algorithms & High Performance Computing', 'Ph.D. (IIT Roorkee)'),
            ('Dr. Anjali Singh', 'Professor', 'Machine Learning & Cognitive Computing', 'Ph.D. (AKTU)'),
            ('Dr. Rahul Agarwal', 'Associate Professor', 'Cyber Security & Network Forensics', 'Ph.D. (JNU)'),
            ('Dr. Sushil Kumar', 'Associate Professor', 'Distributed Systems & Cloud Computing', 'Ph.D. (MNIT)'),
            ('Prof. Amit Kumar', 'Assistant Professor', 'Full Stack Development & DevOps', 'M.Tech (IIT Kanpur)'),
            ('Prof. Ritu Jain', 'Assistant Professor', 'Data Warehousing & Business Intelligence', 'M.Tech (AKTU)'),
            ('Prof. Sandeep Verma', 'Assistant Professor', 'Microservices & System Design', 'M.Tech (NIT Allahabad)'),
            ('Prof. Neha Gupta', 'Assistant Professor', 'Mobile Application Development', 'M.Tech (AKTU)')
        ],
        'labs': [
            ('Microsoft Learn & Azure Cloud Lab', 'High-end workstations with licensed cloud tools and certifications.'),
            ('Google Developer Student Lab', 'Dedicated space for GDSC Android, Flutter, and Firebase projects.'),
            ('AI & Big Data Analytics Lab', 'Equipped with Hadoop, Spark, and TensorFlow frameworks.'),
            ('Software Testing & QA Automation Lab', 'Selenium, JUnit, and Jenkins CI/CD pipeline infrastructure.'),
            ('Competitive Coding Studio', 'High-performance environment for hackathons and coding championships.'),
            ('Computer Networks & Security Lab', 'Cisco Packet Tracer, Wireshark, and hardware routers for network defense.')
        ],
        'curriculum': [
            ('Sem 1', 'Engineering Mathematics I, Engineering Physics, C Programming, Engineering Drawing'),
            ('Sem 2', 'Engineering Mathematics II, Engineering Chemistry, Data Structures, Basic Electronics'),
            ('Sem 3', 'Discrete Structure, OOP with C++/Java, Computer Architecture, Data Structures Lab'),
            ('Sem 4', 'Operating Systems, DBMS, Theory of Automata, Microprocessors & Microcontrollers'),
            ('Sem 5', 'Design & Analysis of Algorithms, Computer Networks, Software Engineering, Web Dev Lab'),
            ('Sem 6', 'Compiler Design, Machine Learning, Cloud Computing Basics, Departmental Elective'),
            ('Sem 7', 'Information Security, AI Applications, Open Elective, Minor Project'),
            ('Sem 8', 'Advanced Computing, Industrial Training, Major Project & Viva Voce')
        ]
    },
    {
        'filename': 'gl-bajaj-ece-department.html',
        'college_name': 'GL Bajaj Institute of Technology & Management, Greater Noida',
        'short_name': 'GL Bajaj Gr. Noida',
        'dept_name': 'Electronics & Communication Engineering (ECE)',
        'hod_name': 'Dr. O.P. Singh',
        'intake': '180 Seats',
        'highest_pkg': '32 LPA',
        'avg_pkg': '7.2 LPA',
        'placed_pct': '88%',
        'recruiters': 'Qualcomm, Intel, Samsung R&D, Texas Instruments, TCS, Infosys, Capgemini, Tech Mahindra',
        'hod_quote': 'Our ECE department bridges hardware and software engineering with state-of-the-art VLSI, Embedded Systems, and 5G communication facilities.',
        'faculty': [
            ('Dr. O.P. Singh', 'Professor & HOD', 'VLSI Design & Semiconductor Devices', 'Ph.D. (IIT BHU)'),
            ('Dr. S.K. Verma', 'Professor', 'Wireless Communication & 5G Systems', 'Ph.D. (IIT Delhi)'),
            ('Dr. R.K. Pandey', 'Associate Professor', 'Embedded Systems & Robotics', 'Ph.D. (AKTU)'),
            ('Dr. Kavita Sharma', 'Associate Professor', 'Digital Signal Processing & Image Processing', 'Ph.D. (MNNIT)'),
            ('Prof. Manoj Tiwari', 'Assistant Professor', 'RF & Microwave Engineering', 'M.Tech (IIT Roorkee)'),
            ('Prof. Swati Goel', 'Assistant Professor', 'Microcontrollers & IoT', 'M.Tech (AKTU)'),
            ('Prof. Alok Yadav', 'Assistant Professor', 'Analog & Digital IC Design', 'M.Tech (NIT Kurukshetra)')
        ],
        'labs': [
            ('Cadence & Synopsys VLSI Design Lab', 'Industry-standard EDA tools for ASIC, FPGA, and SoC design flows.'),
            ('Embedded Systems & ARM Processor Lab', 'ARM Cortex, Keil IDE, and hardware emulation boards.'),
            ('5G & Wireless Communication Lab', 'SDR (Software Defined Radio), spectrum analyzers, and microwave test benches.'),
            ('DSP & Image Processing Lab', 'MATLAB, Simulink, and Texas Instruments DSP starter kits.'),
            ('PCB Fabrication & Prototyping Centre', 'CNC milling and chemical etching units for custom circuit board manufacturing.'),
            ('Robotics & Automation Hub', 'Robotic arms, sensor integration, and industrial PLC trainers.')
        ],
        'curriculum': [
            ('Sem 1', 'Engineering Mathematics I, Semiconductor Physics, Basic Electrical Engg, C Programming'),
            ('Sem 2', 'Engineering Mathematics II, Electronic Materials, Electronic Devices & Circuits'),
            ('Sem 3', 'Digital System Design, Network Analysis & Synthesis, Signals & Systems, Electronic Devices Lab'),
            ('Sem 4', 'Analog Circuits, Microprocessors & Microcontrollers, Electromagnetic Field Theory, Signals Lab'),
            ('Sem 5', 'Integrated Circuits, Digital Signal Processing, Antenna & Wave Propagation, Control Systems'),
            ('Sem 6', 'VLSI Design, Digital Communication, Microcontrollers & Embedded Systems, Department Elective'),
            ('Sem 7', 'Wireless & Mobile Communication, Optical Communication, Open Elective, Major Project Stage I'),
            ('Sem 8', 'Satellite Communication, Radar Engg, Industrial Internship, Major Project Stage II')
        ]
    },
    {
        'filename': 'psit-kanpur-cse-department.html',
        'college_name': 'Pranveer Singh Institute of Technology, Kanpur',
        'short_name': 'PSIT Kanpur',
        'dept_name': 'Computer Science & Engineering (CSE)',
        'hod_name': 'Dr. Akash Srivastava',
        'intake': '300 Seats + 120 AI/ML',
        'highest_pkg': '40 LPA',
        'avg_pkg': '7.8 LPA',
        'placed_pct': '88%',
        'recruiters': 'TCS Digital, Infosys SP, Wipro Elite, HCL, Tech Mahindra, Capgemini, Cognizant, Mindtree, Mphasis',
        'hod_quote': 'PSIT CSE department combines high-standard academic rigor with IBM SkillsBuild and Oracle University industry training to make students globally employable.',
        'faculty': [
            ('Dr. Akash Srivastava', 'Professor & HOD', 'Database Systems & Machine Learning', 'Ph.D. (IIT Kanpur)'),
            ('Dr. Priya Mishra', 'Professor', 'Artificial Intelligence & Neural Networks', 'Ph.D. (AKTU)'),
            ('Dr. R.K. Sharma', 'Associate Professor', 'Cyber Security & Cryptography', 'Ph.D. (HBTU)'),
            ('Dr. Neha Gupta', 'Associate Professor', 'Cloud Computing & Distributed Databases', 'Ph.D. (MNIT)'),
            ('Prof. Saurabh Singh', 'Assistant Professor', 'Object Oriented Design & Java Architectures', 'M.Tech (AKTU)'),
            ('Prof. Deepa Verma', 'Assistant Professor', 'Data Structures & Competitive Algorithms', 'M.Tech (NIT Jalandhar)'),
            ('Prof. Ankur Tiwari', 'Assistant Professor', 'Full Stack Web Engineering', 'M.Tech (AKTU)')
        ],
        'labs': [
            ('Oracle University Workforce Development Lab', 'Authorized Oracle DB 19c and Java Enterprise certifications hub.'),
            ('IBM SkillsBuild Innovation Centre', 'Enterprise cloud computing, AI, and cybersecurity training infrastructure.'),
            ('High-Performance Computing Cluster', 'Multi-node compute cluster for simulations and deep learning models.'),
            ('Advanced Software Development Studio', 'Git, Jenkins, Docker, and modern IDE development suites.'),
            ('Networking & Cyber Range Lab', 'Dedicated hardware testbed for network penetration testing and packet inspection.'),
            ('IoT & Smart Device Lab', 'Sensors, microcontrollers, and wireless transceivers for smart city solutions.')
        ],
        'curriculum': [
            ('Sem 1', 'Engineering Mathematics I, Engineering Chemistry, C Programming, Workshop Practice'),
            ('Sem 2', 'Engineering Mathematics II, Engineering Physics, Data Structures in C, Basic Electrical'),
            ('Sem 3', 'Discrete Mathematics, Data Structures & Algorithms, Computer Organization, OOPs Java'),
            ('Sem 4', 'Operating Systems, DBMS, Theory of Computation, Python for Data Science'),
            ('Sem 5', 'Design Analysis of Algorithms, Computer Networks, Software Engineering, Web Tech'),
            ('Sem 6', 'Compiler Design, Machine Learning, Cloud Computing, Departmental Elective'),
            ('Sem 7', 'Cyber Security, Deep Learning, Open Elective, Project Phase I'),
            ('Sem 8', 'Big Data Engineering, Industry Internship, Project Phase II & Final Defense')
        ]
    },
    {
        'filename': 'niet-greater-noida-cse-department.html',
        'college_name': 'Noida Institute of Engineering & Technology, Greater Noida',
        'short_name': 'NIET Gr. Noida',
        'dept_name': 'Computer Science & Engineering (CSE)',
        'hod_name': 'Dr. Sandeep Arora',
        'intake': '360 Seats + 120 Cyber Security',
        'highest_pkg': '44 LPA',
        'avg_pkg': '8.0 LPA',
        'placed_pct': '91%',
        'recruiters': 'Samsung R&D, TCS Digital, Infosys, Capgemini, Wipro, HCL, Cognizant, Amazon, Tech Mahindra, Paytm',
        'hod_quote': 'With our dedicated Samsung Innovation Lab and AWS Academy, NIET CSE prepares engineering graduates who excel in both product innovation and enterprise development.',
        'faculty': [
            ('Dr. Sandeep Arora', 'Professor & HOD', 'Artificial Intelligence & Image Processing', 'Ph.D. (IIT Delhi)'),
            ('Dr. Ritu Gupta', 'Professor', 'Cyber Security & Network Defense', 'Ph.D. (AKTU)'),
            ('Dr. Divya Singh', 'Associate Professor', 'Cloud Systems & Big Data', 'Ph.D. (DTU)'),
            ('Dr. Atul Kumar', 'Associate Professor', 'Natural Language Processing', 'Ph.D. (MNNIT)'),
            ('Prof. Vivek Shukla', 'Assistant Professor', 'Software Architecture & Agile Methods', 'M.Tech (AKTU)'),
            ('Prof. Megha Bansal', 'Assistant Professor', 'Data Mining & Predictive Modeling', 'M.Tech (NIT Kurukshetra)'),
            ('Prof. Rohit Sharma', 'Assistant Professor', 'Full-Stack JavaScript & DevOps', 'M.Tech (AKTU)')
        ],
        'labs': [
            ('Samsung Innovation & R&D Lab', 'Dedicated IoT, AI, and mobile app testing facility sponsored by Samsung.'),
            ('AWS Academy Cloud Centre', 'Official Amazon Web Services cloud architecture and SysOps curriculum lab.'),
            ('Cyber Security & Threat Intelligence Lab', 'SOC simulation environment with SIEM tools and ethical hacking rigs.'),
            ('Machine Learning & GPU Lab', 'NVIDIA RTX-powered nodes for vision transformers and generative AI.'),
            ('Software Testing & Automation Lab', 'Jira, Selenium, JMeter, and SonarQube quality testing suites.'),
            ('Data Science & R Analytics Studio', 'Hadoop clusters, Tableau, and PowerBI visualization workspaces.')
        ],
        'curriculum': [
            ('Sem 1', 'Engineering Mathematics I, Engineering Physics, Problem Solving using C, Basic Electrical'),
            ('Sem 2', 'Engineering Mathematics II, Engineering Chemistry, Data Structures, Basic Electronics'),
            ('Sem 3', 'Discrete Mathematics, OOP with Java, Computer Organization, Data Structures Lab'),
            ('Sem 4', 'Operating Systems, Database Management Systems, Automata Theory, Python Lab'),
            ('Sem 5', 'Design & Analysis of Algorithms, Computer Networks, Software Engineering, Web Dev Lab'),
            ('Sem 6', 'Compiler Design, Artificial Intelligence, Cloud Computing, Department Elective I'),
            ('Sem 7', 'Cyber Security & Forensics, Distributed Systems, Open Elective I, Capstone Project I'),
            ('Sem 8', 'Advanced AI / ML, Industry Internship, Open Elective II, Capstone Project II')
        ]
    },
    {
        'filename': 'miet-meerut-cse-department.html',
        'college_name': 'Meerut Institute of Engineering & Technology, Meerut',
        'short_name': 'MIET Meerut',
        'dept_name': 'Computer Science & Engineering (CSE)',
        'hod_name': 'Dr. Pradeep Sharma',
        'intake': '240 Seats + 120 IT',
        'highest_pkg': '35 LPA',
        'avg_pkg': '7.5 LPA',
        'placed_pct': '86%',
        'recruiters': 'TCS Digital, Infosys, Wipro, Amazon, HCL, Capgemini, Cognizant, Tech Mahindra, Mindtree',
        'hod_quote': 'MIET CSE department blends practical programming rigor with vibrant technical clubs like Coding Warriors to secure top-tier placements across product and IT MNCs.',
        'faculty': [
            ('Dr. Pradeep Sharma', 'Professor & HOD', 'Artificial Intelligence & Neural Computing', 'Ph.D. (IIT Roorkee)'),
            ('Dr. Seema Tyagi', 'Professor', 'Data Mining & Machine Learning', 'Ph.D. (AKTU)'),
            ('Dr. Ajay Kumar', 'Associate Professor', 'Network Security & Cryptography', 'Ph.D. (CCS University)'),
            ('Dr. Vineet Mittal', 'Associate Professor', 'Distributed Computing & Cloud', 'Ph.D. (MNIT)'),
            ('Prof. Gaurav Tomar', 'Assistant Professor', 'Full-Stack Web Technologies', 'M.Tech (AKTU)'),
            ('Prof. Shalu Singh', 'Assistant Professor', 'Database Optimization & SQL', 'M.Tech (NIT Jalandhar)'),
            ('Prof. Mohit Rastogi', 'Assistant Professor', 'Software Engineering & Testing', 'M.Tech (AKTU)')
        ],
        'labs': [
            ('MIET High-Speed Computing Lab', '120+ Intel i7 systems with SSD storage and high-bandwidth gigabit intranet.'),
            ('AI & Machine Learning Innovation Lab', 'NVIDIA GPU workstations running PyTorch, TensorFlow, and OpenCV.'),
            ('Cloud Computing & Virtualization Centre', 'VMware and OpenStack private cloud environment for distributed systems experiments.'),
            ('IoT & Robotics Research Hub', 'Arduino, Raspberry Pi, LoRaWAN modules, and robotic vision testbenches.'),
            ('Software Testing & Quality Lab', 'Automated testing tools, CI/CD pipelines, and bug tracking suites.'),
            ('Competitive Coding Arena', 'Dedicated environment for CodeForces, HackerRank, and hackathon preparations.')
        ],
        'curriculum': [
            ('Sem 1', 'Engineering Mathematics I, Engineering Chemistry, Programming in C, Basic Electrical'),
            ('Sem 2', 'Engineering Mathematics II, Engineering Physics, Data Structures in C, Basic Electronics'),
            ('Sem 3', 'Discrete Mathematics, OOP with Java/C++, Computer Organization & Architecture, Data Lab'),
            ('Sem 4', 'Operating Systems, DBMS, Theory of Computation, Python Programming Lab'),
            ('Sem 5', 'Design & Analysis of Algorithms, Computer Networks, Software Engineering, Web Lab'),
            ('Sem 6', 'Compiler Design, Machine Learning, Cloud Architecture, Departmental Elective'),
            ('Sem 7', 'Cyber Security, Big Data Analytics, Open Elective, Capstone Project Stage I'),
            ('Sem 8', 'Deep Learning Applications, Industrial Training, Open Elective, Project Defense')
        ]
    }
]

ad_tags = """  <!-- Monetag -->
  
  
  
  
  
  """

out_dir = 'colleges/departments'
os.makedirs(out_dir, exist_ok=True)

for p in dept_pages:
    fac_rows = ''.join([f"<tr><td><strong>{f[0]}</strong></td><td>{f[1]}</td><td>{f[2]}</td><td><span style='background:#e0e7ff;color:#3730a3;padding:2px 8px;border-radius:10px;font-size:12px;font-weight:700;'>{f[3]}</span></td></tr>" for f in p['faculty']])
    lab_cards = ''.join([f"<div class='lab-card'><h4>🔬 {l[0]}</h4><p>{l[1]}</p></div>" for l in p['labs']])
    curr_rows = ''.join([f"<tr><td style='font-weight:700;color:var(--primary);width:100px;'>{c[0]}</td><td>{c[1]}</td></tr>" for c in p['curriculum']])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{p['short_name']} {p['dept_name']} | Faculty, Subjects, Labs & Placement Guide</title>
  <meta name="description" content="Explore {p['college_name']} {p['dept_name']} — comprehensive faculty profiles, semester-wise AKTU syllabus, lab facilities, placement records ({p['highest_pkg']} highest, {p['avg_pkg']} avg), top recruiters and GATE coaching guidance.">
  <meta name="keywords" content="{p['short_name'].lower()} cse department, {p['short_name'].lower()} faculty, {p['short_name'].lower()} placement cse, {p['short_name'].lower()} syllabus, aktu {p['short_name'].lower()} labs">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://akturesults.in/colleges/departments/{p['filename']}">
  <link rel="icon" href="/favicon.png" type="image/png">
{ad_tags}
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "EducationalOrganization",
    "name": "{p['college_name']} – {p['dept_name']}",
    "url": "https://akturesults.in/colleges/departments/{p['filename']}",
    "parentOrganization": {{ "@type": "CollegeOrUniversity", "name": "{p['college_name']}" }},
    "description": "{p['dept_name']} department offering B.Tech with verified placements, advanced research labs, and GATE coaching."
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://akturesults.in/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Colleges", "item": "https://akturesults.in/colleges/" }},
      {{ "@type": "ListItem", "position": 3, "name": "{p['short_name']}", "item": "https://akturesults.in/colleges/" }},
      {{ "@type": "ListItem", "position": 4, "name": "{p['dept_name']}", "item": "https://akturesults.in/colleges/departments/{p['filename']}" }}
    ]
  }}
  </script>
  <style>
    *{{margin:0;padding:0;box-sizing:border-box}}
    :root{{--primary:#4c51bf;--secondary:#667eea;--accent:#38b2ac;--dark:#1a202c;--light:#f7fafc}}
    body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.7;color:var(--dark);background:var(--light)}}
    .container{{max-width:1100px;margin:0 auto;padding:0 20px}}
    nav{{background:#fff;box-shadow:0 2px 10px rgba(0,0,0,.07);padding:14px 0;position:sticky;top:0;z-index:999}}
    .nav-inner{{display:flex;justify-content:space-between;align-items:center}}
    .logo{{font-size:22px;font-weight:800;background:linear-gradient(135deg,var(--primary),var(--secondary));-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-decoration:none}}
    .back-btn{{padding:9px 22px;background:var(--primary);color:#fff;text-decoration:none;border-radius:25px;font-weight:600;font-size:14px}}
    .hero{{background:linear-gradient(135deg,#2d3748,var(--primary));color:#fff;padding:60px 0 45px;text-align:center}}
    .hero h1{{font-size:32px;font-weight:900;margin-bottom:10px;line-height:1.3}}
    .hero p{{font-size:16px;opacity:.9;margin-bottom:16px}}
    .badge{{background:rgba(255,255,255,.15);color:#fff;padding:5px 14px;border-radius:20px;font-size:13px;font-weight:700;display:inline-block;margin:4px}}
    .breadcrumb{{background:#fff;padding:12px 0;border-bottom:1px solid #e2e8f0;font-size:13px}}
    .breadcrumb a{{color:var(--primary);text-decoration:none}}
    .breadcrumb span{{color:#718096;margin:0 6px}}
    section{{background:#fff;margin:24px auto;border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,.06);padding:35px}}
    h2{{font-size:24px;font-weight:800;color:var(--dark);border-left:4px solid var(--primary);padding-left:14px;margin-bottom:20px}}
    h3{{font-size:19px;font-weight:700;color:var(--primary);margin:18px 0 10px}}
    p{{margin-bottom:14px;font-size:15px}}
    .stat-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px;margin:20px 0}}
    .stat-card{{background:linear-gradient(135deg,var(--primary),var(--secondary));color:#fff;padding:20px;border-radius:10px;text-align:center}}
    .stat-card .num{{font-size:28px;font-weight:900}}
    .stat-card .lbl{{font-size:12px;opacity:.9;margin-top:4px}}
    table{{width:100%;border-collapse:collapse;margin:16px 0;font-size:14px}}
    th{{background:#4c51bf;color:#fff;padding:12px 14px;text-align:left}}
    td{{padding:10px 14px;border-bottom:1px solid #e2e8f0}}
    tr:nth-child(even) td{{background:#f8fafc}}
    tr:hover td{{background:#ebf4ff}}
    .lab-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin:16px 0}}
    .lab-card{{background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:18px}}
    .lab-card h4{{color:var(--primary);font-size:15px;margin-bottom:6px}}
    .lab-card p{{font-size:13px;color:#4a5568;margin:0}}
    .hod-box{{background:linear-gradient(135deg,#ebf4ff,#f0fff4);border-radius:12px;padding:24px;margin:20px 0;border-left:5px solid var(--accent)}}
    .hod-box blockquote{{font-style:italic;font-size:16px;color:#2d3748;line-height:1.7}}
    .footer{{background:var(--dark);color:#fff;text-align:center;padding:30px 0;margin-top:50px;font-size:14px}}
    .footer a{{color:#68d391;text-decoration:none}}
    @media(max-width:768px){{.hero h1{{font-size:24px;}}section{{padding:20px;}}}}
  </style>
</head>
<body>
  <nav>
    <div class="container nav-inner">
      <a href="/" class="logo">AKTU Results</a>
      <a href="/colleges/" class="back-btn">← All Colleges</a>
    </div>
  </nav>

  <div class="breadcrumb">
    <div class="container">
      <a href="/">Home</a> <span>›</span>
      <a href="/colleges/">Colleges</a> <span>›</span>
      <a href="/colleges/">{p['short_name']}</a> <span>›</span>
      <span>{p['dept_name']}</span>
    </div>
  </div>

  <div class="hero">
    <div class="container">
      <span class="badge">Department of Excellence</span>
      <span class="badge">Intake: {p['intake']}</span>
      <h1>{p['short_name']} – {p['dept_name']}</h1>
      <p>Faculty Profiles • Semester-wise Curriculum • Labs • Placement & Research Records</p>
      <div>
        <span class="badge">Highest: {p['highest_pkg']}</span>
        <span class="badge">Avg: {p['avg_pkg']}</span>
        <span class="badge">Placement Rate: {p['placed_pct']}</span>
      </div>
    </div>
  </div>

  <div class="container">
    <section>
      <h2>Department Overview</h2>
      <p>The Department of {p['dept_name']} at {p['college_name']} is recognized as one of the premier academic departments under Dr. A.P.J. Abdul Kalam Technical University (AKTU). Combining strong theoretical foundations with intensive laboratory training and industry certifications, the department consistently produces software architects, researchers, and successful entrepreneurs.</p>
      
      <div class="stat-grid">
        <div class="stat-card"><div class="num">{p['highest_pkg']}</div><div class="lbl">Highest Package</div></div>
        <div class="stat-card"><div class="num">{p['avg_pkg']}</div><div class="lbl">Average Package</div></div>
        <div class="stat-card"><div class="num">{p['placed_pct']}</div><div class="lbl">Placement Rate</div></div>
        <div class="stat-card"><div class="num">{p['intake'].split(' ')[0]}</div><div class="lbl">Annual Intake</div></div>
      </div>

      <div class="hod-box">
        <blockquote>"{p['hod_quote']}"</blockquote>
        <div style="margin-top:10px;font-weight:700;color:var(--primary);text-align:right;">— {p['hod_name']}, Head of Department</div>
      </div>
    </section>

    <section>
      <h2>Distinguished Faculty Members</h2>
      <p>The department boasts highly qualified faculty members holding doctorates from premier institutions such as IITs, NITs, and central universities.</p>
      <div style="overflow-x:auto;">
        <table>
          <thead>
            <tr><th>Faculty Name</th><th>Designation</th><th>Specialization</th><th>Qualification</th></tr>
          </thead>
          <tbody>
            {fac_rows}
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Specialized Laboratories & Research Infrastructure</h2>
      <p>State-of-the-art laboratory facilities ensure students gain rigorous hands-on experience in modern tools, frameworks, and cloud platforms.</p>
      <div class="lab-grid">
        {lab_cards}
      </div>
    </section>

    <section>
      <h2>Semester-wise AKTU Curriculum & Core Subjects</h2>
      <p>The CBCS & NEP aligned curriculum covers fundamental theory, systems programming, and modern departmental electives across 8 semesters.</p>
      <div style="overflow-x:auto;">
        <table>
          <thead>
            <tr><th>Semester</th><th>Key Subjects & Practical Labs</th></tr>
          </thead>
          <tbody>
            {curr_rows}
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Placement Track Record & Major Recruiters</h2>
      <p>Graduates from {p['short_name']} {p['dept_name']} are recruited by top global product companies, consulting firms, and leading IT services MNCs.</p>
      <p><strong>Top Visiting Recruiters:</strong> {p['recruiters']}</p>
      <div style="margin-top:20px;padding:16px;background:#f0fff4;border-left:4px solid #38a169;border-radius:8px;">
        <strong>💡 Higher Studies & GATE Guidance:</strong> The department conducts dedicated GATE preparation modules and coding bootcamps. Every year, several students qualify for M.Tech admissions at IITs, NITs, and top universities in the US and Europe.
      </div>
    </section>

    <section style="background:#f8fafc;border:1px solid #e2e8f0;">
      <h2>Related Resources & Tools</h2>
      <p>Explore tools and comparison guides for AKTU colleges:</p>
      <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:12px;">
        <a href="/admissions/uptac-choice-filling-predictor-2026.html" style="background:#fff;border:1px solid #cbd5e0;padding:10px 16px;border-radius:8px;text-decoration:none;font-weight:700;color:var(--primary);font-size:14px;">🎯 Choice Predictor</a>
        <a href="/tools/uptac-scholarship-fee-roi-calculator.html" style="background:#fff;border:1px solid #cbd5e0;padding:10px 16px;border-radius:8px;text-decoration:none;font-weight:700;color:var(--primary);font-size:14px;">💰 Scholarship ROI Calculator</a>
        <a href="/placements/aktu-college-placement-leaderboard-2026.html" style="background:#fff;border:1px solid #cbd5e0;padding:10px 16px;border-radius:8px;text-decoration:none;font-weight:700;color:var(--primary);font-size:14px;">🏆 Placement Leaderboard</a>
        <a href="/colleges/aktu-colleges-filter-directory.html" style="background:#fff;border:1px solid #cbd5e0;padding:10px 16px;border-radius:8px;text-decoration:none;font-weight:700;color:var(--primary);font-size:14px;">🏛️ College Filter Directory</a>
      </div>
    </section>
  </div>

  <div class="footer">
    <div class="container">
      <p>© 2026 <a href="/">AKTU Results Portal</a> — Independent Student Educational Platform</p>
      <p style="margin-top:6px;opacity:.7;font-size:13px;">Disclaimer: Data compiled from official institute publications and student placement records. Verify with respective college authorities.</p>
    </div>
  </div>
  <script defer src="/js/community-banner-widget.js"></script>
</body>
</html>"""

    out_path = os.path.join(out_dir, p['filename'])
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Generated: {out_path}')

print('All 6 department pages generated successfully!')
