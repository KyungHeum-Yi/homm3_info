import os
from PIL import Image

BASE_DIR = os.path.dirname(__file__)
MAGIC_DIR = os.path.join(BASE_DIR, "images", "magic")

# 대표이미지 crop 영역: x=39, y=35, w=222, h=91
# PIL Bounding Box: (left, upper, right, lower)
CROP_BOX = (39, 35, 39 + 222, 35 + 91)

# 대상 마법 종류
MAGIC_TYPES = ["대기마법", "대지마법", "물마법", "불마법"]

def main():
    processed_count = 0

    for magic in MAGIC_TYPES:
        magic_path = os.path.join(MAGIC_DIR, magic)
        src_path = os.path.join(magic_path, "모험마법.jpg")

        if not os.path.exists(src_path):
            print(f"경고: {src_path} 파일을 찾을 수 없습니다.")
            continue

        dst_path = os.path.join(magic_path, "대표이미지.jpg")

        with Image.open(src_path) as img:
            cropped = img.crop(CROP_BOX)
            cropped.save(dst_path, "JPEG", quality=95)
            print(f"저장 완료: {dst_path} (크기: {cropped.size})")
            processed_count += 1

    print(f"\n총 {processed_count}개의 대표이미지가 성공적으로 크롭/저장되었습니다.")

if __name__ == "__main__":
    main()
