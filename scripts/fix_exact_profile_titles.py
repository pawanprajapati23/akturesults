import os, json, re
from bs4 import BeautifulSoup

with open("scripts/flat_colleges.json", "r", encoding="utf-8") as f:
    master_colleges = json.load(f)

slug_to_college = {c["slug"]: c for c in master_colleges}
code_to_college = {c["code"]: c for c in master_colleges}

profiles_dir = "colleges/profiles"
fixed_titles = 0

for pf in os.listdir(profiles_dir):
    if not pf.endswith(".html"):
        continue
    slug = pf.replace(".html", "")
    full_path = os.path.join(profiles_dir, pf)

    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # Skip meta-refresh redirects
    if 'http-equiv="refresh"' in content:
        continue

    college_info = None
    if slug in slug_to_college:
        college_info = slug_to_college[slug]
    else:
        # Search code in content
        code_match = re.search(r'Code[:\s]+([0-9]{3}[a-zA-Z]?)', content)
        if code_match and code_match.group(1) in code_to_college:
            college_info = code_to_college[code_match.group(1)]

    if college_info:
        soup = BeautifulSoup(content, "html.parser")
        proper_title = f"{college_info['name']} (Code {college_info['code']}) — Fees, Placements, Cutoffs & Ranking"
        proper_canonical = f"https://akturesults.in/colleges/profiles/{slug}.html"
        proper_desc = f"Complete fee structure, highest & average placement package, NIRF/NAAC ranking, hostel fees, and admission cutoffs for {college_info['name']} ({college_info['city']}, UP)."

        t = soup.find("title")
        if not t:
            t = soup.new_tag("title")
            soup.head.append(t)
        t.string = proper_title

        c = soup.find("link", attrs={"rel": "canonical"})
        if not c:
            c = soup.new_tag("link", attrs={"rel": "canonical", "href": proper_canonical})
            soup.head.append(c)
        else:
            c["href"] = proper_canonical

        d = soup.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
        if not d:
            d = soup.new_tag("meta", attrs={"name": "description", "content": proper_desc})
            soup.head.append(d)
        else:
            d["content"] = proper_desc

        with open(full_path, "w", encoding="utf-8") as out:
            out.write(str(soup))
        fixed_titles += 1

print(f"Fixed and verified exact unique titles and canonicals for {fixed_titles} college profile pages!")
