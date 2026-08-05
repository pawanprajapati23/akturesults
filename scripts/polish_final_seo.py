import os, json, shutil
from bs4 import BeautifulSoup

# 1. Move component snippets to templates/components
os.makedirs("templates/components", exist_ok=True)
for snippet in ["adsense-integration.html", "floating-action-button.html", "social-share-widget.html"]:
    if os.path.exists(snippet):
        shutil.move(snippet, os.path.join("templates/components", snippet))
        print(f"Moved {snippet} to templates/components/")

# 2. Add EducationalOrganization Schema JSON-LD to any code redirect bridge if missing
code_bridges = [f for f in os.listdir("colleges/codes") if f.endswith(".html")]
for cb in code_bridges:
    p = os.path.join("colleges/codes", cb)
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    if 'application/ld+json' not in content:
        soup = BeautifulSoup(content, "html.parser")
        code_num = cb.replace("code-", "").replace(".html", "").upper()
        schema_json = {
            "@context": "https://schema.org",
            "@type": "EducationalOrganization",
            "name": f"AKTU Institute Code {code_num}",
            "url": f"https://akturesults.in/colleges/codes/{cb}"
        }
        sc_tag = soup.new_tag("script", type="application/ld+json")
        sc_tag.string = json.dumps(schema_json)
        if soup.head:
            soup.head.append(sc_tag)
            with open(p, "w", encoding="utf-8") as out:
                out.write(str(soup))

print("Polished all code bridge structured data!")
