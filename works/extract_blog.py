import re

with open('blog_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

m = re.search(r'<div[^>]*class="[^"]*se-main-container[^"]*"[^>]*>([\s\S]*?)<div[^>]*class="[^"]*blog_market_bridge_set_delivery_popup', html)
if not m:
    m = re.search(r'<div[^>]*class="[^"]*se-main-container[^"]*"[^>]*>([\s\S]*?)<div id="floating_bottom"', html)

content = m.group(1) if m else html

text = re.sub(r'<script[\s\S]*?</script>', '', content)
text = re.sub(r'<style[\s\S]*?</style>', '', text)
text = re.sub(r'<[^>]+>', '\n', text)
lines = [line.strip() for line in text.split('\n') if line.strip()]

with open('blog_clean_text.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Extraction complete. Total lines: {len(lines)}")
