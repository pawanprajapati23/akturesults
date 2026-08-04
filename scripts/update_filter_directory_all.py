import json, re

from build_all_aktu_colleges import colleges_master

directory_items = []
for c in colleges_master:
    directory_items.append({
        "name": c["name"],
        "code": c["code"],
        "city": c["city"],
        "type": c["type"],
        "est": c["est"],
        "naac": c["naac"],
        "nirf": c["nirf"],
        "fee": c["fee"],
        "highest_pkg": c["h_pkg"],
        "avg_pkg": c["avg_pkg"],
        "placement_pct": c["pct"],
        "branches": c["branches"],
        "recruiters": c["rec"],
        "url": f"/colleges/profiles/{c['slug']}.html"
    })

json_str = json.dumps(directory_items, indent=2)

with open('colleges/aktu-colleges-filter-directory.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the collegesData constant
new_content = re.sub(r'const collegesData = \[.*?\];', f'const collegesData = {json_str};', content, flags=re.DOTALL)

with open('colleges/aktu-colleges-filter-directory.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Updated colleges/aktu-colleges-filter-directory.html with all {len(directory_items)} colleges!")
