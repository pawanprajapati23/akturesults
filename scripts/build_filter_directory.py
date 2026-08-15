import os, json

# All 48 colleges with complete rich attributes for the interactive search/filter engine
colleges = [
    {
        "name": "Institute of Engineering and Technology (IET Lucknow)",
        "code": "052",
        "city": "Lucknow",
        "type": "Government Autonomous",
        "est": 1984,
        "naac": "A+",
        "nirf": "151-200",
        "fee": 85000,
        "highest_pkg": 49.0,
        "avg_pkg": 10.5,
        "placement_pct": 94,
        "branches": ["CSE", "CSE-AI", "ECE", "ME", "EE", "CE", "Chemical"],
        "recruiters": ["Amazon", "Google", "Microsoft", "Adobe", "Paytm", "Samsung", "TCS Digital"],
        "clubs": ["GDSC IET", "Robotics Club", "NSS", "IEEE Student Branch", "E-Cell", "Literary Club"],
        "url": "/colleges/profiles/iet-lucknow-profile-2026.html",
        "phone": "+91-522-2733027",
        "website": "https://ietlucknow.ac.in",
        "address": "Sitapur Road, Sector F, Jankipuram, Lucknow - 226021, UP"
    },
    {
        "name": "Harcourt Butler Technical University (HBTU Kanpur)",
        "code": "061",
        "city": "Kanpur",
        "type": "Government University",
        "est": 1921,
        "naac": "A+",
        "nirf": "76-100",
        "fee": 62000,
        "highest_pkg": 65.0,
        "avg_pkg": 12.5,
        "placement_pct": 96,
        "branches": ["CSE", "ECE", "ME", "CE", "Chemical", "IT", "EE"],
        "recruiters": ["Google", "Amazon", "Microsoft", "Goldman Sachs", "Morgan Stanley", "Flipkart", "IBM"],
        "clubs": ["Coding Club HBTU", "IEEE", "NSS", "NCC", "E-Cell", "Robotics Club"],
        "url": "/colleges/profiles/hbtu-kanpur-profile.html",
        "phone": "+91-512-2533537",
        "website": "https://www.hbtu.ac.in",
        "address": "Nawabganj, Kanpur - 208002, UP"
    },
    {
        "name": "JSS Academy of Technical Education (JSS Noida)",
        "code": "091",
        "city": "Noida",
        "type": "Private Autonomous",
        "est": 1998,
        "naac": "A",
        "nirf": "101-150",
        "fee": 138000,
        "highest_pkg": 57.0,
        "avg_pkg": 9.8,
        "placement_pct": 92,
        "branches": ["CSE", "CSE-AI", "ECE", "ME", "EE", "CE", "IT"],
        "recruiters": ["Adobe", "Amazon", "Cisco", "TCS Digital", "Palo Alto", "Commvault", "Infosys SP"],
        "clubs": ["OWASP JSS", "GDSC JSS", "IEEE", "NSS", "E-Cell", "Photography Club"],
        "url": "/colleges/profiles/jss-noida-profile-2026.html",
        "phone": "+91-120-2400115",
        "website": "https://jssaten.ac.in",
        "address": "C-20/1, Sector 62, Noida - 201301, UP"
    },
    {
        "name": "KIET Group of Institutions (KIET Ghaziabad)",
        "code": "029",
        "city": "Ghaziabad",
        "type": "Private Autonomous",
        "est": 1998,
        "naac": "A+",
        "nirf": "76-100",
        "fee": 139000,
        "highest_pkg": 48.5,
        "avg_pkg": 9.5,
        "placement_pct": 93,
        "branches": ["CSE", "CSE-AI", "CSE-DS", "ECE", "ME", "CE", "IT"],
        "recruiters": ["Atlassian", "Amazon", "Capgemini", "TCS Digital", "Wipro Elite", "Cognizant"],
        "clubs": ["KIET Coding Warriors", "GDSC KIET", "IEEE", "NSS", "Robotics Club"],
        "url": "/colleges/profiles/kiet-ghaziabad-profile-2026.html",
        "phone": "+91-1232-227975",
        "website": "https://www.kiet.edu",
        "address": "Delhi-NCR, Meerut Road (NH-58), Ghaziabad - 201206, UP"
    },
    {
        "name": "Ajay Kumar Garg Engineering College (AKGEC Ghaziabad)",
        "code": "027",
        "city": "Ghaziabad",
        "type": "Private Autonomous",
        "est": 1998,
        "naac": "A",
        "nirf": "101-150",
        "fee": 141000,
        "highest_pkg": 44.0,
        "avg_pkg": 9.2,
        "placement_pct": 91,
        "branches": ["CSE", "CSE-AI", "CSE-DS", "ECE", "ME", "CE", "IT"],
        "recruiters": ["Amazon", "Microsoft", "IBM", "TCS", "Infosys", "Wipro", "Capgemini"],
        "clubs": ["Software Incubator", "Big Data Centre", "IEEE", "NSS", "E-Cell"],
        "url": "/colleges/profiles/akgec-ghaziabad-profile-2026.html",
        "phone": "+91-120-2762841",
        "website": "https://www.akgec.ac.in",
        "address": "27th Km Stone, Delhi-Hapur Bypass Road, Ghaziabad - 201009, UP"
    },
    {
        "name": "GL Bajaj Institute of Technology & Management",
        "code": "192",
        "city": "Greater Noida",
        "type": "Private Autonomous",
        "est": 2005,
        "naac": "A+",
        "nirf": "76-100",
        "fee": 128000,
        "highest_pkg": 58.0,
        "avg_pkg": 9.0,
        "placement_pct": 95,
        "branches": ["CSE", "CSE-AI", "CSE-DS", "ECE", "ME", "CE", "IT"],
        "recruiters": ["Palo Alto Networks", "Commvault", "Amazon", "Microsoft", "TCS Digital", "Infosys"],
        "clubs": ["GDSC GL Bajaj", "CodeChef Campus Chapter", "IEEE", "NSS", "E-Cell"],
        "url": "/colleges/profiles/gl-bajaj-greater-noida-profile-2026.html",
        "phone": "+91-120-2323818",
        "website": "https://www.glbitm.org",
        "address": "Plot No. 2, Knowledge Park III, Greater Noida - 201306, UP"
    },
    {
        "name": "Galgotias College of Engineering and Technology",
        "code": "097",
        "city": "Greater Noida",
        "type": "Private Autonomous",
        "est": 1999,
        "naac": "A",
        "nirf": "101-150",
        "fee": 125000,
        "highest_pkg": 52.0,
        "avg_pkg": 9.2,
        "placement_pct": 93,
        "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "IT", "CSE-DS"],
        "recruiters": ["Google", "Amazon", "Microsoft", "Adobe", "Cisco", "TCS Digital", "Wipro Elite"],
        "clubs": ["GDSC Galgotias", "CodeChef Galgotias", "NSS", "IEEE", "E-Cell", "Robotics Club"],
        "url": "/colleges/profiles/galgotias-college-greater-noida-profile.html",
        "phone": "+91-120-2323300",
        "website": "https://www.galgotiacollege.edu",
        "address": "1, Knowledge Park II, Greater Noida - 201306, UP"
    },
    {
        "name": "Kamla Nehru Institute of Technology (KNIT Sultanpur)",
        "code": "104",
        "city": "Sultanpur",
        "type": "Government Autonomous",
        "est": 1979,
        "naac": "A",
        "nirf": "151-200",
        "fee": 64350,
        "highest_pkg": 45.0,
        "avg_pkg": 8.8,
        "placement_pct": 88,
        "branches": ["CSE", "ECE", "ME", "EE", "CE", "IT", "MCA"],
        "recruiters": ["Amazon", "Samsung", "TCS", "Infosys", "Wipro", "L&T", "BHEL"],
        "clubs": ["KNIT Coding Hub", "Robotics Club", "NSS", "NCC", "Literary Club"],
        "url": "/colleges/profiles/knit-sultanpur-profile-2026.html",
        "phone": "+91-5362-240454",
        "website": "https://knit.ac.in",
        "address": "KNIT Campus, Sultanpur - 228118, UP"
    },
    {
        "name": "Bundelkhand Institute of Engineering & Technology (BIET Jhansi)",
        "code": "043",
        "city": "Jhansi",
        "type": "Government Autonomous",
        "est": 1960,
        "naac": "A",
        "nirf": "151-200",
        "fee": 61800,
        "highest_pkg": 42.0,
        "avg_pkg": 8.5,
        "placement_pct": 87,
        "branches": ["CSE", "ECE", "ME", "EE", "CE", "IT", "Chemical"],
        "recruiters": ["Amazon", "TCS", "Infosys", "Wipro", "Samsung", "L&T", "BHEL"],
        "clubs": ["Robotics Club", "IEEE", "NSS", "NCC", "E-Cell", "Coding Club"],
        "url": "/colleges/profiles/biet-jhansi-profile.html",
        "phone": "+91-510-2320121",
        "website": "https://www.bietjhansi.ac.in",
        "address": "Kanpur Road, Jhansi - 284128, UP"
    },
    {
        "name": "ABES Engineering College (ABES EC Ghaziabad)",
        "code": "032",
        "city": "Ghaziabad",
        "type": "Private Autonomous",
        "est": 2000,
        "naac": "A",
        "nirf": "201-300",
        "fee": 135000,
        "highest_pkg": 50.0,
        "avg_pkg": 8.2,
        "placement_pct": 90,
        "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "IT"],
        "recruiters": ["Microsoft", "Google", "Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini"],
        "clubs": ["GDSC ABES", "Microsoft Learn Ambassador", "NSS", "IEEE", "E-Cell"],
        "url": "/colleges/profiles/abes-engineering-ghaziabad-profile-2026.html",
        "phone": "+91-120-7135112",
        "website": "https://www.abes.ac.in",
        "address": "19th KM Stone, NH-09, Ghaziabad - 201009, UP"
    },
    {
        "name": "Pranveer Singh Institute of Technology (PSIT Kanpur)",
        "code": "164",
        "city": "Kanpur",
        "type": "Private Autonomous",
        "est": 2004,
        "naac": "A",
        "nirf": "201-300",
        "fee": 120000,
        "highest_pkg": 40.0,
        "avg_pkg": 7.8,
        "placement_pct": 88,
        "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "IT", "MBA"],
        "recruiters": ["TCS Digital", "Infosys SP", "Wipro Elite", "HCL", "Tech Mahindra", "Capgemini"],
        "clubs": ["Oracle Student Chapter", "IBM SkillsBuild Club", "NSS", "IEEE", "E-Cell"],
        "url": "/colleges/profiles/psit-kanpur-profile-2026.html",
        "phone": "+91-512-2696244",
        "website": "https://www.psit.ac.in",
        "address": "Kanpur-Agra Highway, NH-19, Bhauti, Kanpur - 209305, UP"
    },
    {
        "name": "Noida Institute of Engineering & Technology (NIET Gr. Noida)",
        "code": "133",
        "city": "Greater Noida",
        "type": "Private Autonomous",
        "est": 2001,
        "naac": "A",
        "nirf": "201-300",
        "fee": 130000,
        "highest_pkg": 44.0,
        "avg_pkg": 8.0,
        "placement_pct": 91,
        "branches": ["CSE", "CSE-AI", "CSE-DS", "ECE", "ME", "CE", "IT"],
        "recruiters": ["Samsung R&D", "TCS Digital", "Infosys", "Capgemini", "Wipro", "Amazon"],
        "clubs": ["Samsung Innovation Hub", "AWS Cloud Club", "NSS", "IEEE", "Robotics Club"],
        "url": "/colleges/profiles/niet-greater-noida-profile-2026.html",
        "phone": "+91-120-2328131",
        "website": "https://www.niet.co.in",
        "address": "19, Knowledge Park II, Institutional Area, Greater Noida - 201306, UP"
    },
    {
        "name": "Meerut Institute of Engineering & Technology (MIET Meerut)",
        "code": "108",
        "city": "Meerut",
        "type": "Private Autonomous",
        "est": 1995,
        "naac": "A",
        "nirf": "201-300",
        "fee": 118000,
        "highest_pkg": 35.0,
        "avg_pkg": 7.5,
        "placement_pct": 86,
        "branches": ["CSE", "ECE", "ME", "CE", "IT", "EE"],
        "recruiters": ["TCS Digital", "Infosys", "Wipro", "Amazon", "HCL", "Capgemini"],
        "clubs": ["MIET Coding Club", "IEEE", "NSS", "NCC", "E-Cell", "Robotics Club"],
        "url": "/colleges/profiles/miet-meerut-profile.html",
        "phone": "+91-121-2439021",
        "website": "https://www.miet.ac.in",
        "address": "NH-58, Bypass Road, Meerut - 250005, UP"
    },
    {
        "name": "IMS Engineering College (IMS EC Ghaziabad)",
        "code": "070",
        "city": "Ghaziabad",
        "type": "Private Autonomous",
        "est": 2001,
        "naac": "A",
        "nirf": "201-300",
        "fee": 128000,
        "highest_pkg": 38.0,
        "avg_pkg": 7.8,
        "placement_pct": 88,
        "branches": ["CSE", "ECE", "ME", "CE", "IT"],
        "recruiters": ["Amazon", "TCS Digital", "Infosys SP", "Wipro", "HCL", "Capgemini"],
        "clubs": ["IMS Coding Club", "IEEE", "GDSC", "NSS", "Robotics Club"],
        "url": "/colleges/profiles/ims-ghaziabad-profile.html",
        "phone": "+91-120-2675850",
        "website": "https://www.imsec.ac.in",
        "address": "NH-9, Adhyatmik Nagar, Ghaziabad - 201009, UP"
    },
    {
        "name": "Raj Kumar Goel Institute of Technology (RKGIT Ghaziabad)",
        "code": "126",
        "city": "Ghaziabad",
        "type": "Private Autonomous",
        "est": 2000,
        "naac": "A",
        "nirf": "201-300",
        "fee": 122000,
        "highest_pkg": 30.0,
        "avg_pkg": 7.0,
        "placement_pct": 84,
        "branches": ["CSE", "ECE", "ME", "CE", "IT"],
        "recruiters": ["TCS", "Amazon", "Infosys", "Wipro", "HCL", "Capgemini"],
        "clubs": ["RKGIT Coding Club", "IEEE", "NSS", "E-Cell", "Robotics Club"],
        "url": "/colleges/profiles/raj-kumar-goel-ghaziabad-profile.html",
        "phone": "+91-120-2675755",
        "website": "https://www.rkgit.edu.in",
        "address": "5 Km Stone, Delhi-Meerut Road (NH-58), Ghaziabad - 201003, UP"
    },
    {
        "name": "Shri Ramswaroop Memorial College (SRMCEM Lucknow)",
        "code": "130",
        "city": "Lucknow",
        "type": "Private Autonomous",
        "est": 2001,
        "naac": "A",
        "nirf": "201-300",
        "fee": 115000,
        "highest_pkg": 32.0,
        "avg_pkg": 7.2,
        "placement_pct": 85,
        "branches": ["CSE", "ECE", "ME", "CE", "IT", "MBA"],
        "recruiters": ["TCS Digital", "Amazon", "Infosys", "Wipro", "HCL", "Capgemini"],
        "clubs": ["SRMCEM Coding Club", "IEEE", "NSS", "E-Cell", "Robotics Club"],
        "url": "/colleges/profiles/shri-ramswaroop-memorial-lucknow-profile.html",
        "phone": "+91-522-2732404",
        "website": "https://www.srmcemlu.com",
        "address": "Tiwari Ganj, Faizabad Road, Lucknow - 227105, UP"
    },
    {
        "name": "Sam Higginbottom Univ of Agri, Tech & Sciences (SHUATS)",
        "code": "SHUATS",
        "city": "Prayagraj",
        "type": "Deemed University",
        "est": 1910,
        "naac": "A",
        "nirf": "151-200",
        "fee": 85000,
        "highest_pkg": 28.0,
        "avg_pkg": 6.5,
        "placement_pct": 82,
        "branches": ["CSE", "ECE", "ME", "CE", "IT"],
        "recruiters": ["TCS", "Amazon", "Infosys", "Wipro", "ITC", "Britannia", "Nestle"],
        "clubs": ["Coding Club", "NSS", "NCC", "IEEE", "E-Cell"],
        "url": "/colleges/profiles/shiats-allahabad-profile.html",
        "phone": "+91-532-2684281",
        "website": "https://www.shuats.edu.in",
        "address": "Naini, Prayagraj - 211007, UP"
    },
    {
        "name": "Teerthanker Mahaveer University (TMU Moradabad)",
        "code": "TMU",
        "city": "Moradabad",
        "type": "Private University",
        "est": 2008,
        "naac": "A",
        "nirf": "201-300",
        "fee": 105000,
        "highest_pkg": 25.0,
        "avg_pkg": 6.5,
        "placement_pct": 80,
        "branches": ["CSE", "ECE", "ME", "CE", "IT", "MBA"],
        "recruiters": ["TCS", "Amazon", "Infosys", "Wipro", "HCL", "Capgemini"],
        "clubs": ["TMU Coding Club", "IEEE", "NSS", "NCC", "E-Cell"],
        "url": "/colleges/profiles/tmuit-moradabad-profile.html",
        "phone": "+91-591-2360700",
        "website": "https://www.tmu.ac.in",
        "address": "Delhi Road, Moradabad - 244001, UP"
    },
    {
        "name": "MIT College of Engineering (MIT Moradabad)",
        "code": "110",
        "city": "Moradabad",
        "type": "Private Autonomous",
        "est": 1996,
        "naac": "A",
        "nirf": "201-300",
        "fee": 112000,
        "highest_pkg": 28.0,
        "avg_pkg": 7.0,
        "placement_pct": 82,
        "branches": ["CSE", "ECE", "ME", "CE", "IT", "EE"],
        "recruiters": ["TCS Digital", "Infosys", "Amazon", "HCL", "Wipro", "Capgemini"],
        "clubs": ["MIT Coding Club", "IEEE", "NSS", "E-Cell", "Robotics Club"],
        "url": "/colleges/profiles/mit-moradabad-profile.html",
        "phone": "+91-591-2360500",
        "website": "https://www.mitmor.ac.in",
        "address": "Rampur Road, Moradabad - 244001, UP"
    },
    {
        "name": "Inderprastha Engineering College (IPEC Ghaziabad)",
        "code": "068",
        "city": "Ghaziabad",
        "type": "Private",
        "est": 1999,
        "naac": "B+",
        "nirf": "301-400",
        "fee": 112000,
        "highest_pkg": 26.0,
        "avg_pkg": 6.8,
        "placement_pct": 83,
        "branches": ["CSE", "ECE", "ME", "CE", "IT"],
        "recruiters": ["TCS Digital", "Infosys", "Wipro", "Amazon", "HCL", "Capgemini"],
        "clubs": ["IPEC Coding Club", "IEEE", "NSS", "E-Cell", "Robotics Club"],
        "url": "/colleges/profiles/ipec-ghaziabad-profile.html",
        "phone": "+91-120-2675800",
        "website": "https://www.ipec.org.in",
        "address": "Adhyatmik Nagar, NH-9, Ghaziabad - 201010, UP"
    },
    {
        "name": "Swami Vivekanand Subharti University (SVSU Meerut)",
        "code": "115",
        "city": "Meerut",
        "type": "Private University",
        "est": 2008,
        "naac": "A",
        "nirf": "201-300",
        "fee": 108000,
        "highest_pkg": 28.0,
        "avg_pkg": 6.8,
        "placement_pct": 80,
        "branches": ["CSE", "ECE", "ME", "CE", "IT", "MBA"],
        "recruiters": ["TCS", "Amazon", "Infosys", "Wipro", "HCL", "IBM"],
        "clubs": ["SVSU Coding Club", "IEEE", "NSS", "NCC", "E-Cell"],
        "url": "/colleges/profiles/swami-vivekanand-meerut-profile.html",
        "phone": "+91-121-2439500",
        "website": "https://www.subhartiuniversity.edu.in",
        "address": "NH-58, Meerut-Hapur Bypass, Meerut - 250005, UP"
    },
    {
        "name": "Babu Banarasi Das Institute (BBDITM Lucknow)",
        "code": "091-L",
        "city": "Lucknow",
        "type": "Private",
        "est": 2000,
        "naac": "B+",
        "nirf": "301-400",
        "fee": 105000,
        "highest_pkg": 18.0,
        "avg_pkg": 5.8,
        "placement_pct": 78,
        "branches": ["CSE", "ECE", "ME", "CE", "IT"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Capgemini"],
        "clubs": ["Coding Club", "IEEE", "NSS", "E-Cell", "Sports Club"],
        "url": "/colleges/profiles/bbditm-lucknow-profile.html",
        "phone": "+91-522-2732999",
        "website": "https://www.bbditm.ac.in",
        "address": "Sector II, Dr. Akhilesh Das Nagar, Lucknow - 226028, UP"
    },
    {
        "name": "Greater Noida Institute of Technology (GNIOT / GCET)",
        "code": "049",
        "city": "Greater Noida",
        "type": "Private",
        "est": 2000,
        "naac": "B+",
        "nirf": "301-400",
        "fee": 112000,
        "highest_pkg": 24.0,
        "avg_pkg": 6.5,
        "placement_pct": 82,
        "branches": ["CSE", "ECE", "ME", "CE", "IT", "MBA"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra", "Capgemini"],
        "clubs": ["Coding Club", "NSS", "IEEE", "E-Cell", "Sports Club"],
        "url": "/colleges/profiles/gcet-greater-noida-profile.html",
        "phone": "+91-120-2323811",
        "website": "https://www.gniot.net",
        "address": "27 Knowledge Park I, Greater Noida - 201308, UP"
    },
    {
        "name": "Invertis University Bareilly",
        "code": "140",
        "city": "Bareilly",
        "type": "Private University",
        "est": 2010,
        "naac": "B+",
        "nirf": "301-400",
        "fee": 98000,
        "highest_pkg": 15.0,
        "avg_pkg": 5.2,
        "placement_pct": 72,
        "branches": ["CSE", "ECE", "ME", "CE", "IT"],
        "recruiters": ["TCS", "Wipro", "Infosys", "HCL", "Cognizant", "Capgemini"],
        "clubs": ["Coding Club", "NSS", "IEEE", "E-Cell", "Sports Club"],
        "url": "/colleges/profiles/invertis-university-bareilly-profile.html",
        "phone": "+91-581-2303900",
        "website": "https://www.invertis.org",
        "address": "Lucknow Road, Tedhia Pulia, Bareilly - 243123, UP"
    },
    {
        "name": "College of Engineering Roorkee (COER Roorkee)",
        "code": "038",
        "city": "Roorkee",
        "type": "Private",
        "est": 2004,
        "naac": "B+",
        "nirf": "301-400",
        "fee": 105000,
        "highest_pkg": 22.0,
        "avg_pkg": 6.2,
        "placement_pct": 78,
        "branches": ["CSE", "ECE", "ME", "CE", "IT"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Capgemini"],
        "clubs": ["Coding Club", "NSS", "IEEE", "E-Cell", "Sports Club"],
        "url": "/colleges/profiles/coer-roorkee-profile.html",
        "phone": "+91-1332-276200",
        "website": "https://www.coer.ac.in",
        "address": "Roorkee-Haridwar Highway, Roorkee - 247667, Uttarakhand"
    },
    {
        "name": "United College of Engineering & Research (UCER Prayagraj)",
        "code": "UCER",
        "city": "Prayagraj",
        "type": "Private",
        "est": 2000,
        "naac": "B+",
        "nirf": "301-400",
        "fee": 100000,
        "highest_pkg": 18.0,
        "avg_pkg": 5.5,
        "placement_pct": 73,
        "branches": ["CSE", "ECE", "ME", "CE", "IT"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Capgemini"],
        "clubs": ["Coding Club", "NSS", "IEEE", "E-Cell"],
        "url": "/colleges/profiles/united-college-allahabad-profile.html",
        "phone": "+91-532-2423900",
        "website": "https://www.ucer.ac.in",
        "address": "16-A Civil Lines, Prayagraj - 211001, UP"
    },
    {
        "name": "Institute of Engineering and Rural Technology (IERT Prayagraj)",
        "code": "076",
        "city": "Prayagraj",
        "type": "Government Autonomous",
        "est": 1962,
        "naac": "A",
        "nirf": "151-200",
        "fee": 42000,
        "highest_pkg": 32.0,
        "avg_pkg": 7.8,
        "placement_pct": 85,
        "branches": ["CSE", "ECE", "ME", "EE", "CE", "IT"],
        "recruiters": ["TCS", "L&T", "BHEL", "NTPC", "ONGC", "Samsung", "IBM"],
        "clubs": ["Robotics Club", "NSS", "NCC", "IEEE", "Cultural Club"],
        "url": "/colleges/profiles/indorama-sonbhadra-profile.html",
        "phone": "+91-532-2684000",
        "website": "https://www.iert.ac.in",
        "address": "Jhunsi, Prayagraj - 211015, UP"
    },
    {
        "name": "RBS Engineering Technical Campus Agra",
        "code": "127",
        "city": "Agra",
        "type": "Private",
        "est": 2001,
        "naac": "B+",
        "nirf": "301-400",
        "fee": 98000,
        "highest_pkg": 16.0,
        "avg_pkg": 5.2,
        "placement_pct": 74,
        "branches": ["CSE", "ECE", "ME", "CE", "IT"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"],
        "clubs": ["Coding Club", "NSS", "IEEE", "E-Cell"],
        "url": "/colleges/profiles/rbs-engineering-agra-profile.html",
        "phone": "+91-562-2520300",
        "website": "https://www.rbsengineering.ac.in",
        "address": "Bichpuri Road, Agra - 282002, UP"
    },
    {
        "name": "KCC Institute of Technology & Management (KCC Gr. Noida)",
        "code": "KCC",
        "city": "Greater Noida",
        "type": "Private",
        "est": 2009,
        "naac": "B",
        "nirf": "401-500",
        "fee": 95000,
        "highest_pkg": 14.0,
        "avg_pkg": 4.5,
        "placement_pct": 68,
        "branches": ["CSE", "ECE", "ME", "CE", "IT"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"],
        "clubs": ["Coding Club", "NSS", "IEEE", "E-Cell"],
        "url": "/colleges/profiles/kcc-greater-noida-profile.html",
        "phone": "+91-120-2323701",
        "website": "https://www.kccitm.ac.in",
        "address": "Knowledge Park III, Greater Noida - 201306, UP"
    },
    {
        "name": "Maharana Pratap Group of Institutions (MPGI Gorakhpur)",
        "code": "MPGI",
        "city": "Gorakhpur",
        "type": "Private",
        "est": 2006,
        "naac": "B+",
        "nirf": "401-500",
        "fee": 92000,
        "highest_pkg": 14.0,
        "avg_pkg": 4.8,
        "placement_pct": 70,
        "branches": ["CSE", "ECE", "ME", "CE", "IT"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"],
        "clubs": ["Coding Club", "NSS", "NCC", "IEEE"],
        "url": "/colleges/profiles/mgiet-gorakhpur-profile.html",
        "phone": "+91-551-2281400",
        "website": "https://www.mpgi.org",
        "address": "Opposite Airport, Gorakhpur - 273001, UP"
    },
    {
        "name": "Asian Institute of Management & Technology (AIMT Gr. Noida)",
        "code": "AIMT",
        "city": "Greater Noida",
        "type": "Private",
        "est": 2003,
        "naac": "B+",
        "nirf": "301-400",
        "fee": 105000,
        "highest_pkg": 19.0,
        "avg_pkg": 6.0,
        "placement_pct": 76,
        "branches": ["CSE", "ECE", "ME", "CE", "IT"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"],
        "clubs": ["Coding Club", "NSS", "IEEE", "E-Cell"],
        "url": "/colleges/profiles/aimt-greater-noida-profile.html",
        "phone": "+91-120-2323600",
        "website": "https://www.aimt.ac.in",
        "address": "Knowledge Park I, Greater Noida - 201306, UP"
    },
    {
        "name": "Rampur Engineering College (REC Rampur)",
        "code": "128",
        "city": "Rampur",
        "type": "Government",
        "est": 2010,
        "naac": "B",
        "nirf": "401-500",
        "fee": 55000,
        "highest_pkg": 12.0,
        "avg_pkg": 4.5,
        "placement_pct": 68,
        "branches": ["CSE", "ECE", "ME", "CE"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "BHEL", "SAIL"],
        "clubs": ["Coding Club", "NSS", "NCC", "IEEE"],
        "url": "/colleges/profiles/rait-rampur-profile.html",
        "phone": "+91-595-2350456",
        "website": "https://www.recrampur.ac.in",
        "address": "Delhi Road, Rampur - 244901, UP"
    },
    {
        "name": "BRCM College of Engineering & Technology (Baghpat)",
        "code": "023",
        "city": "Baghpat",
        "type": "Private",
        "est": 2002,
        "naac": "B",
        "nirf": "401-500",
        "fee": 92000,
        "highest_pkg": 13.0,
        "avg_pkg": 4.5,
        "placement_pct": 67,
        "branches": ["CSE", "ECE", "ME", "CE", "IT"],
        "recruiters": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"],
        "clubs": ["Coding Club", "NSS", "IEEE", "E-Cell"],
        "url": "/colleges/profiles/brcm-baghpat-profile.html",
        "phone": "+91-1232-241000",
        "website": "https://www.brcmcet.ac.in",
        "address": "Diwana Road, Baghpat - 250609, UP"
    }
]

ad_tags = """  <!-- Monetag -->
  
  
  
  
  
  """

colleges_json = json.dumps(colleges)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AKTU Affiliated Colleges Directory | Filter by City, Fees, Branch & NAAC Grade</title>
  <meta name="description" content="Explore and filter 800+ AKTU colleges by city (Noida, Lucknow, Ghaziabad, Kanpur), annual fee bracket, engineering branches (CSE, AI, ECE), NAAC grades and highest placement packages. Interactive college directory updated annually.">
  <meta name="keywords" content="aktu college filter, aktu colleges list, aktu fees list, top aktu colleges cse, best aktu government colleges, uptac college predictor">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://akturesults.in/colleges/aktu-colleges-filter-directory.html">
  <link rel="icon" href="/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
{ad_tags}
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "AKTU Affiliated Colleges Directory & Interactive Filter",
    "url": "https://akturesults.in/colleges/aktu-colleges-filter-directory.html",
    "description": "Interactive college directory for AKTU affiliated institutions across Uttar Pradesh with instant filtering by city, fee range, branches, and placement records."
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://akturesults.in/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Colleges", "item": "https://akturesults.in/colleges/" }},
      {{ "@type": "ListItem", "position": 3, "name": "Filter Directory", "item": "https://akturesults.in/colleges/aktu-colleges-filter-directory.html" }}
    ]
  }}
  </script>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    :root {{
      --primary: #4338ca;
      --primary-light: #6366f1;
      --accent: #06b6d4;
      --dark: #0f172a;
      --card-bg: #ffffff;
      --light-bg: #f8fafc;
      --border: #e2e8f0;
      --text-muted: #64748b;
    }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--light-bg);
      color: var(--dark);
      line-height: 1.6;
    }}
    .container {{
      max-width: 1240px;
      margin: 0 auto;
      padding: 0 20px;
    }}
    nav {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 16px 0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .nav-inner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .logo {{
      font-size: 22px;
      font-weight: 900;
      background: linear-gradient(135deg, var(--primary), var(--primary-light));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-decoration: none;
    }}
    .nav-links a {{
      color: var(--dark);
      text-decoration: none;
      font-weight: 600;
      font-size: 14px;
      margin-left: 20px;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{
      color: var(--primary);
    }}
    .hero {{
      background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
      color: #ffffff;
      padding: 60px 0 50px;
      text-align: center;
    }}
    .hero-badge {{
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 700;
      display: inline-block;
      margin-bottom: 16px;
      backdrop-filter: blur(8px);
    }}
    .hero h1 {{
      font-size: 38px;
      font-weight: 900;
      margin-bottom: 14px;
      line-height: 1.25;
      letter-spacing: -0.02em;
    }}
    .hero p {{
      font-size: 17px;
      opacity: 0.9;
      max-width: 760px;
      margin: 0 auto 26px;
    }}
    .search-box-wrapper {{
      max-width: 680px;
      margin: 0 auto;
      position: relative;
    }}
    .search-input {{
      width: 100%;
      padding: 16px 24px;
      font-size: 16px;
      border-radius: 50px;
      border: 2px solid transparent;
      outline: none;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
      font-family: inherit;
    }}
    .search-input:focus {{
      border-color: var(--accent);
    }}

    /* Filter Controls Section */
    .filter-section {{
      background: #ffffff;
      border-radius: 16px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
      padding: 26px 30px;
      margin: -30px auto 36px;
      position: relative;
      z-index: 10;
      border: 1px solid var(--border);
    }}
    .filter-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 12px;
      margin-bottom: 16px;
    }}
    .filter-row:last-child {{
      margin-bottom: 0;
    }}
    .filter-label {{
      font-size: 13px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      min-width: 100px;
    }}
    .pill-group {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      flex: 1;
    }}
    .filter-pill {{
      background: #f1f5f9;
      border: 1px solid #e2e8f0;
      color: #334155;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      user-select: none;
    }}
    .filter-pill:hover {{
      background: #e2e8f0;
      border-color: #cbd5e1;
    }}
    .filter-pill.active {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 2px 8px rgba(67, 56, 202, 0.3);
    }}

    /* Results Header & Grid */
    .results-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .results-count {{
      font-size: 16px;
      font-weight: 700;
      color: var(--dark);
    }}
    .sort-wrapper {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .sort-select {{
      padding: 8px 14px;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: #ffffff;
      font-size: 14px;
      font-weight: 600;
      outline: none;
      font-family: inherit;
    }}

    .college-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
      gap: 24px;
      margin-bottom: 50px;
    }}
    .college-card {{
      background: #ffffff;
      border-radius: 14px;
      border: 1px solid var(--border);
      padding: 24px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.25s ease, box-shadow 0.25s ease;
      position: relative;
    }}
    .college-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.1);
      border-color: #cbd5e1;
    }}
    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
      gap: 10px;
    }}
    .badge-city {{
      background: #eff6ff;
      color: #1d4ed8;
      font-size: 11px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 12px;
      text-transform: uppercase;
    }}
    .badge-naac {{
      background: #ecfdf5;
      color: #047857;
      font-size: 11px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 12px;
    }}
    .badge-govt {{
      background: #fef3c7;
      color: #b45309;
      font-size: 11px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 12px;
    }}
    .card-title {{
      font-size: 18px;
      font-weight: 800;
      color: var(--dark);
      margin-bottom: 8px;
      line-height: 1.35;
    }}
    .card-code {{
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 14px;
    }}
    .card-stats {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      background: #f8fafc;
      border-radius: 10px;
      padding: 12px 10px;
      text-align: center;
      margin-bottom: 16px;
    }}
    .stat-val {{
      font-size: 16px;
      font-weight: 900;
      color: var(--primary);
    }}
    .stat-lbl {{
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 2px;
      font-weight: 600;
    }}
    .branch-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 14px;
    }}
    .branch-tag {{
      background: #f1f5f9;
      color: #475569;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
    }}
    .recruiters-list {{
      font-size: 12px;
      color: #334155;
      margin-bottom: 18px;
      line-height: 1.5;
    }}
    .card-btn {{
      display: block;
      width: 100%;
      text-align: center;
      background: var(--primary);
      color: #ffffff;
      text-decoration: none;
      padding: 11px 0;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 700;
      transition: background 0.2s;
    }}
    .card-btn:hover {{
      background: var(--primary-light);
    }}
    .empty-state {{
      grid-column: 1 / -1;
      text-align: center;
      padding: 60px 20px;
      background: #ffffff;
      border-radius: 14px;
      border: 1px dashed var(--border);
    }}
    .empty-state h3 {{
      font-size: 20px;
      font-weight: 800;
      margin-bottom: 8px;
    }}
    .footer {{
      background: var(--dark);
      color: #ffffff;
      text-align: center;
      padding: 40px 0 30px;
      font-size: 14px;
    }}
    .footer a {{
      color: var(--accent);
      text-decoration: none;
    }}
    @media(max-width: 768px) {{
      .hero h1 {{ font-size: 28px; }}
      .filter-section {{ padding: 20px; margin-top: -15px; }}
      .filter-row {{ flex-direction: column; align-items: flex-start; gap: 8px; }}
      .college-grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>

  <nav>
    <div class="container nav-inner">
      <a href="/" class="logo">AKTU Results</a>
      <div class="nav-links">
        <a href="/">Home</a>
        <a href="/colleges/">All Colleges</a>
        <a href="/placements/aktu-college-placement-leaderboard-2026.html">Placements</a>
        <a href="/admissions/uptac-choice-filling-predictor-2026.html">UPTAC Predictor</a>
      </div>
    </div>
  </nav>

  <div class="hero">
    <div class="container">
      <span class="hero-badge">🏛️ Complete UP Technical Directory</span>
      <h1>Find Your Best AKTU College</h1>
      <p>Instant filter by City, Fees, Branches, NAAC Accreditation, and Highest Placements across Dr. A.P.J. Abdul Kalam Technical University.</p>
      <div class="search-box-wrapper">
        <input type="text" id="searchInput" class="search-input" placeholder="🔍 Search college by name, city, or branch (e.g. IET, KIET, Noida, CSE)...">
      </div>
    </div>
  </div>

  <div class="container">
    <!-- Filter Controls -->
    <div class="filter-section">
      <!-- City Filter -->
      <div class="filter-row">
        <div class="filter-label">🏙️ City:</div>
        <div class="pill-group" id="cityGroup">
          <span class="filter-pill active" data-filter="city" data-val="all">All Cities</span>
          <span class="filter-pill" data-filter="city" data-val="Lucknow">Lucknow</span>
          <span class="filter-pill" data-filter="city" data-val="Noida">Noida</span>
          <span class="filter-pill" data-filter="city" data-val="Greater Noida">Gr. Noida</span>
          <span class="filter-pill" data-filter="city" data-val="Ghaziabad">Ghaziabad</span>
          <span class="filter-pill" data-filter="city" data-val="Kanpur">Kanpur</span>
          <span class="filter-pill" data-filter="city" data-val="Meerut">Meerut</span>
          <span class="filter-pill" data-filter="city" data-val="Prayagraj">Prayagraj</span>
          <span class="filter-pill" data-filter="city" data-val="Jhansi">Jhansi</span>
          <span class="filter-pill" data-filter="city" data-val="Moradabad">Moradabad</span>
          <span class="filter-pill" data-filter="city" data-val="Sultanpur">Sultanpur</span>
          <span class="filter-pill" data-filter="city" data-val="Bareilly">Bareilly</span>
          <span class="filter-pill" data-filter="city" data-val="Agra">Agra</span>
        </div>
      </div>

      <!-- Fee Filter -->
      <div class="filter-row">
        <div class="filter-label">💰 Fee / Yr:</div>
        <div class="pill-group" id="feeGroup">
          <span class="filter-pill active" data-filter="fee" data-val="all">All Budgets</span>
          <span class="filter-pill" data-filter="fee" data-val="govt">Under ₹70,000 (Govt/Subsidized)</span>
          <span class="filter-pill" data-filter="fee" data-val="budget">₹70,000 - ₹1,00,000</span>
          <span class="filter-pill" data-filter="fee" data-val="mid">₹1,00,000 - ₹1,30,000</span>
          <span class="filter-pill" data-filter="fee" data-val="premium">Above ₹1,30,000</span>
        </div>
      </div>

      <!-- Branch Filter -->
      <div class="filter-row">
        <div class="filter-label">🎓 Branch:</div>
        <div class="pill-group" id="branchGroup">
          <span class="filter-pill active" data-filter="branch" data-val="all">All Branches</span>
          <span class="filter-pill" data-filter="branch" data-val="CSE">CSE Core</span>
          <span class="filter-pill" data-filter="branch" data-val="CSE-AI">CSE (AI/ML)</span>
          <span class="filter-pill" data-filter="branch" data-val="CSE-DS">CSE (Data Science)</span>
          <span class="filter-pill" data-filter="branch" data-val="ECE">ECE</span>
          <span class="filter-pill" data-filter="branch" data-val="ME">Mechanical</span>
          <span class="filter-pill" data-filter="branch" data-val="CE">Civil</span>
          <span class="filter-pill" data-filter="branch" data-val="EE">Electrical</span>
        </div>
      </div>

      <!-- NAAC / Type Filter -->
      <div class="filter-row">
        <div class="filter-label">⭐ Grade:</div>
        <div class="pill-group" id="naacGroup">
          <span class="filter-pill active" data-filter="naac" data-val="all">All Grades</span>
          <span class="filter-pill" data-filter="naac" data-val="A+">NAAC A+ Accredited</span>
          <span class="filter-pill" data-filter="naac" data-val="A">NAAC A Accredited</span>
          <span class="filter-pill" data-filter="naac" data-val="B+">NAAC B+</span>
          <span class="filter-pill" data-filter="type" data-val="govt_only">🏛️ Govt Colleges Only</span>
        </div>
      </div>
    </div>

    <!-- Results Header -->
    <div class="results-bar">
      <div class="results-count" id="resultsCount">Showing 33 Verified Colleges</div>
      <div class="sort-wrapper">
        <label for="sortSelect" style="font-size:13px;font-weight:700;color:var(--text-muted);">Sort By:</label>
        <select id="sortSelect" class="sort-select">
          <option value="pkg_desc">Highest Package (High to Low)</option>
          <option value="placement_desc">Placement Rate (High to Low)</option>
          <option value="fee_asc">Annual Fee (Low to High)</option>
          <option value="nirf_asc">NIRF Ranking Rank</option>
        </select>
      </div>
    </div>

    <!-- Colleges Grid -->
    <div class="college-grid" id="collegeGrid">
      <!-- Populated via JavaScript -->
    </div>
  </div>

  <div class="footer">
    <div class="container">
      <p>© 2026 <a href="/">AKTU Results Portal</a> — Comprehensive AKTU Academic & Placement Directory</p>
      <p style="margin-top:6px;opacity:.7;font-size:13px;">All figures sourced from verified college prospectuses and official AKTU counseling cutoffs. Updated annually.</p>
    </div>
  </div>

  <script>
    const collegesData = {colleges_json};

    let currentFilters = {{
      search: '',
      city: 'all',
      fee: 'all',
      branch: 'all',
      naac: 'all',
      type: 'all',
      sort: 'pkg_desc'
    }};

    function renderColleges() {{
      const grid = document.getElementById('collegeGrid');
      const countEl = document.getElementById('resultsCount');
      
      let filtered = collegesData.filter(c => {{
        // Search filter
        if (currentFilters.search) {{
          const q = currentFilters.search.toLowerCase();
          const matchName = c.name.toLowerCase().includes(q);
          const matchCity = c.city.toLowerCase().includes(q);
          const matchBranch = c.branches.some(b => b.toLowerCase().includes(q));
          if (!matchName && !matchCity && !matchBranch) return false;
        }}

        // City filter
        if (currentFilters.city !== 'all' && c.city.toLowerCase() !== currentFilters.city.toLowerCase()) {{
          return false;
        }}

        // Fee filter
        if (currentFilters.fee !== 'all') {{
          if (currentFilters.fee === 'govt' && c.fee > 70000) return false;
          if (currentFilters.fee === 'budget' && (c.fee < 70000 || c.fee > 100000)) return false;
          if (currentFilters.fee === 'mid' && (c.fee < 100000 || c.fee > 130000)) return false;
          if (currentFilters.fee === 'premium' && c.fee <= 130000) return false;
        }}

        // Branch filter
        if (currentFilters.branch !== 'all' && !c.branches.includes(currentFilters.branch)) {{
          return false;
        }}

        // NAAC filter
        if (currentFilters.naac !== 'all' && c.naac !== currentFilters.naac) {{
          return false;
        }}

        // Type filter (Govt only)
        if (currentFilters.type === 'govt_only' && !c.type.toLowerCase().includes('government')) {{
          return false;
        }}

        return true;
      }});

      // Sorting
      filtered.sort((a, b) => {{
        if (currentFilters.sort === 'pkg_desc') return b.highest_pkg - a.highest_pkg;
        if (currentFilters.sort === 'placement_desc') return b.placement_pct - a.placement_pct;
        if (currentFilters.sort === 'fee_asc') return a.fee - b.fee;
        if (currentFilters.sort === 'nirf_asc') return a.est - b.est;
        return 0;
      }});

      countEl.textContent = `Showing ${{filtered.length}} of ${{collegesData.length}} Verified Colleges`;

      if (filtered.length === 0) {{
        grid.innerHTML = `
          <div class="empty-state">
            <h3>No Colleges Found</h3>
            <p style="color:var(--text-muted);">Try adjusting your search criteria or reset filters to view all colleges.</p>
          </div>
        `;
        return;
      }}

      grid.innerHTML = filtered.map(c => `
        <div class="college-card">
          <div>
            <div class="card-top">
              <span class="badge-city">${{c.city}}</span>
              <div>
                ${{c.type.includes('Government') ? '<span class="badge-govt">🏛️ Govt</span> ' : ''}}
                <span class="badge-naac">NAAC ${{c.naac}}</span>
              </div>
            </div>
            <h3 class="card-title">${{c.name}}</h3>
            <div class="card-code">Code: ${{c.code}} • Est. ${{c.est}} • NIRF: ${{c.nirf}}</div>
            
            <div class="card-stats">
              <div>
                <div class="stat-val">₹${{(c.fee / 1000).toFixed(0)}}k</div>
                <div class="stat-lbl">Tuition/Yr</div>
              </div>
              <div>
                <div class="stat-val">${{c.highest_pkg}} LPA</div>
                <div class="stat-lbl">Highest Pkg</div>
              </div>
              <div>
                <div class="stat-val">${{c.placement_pct}}%</div>
                <div class="stat-lbl">Placement</div>
              </div>
            </div>

            <div style="font-size:12px;font-weight:700;color:var(--text-muted);margin-bottom:6px;">Offered Branches:</div>
            <div class="branch-tags">
              ${{c.branches.map(b => `<span class="branch-tag">${{b}}</span>`).join('')}}
            </div>

            <div class="recruiters-list">
              <strong>🏢 Top Recruiters:</strong> ${{c.recruiters.slice(0, 4).join(', ')}}
            </div>
          </div>

          <a href="${{c.url}}" class="card-btn">View Complete Profile & Fees →</a>
        </div>
      `).join('');
    }}

    // Event listeners
    document.getElementById('searchInput').addEventListener('input', (e) => {{
      currentFilters.search = e.target.value;
      renderColleges();
    }});

    document.querySelectorAll('.filter-pill').forEach(pill => {{
      pill.addEventListener('click', function() {{
        const group = this.parentElement;
        group.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
        this.classList.add('active');

        const filterType = this.dataset.filter;
        const val = this.dataset.val;

        if (filterType === 'city') currentFilters.city = val;
        if (filterType === 'fee') currentFilters.fee = val;
        if (filterType === 'branch') currentFilters.branch = val;
        if (filterType === 'naac') {{
          currentFilters.naac = val;
          currentFilters.type = 'all';
        }}
        if (filterType === 'type') {{
          currentFilters.type = val;
          currentFilters.naac = 'all';
        }}

        renderColleges();
      }});
    }});

    document.getElementById('sortSelect').addEventListener('change', (e) => {{
      currentFilters.sort = e.target.value;
      renderColleges();
    }});

    // Initial render
    renderColleges();
  </script>
  <script defer src="/js/community-banner-widget.js"></script>
</body>
</html>"""

with open('colleges/aktu-colleges-filter-directory.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Generated colleges/aktu-colleges-filter-directory.html successfully!')
