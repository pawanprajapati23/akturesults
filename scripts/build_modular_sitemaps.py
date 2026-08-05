import os, datetime, xml.sax.saxutils
import xml.etree.ElementTree as ET

today = datetime.datetime.now().strftime("%Y-%m-%d")

# Collect pages by category
core_pages = []
college_pages = []
syllabus_pages = []
all_pages = []

for root, dirs, files in os.walk("."):
    if any(p in root for p in [".git", ".system_generated", "node_modules", "scratch", "templates"]):
        continue
    for f in files:
        if f.endswith(".html"):
            rel = os.path.relpath(os.path.join(root, f), ".").replace("\\", "/")
            if rel.startswith("./"): rel = rel[2:]
            
            if rel == "404.html" or rel.startswith("templates/"):
                continue
                
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
                
            item = (url, priority, changefreq)
            all_pages.append(item)
            
            if rel.startswith("colleges/"):
                college_pages.append(item)
            elif rel.startswith("syllabus/") or rel.startswith("notes/"):
                syllabus_pages.append(item)
            else:
                core_pages.append(item)

def generate_urlset_xml(pages, filepath):
    pages.sort(key=lambda x: x[0])
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for url, priority, changefreq in pages:
        safe_url = xml.sax.saxutils.escape(url)
        lines.append('  <url>')
        lines.append(f'    <loc>{safe_url}</loc>')
        lines.append(f'    <lastmod>{today}</lastmod>')
        lines.append(f'    <changefreq>{changefreq}</changefreq>')
        lines.append(f'    <priority>{priority}</priority>')
        lines.append('  </url>')
    lines.append('</urlset>')
    
    xml_str = "\n".join(lines)
    # Strict validation
    ET.fromstring(xml_str)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(xml_str)
    print(f"Generated {filepath} ({len(pages)} URLs) - 100% Valid XML!")

# 1. Generate child sitemaps
generate_urlset_xml(all_pages, "sitemap.xml")
generate_urlset_xml(all_pages, "sitemap-all.xml")
generate_urlset_xml(core_pages, "sitemap-main.xml")
generate_urlset_xml(college_pages, "sitemap-colleges.xml")
generate_urlset_xml(syllabus_pages, "sitemap-syllabus.xml")

# 2. Generate standard sitemap_index.xml
sitemaps_list = [
    "https://akturesults.in/sitemap-main.xml",
    "https://akturesults.in/sitemap-colleges.xml",
    "https://akturesults.in/sitemap-syllabus.xml",
    "https://akturesults.in/sitemap-all.xml"
]

index_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]
for sm in sitemaps_list:
    index_lines.append('  <sitemap>')
    index_lines.append(f'    <loc>{sm}</loc>')
    index_lines.append(f'    <lastmod>{today}</lastmod>')
    index_lines.append('  </sitemap>')
index_lines.append('</sitemapindex>')

index_xml = "\n".join(index_lines)
ET.fromstring(index_xml)
with open("sitemap_index.xml", "w", encoding="utf-8") as f:
    f.write(index_xml)
print("Generated sitemap_index.xml - 100% Valid XML Index!")

# Update robots.txt
robots_content = f"""User-agent: *
Allow: /

User-agent: Mediapartners-Google
Allow: /

Sitemap: https://akturesults.in/sitemap.xml
Sitemap: https://akturesults.in/sitemap_index.xml
Sitemap: https://akturesults.in/sitemap-main.xml
Sitemap: https://akturesults.in/sitemap-colleges.xml
Sitemap: https://akturesults.in/sitemap-syllabus.xml
"""

with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)
print("Updated robots.txt with all sitemaps!")

