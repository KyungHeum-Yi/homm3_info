import os
import re
from PIL import Image

raw_dir = r"C:\SourceCode\homm3_info\images\raw_data\영웅직업"
out_dir = r"C:\SourceCode\homm3_info\images\jobs"
os.makedirs(out_dir, exist_ok=True)

raw_files = [f for f in os.listdir(raw_dir) if f.endswith(".png")]
print("Raw files in folder:", len(raw_files))
for f in sorted(raw_files):
    print(" -", f)

# Read jobs_data.js
with open("jobs_data.js", "r", encoding="utf-8") as f:
    js_content = f.read()

# Crop coordinates: x504 y408 w824 h642
box = (504, 408, 504 + 824, 408 + 642)
print("Crop box:", box)

# Match job name to raw file
# e.g., nameKo "마스터 전사" -> "마스터전사.png"
# "어벤저" -> "어벤져.png"
# "필드 마샬" -> "필드마샬.png"
# "비스트 로드" -> "비스트로드.png"
# "전투마법사" -> "전투마법사.png"
