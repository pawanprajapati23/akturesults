import os, json, re
from bs4 import BeautifulSoup

# 1. Identify and fix missing titles, meta descriptions, canonicals, viewports
fixed_count = 0

for root, dirs, files in os.walk("."):
    if ".git" in root or ".system_generated" in root or "node_modules" in root or "scratch" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            rel_path = os.path.relpath(os.path.join(root, f), ".").replace("\\", "/")
            if rel_path.startswith("./"): rel_path = rel_path[2:]

            with open(rel_path, "r", encoding="utf-8", errors="ignore") as file_obj:
                content = file_obj.read()

            soup = BeautifulSoup(content, "html.parser")
            changed = False

            # Check Viewport
            if not soup.find("meta", attrs={"name": re.compile(r"^viewport$", re.I)}):
                if soup.head:
                    vp = soup.new_tag("meta", attrs={"name": "viewport", "content": "width=device-width, initial-scale=1.0"})
                    soup.head.insert(0, vp)
                    changed = True

            # Check Title
            title_tag = soup.find("title")
            if not title_tag or not title_tag.text.strip():
                clean_name = f.replace("-", " ").replace(".html", "").title()
                if not title_tag:
                    title_tag = soup.new_tag("title")
                    if soup.head:
                        soup.head.append(title_tag)
                title_tag.string = f"{clean_name} — AKTU Portal"
                changed = True

            # Check Meta Description
            desc_tag = soup.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
            if not desc_tag or not desc_tag.get("content", "").strip():
                title_text = title_tag.text.strip() if title_tag else f.replace("-", " ").replace(".html", "")
                if not desc_tag:
                    desc_tag = soup.new_tag("meta", attrs={"name": "description", "content": f"Official resources, syllabus, updates, and student tools for {title_text} on AKTU Results Portal."})
                    if soup.head:
                        soup.head.append(desc_tag)
                else:
                    desc_tag["content"] = f"Official resources, syllabus, updates, and student tools for {title_text} on AKTU Results Portal."
                changed = True

            # Check Canonical
            canon_tag = soup.find("link", attrs={"rel": "canonical"})
            if not canon_tag or not canon_tag.get("href", "").strip():
                if not canon_tag:
                    canon_tag = soup.new_tag("link", attrs={"rel": "canonical", "href": f"https://akturesults.in/{rel_path}"})
                    if soup.head:
                        soup.head.append(canon_tag)
                else:
                    canon_tag["href"] = f"https://akturesults.in/{rel_path}"
                changed = True

            # Check Monetag
            if "monetag" not in content and not ("http-equiv=\"refresh\"" in content):
                if soup.head:
                    monetag_meta = soup.new_tag("meta", attrs={"name": "monetag", "content": "4b20c6816d7cac00b3d6430a41d4d86f"})
                    soup.head.append(monetag_meta)
                    changed = True

            if changed:
                with open(rel_path, "w", encoding="utf-8") as out_f:
                    out_f.write(str(soup))
                fixed_count += 1

print(f"Audited and auto-patched SEO tags in {fixed_count} HTML files!")
