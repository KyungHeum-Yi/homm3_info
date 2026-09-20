import os
import re
from PIL import Image

# 설정
IMAGES_DIR = os.path.join(os.path.dirname(__file__), "images")
MAGIC_OUTPUT_DIR = os.path.join(IMAGES_DIR, "magic")

# crop 좌표: x=516, y=434, w=881, h=595
# PIL Image.crop() tuple: (left, upper, right, lower)
CROP_BOX = (516, 434, 516 + 881, 434 + 595)

def main():
    if not os.path.exists(IMAGES_DIR):
        print(f"Error: {IMAGES_DIR} not found.")
        return

    # 대기마법_모험마법.png 등 파일 검색 정규표현식
    pattern = re.compile(r"^(.+마법)_(모험마법|전투마법)\.(png|jpg|jpeg)$")

    files = [f for f in os.listdir(IMAGES_DIR) if os.path.isfile(os.path.join(IMAGES_DIR, f))]
    processed_count = 0

    for filename in sorted(files):
        match = pattern.match(filename)
        if match:
            magic_type = match.group(1)  # e.g., '대기마법'
            spell_type = match.group(2)  # e.g., '모험마법' or '전투마법'

            target_folder = os.path.join(MAGIC_OUTPUT_DIR, magic_type)
            os.makedirs(target_folder, exist_ok=True)

            src_path = os.path.join(IMAGES_DIR, filename)
            dst_path = os.path.join(target_folder, f"{spell_type}.jpg")

            print(f"Processing: {filename} -> {os.path.relpath(dst_path, IMAGES_DIR)}")

            with Image.open(src_path) as img:
                # RGB로 변환 (PNG 투명도 알파 채널 대응 및 JPG 저장용)
                rgb_img = img.convert("RGB")
                cropped_img = rgb_img.crop(CROP_BOX)
                cropped_img.save(dst_path, "JPEG", quality=95)
                processed_count += 1

    print(f"\n완료: 총 {processed_count}개의 이미지를 크롭하여 저장했습니다.")

if __name__ == "__main__":
    main()
