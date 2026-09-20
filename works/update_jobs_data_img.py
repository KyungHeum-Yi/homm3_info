import re

with open("jobs_data.js", "r", encoding="utf-8") as f:
    content = f.read()

# Replace image: "images/jobs/xxx.png" with image: "images/jobs/{id}.png"
# Let's match each job object
def replacer(match):
    full_block = match.group(0)
    job_id_match = re.search(r'id:\s*"([^"]+)"', full_block)
    if job_id_match:
        job_id = job_id_match.group(1)
        new_img = f'image: "images/jobs/{job_id}.png"'
        full_block = re.sub(r'image:\s*"[^"]+"', new_img, full_block)
    return full_block

# Match each object { ... }
new_content = re.sub(r'\{\s*id:\s*"[^"]+"[\s\S]*?traits:[\s\S]*?skills:[\s\S]*?\}', replacer, content)

with open("jobs_data.js", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated jobs_data.js successfully!")
