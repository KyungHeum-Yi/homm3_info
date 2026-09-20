import os
import re

pages_dir = r"c:\SourceCode\homm3_info\pages"

for filename in os.listdir(pages_dir):
    if not filename.endswith(".html"):
        continue
    filepath = os.path.join(pages_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update href="index.html" to href="../index.html"
    content = content.replace('href="index.html"', 'href="../index.html"')

    # 2. Update script tags for root js files
    for js_name in ["heroes_data.js", "jobs_data.js", "magic_data.js"]:
        content = content.replace(f'src="{js_name}"', f'src="../{js_name}"')

    # 3. Update hardcoded image paths in HTML
    # Note: Look for src="images/..." and replace with src="../images/..."
    content = re.sub(r'src="images/', 'src="../images/', content)
    # Also in magic onclick: openModal('...', 'images/...')
    content = re.sub(r"'images/", "'../images/", content)

    # 4. In JS code inside html if images/ is used as string:
    # e.g. 'images/heroes_info/' -> '../images/heroes_info/'
    # e.g. "images/heroes_info/" -> "../images/heroes_info/"
    content = content.replace("'images/heroes_info/", "'../images/heroes_info/")
    content = content.replace('"images/heroes_info/', '"../images/heroes_info/')
    content = content.replace("'images/magic/", "'../images/magic/")
    content = content.replace('"images/magic/', '"../images/magic/')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated {filename}")
