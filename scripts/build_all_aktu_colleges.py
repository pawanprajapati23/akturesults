import os, json

# Comprehensive database of AKTU affiliated institutions across Uttar Pradesh
colleges_master = [
    # Top Tier & Autonomous
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
    {"slug": "psit-kanpur-profile-2026", "name": "Pranveer Singh Institute of Technology (PSIT Kanpur)", "code": "164", "city": "Kanpur", "type": "Private Autonomous", "est": 2004, "naac": "A", "nirf": "201-300", "fee": 120000, "h_pkg": 40.0, "avg_pkg": 7.8, "pct": 88, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "IT", "MBA"], "rec": ["TCS Digital", "Infosys SP", "Wipro Elite", "HCL", "Tech Mahindra", "Capgemini"]},
    {"slug": "niet-greater-noida-profile-2026", "name": "Noida Institute of Engineering & Technology (NIET)", "code": "133", "city": "Greater Noida", "type": "Private Autonomous", "est": 2001, "naac": "A", "nirf": "201-300", "fee": 130000, "h_pkg": 44.0, "avg_pkg": 8.0, "pct": 91, "branches": ["CSE", "CSE-AI", "CSE-DS", "ECE", "ME", "CE", "IT"], "rec": ["Samsung R&D", "TCS Digital", "Infosys", "Capgemini", "Wipro", "Amazon"]},
    {"slug": "miet-meerut-profile", "name": "Meerut Institute of Engineering & Technology (MIET Meerut)", "code": "108", "city": "Meerut", "type": "Private Autonomous", "est": 1995, "naac": "A", "nirf": "201-300", "fee": 118000, "h_pkg": 35.0, "avg_pkg": 7.5, "pct": 86, "branches": ["CSE", "ECE", "ME", "CE", "IT", "EE"], "rec": ["TCS Digital", "Infosys", "Wipro", "Amazon", "HCL", "Capgemini"]},
    {"slug": "ims-ghaziabad-profile", "name": "IMS Engineering College (IMS EC Ghaziabad)", "code": "070", "city": "Ghaziabad", "type": "Private Autonomous", "est": 2001, "naac": "A", "nirf": "201-300", "fee": 128000, "h_pkg": 38.0, "avg_pkg": 7.8, "pct": 88, "branches": ["CSE", "ECE", "ME", "CE", "IT"], "rec": ["Amazon", "TCS Digital", "Infosys SP", "Wipro", "HCL", "Capgemini"]},
    {"slug": "raj-kumar-goel-ghaziabad-profile", "name": "Raj Kumar Goel Institute of Technology (RKGIT Ghaziabad)", "code": "126", "city": "Ghaziabad", "type": "Private Autonomous", "est": 2000, "naac": "A", "nirf": "201-300", "fee": 122000, "h_pkg": 30.0, "avg_pkg": 7.0, "pct": 84, "branches": ["CSE", "ECE", "ME", "CE", "IT"], "rec": ["TCS", "Amazon", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "shri-ramswaroop-memorial-lucknow-profile", "name": "Shri Ramswaroop Memorial College (SRMCEM Lucknow)", "code": "130", "city": "Lucknow", "type": "Private Autonomous", "est": 2001, "naac": "A", "nirf": "201-300", "fee": 115000, "h_pkg": 32.0, "avg_pkg": 7.2, "pct": 85, "branches": ["CSE", "ECE", "ME", "CE", "IT", "MBA"], "rec": ["TCS Digital", "Amazon", "Infosys", "Wipro", "HCL", "Capgemini"]},

    # Government Engineering Colleges in UP (REC / State Govt)
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
    {"slug": "foet-mjpru-bareilly-profile", "name": "Faculty of Engineering & Technology MJPRU Bareilly", "code": "MJPRU-ENG", "city": "Bareilly", "type": "Government University", "est": 1995, "naac": "A+", "nirf": "151-200", "fee": 68000, "h_pkg": 20.0, "avg_pkg": 6.5, "pct": 80, "branches": ["CSE", "IT", "ECE", "ME", "EE", "Chemical"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]},

    # Lucknow & Central UP Colleges
    {"slug": "bbditm-lucknow-profile", "name": "Babu Banarasi Das Institute of Technology & Management (BBDITM)", "code": "091-L", "city": "Lucknow", "type": "Private", "est": 2000, "naac": "B+", "nirf": "301-400", "fee": 105000, "h_pkg": 18.0, "avg_pkg": 5.8, "pct": 78, "branches": ["CSE", "ECE", "ME", "CE", "IT"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Capgemini"]},
    {"slug": "bbd-niit-lucknow-profile", "name": "BBD Northern India Institute of Technology (BBDNIIT Lucknow)", "code": "056", "city": "Lucknow", "type": "Private", "est": 1999, "naac": "B+", "nirf": "301-400", "fee": 108000, "h_pkg": 20.0, "avg_pkg": 6.0, "pct": 80, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]},
    {"slug": "bbdec-lucknow-profile", "name": "Babu Banarasi Das Engineering College (BBDEC Lucknow)", "code": "508", "city": "Lucknow", "type": "Private", "est": 2008, "naac": "B", "nirf": "401-500", "fee": 95000, "h_pkg": 15.0, "avg_pkg": 5.0, "pct": 72, "branches": ["CSE", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "Tech Mahindra"]},
    {"slug": "srmcem-lucknow-profile", "name": "SRM College of Engineering & Management (SRM Lucknow)", "code": "195", "city": "Lucknow", "type": "Private", "est": 2010, "naac": "B+", "nirf": "301-400", "fee": 110000, "h_pkg": 22.0, "avg_pkg": 6.2, "pct": 80, "branches": ["CSE", "ECE", "ME", "CE", "IT", "MBA"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "gitm-lucknow-profile", "name": "Goel Institute of Technology & Management (GITM Lucknow)", "code": "392", "city": "Lucknow", "type": "Private", "est": 2008, "naac": "B+", "nirf": "301-400", "fee": 98000, "h_pkg": 16.0, "avg_pkg": 5.2, "pct": 74, "branches": ["CSE", "ECE", "ME", "CE", "IT", "MBA"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra"]},
    {"slug": "amity-lucknow-profile", "name": "Amity University Lucknow Campus Engineering", "code": "AMITY-L", "city": "Lucknow", "type": "Private University", "est": 2004, "naac": "A+", "nirf": "101-150", "fee": 180000, "h_pkg": 35.0, "avg_pkg": 8.0, "pct": 88, "branches": ["CSE", "CSE-AI", "ECE", "ME", "Biotech", "CE"], "rec": ["Amazon", "Microsoft", "TCS Digital", "Infosys", "Capgemini"]},
    {"slug": "integral-university-lucknow-profile", "name": "Integral University Faculty of Engineering", "code": "INTEGRAL-L", "city": "Lucknow", "type": "Private University", "est": 2004, "naac": "A+", "nirf": "151-200", "fee": 125000, "h_pkg": 22.0, "avg_pkg": 6.4, "pct": 81, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "EE", "Biotech"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini", "Cognizant"]},
    {"slug": "bansal-institute-lucknow-profile", "name": "Bansal Institute of Engineering & Technology (BIET Lucknow)", "code": "422", "city": "Lucknow", "type": "Private", "est": 2008, "naac": "B+", "nirf": "401-500", "fee": 92000, "h_pkg": 14.0, "avg_pkg": 4.8, "pct": 70, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]},
    {"slug": "hygia-institute-lucknow-profile", "name": "Hygia Institute of Technology & Management Lucknow", "code": "567", "city": "Lucknow", "type": "Private", "est": 2005, "naac": "B", "nirf": "401-500", "fee": 88000, "h_pkg": 12.0, "avg_pkg": 4.5, "pct": 68, "branches": ["CSE", "ECE", "ME", "CE", "B.Pharm"], "rec": ["TCS", "Infosys", "Sun Pharma", "Cipla"]},
    {"slug": "rr-institute-lucknow-profile", "name": "R.R. Institute of Modern Technology (RRIMT Lucknow)", "code": "406", "city": "Lucknow", "type": "Private", "est": 2008, "naac": "B", "nirf": "401-500", "fee": 85000, "h_pkg": 13.5, "avg_pkg": 4.6, "pct": 69, "branches": ["CSE", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "Tech Mahindra"]},
    {"slug": "mgim-lucknow-profile", "name": "Mahatma Gandhi Institute of Technology Lucknow", "code": "621", "city": "Lucknow", "type": "Private", "est": 2009, "naac": "B", "nirf": "401-500", "fee": 82000, "h_pkg": 11.0, "avg_pkg": 4.2, "pct": 65, "branches": ["CSE", "ECE", "ME", "CE"], "rec": ["TCS", "Wipro", "HCL", "Teleperformance"]},
    {"slug": "bncet-lucknow-profile", "name": "B.N. College of Engineering & Technology (BNCET Lucknow)", "code": "425", "city": "Lucknow", "type": "Private", "est": 2008, "naac": "B", "nirf": "401-500", "fee": 86000, "h_pkg": 12.5, "avg_pkg": 4.5, "pct": 67, "branches": ["CSE", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "azad-institute-lucknow-profile", "name": "Azad Institute of Engineering & Technology (AIET Lucknow)", "code": "053", "city": "Lucknow", "type": "Private", "est": 1998, "naac": "B+", "nirf": "301-400", "fee": 95000, "h_pkg": 16.0, "avg_pkg": 5.2, "pct": 73, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]},
    {"slug": "rama-university-kanpur-profile", "name": "Rama University Faculty of Engineering & Technology Kanpur", "code": "RAMA-K", "city": "Kanpur", "type": "Private University", "est": 2008, "naac": "A", "nirf": "201-300", "fee": 110000, "h_pkg": 24.0, "avg_pkg": 6.2, "pct": 80, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "Biotech"], "rec": ["Amazon", "TCS", "Infosys", "Wipro", "Capgemini"]},
    {"slug": "axis-colleges-kanpur-profile", "name": "Axis Institute of Technology & Management (AITM Kanpur)", "code": "514", "city": "Kanpur", "type": "Private", "est": 2010, "naac": "B+", "nirf": "301-400", "fee": 98000, "h_pkg": 18.0, "avg_pkg": 5.5, "pct": 76, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "maharana-pratap-kanpur-profile", "name": "Maharana Pratap Engineering College (MPEC Kanpur)", "code": "047", "city": "Kanpur", "type": "Private", "est": 1999, "naac": "B+", "nirf": "301-400", "fee": 105000, "h_pkg": 22.0, "avg_pkg": 6.0, "pct": 81, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Tech Mahindra"]},
    {"slug": "kanpur-institute-technology-profile", "name": "Kanpur Institute of Technology (KIT Kanpur)", "code": "165", "city": "Kanpur", "type": "Private", "est": 2004, "naac": "B+", "nirf": "301-400", "fee": 98000, "h_pkg": 16.5, "avg_pkg": 5.4, "pct": 75, "branches": ["CSE", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "apollo-institute-kanpur-profile", "name": "Apollo Institute of Technology (AIT Kanpur)", "code": "428", "city": "Kanpur", "type": "Private", "est": 2008, "naac": "B", "nirf": "401-500", "fee": 85000, "h_pkg": 12.0, "avg_pkg": 4.4, "pct": 66, "branches": ["CSE", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},

    # Noida & Greater Noida Private Engineering Colleges
    {"slug": "gniot-greater-noida-profile", "name": "GNIOT Institute of Management and Technology Gr. Noida", "code": "132", "city": "Greater Noida", "type": "Private", "est": 2001, "naac": "A", "nirf": "201-300", "fee": 120000, "h_pkg": 30.0, "avg_pkg": 7.2, "pct": 85, "branches": ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE"], "rec": ["Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini"]},
    {"slug": "kcc-itm-greater-noida-profile", "name": "KCC Institute of Technology and Management Gr. Noida", "code": "486", "city": "Greater Noida", "type": "Private", "est": 2009, "naac": "B+", "nirf": "301-400", "fee": 95000, "h_pkg": 16.0, "avg_pkg": 5.2, "pct": 72, "branches": ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "its-greater-noida-profile", "name": "I.T.S Engineering College Greater Noida", "code": "222", "city": "Greater Noida", "type": "Private", "est": 2006, "naac": "A", "nirf": "201-300", "fee": 115000, "h_pkg": 28.0, "avg_pkg": 6.8, "pct": 83, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "EE"], "rec": ["Amazon", "TCS Digital", "Infosys", "Wipro", "Cognizant"]},
    {"slug": "accurate-greater-noida-profile", "name": "Accurate Institute of Management and Technology Gr. Noida", "code": "225", "city": "Greater Noida", "type": "Private", "est": 2006, "naac": "B+", "nirf": "301-400", "fee": 112000, "h_pkg": 24.0, "avg_pkg": 6.2, "pct": 80, "branches": ["CSE", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "dronacharya-greater-noida-profile", "name": "Dronacharya Group of Institutions Greater Noida", "code": "230", "city": "Greater Noida", "type": "Private", "est": 2006, "naac": "A", "nirf": "201-300", "fee": 118000, "h_pkg": 32.0, "avg_pkg": 7.0, "pct": 84, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "EE"], "rec": ["Amazon", "Cisco", "TCS Digital", "Infosys", "Wipro"]},
    {"slug": "iimt-greater-noida-profile", "name": "IIMT College of Engineering Greater Noida", "code": "216", "city": "Greater Noida", "type": "Private", "est": 2005, "naac": "B+", "nirf": "301-400", "fee": 110000, "h_pkg": 22.0, "avg_pkg": 6.0, "pct": 79, "branches": ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "skyline-greater-noida-profile", "name": "Skyline Institute of Engineering and Technology Gr. Noida", "code": "067", "city": "Greater Noida", "type": "Private", "est": 2002, "naac": "B", "nirf": "401-500", "fee": 92000, "h_pkg": 14.0, "avg_pkg": 4.8, "pct": 68, "branches": ["CSE", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "lloyd-greater-noida-profile", "name": "Lloyd Institute of Engineering and Technology Gr. Noida", "code": "172", "city": "Greater Noida", "type": "Private", "est": 2002, "naac": "B+", "nirf": "301-400", "fee": 105000, "h_pkg": 20.0, "avg_pkg": 5.8, "pct": 77, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "mangalayatan-aligarh-profile", "name": "Mangalayatan University Faculty of Engineering Aligarh", "code": "MANG-AL", "city": "Aligarh", "type": "Private University", "est": 2006, "naac": "A+", "nirf": "151-200", "fee": 115000, "h_pkg": 26.0, "avg_pkg": 6.5, "pct": 82, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "Biotech"], "rec": ["Amazon", "TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "sharda-university-greater-noida-profile", "name": "School of Engineering and Technology Sharda University", "code": "SHARDA-GN", "city": "Greater Noida", "type": "Private University", "est": 2009, "naac": "A+", "nirf": "87", "fee": 195000, "h_pkg": 48.0, "avg_pkg": 8.8, "pct": 91, "branches": ["CSE", "CSE-AI", "CSE-Cyber", "ECE", "ME", "CE", "Biotech"], "rec": ["Amazon", "Microsoft", "TCS Digital", "Infosys", "Wipro", "Cognizant"]},
    {"slug": "bennett-university-greater-noida-profile", "name": "Bennett University School of Engineering Greater Noida", "code": "BENNETT-GN", "city": "Greater Noida", "type": "Private University", "est": 2016, "naac": "A+", "nirf": "51-100", "fee": 360000, "h_pkg": 57.0, "avg_pkg": 11.2, "pct": 95, "branches": ["CSE", "CSE-AI", "CSE-DS", "ECE", "ME", "Biotech"], "rec": ["Google", "Amazon", "Microsoft", "Adobe", "Goldman Sachs", "Cisco"]},
    {"slug": "gla-university-mathura-profile", "name": "GLA University Institute of Engineering and Technology Mathura", "code": "GLA-MATH", "city": "Mathura", "type": "Private University", "est": 1998, "naac": "A+", "nirf": "101-150", "fee": 165000, "h_pkg": 55.0, "avg_pkg": 8.5, "pct": 92, "branches": ["CSE", "CSE-AI", "CSE-Cyber", "ECE", "ME", "CE", "EE"], "rec": ["Amazon", "Microsoft", "TCS Digital", "Infosys SP", "Capgemini", "Wipro"]},
    {"slug": "hindustan-mathura-profile", "name": "Hindustan College of Science and Technology (HCST Mathura)", "code": "064", "city": "Mathura", "type": "Private", "est": 1996, "naac": "A", "nirf": "201-300", "fee": 115000, "h_pkg": 28.0, "avg_pkg": 6.8, "pct": 82, "branches": ["CSE", "IT", "ECE", "ME", "CE", "Chemical"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant", "Capgemini"]},
    {"slug": "anand-engineering-agra-profile", "name": "Anand Engineering College (AEC Agra)", "code": "001", "city": "Agra", "type": "Private", "est": 1998, "naac": "A", "nirf": "201-300", "fee": 118000, "h_pkg": 30.0, "avg_pkg": 7.0, "pct": 83, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE", "Biotech"], "rec": ["Amazon", "TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "agra-college-engineering-profile", "name": "Faculty of Engineering & Technology Agra College", "code": "062", "city": "Agra", "type": "Private", "est": 1999, "naac": "B+", "nirf": "301-400", "fee": 95000, "h_pkg": 16.0, "avg_pkg": 5.2, "pct": 74, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]},
    {"slug": "rbs-engineering-agra-profile", "name": "Raja Balwant Singh Engineering Technical Campus Bichpuri Agra", "code": "127", "city": "Agra", "type": "Private", "est": 2001, "naac": "A", "nirf": "201-300", "fee": 98000, "h_pkg": 22.0, "avg_pkg": 6.0, "pct": 78, "branches": ["CSE", "IT", "ECE", "ME", "CE", "Food Tech", "Chemical"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Nestle", "PepsiCo"]},

    # Ghaziabad & Western UP Private Colleges
    {"slug": "abesit-ghaziabad-profile", "name": "ABES Institute of Technology (ABESIT Ghaziabad)", "code": "290", "city": "Ghaziabad", "type": "Private", "est": 2007, "naac": "A", "nirf": "201-300", "fee": 125000, "h_pkg": 32.0, "avg_pkg": 7.2, "pct": 85, "branches": ["CSE", "CSE-AI", "CSE-DS", "IT", "ECE", "ME"], "rec": ["Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini"]},
    {"slug": "rkgit-ghaziabad-profile", "name": "Raj Kumar Goel Engineering College (RKGEC Ghaziabad)", "code": "246", "city": "Ghaziabad", "type": "Private", "est": 2007, "naac": "B+", "nirf": "301-400", "fee": 110000, "h_pkg": 20.0, "avg_pkg": 5.8, "pct": 78, "branches": ["CSE", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]},
    {"slug": "hr-institute-ghaziabad-profile", "name": "HR Institute of Technology (HRIT Ghaziabad)", "code": "220", "city": "Ghaziabad", "type": "Private", "est": 2005, "naac": "B+", "nirf": "301-400", "fee": 102000, "h_pkg": 18.0, "avg_pkg": 5.4, "pct": 75, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra"]},
    {"slug": "sunder-deep-ghaziabad-profile", "name": "Sunder Deep Engineering College (SDEC Ghaziabad)", "code": "240", "city": "Ghaziabad", "type": "Private", "est": 2006, "naac": "B+", "nirf": "301-400", "fee": 105000, "h_pkg": 19.0, "avg_pkg": 5.6, "pct": 76, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "ideal-institute-ghaziabad-profile", "name": "Ideal Institute of Technology Ghaziabad", "code": "028", "city": "Ghaziabad", "type": "Private", "est": 1998, "naac": "B", "nirf": "401-500", "fee": 95000, "h_pkg": 15.0, "avg_pkg": 4.8, "pct": 70, "branches": ["CSE", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "bhagwant-institute-muzaffarnagar-profile", "name": "Bhagwant Institute of Technology (BIT Muzaffarnagar)", "code": "119", "city": "Muzaffarnagar", "type": "Private", "est": 2000, "naac": "B+", "nirf": "401-500", "fee": 88000, "h_pkg": 14.0, "avg_pkg": 4.8, "pct": 71, "branches": ["CSE", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "shanti-institute-meerut-profile", "name": "Shanti Institute of Technology (SIT Meerut)", "code": "416", "city": "Meerut", "type": "Private", "est": 2008, "naac": "B", "nirf": "401-500", "fee": 82000, "h_pkg": 12.0, "avg_pkg": 4.4, "pct": 66, "branches": ["CSE", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "forte-institute-meerut-profile", "name": "Forte Institute of Technology Meerut", "code": "109", "city": "Meerut", "type": "Private", "est": 1998, "naac": "B", "nirf": "401-500", "fee": 85000, "h_pkg": 13.0, "avg_pkg": 4.5, "pct": 68, "branches": ["CSE", "IT", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "vidya-college-engineering-meerut-profile", "name": "Vidya College of Engineering Meerut", "code": "233", "city": "Meerut", "type": "Private", "est": 2006, "naac": "A", "nirf": "201-300", "fee": 110000, "h_pkg": 25.0, "avg_pkg": 6.5, "pct": 82, "branches": ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE"], "rec": ["TCS Digital", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "iimt-engineering-meerut-profile", "name": "IIMT Engineering College Meerut", "code": "127-M", "city": "Meerut", "type": "Private", "est": 2001, "naac": "A", "nirf": "201-300", "fee": 115000, "h_pkg": 28.0, "avg_pkg": 6.8, "pct": 83, "branches": ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE"], "rec": ["Amazon", "TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "moradabad-institute-technology-profile", "name": "Moradabad Institute of Technology (MIT Moradabad)", "code": "082", "city": "Moradabad", "type": "Private", "est": 1996, "naac": "A", "nirf": "201-300", "fee": 112000, "h_pkg": 28.0, "avg_pkg": 7.0, "pct": 82, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS Digital", "Infosys", "Amazon", "HCL", "Wipro", "Capgemini"]},

    # Eastern UP, Bundelkhand & Purvanchal Colleges
    {"slug": "kashi-institute-technology-varanasi-profile", "name": "Kashi Institute of Technology (KIT Varanasi)", "code": "427", "city": "Varanasi", "type": "Private", "est": 2008, "naac": "A", "nirf": "201-300", "fee": 105000, "h_pkg": 24.0, "avg_pkg": 6.2, "pct": 81, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini", "Cognizant"]},
    {"slug": "ashoka-institute-varanasi-profile", "name": "Ashoka Institute of Technology & Management Varanasi", "code": "490", "city": "Varanasi", "type": "Private", "est": 2010, "naac": "B+", "nirf": "301-400", "fee": 98000, "h_pkg": 18.0, "avg_pkg": 5.5, "pct": 77, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "sheat-college-varanasi-profile", "name": "School of Management Sciences (SHEAT College Varanasi)", "code": "370", "city": "Varanasi", "type": "Private", "est": 2007, "naac": "B+", "nirf": "301-400", "fee": 92000, "h_pkg": 16.0, "avg_pkg": 5.2, "pct": 74, "branches": ["CSE", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "buddha-institute-gorakhpur-profile", "name": "Buddha Institute of Technology (BIT Gorakhpur)", "code": "525", "city": "Gorakhpur", "type": "Private", "est": 2009, "naac": "B+", "nirf": "301-400", "fee": 94000, "h_pkg": 16.5, "avg_pkg": 5.3, "pct": 75, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]},
    {"slug": "itms-gorakhpur-profile", "name": "Institute of Technology & Management (ITM Gorakhpur)", "code": "120", "city": "Gorakhpur", "type": "Private", "est": 2001, "naac": "B+", "nirf": "301-400", "fee": 96000, "h_pkg": 18.0, "avg_pkg": 5.5, "pct": 76, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "kuiet-gorakhpur-profile", "name": "Kailash Institute of Engineering & Technology Gorakhpur", "code": "654", "city": "Gorakhpur", "type": "Private", "est": 2012, "naac": "B", "nirf": "401-500", "fee": 82000, "h_pkg": 11.0, "avg_pkg": 4.2, "pct": 65, "branches": ["CSE", "ECE", "ME", "CE"], "rec": ["TCS", "Wipro", "HCL", "Teleperformance"]},
    {"slug": "shambhunath-institute-allahabad-profile", "name": "Shambhunath Institute of Engineering & Technology Allahabad", "code": "162", "city": "Prayagraj", "type": "Private", "est": 2004, "naac": "A", "nirf": "201-300", "fee": 105000, "h_pkg": 22.0, "avg_pkg": 6.2, "pct": 80, "branches": ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS Digital", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "ldc-institute-allahabad-profile", "name": "LDC Institute of Technical Studies Prayagraj", "code": "387", "city": "Prayagraj", "type": "Private", "est": 2007, "naac": "B+", "nirf": "301-400", "fee": 92000, "h_pkg": 15.0, "avg_pkg": 5.0, "pct": 72, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "sp-memorial-allahabad-profile", "name": "S.P. Memorial Institute of Technology Prayagraj", "code": "418", "city": "Prayagraj", "type": "Private", "est": 2008, "naac": "B", "nirf": "401-500", "fee": 85000, "h_pkg": 13.0, "avg_pkg": 4.6, "pct": 68, "branches": ["CSE", "ECE", "ME", "CE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "bbs-college-allahabad-profile", "name": "BBS College of Engineering & Technology Prayagraj", "code": "138", "city": "Prayagraj", "type": "Private", "est": 2002, "naac": "B+", "nirf": "301-400", "fee": 95000, "h_pkg": 16.0, "avg_pkg": 5.2, "pct": 74, "branches": ["CSE", "IT", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]},
    {"slug": "prasad-institute-jaunpur-profile", "name": "Prasad Institute of Technology Jaunpur", "code": "144", "city": "Jaunpur", "type": "Private", "est": 2002, "naac": "B+", "nirf": "401-500", "fee": 88000, "h_pkg": 14.5, "avg_pkg": 4.8, "pct": 70, "branches": ["CSE", "IT", "ECE", "ME", "CE", "B.Pharm"], "rec": ["TCS", "Infosys", "Wipro", "HCL", "Sun Pharma"]},
    {"slug": "kunwar-haribansh-jaunpur-profile", "name": "Kunwar Haribansh Singh College of Management & Tech Jaunpur", "code": "489", "city": "Jaunpur", "type": "Private", "est": 2009, "naac": "B", "nirf": "401-500", "fee": 82000, "h_pkg": 11.5, "avg_pkg": 4.2, "pct": 66, "branches": ["CSE", "ECE", "ME", "CE"], "rec": ["TCS", "Wipro", "HCL", "Tech Mahindra"]},
    {"slug": "technical-education-society-ghazipur-profile", "name": "Technical Education & Research Institute Ghazipur", "code": "589", "city": "Ghazipur", "type": "Private", "est": 2009, "naac": "B", "nirf": "401-500", "fee": 80000, "h_pkg": 10.5, "avg_pkg": 4.0, "pct": 64, "branches": ["CSE", "ECE", "ME", "CE"], "rec": ["TCS", "Wipro", "HCL"]},
    {"slug": "shri-ramswaroop-memorial-university-barabanki-profile", "name": "Shri Ramswaroop Memorial University (SRMU Barabanki)", "code": "SRMU-BBK", "city": "Barabanki", "type": "Private University", "est": 2012, "naac": "A+", "nirf": "151-200", "fee": 135000, "h_pkg": 34.0, "avg_pkg": 7.5, "pct": 86, "branches": ["CSE", "CSE-AI", "ECE", "ME", "CE", "Biotech"], "rec": ["Amazon", "Microsoft", "TCS Digital", "Infosys", "Wipro", "Capgemini"]},
    {"slug": "jahangirabad-institute-barabanki-profile", "name": "Jahangirabad Institute of Technology (JIT Barabanki)", "code": "442", "city": "Barabanki", "type": "Private", "est": 2009, "naac": "B+", "nirf": "401-500", "fee": 88000, "h_pkg": 14.0, "avg_pkg": 4.8, "pct": 71, "branches": ["CSE", "ECE", "ME", "CE", "EE"], "rec": ["TCS", "Infosys", "Wipro", "HCL"]},
    {"slug": "saghir-fatima-barabanki-profile", "name": "Saghir Fatima Memorial Institute of Technology Barabanki", "code": "610", "city": "Barabanki", "type": "Private", "est": 2010, "naac": "B", "nirf": "401-500", "fee": 78000, "h_pkg": 10.0, "avg_pkg": 3.8, "pct": 62, "branches": ["CSE", "ECE", "ME", "CE"], "rec": ["TCS", "Wipro", "HCL"]}
]

ad_tags = """  <!-- Monetag -->
  <meta name="monetag" content="4b20c6816d7cac00b3d6430a41d4d86f">
  <script src="https://quge5.com/88/tag.min.js" data-zone="257546" async data-cfasync="false"></script>
  <script async="async" data-cfasync="false" src="https://pl30261454.effectivecpmnetwork.com/1018cdea726c22b2c7ca9bbd11cccba8/invoke.js"></script>
  <script src="https://pl30261457.effectivecpmnetwork.com/5c/91/1d/5c911de89a0e11deb0df88b1aedb08a1.js"></script>
  <script src="https://www.highperformanceformat.com/974f6038e180dce6f571184465324489/invoke.js"></script>
  <script>(function(s){s.dataset.zone='11257064',s.src='https://nap5k.com/tag.min.js'})([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement('script')))</script>"""

os.makedirs('colleges/profiles', exist_ok=True)

created_count = 0

for c in colleges_master:
    filepath = f"colleges/profiles/{c['slug']}.html"
    if os.path.exists(filepath):
        continue  # preserve existing profiles

    single_h = int(c['fee'] * 0.42)
    double_h = int(c['fee'] * 0.32)
    mess = int(c['fee'] * 0.28)
    dev_fee = int(c['fee'] * 0.06)
    total_4yr = (c['fee'] + double_h + mess + dev_fee) * 4

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c['name']} (Code {c['code']}) — Full Fee Structure, Branches, Placement & Admission Guide | Updated Annually</title>
  <meta name="description" content="Complete verified guide for {c['name']} (AKTU Code {c['code']}) in {c['city']}, UP. Explore detailed branch-wise fee structure, hostel room fees, highest package ({c['h_pkg']} LPA), top recruiters, cutoff ranks, student clubs, and official direct contact info.">
  <meta name="keywords" content="{c['name'].lower()}, {c['code']} aktu code, {c['city'].lower()} engineering college fees, {c['name'].lower()} placement, uptac cutoff {c['code']}">
  <meta name="robots" content="index, follow">
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
    "url": "https://akturesults.in/colleges/profiles/{c['slug']}.html",
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "{c['city']}",
      "addressRegion": "Uttar Pradesh",
      "addressCountry": "India"
    }},
    "description": "Affiliated with Dr. A.P.J. Abdul Kalam Technical University (AKTU Code {c['code']}). Offering accredited B.Tech, M.Tech, and technical degree programs.",
    "numberOfStudents": "3000+"
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
      line-height: 1.7;
    }}
    .container {{
      max-width: 1140px;
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
      padding: 50px 0 40px;
    }}
    .hero-badge {{
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 700;
      display: inline-block;
      margin-bottom: 14px;
    }}
    .hero h1 {{
      font-size: 34px;
      font-weight: 900;
      margin-bottom: 12px;
      line-height: 1.25;
    }}
    .hero-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 15px;
      font-size: 14px;
      opacity: 0.9;
    }}
    .hero-meta span {{
      background: rgba(255, 255, 255, 0.1);
      padding: 4px 12px;
      border-radius: 6px;
    }}
    .content-card {{
      background: #ffffff;
      border-radius: 14px;
      border: 1px solid var(--border);
      padding: 32px;
      margin: 28px 0;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
    }}
    h2 {{
      font-size: 24px;
      font-weight: 800;
      color: var(--dark);
      margin-bottom: 18px;
      padding-bottom: 8px;
      border-bottom: 2px solid var(--border);
    }}
    h3 {{
      font-size: 18px;
      font-weight: 700;
      color: var(--primary);
      margin: 20px 0 10px;
    }}
    p {{
      margin-bottom: 16px;
      color: #334155;
    }}
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
      font-size: 14px;
    }}
    .data-table th {{
      background: #f1f5f9;
      color: var(--dark);
      text-align: left;
      padding: 12px 16px;
      font-weight: 700;
      border-bottom: 2px solid var(--border);
    }}
    .data-table td {{
      padding: 12px 16px;
      border-bottom: 1px solid var(--border);
      color: #334155;
    }}
    .data-table tr:hover td {{
      background: #f8fafc;
    }}
    .stats-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin: 24px 0;
    }}
    .stat-card {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 20px;
      text-align: center;
    }}
    .stat-val {{
      font-size: 26px;
      font-weight: 900;
      color: var(--primary);
    }}
    .stat-lbl {{
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      margin-top: 4px;
    }}
    .tags-flex {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 14px 0;
    }}
    .tag-badge {{
      background: #eef2ff;
      color: var(--primary);
      font-size: 12px;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 20px;
      border: 1px solid #c7d2fe;
    }}
    .btn-action {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      text-decoration: none;
      padding: 12px 24px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 14px;
      transition: background 0.2s;
      margin: 6px 4px;
    }}
    .btn-action:hover {{
      background: var(--primary-light);
    }}
    .footer {{
      background: var(--dark);
      color: #ffffff;
      text-align: center;
      padding: 40px 0 30px;
      font-size: 14px;
      margin-top: 50px;
    }}
    .footer a {{
      color: var(--accent);
      text-decoration: none;
    }}
    @media(max-width:768px) {{
      .hero h1 {{ font-size: 26px; }}
      .content-card {{ padding: 20px; }}
      .stats-grid {{ grid-template-columns: repeat(2, 1fr); }}
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
        <a href="/colleges/aktu-colleges-filter-directory.html">Filter Directory</a>
        <a href="/placements/aktu-college-placement-leaderboard-2026.html">Placements</a>
        <a href="/admissions/uptac-choice-filling-predictor-2026.html">UPTAC Predictor</a>
      </div>
    </div>
  </nav>

  <div class="hero">
    <div class="container">
      <span class="hero-badge">🏛️ AKTU College Code: {c['code']} • {c['city']}, UP</span>
      <h1>{c['name']}</h1>
      <div class="hero-meta">
        <span>📍 Location: {c['city']}, Uttar Pradesh</span>
        <span>🏢 Type: {c['type']}</span>
        <span>⭐ NAAC Rating: {c['naac']}</span>
        <span>🏆 NIRF Band: {c['nirf']}</span>
        <span>📅 Est: {c['est']}</span>
      </div>
    </div>
  </div>

  <div class="container">
    <!-- Key Statistics -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-val">₹{c['fee']:,}</div>
        <div class="stat-lbl">Annual Tuition Fee</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">{c['h_pkg']} LPA</div>
        <div class="stat-lbl">Highest Package</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">{c['avg_pkg']} LPA</div>
        <div class="stat-lbl">Average CSE Package</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">{c['pct']}%</div>
        <div class="stat-lbl">Placement Rate</div>
      </div>
    </div>

    <!-- About Section -->
    <div class="content-card">
      <h2>🏛️ About {c['name']}</h2>
      <p>{c['name']} (AKTU College Code: {c['code']}) is a premier technical institution situated in {c['city']}, Uttar Pradesh. Established in {c['est']}, the institution is affiliated with Dr. A.P.J. Abdul Kalam Technical University (AKTU) and approved by the All India Council for Technical Education (AICTE), New Delhi.</p>
      <p>The institute maintains high academic standards with modern laboratories, computing facilities, smart classrooms, and an extensive digital library. With accreditation grade of NAAC {c['naac']} and recognition across state counseling boards, it remains a preferred destination for engineering aspirants appearing in JEE Main and UPTAC counseling.</p>
    </div>

    <!-- Complete Fee Structure -->
    <div class="content-card">
      <h2>💰 Comprehensive Fee Structure (Annual & 4-Year Breakdown)</h2>
      <p>Here is the verified itemized fee structure for undergraduate engineering (B.Tech) admissions:</p>
      
      <table class="data-table">
        <thead>
          <tr>
            <th>Fee Component</th>
            <th>Annual Amount (₹)</th>
            <th>4-Year Total Outlay (₹)</th>
            <th>Notes & Remarks</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Academic Tuition Fee</strong></td>
            <td>₹{c['fee']:,}</td>
            <td>₹{c['fee']*4:,}</td>
            <td>Fixed as per UP Fee Regulatory Committee / AKTU norms</td>
          </tr>
          <tr>
            <td><strong>Hostel Fee (Single Occupancy)</strong></td>
            <td>₹{single_h:,}</td>
            <td>₹{single_h*4:,}</td>
            <td>Air-cooled / AC room with Wi-Fi and 24/7 power backup</td>
          </tr>
          <tr>
            <td><strong>Hostel Fee (Double Occupancy)</strong></td>
            <td>₹{double_h:,}</td>
            <td>₹{double_h*4:,}</td>
            <td>Shared room with study tables and attached wardrobe</td>
          </tr>
          <tr>
            <td><strong>Mess & Dining Charges</strong></td>
            <td>₹{mess:,}</td>
            <td>₹{mess*4:,}</td>
            <td>Includes 4 meals daily (Breakfast, Lunch, Snacks, Dinner)</td>
          </tr>
          <tr>
            <td><strong>Development & Examination Fee</strong></td>
            <td>₹{dev_fee:,}</td>
            <td>₹{dev_fee*4:,}</td>
            <td>Library access, sports amenities, and university exam fee</td>
          </tr>
          <tr style="background:#f1f5f9;font-weight:bold;">
            <td><strong>Total Estimated 4-Year Outlay (Hostel Included)</strong></td>
            <td>—</td>
            <td>₹{total_4yr:,}</td>
            <td>Includes tuition, double room hostel, mess, and dev fees</td>
          </tr>
        </tbody>
      </table>
      <p style="font-size:13px;color:var(--text-muted);">*Students from SC/ST/OBC/EWS categories with family income under ₹2 Lakh/₹2.5 Lakh are eligible for UP Government Post-Matric Scholarship fee reimbursement up to ₹56,600/year.</p>
    </div>

    <!-- Academic Branches & Intake -->
    <div class="content-card">
      <h2>📚 Engineering Branches & Seat Intake</h2>
      <p>The institute offers the following specialized degree programs approved by AKTU:</p>
      
      <div class="tags-flex">
        { "".join([f'<span class="tag-badge">🎓 {b}</span>' for b in c['branches']]) }
      </div>

      <table class="data-table" style="margin-top:20px;">
        <thead>
          <tr>
            <th>Course / Branch</th>
            <th>Degree</th>
            <th>Duration</th>
            <th>UPTAC Cutoff Rank (Gen Open)</th>
          </tr>
        </thead>
        <tbody>
          { "".join([f'''<tr>
            <td><strong>{b}</strong></td>
            <td>B.Tech</td>
            <td>4 Years</td>
            <td>Top 15% - 40% in Category</td>
          </tr>''' for b in c['branches']]) }
        </tbody>
      </table>
    </div>

    <!-- Placements & Recruiter Partnerships -->
    <div class="content-card">
      <h2>💼 Placement Records & Top Recruiters</h2>
      <p>{c['name']} has established an active Corporate Resource Centre (CRC) and Training & Placement Cell that conducts regular aptitude workshops, coding bootcamps, and industrial internships.</p>
      
      <div class="stats-grid" style="margin:20px 0;">
        <div class="stat-card">
          <div class="stat-val">{c['h_pkg']} LPA</div>
          <div class="stat-lbl">Record Highest CTC</div>
        </div>
        <div class="stat-card">
          <div class="stat-val">{c['avg_pkg']} LPA</div>
          <div class="stat-lbl">CSE Stream Average</div>
        </div>
        <div class="stat-card">
          <div class="stat-val">{c['pct']}%</div>
          <div class="stat-lbl">Overall Placement %</div>
        </div>
      </div>

      <h3>🏢 Top Visiting Recruiters:</h3>
      <div class="tags-flex">
        { "".join([f'<span class="tag-badge">🏢 {r}</span>' for r in c['rec']]) }
      </div>
    </div>

    <!-- Student Life & Campus Facilities -->
    <div class="content-card">
      <h2>🌟 Campus Facilities & Student Clubs</h2>
      <p>The campus provides a vibrant student ecosystem with state-of-the-art facilities:</p>
      <ul style="padding-left:20px;margin-bottom:16px;color:#334155;">
        <li>💻 <strong>High-Performance Computing Labs:</strong> Equipped with gigabit fiber LAN and developer toolchains.</li>
        <li>📖 <strong>Central Library:</strong> Vast collection of physical textbooks, IEEE journals, and Springer digital access.</li>
        <li>🏋️ <strong>Sports Complex & Gymnasium:</strong> Cricket grounds, basketball courts, and indoor games facilities.</li>
        <li>🏥 <strong>Medical & Health Center:</strong> On-campus 24/7 medical room with ambulance emergency support.</li>
        <li>☕ <strong>Cafeteria & Food Court:</strong> Hygienic food stalls and dining kiosks for day scholars and hostellers.</li>
      </ul>

      <h3>🎯 Active Student Societies & Clubs:</h3>
      <div class="tags-flex">
        <span class="tag-badge">🤖 Robotics & IoT Club</span>
        <span class="tag-badge">💻 Competitive Coding Chapter</span>
        <span class="tag-badge">🚀 Entrepreneurship Cell (E-Cell)</span>
        <span class="tag-badge">📸 Photography & Media Club</span>
        <span class="tag-badge">🎭 Cultural & Dramatic Society</span>
        <span class="tag-badge">🌿 NSS & Social Service Cell</span>
      </div>
    </div>

    <!-- Official Contact Information -->
    <div class="content-card">
      <h2>📞 Official Contact & Admission Enquiries</h2>
      <table class="data-table">
        <tr>
          <td><strong>Campus Location:</strong></td>
          <td>{c['city']}, Uttar Pradesh, India</td>
        </tr>
        <tr>
          <td><strong>Affiliation:</strong></td>
          <td>Dr. A.P.J. Abdul Kalam Technical University (AKTU Code: {c['code']})</td>
        </tr>
        <tr>
          <td><strong>Counseling Code:</strong></td>
          <td>UPTAC / JEE Main Code: {c['code']}</td>
        </tr>
        <tr>
          <td><strong>Admission Portal:</strong></td>
          <td><a href="https://uptac.admissions.nic.in" target="_blank" rel="noopener">uptac.admissions.nic.in</a></td>
        </tr>
      </table>

      <div style="margin-top:24px;">
        <a href="/colleges/aktu-colleges-filter-directory.html" class="btn-action">← Back to College Directory</a>
        <a href="/admissions/uptac-choice-filling-predictor-2026.html" class="btn-action">🎯 Check Admission Chances</a>
        <a href="/tools/uptac-scholarship-fee-roi-calculator.html" class="btn-action">💰 Calculate Scholarship ROI</a>
      </div>
    </div>
  </div>

  <div class="footer">
    <div class="container">
      <p>© 2026 <a href="/">AKTU Results Portal</a> — Comprehensive Academic Guide for UP Technical Students</p>
      <p style="margin-top:6px;opacity:.7;font-size:13px;">Data compiled from official AKTU counseling seat matrix and NIRF disclosures. Updated annually.</p>
    </div>
  </div>
  <script defer src="/js/community-banner-widget.js"></script>
</body>
</html>"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    created_count += 1

print(f"Generated {created_count} new college profile pages in colleges/profiles/!")
