import os
import re
import datetime
import xml.etree.ElementTree as ET

BASE_DIR = "/home/techiedevang/akturesults"

ANALYTICS_SNIPPET = """    <!-- ===== ANALYTICS ===== -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-83VE8HR3T8"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-83VE8HR3T8');
    </script>
    <script defer src="/_vercel/insights/script.js"></script>
    <script defer src="/_vercel/speed-insights/script.js"></script>
"""

# 1. Update 40 dummy subject files to noindex, nofollow
dummy_subjects_pattern = re.compile(r"subject-bcs-3(2[1-9]|[3-5][0-9]|60)")
dummy_count = 0

for root, dirs, files in os.walk(BASE_DIR):
    if any(p in root for p in [".git", "node_modules"]):
        continue
    for f in files:
        if f.endswith(".html") and dummy_subjects_pattern.search(f):
            filepath = os.path.join(root, f)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            # replace robots
            new_content = re.sub(
                r'<meta\s+content=["\']index,\s*follow["\']\s+name=["\']robots["\']\s*/?>',
                '<meta content="noindex, nofollow" name="robots"/>',
                content,
                flags=re.IGNORECASE
            )
            new_content = re.sub(
                r'<meta\s+name=["\']robots["\']\s+content=["\']index,\s*follow["\']\s*/?>',
                '<meta name="robots" content="noindex, nofollow"/>',
                new_content,
                flags=re.IGNORECASE
            )
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(new_content)
                dummy_count += 1

print(f"Updated {dummy_count} dummy subject files with noindex, nofollow.")

# 2. Inject Analytics to all HTML files
injected_count = 0
already_had_count = 0

for root, dirs, files in os.walk(BASE_DIR):
    if any(p in root for p in [".git", "node_modules", "templates"]):
        continue
    for f in files:
        if f.endswith(".html"):
            filepath = os.path.join(root, f)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
                content = file.read()
            
            # check if GA4 is present
            has_ga = "G-83VE8HR3T8" in content
            has_vercel = "/_vercel/insights" in content
            
            if has_ga and has_vercel:
                already_had_count += 1
                continue
            
            # If partially present or not present, ensure standard snippet is inside <head>
            if not has_ga:
                if "</head>" in content:
                    content = content.replace("</head>", f"{ANALYTICS_SNIPPET}</head>", 1)
                elif "<head>" in content:
                    content = content.replace("<head>", f"<head>\n{ANALYTICS_SNIPPET}", 1)
                injected_count += 1
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(content)
            elif not has_vercel:
                # Add vercel scripts before </head>
                v_scripts = """    <script defer src="/_vercel/insights/script.js"></script>\n    <script defer src="/_vercel/speed-insights/script.js"></script>\n"""
                content = content.replace("</head>", f"{v_scripts}</head>", 1)
                injected_count += 1
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(content)

print(f"Analytics Injection: {injected_count} files injected, {already_had_count} already had full tracking.")

# 3. Rebuild clean XML sitemaps excluding dummy pages & 404s
today = datetime.datetime.now().strftime("%Y-%m-%d")

core_pages = []
college_pages = []
syllabus_pages = []
all_pages = []

for root, dirs, files in os.walk(BASE_DIR):
    if any(p in root for p in [".git", ".system_generated", "node_modules", "scratch", "templates"]):
        continue
    for f in files:
        if f.endswith(".html"):
            rel = os.path.relpath(os.path.join(root, f), BASE_DIR).replace("\\", "/")
            if rel.startswith("./"): rel = rel[2:]
            
            # Skip 404, templates, and dummy subjects
            if rel == "404.html" or rel.startswith("templates/"):
                continue
            if dummy_subjects_pattern.search(rel):
                continue
                
            if rel == "index.html":
                url = "https://akturesults.in/"
                priority = "1.0"
                changefreq = "daily"
            elif rel.startswith("tools/") or rel in ["grade-calculator.html", "attendance-calculator.html", "calculators.html", "check-result.html"]:
                url = f"https://akturesults.in/{rel}"
                priority = "0.9"
                changefreq = "weekly"
            elif rel.startswith("colleges/profiles/"):
                url = f"https://akturesults.in/{rel}"
                priority = "0.8"
                changefreq = "monthly"
            elif rel.startswith("syllabus/") or rel.startswith("notes/"):
                url = f"https://akturesults.in/{rel}"
                priority = "0.8"
                changefreq = "monthly"
            elif rel.startswith("admissions/") or rel.startswith("results/") or rel.startswith("exams/") or rel.startswith("placements/"):
                url = f"https://akturesults.in/{rel}"
                priority = "0.8"
                changefreq = "weekly"
            else:
                url = f"https://akturesults.in/{rel}"
                priority = "0.7"
                changefreq = "monthly"
                
            entry = {"url": url, "lastmod": today, "changefreq": changefreq, "priority": priority}
            all_pages.append(entry)
            
            if rel.startswith("colleges/"):
                college_pages.append(entry)
            elif rel.startswith("syllabus/"):
                syllabus_pages.append(entry)
            else:
                core_pages.append(entry)

def generate_urlset_xml(pages, filepath):
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
    full_path = os.path.join(BASE_DIR, filepath)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(xml_str)
    print(f"Generated {filepath} ({len(pages)} URLs) - Valid XML.")

generate_urlset_xml(all_pages, "sitemap.xml")
generate_urlset_xml(all_pages, "sitemap-all.xml")
generate_urlset_xml(core_pages, "sitemap-main.xml")
generate_urlset_xml(college_pages, "sitemap-colleges.xml")
generate_urlset_xml(syllabus_pages, "sitemap-syllabus.xml")

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
with open(os.path.join(BASE_DIR, "sitemap_index.xml"), "w", encoding="utf-8") as f:
    f.write(index_xml)
print("Generated sitemap_index.xml - Valid XML Index.")
