# 🏙️ Repolis — sigco3111의 도시

> **sigco3111의 모든 GitHub repo가 사는 3D 도시.** 건물은 트래픽이 자라고, LLM 택시가 안내한다.

<!-- 배지: GitHub 표준 -->
<p align="left">
  <a href="https://github.com/sigco3111/Repolis/blob/main/LICENSE"><img src="https://img.shields.io/github/license/sigco3111/Repolis?style=for-the-badge" alt="License"></a>
  <a href="https://github.com/sigco3111/Repolis/releases"><img src="https://img.shields.io/github/v/release/sigco3111/Repolis?style=for-the-badge" alt="Release"></a>
  <a href="https://github.com/sigco3111/Repolis/stargazers"><img src="https://img.shields.io/github/stars/sigco3111/Repolis?style=for-the-badge" alt="Stars"></a>
  <a href="https://github.com/sigco3111/Repolis/network/members"><img src="https://img.shields.io/github/forks/sigco3111/Repolis?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/sigco3111/Repolis/actions"><img src="https://img.shields.io/github/actions/workflow-status/sigco3111/Repolis/refresh.yml?style=for-the-badge" alt="Build Status"></a>
  <a href="https://github.com/sigco3111?tab=repositories"><img src="https://img.shields.io/github/repos/sigco3111?style=for-the-badge&label=%F0%9F%8F%98%EF%B8%8F_repos&color=22c55e" alt="sigco3111's public repos (live)"></a>
</p>

<p align="left">
  <a href="https://sigco3111.github.io/Repolis/"><img src="https://img.shields.io/badge/🌆_LIVE_DEMO-sigco3111.github.io-FF6B6B?style=for-the-badge" alt="Live Demo"></a>
  <a href="https://github.com/sigco3111/Repolis"><img src="https://img.shields.io/badge/🐙_REPO-GitHub-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="https://github.com/sigco3111/gh-traffic-monitor"><img src="https://img.shields.io/badge/📊_DATA-gh--traffic--monitor-4ECDC4?style=for-the-badge" alt="Data Backend"></a>
</p>

---

## ✨ 30초 만에 도시 구경하기

<p align="center">
  <a href="https://sigco3111.github.io/Repolis/">
    <img src="https://sigco3111.github.io/Repolis/assets/banner.svg" alt="Repolis Banner — sigco3111의 3D 도시" width="800"/>
  </a>
</p>

### 👉 **[🌆 https://sigco3111.github.io/Repolis/](https://sigco3111.github.io/Repolis/)**

> **WASD**로 도시 걸어다니기 · 🚕 버튼으로 **자연어 택시** 호출 · 🏛️ **Contribution Library** 구경하기
> 첫 로딩 후 건물 클릭으로 repo 정보를 보거나, 🌙 토글로 야경 모드 전환.

---

## 🗺️ 목차 (`Table of Contents`)

