import re

def update_adventure_spells_onclick():
    with open('homm3_magic_info.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 패턴: onclick="openModal('계열 - 마법명', 'images/magic/계열/모험마법/마법명.jpg')"
    # 교체: onclick="openModal('마법명 (모험마법 상세)', 'images/magic/모험마법info/마법명.jpg')"
    pattern = re.compile(r'onclick="openModal\(\'([^\']+마법) - ([^\']+)\',\s*\'images/magic/[^\']+/모험마법/([^\']+)\.jpg\'\)"')

    def replacer(match):
        magic_type = match.group(1)
        spell_name = match.group(2)
        return f'onclick="openModal(\'{magic_type} - {spell_name} (모험마법 상세)\', \'images/magic/모험마법info/{spell_name}.jpg\')"'

    new_html, count = pattern.subn(replacer, html)
    print(f"총 {count}개의 모험마법 클릭 이벤트가 images/magic/모험마법info/{'{마법명}'}.jpg 로 교체되었습니다.")

    with open('homm3_magic_info.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

if __name__ == '__main__':
    update_adventure_spells_onclick()
