const JOBS_DATA = [
  // ── 1. 순수 전사 계열 ──────────────────────────────────────────────
  {
    id: "master_warrior",
    nameKo: "마스터 전사",
    nameEn: "Master Warrior",
    category: "warrior",
    tier: "Master",
    pointsReq: "전사 32 pts",
    reqDesc: "전사 스킬 포인트 32 달성",
    tagCode: "W",
    imageMale: "images/jobs/master_warrior.png",
    imageFemale: "images/jobs/master_warrior_f.png",
    summary: "기본적인 부대 공격력과 치명타 확률을 강화하는 전사 입문 직업",
    traits: [
      { name: "최대 데미지 +10%", type: "buff" },
      { name: "크리티컬 +10%", type: "buff" }
    ],
    skills: [
      {
        name: "훈련 마스터",
        desc: "전투의 달인인 전사는 그의 군대를 훈련시킬 수 있습니다. 모든 유닛이 +10%의 최대 데미지를 가집니다."
      },
      {
        name: "크리티컬 공격",
        desc: "당신의 군대는 적의 약점을 찾아 공격할 수 있습니다. +10%의 크리티컬 확률이 상승합니다."
      }
    ]
  },
  {
    id: "gm_warrior",
    nameKo: "그랜드마스터 전사",
    nameEn: "Grandmaster Warrior",
    category: "warrior",
    tier: "Grandmaster",
    pointsReq: "전사 55 pts",
    reqDesc: "전사 스킬 포인트 55 달성",
    tagCode: "WW",
    imageMale: "images/jobs/gm_warrior.png",
    imageFemale: "images/jobs/gm_warrior_f.png",
    summary: "각성 마법을 자동 습득하고 부관 및 심복 전투력과 부대 치명타를 대폭 강화",
    specialNote: "그랜드마스터 전사를 포함하는 직업군은 마법 '각성'을 자동으로 배웁니다.",
    traits: [
      { name: "마법 '각성' 습득", type: "special" },
      { name: "최대 데미지 +20%", type: "buff" },
      { name: "크리티컬 +20%", type: "buff" },
      { name: "부관·심복 전투력 +20%", type: "buff" }
    ],
    skills: [
      {
        name: "각성 (Awakening)",
        desc: "그랜드마스터 전사 계열의 고유 권능으로 마법 '각성'을 자동으로 습득합니다."
      },
      {
        name: "엘리트 군대",
        desc: "끝없는 훈련과 예외없는 규율은 당신의 군대를 두려움의 존재로 만들었습니다. 모든 유닛이 +20%의 최대 데미지를 가집니다."
      },
      {
        name: "크리티컬 공격 II",
        desc: "당신의 군대는 적의 약점을 찾아 공격할 수 있습니다. +20%의 크리티컬 확률이 상승합니다."
      },
      {
        name: "부관",
        desc: "당신의 부관이 당신의 전투 능력으로부터 많은 것을 배웠습니다. 부관과 심복의 모든 전투능력 +20%가 적용됩니다."
      }
    ]
  },
  {
    id: "legend_warrior",
    nameKo: "레전드 전사",
    nameEn: "Legend Warrior",
    category: "warrior",
    tier: "Legend",
    pointsReq: "전사 72 pts",
    reqDesc: "전사 스킬 포인트 72 달성 (레전드+마스터 조합 시 레전드 직업으로 유지)",
    tagCode: "WWW",
    imageMale: "images/jobs/legend_warrior.png",
    imageFemale: "images/jobs/legend_warrior_f.png",
    summary: "모든 아군 유닛의 공격 횟수 1회 증가 및 반격 데미지 50% 반감",
    specialNote: "그랜드마스터 전사를 포함하므로 마법 '각성'을 자동으로 배웁니다.",
    traits: [
      { name: "마법 '각성' 습득", type: "special" },
      { name: "아군 공격횟수 +1회", type: "buff" },
      { name: "반격 피해 50% 감소", type: "buff" },
      { name: "최대 데미지 +20%", type: "buff" },
      { name: "크리티컬 +20%", type: "buff" }
    ],
    skills: [
      {
        name: "분노",
        desc: "가장 뛰어난 전사가 지휘하는 군대는 내면의 분노를 이용하여 한계를 뛰어넘습니다. 모든 아군 유닛의 공격횟수가 1회 늘어납니다."
      },
      {
        name: "인내",
        desc: "공격이 최선의 방어이고, 군대는 어떻게 공격해야 반격을 피할 수 있는지 익혔습니다. 반격으로부터 절반의 데미지만 받습니다."
      },
      {
        name: "엘리트 군대",
        desc: "모든 유닛이 +20%의 최대 데미지를 가집니다."
      },
      {
        name: "크리티컬 공격 II",
        desc: "+20%의 크리티컬 확률이 상승합니다."
      }
    ]
  },

  // ── 2. 순수 탐험가 계열 ────────────────────────────────────────────
  {
    id: "master_explorer",
    nameKo: "마스터 탐험가",
    nameEn: "Master Explorer",
    category: "explorer",
    tier: "Master",
    pointsReq: "탐험가 32 pts",
    reqDesc: "탐험가 스킬 포인트 32 달성",
    tagCode: "A",
    imageMale: "images/jobs/master_explorer.png",
    imageFemale: "images/jobs/master_explorer_f.png",
    summary: "아이템/자원/광산 방문 시 이동력 무소모 및 마을 점령 골드 보너스",
    traits: [
      { name: "파밍 이동력 0소모", type: "buff" },
      { name: "점령시 +5,000G & 모병 증가", type: "buff" }
    ],
    skills: [
      {
        name: "약탈 I",
        desc: "골드, 자원, 아티팩트를 이동력 소모 없이 획득할 수 있습니다. 광산을 점령하거나 유닛 저장소를 방문하는데도 이동력이 소모되지 않습니다."
      },
      {
        name: "군주 I",
        desc: "마을을 점령했을 때 5,000 골드를 획득하며, 해당 마을에서 고용 가능한 유닛 수를 늘립니다."
      }
    ]
  },
  {
    id: "gm_explorer",
    nameKo: "그랜드마스터 탐험가",
    nameEn: "Grandmaster Explorer",
    category: "explorer",
    tier: "Grandmaster",
    pointsReq: "탐험가 55 pts",
    reqDesc: "탐험가 스킬 포인트 55 달성",
    tagCode: "AA",
    imageMale: "images/jobs/gm_explorer.png",
    imageFemale: "images/jobs/gm_explorer_f.png",
    summary: "전투 진입/종료 이동력 무소모, 주간 무료 유닛 보급 및 점령 골드 증가",
    traits: [
      { name: "전투 이동력 0소모", type: "buff" },
      { name: "점령시 +10,000G", type: "buff" },
      { name: "매주 추가 유닛 획득", type: "buff" }
    ],
    skills: [
      {
        name: "약탈 II",
        desc: "골드, 자원, 아티팩트를 이동력 소모 없이 획득합니다. 광산/저장소 방문은 물론 전투에도 이동력이 전혀 소모되지 않습니다."
      },
      {
        name: "군주 II",
        desc: "마을 점령 시 10,000 골드를 획득하며 고용 가능 유닛 수를 증가시킵니다."
      },
      {
        name: "다수의 힘",
        desc: "뛰어난 탐험가는 매주 추가적인 유닛을 영웅 부대로 직접 지원받습니다."
      }
    ]
  },
  {
    id: "legend_explorer",
    nameKo: "레전드 탐험가",
    nameEn: "Legend Explorer",
    category: "explorer",
    tier: "Legend",
    pointsReq: "탐험가 72 pts",
    reqDesc: "탐험가 스킬 포인트 72 달성 (레전드+마스터 조합 시 레전드 직업으로 유지)",
    tagCode: "AAA",
    imageMale: "images/jobs/legend_explorer.png",
    imageFemale: "images/jobs/legend_explorer_f.png",
    summary: "자원 습득 시 이동력 오히려 회복, 필드 즉시 유닛 업그레이드 가능",
    traits: [
      { name: "파밍시 이동력 회복", type: "buff" },
      { name: "필드 즉시 업그레이드", type: "special" },
      { name: "점령시 +15,000G", type: "buff" },
      { name: "매주 추가 유닛 획득", type: "buff" }
    ],
    skills: [
      {
        name: "정복자",
        desc: "골드, 자원, 아티팩트를 획득할 때 이동력을 소모하지 않고 오히려 증가합니다! 광산/유닛저장소 방문 및 전투 시에도 이동력이 소모되지 않습니다."
      },
      {
        name: "대군주",
        desc: "마을 점령 시 15,000 골드를 획득하며 마을 내 고용 가능 유닛 수가 대폭 늘어납니다."
      },
      {
        name: "다수의 힘",
        desc: "매주 추가적인 유닛을 지속적으로 획득합니다."
      },
      {
        name: "훈련 교관",
        desc: "가장 뛰어난 탐험가는 모든 훈련에 관한 지식을 보유합니다. 업그레이드되지 않은 유닛을 영웅 창에서 경험치 버튼 우클릭으로 즉시 업그레이드할 수 있습니다."
      }
    ]
  },

  // ── 3. 순수 마법사 계열 ────────────────────────────────────────────
  {
    id: "master_mage",
    nameKo: "마스터 마법사",
    nameEn: "Master Mage",
    category: "mage",
    tier: "Master",
    pointsReq: "마법사 32 pts",
    reqDesc: "마법사 스킬 포인트 32 달성",
    tagCode: "M",
    imageMale: "images/jobs/master_mage.png",
    imageFemale: "images/jobs/master_mage_f.png",
    summary: "전투당 1회 마법 추가 시전(멀티캐스트) 및 마법 피해 20% 감소",
    traits: [
      { name: "전투당 마법 2회 시전 (1회)", type: "buff" },
      { name: "주문 데미지 20% 감소", type: "buff" }
    ],
    skills: [
      {
        name: "멀티캐스트 I",
        desc: "아케인을 수년간 연마한 끝에 전투 중 한 번 주문을 추가로 시전할 수 있게 되었습니다."
      },
      {
        name: "원소 저항",
        desc: "원소 마법의 끝없는 수련 끝에 적 주문으로 받는 데미지가 20% 감소했습니다."
      }
    ]
  },
  {
    id: "gm_mage",
    nameKo: "그랜드마스터 마법사",
    nameEn: "Grandmaster Mage",
    category: "mage",
    tier: "Grandmaster",
    pointsReq: "마법사 55 pts",
    reqDesc: "마법사 스킬 포인트 55 달성",
    tagCode: "MM",
    imageMale: "images/jobs/gm_mage.png",
    imageFemale: "images/jobs/gm_mage_f.png",
    summary: "매 턴마다 주문 2회 시전 가능 및 아케인 선지자 효과",
    traits: [
      { name: "매 턴 마법 2회 시전", type: "buff" },
      { name: "주문 데미지 20% 감소", type: "buff" },
      { name: "아케인 선지자", type: "special" }
    ],
    skills: [
      {
        name: "멀티캐스트 II",
        desc: "아케인에 삶을 헌신한 끝에 매 턴 1번 추가 주문을 쓸 수 있게 되었습니다 (턴당 2회 시전)."
      },
      {
        name: "원소 저항",
        desc: "주문으로 받는 데미지가 20% 감소했습니다."
      },
      {
        name: "아케인 선지자",
        desc: "미래를 보는 능력으로 어떤 주문이 더 효과적인 위력을 발휘할 지 알 수 있습니다."
      }
    ]
  },
  {
    id: "legend_mage",
    nameKo: "레전드 마법사",
    nameEn: "Legend Mage",
    category: "mage",
    tier: "Legend",
    pointsReq: "마법사 72 pts",
    reqDesc: "마법사 스킬 포인트 72 달성 (레전드+마스터 조합 시 레전드 직업으로 유지)",
    tagCode: "MMM",
    imageMale: "images/jobs/legend_mage.png",
    imageFemale: "images/jobs/legend_mage_f.png",
    summary: "마나 소모 없는 공격마법 추가 난사(초토화) 및 주문력 +15, 마법뎀 +15%",
    traits: [
      { name: "매 턴 마법 2회 시전", type: "buff" },
      { name: "초토화 (무료 마법 추가시전)", type: "buff" },
      { name: "마법강화 +15 & 뎀 +15%", type: "buff" },
      { name: "아케인 선지자", type: "special" }
    ],
    skills: [
      {
        name: "초토화",
        desc: "마법 사용 시 마나를 소모하지 않고 임의의 적에게 공격 마법을 자동으로 추가 시전합니다."
      },
      {
        name: "채널링",
        desc: "정신을 집중하여 주문의 위력을 극대화합니다. +15 마법강화(주문력)와 +15% 주문 데미지 보너스를 얻습니다."
      },
      {
        name: "멀티캐스트 II",
        desc: "매 턴 1번 추가 주문을 쓸 수 있습니다."
      },
      {
        name: "아케인 선지자",
        desc: "주문 효율을 직관적으로 통찰할 수 있습니다."
      }
    ]
  },

  // ── 4. 마법사 + 탐험가 계열 ─────────────────────────────────────────
  {
    id: "druid",
    nameKo: "드루이드",
    nameEn: "Druid",
    category: "mage_explorer",
    tier: "Master Dual",
    pointsReq: "마법사 M + 탐험가 M",
    reqDesc: "마스터 마법사(32) + 마스터 탐험가(32)",
    tagCode: "MA",
    imageMale: "images/jobs/druid.png",
    imageFemale: "images/jobs/druid_f.png",
    summary: "전투 후 1개 부대 무료 부활/회복 및 보조 버프 마법 다음 전투로 이월",
    traits: [
      { name: "전투 후 부대 회복", type: "buff" },
      { name: "버프 마법 다음 전투 유지", type: "buff" },
      { name: "전투당 마법 2회 시전 (1회)", type: "buff" }
    ],
    skills: [
      {
        name: "자연치유사",
        desc: "드루이드는 전투 후 한 부대를 회복시킬 수 있습니다. 응급치료텐트를 요구하지 않습니다."
      },
      {
        name: "집중",
        desc: "특별한 드루이드의 능력으로 보조 마법을 다음 전투까지 지속시킵니다. 최대 3개 주문까지 지속되며, 다음 전투에선 1턴 동안 유지됩니다."
      },
      {
        name: "멀티캐스트 I",
        desc: "전투 중 1번 주문을 추가로 시전할 수 있습니다."
      }
    ]
  },
  {
    id: "beast_lord",
    nameKo: "비스트 로드",
    nameEn: "Beast Lord",
    category: "mage_explorer",
    tier: "GM Hybrid",
    pointsReq: "마법사 GM + 탐험가 M",
    reqDesc: "그랜드마스터 마법사(55) + 마스터 탐험가(32)",
    tagCode: "MMA",
    imageMale: "images/jobs/beast_lord.png",
    imageFemale: "images/jobs/beast_lord_f.png",
    summary: "물리 피해 고정 경감(3×영웅레벨) 및 매 전투 지형 맞춤형 유닛 3회 소환",
    traits: [
      { name: "물리 피해 경감 (3×Lv)", type: "buff" },
      { name: "전투마다 유닛 3회 소환", type: "buff" },
      { name: "매 턴 마법 2회 시전", type: "buff" },
      { name: "전투 후 부대 회복", type: "buff" }
    ],
    skills: [
      {
        name: "자연의 수호",
        desc: "자연의 가호로 물리공격을 방어합니다. 모든 공격에 3×영웅레벨의 데미지만큼을 감소시킵니다. (부관 제외)"
      },
      {
        name: "교감",
        desc: "자연과 교감하여 전장의 지형에 맞는 임의의 유닛이 매 전투 3번 소환되어 아군을 돕습니다."
      },
      {
        name: "멀티캐스트 II",
        desc: "매 턴 1번 추가 주문을 쓸 수 있습니다."
      },
      {
        name: "자연치유사",
        desc: "전투 후 한 부대를 회복시킵니다. (텐트 불필요)"
      }
    ]
  },
  {
    id: "cardinal",
    nameKo: "카디널",
    nameEn: "Cardinal",
    category: "mage_explorer",
    tier: "GM Hybrid",
    pointsReq: "마법사 M + 탐험가 GM",
    reqDesc: "마스터 마법사(32) + 그랜드마스터 탐험가(55)",
    tagCode: "MAA",
    imageMale: "images/jobs/cardinal.png",
    imageFemale: "images/jobs/cardinal_f.png",
    summary: "모든 아군 무제한 반격 특성 부여 및 매 전투 아군 전체 3회 버프 마법 시전",
    traits: [
      { name: "전 아군 무제한 반격", type: "buff" },
      { name: "전 아군 버프 3회 자동시전", type: "buff" },
      { name: "물리 피해 경감 (3×Lv)", type: "buff" },
      { name: "점령시 +10,000G", type: "buff" }
    ],
    skills: [
      {
        name: "천상의 무구",
        desc: "카디널의 군대가 사용하는 신성한 무구는 특별한 능력을 부여합니다. 모든 아군이 무제한 반격 특성을 얻습니다."
      },
      {
        name: "신성 개입",
        desc: "군대는 천상의 가호를 받습니다. 매 전투 모든 아군에게 임의의 버프 마법이 3회 시전됩니다."
      },
      {
        name: "수호자",
        desc: "신성한 힘으로 물리공격을 방어하여 모든 공격에 3×영웅레벨의 데미지를 감소시킵니다. (부관 제외)"
      },
      {
        name: "군주 II",
        desc: "마을 점령 시 10,000 골드 및 유닛 고용량을 늘립니다."
      }
    ]
  },

  // ── 5. 전사 + 마법사 계열 ───────────────────────────────────────────
  {
    id: "battle_mage",
    nameKo: "전투마법사",
    nameEn: "Battle Mage",
    category: "warrior_mage",
    tier: "Master Dual",
    pointsReq: "전사 M + 마법사 M",
    reqDesc: "마스터 전사(32) + 마스터 마법사(32)",
    tagCode: "WM",
    imageMale: "images/jobs/battle_mage.png",
    imageFemale: "images/jobs/battle_mage_f.png",
    summary: "전투 개시 전 무상 공격 마법 선제 시전 및 데미지 버프와 멀티캐스트",
    traits: [
      { name: "전투 전 무료 마법 기습", type: "buff" },
      { name: "전투당 마법 2회 시전 (1회)", type: "buff" },
      { name: "최대 데미지 +10%", type: "buff" }
    ],
    skills: [
      {
        name: "마법 기습",
        desc: "파괴적이고 피할 수 없는 주문을 전투 시작 전에 즉시 시전합니다. 주문 점수나 마나를 소모하지 않습니다."
      },
      {
        name: "훈련 마스터",
        desc: "모든 유닛이 +10%의 최대 데미지를 가집니다."
      },
      {
        name: "멀티캐스트 I",
        desc: "전투 중 한 번 주문을 추가로 시전할 수 있습니다."
      }
    ]
  },
  {
    id: "reaver",
    nameKo: "리버",
    nameEn: "Reaver",
    category: "warrior_mage",
    tier: "GM Hybrid",
    pointsReq: "전사 GM + 마법사 M",
    reqDesc: "그랜드마스터 전사(55) + 마스터 마법사(32)",
    tagCode: "WWM",
    imageMale: "images/jobs/reaver.png",
    imageFemale: "images/jobs/reaver_f.png",
    summary: "모든 아군 무반격 공격, 적 전체 최대 체력 -20% 및 전투 승리 시 이동력 +200",
    specialNote: "그랜드마스터 전사를 포함하므로 마법 '각성'을 자동으로 배웁니다.",
    traits: [
      { name: "마법 '각성' 습득", type: "special" },
      { name: "전 아군 무반격 공격", type: "buff" },
      { name: "적 최대 체력 -20%", type: "buff" },
      { name: "전투 승리시 이동력 +200", type: "buff" },
      { name: "최대 데미지 +20%", type: "buff" }
    ],
    skills: [
      {
        name: "전율",
        desc: "적들을 공포에 떨게 만들어 반격을 할 수 없게 만듭니다. 모든 아군이 무반격 공격 특성을 얻습니다."
      },
      {
        name: "워 크라이",
        desc: "위협적인 울부짖음으로 적들의 최대 체력을 20% 깎습니다."
      },
      {
        name: "전쟁의 길",
        desc: "당신의 군대는 파괴와 살육을 즐깁니다. 전투 시마다 이동력이 200 증가합니다."
      },
      {
        name: "엘리트 군대",
        desc: "모든 유닛이 +20%의 최대 데미지를 가집니다."
      }
    ]
  },
  {
    id: "heretic",
    nameKo: "헤레틱",
    nameEn: "Heretic",
    category: "warrior_mage",
    tier: "GM Hybrid",
    pointsReq: "전사 M + 마법사 GM",
    reqDesc: "마스터 전사(32) + 그랜드마스터 마법사(55)",
    tagCode: "WMM",
    imageMale: "images/jobs/heretic.png",
    imageFemale: "images/jobs/heretic_f.png",
    summary: "매 전투 모든 적군에게 디버프 3회 시전, 전투 전 마법 기습 및 이동력 보너스",
    traits: [
      { name: "적 전체 디버프 3회 시전", type: "buff" },
      { name: "전투 전 무료 마법 기습", type: "buff" },
      { name: "매 턴 마법 2회 시전", type: "buff" },
      { name: "전투 승리시 이동력 +200", type: "buff" }
    ],
    skills: [
      {
        name: "공포의 외침",
        desc: "당신의 존재만으로 적들은 전의를 상실합니다. 매 전투 모든 적에게 임의의 디버프 마법을 3회 시전합니다."
      },
      {
        name: "마법 기습",
        desc: "파괴적이고 피할 수 없는 주문을 전투 시작 전에 마나 소모 없이 시전합니다."
      },
      {
        name: "멀티캐스트 II",
        desc: "매 턴 1번 추가 주문을 쓸 수 있습니다."
      },
      {
        name: "전쟁의 길",
        desc: "전투 시마다 이동력이 200 증가합니다."
      }
    ]
  },

  // ── 6. 전사 + 탐험가 계열 ───────────────────────────────────────────
  {
    id: "hunter",
    nameKo: "헌터",
    nameEn: "Hunter",
    category: "warrior_explorer",
    tier: "Master Dual",
    pointsReq: "전사 M + 탐험가 M",
    reqDesc: "마스터 전사(32) + 마스터 탐험가(32)",
    tagCode: "WA",
    imageMale: "images/jobs/hunter.png",
    imageFemale: "images/jobs/hunter_f.png",
    summary: "적 첫 턴 마법 봉쇄 및 모든 사격 유닛의 1턴 우선 행동",
    traits: [
      { name: "적 1턴 마법 봉쇄", type: "buff" },
      { name: "모든 궁수 1턴 우선행동", type: "buff" },
      { name: "최대 데미지 +10%", type: "buff" }
    ],
    skills: [
      {
        name: "마법 방어",
        desc: "당신의 적을 공포에 떨게 만들어, 첫 턴에 아무런 마법도 쓸 수 없게 만듭니다."
      },
      {
        name: "선제 사격",
        desc: "모든 사격 유닛이 첫 턴에 우선적으로 행동합니다."
      },
      {
        name: "훈련 마스터",
        desc: "모든 유닛이 +10%의 최대 데미지를 가집니다."
      }
    ]
  },
  {
    id: "warlord",
    nameKo: "워로드",
    nameEn: "Warlord",
    category: "warrior_explorer",
    tier: "GM Hybrid",
    pointsReq: "전사 GM + 탐험가 M",
    reqDesc: "그랜드마스터 전사(55) + 마스터 탐험가(32)",
    tagCode: "WWA",
    imageMale: "images/jobs/warlord.png",
    imageFemale: "images/jobs/warlord_f.png",
    summary: "모든 아군 브레스 공격 부여(오인사격 없음), 승리 시 영구 스탯 상승 기회",
    specialNote: "그랜드마스터 전사를 포함하므로 마법 '각성'을 자동으로 배웁니다.",
    traits: [
      { name: "마법 '각성' 습득", type: "special" },
      { name: "전 아군 브레스 공격 부여", type: "buff" },
      { name: "전투 승리시 영웅 스탯 증가", type: "buff" },
      { name: "적 1턴 마법 봉쇄", type: "buff" },
      { name: "최대 데미지 +20%", type: "buff" }
    ],
    skills: [
      {
        name: "습격",
        desc: "모든 아군 궁수가 첫 턴에 행동하며, 모든 아군이 브레스 공격을 할 수 있습니다. 또한 브레스 공격이 더 이상 아군을 공격하지 않습니다."
      },
      {
        name: "강행군",
        desc: "워로드의 군대는 전투를 통해 더욱 많은 것을 배웁니다. 매 전투 영웅의 능력치가 영구 상승할 확률이 생깁니다."
      },
      {
        name: "마법 방어",
        desc: "적을 위압하여 첫 턴에 마법을 사용할 수 없게 만듭니다."
      },
      {
        name: "엘리트 군대",
        desc: "모든 유닛이 +20%의 최대 데미지를 가집니다."
      }
    ]
  },
  {
    id: "field_marshal",
    nameKo: "필드 마샬",
    nameEn: "Field Marshal",
    category: "warrior_explorer",
    tier: "GM Hybrid",
    pointsReq: "전사 M + 탐험가 GM",
    reqDesc: "마스터 전사(32) + 그랜드마스터 탐험가(55)",
    tagCode: "WAA",
    imageMale: "images/jobs/field_marshal.png",
    imageFemale: "images/jobs/field_marshal_f.png",
    summary: "아군 전체 비행 및 속도+4, 적 영웅 마나 50% 삭감 및 1턴 마법면역",
    traits: [
      { name: "전 아군 비행 & 속도+4", type: "buff" },
      { name: "적 마나 50% 삭감 & 마법면역", type: "buff" },
      { name: "적 비행 불가 & 속도-4", type: "buff" },
      { name: "점령시 +10,000G", type: "buff" }
    ],
    skills: [
      {
        name: "거룩한 마구",
        desc: "빛을 형상화하여 이용합니다. 모든 아군이 비행 능력을 얻으며 첫 턴에 속도가 4 증가합니다."
      },
      {
        name: "공포의 그림자",
        desc: "본능적인 공포를 심어줍니다. 모든 적들이 비행을 할 수 없게 되며 첫 턴에 속도가 4 감소합니다."
      },
      {
        name: "마법 제압",
        desc: "적 영웅과 전투 시 적 영웅의 마나가 반감되며, 첫 턴에 아군 전체가 마법에 완전 면역이 됩니다."
      },
      {
        name: "군주 II",
        desc: "마을 점령 시 10,000 골드 및 유닛 고용량을 늘립니다."
      }
    ]
  },

  // ── 7. 종결 및 특수 직업 ──────────────────────────────────────────
  {
    id: "general",
    nameKo: "제너럴",
    nameEn: "General",
    category: "special",
    tier: "Trap Master",
    pointsReq: "전사 M + 마법사 M + 탐험가 M",
    reqDesc: "3계열 모두 마스터 달성 시 강제 전직",
    tagCode: "WMA",
    imageMale: "images/jobs/general.png",
    imageFemale: "images/jobs/general_f.png",
    summary: "3계열을 고루 찍었을 때 자동 전직되는 최약체 함정 직업",
    specialNote: "치트를 쓰거나 기존 HOMM3 방식대로 분산 육성하면 전직되며, 모드 내에서 가장 안 좋은 직업으로 설계되었습니다.",
    traits: [
      { name: "최약체 함정 직업", type: "debuff" },
      { name: "최대 데미지 +10%", type: "buff" },
      { name: "점령시 +5,000G", type: "buff" },
      { name: "전투당 마법 2회 시전 (1회)", type: "buff" },
      { name: "이동력 +200", type: "buff" }
    ],
    skills: [
      {
        name: "행군",
        desc: "모든 분야에 능통한 제너럴은 군대를 조금 더 유연하게 운영할 수 있습니다. 200의 추가 이동력을 가집니다."
      },
      {
        name: "훈련 마스터",
        desc: "모든 유닛이 +10%의 최대 데미지를 가집니다."
      },
      {
        name: "군주 I",
        desc: "마을 점령 시 5,000 골드를 획득하며 고용 유닛 수를 늘립니다."
      },
      {
        name: "멀티캐스트 I",
        desc: "전투 중 한 번 주문을 추가로 시전할 수 있습니다."
      }
    ]
  },
  {
    id: "guardian",
    nameKo: "가디언",
    nameEn: "Guardian",
    category: "special",
    tier: "Double GM",
    pointsReq: "마법사 GM + 탐험가 GM",
    reqDesc: "그랜드마스터 마법사(55) + 그랜드마스터 탐험가(55) (아티팩트 필요)",
    tagCode: "MMAA",
    imageMale: "images/jobs/guardian.png",
    imageFemale: "images/jobs/guardian_f.png",
    summary: "매 턴 아군 전체 부활 시전 (단, 모든 유닛 생명체화 및 최대체력 -20%)",
    specialNote: "그랜드마스터 2개를 동시 달성해야 하므로 특수 아티팩트 지원이 필요합니다.",
    traits: [
      { name: "매 턴 전 아군 부활 자동시전", type: "buff" },
      { name: "전 유닛 생명체화 (정신마법 취약)", type: "debuff" },
      { name: "최대 생명력 -20% 감소", type: "debuff" }
    ],
    skills: [
      {
        name: "불사",
        desc: "가디언의 군대는 생명의 계약으로 축복받아, 매 턴마다 모든 아군 부대에게 부활(Resurrection) 마법을 자동으로 시전합니다."
      },
      {
        name: "생명의 축복 (페널티)",
        desc: "모든 아군이 자연의 섭리를 따라 생명체가 되며(언데드/기계도 포함), 정신 마법의 영향을 받게 됩니다. 또한 최대 생명력이 20% 감소합니다."
      }
    ]
  },
  {
    id: "slayer",
    nameKo: "슬레이어",
    nameEn: "Slayer",
    category: "special",
    tier: "Double GM",
    pointsReq: "전사 GM + 마법사 GM",
    reqDesc: "그랜드마스터 전사(55) + 그랜드마스터 마법사(55) (아티팩트 필요)",
    tagCode: "WWMM",
    imageMale: "images/jobs/slayer.png",
    imageFemale: "images/jobs/slayer_f.png",
    summary: "아군 공격 시 무작위 공격마법 난사 (단, 시야 대폭 감소 및 턴당 마나 증발)",
    specialNote: "그랜드마스터 전사를 포함하므로 마법 '각성'을 자동으로 배웁니다.",
    traits: [
      { name: "마법 '각성' 습득", type: "special" },
      { name: "타격시 무작위 공격마법 자동시전", type: "buff" },
      { name: "영웅 시야 대폭 감소", type: "debuff" },
      { name: "매 턴 영웅Lv만큼 마나 소모", type: "debuff" }
    ],
    skills: [
      {
        name: "어둠의 의식",
        desc: "슬레이어의 군대는 금지된 마법으로 무장되어 있습니다. 모든 아군이 공격할 때마다 대상에게 임의의 공격 마법이나 디버프를 즉시 시전합니다."
      },
      {
        name: "피의 댓가 (페널티)",
        desc: "금지된 마법의 댓가로 영웅의 시야가 크게 줄어들며, 전투 중 매 턴 영웅 레벨만큼의 마나를 강제로 잃습니다."
      }
    ]
  },
  {
    id: "avenger",
    nameKo: "어벤저",
    nameEn: "Avenger",
    category: "special",
    tier: "Double GM",
    pointsReq: "전사 GM + 탐험가 GM",
    reqDesc: "그랜드마스터 전사(55) + 그랜드마스터 탐험가(55) (아티팩트 필요)",
    tagCode: "WWAA",
    imageMale: "images/jobs/avenger.png",
    imageFemale: "images/jobs/avenger_f.png",
    summary: "첫 턴 모든 적 행동 불가 & 아군 전장 무제한 이동 (단, 전투당 이동력 추가소모)",
    specialNote: "그랜드마스터 전사를 포함하므로 마법 '각성'을 자동으로 배웁니다.",
    traits: [
      { name: "마법 '각성' 습득", type: "special" },
      { name: "첫 턴 모든 적 행동 불가 (턴 스킵)", type: "buff" },
      { name: "첫 턴 아군 전장 무제한 이동", type: "buff" },
      { name: "전투시 이동력 추가 소모", type: "debuff" }
    ],
    skills: [
      {
        name: "완벽한 공세",
        desc: "적들이 전투 태세를 마치기 전에 기습하여, 첫 턴에 모든 적군이 일절 행동하지 못하게 합니다. 또한 모든 아군 유닛이 첫 턴에 전장의 어디든 즉시 도달할 수 있습니다."
      },
      {
        name: "경계 태세 (페널티)",
        desc: "군대가 항상 극한의 경계 태세를 유지하여 더 많은 피로가 쌓이며, 전투 시마다 이동력을 추가로 소모합니다."
      }
    ]
  }
];
