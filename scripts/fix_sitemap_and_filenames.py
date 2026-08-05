import os, re, xml.sax.saxutils
import xml.etree.ElementTree as ET

# 1. Rename files with & to -and-
renames = [
    ("syllabus/subjects/subject-bcs-402-theory-of-automata-and-formal-languages-tafl.html",
     "syllabus/subjects/subject-bcs-402-theory-of-automata-and-formal-languages-tafl.html"),
    ("syllabus/subjects/subject-bcs-302-computer-organization-and-architecture-coa.html",
     "syllabus/subjects/subject-bcs-302-computer-organization-and-architecture-coa.html"),
    ("syllabus/subjects/subject-bcs-501-design-and-analysis-of-algorithms-daa.html",
     "syllabus/subjects/subject-bcs-501-design-and-analysis-of-algorithms-daa.html")
]

for old_path, new_path in renames:
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")

# 2. Update references in all HTML files
for root, dirs, files in os.walk("."):
    if any(p in root for p in [".git", ".system_generated", "node_modules", "scratch"]):
        continue
    for f in files:
        if f.endswith(".html") or f.endswith(".js") or f.endswith(".json") or f.endswith(".py"):
            p = os.path.join(root, f)
            with open(p, "r", encoding="utf-8", errors="ignore") as file_obj:
                content = file_obj.read()
            
            changed = False
            for old_path, new_path in renames:
                old_sub = os.path.basename(old_path)
                new_sub = os.path.basename(new_path)
                if old_sub in content:
                    content = content.replace(old_sub, new_sub)
                    changed = True
                
            if changed:
                with open(p, "w", encoding="utf-8") as out:
                    out.write(content)

print("Updated all internal references!")

