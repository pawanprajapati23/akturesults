import os, json, re
from bs4 import BeautifulSoup
from PIL import Image

print("=== STARTING MASTER CODEBASE & SEO REPAIR ===")

# 1. OPTIMIZE FAVICON
try:
    if os.path.exists("favicon.png"):
        img = Image.open("favicon.png")
        img.thumbnail((64, 64), Image.Resampling.LANCZOS)
        img.save("favicon.png", "PNG", optimize=True)
        print(f"Compressed favicon.png to {os.path.getsize('favicon.png')} bytes!")
except Exception as e:
    print(f"Favicon optimization note: {e}")

# 2. PROCESS ALL HTML FILES
total_scanned = 0
js_errors_fixed = 0
h1_fixed = 0
og_injected = 0
schema_injected = 0
redirect_noindex_added = 0

for root, dirs, files in os.walk("."):
    if any(p in root for p in [".git", ".system_generated", "node_modules", "scratch", "templates"]):
        continue
    for f in files:
        if not f.endswith(".html"):
            continue
        total_scanned += 1
        rel_path = os.path.relpath(os.path.join(root, f), ".").replace("\\", "/")
        if rel_path.startswith("./"): rel_path = rel_path[2:]
        full_path = os.path.join(root, f)

        try:
            with open(full_path, "r", encoding="utf-8", errors="ignore") as file_obj:
                content = file_obj.read()

            changed = False
            is_redirect = ("http-equiv=\"refresh\"" in content or "window.location.href" in content) and len(content) < 1500

            # Fix 1: Broken JS Syntax & Obsolete atOptions
            if "<script>.pop().appendChild(document.createElement('script')))</script>" in content:
                content = content.replace("<script>.pop().appendChild(document.createElement('script')))</script>", "")
                js_errors_fixed += 1
                changed = True

            # Strip atOptions blocks if corrupted
            if "atOptions = {" in content:
                content = re.sub(r'<script>\s*atOptions\s*=\s*\{.*?\};\s*</script>', '', content, flags=re.DOTALL)
                changed = True

            soup = BeautifulSoup(content, "html.parser")
            if not soup.head:
                continue

            # Fix 2: Header H1 to DIV / SPAN
            header = soup.find("header")
            if header:
                h1_in_header = header.find("h1")
                if h1_in_header:
                    h1_in_header.name = "div"
                    h1_fixed += 1
                    changed = True

            # Fix 3: Robots noindex for redirect stubs
            if is_redirect:
                if not soup.find("meta", attrs={"name": "robots"}):
                    robots_tag = soup.new_tag("meta", attrs={"name": "robots", "content": "noindex, follow"})
                    soup.head.append(robots_tag)
                    redirect_noindex_added += 1
                    changed = True

            # Extract Title & Description for OG Tags
            title_tag = soup.find("title")
            page_title = title_tag.text.strip() if title_tag else "AKTU Results & Student Portal"
            desc_tag = soup.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
            page_desc = desc_tag["content"].strip() if desc_tag and desc_tag.get("content") else f"Official student resources and information for {page_title} on AKTU Results Portal."
            canon_tag = soup.find("link", attrs={"rel": "canonical"})
            page_url = canon_tag["href"].strip() if canon_tag and canon_tag.get("href") else f"https://akturesults.in/{rel_path}"

            # Fix 4: OpenGraph & Twitter Cards
            if not soup.find("meta", attrs={"property": "og:title"}):
                og_t = soup.new_tag("meta", attrs={"property": "og:title", "content": page_title})
                og_d = soup.new_tag("meta", attrs={"property": "og:description", "content": page_desc})
                og_u = soup.new_tag("meta", attrs={"property": "og:url", "content": page_url})
                og_type = soup.new_tag("meta", attrs={"property": "og:type", "content": "website"})
                og_img = soup.new_tag("meta", attrs={"property": "og:image", "content": "https://akturesults.in/images/og-banner.png"})
                tw_card = soup.new_tag("meta", attrs={"name": "twitter:card", "content": "summary_large_image"})

                for tag in [og_t, og_d, og_u, og_type, og_img, tw_card]:
                    soup.head.append(tag)
                og_injected += 1
                changed = True

            # Fix 5: Schema.org Structured Data
            existing_schemas = soup.find_all("script", type="application/ld+json")
            if len(existing_schemas) == 0 and not is_redirect:
                # Determine schema type based on section
                if rel_path.startswith("syllabus/"):
                    schema_data = {
                        "@context": "https://schema.org",
                        "@type": "Course",
                        "name": page_title,
                        "description": page_desc,
                        "provider": {
                            "@type": "EducationalOrganization",
                            "name": "Dr. A.P.J. Abdul Kalam Technical University (AKTU)",
                            "sameAs": "https://aktu.ac.in"
                        }
                    }
                elif rel_path.startswith("tools/"):
                    schema_data = {
                        "@context": "https://schema.org",
                        "@type": "WebApplication",
                        "name": page_title,
                        "description": page_desc,
                        "applicationCategory": "EducationalApplication",
                        "operatingSystem": "All"
                    }
                elif rel_path.startswith("results/") or rel_path.startswith("exams/"):
                    schema_data = {
                        "@context": "https://schema.org",
                        "@type": "EducationalEvent",
                        "name": page_title,
                        "description": page_desc,
                        "organizer": {
                            "@type": "EducationalOrganization",
                            "name": "AKTU Lucknow"
                        }
                    }
                else:
                    schema_data = {
                        "@context": "https://schema.org",
                        "@type": "WebPage",
                        "name": page_title,
                        "description": page_desc,
                        "url": page_url
                    }

                sc_tag = soup.new_tag("script", type="application/ld+json")
                sc_tag.string = json.dumps(schema_data)
                soup.head.append(sc_tag)
                schema_injected += 1
                changed = True

            if changed:
                with open(full_path, "w", encoding="utf-8") as out:
                    out.write(str(soup))

        except Exception as e:
            print(f"Error repairing {rel_path}: {e}")

print(f"\n=== MASTER REPAIR COMPLETE ===")
print(f"Total HTML files scanned: {total_scanned}")
print(f"1. Broken JS syntax errors eradicated: {js_errors_fixed}")
print(f"2. Header H1 conflicts normalized: {h1_fixed}")
print(f"3. OpenGraph / Twitter Cards injected: {og_injected}")
print(f"4. Missing Schema.org JSON-LD generated: {schema_injected}")
print(f"5. Noindex added to redirect stubs: {redirect_noindex_added}")
