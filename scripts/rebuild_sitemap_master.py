import os, datetime

BASE_URL = "https://akturesults.in"
now_date = datetime.date.today().isoformat()

pages = []

# Scan all html files
for root, dirs, files in os.walk("."):
    if ".git" in root or ".system_generated" in root or "node_modules" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            rel_path = os.path.relpath(os.path.join(root, file), ".").replace("\\", "/")
            if rel_path.startswith("./"):
                rel_path = rel_path[2:]
            
            # Skip test or scratch files if any
            if "scratch" in rel_path or "test" in rel_path:
                continue

            if rel_path == "index.html":
                url = f"{BASE_URL}/"
                priority = "1.0"
                changefreq = "daily"
            elif rel_path.startswith("colleges/profiles/"):
                url = f"{BASE_URL}/{rel_path}"
                priority = "0.9"
                changefreq = "weekly"
            elif rel_path.startswith("colleges/codes/"):
                url = f"{BASE_URL}/{rel_path}"
                priority = "0.8"
                changefreq = "monthly"
            elif "predictor" in rel_path or "calculator" in rel_path or "filter-directory" in rel_path:
                url = f"{BASE_URL}/{rel_path}"
                priority = "0.9"
                changefreq = "daily"
            elif "district" in rel_path:
                url = f"{BASE_URL}/{rel_path}"
                priority = "0.85"
                changefreq = "weekly"
            else:
                url = f"{BASE_URL}/{rel_path}"
                priority = "0.8"
                changefreq = "weekly"

            pages.append((url, priority, changefreq))

pages.sort(key=lambda x: x[0])

xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

for url, priority, changefreq in pages:
    xml_lines.append("  <url>")
    xml_lines.append(f"    <loc>{url}</loc>")
    xml_lines.append(f"    <lastmod>{now_date}</lastmod>")
    xml_lines.append(f"    <changefreq>{changefreq}</changefreq>")
    xml_lines.append(f"    <priority>{priority}</priority>")
    xml_lines.append("  </url>")

xml_lines.append("</urlset>")

sitemap_content = "\n".join(xml_lines)
with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"Master sitemap.xml generated with {len(pages)} indexed URLs!")
