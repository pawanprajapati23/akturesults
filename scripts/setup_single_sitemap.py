import os
import re
import datetime
import xml.etree.ElementTree as ET

BASE_DIR = "/home/techiedevang/akturesults"

# 1. Remove all other sitemaps
extra_sitemaps = [
    "sitemap-main.xml",
    "sitemap-colleges.xml",
    "sitemap-syllabus.xml",
    "sitemap-all.xml",
    "sitemap_index.xml"
]
for sm in extra_sitemaps:
    path = os.path.join(BASE_DIR, sm)
    if os.path.exists(path):
        os.remove(path)
        print(f"Deleted {sm}")

# 2. Build single master sitemap.xml with www.akturesults.in
today = datetime.datetime.now().strftime("%Y-%m-%d")
dummy_subjects_pattern = re.compile(r"subject-bcs-3(2[1-9]|[3-5][0-9]|60)")

pages = []
for root, dirs, files in os.walk(BASE_DIR):
    if any(p in root for p in [".git", ".system_generated", "node_modules", "scratch", "templates"]):
        continue
    for f in files:
        if f.endswith(".html"):
            rel = os.path.relpath(os.path.join(root, f), BASE_DIR).replace("\\", "/")
            if rel.startswith("./"):
                rel = rel[2:]
            
            if rel == "404.html" or rel.startswith("templates/"):
                continue
            if dummy_subjects_pattern.search(rel):
                continue
                
            if rel == "index.html":
                url = "https://www.akturesults.in/"
                priority = "1.0"
                changefreq = "daily"
            elif rel.startswith("tools/") or rel in ["grade-calculator.html", "attendance-calculator.html", "calculators.html", "check-result.html"]:
                url = f"https://www.akturesults.in/{rel}"
                priority = "0.9"
                changefreq = "weekly"
            elif rel.startswith("colleges/profiles/"):
                url = f"https://www.akturesults.in/{rel}"
                priority = "0.8"
                changefreq = "monthly"
            elif rel.startswith("syllabus/") or rel.startswith("notes/"):
                url = f"https://www.akturesults.in/{rel}"
                priority = "0.8"
                changefreq = "monthly"
            elif rel.startswith("admissions/") or rel.startswith("results/") or rel.startswith("exams/") or rel.startswith("placements/"):
                url = f"https://www.akturesults.in/{rel}"
                priority = "0.8"
                changefreq = "weekly"
            else:
                url = f"https://www.akturesults.in/{rel}"
                priority = "0.7"
                changefreq = "monthly"
                
            pages.append({"url": url, "lastmod": today, "changefreq": changefreq, "priority": priority})

lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]
for p in pages:
    lines.append('  <url>')
    lines.append(f'    <loc>{p["url"]}</loc>')
    lines.append(f'    <lastmod>{p["lastmod"]}</lastmod>')
    lines.append(f'    <changefreq>{p["changefreq"]}</changefreq>')
    lines.append(f'    <priority>{p["priority"]}</priority>')
    lines.append('  </url>')
lines.append('</urlset>')

xml_str = "\n".join(lines)
ET.fromstring(xml_str)
sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(xml_str)
print(f"Generated single master sitemap.xml with {len(pages)} URLs - 100% Valid XML!")

# 3. Update canonical tags and URLs from https://akturesults.in to https://www.akturesults.in in all HTML files
updated_html_count = 0
for root, dirs, files in os.walk(BASE_DIR):
    if any(p in root for p in [".git", "node_modules"]):
        continue
    for f in files:
        if f.endswith(".html"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            # Avoid duplicate www
            new_content = re.sub(r"https://(?<!www\.)akturesults\.in", "https://www.akturesults.in", content)
            new_content = new_content.replace("https://www.www.akturesults.in", "https://www.akturesults.in")
            
            if new_content != content:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(new_content)
                updated_html_count += 1

print(f"Updated {updated_html_count} HTML files to use https://www.akturesults.in canonical and URLs!")
