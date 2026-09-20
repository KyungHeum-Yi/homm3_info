import re

def update_magic_info_page():
    with open('homm3_magic_info.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. <script src="magic_data.js"></script> 추가
    old_head = '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;800;900&family=Noto+Sans+KR:wght@400;500;700;900&display=swap" rel="stylesheet">'
    new_head = old_head + '\n<script src="magic_data.js"></script>'
    if 'magic_data.js' not in html:
        html = html.replace(old_head, new_head)

    # 2. CSS 스타일 추가: 마법 등급 뱃지 및 단계 필터 버튼
    badge_css = '''
/* ── 마법 등급(레벨) 스티커 뱃지 스타일 ─────────── */
.level-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.68rem;
  font-weight: 800;
  padding: 1px 5px;
  border-radius: 4px;
  margin-right: 4px;
  line-height: 1.2;
  vertical-align: middle;
  letter-spacing: 0.2px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.5);
  flex-shrink: 0;
}
.level-badge-1 { background: #334155; color: #cbd5e1; border: 1px solid #64748b; }
.level-badge-2 { background: #1e3a5f; color: #93c5fd; border: 1px solid #3b82f6; }
.level-badge-3 { background: #064e3b; color: #6ee7b7; border: 1px solid #10b981; }
.level-badge-4 { background: #4c1d95; color: #c4b5fd; border: 1px solid #8b5cf6; }
.level-badge-5 { background: #7c2d12; color: #fed7aa; border: 1px solid #f97316; box-shadow: 0 0 8px rgba(249, 115, 22, 0.4); }

/* 단계 필터 버튼 */
.level-btn {
  background: #20232c;
  color: #8c94a9;
  border: 1px solid #383d4e;
  padding: 5px 11px;
  border-radius: 6px;
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
}
.level-btn:hover {
  background: #2b3040;
  color: #fff;
  border-color: #ffd700;
}
.level-btn.active {
  background: linear-gradient(135deg, #c5a059, #9e7d3b);
  color: #121316;
  border-color: #ffd700;
  font-weight: 800;
  box-shadow: 0 0 10px rgba(197, 160, 89, 0.4);
}
'''
    # .spell-name CSS 바로 아래에 뱃지 CSS 삽입
    target_css_anchor = '.spell-name {'
    html = html.replace('.spell-name {', badge_css + '\n.spell-name {')

    # 3. Controls UI에 단계 필터 버튼 그룹 추가
    old_controls_row = '''      <div class="tab-group" id="typeTabs">
        <span class="group-label">마법 분류:</span>
        <button class="type-btn active" data-type="ALL">모두 보기</button>
        <button class="type-btn" data-type="모험마법">모험마법</button>
        <button class="type-btn" data-type="전투마법">전투마법</button>
      </div>'''

    new_controls_row = '''      <div class="tab-group" id="typeTabs">
        <span class="group-label">마법 분류:</span>
        <button class="type-btn active" data-type="ALL">모두 보기</button>
        <button class="type-btn" data-type="모험마법">모험마법</button>
        <button class="type-btn" data-type="전투마법">전투마법</button>
      </div>

      <div class="tab-group" id="levelTabs">
        <span class="group-label">마법 등급:</span>
        <button class="level-btn active" data-level="ALL">전체</button>
        <button class="level-btn" data-level="1">1단</button>
        <button class="level-btn" data-level="2">2단</button>
        <button class="level-btn" data-level="3">3단</button>
        <button class="level-btn" data-level="4">4단</button>
        <button class="level-btn" data-level="5">5단</button>
      </div>'''

    html = html.replace(old_controls_row, new_controls_row)

    # 4. Javascript 로직 업데이트:
    # - JSON/JS 데이터 읽어서 모든 .spell-item에 data-level과 스티커 뱃지 DOM 추가
    # - 단계 필터링(levelTabs) 이벤트 및 applyFilters()에 level 조건 추가
    old_script_start = '<script>\nlet currentMagic = "ALL";\nlet currentType = "ALL";'
    new_script_start = '''<script>
let currentMagic = "ALL";
let currentType = "ALL";
let currentLevel = "ALL";
let magicData = {};

// 마법 등급 데이터 로드 및 각 마법 카드에 스티커 뱃지 부착
async function initMagicData() {
  if (window.MAGIC_DATA && window.MAGIC_DATA.spells) {
    magicData = window.MAGIC_DATA.spells;
  } else {
    try {
      const res = await fetch("magic_data.json");
      if (res.ok) {
        const data = await res.json();
        magicData = data.spells;
      }
    } catch(e) {
      console.warn("magic_data.json fetch failed, checking window.MAGIC_DATA:", e);
      if (window.MAGIC_DATA) magicData = window.MAGIC_DATA.spells;
    }
  }

  // 모든 spell-item에 data-level 속성 부여 및 spell-name 앞에 스티커 뱃지 삽입
  document.querySelectorAll(".spell-item").forEach(item => {
    const nameEl = item.querySelector(".spell-name");
    if (!nameEl) return;
    const spellName = nameEl.innerText.trim();
    const info = magicData[spellName];
    if (info && info.level) {
      item.setAttribute("data-level", info.level);
      // 스티커 뱃지 엘리먼트 생성
      const badge = document.createElement("span");
      badge.className = `level-badge level-badge-${info.level}`;
      badge.innerText = `${info.level}단`;
      nameEl.insertBefore(badge, nameEl.firstChild);
    }
  });

  applyFilters();
}

// 마법 등급 탭 필터
document.querySelectorAll("#levelTabs .level-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll("#levelTabs .level-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    currentLevel = btn.getAttribute("data-level");
    applyFilters();
  });
});'''

    html = html.replace(old_script_start, new_script_start)

    # 5. applyFilters() 내부에 matchesLevel 조건 추가
    old_apply_spell_loop = '''      spellItems.forEach(item => {
        const spellName = item.querySelector(".spell-name").innerText.toLowerCase();
        const matchesSearch = !searchTerm || spellName.includes(searchTerm);

        if (matchesCat && matchesSearch) {'''

    new_apply_spell_loop = '''      spellItems.forEach(item => {
        const spellName = item.querySelector(".spell-name").innerText.toLowerCase();
        const matchesSearch = !searchTerm || spellName.includes(searchTerm);
        const itemLevel = item.getAttribute("data-level");
        const matchesLevel = (currentLevel === "ALL" || currentLevel === itemLevel);

        if (matchesCat && matchesSearch && matchesLevel) {'''

    html = html.replace(old_apply_spell_loop, new_apply_spell_loop)

    # 6. DOMContentLoaded 시 initMagicData 호출
    old_end = 'document.addEventListener("keydown", (e) => {'
    new_end = 'window.addEventListener("DOMContentLoaded", initMagicData);\n\ndocument.addEventListener("keydown", (e) => {'
    html = html.replace(old_end, new_end)

    with open('homm3_magic_info.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("homm3_magic_info.html updated successfully with level badges and level filtering!")

if __name__ == '__main__':
    update_magic_info_page()
