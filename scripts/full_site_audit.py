import os, json, re
from bs4 import BeautifulSoup
from collections import defaultdict

total_files = 0
missing_title = []
missing_desc = []
missing_canonical = []
missing_viewport = []
missing_h1 = []
multiple_h1 = []
missing_jsonld = []
invalid_jsonld = []
missing_ad_monetag = []
titles_map = defaultdict(list)
desc_map = defaultdict(list)
canonical_map = defaultdict(list)

for root, dirs, files in os.walk("."):
    if ".git" in root or ".system_generated" in root or "node_modules" in root or "scratch" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            total_files += 1
            rel_path = os.path.relpath(os.path.join(root, f), ".").replace("\\", "/")
            if rel_path.startswith("./"): rel_path = rel_path[2:]

            try:
                with open(rel_path, "r", encoding="utf-8", errors="ignore") as file_obj:
                    content = file_obj.read()
                    soup = BeautifulSoup(content, "html.parser")

                # 1. Title check
                title_tag = soup.find("title")
                if not title_tag or not title_tag.text.strip():
                    missing_title.append(rel_path)
                else:
                    t_text = title_tag.text.strip()
                    titles_map[t_text].append(rel_path)

                # 2. Meta description check
                desc_tag = soup.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
                if not desc_tag or not desc_tag.get("content", "").strip():
                    missing_desc.append(rel_path)
                else:
                    d_text = desc_tag["content"].strip()
                    desc_map[d_text].append(rel_path)

                # 3. Canonical tag check
                canon_tag = soup.find("link", attrs={"rel": "canonical"})
                if not canon_tag or not canon_tag.get("href", "").strip():
                    missing_canonical.append(rel_path)
                else:
                    canonical_map[canon_tag["href"].strip()].append(rel_path)

                # 4. Viewport check
                vp_tag = soup.find("meta", attrs={"name": re.compile(r"^viewport$", re.I)})
                if not vp_tag:
                    missing_viewport.append(rel_path)

                # 5. H1 checks (skip redirect bridge files)
                if not ("Redirecting" in content and "http-equiv=\"refresh\"" in content):
                    h1_tags = soup.find_all("h1")
                    if len(h1_tags) == 0:
                        missing_h1.append(rel_path)
                    elif len(h1_tags) > 1:
                        multiple_h1.append((rel_path, len(h1_tags)))

                # 6. JSON-LD Structured Data
                json_ld_scripts = soup.find_all("script", type="application/ld+json")
                if len(json_ld_scripts) == 0 and not ("http-equiv=\"refresh\"" in content):
                    missing_jsonld.append(rel_path)
                else:
                    for j_tag in json_ld_scripts:
                        try:
                            if j_tag.string:
                                json.loads(j_tag.string)
                        except Exception as je:
                            invalid_jsonld.append((rel_path, str(je)))

                # 7. Ad Monetization
                if "monetag" not in content and not ("http-equiv=\"refresh\"" in content):
                    missing_ad_monetag.append(rel_path)

            except Exception as e:
                print(f"Error reading {rel_path}: {e}")

# Duplicate analysis
duplicate_titles = {k: v for k, v in titles_map.items() if len(v) > 1}
duplicate_descs = {k: v for k, v in desc_map.items() if len(v) > 1}
duplicate_canonicals = {k: v for k, v in canonical_map.items() if len(v) > 1}

print("==============================================")
print(f"       FULL SITE AUDIT REPORT (Total: {total_files} HTML pages)")
print("==============================================")
print(f"1. Missing Titles: {len(missing_title)}")
print(f"2. Missing Meta Descriptions: {len(missing_desc)}")
print(f"3. Missing Canonical Links: {len(missing_canonical)}")
print(f"4. Missing Viewport Tags: {len(missing_viewport)}")
print(f"5. Pages Missing H1: {len(missing_h1)}")
print(f"6. Pages with Multiple H1s: {len(multiple_h1)}")
print(f"7. Pages Missing Schema JSON-LD: {len(missing_jsonld)}")
print(f"8. Invalid JSON-LD Syntax: {len(invalid_jsonld)}")
print(f"9. Pages Missing Monetag/Ads: {len(missing_ad_monetag)}")
print(f"10. Duplicate Title Sets: {len(duplicate_titles)}")
print(f"11. Duplicate Description Sets: {len(duplicate_descs)}")
print(f"12. Duplicate Canonical Sets: {len(duplicate_canonicals)}")
print("==============================================")

if duplicate_titles:
    print("\nSample Duplicate Titles (Top 5):")
    for k, v in list(duplicate_titles.items())[:5]:
        print(f"  - \"{k}\" -> {len(v)} occurrences (e.g. {v[:2]})")

if duplicate_canonicals:
    print("\nSample Duplicate Canonicals (Top 5):")
    for k, v in list(duplicate_canonicals.items())[:5]:
        print(f"  - \"{k}\" -> {len(v)} occurrences (e.g. {v[:2]})")