1. [🌆 라이브 데모](#-30초-만에-도시-구경하기)
2. [🤔 왜 이게 필요한가](#-왜-이게-필요한가-why-this-exists)
3. [✨ 무엇이 다른가](#-무엇이-다른가-what-makes-this-fork-different)
4. [🏙️ 우리 도시 한눈에](#-우리-도시-한눈에-our-city-at-a-glance)
5. [🧠 작동 원리](#-작동-원리-how-it-works)
6. [🚀 빠른 시작](#-빠른-시작-quick-start)
7. [🎮 도시에서 할 수 있는 것](#-도시에서-할-수-있는-것-what-you-can-do)
8. [🚕 택시 3가지 모드](#-택시-3가지-모드-taxi-modes)
9. [📅 자동화](#-자동화-automation)
10. [🗺️ 로드맵](#-로드맵-roadmap)
11. [🙏 감사의 말](#-감사의-말)
12. [📄 라이선스](#-라이선스)

---

## 🤔 왜 이게 필요한가 (`Why this exists`)

GitHub은 repo의 **트래픽 데이터**(방문자, 클론, 포크, 별)를 **14일 롤링 윈도우**로만 보여줍니다. 즉:

| 문제 | 영향 |
|---|---|
| 14일 넘은 방문자 데이터 사라짐 | "내 repo가 지금까지 몇 명 왔지?" 못 답함 |
| 14일 넘은 clone 데이터 사라짐 | "내 코드가 지금까지 몇 번 clone됐지?" 못 답함 |
| 평생 인기 repo 순위 못 만듦 | "내 OSS 중 가장 인기있는 건?" 추적 불가 |

`Repolis`는 이 데이터를 **매일 누적 CSV로 보존**하고, **3D 도시로 시각화**합니다. 건물 높이는 방문자, 너비는 포크, 장식은 클론, 정원 크기는 view, 지붕 금박은 별. **도시를 걸으면 작업 흐름이 보이고, 야경에서 활발한 repo 창문이 빛납니다.**

## ✨ 무엇이 다른가 (`What makes this fork different`)

원작 [hyeonsangjeon/Repolis](https://github.com/hyeonsangjeon/Repolis)와 비교:

| 측면 | 원작 | sigco3111 fork v0.1.0 | **sigco3111 fork v0.2.0** |
|---|---|---|---|
| 데이터 백엔드 | 자체 `collect_traffic.py` (3-layer CSV) | gh-traffic-monitor (단일 레이어) | ✅ 동일 |
| 의존성 | `gh CLI` + 자체 Python | `gh CLI` + gh-traffic-monitor **zero-deps** | ✅ 동일 |
| 도시 데이터 | 60~80개 repo | 전부 (모두 트래픽 추적) | ✅ 동일 |
| LLM 택시 모드 | Local + WebLLM + AI proxy | Local only | **Local + WebLLM + AI proxy (전부)** ✅ |
| Multi-player (PartyKit) | ✅ 있음 | ✅ 그대로 유지 | ✅ 동일 |
| Contribution Library | 6 카테고리 × 50+ 항목 (논문/수상/AWS 활동) | null (비어있음) | **6 카테고리 × 23 항목 (sigco3111 큐레이션)** ✅ |
| 데이터 갱신 | 매일 1회 cron | 6시간마다 cron | **매일 빌드 + 4시간 traffic** (이중 cron) ✅ |
| GitHub Actions 사용 | 1회/일 | 4회/일 | **5회/일** (한도 내) |

## 🏙️ 우리 도시 한눈에 (`Our city at a glance`)

<p align="center">
  <img src="https://sigco3111.github.io/Repolis/assets/social-preview.png" alt="Repolis 도시 미리보기" width="720"/>
</p>

### 📊 도시 통계 (`live` · 매일 자동 갱신)

| 지표 | 값 |
|---|---|
| 총 public repo (live) | ![repos](https://img.shields.io/github/repos/sigco3111?style=flat-square&color=22c55e) |
| 트래픽 추적 중 | _매일 cron으로 `repos.json` 자동 갱신 (정확한 수는 [repos.json](https://github.com/sigco3111/Repolis/blob/main/repos.json) 참고)_ |
| 도시 갱신 | ![refresh](https://img.shields.io/github/actions/workflow-status/sigco3111/Repolis/refresh.yml?style=flat-square) |

### 🎨 언어 분포 (상위 5)

| 언어 | repo 수 | 비율 |
|---|---:|---:|
| TypeScript | 117 | 75% |
| Python | 13 | 8% |
| JavaScript | 9 | 6% |
| HTML | 7 | 5% |
| Other | 9 | 6% |

### 🏆 점수 상위 5개 (트래픽 종합)

| Rank | Repo | 점수 | Clones | 별 | 한 줄 설명 |
|---:|---|---:|---:|---:|---|
| 0 | **opencode-harness-bridge** | 4.81 | 325 | ★1 | Claude Code/Codex → OpenCode 안전 이주 |
| 1 | blog-images | 4.62 | 737 | ★0 | ICBM 블로그 이미지 호스팅 |
| 2 | icbm2-knowledge-graph | 4.52 | 213 | ★1 | 지식 그래프 자동 구축 |
| 3 | opencode-trading | 4.37 | 171 | ★1 | TradingCodex → OpenCode 어댑터 |
| 4 | icbm2-skills-marketplace | 4.24 | 234 | ★0 | 스킬 마켓플레이스 |

## 🧠 작동 원리 (`How it works`)

```
┌─────────────────────────────────────────────────────────────┐
│  1️⃣ GitHub Actions (4시간마다 + 매일 1회) 트리거            │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  2️⃣ gh-traffic-monitor: sigco3111의 모든 공개 repo 트래픽 수집 │
│     → data/logs/YYYY-MM-DD.csv (일별)                      │
│     → data/logs/_cumulative.csv (평생 누적)                  │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  3️⃣ scripts/build_repos.py: metadata + social 병합          │
│     - description · language · topics · license              │
│     - openGraphImageUrl (GraphQL)                            │
│     - 점수 = log(visitors)·1.0 + log(clones)·0.7 +           │
│             log(forks)·0.6 + log(stars)·0.5                  │
│     → repos.json (각 entry ~30 필드, score 순)               │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│  4️⃣ GitHub Pages: index.html (Three.js) 자동 배포            │
│     - 건물 자동 배치 (상위 14 = 다운타운, 나머지 = 동네)     │
│     - WASD/joystick 도보 이동                                │
│     - LLM 택시 3모드 (Local · WebLLM · AI proxy)             │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 빠른 시작 (`Quick start`)

### 옵션 1: 우리 도시 바로 보기 (1초)

👉 **[https://sigco3111.github.io/Repolis/](https://sigco3111.github.io/Repolis/)** 클릭

### 옵션 2: 본인 도시 만들기 (15분)

```bash
# 1. 이 repo를 본인 계정으로 fork
gh repo fork sigco3111/Repolis --clone --remote
cd Repolis

# 2. gh-traffic-monitor 설치 + 트래픽 수집 (3분)
git clone https://github.com/sigco3111/gh-traffic-monitor /tmp/gtm
pip install -e /tmp/gtm
python -m gh_traffic_monitor --owner YOUR_USERNAME --log-dir ./data/logs collect

# 3. OWNER 본인 이름으로 변경
sed -i '' "s/const OWNER = 'sigco3111'/const OWNER = 'YOUR_USERNAME'/" index.html

# 4. repos.json 빌드
gh auth login  # 또는 GH_TOKEN 환경 변수
REPO_OWNER=YOUR_USERNAME python3 scripts/build_repos.py

# 5. 로컬 서버로 미리보기
python3 -m http.server 8000
# 브라우저: http://localhost:8000

# 6. GitHub Pages 활성화 + 푸시
gh repo edit YOUR_USERNAME/Repolis --enable-pages --source main --source-path /
git push -u origin main
```

### 옵션 3: 본인 "Contribution Library" 큐레이션

`index.html`에서 `LIBDATA` 배열을 본인 작품으로 교체:

```js
const LIBREPO = 'https://github.com/YOU/YOUR_BEST_REPO';
const LIBDATA = [
  { icon: '🛠️', ko: '시그니처 OSS', en: 'Signature OSS', items: [
    { t: { ko: '내 첫 OSS — ...', en: 'My first OSS — ...' }, m: 'YOU · MIT', u: '...' },
    // ... 더 추가
  ]},
  // 6개 카테고리 권장
];
```

## 🎮 도시에서 할 수 있는 것 (`What you can do`)

| 동작 | 단축키 | 설명 |
|---|---|---|
| **걷기** | WASD / 방향키 / 화면 joystick | 도보로 도시 탐험 |
| **건물 클릭** | 다가가면 자동 | repo 카드 오픈 + GitHub 링크 |
| **택시 호출** | 우하단 🚕 버튼 | 자연어 질문 → repo 안내 → 픽업 → 운전 |
| **모드 전환** | 🌙 / ☀️ 토글 | 낮↔밤 전환 (밤에 활발한 repo 창문 빛남) |
| **다국어** | 우상단 🇰🇷 / 🇺🇸 | 한국어 ↔ 영어 UI |
| **멀티플레이어** | 🟢 카운터 | 다른 방문자 아바타 실시간 표시 |
| **Library 방문** | 도시 끝 사거리 너머 | Contribution Library (6 카테고리 × 23 작품) |

## 🚕 택시 3가지 모드 (`Taxi modes`)

택시 버튼 클릭 → 상단 드롭다운으로 모드 전환. **기본은 Local mode**.

| 모드 | 키 | 의존성 | 품질 | 첫 사용 |
|---|---|---|---|---|
| **🟢 Local** (default) | ❌ 0 | 0 (의존성 0) | 좋음 (synonym + metric 인식) | 즉시 |
| **🟡 WebLLM** | ❌ 0 | ~1GB 모델 (브라우저 안 LLM) | 더 좋음 (Llama-3.2-1B 추론) | ~30초 |
| **🔵 AI proxy** | ✅ 필요 | Vercel/Azure endpoint | 최고 (Azure OpenAI) | 즉시 |

### 예시 질문 (어떤 모드든 작동)

```
"가장 인기있는 repo"
"AI agent 관련 repo"
"한국어 STT 패키지"
"가장 많이 fork된 repo"
"아무거나"
"library"           ← Contribution Library로 안내
"도시에서 가장 큰 건물"  ← 다운타운 1번 건물
```

### WebLLM 모드 활성화

`index.html`에 이미 구현되어 있어 **드롭다운에서 "WebLLM · 브라우저AI"** 선택만 하면 됩니다.
- 첫 클릭 시 ~1GB 모델을 브라우저가 다운로드 (캐시됨)
- WebGPU 미지원 브라우저(Safari/Firefox 일부)에서는 동작 안 함

### AI proxy 모드 활성화

`api/taxi.js`는 그대로 사용 가능합니다. 본인 Vercel/Azure endpoint가 있다면:

1. Vercel에 이 repo의 `api/taxi.js` 배포
2. 환경 변수 4개 설정:
   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_DEPLOYMENT`
   - `AZURE_OPENAI_KEY`
   - `AZURE_OPENAI_API_VERSION` (기본: `2024-08-01-preview`)
3. 택시 드롭다운에서 "AI 프록시" 선택 → endpoint URL 입력

## 📅 자동화 (`Automation`)

### 이중 cron (GitHub Actions 무료 한도 내)

| 워크플로 | 트리거 | 효과 | 월 실행 |
|---|---|---|---:|
| `traffic-refresh.yml` | **4시간마다** (`0 */4 * * *`) | `gh-traffic-monitor` 단독, traffic만 | ~180회 |
| `refresh.yml` | **매일 1회** (`0 0 * * *`) | 전체 빌드 + Pages 배포 | ~30회 |
| `refresh.yml` workflow_dispatch | 수동 | 즉시 전체 빌드 | 무제한 |
| `refresh.yml` push (빌더 변경) | main 변경 | 빌더 수정 즉시 반영 | 변경마다 |

### 수동 트리거 (가장 빠른 반영)

```bash
# 저장소 추가/삭제 후 즉시 반영
gh workflow run refresh.yml --repo sigco3111/Repolis
# → 1~2분 안에 도시 갱신
```

## 🗺️ 로드맵 (`Roadmap`)

> **v0.2.0이 기능 추가 마지막 버전**입니다. 이후는 **성능/안정성/관측성/자동화** 개선만 진행됩니다.

### ✅ v0.1.0 (2026-06-23) — 도시 첫 빌드
- [x] sigco3111 모든 공개 repo를 도시로 시각화 (점수 기반 그라데이션)
- [x] gh-traffic-monitor v0.1.0 데이터 백엔드
- [x] 6시간 cron 자동 갱신
- [x] GitHub Pages 라이브 (`sigco3111.github.io/Repolis`)

### ✅ v0.2.0 (2026-06-23) — 택시 + Library
- [x] LLM 택시 3모드 (Local + WebLLM + AI proxy)
- [x] Contribution Library (sigco3111 6 카테고리 × 23 작품)
- [x] 이중 cron (traffic 4h + build 24h)
- [x] Social preview (1280×640 PNG)

### 🔜 v0.3.0 — 자동화 + 안정성
- [ ] **자동 social-preview 캡처** (Actions Playwright로 도시 자체 스크린샷)
- [ ] 빌더 캐싱 (etag 기반, 30초 → 10초)
- [ ] gh-traffic-monitor rate limit 자동 백오프
- [ ] cron 실패 알림 (실패 시 텔레그램 DM)
- [ ] 도시 빌드 검증 (repos.json schema check)

### 📋 v0.4.0 — 성능 + 관측성
- [ ] Three.js 메모리 프로파일링 + 최적화
- [ ] 첫 로딩 LCP < 3초
- [ ] cron 실행 메트릭 (성공률, 평균 시간)
- [ ] 도시 빌드 diff (어제 vs 오늘)

### 💭 v0.5.0 — 확장성 + 멀티계정
- [ ] 멀티 owner 지원 (조직/팀 단위 도시)
- [ ] gh-traffic-monitor GraphQL batch
- [ ] GitHub App 인증 (PAT 의존 제거)

## ⚠️ 알려진 한계 (`Known limits`)

- **첫 24~48시간**: GitHub Traffic API가 visitor 데이터를 노출하는 데 시간이 걸립니다. `uniques=0`이어도 정상이에요.
- **14일 룰**: GitHub이 14일 넘은 traffic을 자체 삭제합니다 → **매일 실행이 필수**.
- **WebLLM 모드**: 첫 사용 시 ~1GB 모델 다운로드 (한 번만). WebGPU 미지원 브라우저는 동작 안 함.
- **AI proxy 모드**: 본인 endpoint 필요. 없으면 Local 모드 사용 권장.
- **다국어**: 한국어 / 영어만 지원. 일본어/중국어는 v0.6.0+ 검토.

## 🔧 기술 스택 (`Tech stack`)

| 영역 | 기술 |
|---|---|
| 3D 엔진 | **Three.js** (단일 `index.html` 187KB) |
| 데이터 백엔드 | **[gh-traffic-monitor](https://github.com/sigco3111/gh-traffic-monitor)** (Python, zero-deps) |
| 빌더 | Python `scripts/build_repos.py` (stdlib only + gh CLI) |
| 멀티플레이어 | PartyKit (Cloudflare Workers) |
| LLM 옵션 | 로컬 synonym 매칭 / WebLLM (WebGPU) / Vercel proxy (Azure OpenAI) |
| 호스팅 | GitHub Pages (HTTPS enforced) |
| CI/CD | GitHub Actions (월 ~210회, 무료 한도 내) |

## 🙏 감사의 말 (`Credits`)

| 기여 | 제공 |
|---|---|
| **원작 + 도시 엔진** | [hyeonsangjeon/Repolis](https://github.com/hyeonsangjeon/Repolis) — 196개 파일, 185KB 단일 HTML의 놀라운 3D 세계 + LLM 택시 + 멀티플레이어 |
| **데이터 백엔드** | **[gh-traffic-monitor](https://github.com/sigco3111/gh-traffic-monitor)** — 14일 롤링 한계를 매일 누적으로 해결 |
| **3D 라이브러리** | Three.js 커뮤니티 |
| **CI/CD** | GitHub Actions + Pages |
| **호스팅** | GitHub Pages (무료) |

## 📄 라이선스 (`License`)

MIT — 원작 hyeonsangjeon/Repolis도 MIT.

<p align="center">
  <sub>Built with 🏙️ by sigco3111 · Generated 2026-06-23 · Last updated via GitHub Actions</sub>
</p>
