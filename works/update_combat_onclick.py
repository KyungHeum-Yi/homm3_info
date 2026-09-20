import re

def update_combat_spells_onclick():
    with open('homm3_magic_info.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 패턴: onclick="openModal('계열 - 마법명', 'images/magic/계열/전투마법/마법명.jpg')"
    # 교체: onclick="openModal('계열 - 마법명 (전투마법 상세)', 'images/magic/전투마법info/마법명.jpg')"
    pattern = re.compile(r'onclick="openModal\(\'([^\']+마법) - ([^\']+)\',\s*\'images/magic/[^\']+/전투마법/([^\']+)\.jpg\'\)"')

    def replacer(match):
        magic_type = match.group(1)
        spell_name = match.group(2)
        return f'onclick="openModal(\'{magic_type} - {spell_name} (전투마법 상세)\', \'images/magic/전투마법info/{spell_name}.jpg\')"'

    new_html, count = pattern.subn(replacer, html)
    print(f"총 {count}개의 전투마법 클릭 이벤트가 images/magic/전투마법info/ 로 교체되었습니다.")

    with open('homm3_magic_info.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

if __name__ == '__main__':
    update_combat_spells_onclick()
