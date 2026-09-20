import os

files = [
    'pages/homm3_hero_info.html',
    'pages/homm3_job_info.html',
    'pages/homm3_magic_info.html',
    'pages/heroes_cards.html'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace script src
    content = content.replace('src="heroes_data.js"', 'src="data/heroes_data.js"')
    content = content.replace('src="jobs_data.js"', 'src="data/jobs_data.js"')
    content = content.replace('src="magic_data.js"', 'src="data/magic_data.js"')

    # Replace fetch json
    content = content.replace("fetch('heroes_data.json')", "fetch('data/heroes_data.json')")
    content = content.replace('fetch("heroes_data.json")', 'fetch("data/heroes_data.json")')
    content = content.replace("fetch('magic_data.json')", "fetch('data/magic_data.json')")
    content = content.replace('fetch("magic_data.json")', 'fetch("data/magic_data.json")')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {fpath}")
