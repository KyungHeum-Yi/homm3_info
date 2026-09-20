import os
from PIL import Image

BASE_DIR = os.path.dirname(__file__)
MAGIC_DIR = os.path.join(BASE_DIR, "images", "magic")

# 마법 셀 크기 (W: 107, H: 99에서 아래쪽 -16px -> 83)
W = 107
H = 83

# X 좌표 목록 (열 1, 2, 3) - 좌측으로 2px 이동
# 좌측 페이지:
LEFT_X = [33 - 2, 167 - 2, 302 - 2]  # [31, 165, 300]
# 우측 페이지:
RIGHT_X = [474 - 2, 608 - 2, 743 - 2]  # [472, 606, 741]

# Y 좌표 목록 (행 1, 2, 3, 4) - 위로 2px 이동
Y_ROWS = [28 - 2, 163 - 2, 298 - 2, 433 - 2]  # [26, 161, 296, 431]

# 슬롯 정의 함수: 순서대로 (x, y, w, h) 반환
# 좌측 페이지:
# (1,1), (2,1)은 대표이미지이므로 슬롯 1은 (3,1)
# 슬롯 2: (1,2), 슬롯 3: (2,2), 슬롯 4: (3,2)
# 슬롯 5: (1,3), 슬롯 6: (2,3), 슬롯 7: (3,3)
# 슬롯 8: (1,4), 슬롯 9: (2,4), 슬롯 10: (3,4)
# 우측 페이지:
# 슬롯 11: (1,1), 슬롯 12: (2,1), 슬롯 13: (3,1)
# 슬롯 14~16: (1,2)~(3,2)
# 슬롯 17~19: (1,3)~(3,3)
# 슬롯 20~22: (1,4)~(3,4)
def get_slot_boxes():
    slots = []
    
    # 좌측 페이지 (총 10칸)
    # 행 1: (3, 1) 만 해당
    slots.append((LEFT_X[2], Y_ROWS[0], W, H))
    # 행 2: (1,2), (2,2), (3,2)
    for col in range(3):
        slots.append((LEFT_X[col], Y_ROWS[1], W, H))
    # 행 3: (1,3), (2,3), (3,3)
    for col in range(3):
        slots.append((LEFT_X[col], Y_ROWS[2], W, H))
    # 행 4: (1,4), (2,4), (3,4)
    for col in range(3):
        slots.append((LEFT_X[col], Y_ROWS[3], W, H))

    # 우측 페이지 (총 12칸)
    for row in range(4):
        for col in range(3):
            slots.append((RIGHT_X[col], Y_ROWS[row], W, H))
            
    return slots

# 마법 데이터 정의
SPELLS_DATA = {
    "대기마법": {
        "모험마법": ["대기 조망", "대지 조망", "예견", "순풍", "귀환", "비행"],
        "전투마법": [
            "대기의 저항력", "마법 화살", "정확성", "행운", "가속", "마법 반사",
            "반격", "방어막", "방해 광선", "번개", "언데드 파괴", "헌신",
            "뱀파이어릭 터치", "연속 번개", "최면", "대천사 소환"
        ]
    },
    "대지마법": {
        "모험마법": ["대기 조망", "대지 조망", "귀환", "역전"],
        "전투마법": [
            "대지의 저항력", "마법 화살", "모래늪", "석갑", "둔화", "방패",
            "중력장", "지진", "마법 거부", "시체 조종", "죽음의 물결",
            "땅의 정령 소환", "부활", "유성 폭풍", "내파", "유령 소환"
        ]
    },
    "물마법": {
        "모험마법": ["대기 조망", "대지 조망", "마법사의 눈", "차원의 문"],
        "전투마법": [
            "마법 화살", "물의 저항력", "치료", "환희", "약화", "얼음 화살",
            "축복", "해재", "망각", "순간이동", "얼음 고리", "기원",
            "복재", "블리자드"
        ]
    },
    "불마법": {
        "모험마법": ["대기 조망", "대지 조망", "마법사의 눈", "소망의 문", "차원의 문"],
        "전투마법": [
            "마법 화살", "불의 저항력", "지뢰", "피의 굶주림", "광분", "저주",
            "화염의 벽", "불의 방패", "불의 정령 소환", "인챈트", "장님",
            "파이어볼", "버서크", "아마겟돈", "희생", "드래곤 스트렝스"
        ]
    }
}

def main():
    slots = get_slot_boxes()
    total_cropped = 0

    for magic_type, categories in SPELLS_DATA.items():
        for category, spell_list in categories.items():
            src_image_path = os.path.join(MAGIC_DIR, magic_type, f"{category}.jpg")
            if not os.path.exists(src_image_path):
                print(f"[경고] 원본 이미지를 찾을 수 없습니다: {src_image_path}")
                continue

            # 저장 폴더: images/magic/{magic_type}/{category}/
            save_dir = os.path.join(MAGIC_DIR, magic_type, category)
            os.makedirs(save_dir, exist_ok=True)

            with Image.open(src_image_path) as img:
                img_w, img_h = img.size
                print(f"\n--- [{magic_type} - {category}] 처리 중 (마법 {len(spell_list)}개) ---")

                for idx, spell_name in enumerate(spell_list):
                    if idx >= len(slots):
                        print(f"[오류] 정의된 슬롯 수({len(slots)})를 초과했습니다: {spell_name}")
                        break

                    x, y, w, h = slots[idx]
                    crop_box = (x, y, x + w, y + h)

                    # 이미지 범위 체크
                    if x + w > img_w or y + h > img_h:
                        print(f"[경고] 좌표가 이미지 범위를 벗어남: {spell_name} {crop_box} vs ({img_w}, {img_h})")

                    cropped = img.crop(crop_box)
                    # 특수문자 또는 파일명 안전 처리
                    safe_spell_name = spell_name.replace("/", "_").strip()
                    dst_file = os.path.join(save_dir, f"{safe_spell_name}.jpg")
                    cropped.save(dst_file, "JPEG", quality=95)
                    print(f"  [{idx+1:02d}] {safe_spell_name}.jpg (x={x}, y={y}, w={w}, h={h}) -> 저장 완료")
                    total_cropped += 1

    print(f"\n==========================================")
    print(f"모든 마법 크롭 완료! 총 {total_cropped}개의 마법 이미지가 저장되었습니다.")
    print(f"==========================================")

if __name__ == "__main__":
    main()
