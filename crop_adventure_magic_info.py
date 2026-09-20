import os
from PIL import Image

BASE_DIR = os.path.dirname(__file__)
MAGIC_DIR = os.path.join(BASE_DIR, "images", "magic")
OUTPUT_DIR = os.path.join(MAGIC_DIR, "모험마법info")

# crop 좌표: x=643, y=577, w=627, h=446
CROP_BOX = (643, 577, 643 + 627, 577 + 446)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    files = [f for f in os.listdir(MAGIC_DIR) if f.endswith(".png")]
    count = 0

    for file in sorted(files):
        src_path = os.path.join(MAGIC_DIR, file)
        spell_name = os.path.splitext(file)[0]
        dst_path = os.path.join(OUTPUT_DIR, f"{spell_name}.jpg")

        with Image.open(src_path) as img:
            rgb_img = img.convert("RGB")
            # 예견 마법은 설명창 높이가 더 커서 개별 좌표 적용: x=644, y=531, w=626, h=538
            box = (644, 531, 644 + 626, 531 + 538) if spell_name == "예견" else CROP_BOX
            cropped = rgb_img.crop(box)
            cropped.save(dst_path, "JPEG", quality=95)
            print(f"[{count+1}] 크롭 완료: {file} -> {os.path.relpath(dst_path, BASE_DIR)} {cropped.size}")
            count += 1

    print(f"\n총 {count}개의 모험마법 인게임 캡쳐 이미지를 크롭하여 저장했습니다.")

if __name__ == "__main__":
    main()
