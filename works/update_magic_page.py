import re

def update_magic_page():
    with open('homm3_magic_info.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Controls 검색창 추가
    old_controls = '''      <div class="tab-group" id="typeTabs">
        <span class="group-label">마법 분류:</span>
        <button class="type-btn active" data-type="ALL">모두 보기</button>
        <button class="type-btn" data-type="모험마법">모험마법</button>
        <button class="type-btn" data-type="전투마법">전투마법</button>
      </div>
    </div>
  </div>'''

    new_controls = '''      <div class="tab-group" id="typeTabs">
        <span class="group-label">마법 분류:</span>
        <button class="type-btn active" data-type="ALL">모두 보기</button>
        <button class="type-btn" data-type="모험마법">모험마법</button>
        <button class="type-btn" data-type="전투마법">전투마법</button>
      </div>

      <div class="search-box">
        <span class="search-icon">&#128269;</span>
        <input type="text" id="magicSearchInput" placeholder="마법 이름 검색 (예: 가속, 부활, 축복)..." oninput="applyFilters()">
      </div>
    </div>
  </div>'''

    text = text.replace(old_controls, new_controls)

    # 2. 버튼 영역 제거
    text = re.sub(r'<div class="fullbook-shortcuts">[\s\S]*?</div>\s*</div>', '</div>', text)

    # 3. 대표이미지 클릭 이벤트 교체
    for el in ['대기마법', '대지마법', '물마법', '불마법']:
        text = text.replace(
            f'onclick="openModal(\'{el} - 전체 마법책 스크린샷 (모험마법)\', \'images/magic/{el}/모험마법.jpg\')"',
            f'onclick="openBookModal(\'{el}\')"'
        )

    # 4. CSS 업데이트
    new_css = '''/* ── Search Input Box ────────────────────────── */
.search-box {
  position: relative;
  min-width: 260px;
}
.search-box input {
  width: 100%;
  padding: 8px 14px 8px 34px;
  background: #20232c;
  border: 1px solid #3d4254;
  border-radius: 8px;
  color: #fff;
  font-size: 0.88rem;
  transition: all 0.2s ease;
}
.search-box input:focus {
  outline: none;
  border-color: #ffd700;
  box-shadow: 0 0 10px rgba(255, 215, 0, 0.35);
}
.search-icon {
  position: absolute;
  left: 10px;
  top: 50%;
  transform: translateY(-50%);
  color: #7d859b;
  font-size: 0.95rem;
}

/* ── Modal for Full Image View & Swipe Slider ──── */
.modal-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.88);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
}
.modal-overlay.active {
  display: flex;
}
.modal-content {
  background: #1a1c23;
  border: 2px solid var(--border-gold);
  border-radius: 12px;
  box-shadow: 0 0 35px rgba(0,0,0,0.9), 0 0 25px var(--gold-glow);
  max-width: 95vw;
  max-height: 94vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  position: relative;
  width: 960px;
}
.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 20px;
  background: #222530;
  border-bottom: 1px solid #3d4254;
}
.modal-title {
  font-size: 1.15rem;
  font-weight: 800;
  color: #ffd700;
  display: flex;
  align-items: center;
  gap: 10px;
}
.modal-close {
  background: none;
  border: none;
  color: #a0a5b5;
  font-size: 1.8rem;
  cursor: pointer;
  line-height: 1;
  transition: color 0.2s;
}
.modal-close:hover { color: #ff4757; }

/* ── Swipe / Slider Styles ─────────────────────── */
.slider-tabs {
  display: flex;
  background: #15171e;
  border-bottom: 1px solid #2d313f;
}
.slider-tab-btn {
  flex: 1;
  padding: 10px 16px;
  background: none;
  border: none;
  color: #8c94a9;
  font-size: 0.92rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  border-bottom: 3px solid transparent;
}
.slider-tab-btn:hover {
  color: #fff;
  background: rgba(255,255,255,0.03);
}
.slider-tab-btn.active {
  color: #ffd700;
  border-bottom-color: #ffd700;
  background: rgba(255, 215, 0, 0.05);
}

.slider-wrapper {
  position: relative;
  overflow: hidden;
  background: #0e1014;
  touch-action: pan-y;
  user-select: none;
}
.slider-track {
  display: flex;
  width: 200%;
  transition: transform 0.35s cubic-bezier(0.25, 1, 0.5, 1);
}
.slider-slide {
  width: 50%;
  padding: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
}
.modal-img {
  max-width: 100%;
  max-height: 72vh;
  object-fit: contain;
  border-radius: 6px;
  border: 1px solid #33384a;
  box-shadow: 0 4px 18px rgba(0,0,0,0.8);
}

.slide-nav-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(20, 22, 28, 0.75);
  color: #ffd700;
  border: 1px solid #3d4254;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  cursor: pointer;
  transition: all 0.2s ease;
  z-index: 10;
}
.slide-nav-btn:hover {
  background: #ffd700;
  color: #121316;
  border-color: #ffd700;
  box-shadow: 0 0 12px var(--gold-glow);
}
.slide-prev { left: 14px; }
.slide-next { right: 14px; }

.slider-dots {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  padding: 10px;
  background: #15171e;
  border-top: 1px solid #262a36;
}
.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #383d4e;
  cursor: pointer;
  transition: all 0.2s ease;
}
.dot.active {
  background: #ffd700;
  transform: scale(1.25);
  box-shadow: 0 0 8px rgba(255, 215, 0, 0.6);
}
'''
    css_pattern = re.compile(r'/\* ── Modal for Full Image View ────────────────── \*/[\s\S]*?(?=</style>)')
    text = css_pattern.sub(new_css, text)

    # 5. Modal HTML 교체
    old_modal = '''<!-- Full View Modal -->
<div class="modal-overlay" id="imageModal" onclick="closeModal()">
  <div class="modal-content" onclick="event.stopPropagation()">
    <div class="modal-header">
      <div class="modal-title" id="modalTitle">마법 정보</div>
      <button class="modal-close" onclick="closeModal()">&times;</button>
    </div>
    <div class="modal-body">
      <img id="modalImg" class="modal-img" src="" alt="마법 전체 보기">
    </div>
  </div>
</div>'''

    new_modal = '''<!-- Full View / Swipe Slider Modal -->
<div class="modal-overlay" id="imageModal" onclick="closeModal()">
  <div class="modal-content" onclick="event.stopPropagation()">
    <div class="modal-header">
      <div class="modal-title" id="modalTitle">마법 정보</div>
      <button class="modal-close" onclick="closeModal()">&times;</button>
    </div>
    
    <!-- 슬라이더 탭 (모험마법 / 전투마법) -->
    <div class="slider-tabs" id="sliderTabs">
      <button class="slider-tab-btn active" id="tabAdventure" onclick="goToSlide(0)">🗺️ 모험마법 책</button>
      <button class="slider-tab-btn" id="tabCombat" onclick="goToSlide(1)">⚔️ 전투마법 책</button>
    </div>

    <!-- 스와이프 슬라이더 래퍼 -->
    <div class="slider-wrapper" id="sliderWrapper">
      <button class="slide-nav-btn slide-prev" onclick="prevSlide()">&lsaquo;</button>
      <button class="slide-nav-btn slide-next" onclick="nextSlide()">&rsaquo;</button>

      <div class="slider-track" id="sliderTrack">
        <div class="slider-slide">
          <img id="modalImgAdventure" class="modal-img" src="" alt="모험마법 책">
        </div>
        <div class="slider-slide">
          <img id="modalImgCombat" class="modal-img" src="" alt="전투마법 책">
        </div>
      </div>
    </div>

    <!-- 슬라이더 도트 인디케이터 -->
    <div class="slider-dots" id="sliderDots">
      <span class="dot active" onclick="goToSlide(0)"></span>
      <span class="dot" onclick="goToSlide(1)"></span>
    </div>
  </div>
</div>'''
    text = text.replace(old_modal, new_modal)

    # 6. Script 교체
    new_script = '''<script>
let currentMagic = "ALL";
let currentType = "ALL";
let currentSlideIndex = 0;

// 마법 계열 탭 필터
document.querySelectorAll("#magicTabs .magic-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll("#magicTabs .magic-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    currentMagic = btn.getAttribute("data-magic");
    applyFilters();
  });
});

// 마법 분류(모험/전투) 필터
document.querySelectorAll("#typeTabs .type-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll("#typeTabs .type-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    currentType = btn.getAttribute("data-type");
    applyFilters();
  });
});

// 검색 및 필터링 통합 함수
function applyFilters() {
  const searchTerm = (document.getElementById("magicSearchInput").value || "").trim().toLowerCase();
  const sections = document.querySelectorAll(".element-section");

  sections.forEach(sec => {
    const secMagic = sec.getAttribute("data-element");
    const matchesMagic = (currentMagic === "ALL" || currentMagic === secMagic);

    const catBlocks = sec.querySelectorAll(".category-block");
    let totalVisibleSpellsInSec = 0;

    catBlocks.forEach(block => {
      const cat = block.getAttribute("data-cat");
      const matchesCat = (currentType === "ALL" || currentType === cat);

      const spellItems = block.querySelectorAll(".spell-item");
      let visibleSpellsInBlock = 0;

      spellItems.forEach(item => {
        const spellName = item.querySelector(".spell-name").innerText.toLowerCase();
        const matchesSearch = !searchTerm || spellName.includes(searchTerm);

        if (matchesCat && matchesSearch) {
          item.style.display = "flex";
          visibleSpellsInBlock++;
        } else {
          item.style.display = "none";
        }
      });

      if (matchesCat && visibleSpellsInBlock > 0) {
        block.style.display = "block";
        totalVisibleSpellsInSec += visibleSpellsInBlock;
      } else {
        block.style.display = "none";
      }
    });

    if (matchesMagic && totalVisibleSpellsInSec > 0) {
      sec.style.display = "block";
    } else {
      sec.style.display = "none";
    }
  });
}

// ── 모달 & 2-Slice 스와이프 슬라이더 제어 ─────────
function openBookModal(elementName, initialSlide = 0) {
  document.getElementById("modalTitle").innerText = `${elementName} 전체 마법책`;
  
  document.getElementById("modalImgAdventure").src = `images/magic/${elementName}/모험마법.jpg`;
  document.getElementById("modalImgCombat").src = `images/magic/${elementName}/전투마법.jpg`;

  // 슬라이더 UI 노출
  document.getElementById("sliderTabs").style.display = "flex";
  document.getElementById("sliderDots").style.display = "flex";
  document.querySelectorAll(".slide-nav-btn").forEach(btn => btn.style.display = "flex");

  goToSlide(initialSlide);

  document.getElementById("imageModal").classList.add("active");
  document.body.style.overflow = "hidden";
}

// 개별 단일 마법 클릭 시 (슬라이더 없이 단일 이미지 보기)
function openModal(title, imgSrc) {
  document.getElementById("modalTitle").innerText = title;
  document.getElementById("modalImgAdventure").src = imgSrc;

  // 단일 마법일 때는 탭과 슬라이드 버튼 숨김
  document.getElementById("sliderTabs").style.display = "none";
  document.getElementById("sliderDots").style.display = "none";
  document.querySelectorAll(".slide-nav-btn").forEach(btn => btn.style.display = "none");

  goToSlide(0);

  document.getElementById("imageModal").classList.add("active");
  document.body.style.overflow = "hidden";
}

function goToSlide(index) {
  currentSlideIndex = index;
  const track = document.getElementById("sliderTrack");
  track.style.transform = `translateX(-${index * 50}%)`;

  const tabs = document.querySelectorAll(".slider-tab-btn");
  tabs.forEach((tab, i) => {
    if (i === index) tab.classList.add("active");
    else tab.classList.remove("active");
  });

  const dots = document.querySelectorAll(".slider-dots .dot");
  dots.forEach((dot, i) => {
    if (i === index) dot.classList.add("active");
    else dot.classList.remove("active");
  });
}

function prevSlide() {
  goToSlide(currentSlideIndex === 0 ? 1 : 0);
}

function nextSlide() {
  goToSlide(currentSlideIndex === 0 ? 1 : 0);
}

function closeModal() {
  document.getElementById("imageModal").classList.remove("active");
  document.body.style.overflow = "";
}

// 터치 & 마우스 드래그 스와이프 제어
const sliderWrapper = document.getElementById("sliderWrapper");
let startX = 0;
let isDragging = false;

sliderWrapper.addEventListener("touchstart", (e) => {
  startX = e.touches[0].clientX;
}, { passive: true });

sliderWrapper.addEventListener("touchend", (e) => {
  const endX = e.changedTouches[0].clientX;
  handleSwipe(startX, endX);
}, { passive: true });

sliderWrapper.addEventListener("mousedown", (e) => {
  startX = e.clientX;
  isDragging = true;
});

sliderWrapper.addEventListener("mouseup", (e) => {
  if (!isDragging) return;
  isDragging = false;
  handleSwipe(startX, e.clientX);
});

function handleSwipe(start, end) {
  const diff = start - end;
  if (Math.abs(diff) > 40) {
    if (diff > 0) {
      goToSlide(1); // 왼쪽으로 드래그 -> 다음 슬라이드(전투마법)
    } else {
      goToSlide(0); // 오른쪽으로 드래그 -> 이전 슬라이드(모험마법)
    }
  }
}

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") closeModal();
  if (document.getElementById("imageModal").classList.contains("active")) {
    if (e.key === "ArrowLeft") goToSlide(0);
    if (e.key === "ArrowRight") goToSlide(1);
  }
});
</script>'''
    script_pattern = re.compile(r'<script>[\s\S]*?</script>')
    text = script_pattern.sub(new_script, text)

    with open('homm3_magic_info.html', 'w', encoding='utf-8') as f:
        f.write(text)

    print("Success updating homm3_magic_info.html")

if __name__ == '__main__':
    update_magic_page()
