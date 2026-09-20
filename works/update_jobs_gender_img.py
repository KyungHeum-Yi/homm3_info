import re

with open("jobs_data.js", "r", encoding="utf-8") as f:
    content = f.read()

# Replace image: "images/jobs/{id}.png"
# with:
# imageMale: "images/jobs/{id}.png",
# imageFemale: "images/jobs/{id}_f.png"
def replacer(match):
    full_block = match.group(0)
    job_id_match = re.search(r'id:\s*"([^"]+)"', full_block)
    if job_id_match:
        job_id = job_id_match.group(1)
        replacement = f'imageMale: "images/jobs/{job_id}.png",\n    imageFemale: "images/jobs/{job_id}_f.png"'
        full_block = re.sub(r'image:\s*"[^"]+"', replacement, full_block)
    return full_block

new_content = re.sub(r'\{\s*id:\s*"[^"]+"[\s\S]*?traits:[\s\S]*?skills:[\s\S]*?\}', replacer, content)

with open("jobs_data.js", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated jobs_data.js with imageMale and imageFemale successfully!")
