import os
from PIL import Image

BASE_DIR = os.path.dirname(__file__)
MAGIC_DIR = os.path.join(BASE_DIR, "images", "magic")
OUTPUT_DIR = os.path.join(MAGIC_DIR, "전투마법info")

# 고정 너비 및 좌측 시작점
DEFAULT_X = 644
DEFAULT_W = 626

def find_crop_box(img_path):
    with Image.open(img_path) as img:
        rgb_img = img.convert("RGB")
        w, h = rgb_img.size

        # 1. 상단 (y1) 탐색: (x+3, y+3..5)가 황금색 테두리 (172, 148, 68)인지 확인
        y1 = None
        for y in range(350, 900):
            for x in [643, 644, 645]:
                p1 = rgb_img.getpixel((x + 3, y + 3))[:3]
                p2 = rgb_img.getpixel((x + 3, y + 4))[:3]
                p3 = rgb_img.getpixel((x + 3, y + 5))[:3]
                if (abs(p1[0] - 172) <= 3 and abs(p1[1] - 148) <= 3 and abs(p1[2] - 68) <= 3 and
                    abs(p2[0] - 172) <= 3 and abs(p2[1] - 148) <= 3 and abs(p2[2] - 68) <= 3 and
                    abs(p3[0] - 172) <= 3 and abs(p3[1] - 148) <= 3 and abs(p3[2] - 68) <= 3):
                    y1 = y
                    break
            if y1 is not None:
                break

        # 2. 하단 (y2) 탐색: x=646 세로 라인에서 하단 프레임 끝점 탐색
        # 끝점은 (127~128, 103~105, 62~67) 바로 뒤에 밝은 황금색 하이라이트(r>215, g>195)가 오는 패턴
        y2 = None
        if y1 is not None:
            for y in range(y1 + 250, min(h, y1 + 850)):
                p = rgb_img.getpixel((646, y))[:3]
                # 하단 밝은 하이라이트 픽셀 검출
                if p[0] >= 218 and p[1] >= 195 and p[2] >= 115:
                    prev_p = rgb_img.getpixel((646, y - 1))[:3]
                    # 직전 픽셀이 어두운 테두리 계열인지 확인
                    if prev_p[0] <= 190:
                        y2 = y + 1
                        break

        # 기본값 폴백 (검출 실패 시)
        if y1 is None:
            y1 = 531
        if y2 is None:
            y2 = y1 + 538

        box = (DEFAULT_X, y1, DEFAULT_X + DEFAULT_W, y2)
        return box, y1, y2 - y1

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    files = [f for f in os.listdir(MAGIC_DIR) if f.endswith(".png")]
    print(f"전체 대상 전투마법 파일 수: {len(files)}개")

    results = []
    for idx, file in enumerate(sorted(files)):
        src_path = os.path.join(MAGIC_DIR, file)
        spell_name = os.path.splitext(file)[0]
        dst_path = os.path.join(OUTPUT_DIR, f"{spell_name}.jpg")

        box, y, h = find_crop_box(src_path)

        with Image.open(src_path) as img:
            rgb_img = img.convert("RGB")
            cropped = rgb_img.crop(box)
            cropped.save(dst_path, "JPEG", quality=95)
            results.append((spell_name, box, cropped.size))
            print(f"[{idx+1:02d}/{len(files)}] {spell_name}: x={box[0]}, y={y}, w={box[2]-box[0]}, h={h} -> 저장 완료")

    print("\n==========================================")
    print(f"전체 {len(results)}개 전투마법 이미지 크롭 완료!")
    print("==========================================")

if __name__ == "__main__":
    main()
