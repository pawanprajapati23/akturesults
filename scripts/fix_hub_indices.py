import os, shutil

# Remove temporary files in scripts/colleges if any
if os.path.exists("scripts/colleges"):
    shutil.rmtree("scripts/colleges")

hubs = {
    "colleges/index.html": {
        "title": "AKTU Colleges Directory & Institute List",
        "redirect": "/colleges/aktu-colleges-filter-directory.html",
        "desc": "Complete directory of AKTU affiliated colleges across Uttar Pradesh."
    },
    "syllabus/index.html": {
        "title": "AKTU Syllabus Hub — B.Tech, MBA, MCA, B.Pharm",
        "redirect": "/syllabus.html",
        "desc": "Download semester-wise and branch-wise AKTU syllabus."
    },
    "results/index.html": {
        "title": "AKTU One View Results Portal",
        "redirect": "/results.html",
        "desc": "Check AKTU One View semester result and scorecard."
    },
    "admissions/index.html": {
        "title": "AKTU / UPTAC Admissions & Counseling Portal",
        "redirect": "/admissions/uptac-choice-filling-predictor-2026.html",
        "desc": "UPTAC counseling choice filling predictor and cutoffs."
    },
    "tools/index.html": {
        "title": "AKTU Student Tools & Calculators",
        "redirect": "/calculators.html",
        "desc": "AKTU CGPA, Grace Marks, and COP Fee Calculators."
    },
    "placements/index.html": {
        "title": "AKTU Placement Statistics & Leaderboard",
        "redirect": "/placements/aktu-college-placement-leaderboard-2026.html",
        "desc": "AKTU highest package and campus recruitment leaderboard."
    }
}

for path, data in hubs.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data['title']}</title>
  <meta name="description" content="{data['desc']}">
  <link rel="canonical" href="https://akturesults.in{data['redirect']}">
  <meta http-equiv="refresh" content="0; url={data['redirect']}">
  <script>window.location.href = '{data['redirect']}';</script>
</head>
<body>
  <p>Redirecting to <a href="{data['redirect']}">{data['title']}</a>...</p>
</body>
</html>"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created hub redirect: {path}")

