import json, re

with open("scripts/flat_colleges.json", "r", encoding="utf-8") as f:
    master_colleges = json.load(f)

existing_codes = set(str(c["code"]) for c in master_colleges)

final_batch = [
    ("851", "Shambhunath Institute of Pharmacy Prayagraj", "Prayagraj", "Private", 2006, "A", "101-150 (Pharmacy)", 110000, 16.0, 5.0, 80, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Lupin"]),
    ("852", "Pranveer Singh Institute of Pharmacy Kanpur", "Kanpur", "Private", 2008, "A", "76-100 (Pharmacy)", 125000, 20.0, 5.8, 85, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Dr. Reddy's"]),
    ("853", "Maharana Pratap College of Pharmacy Kanpur", "Kanpur", "Private", 2005, "B+", "101-150 (Pharmacy)", 105000, 15.0, 4.8, 78, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Mankind"]),
    ("854", "Kanpur Institute of Pharmacy", "Kanpur", "Private", 2006, "B+", "101-150 (Pharmacy)", 100000, 14.5, 4.8, 76, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Torrent"]),
    ("855", "Axis Institute of Pharmacy Kanpur", "Kanpur", "Private", 2010, "B+", "101-150 (Pharmacy)", 98000, 14.0, 4.6, 75, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Alkem"]),
    ("856", "MIET School of Pharmacy Meerut", "Meerut", "Private", 2005, "A", "76-100 (Pharmacy)", 118000, 18.0, 5.5, 84, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Lupin"]),
    ("857", "Dewan School of Pharmacy Meerut", "Meerut", "Private", 2006, "B+", "101-150 (Pharmacy)", 98000, 14.0, 4.6, 75, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Abbott"]),
    ("858", "Vidya Institute of Pharmacy Meerut", "Meerut", "Private", 2007, "B+", "101-150 (Pharmacy)", 102000, 15.0, 4.8, 78, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Cipla"]),
    ("859", "Anand College of Pharmacy Agra", "Agra", "Private", 2006, "A", "101-150 (Pharmacy)", 108000, 16.0, 5.0, 80, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Lupin"]),
    ("860", "Hindustan Institute of Pharmacy Mathura", "Mathura", "Private", 2006, "A", "101-150 (Pharmacy)", 110000, 16.5, 5.2, 81, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "GSK"]),
    ("861", "RBS Management Technical Campus Pharmacy Wing", "Agra", "Private Aided", 2000, "A", "101-150 (Pharmacy)", 95000, 15.5, 5.0, 80, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Mankind"]),
    ("862", "Babu Banarasi Das College of Dental Sciences", "Lucknow", "Private", 2000, "A", "40-60 (Dental)", 280000, 15.0, 6.5, 90, ["BDS", "MDS"], ["Fortis", "Max Healthcare", "Apollo Dental"]),
    ("863", "Saraswati Dental College Lucknow", "Lucknow", "Private", 1998, "A", "40-60 (Dental)", 275000, 14.0, 6.2, 88, ["BDS", "MDS"], ["Apollo", "Fortis", "Medanta"]),
    ("864", "Subharti Dental College Meerut", "Meerut", "Private University", 1996, "A+", "25-40 (Dental)", 290000, 16.0, 7.0, 92, ["BDS", "MDS"], ["Apollo", "Max", "Fortis"]),
    ("865", "Santosh Dental College Ghaziabad", "Ghaziabad", "Private Deemed", 1995, "A", "30-50 (Dental)", 300000, 16.5, 7.2, 92, ["BDS", "MDS"], ["Apollo", "Fortis", "Medanta"]),
    ("866", "ITM College of Pharmacy Gorakhpur", "Gorakhpur", "Private", 2008, "B+", "101-150 (Pharmacy)", 98000, 14.0, 4.6, 75, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Lupin"]),
    ("867", "KIPM College of Pharmacy Gorakhpur", "Gorakhpur", "Private", 2010, "B", "151-200 (Pharmacy)", 92000, 13.0, 4.4, 72, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Mankind"]),
    ("868", "Buddha Institute of Pharmacy Gorakhpur", "Gorakhpur", "Private", 2011, "B+", "101-150 (Pharmacy)", 95000, 13.5, 4.5, 74, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Torrent"]),
    ("869", "Ashoka Institute of Pharmacy Varanasi", "Varanasi", "Private", 2010, "B+", "101-150 (Pharmacy)", 100000, 15.0, 4.8, 76, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Dr. Reddy's"]),
    ("870", "Kashi Institute of Pharmacy Varanasi", "Varanasi", "Private", 2009, "B+", "101-150 (Pharmacy)", 98000, 14.5, 4.7, 75, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Alkem"]),
    ("871", "Aryakul College of Pharmacy & Research Lucknow", "Lucknow", "Private", 2007, "B+", "101-150 (Pharmacy)", 98000, 14.0, 4.6, 75, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Lupin"]),
    ("872", "Goel Institute of Pharmacy & Sciences Lucknow", "Lucknow", "Private", 2008, "B+", "101-150 (Pharmacy)", 102000, 15.0, 4.8, 78, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Mankind"]),
    ("873", "Bansal College of Pharmacy Lucknow", "Lucknow", "Private", 2009, "B", "151-200 (Pharmacy)", 92000, 13.0, 4.4, 72, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Torrent"]),
    ("874", "BN College of Pharmacy Lucknow", "Lucknow", "Private", 2009, "B", "151-200 (Pharmacy)", 90000, 12.5, 4.3, 70, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Alkem"]),
    ("875", "R.R. College of Pharmacy Lucknow", "Lucknow", "Private", 2009, "B", "151-200 (Pharmacy)", 90000, 12.5, 4.3, 70, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "GSK"]),
    ("876", "Hygia Academy of Pharmacy Lucknow", "Lucknow", "Private", 2005, "B+", "101-150 (Pharmacy)", 95000, 14.0, 4.5, 74, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Abbott"]),
    ("877", "Rameshwaram Institute of Pharmacy Lucknow", "Lucknow", "Private", 2005, "B+", "101-150 (Pharmacy)", 95000, 14.0, 4.5, 74, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Lupin"]),
    ("878", "Saroj Institute of Pharmacy Lucknow", "Lucknow", "Private", 2001, "B+", "101-150 (Pharmacy)", 98000, 14.5, 4.7, 75, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Sun Pharma"]),
    ("879", "Central Institute of Pharmacy Lucknow", "Lucknow", "Private", 2008, "B", "151-200 (Pharmacy)", 90000, 12.5, 4.3, 70, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Cipla"]),
    ("880", "Future Institute of Pharmacy Bareilly", "Bareilly", "Private", 2010, "B+", "101-150 (Pharmacy)", 95000, 14.0, 4.6, 75, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Mankind"]),
    ("881", "Rajshree College of Pharmacy Bareilly", "Bareilly", "Private", 2010, "B+", "101-150 (Pharmacy)", 98000, 14.5, 4.7, 76, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Lupin"]),
    ("882", "ANA Institute of Pharmaceutical Sciences Bareilly", "Bareilly", "Private", 2010, "B", "151-200 (Pharmacy)", 88000, 12.5, 4.3, 70, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Torrent"]),
    ("883", "Shri Siddhi Vinayak Institute of Pharmacy Bareilly", "Bareilly", "Private", 2009, "B+", "101-150 (Pharmacy)", 92000, 13.5, 4.5, 73, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Alkem"]),
    ("884", "Lotus Institute of Pharmacy Bareilly", "Bareilly", "Private", 2008, "B", "151-200 (Pharmacy)", 88000, 12.5, 4.3, 70, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "GSK"]),
    ("885", "MIT College of Pharmacy Moradabad", "Moradabad", "Private", 2008, "B+", "101-150 (Pharmacy)", 98000, 14.5, 4.7, 76, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Dr. Reddy's"]),
    ("886", "Apex Institute of Pharmacy Rampur", "Rampur", "Private", 2009, "B", "151-200 (Pharmacy)", 88000, 12.5, 4.3, 70, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Cipla"]),
    ("887", "Disha Institute of Pharmacy Bijnor", "Bijnor", "Private", 2009, "B", "151-200 (Pharmacy)", 85000, 12.0, 4.2, 68, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Mankind"]),
    ("888", "Saraswati Institute of Pharmacy Hapur", "Hapur", "Private", 2009, "B", "151-200 (Pharmacy)", 88000, 12.5, 4.4, 70, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Lupin"]),
    ("889", "JMS College of Pharmacy Hapur", "Hapur", "Private", 2011, "B+", "101-150 (Pharmacy)", 92000, 13.5, 4.5, 73, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Torrent"]),
    ("890", "Shree Ganpati Institute of Pharmacy Ghaziabad", "Ghaziabad", "Private", 2006, "B+", "101-150 (Pharmacy)", 95000, 14.0, 4.6, 74, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Alkem"]),
    ("891", "HR Institute of Pharmacy Ghaziabad", "Ghaziabad", "Private", 2006, "B+", "101-150 (Pharmacy)", 100000, 15.0, 4.8, 76, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "GSK"]),
    ("892", "Sanskar College of Pharmacy Ghaziabad", "Ghaziabad", "Private", 2006, "B+", "101-150 (Pharmacy)", 98000, 14.5, 4.7, 75, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Sun Pharma"]),
    ("893", "Sunder Deep Pharmacy College Ghaziabad", "Ghaziabad", "Private", 2007, "B+", "101-150 (Pharmacy)", 98000, 14.5, 4.7, 75, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Cipla"]),
    ("894", "Lord Krishna College of Pharmacy Ghaziabad", "Ghaziabad", "Private", 2007, "B", "151-200 (Pharmacy)", 90000, 12.5, 4.3, 70, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Mankind"]),
    ("895", "Accurate College of Pharmacy Greater Noida", "Greater Noida", "Private", 2007, "B+", "101-150 (Pharmacy)", 105000, 15.5, 4.9, 78, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Dr. Reddy's"]),
    ("896", "GNIOT Institute of Professional Studies Gr. Noida", "Greater Noida", "Private", 2008, "A", "101-150", 115000, 18.0, 5.5, 82, ["BBA", "BCA", "B.Com"], ["Amazon", "TCS", "Infosys", "Wipro"]),
    ("897", "GL Bajaj Group of Institutions Gr. Noida Campus", "Greater Noida", "Private", 2008, "A", "101-150", 120000, 20.0, 6.0, 84, ["BBA", "BCA", "MCA"], ["Amazon", "TCS", "Infosys", "Capgemini"]),
    ("898", "KCC Institute of Legal & Higher Education Gr. Noida", "Greater Noida", "Private", 2010, "B+", "301-400", 95000, 15.0, 5.0, 75, ["BBA", "BCA", "BA.LLB"], ["TCS", "Infosys", "Wipro", "HCL"]),
    ("899", "Dronacharya School of Management Gr. Noida", "Greater Noida", "Private", 2008, "B+", "301-400", 100000, 16.0, 5.2, 76, ["MBA", "BBA", "BCA"], ["TCS", "Infosys", "Wipro", "Capgemini"]),
    ("900", "IIMT College of Science & Technology Gr. Noida", "Greater Noida", "Private", 2008, "B+", "301-400", 102000, 16.5, 5.2, 77, ["BCA", "B.Sc CS", "MCA"], ["TCS", "Infosys", "Wipro", "HCL"]),
    ("901", "Lloyd Law College Greater Noida", "Greater Noida", "Private Autonomous", 2003, "A+", "10-25 (Law)", 185000, 24.0, 7.8, 92, ["BA.LLB", "BBA.LLB", "LLM"], ["Khaitan & Co", "Shardul Amarchand", "Luthra & Luthra", "AZB"]),
    ("902", "Mangalmay Institute of Management & Technology", "Greater Noida", "Private", 2002, "A", "151-200", 115000, 20.0, 6.0, 82, ["MBA", "BBA", "BCA"], ["Amazon", "TCS", "Infosys", "Wipro"]),
    ("903", "Skyline Business School Greater Noida", "Greater Noida", "Private", 2003, "B+", "301-400", 100000, 16.0, 5.2, 75, ["MBA", "PGDM", "BBA"], ["TCS", "Infosys", "Wipro", "HCL"]),
    ("904", "GNIT College of Pharmacy Greater Noida", "Greater Noida", "Private", 2008, "B+", "101-150 (Pharmacy)", 105000, 15.5, 4.9, 78, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Lupin"]),
    ("905", "IEC School of Pharmacy Greater Noida", "Greater Noida", "Private", 2005, "B+", "101-150 (Pharmacy)", 105000, 15.0, 4.8, 77, ["B.Pharm", "M.Pharm"], ["Cipla", "Sun Pharma", "Alkem"]),
    ("906", "Vivekananda College of Law & Management Aligarh", "Aligarh", "Private", 2009, "B", "401-500", 80000, 12.0, 4.3, 65, ["BBA", "BCA", "BA.LLB"], ["TCS", "Infosys", "Wipro"]),
    ("907", "Institute of Technology & Science (ITS Mohan Nagar)", "Ghaziabad", "Private Autonomous", 1995, "A+", "76-100", 145000, 28.0, 7.5, 90, ["MCA", "MBA", "BBA", "BCA"], ["Amazon", "TCS Digital", "Infosys SP", "Capgemini", "Wipro"]),
    ("908", "ITS Dental College Muradnagar Ghaziabad", "Ghaziabad", "Private", 2000, "A", "30-50 (Dental)", 310000, 18.0, 7.5, 92, ["BDS", "MDS"], ["Apollo", "Fortis", "Max Healthcare"]),
    ("909", "ITS Dental College Greater Noida", "Greater Noida", "Private", 2006, "A", "30-50 (Dental)", 305000, 17.5, 7.4, 91, ["BDS", "MDS"], ["Apollo", "Fortis", "Medanta"]),
    ("910", "ITS School of Management Greater Noida", "Greater Noida", "Private", 2007, "A", "101-150", 125000, 22.0, 6.5, 85, ["PGDM", "MBA"], ["Amazon", "TCS", "Infosys", "Flipkart", "HDFC"]),
    ("911", "IMS Law College Noida", "Noida", "Private", 2004, "A", "25-50 (Law)", 140000, 18.0, 6.2, 85, ["BA.LLB", "B.Com.LLB", "LLB"], ["Trilegal", "Shardul Amarchand", "Fox Mandal"]),
    ("912", "Jaipuria School of Business Indirapuram", "Ghaziabad", "Private", 2008, "A", "101-150", 160000, 25.0, 7.2, 88, ["PGDM", "MBA"], ["Deloitte", "KPMG", "EY", "Amazon", "HDFC"]),
    ("913", "INMANTEC Institutions Ghaziabad", "Ghaziabad", "Private", 1995, "B+", "301-400", 98000, 16.0, 5.2, 76, ["BBA", "BCA", "MCA", "MBA"], ["TCS", "Infosys", "Wipro", "HCL"]),
    ("914", "ABESIT College of Pharmacy Ghaziabad", "Ghaziabad", "Private", 2018, "A", "101-150 (Pharmacy)", 115000, 16.5, 5.2, 82, ["B.Pharm", "D.Pharm"], ["Cipla", "Sun Pharma", "Dr. Reddy's", "Lupin"])
]

count_added = 0
for item in final_batch:
    code, name, city, aff_type, est, naac, nirf, fee, h_pkg, avg_pkg, pct, branches, rec = item
    if code in existing_codes:
        continue
    
    slug_raw = re.sub(r'[^a-zA-Z0-9\s-]', '', name.lower()).strip()
    slug = re.sub(r'[\s]+', '-', slug_raw) + "-profile"
    
    # Check duplicate slug
    if any(x["slug"] == slug for x in master_colleges):
        slug = f"{slug}-{code.lower()}"
    
    master_colleges.append({
        "slug": slug,
        "code": code,
        "name": name,
        "city": city,
        "district": city,
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
    existing_codes.add(code)
    count_added += 1

print(f"Added {count_added} final batch institutes! TOTAL COLLEGES IN MASTER DATABASE: {len(master_colleges)}")

with open("scripts/flat_colleges.json", "w", encoding="utf-8") as f:
    json.dump(master_colleges, f, indent=2)

print("Updated flat_colleges.json successfully!")
