import os
import re
from PIL import Image

raw_dir = r"C:\SourceCode\homm3_info\images\raw_data\영웅직업"
out_dir = r"C:\SourceCode\homm3_info\images\jobs"
os.makedirs(out_dir, exist_ok=True)

# 17개 직업과 원본 스크린샷 파일 매핑
mapping = {
    "master_warrior": ("마스터 전사", "마스터전사.png"),
    "gm_warrior": ("그랜드마스터 전사", "그랜드마스터전사.png"),
    "legend_warrior": ("레전드 전사", "레전드전사.png"),
    
    "master_explorer": ("마스터 탐험가", "마스터탐험가.png"),
    "gm_explorer": ("그랜드마스터 탐험가", "그랜드마스터탐험가.png"),
    "legend_explorer": ("레전드 탐험가", "레전드탐험가.png"),
    
    "master_mage": ("마스터 마법사", "마스터마법사.png"),
    "gm_mage": ("그랜드마스터 마법사", "그랜드마스터마법사.png"),
    "legend_mage": ("레전드 마법사", "레전드마법사.png"),
    
    "druid": ("드루이드", "드루이드.png"),
    "beast_lord": ("비스트 로드", "비스트로드.png"),
    "cardinal": ("카디널", "카디널.png"),
    
    "battle_mage": ("전투마법사", "전투마법사.png"),
    "reaver": ("리버", "리버.png"),
    "heretic": ("헤레틱", "헤레틱.png"),
    
    "hunter": ("헌터", "헌터.png"),
    "warlord": ("워로드", "워로드.png"),
    "field_marshal": ("필드 마샬", "필드마샬.png"),
    
    "general": ("제너럴", "제너럴.png"),
    "guardian": ("가디언", "가디언.png"),
    "slayer": ("슬레이어", "슬레이어.png"),
    "avenger": ("어벤저", "어벤져.png"),
}

# Crop coordinates: x504 y408 w824 h642
box = (504, 408, 504 + 824, 408 + 642)
print("Crop box:", box)

success_count = 0
for job_id, (name, filename) in mapping.items():
    src_path = os.path.join(raw_dir, filename)
    dst_name = f"{job_id}.png"
    dst_path = os.path.join(out_dir, dst_name)
    
    if not os.path.exists(src_path):
        print(f"[ERROR] Source not found: {src_path}")
        continue
        
    img = Image.open(src_path)
    cropped = img.crop(box)
    cropped.save(dst_path, "PNG")
    print(f"[OK] Cropped {name} -> {dst_name} ({cropped.size})")
    success_count += 1

print(f"\nTotal cropped: {success_count}/{len(mapping)}")
