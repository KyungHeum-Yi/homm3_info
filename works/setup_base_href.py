import os
import re

files = [
    'pages/homm3_hero_info.html',
    'pages/homm3_job_info.html',
    'pages/homm3_adjutant_info.html',
    'pages/homm3_magic_info.html',
    'pages/heroes_cards.html'
]

pages = [
    'homm3_hero_info.html',
    'homm3_job_info.html',
    'homm3_adjutant_info.html',
    'homm3_magic_info.html',
    'heroes_cards.html'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add <base href="../"> if not present
    if '<base href="../">' not in content:
        content = content.replace('<head>', '<head>\n<base href="../">')

    # 2. Update navigation links to include pages/
    for page in pages:
        content = re.sub(r'href=(["\'])' + re.escape(page) + r'(["\'])', r'href=\1pages/' + page + r'\2', content)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {fpath}")
