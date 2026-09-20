import urllib.request
import re

url = 'https://blog.naver.com/PostView.naver?blogId=gigi905&logNo=221933502815'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

# Post view area
start_tag = '<div id="postViewArea"'
end_tag = '<div class="post_footer_contents"'

if start_tag in html:
    part = html.split(start_tag)[1]
    if end_tag in part:
        part = part.split(end_tag)[0]
else:
    part = html[100000:220000]

def repl_img(m):
    tag = m.group(0)
    alt_m = re.search(r'alt="([^"]+)"', tag)
    src_m = re.search(r'src="([^"]+)"', tag)
    alt_val = alt_m.group(1) if alt_m else ""
    src_val = src_m.group(1) if src_m else ""
    return f"\n[IMAGE: {alt_val} | {src_val}]\n"

part_img = re.sub(r'<img[^>]+>', repl_img, part)
text = re.sub(r'<[^>]+>', '\n', part_img)
lines = [l.strip() for l in text.splitlines() if l.strip()]

with open('adjutant_blog_content.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Successfully extracted {len(lines)} lines to adjutant_blog_content.txt")
