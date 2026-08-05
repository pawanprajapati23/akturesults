import os, json, re
from bs4 import BeautifulSoup
from collections import defaultdict

with open("scripts/flat_colleges.json", "r", encoding="utf-8") as f:
    master_colleges = json.load(f)

# Map code to canonical slug
code_to_master = {c["code"]: c for c in master_colleges}
canonical_slugs = {c["slug"] for c in master_colleges}

profiles_dir = "colleges/profiles"
all_profiles = [f for f in os.listdir(profiles_dir) if f.endswith(".html")]

redirects_created = 0

for profile_file in all_profiles:
    slug = profile_file.replace(".html", "")
    full_path = os.path.join(profiles_dir, profile_file)

    if slug not in canonical_slugs:
        # Try to find which college this belongs to
        try:
            with open(full_path, "r", encoding="utf-8", errors="ignore") as pf:
                txt = pf.read()
            
            # Find code in file
            code_match = re.search(r'Code[:\s]+([0-9]{3}[a-zA-Z]?)', txt)
            if code_match:
                code = code_match.group(1)
                if code in code_to_master:
                    primary_slug = code_to_master[code]["slug"]
                    if primary_slug != slug and os.path.exists(os.path.join(profiles_dir, f"{primary_slug}.html")):
                        # Turn this into a redirect to primary profile
                        redir_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{code_to_master[code]['name']} (Code {code})</title>
  <link rel="canonical" href="https://akturesults.in/colleges/profiles/{primary_slug}.html">
  <meta http-equiv="refresh" content="0; url=/colleges/profiles/{primary_slug}.html">
  <script>window.location.href = '/colleges/profiles/{primary_slug}.html';</script>
</head>
<body>
  <p>Redirecting to <a href="/colleges/profiles/{primary_slug}.html">{code_to_master[code]['name']}</a>...</p>
</body>
</html>"""
                        with open(full_path, "w", encoding="utf-8") as out:
                            out.write(redir_html)
                        redirects_created += 1
                        print(f"Consolidated duplicate: {slug} -> {primary_slug}")
        except Exception as e:
            print(f"Error processing {profile_file}: {e}")

print(f"Consolidated {redirects_created} duplicate profile aliases into clean SEO redirects!")
