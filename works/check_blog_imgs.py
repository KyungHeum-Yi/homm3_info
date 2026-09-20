import re

with open('blog_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

imgs = re.findall(r'https?://[^\s"\'<>]+?\.(?:png|jpg|jpeg|gif)', html)
acm_imgs = [i for i in imgs if 'postfiles' in i or 'blogfiles' in i or 'blogthumb' in i]
print(f"Total images: {len(imgs)}, Blog uploaded images: {len(acm_imgs)}")
for img in set(acm_imgs):
    print(img)
