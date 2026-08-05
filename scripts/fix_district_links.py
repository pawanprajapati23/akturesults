import re, glob

# Update colleges/profiles/*.html to point to uptac-cutoff-{city}-2026.html
for f in glob.glob('colleges/profiles/*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    def repl(m):
        city_slug = m.group(1).lower().replace(' ', '-')
        return f'/admissions/districts/uptac-cutoff-{city_slug}-2026.html'

    new_content = re.sub(r'/admissions/districts/([a-zA-Z0-9\-]+)-engineering-colleges-cutoff\.html', repl, content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)

print("Fixed district links across all college profile pages!")
