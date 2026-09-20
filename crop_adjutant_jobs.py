import os
from PIL import Image

BASE_DIR = os.path.dirname(__file__)
RAW_DIR = os.path.join(BASE_DIR, "images", "raw_data", "부관직업")
OUTPUT_DIR = os.path.join(BASE_DIR, "images", "부관직업info")

# 개별 부관 직업 설명 팝업 박스 (17개 직업)
# 모서리 금색 프레임 패턴 검증 좌표:
# x1: 677, y1: 547, x2: 1243, y2: 1023 (width: 566, height: 476)
INDIVIDUAL_JOB_BOX = (677, 547, 1243, 1023)

# 전체 부관 직업 선택 대형 다이얼로그 박스 ("전체직업.png")
# x1: 494, y1: 360, x2: 1426, y2: 1242 (width: 932, height: 882)
ALL_JOB_BOX = (494, 360, 1426, 1242)

def main():
    if not os.path.exists(RAW_DIR):
        print(f"오류: {RAW_DIR} 폴더를 찾을 수 없습니다.")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    files = sorted([f for f in os.listdir(RAW_DIR) if f.lower().endswith((".png", ".jpg", ".jpeg"))])
    print(f"처리 대상 이미지 파일 수: {len(files)}개")

    success_count = 0
    for idx, filename in enumerate(files, start=1):
        job_name = os.path.splitext(filename)[0]
        src_path = os.path.join(RAW_DIR, filename)
        dst_path = os.path.join(OUTPUT_DIR, f"{job_name}.jpg")

        # '전체직업' 여부에 따라 알맞은 프레임 크롭 좌표 선택
        crop_box = ALL_JOB_BOX if job_name == "전체직업" else INDIVIDUAL_JOB_BOX

        with Image.open(src_path) as img:
            rgb_img = img.convert("RGB")
            cropped_img = rgb_img.crop(crop_box)
            cropped_img.save(dst_path, "JPEG", quality=95)

            w, h = cropped_img.size
            print(f"[{idx:02d}/{len(files)}] {job_name}: crop {crop_box} -> {w}x{h} 저장 완료 ({os.path.relpath(dst_path, BASE_DIR)})")
            success_count += 1

    print("\n==========================================")
    print(f"총 {success_count}개 부관 직업 이미지 크롭 완료!")
    print(f"저장 폴더: {os.path.abspath(OUTPUT_DIR)}")
    print("==========================================")

if __name__ == "__main__":
    main()
