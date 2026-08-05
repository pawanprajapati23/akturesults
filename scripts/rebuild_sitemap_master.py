import os, datetime, xml.sax.saxutils
import xml.etree.ElementTree as ET

today = datetime.datetime.now().strftime("%Y-%m-%d")

# Find all HTML files
valid_pages = []
for root, dirs, files in os.walk("."):
    if any(p in root for p in [".git", ".system_generated", "node_modules", "scratch", "templates"]):
        continue
    for f in files:
        if f.endswith(".html"):
            rel = os.path.relpath(os.path.join(root, f), ".").replace("\\", "/")
            if rel.startswith("./"): rel = rel[2:]
            
            # Skip 404 and template snippets
            if rel == "404.html" or rel.startswith("templates/"):
                continue
                
            # Determine priority & frequency
            if rel == "index.html":
                url = "https://akturesults.in/"
                priority = "1.0"
                changefreq = "daily"
            elif rel.startswith("tools/") or rel == "grade-calculator.html" or rel == "attendance-calculator.html" or rel == "calculators.html":
                url = f"https://akturesults.in/{rel}"
                priority = "0.9"
                changefreq = "weekly"
            elif rel.startswith("colleges/profiles/"):
                url = f"https://akturesults.in/{rel}"
                priority = "0.9"
                changefreq = "weekly"
            elif rel.startswith("syllabus/") or rel.startswith("notes/"):
                url = f"https://akturesults.in/{rel}"
                priority = "0.8"
                changefreq = "weekly"
            elif rel.startswith("admissions/") or rel.startswith("results/") or rel.startswith("exams/") or rel.startswith("placements/"):
                url = f"https://akturesults.in/{rel}"
                priority = "0.8"
                changefreq = "weekly"
            elif rel.startswith("colleges/codes/"):
                url = f"https://akturesults.in/{rel}"
                priority = "0.7"
                changefreq = "monthly"
            else:
                url = f"https://akturesults.in/{rel}"
                priority = "0.7"
                changefreq = "monthly"
                
            valid_pages.append((url, priority, changefreq))

valid_pages.sort(key=lambda x: x[0])

xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

for url, priority, changefreq in valid_pages:
    safe_url = xml.sax.saxutils.escape(url)
    xml_lines.append('  <url>')
    xml_lines.append(f'    <loc>{safe_url}</loc>')
    xml_lines.append(f'    <lastmod>{today}</lastmod>')
    xml_lines.append(f'    <changefreq>{changefreq}</changefreq>')
    xml_lines.append(f'    <priority>{priority}</priority>')
    xml_lines.append('  </url>')

xml_lines.append('</urlset>')
xml_content = "\n".join(xml_lines)

# Validate XML parsing
try:
    root_el = ET.fromstring(xml_content)
    print(f"XML Validation PASSED: {len(root_el)} URLs parsed successfully with zero errors!")
    with open("sitemap.xml", "w", encoding="utf-8") as out:
        out.write(xml_content)
    print(f"Master sitemap.xml generated and saved with {len(valid_pages)} clean, valid URLs!")
except Exception as e:
    print(f"FATAL XML PARSER ERROR: {e}")
    raise e
