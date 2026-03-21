#!/bin/bash
# Update theme to darker orange in all trending pages

for file in grade-calculator.html syllabus.html revaluation-process.html erp-login-guide.html back-paper-result.html aktu-erp-login-2026.html aktu-memes.html aktu-college-comparison.html; do
  if [ -f "$file" ]; then
    sed -i 's/--primary: #ff6b35/--primary: #e85d24/g' "$file"
    sed -i 's/--primary-dark: #e55a28/--primary-dark: #d44a15/g' "$file"
    sed -i 's/--secondary: #ff8c42/--secondary: #bf3e0f/g' "$file"
    sed -i 's/rgba(255, 107, 53/rgba(232, 93, 36/g' "$file"
    sed -i 's/rgba(255, 140, 66/rgba(212, 74, 21/g' "$file"
    echo "✅ Updated $file"
  fi
done
echo "🎨 All pages updated to darker orange theme!"
