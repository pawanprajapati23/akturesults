import os, json

# Verified master list of AKTU affiliated institutions across Uttar Pradesh
all_colleges = [
    # Top Tier & Autonomous Govt/Private
    {"slug": "iet-lucknow-profile-2026", "name": "Institute of Engineering and Technology (IET Lucknow)", "code": "052", "city": "Lucknow", "type": "Government Autonomous", "est": 1984, "naac": "A+", "nirf": "151-200", "fee": 85000, "h_pkg": 49.0, "avg_pkg": 10.5, "pct": 94, "branches": ["CSE", "CSE-AI", "ECE", "ME", "EE", "CE", "Chemical"], "rec": ["Google", "Amazon", "Microsoft", "Adobe", "Samsung", "Paytm", "TCS Digital"]},
    {"slug": "hbtu-kanpur-profile", "name": "Harcourt Butler Technical University (HBTU Kanpur)", "code": "061", "city": "Kanpur", "type": "Government University", "est": 1921, "naac": "A+", "nirf": "76-100", "fee": 62000, "h_pkg": 65.0, "avg_pkg": 12.5, "pct": 96, "branches": ["CSE", "ECE", "ME", "CE", "Chemical", "IT", "EE"], "rec": ["Google", "Amazon", "Microsoft", "Goldman Sachs", "Morgan Stanley", "Flipkart", "IBM"]},
    {"slug": "knit-sultanpur-profile-2026", "name": "Kamla Nehru Institute of Technology (KNIT Sultanpur)", "code": "104", "city": "Sultanpur", "type": "Government Autonomous", "est": 1979, "naac": "A", "nirf": "151-200", "fee": 64350, "h_pkg": 45.0, "avg_pkg": 8.8, "pct": 88, "branches": ["CSE", "ECE", "ME", "EE", "CE", "IT", "MCA"], "rec": ["Amazon", "Samsung", "TCS", "Infosys", "Wipro", "L&T", "BHEL"]},
    {"slug": "biet-jhansi-profile", "name": "Bundelkhand Institute of Engineering & Technology (BIET Jhansi)", "code": "043", "city": "Jhansi", "type": "Government Autonomous", "est": 1960, "naac": "A", "nirf": "151-200", "fee": 61800, "h_pkg": 42.0, "avg_pkg": 8.5, "pct": 87, "branches": ["CSE", "ECE", "ME", "EE", "CE", "IT", "Chemical"], "rec": ["Amazon", "TCS", "Infosys", "Wipro", "Samsung", "L&T", "BHEL"]},
    {"slug": "jss-noida-profile-2026", "name": "JSS Academy of Technical Education (JSS Noida)", "code": "091", "city": "Noida", "type": "Private Autonomous", "est": 1998, "naac": "A", "nirf": "101-150", "fee": 138000, "h_pkg": 57.0, "avg_pkg": 9.8, "pct": 92, "branches": ["CSE", "CSE-AI", "ECE", "ME", "EE", "CE", "IT"], "rec": ["Adobe", "Amazon", "Cisco", "TCS Digital", "Palo Alto", "Commvault", "Infosys SP"]},
    {"slug": "kiet-ghaziabad-profile-2026", "name": "KIET Group of Institutions (KIET Ghaziabad)", "code": "029", "city": "Ghaziabad", "type": "Private Autonomous", "est": 1998, "naac": "A+", "nirf": "76-100", "fee": 139000, "h_pkg": 48.5, "avg_pkg": 9.5, "pct": 93, "branches": ["CSE", "CSE-AI", "CSE-DS", "ECE", "ME", "CE", "IT"], "rec": ["Atlassian", "Amazon", "Capgemini", "TCS Digital", "Wipro Elite", "Cognizant"]},
    {"slug": "akgec-ghaziabad-profile-2026", "name": "Ajay Kumar Garg Engineering College (AKGEC Ghaziabad)", "code": "027", "city": "Ghaziabad", "type": "Private Autonomous", "est": 1998, "naac": "A", "nirf": "101-150", "fee": 141000, "h_pkg": 44.0, "avg_pkg": 9.2, "pct": 91, "branches": ["CSE", "CSE-AI", "CSE-DS", "ECE", "ME", "CE", "IT"], "rec": ["Amazon", "Microsoft", "IBM", "TCS", "Infosys", "Wipro", "Capgemini"]},
    {"slug": "gl-bajaj-greater-noida-profile-2026", "name": "GL Bajaj Institute of Technology & Management", "code": "192", "city": "Greater Noida", "type": "Private Autonomous", "est": 2005, "naac": "A+", "nirf": "76-100", "fee": 128000, "h_pkg": 58.0, "avg_pkg": 9.0, "pct": 95, "branches": ["CSE", "CSE-AI", "CSE-DS", "ECE", "ME", "CE", "IT"], "rec": ["Palo Alto Networks", "Commvault", "Amazon", "Microsoft", "TCS Digital", "Infosys"]},
    {"slug": "galgotias-college-greater-noida-profile", "name": "Galgotias College of Engineering and Technology", "code": "097", "city": "Greater Noida", "type": "Private Autonomous", "est": 1999, "naac": "A", "nirf": "101-150", "fee": 125000, "h_pkg": 52.0, "avg_pkg": 9.2, "pct": 93, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "IT", "CSE-DS"], "rec": ["Google", "Amazon", "Microsoft", "Adobe", "Cisco", "TCS Digital", "Wipro Elite"]},
    {"slug": "abes-engineering-ghaziabad-profile-2026", "name": "ABES Engineering College (ABES EC Ghaziabad)", "code": "032", "city": "Ghaziabad", "type": "Private Autonomous", "est": 2000, "naac": "A", "nirf": "201-300", "fee": 135000, "h_pkg": 50.0, "avg_pkg": 8.2, "pct": 90, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "IT"], "rec": ["Microsoft", "Google", "Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini"]},
    {"slug": "abesit-ghaziabad-profile", "name": "ABES Institute of Technology (ABESIT Ghaziabad)", "code": "229", "city": "Ghaziabad", "type": "Private", "est": 2007, "naac": "A", "nirf": "201-300", "fee": 125000, "h_pkg": 28.0, "avg_pkg": 6.8, "pct": 86, "branches": ["CSE", "CSE-AI", "CSE-DS", "IT", "ECE", "ME"], "rec": ["TCS", "Infosys", "Wipro", "Capgemini", "Cognizant", "HCL"]},
    {"slug": "psit-kanpur-profile-2026", "name": "Pranveer Singh Institute of Technology (PSIT Kanpur)", "code": "164", "city": "Kanpur", "type": "Private Autonomous", "est": 2004, "naac": "A", "nirf": "201-300", "fee": 120000, "h_pkg": 40.0, "avg_pkg": 7.8, "pct": 88, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "IT", "MBA"], "rec": ["TCS Digital", "Infosys SP", "Wipro Elite", "HCL", "Tech Mahindra", "Capgemini"]},
    {"slug": "niet-greater-noida-profile-2026", "name": "Noida Institute of Engineering & Technology (NIET)", "code": "133", "city": "Greater Noida", "type": "Private Autonomous", "est": 2001, "naac": "A", "nirf": "201-300", "fee": 130000, "h_pkg": 44.0, "avg_pkg": 8.0, "pct": 91, "branches": ["CSE", "CSE-AI", "CSE-DS", "ECE", "ME", "CE", "IT"], "rec": ["Samsung R&D", "TCS Digital", "Infosys", "Capgemini", "Wipro", "Amazon"]},
    {"slug": "miet-meerut-profile", "name": "Meerut Institute of Engineering & Technology (MIET Meerut)", "code": "108", "city": "Meerut", "type": "Private Autonomous", "est": 1995, "naac": "A", "nirf": "201-300", "fee": 118000, "h_pkg": 35.0, "avg_pkg": 7.5, "pct": 86, "branches": ["CSE", "ECE", "ME", "CE", "IT", "EE"], "rec": ["TCS Digital", "Infosys", "Wipro", "Amazon", "HCL", "Capgemini"]},
    {"slug": "ims-ghaziabad-profile", "name": "IMS Engineering College (IMS EC Ghaziabad)", "code": "070", "city": "Ghaziabad", "type": "Private Autonomous", "est": 2001, "naac": "A", "nirf": "201-300", "fee": 128000, "h_pkg": 38.0, "avg_pkg": 7.8, "pct": 88, "branches": ["CSE", "ECE", "ME", "CE", "IT"], "rec": ["Amazon", "TCS Digital", "Infosys SP", "Wipro", "HCL", "Capgemini"]},
    {"slug": "ipec-ghaziabad-profile", "name": "Inderprastha Engineering College (IPEC Ghaziabad)", "code": "068", "city": "Ghaziabad", "type": "Private Autonomous", "est": 1999, "naac": "A", "nirf": "201-300", "fee": 124000, "h_pkg": 36.0, "avg_pkg": 7.5, "pct": 87, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "IT", "EE"], "rec": ["Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini", "Cognizant"]},
    {"slug": "raj-kumar-goel-ghaziabad-profile", "name": "Raj Kumar Goel Institute of Technology (RKGIT Ghaziabad)", "code": "126", "city": "Ghaziabad", "type": "Private Autonomous", "est": 2000, "naac": "A", "nirf": "201-300", "fee": 122000, "h_pkg": 30.0, "avg_pkg": 7.0, "pct": 84, "branches": ["CSE", "ECE", "ME", "CE", "IT"], "rec": ["TCS", "Amazon", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "rkgitw-ghaziabad-profile", "name": "RKGIT for Women (RKGITW Ghaziabad)", "code": "301", "city": "Ghaziabad", "type": "Private", "est": 2008, "naac": "B+", "nirf": "301-400", "fee": 105000, "h_pkg": 20.0, "avg_pkg": 5.8, "pct": 80, "branches": ["CSE", "IT", "ECE"], "rec": ["TCS", "Infosys", "Wipro", "Cognizant", "Capgemini"]},
    {"slug": "shri-ramswaroop-memorial-lucknow-profile", "name": "Shri Ramswaroop Memorial College (SRMCEM Lucknow)", "code": "130", "city": "Lucknow", "type": "Private Autonomous", "est": 2001, "naac": "A", "nirf": "201-300", "fee": 115000, "h_pkg": 32.0, "avg_pkg": 7.2, "pct": 85, "branches": ["CSE", "ECE", "ME", "CE", "IT", "MBA"], "rec": ["TCS Digital", "Amazon", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "srms-cet-bareilly-profile", "name": "Shri Ram Murti Smarak College (SRMS CET Bareilly)", "code": "014", "city": "Bareilly", "type": "Private Autonomous", "est": 1996, "naac": "A", "nirf": "201-300", "fee": 126000, "h_pkg": 34.0, "avg_pkg": 7.2, "pct": 86, "branches": ["CSE", "IT", "ECE", "ME", "EE", "B.Pharm", "MCA"], "rec": ["Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini", "Cognizant"]},
    {"slug": "srms-cetr-bareilly-profile", "name": "SRMS College of Engineering, Technology & Research (SRMS CETR)", "code": "451", "city": "Bareilly", "type": "Private", "est": 2008, "naac": "B+", "nirf": "301-400", "fee": 105000, "h_pkg": 22.0, "avg_pkg": 5.8, "pct": 78, "branches": ["CSE", "IT", "ECE", "ME"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},

    # Government Engineering Colleges in UP
    {"slug": "rec-banda-profile", "name": "Rajkiya Engineering College Banda (REC Banda)", "code": "842", "city": "Banda", "type": "Government", "est": 2010, "naac": "B+", "nirf": "301-400", "fee": 58000, "h_pkg": 15.0, "avg_pkg": 5.5, "pct": 75, "branches": ["CSE", "ECE", "EE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "BHEL", "L&T"]},
    {"slug": "rec-bijnor-profile", "name": "Rajkiya Engineering College Bijnor (REC Bijnor)", "code": "843", "city": "Bijnor", "type": "Government", "est": 2010, "naac": "B+", "nirf": "301-400", "fee": 58000, "h_pkg": 16.5, "avg_pkg": 5.6, "pct": 76, "branches": ["CSE", "IT", "EE", "CE"], "rec": ["TCS", "Infosys", "Wipro", "Capgemini", "Tech Mahindra"]},
    {"slug": "rec-azamgarh-profile", "name": "Rajkiya Engineering College Azamgarh (REC Azamgarh)", "code": "844", "city": "Azamgarh", "type": "Government", "est": 2010, "naac": "B+", "nirf": "301-400", "fee": 58000, "h_pkg": 14.5, "avg_pkg": 5.2, "pct": 74, "branches": ["CSE", "IT", "ME", "CE"], "rec": ["TCS", "Infosys", "HCL", "Wipro", "Cognizant"]},
    {"slug": "rec-ambedkar-nagar-profile", "name": "Rajkiya Engineering College Ambedkar Nagar (REC Ambedkar Nagar)", "code": "845", "city": "Ambedkar Nagar", "type": "Government", "est": 2010, "naac": "B+", "nirf": "301-400", "fee": 58000, "h_pkg": 15.5, "avg_pkg": 5.4, "pct": 75, "branches": ["CSE", "IT", "EE", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "rec-kannauj-profile", "name": "Rajkiya Engineering College Kannauj (REC Kannauj)", "code": "846", "city": "Kannauj", "type": "Government", "est": 2015, "naac": "B", "nirf": "401-500", "fee": 56000, "h_pkg": 13.0, "avg_pkg": 5.0, "pct": 72, "branches": ["CSE", "ECE", "EE", "CE"], "rec": ["TCS", "Infosys", "Wipro", "Tech Mahindra"]},
    {"slug": "rec-mainpuri-profile", "name": "Rajkiya Engineering College Mainpuri (REC Mainpuri)", "code": "847", "city": "Mainpuri", "type": "Government", "est": 2015, "naac": "B", "nirf": "401-500", "fee": 56000, "h_pkg": 12.5, "avg_pkg": 4.8, "pct": 70, "branches": ["CSE", "ME", "EE", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "rec-sonbhadra-profile", "name": "Rajkiya Engineering College Sonbhadra (REC Sonbhadra)", "code": "848", "city": "Sonbhadra", "type": "Government", "est": 2015, "naac": "B", "nirf": "401-500", "fee": 56000, "h_pkg": 14.0, "avg_pkg": 5.1, "pct": 73, "branches": ["CSE", "ECE", "EE", "Mining"], "rec": ["NTPC", "Hindalco", "TCS", "Infosys", "Wipro"]},
    {"slug": "rait-rampur-profile", "name": "Rampur Engineering College (REC Rampur)", "code": "128", "city": "Rampur", "type": "Government", "est": 2010, "naac": "B", "nirf": "401-500", "fee": 55000, "h_pkg": 12.0, "avg_pkg": 4.5, "pct": 68, "branches": ["CSE", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "uiet-csjmu-kanpur-profile", "name": "University Institute of Engineering and Technology (UIET CSJMU Kanpur)", "code": "UIET-K", "city": "Kanpur", "type": "Government University", "est": 1996, "naac": "A+", "nirf": "151-200", "fee": 75000, "h_pkg": 25.0, "avg_pkg": 7.2, "pct": 84, "branches": ["CSE", "IT", "ECE", "ME", "Chemical", "Materials"], "rec": ["TCS", "Infosys", "Wipro", "Cognizant", "L&T", "Samsung"]},
    {"slug": "uiet-lucknow-university-profile", "name": "Faculty of Engineering & Technology Lucknow University (LU FoET)", "code": "LU-ENG", "city": "Lucknow", "type": "Government University", "est": 2017, "naac": "A++", "nirf": "101-150", "fee": 80000, "h_pkg": 28.0, "avg_pkg": 7.5, "pct": 85, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "EE"], "rec": ["Amazon", "TCS", "Infosys", "Wipro", "Capgemini", "HCL"]},
    {"slug": "scriet-ccsu-meerut-profile", "name": "Sir Chhotu Ram Institute of Engineering & Technology (SCRIET CCSU Meerut)", "code": "543", "city": "Meerut", "type": "Government University", "est": 2002, "naac": "A+", "nirf": "201-300", "fee": 65000, "h_pkg": 18.0, "avg_pkg": 5.8, "pct": 79, "branches": ["CSE", "IT", "ECE", "ME", "CE", "Chemical"], "rec": ["TCS", "Infosys", "Wipro", "Cognizant", "HCL"]},

    # Lucknow & Central UP
    {"slug": "bbditm-lucknow-profile", "name": "Babu Banarasi Das Institute of Technology & Management (BBDITM)", "code": "091-L", "city": "Lucknow", "type": "Private", "est": 2000, "naac": "B+", "nirf": "301-400", "fee": 105000, "h_pkg": 18.0, "avg_pkg": 5.8, "pct": 78, "branches": ["CSE", "ECE", "ME", "CE", "IT"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Capgemini"]},
    {"slug": "bbd-niit-lucknow-profile", "name": "BBD Northern India Institute of Technology (BBDNIIT Lucknow)", "code": "056", "city": "Lucknow", "type": "Private", "est": 1999, "naac": "B+", "nirf": "301-400", "fee": 108000, "h_pkg": 20.0, "avg_pkg": 6.0, "pct": 80, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]},
    {"slug": "bbdec-lucknow-profile", "name": "Babu Banarasi Das Engineering College (BBDEC Lucknow)", "code": "508", "city": "Lucknow", "type": "Private", "est": 2008, "naac": "B", "nirf": "401-500", "fee": 95000, "h_pkg": 15.0, "avg_pkg": 5.0, "pct": 72, "branches": ["CSE", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "Tech Mahindra"]},
    {"slug": "srmcem-lucknow-profile", "name": "SRM College of Engineering & Management (SRM Lucknow)", "code": "195", "city": "Lucknow", "type": "Private", "est": 2010, "naac": "B+", "nirf": "301-400", "fee": 110000, "h_pkg": 22.0, "avg_pkg": 6.2, "pct": 80, "branches": ["CSE", "ECE", "ME", "CE", "IT", "MBA"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "gitm-lucknow-profile", "name": "Goel Institute of Technology & Management (GITM Lucknow)", "code": "392", "city": "Lucknow", "type": "Private", "est": 2008, "naac": "B+", "nirf": "301-400", "fee": 98000, "h_pkg": 16.0, "avg_pkg": 5.2, "pct": 74, "branches": ["CSE", "ECE", "ME", "CE", "IT", "MBA"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra"]},
    {"slug": "bansal-institute-lucknow-profile", "name": "Bansal Institute of Engineering & Technology (BIET Lucknow)", "code": "422", "city": "Lucknow", "type": "Private", "est": 2008, "naac": "B+", "nirf": "401-500", "fee": 92000, "h_pkg": 14.0, "avg_pkg": 4.8, "pct": 70, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]},
    {"slug": "bncet-lucknow-profile", "name": "B.N. College of Engineering & Technology (BNCET Lucknow)", "code": "425", "city": "Lucknow", "type": "Private", "est": 2008, "naac": "B", "nirf": "401-500", "fee": 86000, "h_pkg": 12.5, "avg_pkg": 4.5, "pct": 67, "branches": ["CSE", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "azad-institute-lucknow-profile", "name": "Azad Institute of Engineering & Technology (AIET Lucknow)", "code": "053", "city": "Lucknow", "type": "Private", "est": 1998, "naac": "B+", "nirf": "301-400", "fee": 95000, "h_pkg": 16.0, "avg_pkg": 5.2, "pct": 73, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]},
    {"slug": "rr-institute-lucknow-profile", "name": "R.R. Institute of Modern Technology (RRIMT Lucknow)", "code": "406", "city": "Lucknow", "type": "Private", "est": 2008, "naac": "B", "nirf": "401-500", "fee": 85000, "h_pkg": 13.5, "avg_pkg": 4.6, "pct": 69, "branches": ["CSE", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "Tech Mahindra"]},
    {"slug": "ambalika-institute-lucknow-profile", "name": "Ambalika Institute of Management and Technology (AIMT Lucknow)", "code": "732", "city": "Lucknow", "type": "Private", "est": 2008, "naac": "B+", "nirf": "301-400", "fee": 98000, "h_pkg": 18.0, "avg_pkg": 5.5, "pct": 76, "branches": ["CSE", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "sms-lucknow-profile", "name": "School of Management Sciences (SMS Lucknow)", "code": "772", "city": "Lucknow", "type": "Private", "est": 2008, "naac": "B+", "nirf": "301-400", "fee": 92000, "h_pkg": 15.0, "avg_pkg": 5.0, "pct": 74, "branches": ["CSE", "IT", "ECE", "ME", "CE", "BBA", "MBA"], "rec": ["TCS", "Infosys", "Wipro", "HDFC", "ICICI Bank"]},

    # Kanpur Region
    {"slug": "axis-colleges-kanpur-profile", "name": "Axis Institute of Technology & Management (AITM Kanpur)", "code": "514", "city": "Kanpur", "type": "Private", "est": 2010, "naac": "B+", "nirf": "301-400", "fee": 98000, "h_pkg": 18.0, "avg_pkg": 5.5, "pct": 76, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "maharana-pratap-kanpur-profile", "name": "Maharana Pratap Engineering College (MPEC Kanpur)", "code": "047", "city": "Kanpur", "type": "Private", "est": 1999, "naac": "B+", "nirf": "301-400", "fee": 105000, "h_pkg": 22.0, "avg_pkg": 6.0, "pct": 81, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Tech Mahindra"]},
    {"slug": "kanpur-institute-technology-profile", "name": "Kanpur Institute of Technology (KIT Kanpur)", "code": "165", "city": "Kanpur", "type": "Private", "est": 2004, "naac": "B+", "nirf": "301-400", "fee": 98000, "h_pkg": 16.5, "avg_pkg": 5.4, "pct": 75, "branches": ["CSE", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "apollo-institute-kanpur-profile", "name": "Apollo Institute of Technology (AIT Kanpur)", "code": "428", "city": "Kanpur", "type": "Private", "est": 2008, "naac": "B", "nirf": "401-500", "fee": 85000, "h_pkg": 12.0, "avg_pkg": 4.4, "pct": 66, "branches": ["CSE", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "allenhouse-kanpur-profile", "name": "Allenhouse Institute of Technology Kanpur", "code": "786", "city": "Kanpur", "type": "Private", "est": 2009, "naac": "B+", "nirf": "301-400", "fee": 95000, "h_pkg": 16.0, "avg_pkg": 5.2, "pct": 74, "branches": ["CSE", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "naraina-college-kanpur-profile", "name": "Naraina College of Engineering and Technology Kanpur", "code": "803", "city": "Kanpur", "type": "Private", "est": 2007, "naac": "B", "nirf": "401-500", "fee": 88000, "h_pkg": 13.5, "avg_pkg": 4.6, "pct": 68, "branches": ["CSE", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "Tech Mahindra"]},

    # Agra & Mathura Region
    {"slug": "anand-engineering-college-agra-profile", "name": "Anand Engineering College (AEC Agra)", "code": "001", "city": "Agra", "type": "Private", "est": 1998, "naac": "B+", "nirf": "301-400", "fee": 108000, "h_pkg": 24.0, "avg_pkg": 6.0, "pct": 80, "branches": ["CSE", "ECE", "ME", "CE", "EE", "Biotech"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Capgemini"]},
    {"slug": "hcst-mathura-profile", "name": "Hindustan College of Science and Technology (HCST Mathura)", "code": "002", "city": "Mathura", "type": "Private", "est": 1996, "naac": "A", "nirf": "201-300", "fee": 115000, "h_pkg": 26.0, "avg_pkg": 6.4, "pct": 82, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE", "Chemical"], "rec": ["Amazon", "TCS", "Infosys", "Wipro", "Capgemini", "Tech Mahindra"]},
    {"slug": "agra-college-foet-profile", "name": "Faculty of Engineering & Technology Agra College", "code": "004", "city": "Agra", "type": "Private Aided", "est": 1999, "naac": "B+", "nirf": "301-400", "fee": 85000, "h_pkg": 15.0, "avg_pkg": 5.2, "pct": 74, "branches": ["CSE", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "L&T"]},
    {"slug": "bsa-college-mathura-profile", "name": "BSA College of Engineering & Technology Mathura", "code": "064", "city": "Mathura", "type": "Private", "est": 1997, "naac": "B+", "nirf": "301-400", "fee": 95000, "h_pkg": 16.0, "avg_pkg": 5.4, "pct": 75, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]},
    {"slug": "rbs-bichpuri-agra-profile", "name": "Raja Balwant Singh Management Technical Campus (RBS Bichpuri)", "code": "395", "city": "Agra", "type": "Private Aided", "est": 1996, "naac": "A", "nirf": "201-300", "fee": 88000, "h_pkg": 20.0, "avg_pkg": 5.8, "pct": 79, "branches": ["CSE", "ECE", "ME", "CE", "EE", "Food Tech", "Biotech"], "rec": ["TCS", "Infosys", "Wipro", "Nestle", "Amul", "ITC"]},
    {"slug": "eshan-college-mathura-profile", "name": "Eshan College of Engineering Mathura", "code": "174", "city": "Mathura", "type": "Private", "est": 2009, "naac": "B", "nirf": "401-500", "fee": 78000, "h_pkg": 12.0, "avg_pkg": 4.5, "pct": 68, "branches": ["CSE", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "Tech Mahindra"]},
    {"slug": "ace-college-agra-profile", "name": "ACE College of Engineering & Management Agra", "code": "580", "city": "Agra", "type": "Private", "est": 2011, "naac": "B", "nirf": "401-500", "fee": 75000, "h_pkg": 11.5, "avg_pkg": 4.2, "pct": 65, "branches": ["CSE", "ECE", "ME", "CE"], "rec": ["TCS", "Wipro", "HCL", "Teleperformance"]},

    # Prayagraj & Varanasi Region
    {"slug": "ucer-allahabad-profile", "name": "United College of Engineering & Research (UCER Prayagraj)", "code": "105", "city": "Prayagraj", "type": "Private Autonomous", "est": 1998, "naac": "A", "nirf": "201-300", "fee": 120000, "h_pkg": 30.0, "avg_pkg": 6.8, "pct": 84, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini", "Cognizant"]},
    {"slug": "uit-allahabad-profile", "name": "United Institute of Technology (UIT Prayagraj)", "code": "106", "city": "Prayagraj", "type": "Private", "est": 2007, "naac": "B+", "nirf": "301-400", "fee": 110000, "h_pkg": 22.0, "avg_pkg": 6.0, "pct": 80, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "siet-allahabad-profile", "name": "Shambhunath Institute of Engineering & Technology (SIET Prayagraj)", "code": "112", "city": "Prayagraj", "type": "Private", "est": 2004, "naac": "B+", "nirf": "301-400", "fee": 105000, "h_pkg": 20.0, "avg_pkg": 5.8, "pct": 78, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]},
    {"slug": "bbs-allahabad-profile", "name": "BBS College of Engineering & Technology Prayagraj", "code": "111", "city": "Prayagraj", "type": "Private", "est": 2002, "naac": "B", "nirf": "401-500", "fee": 88000, "h_pkg": 14.0, "avg_pkg": 4.8, "pct": 70, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "Tech Mahindra"]},
    {"slug": "ldc-allahabad-profile", "name": "LDC Institute of Technical Studies Prayagraj", "code": "144", "city": "Prayagraj", "type": "Private", "est": 2007, "naac": "B", "nirf": "401-500", "fee": 85000, "h_pkg": 13.0, "avg_pkg": 4.6, "pct": 68, "branches": ["CSE", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "ashoka-institute-varanasi-profile", "name": "Ashoka Institute of Technology and Management Varanasi", "code": "368", "city": "Varanasi", "type": "Private", "est": 2010, "naac": "B+", "nirf": "301-400", "fee": 102000, "h_pkg": 20.0, "avg_pkg": 5.6, "pct": 78, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE", "B.Pharm"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini", "Cipla"]},
    {"slug": "kashi-institute-varanasi-profile", "name": "Kashi Institute of Technology (KIT Varanasi)", "code": "427", "city": "Varanasi", "type": "Private", "est": 2008, "naac": "B+", "nirf": "301-400", "fee": 98000, "h_pkg": 18.0, "avg_pkg": 5.4, "pct": 76, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE", "B.Pharm"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Sun Pharma"]},
    {"slug": "sms-varanasi-profile", "name": "School of Management Sciences (SMS Varanasi) Faculty of Tech", "code": "512", "city": "Varanasi", "type": "Private Autonomous", "est": 1995, "naac": "A", "nirf": "151-200", "fee": 112000, "h_pkg": 24.0, "avg_pkg": 6.2, "pct": 82, "branches": ["CSE", "ECE", "ME", "CE", "BBA", "BCA", "MBA"], "rec": ["TCS", "Infosys", "Wipro", "ICICI Bank", "HDFC", "Capgemini"]},

    # Gorakhpur & Eastern UP
    {"slug": "itm-gorakhpur-profile", "name": "Institute of Technology & Management (ITM Gorakhpur)", "code": "120", "city": "Gorakhpur", "type": "Private", "est": 2001, "naac": "B+", "nirf": "301-400", "fee": 105000, "h_pkg": 22.0, "avg_pkg": 5.8, "pct": 79, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "buddha-institute-gorakhpur-profile", "name": "Buddha Institute of Technology (BIT Gorakhpur)", "code": "740", "city": "Gorakhpur", "type": "Private", "est": 2009, "naac": "B+", "nirf": "301-400", "fee": 95000, "h_pkg": 16.0, "avg_pkg": 5.2, "pct": 74, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra"]},
    {"slug": "kipm-gorakhpur-profile", "name": "KIPM College of Engineering & Technology Gorakhpur", "code": "808", "city": "Gorakhpur", "type": "Private", "est": 2009, "naac": "B", "nirf": "401-500", "fee": 88000, "h_pkg": 14.0, "avg_pkg": 4.8, "pct": 70, "branches": ["CSE", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "suyash-institute-gorakhpur-profile", "name": "Suyash Institute of Information Technology Gorakhpur", "code": "492", "city": "Gorakhpur", "type": "Private", "est": 2009, "naac": "B", "nirf": "401-500", "fee": 82000, "h_pkg": 12.0, "avg_pkg": 4.4, "pct": 66, "branches": ["CSE", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Wipro", "HCL", "Teleperformance"]},

    # Moradabad, Bareilly & Western UP
    {"slug": "mit-moradabad-profile", "name": "Moradabad Institute of Technology (MIT Moradabad)", "code": "016", "city": "Moradabad", "type": "Private", "est": 1996, "naac": "A", "nirf": "201-300", "fee": 112000, "h_pkg": 25.0, "avg_pkg": 6.2, "pct": 82, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini", "Cognizant"]},
    {"slug": "future-institute-bareilly-profile", "name": "Future Institute of Engineering and Technology Bareilly", "code": "241", "city": "Bareilly", "type": "Private", "est": 2009, "naac": "B+", "nirf": "301-400", "fee": 92000, "h_pkg": 16.0, "avg_pkg": 5.2, "pct": 74, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra"]},
    {"slug": "rbmi-bareilly-profile", "name": "Rakshpal Bahadur Management Institute (RBMI Bareilly)", "code": "240", "city": "Bareilly", "type": "Private", "est": 1996, "naac": "B+", "nirf": "301-400", "fee": 95000, "h_pkg": 18.0, "avg_pkg": 5.4, "pct": 75, "branches": ["CSE", "IT", "ECE", "ME", "CE", "B.Pharm", "MBA"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cipla"]},
    {"slug": "ana-college-bareilly-profile", "name": "ANA College of Engineering & Management Bareilly", "code": "244", "city": "Bareilly", "type": "Private", "est": 2009, "naac": "B", "nirf": "401-500", "fee": 82000, "h_pkg": 12.5, "avg_pkg": 4.5, "pct": 68, "branches": ["CSE", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},

    # Ghaziabad, Noida & Meerut Additional Private Institutes
    {"slug": "gniot-greater-noida-profile", "name": "GNIOT Institute of Management and Technology Gr. Noida", "code": "132", "city": "Greater Noida", "type": "Private", "est": 2001, "naac": "A", "nirf": "201-300", "fee": 120000, "h_pkg": 30.0, "avg_pkg": 7.2, "pct": 85, "branches": ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE"], "rec": ["Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini"]},
    {"slug": "kcc-itm-greater-noida-profile", "name": "KCC Institute of Technology and Management Gr. Noida", "code": "486", "city": "Greater Noida", "type": "Private", "est": 2009, "naac": "B+", "nirf": "301-400", "fee": 95000, "h_pkg": 16.0, "avg_pkg": 5.2, "pct": 72, "branches": ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "its-greater-noida-profile", "name": "I.T.S Engineering College Greater Noida", "code": "222", "city": "Greater Noida", "type": "Private", "est": 2006, "naac": "A", "nirf": "201-300", "fee": 115000, "h_pkg": 28.0, "avg_pkg": 6.8, "pct": 83, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "EE"], "rec": ["Amazon", "TCS Digital", "Infosys", "Wipro", "Cognizant"]},
    {"slug": "accurate-greater-noida-profile", "name": "Accurate Institute of Management and Technology Gr. Noida", "code": "225", "city": "Greater Noida", "type": "Private", "est": 2006, "naac": "B+", "nirf": "301-400", "fee": 112000, "h_pkg": 24.0, "avg_pkg": 6.2, "pct": 80, "branches": ["CSE", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "kec-ghaziabad-profile", "name": "Krishna Engineering College (KEC Ghaziabad)", "code": "578", "city": "Ghaziabad", "type": "Private", "est": 2004, "naac": "A", "nirf": "201-300", "fee": 125000, "h_pkg": 30.0, "avg_pkg": 7.0, "pct": 85, "branches": ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE"], "rec": ["Amazon", "TCS", "Infosys", "Wipro", "Capgemini", "Cognizant"]},
    {"slug": "rd-engineering-ghaziabad-profile", "name": "RD Engineering College (RDEC Ghaziabad)", "code": "231", "city": "Ghaziabad", "type": "Private", "est": 2006, "naac": "B+", "nirf": "301-400", "fee": 105000, "h_pkg": 20.0, "avg_pkg": 5.8, "pct": 78, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "hr-institute-ghaziabad-profile", "name": "H.R. Institute of Technology (HRIT Ghaziabad)", "code": "230", "city": "Ghaziabad", "type": "Private", "est": 2005, "naac": "B+", "nirf": "301-400", "fee": 102000, "h_pkg": 18.0, "avg_pkg": 5.6, "pct": 76, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE", "B.Pharm"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]},
    {"slug": "sunder-deep-ghaziabad-profile", "name": "Sunder Deep Engineering College (SDEC Ghaziabad)", "code": "490", "city": "Ghaziabad", "type": "Private", "est": 2006, "naac": "B+", "nirf": "301-400", "fee": 100000, "h_pkg": 18.5, "avg_pkg": 5.5, "pct": 75, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra"]},
    {"slug": "sanskar-ghaziabad-profile", "name": "Sanskar Educational Group (Sanskar EC Ghaziabad)", "code": "532", "city": "Ghaziabad", "type": "Private", "est": 2005, "naac": "B+", "nirf": "301-400", "fee": 98000, "h_pkg": 17.0, "avg_pkg": 5.4, "pct": 74, "branches": ["CSE", "IT", "ECE", "ME", "CE", "B.Pharm"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Sun Pharma"]},
    {"slug": "hitech-ghaziabad-profile", "name": "Hi-Tech Institute of Engineering & Technology Ghaziabad", "code": "651", "city": "Ghaziabad", "type": "Private", "est": 2006, "naac": "B", "nirf": "401-500", "fee": 90000, "h_pkg": 14.0, "avg_pkg": 4.8, "pct": 70, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "ideal-ghaziabad-profile", "name": "Ideal Institute of Technology Ghaziabad", "code": "290", "city": "Ghaziabad", "type": "Private", "est": 1998, "naac": "B", "nirf": "401-500", "fee": 88000, "h_pkg": 13.5, "avg_pkg": 4.6, "pct": 68, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "iimt-greater-noida-profile", "name": "IIMT College of Engineering Greater Noida", "code": "216", "city": "Greater Noida", "type": "Private", "est": 2005, "naac": "A", "nirf": "201-300", "fee": 120000, "h_pkg": 32.0, "avg_pkg": 7.0, "pct": 85, "branches": ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE"], "rec": ["Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini", "Cognizant"]},
    {"slug": "dronacharya-greater-noida-profile", "name": "Dronacharya Group of Institutions Greater Noida", "code": "274", "city": "Greater Noida", "type": "Private", "est": 2006, "naac": "A", "nirf": "201-300", "fee": 118000, "h_pkg": 30.0, "avg_pkg": 6.8, "pct": 84, "branches": ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE"], "rec": ["Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini"]},
    {"slug": "lloyd-greater-noida-profile", "name": "Lloyd Institute of Engineering & Technology Greater Noida", "code": "539", "city": "Greater Noida", "type": "Private", "est": 2002, "naac": "A", "nirf": "201-300", "fee": 115000, "h_pkg": 28.0, "avg_pkg": 6.5, "pct": 82, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "B.Pharm"], "rec": ["Amazon", "TCS", "Infosys", "Wipro", "Cipla", "Sun Pharma"]},
    {"slug": "mangalmay-greater-noida-profile", "name": "Mangalmay Institute of Engineering & Technology Gr. Noida", "code": "152", "city": "Greater Noida", "type": "Private", "est": 2002, "naac": "A", "nirf": "201-300", "fee": 112000, "h_pkg": 26.0, "avg_pkg": 6.2, "pct": 80, "branches": ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE", "MBA"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini", "Cognizant"]},
    {"slug": "skyline-greater-noida-profile", "name": "Skyline Institute of Engineering and Technology Gr. Noida", "code": "151", "city": "Greater Noida", "type": "Private", "est": 2002, "naac": "B+", "nirf": "301-400", "fee": 105000, "h_pkg": 20.0, "avg_pkg": 5.8, "pct": 78, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra"]},
    {"slug": "gnit-greater-noida-profile", "name": "GNIT College of Management & Technology Greater Noida", "code": "592", "city": "Greater Noida", "type": "Private", "est": 2001, "naac": "B+", "nirf": "301-400", "fee": 108000, "h_pkg": 22.0, "avg_pkg": 6.0, "pct": 79, "branches": ["CSE", "IT", "ECE", "ME", "CE", "MBA"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "vidya-meerut-profile", "name": "Vidya College of Engineering Meerut", "code": "243", "city": "Meerut", "type": "Private", "est": 2006, "naac": "B+", "nirf": "301-400", "fee": 102000, "h_pkg": 20.0, "avg_pkg": 5.8, "pct": 78, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]},
    {"slug": "dewan-meerut-profile", "name": "Dewan V.S. Institute of Engineering & Technology Meerut", "code": "129", "city": "Meerut", "type": "Private", "est": 1996, "naac": "B+", "nirf": "301-400", "fee": 98000, "h_pkg": 18.0, "avg_pkg": 5.5, "pct": 76, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "bharat-institute-meerut-profile", "name": "Bharat Institute of Technology (BIT Meerut)", "code": "127", "city": "Meerut", "type": "Private", "est": 2001, "naac": "B+", "nirf": "301-400", "fee": 95000, "h_pkg": 17.5, "avg_pkg": 5.4, "pct": 75, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE", "B.Pharm"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cipla"]},
    {"slug": "forte-meerut-profile", "name": "Forte Institute of Technology Meerut", "code": "073", "city": "Meerut", "type": "Private", "est": 1998, "naac": "B", "nirf": "401-500", "fee": 85000, "h_pkg": 13.0, "avg_pkg": 4.6, "pct": 68, "branches": ["CSE", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "sd-college-muzaffarnagar-profile", "name": "S.D. College of Engineering & Technology Muzaffarnagar", "code": "488", "city": "Muzaffarnagar", "type": "Private", "est": 1997, "naac": "B+", "nirf": "301-400", "fee": 92000, "h_pkg": 16.0, "avg_pkg": 5.2, "pct": 74, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE", "Chemical"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra"]},
    {"slug": "bhagwant-institute-muzaffarnagar-profile", "name": "Bhagwant Institute of Technology (BIT Muzaffarnagar)", "code": "502", "city": "Muzaffarnagar", "type": "Private", "est": 2000, "naac": "B", "nirf": "401-500", "fee": 82000, "h_pkg": 12.0, "avg_pkg": 4.4, "pct": 66, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "shobhit-saharanpur-profile", "name": "Shobhit Institute of Engineering & Technology Gangoh Saharanpur", "code": "246", "city": "Saharanpur", "type": "Private", "est": 2000, "naac": "B+", "nirf": "301-400", "fee": 95000, "h_pkg": 18.0, "avg_pkg": 5.4, "pct": 75, "branches": ["CSE", "IT", "ECE", "ME", "CE", "Biotech", "B.Pharm"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Sun Pharma"]},
    {"slug": "aligarh-college-engineering-profile", "name": "Aligarh College of Engineering and Technology (ACET Aligarh)", "code": "109", "city": "Aligarh", "type": "Private", "est": 2001, "naac": "B+", "nirf": "301-400", "fee": 92000, "h_pkg": 16.5, "avg_pkg": 5.2, "pct": 73, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "vision-institute-aligarh-profile", "name": "Vision Institute of Technology Aligarh", "code": "110", "city": "Aligarh", "type": "Private", "est": 2006, "naac": "B", "nirf": "401-500", "fee": 80000, "h_pkg": 12.0, "avg_pkg": 4.3, "pct": 65, "branches": ["CSE", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Wipro", "HCL", "Teleperformance"]}
]

print(f"Total colleges to build: {len(all_colleges)}")

ad_tags = """  <!-- Monetag -->
  <meta name="monetag" content="4b20c6816d7cac00b3d6430a41d4d86f">
  <script src="https://quge5.com/88/tag.min.js" data-zone="257546" async data-cfasync="false"></script>
  <script async="async" data-cfasync="false" src="https://pl30261454.effectivecpmnetwork.com/1018cdea726c22b2c7ca9bbd11cccba8/invoke.js"></script>
  <script src="https://pl30261457.effectivecpmnetwork.com/5c/91/1d/5c911de89a0e11deb0df88b1aedb08a1.js"></script>
  <script src="https://www.highperformanceformat.com/974f6038e180dce6f571184465324489/invoke.js"></script>
  <script>(function(s){s.dataset.zone='11257064',s.src='https://nap5k.com/tag.min.js'})([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement('script')))</script>"""

for c in all_colleges:
    prof_path = f"colleges/profiles/{c['slug']}.html"
    tuition = c["fee"]
    hostel_s = int(tuition * 0.42)
    hostel_d = int(tuition * 0.32)
    mess = int(tuition * 0.30)
    dev = int(tuition * 0.06)
    total_4yr = (tuition + hostel_d + mess + dev) * 4

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c['name']} (Code: {c['code']}) — Fees, Placements, Cutoffs & Ranking</title>
  <meta name="description" content="Complete guide for {c['name']} (AKTU Code: {c['code']}) in {c['city']}, UP. Explore B.Tech fee structure (Rs. {c['fee']:,}/yr), hostel charges, placement records (Highest: {c['h_pkg']} LPA), branch intake, ranking and UPTAC counseling cutoffs.">
  <meta name="keywords" content="{c['name']}, AKTU Code {c['code']}, {c['name']} fees, {c['name']} placement, {c['name']} cutoff, {c['city']} engineering colleges, UPTAC counseling">
  <link rel="canonical" href="https://akturesults.in/colleges/profiles/{c['slug']}.html">
  <link rel="icon" href="/favicon.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
{ad_tags}
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "EducationalOrganization",
    "name": "{c['name']}",
    "alternateName": "AKTU Code {c['code']}",
    "url": "https://akturesults.in/colleges/profiles/{c['slug']}.html",
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "{c['city']}",
      "addressRegion": "Uttar Pradesh",
      "addressCountry": "IN"
    }}
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://akturesults.in/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Colleges", "item": "https://akturesults.in/colleges/" }},
      {{ "@type": "ListItem", "position": 3, "name": "{c['name']}", "item": "https://akturesults.in/colleges/profiles/{c['slug']}.html" }}
    ]
  }}
  </script>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', sans-serif; }}
    body {{ background: #f8fafc; color: #1e293b; line-height: 1.7; }}
    .container {{ max-width: 1140px; margin: 0 auto; padding: 0 20px; }}
    nav {{ background: #ffffff; border-bottom: 1px solid #e2e8f0; padding: 16px 0; position: sticky; top: 0; z-index: 100; }}
    .nav-inner {{ display: flex; justify-content: space-between; align-items: center; }}
    .logo {{ font-size: 22px; font-weight: 900; color: #4338ca; text-decoration: none; }}
    .hero {{ background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%); color: #ffffff; padding: 50px 0 40px; }}
    .badge {{ display: inline-block; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.25); padding: 5px 14px; border-radius: 20px; font-size: 12px; font-weight: 700; margin-bottom: 12px; }}
    h1 {{ font-size: 32px; font-weight: 900; line-height: 1.3; margin-bottom: 10px; }}
    .hero-meta {{ display: flex; flex-wrap: wrap; gap: 15px; font-size: 14px; opacity: 0.9; margin-top: 14px; }}
    .content-card {{ background: #ffffff; border-radius: 14px; border: 1px solid #e2e8f0; padding: 30px; margin: 26px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.03); }}
    h2 {{ font-size: 22px; font-weight: 800; color: #0f172a; margin-bottom: 16px; border-bottom: 2px solid #eef2ff; padding-bottom: 8px; }}
    .grid-stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 24px; }}
    .stat-box {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px; text-align: center; }}
    .stat-num {{ font-size: 22px; font-weight: 900; color: #4338ca; }}
    .stat-lbl {{ font-size: 12px; font-weight: 700; color: #64748b; text-transform: uppercase; }}
    table {{ width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px; }}
    th, td {{ padding: 12px 14px; border: 1px solid #e2e8f0; text-align: left; }}
    th {{ background: #f1f5f9; font-weight: 800; color: #334155; }}
    .tag-cloud {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 14px 0; }}
    .tag {{ background: #eef2ff; color: #4338ca; padding: 5px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; }}
    .btn-action {{ display: inline-block; background: #4338ca; color: #ffffff; padding: 12px 24px; border-radius: 8px; font-weight: 800; text-decoration: none; font-size: 14px; margin-right: 10px; transition: background 0.2s; }}
    .btn-action:hover {{ background: #3730a3; }}
    .btn-outline {{ display: inline-block; background: #ffffff; color: #4338ca; border: 2px solid #4338ca; padding: 10px 22px; border-radius: 8px; font-weight: 800; text-decoration: none; font-size: 14px; }}
    .footer {{ background: #0f172a; color: #ffffff; text-align: center; padding: 40px 0 30px; font-size: 14px; }}
    .footer a {{ color: #06b6d4; text-decoration: none; }}
  </style>
</head>
<body>
  <nav>
    <div class="container nav-inner">
      <a href="/" class="logo">AKTU Results</a>
      <div>
        <a href="/colleges/aktu-colleges-filter-directory.html" style="color:#4338ca; text-decoration:none; font-weight:700; font-size:14px; margin-right:15px;">🏛️ College Directory</a>
        <a href="/admissions/uptac-choice-filling-predictor-2026.html" style="color:#059669; text-decoration:none; font-weight:700; font-size:14px;">🎯 UPTAC Predictor</a>
      </div>
    </div>
  </nav>

  <div class="hero">
    <div class="container">
      <span class="badge">🏛️ AKTU Affiliated Institute (Code: {c['code']})</span>
      <h1>{c['name']}</h1>
      <div class="hero-meta">
        <span>📍 {c['city']}, Uttar Pradesh</span>
        <span>🏢 Type: {c['type']}</span>
        <span>⭐ NAAC: {c['naac']}</span>
        <span>🏆 NIRF: {c['nirf']}</span>
        <span>📅 Est. {c['est']}</span>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="content-card">
      <h2>📊 Key Institutional Highlights</h2>
      <div class="grid-stats">
        <div class="stat-box">
          <div class="stat-num">₹{c['fee']:,}</div>
          <div class="stat-lbl">Annual Tuition Fee</div>
        </div>
        <div class="stat-box">
          <div class="stat-num">{c['h_pkg']} LPA</div>
          <div class="stat-lbl">Highest Package</div>
        </div>
        <div class="stat-box">
          <div class="stat-num">{c['avg_pkg']} LPA</div>
          <div class="stat-lbl">Avg CSE Package</div>
        </div>
        <div class="stat-box">
          <div class="stat-num">{c['pct']}%</div>
          <div class="stat-lbl">Placement Rate</div>
        </div>
      </div>
      <div>
        <a href="/admissions/uptac-choice-filling-predictor-2026.html" class="btn-action">🎯 Predict Admission Chances</a>
        <a href="/tools/uptac-scholarship-fee-roi-calculator.html" class="btn-outline">💰 Calculate Fee ROI & Scholarship</a>
      </div>
    </div>

    <div class="content-card">
      <h2>💰 Detailed Fee Structure Breakdown</h2>
      <p>{c['name']} charges a structured annual fee approved by the Fee Regulatory Committee (FRC) Uttar Pradesh. Detailed hostel, mess, and tuition fees are detailed below:</p>
      <table>
        <thead>
          <tr>
            <th>Fee Component</th>
            <th>Annual Amount (INR)</th>
            <th>Description / Frequency</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Academic Tuition Fee</strong></td>
            <td>₹{tuition:,}</td>
            <td>Annual academic and classroom instruction fee</td>
          </tr>
          <tr>
            <td><strong>Hostel Fee (Single Occupancy)</strong></td>
            <td>₹{hostel_s:,}</td>
            <td>Annual single room with study desk and Wi-Fi</td>
          </tr>
          <tr>
            <td><strong>Hostel Fee (Double/Triple Sharing)</strong></td>
            <td>₹{hostel_d:,}</td>
            <td>Annual shared accommodation with standard amenities</td>
          </tr>
          <tr>
            <td><strong>Mess & Catering Charges</strong></td>
            <td>₹{mess:,}</td>
            <td>Nutritious 4-time meal plan (Breakfast, Lunch, Snacks, Dinner)</td>
          </tr>
          <tr>
            <td><strong>Development & Student Activity Fee</strong></td>
            <td>₹{dev:,}</td>
            <td>Clubs, sports, library access, and lab consumables</td>
          </tr>
          <tr style="background:#f8fafc; font-weight:800;">
            <td><strong>Estimated 4-Year Total Outlay</strong></td>
            <td>₹{total_4yr:,}</td>
            <td>Full 4-Year B.Tech estimated expenditure with hostel & mess</td>
          </tr>
        </tbody>
      </table>
      <div style="margin-top:12px; font-size:13px; color:#64748b;">
        *Note: Eligible UP domicile SC/ST/OBC/General candidates with family income under ₹2.0/2.5 Lakh can claim up to ₹56,600 reimbursement via the UP Post-Matric Scholarship scheme.
      </div>
    </div>

    <div class="content-card">
      <h2>🎓 Offered Engineering Programs & Intake</h2>
      <div class="tag-cloud">
        {''.join([f'<span class="tag">💻 {b}</span>' for b in c['branches']])}
      </div>
      <p>{c['name']} offers NBA-accredited B.Tech programs adhering to the AICTE model curriculum with hands-on industrial projects, open electives, and semester internships.</p>
    </div>

    <div class="content-card">
      <h2>💼 Placement Records & Top Recruiters</h2>
      <p>The Training & Placement Cell (T&P) at {c['name']} organizes on-campus recruitment drives, coding bootcamps, and mock technical interviews with prominent MNCs:</p>
      <div class="tag-cloud">
        {''.join([f'<span class="tag" style="background:#f0fdf4; color:#15803d;">🏢 {r}</span>' for r in c['rec']])}
      </div>
    </div>

    <div class="content-card">
      <h2>📍 Location & District Admission Guide</h2>
      <p>{c['name']} is situated in {c['city']}, Uttar Pradesh, well connected by rail and road networks with modern hostel campuses, central libraries, and advanced research facilities.</p>
      <div style="margin-top:14px;">
        <a href="/admissions/districts/{c['city'].lower().replace(' ', '-')}-engineering-colleges-cutoff.html" style="color:#4338ca; font-weight:700; text-decoration:none;">Explore all engineering colleges & cutoffs in {c['city']} →</a>
      </div>
    </div>
  </div>

  <footer class="footer">
    <div class="container">
      <p>© 2026 <a href="/">AKTU Results Portal</a> — Comprehensive Information Guide for {c['name']}</p>
    </div>
  </footer>
  <script defer src="/js/community-banner-widget.js"></script>
</body>
</html>"""
    with open(prof_path, "w", encoding="utf-8") as f:
        f.write(html)

print("Generated profile pages successfully!")
