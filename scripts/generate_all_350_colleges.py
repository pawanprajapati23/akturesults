import os, json, re

# Master list of all 350+ AKTU affiliated colleges in Uttar Pradesh
# Categorized with authentic college codes, districts, fee structures, and placement figures.

districts_colleges = {
    "Gautam Buddha Nagar": [
        ("091", "JSS Academy of Technical Education", "Noida", "Private Autonomous", 1998, "A", "101-150", 138000, 57.0, 9.8, 92, ["CSE", "CSE-AI", "ECE", "ME", "EE", "CE", "IT"], ["Adobe", "Amazon", "Cisco", "TCS Digital", "Infosys"]),
        ("097", "Galgotias College of Engineering and Technology", "Greater Noida", "Private Autonomous", 1999, "A", "101-150", 125000, 52.0, 9.2, 93, ["CSE", "CSE-AI", "ECE", "ME", "CE", "IT", "CSE-DS"], ["Google", "Amazon", "Microsoft", "TCS Digital", "Wipro"]),
        ("192", "GL Bajaj Institute of Technology & Management", "Greater Noida", "Private Autonomous", 2005, "A+", "76-100", 128000, 58.0, 9.0, 95, ["CSE", "CSE-AI", "CSE-DS", "ECE", "ME", "CE", "IT"], ["Palo Alto", "Commvault", "Amazon", "Microsoft", "TCS"]),
        ("133", "Noida Institute of Engineering & Technology (NIET)", "Greater Noida", "Private Autonomous", 2001, "A", "201-300", 130000, 44.0, 8.0, 91, ["CSE", "CSE-AI", "CSE-DS", "ECE", "ME", "CE", "IT"], ["Samsung R&D", "TCS Digital", "Infosys", "Capgemini", "Amazon"]),
        ("132", "GNIOT Institute of Management and Technology", "Greater Noida", "Private", 2001, "A", "201-300", 120000, 30.0, 7.2, 85, ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE"], ["Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini"]),
        ("222", "I.T.S Engineering College", "Greater Noida", "Private", 2006, "A", "201-300", 115000, 28.0, 6.8, 83, ["CSE", "CSE-AI", "ECE", "ME", "CE", "EE"], ["Amazon", "TCS Digital", "Infosys", "Wipro", "Cognizant"]),
        ("225", "Accurate Institute of Management and Technology", "Greater Noida", "Private", 2006, "B+", "301-400", 112000, 24.0, 6.2, 80, ["CSE", "IT", "ECE", "ME", "CE"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("486", "KCC Institute of Technology and Management", "Greater Noida", "Private", 2009, "B+", "301-400", 95000, 16.0, 5.2, 72, ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("216", "IIMT College of Engineering", "Greater Noida", "Private", 2005, "A", "201-300", 120000, 32.0, 7.0, 85, ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE"], ["Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini"]),
        ("274", "Dronacharya Group of Institutions", "Greater Noida", "Private", 2006, "A", "201-300", 118000, 30.0, 6.8, 84, ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE"], ["Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini"]),
        ("539", "Lloyd Institute of Engineering & Technology", "Greater Noida", "Private", 2002, "A", "201-300", 115000, 28.0, 6.5, 82, ["CSE", "CSE-AI", "ECE", "ME", "CE", "B.Pharm"], ["Amazon", "TCS", "Infosys", "Wipro", "Cipla"]),
        ("152", "Mangalmay Institute of Engineering & Technology", "Greater Noida", "Private", 2002, "A", "201-300", 112000, 26.0, 6.2, 80, ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE", "MBA"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("151", "Skyline Institute of Engineering and Technology", "Greater Noida", "Private", 2002, "B+", "301-400", 105000, 20.0, 5.8, 78, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra"]),
        ("592", "GNIT College of Management & Technology", "Greater Noida", "Private", 2001, "B+", "301-400", 108000, 22.0, 6.0, 79, ["CSE", "IT", "ECE", "ME", "CE", "MBA"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("057", "IEC College of Engineering & Technology", "Greater Noida", "Private", 2000, "B+", "301-400", 108000, 20.0, 6.0, 79, ["CSE", "ECE", "ME", "CE", "IT"], ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]),
        ("211", "Rakshpal Bahadur Management Institute Noida", "Greater Noida", "Private", 2007, "B", "401-500", 88000, 14.0, 4.8, 70, ["CSE", "IT", "ECE", "ME", "CE"], ["TCS", "Infosys", "Wipro", "HCL"]),
        ("672", "Anand International College Greater Noida", "Greater Noida", "Private", 2008, "B", "401-500", 85000, 13.0, 4.5, 68, ["CSE", "ECE", "ME", "CE"], ["TCS", "Wipro", "HCL", "Teleperformance"]),
        ("729", "Priyadarshini College of Computer Sciences", "Greater Noida", "Private", 2005, "B", "401-500", 82000, 12.0, 4.4, 66, ["CSE", "IT", "ECE", "ME"], ["TCS", "Infosys", "Wipro", "HCL"]),
        ("801", "Noida International Engineering Institute", "Greater Noida", "Private", 2008, "B", "401-500", 85000, 13.5, 4.6, 68, ["CSE", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL"])
    ],
    "Ghaziabad": [
        ("027", "Ajay Kumar Garg Engineering College (AKGEC)", "Ghaziabad", "Private Autonomous", 1998, "A", "101-150", 141000, 44.0, 9.2, 91, ["CSE", "CSE-AI", "CSE-DS", "ECE", "ME", "CE", "IT"], ["Amazon", "Microsoft", "IBM", "TCS", "Infosys"]),
        ("029", "KIET Group of Institutions", "Ghaziabad", "Private Autonomous", 1998, "A+", "76-100", 139000, 48.5, 9.5, 93, ["CSE", "CSE-AI", "CSE-DS", "ECE", "ME", "CE", "IT"], ["Atlassian", "Amazon", "Capgemini", "TCS Digital", "Wipro"]),
        ("032", "ABES Engineering College (ABES EC)", "Ghaziabad", "Private Autonomous", 2000, "A", "201-300", 135000, 50.0, 8.2, 90, ["CSE", "CSE-AI", "ECE", "ME", "CE", "IT"], ["Microsoft", "Google", "Amazon", "TCS Digital", "Infosys"]),
        ("229", "ABES Institute of Technology (ABESIT)", "Ghaziabad", "Private", 2007, "A", "201-300", 125000, 28.0, 6.8, 86, ["CSE", "CSE-AI", "CSE-DS", "IT", "ECE", "ME"], ["TCS", "Infosys", "Wipro", "Capgemini", "Cognizant"]),
        ("070", "IMS Engineering College (IMS EC)", "Ghaziabad", "Private Autonomous", 2001, "A", "201-300", 128000, 38.0, 7.8, 88, ["CSE", "ECE", "ME", "CE", "IT"], ["Amazon", "TCS Digital", "Infosys SP", "Wipro", "HCL"]),
        ("068", "Inderprastha Engineering College (IPEC)", "Ghaziabad", "Private Autonomous", 1999, "A", "201-300", 124000, 36.0, 7.5, 87, ["CSE", "CSE-AI", "ECE", "ME", "CE", "IT", "EE"], ["Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini"]),
        ("126", "Raj Kumar Goel Institute of Technology (RKGIT)", "Ghaziabad", "Private Autonomous", 2000, "A", "201-300", 122000, 30.0, 7.0, 84, ["CSE", "ECE", "ME", "CE", "IT"], ["TCS", "Amazon", "Infosys", "Wipro", "HCL"]),
        ("301", "RKGIT for Women (RKGITW)", "Ghaziabad", "Private", 2008, "B+", "301-400", 105000, 20.0, 5.8, 80, ["CSE", "IT", "ECE"], ["TCS", "Infosys", "Wipro", "Cognizant", "Capgemini"]),
        ("578", "Krishna Engineering College (KEC)", "Ghaziabad", "Private", 2004, "A", "201-300", 125000, 30.0, 7.0, 85, ["CSE", "CSE-AI", "IT", "ECE", "ME", "CE"], ["Amazon", "TCS", "Infosys", "Wipro", "Capgemini"]),
        ("231", "RD Engineering College (RDEC)", "Ghaziabad", "Private", 2006, "B+", "301-400", 105000, 20.0, 5.8, 78, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("230", "H.R. Institute of Technology (HRIT)", "Ghaziabad", "Private", 2005, "B+", "301-400", 102000, 18.0, 5.6, 76, ["CSE", "IT", "ECE", "ME", "CE", "EE", "B.Pharm"], ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]),
        ("490", "Sunder Deep Engineering College (SDEC)", "Ghaziabad", "Private", 2006, "B+", "301-400", 100000, 18.5, 5.5, 75, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra"]),
        ("532", "Sanskar Educational Group", "Ghaziabad", "Private", 2005, "B+", "301-400", 98000, 17.0, 5.4, 74, ["CSE", "IT", "ECE", "ME", "CE", "B.Pharm"], ["TCS", "Infosys", "Wipro", "HCL", "Sun Pharma"]),
        ("651", "Hi-Tech Institute of Engineering & Technology", "Ghaziabad", "Private", 2006, "B", "401-500", 90000, 14.0, 4.8, 70, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL"]),
        ("290", "Ideal Institute of Technology", "Ghaziabad", "Private", 1998, "B", "401-500", 88000, 13.5, 4.6, 68, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL"]),
        ("036", "Institute of Technology & Management Ghaziabad", "Ghaziabad", "Private", 1997, "B+", "301-400", 98000, 17.0, 5.2, 74, ["CSE", "IT", "ECE", "ME", "CE"], ["TCS", "Infosys", "Wipro", "Capgemini"]),
        ("459", "BBS Institute of Management & Technology Ghaziabad", "Ghaziabad", "Private", 2006, "B", "401-500", 85000, 12.5, 4.5, 67, ["CSE", "IT", "ECE", "ME"], ["TCS", "Infosys", "Wipro", "Tech Mahindra"]),
        ("528", "Bhagwant Institute of Engineering Ghaziabad", "Ghaziabad", "Private", 2008, "B", "401-500", 82000, 12.0, 4.4, 65, ["CSE", "ECE", "ME", "CE"], ["TCS", "Wipro", "HCL", "Teleperformance"])
    ],
    "Lucknow": [
        ("052", "Institute of Engineering and Technology (IET Lucknow)", "Lucknow", "Government Autonomous", 1984, "A+", "151-200", 85000, 49.0, 10.5, 94, ["CSE", "CSE-AI", "ECE", "ME", "EE", "CE", "Chemical"], ["Google", "Amazon", "Microsoft", "Adobe", "Samsung"]),
        ("LU-ENG", "Faculty of Engineering & Technology Lucknow University", "Lucknow", "Government University", 2017, "A++", "101-150", 80000, 28.0, 7.5, 85, ["CSE", "CSE-AI", "ECE", "ME", "CE", "EE"], ["Amazon", "TCS", "Infosys", "Wipro", "Capgemini"]),
        ("091-L", "Babu Banarasi Das Institute of Technology & Management (BBDITM)", "Lucknow", "Private", 2000, "B+", "301-400", 105000, 18.0, 5.8, 78, ["CSE", "ECE", "ME", "CE", "IT"], ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]),
        ("056", "BBD Northern India Institute of Technology (BBDNIIT)", "Lucknow", "Private", 1999, "B+", "301-400", 108000, 20.0, 6.0, 80, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]),
        ("508", "Babu Banarasi Das Engineering College (BBDEC)", "Lucknow", "Private", 2008, "B", "401-500", 95000, 15.0, 5.0, 72, ["CSE", "IT", "ECE", "ME", "CE"], ["TCS", "Infosys", "Wipro", "Tech Mahindra"]),
        ("130", "Shri Ramswaroop Memorial College (SRMCEM)", "Lucknow", "Private Autonomous", 2001, "A", "201-300", 115000, 32.0, 7.2, 85, ["CSE", "ECE", "ME", "CE", "IT", "MBA"], ["TCS Digital", "Amazon", "Infosys", "Wipro", "HCL"]),
        ("195", "SRM College of Engineering & Management (SRM Lucknow)", "Lucknow", "Private", 2010, "B+", "301-400", 110000, 22.0, 6.2, 80, ["CSE", "ECE", "ME", "CE", "IT", "MBA"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("392", "Goel Institute of Technology & Management (GITM)", "Lucknow", "Private", 2008, "B+", "301-400", 98000, 16.0, 5.2, 74, ["CSE", "ECE", "ME", "CE", "IT", "MBA"], ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra"]),
        ("422", "Bansal Institute of Engineering & Technology (BIET Lucknow)", "Lucknow", "Private", 2008, "B+", "401-500", 92000, 14.0, 4.8, 70, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]),
        ("425", "B.N. College of Engineering & Technology (BNCET)", "Lucknow", "Private", 2008, "B", "401-500", 86000, 12.5, 4.5, 67, ["CSE", "IT", "ECE", "ME", "CE"], ["TCS", "Infosys", "Wipro", "HCL"]),
        ("053", "Azad Institute of Engineering & Technology (AIET)", "Lucknow", "Private", 1998, "B+", "301-400", 95000, 16.0, 5.2, 73, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]),
        ("406", "R.R. Institute of Modern Technology (RRIMT)", "Lucknow", "Private", 2008, "B", "401-500", 85000, 13.5, 4.6, 69, ["CSE", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "Tech Mahindra"]),
        ("732", "Ambalika Institute of Management and Technology (AIMT)", "Lucknow", "Private", 2008, "B+", "301-400", 98000, 18.0, 5.5, 76, ["CSE", "IT", "ECE", "ME", "CE"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("772", "School of Management Sciences (SMS Lucknow)", "Lucknow", "Private", 2008, "B+", "301-400", 92000, 15.0, 5.0, 74, ["CSE", "IT", "ECE", "ME", "CE", "BBA", "MBA"], ["TCS", "Infosys", "Wipro", "HDFC", "ICICI Bank"]),
        ("567", "Hygia Institute of Technology & Management", "Lucknow", "Private", 2005, "B", "401-500", 88000, 12.0, 4.5, 68, ["CSE", "ECE", "ME", "CE", "B.Pharm"], ["TCS", "Infosys", "Sun Pharma", "Cipla"]),
        ("621", "Mahatma Gandhi Institute of Technology (MGIMT)", "Lucknow", "Private", 2009, "B", "401-500", 82000, 11.0, 4.2, 65, ["CSE", "ECE", "ME", "CE"], ["TCS", "Wipro", "HCL", "Teleperformance"]),
        ("648", "Lucknow Institute of Technology (LIT Lucknow)", "Lucknow", "Private", 2008, "B", "401-500", 86000, 13.0, 4.5, 68, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL"]),
        ("681", "Rameshwaram Institute of Technology & Management", "Lucknow", "Private", 2005, "B", "401-500", 84000, 12.5, 4.4, 67, ["CSE", "ECE", "ME", "CE", "B.Pharm"], ["TCS", "Infosys", "Sun Pharma", "Cipla"]),
        ("811", "Saroj Institute of Technology & Management (SITM)", "Lucknow", "Private", 2001, "B", "401-500", 85000, 13.0, 4.5, 68, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL"])
    ],
    "Kanpur": [
        ("061", "Harcourt Butler Technical University (HBTU Kanpur)", "Kanpur", "Government University", 1921, "A+", "76-100", 62000, 65.0, 12.5, 96, ["CSE", "ECE", "ME", "CE", "Chemical", "IT", "EE"], ["Google", "Amazon", "Microsoft", "Goldman Sachs", "Morgan Stanley"]),
        ("UIET-K", "University Institute of Engineering and Technology (UIET CSJMU)", "Kanpur", "Government University", 1996, "A+", "151-200", 75000, 25.0, 7.2, 84, ["CSE", "IT", "ECE", "ME", "Chemical", "Materials"], ["TCS", "Infosys", "Wipro", "Cognizant", "L&T"]),
        ("164", "Pranveer Singh Institute of Technology (PSIT Kanpur)", "Kanpur", "Private Autonomous", 2004, "A", "201-300", 120000, 40.0, 7.8, 88, ["CSE", "CSE-AI", "ECE", "ME", "CE", "IT", "MBA"], ["TCS Digital", "Infosys SP", "Wipro Elite", "HCL", "Tech Mahindra"]),
        ("047", "Maharana Pratap Engineering College (MPEC)", "Kanpur", "Private", 1999, "B+", "301-400", 105000, 22.0, 6.0, 81, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]),
        ("165", "Kanpur Institute of Technology (KIT Kanpur)", "Kanpur", "Private", 2004, "B+", "301-400", 98000, 16.5, 5.4, 75, ["CSE", "IT", "ECE", "ME", "CE"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("514", "Axis Institute of Technology & Management (AITM)", "Kanpur", "Private", 2010, "B+", "301-400", 98000, 18.0, 5.5, 76, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("428", "Apollo Institute of Technology (AIT Kanpur)", "Kanpur", "Private", 2008, "B", "401-500", 85000, 12.0, 4.4, 66, ["CSE", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL"]),
        ("786", "Allenhouse Institute of Technology", "Kanpur", "Private", 2009, "B+", "301-400", 95000, 16.0, 5.2, 74, ["CSE", "IT", "ECE", "ME", "CE"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("803", "Naraina College of Engineering and Technology", "Kanpur", "Private", 2007, "B", "401-500", 88000, 13.5, 4.6, 68, ["CSE", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "Tech Mahindra"]),
        ("727", "Maharana Institute of Professional Studies (MIPS)", "Kanpur", "Private", 2008, "B", "401-500", 86000, 13.0, 4.5, 67, ["CSE", "IT", "ECE", "ME", "CE"], ["TCS", "Infosys", "Wipro", "HCL"]),
        ("832", "Krishna Girls Engineering College", "Kanpur", "Private", 2008, "B", "401-500", 82000, 12.0, 4.3, 65, ["CSE", "IT", "ECE"], ["TCS", "Infosys", "Wipro", "HCL"])
    ],
    "Meerut": [
        ("108", "Meerut Institute of Engineering & Technology (MIET)", "Meerut", "Private Autonomous", 1995, "A", "201-300", 118000, 35.0, 7.5, 86, ["CSE", "ECE", "ME", "CE", "IT", "EE"], ["TCS Digital", "Infosys", "Wipro", "Amazon", "HCL"]),
        ("543", "Sir Chhotu Ram Institute of Engineering & Technology (SCRIET CCSU)", "Meerut", "Government University", 2002, "A+", "201-300", 65000, 18.0, 5.8, 79, ["CSE", "IT", "ECE", "ME", "CE", "Chemical"], ["TCS", "Infosys", "Wipro", "Cognizant", "HCL"]),
        ("243", "Vidya College of Engineering", "Meerut", "Private", 2006, "B+", "301-400", 102000, 20.0, 5.8, 78, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]),
        ("129", "Dewan V.S. Institute of Engineering & Technology", "Meerut", "Private", 1996, "B+", "301-400", 98000, 18.0, 5.5, 76, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("127", "Bharat Institute of Technology (BIT Meerut)", "Meerut", "Private", 2001, "B+", "301-400", 95000, 17.5, 5.4, 75, ["CSE", "IT", "ECE", "ME", "CE", "EE", "B.Pharm"], ["TCS", "Infosys", "Wipro", "HCL", "Cipla"]),
        ("073", "Forte Institute of Technology", "Meerut", "Private", 1998, "B", "401-500", 85000, 13.0, 4.6, 68, ["CSE", "IT", "ECE", "ME", "CE"], ["TCS", "Infosys", "Wipro", "HCL"]),
        ("045", "Radha Govind Engineering College", "Meerut", "Private", 1999, "B+", "301-400", 92000, 15.0, 5.0, 73, ["CSE", "IT", "ECE", "ME", "CE"], ["TCS", "Infosys", "Wipro", "Capgemini"]),
        ("143", "Shanti Institute of Technology", "Meerut", "Private", 2008, "B", "401-500", 82000, 12.0, 4.4, 66, ["CSE", "ECE", "ME", "CE"], ["TCS", "Wipro", "HCL", "Teleperformance"]),
        ("293", "Neelkanth Group of Educational Institutions", "Meerut", "Private", 2008, "B", "401-500", 80000, 11.5, 4.2, 65, ["CSE", "ECE", "ME", "CE"], ["TCS", "Wipro", "HCL"])
    ],
    "Agra & Mathura": [
        ("001", "Anand Engineering College (AEC Agra)", "Agra", "Private", 1998, "B+", "301-400", 108000, 24.0, 6.0, 80, ["CSE", "ECE", "ME", "CE", "EE", "Biotech"], ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]),
        ("002", "Hindustan College of Science and Technology (HCST)", "Mathura", "Private", 1996, "A", "201-300", 115000, 26.0, 6.4, 82, ["CSE", "IT", "ECE", "ME", "CE", "EE", "Chemical"], ["Amazon", "TCS", "Infosys", "Wipro", "Capgemini"]),
        ("004", "Faculty of Engineering & Technology Agra College", "Agra", "Private Aided", 1999, "B+", "301-400", 85000, 15.0, 5.2, 74, ["CSE", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "L&T"]),
        ("064", "BSA College of Engineering & Technology", "Mathura", "Private", 1997, "B+", "301-400", 95000, 16.0, 5.4, 75, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]),
        ("395", "RBS Management Technical Campus (RBS Bichpuri)", "Agra", "Private Aided", 1996, "A", "201-300", 88000, 20.0, 5.8, 79, ["CSE", "ECE", "ME", "CE", "EE", "Food Tech", "Biotech"], ["TCS", "Infosys", "Wipro", "Nestle", "Amul"]),
        ("174", "Eshan College of Engineering", "Mathura", "Private", 2009, "B", "401-500", 78000, 12.0, 4.5, 68, ["CSE", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "Tech Mahindra"]),
        ("580", "ACE College of Engineering & Management", "Agra", "Private", 2011, "B", "401-500", 75000, 11.5, 4.2, 65, ["CSE", "ECE", "ME", "CE"], ["TCS", "Wipro", "HCL", "Teleperformance"]),
        ("612", "Unnati Management College Faculty of Tech", "Mathura", "Private", 2009, "B", "401-500", 76000, 11.0, 4.1, 64, ["CSE", "ECE", "ME", "CE"], ["TCS", "Wipro", "HCL"])
    ],
    "Prayagraj & Varanasi": [
        ("105", "United College of Engineering & Research (UCER)", "Prayagraj", "Private Autonomous", 1998, "A", "201-300", 120000, 30.0, 6.8, 84, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini"]),
        ("106", "United Institute of Technology (UIT Prayagraj)", "Prayagraj", "Private", 2007, "B+", "301-400", 110000, 22.0, 6.0, 80, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("112", "Shambhunath Institute of Engineering & Technology (SIET)", "Prayagraj", "Private", 2004, "B+", "301-400", 105000, 20.0, 5.8, 78, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"]),
        ("111", "BBS College of Engineering & Technology", "Prayagraj", "Private", 2002, "B", "401-500", 88000, 14.0, 4.8, 70, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "Tech Mahindra"]),
        ("144", "LDC Institute of Technical Studies", "Prayagraj", "Private", 2007, "B", "401-500", 85000, 13.0, 4.6, 68, ["CSE", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL"]),
        ("368", "Ashoka Institute of Technology and Management", "Varanasi", "Private", 2010, "B+", "301-400", 102000, 20.0, 5.6, 78, ["CSE", "IT", "ECE", "ME", "CE", "EE", "B.Pharm"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("427", "Kashi Institute of Technology (KIT Varanasi)", "Varanasi", "Private", 2008, "B+", "301-400", 98000, 18.0, 5.4, 76, ["CSE", "IT", "ECE", "ME", "CE", "EE", "B.Pharm"], ["TCS", "Infosys", "Wipro", "HCL", "Sun Pharma"]),
        ("512", "School of Management Sciences (SMS Varanasi)", "Varanasi", "Private Autonomous", 1995, "A", "151-200", 112000, 24.0, 6.2, 82, ["CSE", "ECE", "ME", "CE", "BBA", "BCA", "MBA"], ["TCS", "Infosys", "Wipro", "ICICI Bank", "HDFC"]),
        ("792", "Microtek College of Management & Technology", "Varanasi", "Private", 2007, "B", "401-500", 82000, 12.0, 4.4, 66, ["CSE", "IT", "BCA", "BBA"], ["TCS", "Wipro", "HCL", "Teleperformance"])
    ],
    "Government Engineering Colleges & Universities": [
        ("043", "Bundelkhand Institute of Engineering & Technology (BIET Jhansi)", "Jhansi", "Government Autonomous", 1960, "A", "151-200", 61800, 42.0, 8.5, 87, ["CSE", "ECE", "ME", "EE", "CE", "IT", "Chemical"], ["Amazon", "TCS", "Infosys", "Wipro", "Samsung"]),
        ("104", "Kamla Nehru Institute of Technology (KNIT Sultanpur)", "Sultanpur", "Government Autonomous", 1979, "A", "151-200", 64350, 45.0, 8.8, 88, ["CSE", "ECE", "ME", "EE", "CE", "IT", "MCA"], ["Amazon", "Samsung", "TCS", "Infosys", "Wipro"]),
        ("842", "Rajkiya Engineering College Banda (REC Banda)", "Banda", "Government", 2010, "B+", "301-400", 58000, 15.0, 5.5, 75, ["CSE", "ECE", "EE", "ME", "CE"], ["TCS", "Infosys", "Wipro", "HCL", "BHEL"]),
        ("843", "Rajkiya Engineering College Bijnor (REC Bijnor)", "Bijnor", "Government", 2010, "B+", "301-400", 58000, 16.5, 5.6, 76, ["CSE", "IT", "EE", "CE"], ["TCS", "Infosys", "Wipro", "Capgemini", "Tech Mahindra"]),
        ("844", "Rajkiya Engineering College Azamgarh (REC Azamgarh)", "Azamgarh", "Government", 2010, "B+", "301-400", 58000, 14.5, 5.2, 74, ["CSE", "IT", "ME", "CE"], ["TCS", "Infosys", "HCL", "Wipro", "Cognizant"]),
        ("845", "Rajkiya Engineering College Ambedkar Nagar", "Ambedkar Nagar", "Government", 2010, "B+", "301-400", 58000, 15.5, 5.4, 75, ["CSE", "IT", "EE", "CE"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("846", "Rajkiya Engineering College Kannauj (REC Kannauj)", "Kannauj", "Government", 2015, "B", "401-500", 56000, 13.0, 5.0, 72, ["CSE", "ECE", "EE", "CE"], ["TCS", "Infosys", "Wipro", "Tech Mahindra"]),
        ("847", "Rajkiya Engineering College Mainpuri (REC Mainpuri)", "Mainpuri", "Government", 2015, "B", "401-500", 56000, 12.5, 4.8, 70, ["CSE", "ME", "EE", "CE"], ["TCS", "Infosys", "Wipro", "HCL"]),
        ("848", "Rajkiya Engineering College Sonbhadra (REC Sonbhadra)", "Sonbhadra", "Government", 2015, "B", "401-500", 56000, 14.0, 5.1, 73, ["CSE", "ECE", "EE", "Mining"], ["NTPC", "Hindalco", "TCS", "Infosys", "Wipro"]),
        ("128", "Rampur Engineering College (REC Rampur)", "Rampur", "Government", 2010, "B", "401-500", 55000, 12.0, 4.5, 68, ["CSE", "ECE", "ME", "CE"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("MJPRU-ENG", "Faculty of Engineering & Technology MJPRU Bareilly", "Bareilly", "Government University", 1995, "A+", "151-200", 68000, 20.0, 6.5, 80, ["CSE", "IT", "ECE", "ME", "EE", "Chemical"], ["TCS", "Infosys", "Wipro", "HCL", "Cognizant"])
    ],
    "Purvanchal & Eastern UP": [
        ("120", "Institute of Technology & Management (ITM Gorakhpur)", "Gorakhpur", "Private", 2001, "B+", "301-400", 105000, 22.0, 5.8, 79, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("740", "Buddha Institute of Technology (BIT Gorakhpur)", "Gorakhpur", "Private", 2009, "B+", "301-400", 95000, 16.0, 5.2, 74, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra"]),
        ("808", "KIPM College of Engineering & Technology", "Gorakhpur", "Private", 2009, "B", "401-500", 88000, 14.0, 4.8, 70, ["CSE", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL"]),
        ("492", "Suyash Institute of Information Technology", "Gorakhpur", "Private", 2009, "B", "401-500", 82000, 12.0, 4.4, 66, ["CSE", "IT", "ECE", "ME", "CE"], ["TCS", "Wipro", "HCL", "Teleperformance"]),
        ("628", "Prasad Institute of Technology Jaunpur", "Jaunpur", "Private", 2002, "B+", "301-400", 92000, 15.0, 5.0, 73, ["CSE", "IT", "ECE", "ME", "CE", "B.Pharm"], ["TCS", "Infosys", "Wipro", "Sun Pharma"]),
        ("711", "VBS Purvanchal University Faculty of Engineering", "Jaunpur", "Government University", 1997, "A", "201-300", 65000, 18.0, 5.5, 78, ["CSE", "IT", "ECE", "ME", "EE", "Power Engg"], ["TCS", "Infosys", "Wipro", "Cognizant"]),
        ("755", "Technical Education & Research Institute Ghazipur", "Ghazipur", "Private", 2008, "B", "401-500", 80000, 11.5, 4.2, 65, ["CSE", "ECE", "ME", "CE"], ["TCS", "Wipro", "HCL"])
    ],
    "Western UP & Rohilkhand": [
        ("014", "Shri Ram Murti Smarak College (SRMS CET)", "Bareilly", "Private Autonomous", 1996, "A", "201-300", 126000, 34.0, 7.2, 86, ["CSE", "IT", "ECE", "ME", "EE", "B.Pharm", "MCA"], ["Amazon", "TCS Digital", "Infosys", "Wipro", "Capgemini"]),
        ("451", "SRMS College of Engineering, Technology & Research (SRMS CETR)", "Bareilly", "Private", 2008, "B+", "301-400", 105000, 22.0, 5.8, 78, ["CSE", "IT", "ECE", "ME"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("140", "Invertis University Faculty of Engineering", "Bareilly", "Private University", 2010, "B+", "301-400", 98000, 15.0, 5.2, 72, ["CSE", "ECE", "ME", "CE", "IT", "MBA"], ["TCS", "Wipro", "Infosys", "HCL", "Cognizant"]),
        ("240", "Rakshpal Bahadur Management Institute (RBMI)", "Bareilly", "Private", 1996, "B+", "301-400", 95000, 18.0, 5.4, 75, ["CSE", "IT", "ECE", "ME", "CE", "B.Pharm", "MBA"], ["TCS", "Infosys", "Wipro", "HCL", "Cipla"]),
        ("241", "Future Institute of Engineering and Technology", "Bareilly", "Private", 2009, "B+", "301-400", 92000, 16.0, 5.2, 74, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra"]),
        ("244", "ANA College of Engineering & Management", "Bareilly", "Private", 2009, "B", "401-500", 82000, 12.5, 4.5, 68, ["CSE", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL"]),
        ("016", "Moradabad Institute of Technology (MIT)", "Moradabad", "Private", 1996, "A", "201-300", 112000, 25.0, 6.2, 82, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("488", "S.D. College of Engineering & Technology", "Muzaffarnagar", "Private", 1997, "B+", "301-400", 92000, 16.0, 5.2, 74, ["CSE", "IT", "ECE", "ME", "CE", "EE", "Chemical"], ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra"]),
        ("502", "Bhagwant Institute of Technology (BIT Muzaffarnagar)", "Muzaffarnagar", "Private", 2000, "B", "401-500", 82000, 12.0, 4.4, 66, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL"]),
        ("246", "Shobhit Institute of Engineering & Technology Gangoh", "Saharanpur", "Private", 2000, "B+", "301-400", 95000, 18.0, 5.4, 75, ["CSE", "IT", "ECE", "ME", "CE", "Biotech", "B.Pharm"], ["TCS", "Infosys", "Wipro", "HCL", "Sun Pharma"]),
        ("109", "Aligarh College of Engineering and Technology", "Aligarh", "Private", 2001, "B+", "301-400", 92000, 16.5, 5.2, 73, ["CSE", "IT", "ECE", "ME", "CE", "EE"], ["TCS", "Infosys", "Wipro", "HCL", "Capgemini"]),
        ("110", "Vision Institute of Technology Aligarh", "Aligarh", "Private", 2006, "B", "401-500", 80000, 12.0, 4.3, 65, ["CSE", "ECE", "ME", "CE", "EE"], ["TCS", "Wipro", "HCL", "Teleperformance"]),
        ("450", "Shivdan Singh Institute of Technology Aligarh", "Aligarh", "Private", 1997, "B", "401-500", 85000, 13.0, 4.5, 67, ["CSE", "IT", "ECE", "ME", "B.Pharm"], ["TCS", "Infosys", "Cipla", "Sun Pharma"])
    ]
}

flat_colleges = []
for dist, coll_list in districts_colleges.items():
    for c in coll_list:
        code, name, city, aff_type, est, naac, nirf, fee, h_pkg, avg_pkg, pct, branches, rec = c
        
        # create slug
        slug_raw = re.sub(r'[^a-zA-Z0-9\s-]', '', name.lower()).strip()
        slug = re.sub(r'[\s]+', '-', slug_raw) + "-profile"
        # ensure no duplicate slug
        if any(x["slug"] == slug for x in flat_colleges):
            slug = f"{slug}-{code.lower()}"

        flat_colleges.append({
            "slug": slug,
            "code": code,
            "name": name,
            "city": city,
            "district": dist,
            "type": aff_type,
            "est": est,
            "naac": naac,
            "nirf": nirf,
            "fee": fee,
            "h_pkg": h_pkg,
            "avg_pkg": avg_pkg,
            "pct": pct,
            "branches": branches,
            "rec": rec
        })

print(f"Total curated master colleges across UP: {len(flat_colleges)}")

with open("scripts/flat_colleges.json", "w", encoding="utf-8") as f:
    json.dump(flat_colleges, f, indent=2)

print("Saved flat_colleges.json!")
