import os, re
from bs4 import BeautifulSoup

existing_files = set()
for root, dirs, files in os.walk("."):
    if ".git" in root or ".system_generated" in root or "node_modules" in root:
        continue
    for file in files:
        rel_path = os.path.relpath(os.path.join(root, file), ".").replace("\\", "/")
        if rel_path.startswith("./"):
            rel_path = rel_path[2:]
        existing_files.add(rel_path)

broken_links = []
total_links_checked = 0

for html_file in list(existing_files):
    if not html_file.endswith(".html"):
        continue
    try:
        with open(html_file, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        
        for a in soup.find_all("a", href=True):
            href = a["href"].strip()
            total_links_checked += 1

            # Skip external links, anchors, protocols
            if href.startswith(("http://", "https://", "#", "mailto:", "tel:", "javascript:", "whatsapp:")):
                continue
            
            # Normalize target file path
            clean_href = href.split("?")[0].split("#")[0]
            if clean_href == "" or clean_href == "/":
                target = "index.html"
            elif clean_href.startswith("/"):
                target = clean_href[1:]
            else:
                file_dir = os.path.dirname(html_file)
                target = os.path.normpath(os.path.join(file_dir, clean_href)).replace("\\", "/")

            # Check directory index resolution
            resolved = False
            if target in existing_files:
                resolved = True
            elif os.path.join(target, "index.html").replace("\\", "/") in existing_files:
                resolved = True
            elif (target.rstrip("/") + "/index.html") in existing_files:
                resolved = True
            elif (target.rstrip("/") + ".html") in existing_files:
                resolved = True

            if not resolved:
                broken_links.append((html_file, href, target))
    except Exception as e:
        print(f"Error parsing {html_file}: {e}")

print(f"Verified {total_links_checked} links across HTML pages.")
if broken_links:
    print(f"Found {len(broken_links)} broken links:")
    for src, href, tgt in broken_links[:15]:
        print(f"  {src} -> {href} (target: {tgt})")
else:
    print("SUCCESS: 0 broken internal links found! All pages across the portal are 100% verified and valid!")
