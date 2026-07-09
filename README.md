# 🏙️ Repolis — the City of Repos

**sigco3111의 모든 GitHub repo가 사는 3D 도시** · 별빛 학자 셋이 안내하고, 도시 자체가 평생 누적 트래픽을 보여준다

<p align="left">
  <a href="./LICENSE"><img src="https://img.shields.io/github/license/sigco3111/Repolis?style=for-the-badge" alt="License"></a>
  <a href="https://github.com/sigco3111/Repolis/stargazers"><img src="https://img.shields.io/github/stars/sigco3111/Repolis?style=for-the-badge" alt="Stars"></a>
  <a href="https://github.com/sigco3111/Repolis/network/members"><img src="https://img.shields.io/github/forks/sigco3111/Repolis?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/sigco3111/Repolis/actions/workflows/refresh.yml"><img src="https://img.shields.io/github/actions/workflow-status/sigco3111/Repolis/refresh.yml?style=for-the-badge" alt="Build Status"></a>
  <a href="https://github.com/sigco3111?tab=repositories"><img src="https://img.shields.io/github/repos/sigco3111?style=for-the-badge&color=22c55e" alt="sigco3111's public repos"></a>
</p>

<p align="left">
  <a href="https://sigco3111.github.io/Repolis/"><img src="https://img.shields.io/badge/🌆_LIVE-sigco3111.github.io-FF6B6B?style=for-the-badge" alt="Live Demo"></a>
  <a href="https://github.com/sigco3111/Repolis"><img src="https://img.shields.io/badge/🐙_REPO-GitHub-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="https://github.com/sigco3111/gh-traffic-monitor"><img src="https://img.shields.io/badge/📊_DATA-gh--traffic--monitor-4ECDC4?style=for-the-badge" alt="Data Backend"></a>
</p>

---

## ✨ 30초 만에 도시 구경하기

<p align="center">
  <a href="https://sigco3111.github.io/Repolis/">
    <img src="https://sigco3111.github.io/Repolis/assets/banner.svg" alt="Repolis Banner" width="800"/>
  </a>
</p>

### 👉 **[🌆 https://sigco3111.github.io/Repolis/](https://sigco3111.github.io/Repolis/)**

> **WASD**로 도시 걸어다니기 · 🚕 **POLARIS 택시** 호출 · 🌟 **별빛 학자 셋**에게 질문하기 · 🌙 야경 모드

건물 **높이=방문자**, **너비=포크**, **장식=클론**, **정원=조회수**, **지붕 금박=별** — 야경에서는 최근 push한 repo 창문이 빛난다.

---

## 📑 목차

1. [왜 만들었나](#왜-만들었나-why-this-exists)
2. [v0.3.0에서 달라진 점](#v030에서-달라진-점-whats-new)
3. [도시 한눈에](#도시-한눈에-city-at-a-glance)
4. [아키텍처](#아키텍처-architecture)
5. [빠른 시작](#빠른-시작-quick-start)
6. [택시 + 학자](#택시--학자-taxi--scholars)
7. [Kronos Council](#kronos-council)
8. [공유 가능한 도시](#공유-가능한-도시-shareable-towns)
9. [Contribution Library](#contribution-library)
10. [자동화](#자동화-automation)
11. [알려진 한계](#알려진-한계-known-limits)
12. [기술 스택](#기술-스택-tech-stack)
13. [감사와 라이선스](#감사와-라이선스)

---

## 왜 만들었나 (`Why this exists`)

GitHub은 traffic 데이터를 **14일 롤링 윈도우**로만 보여준다. 14일이 지나면 방문자·클론·포크 수가 영원히 사라진다.

| 문제 | 결과 |
|---|---|
| 14일 지난 방문자 데이터 소실 | "내 repo에 지금까지 몇 명 왔지?" 못 답함 |
| 14일 지난 clone 데이터 소실 | 평생 인기 repo 순위 못 만듦 |
| 정적 빌드 | 살아있는 OSS 작업 흐름이 안 보임 |

**Repolis**는 그 데이터를 **매일 누적 CSV로 영구 보존**하고, 그 누적값으로 **3D 도시를 짓는다.** 도시를 걸으면 작업 흐름이 보이고, 야경에서 활발한 repo 창문이 빛난다.

---

## v0.3.0에서 달라진 점 (`What's new`)

이 fork는 [hyeonsangjeon/Repolis](https://github.com/hyeonsangjeon/Repolis) v1.64.0 위에 sigco3111 데이터를 얹은 v0.3.0이다.

| 기능 | 원작 (hyeonsangjeon v1.64.0) | sigco3111 fork v0.3.0 |
|---|---|---|
| 데이터 백엔드 | 자체 `collect_traffic.py` (3-layer CSV) | **[gh-traffic-monitor](https://github.com/sigco3111/gh-traffic-monitor)** (zero-deps, 단일 레이어) |
| 도시 데이터 | 60~80개 repo | **sigco3111의 모든 public repo** (193개, 매일 갱신) |
| Scholar NPC | (없음) | **POLARIS · VEGA · RIGEL** (MCP-grounded, 별자리 표시) |
| Grounded 택시 | (없음) | **🛰️ AI Foundry Live** — Cloudflare Worker가 KB retrieval + in-persona chat |
| Kronos Council | ✅ 있음 | ✅ 그대로 유지 (deterministic debate → verdict, 130+56 checks) |
| Contribution Library | 6 카테고리 × 50+ 항목 (논문/수상/AWS) | **6 카테고리 × 25 작품** (sigco3111 OSS/게임/에이전트/커뮤니티/3D/학습) |
| Shareable towns `?user=` | ✅ 있음 | ✅ 그대로 유지 (남의 도시도 탐험) |
| Multiplayer (PartyKit) | ✅ 있음 | ✅ 그대로 유지 |
| 자동화 | 매일 1회 cron | **이중 cron** — traffic 4h + build 24h |
| 다국어 | 한국어 / 영어 | ✅ 동일 |

---

## 도시 한눈에 (`City at a glance`)

<p align="center">
  <img src="https://sigco3111.github.io/Repolis/assets/social-preview.png" alt="Repolis 도시 미리보기" width="720"/>
</p>

### 📊 라이브 지표

| 지표 | 값 |
|---|---|
| 총 public repo | ![repos](https://img.shields.io/github/repos/sigco3111?style=flat-square&color=22c55e) |
| 도시 데이터 | `repos.json` (매일 cron 자동 갱신, [소스](https://github.com/sigco3111/Repolis/blob/main/repos.json)) |
| 도시 빌드 상태 | ![refresh](https://img.shields.io/github/actions/workflow-status/sigco3111/Repolis/refresh.yml?style=flat-square) |
| Traffic 누적 | `data/logs/_cumulative.csv` (매일 append) |

### 🏗️ 도시 구조 (Traffic → Architecture)

`scripts/build_repos.py`가 누적 트래픽을 점수화하고, `index.html`이 그 점수로 건물을 짓는다:

| 신호 | 건축 요소 |
|---|---|
| 👁 unique visitors | 건물 **높이** |
| ⑂ forks | 건물 **너비** (lot size) |
| ⬇ clones | **장식** (배너, 금테) |
| 📈 views | **정원** · 펜스 |
| ⭐ stars | **지붕 금박** |
| 🌙 최근 push · clones · views | **야경 창문 빛** |

점수 상위 14개는 **다운타운** (high-rise), 나머지는 **동네** (ring-road cottages). [전체 데이터 모델 → `docs/domain-model.md`](docs/domain-model.md)

---

## 아키텍처 (`Architecture`)

```
┌─────────────────────────────────────────────────────────────────────┐
│ 1️⃣  GitHub Actions (cron)                                          │
│     • traffic-refresh.yml  — 4시간마다 traffic만                     │
│     • refresh.yml          — 매일 1회 전체 빌드 + Pages 배포         │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 2️⃣  gh-traffic-monitor                                              │
│     → data/logs/YYYY-MM-DD.csv  (일별)                               │
│     → data/logs/_cumulative.csv  (평생 누적)                         │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 3️⃣  scripts/build_repos.py                                          │
│     • metadata + social 병합 (GraphQL openGraphImageUrl)            │
│     • 점수 = log(visitors)·1.0 + log(clones)·0.7 +                   │
│             log(forks)·0.6 + log(stars)·0.5                          │
│     → repos.json (~30 필드 × N repo, score 순)                       │
└─────────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 4️⃣  GitHub Pages — index.html (단일 파일, Three.js r0.160)         │
│     • 건물 자동 배치 (다운타운 + 동네)                              │
│     • WASD 도보 + WoW-style 카메라                                  │
│     • POLARIS 택시 + 3 학자 NPC + Kronos Council                    │
└─────────────────────────────────────────────────────────────────────┘
```

선택: Grounded AI — [`cloudflare-taxi/`](cloudflare-taxi/) Cloudflare Worker가 POLARIS / VEGA / RIGEL의 KB retrieval과 in-persona chat을 담당한다. Worker가 unconfigured면 모든 모드는 silent Local fallback.

---

## 빠른 시작 (`Quick start`)

### 옵션 1: 라이브 데모 (1초)

👉 **[https://sigco3111.github.io/Repolis/](https://sigco3111.github.io/Repolis/)** 클릭

### 옵션 2: 본인 도시로 빌드 (15분)

```bash
# 1. Fork + clone
gh repo fork sigco3111/Repolis --clone --remote
cd Repolis

# 2. gh-traffic-monitor 설치 (zero-deps, 1분)
git clone https://github.com/sigco3111/gh-traffic-monitor /tmp/gtm
pip install -e /tmp/gtm
python -m gh_traffic_monitor --owner YOUR_USERNAME --log-dir ./data/logs collect

# 3. OWNER 본인 이름으로 교체
sed -i '' "s/const OWNER = 'sigco3111'/const OWNER = 'YOUR_USERNAME'/" index.html

# 4. repos.json 빌드
gh auth login
REPO_OWNER=YOUR_USERNAME python3 scripts/build_repos.py

# 5. 로컬 미리보기
python3 -m http.server 8000   # http://localhost:8000

# 6. GitHub Pages 활성화 + push
gh repo edit YOUR_USERNAME/Repolis --enable-pages --source main --source-path /
git push -u origin main
```

### 옵션 3: Contribution Library를 본인 작품으로

`index.html`의 `LIBDATA` 배열을 본인 작품으로 교체한다. 6개 카테고리 권장:

```js
const LIBDATA = [
  { icon: '🛠️', ko: '시그니처 OSS', en: 'Signature OSS', items: [
    { t: { ko: '내 첫 OSS — ...', en: 'My first OSS — ...' }, m: 'YOU · MIT', u: 'https://github.com/YOU/repo' },
    // ...
  ]},
  // ... 5개 카테고리 더
];
```

---

## 택시 + 학자 (`Taxi & Scholars`)

POLARIS가 도시로 안내하고, VEGA·RIGEL이 질문에 답한다. 각 NPC는 **하나의 MCP 지식 출처**에 grounding되어 있다.

| NPC | 역할 | 지식 출처 (MCP) | 호출법 |
|---|---|---|---|
| 🚕 **POLARIS** · the Wayfinder | 택시 (자연어 → repo 픽업) | GitHub MCP | "가장 인기있는 repo" / "AI agent 관련 repo" |
| 📘 **VEGA** · the Archivist | MS Docs 엔지니어 | Microsoft Learn MCP | "Azure Functions 어떻게 써?" |
| 🗺️ **RIGEL** · the Cartographer | DeepWiki 탐험가 | DeepWiki MCP | "Three.js 구조 설명해줘" |

### 택시 모드 3가지

택시 버튼 → 상단 드롭다운으로 모드 전환. 기본은 **Local**.

| 모드 | 의존성 | 첫 사용 | 품질 |
|---|---|---|---|
| 🟢 **Local** (default) | 0 | 즉시 | 좋음 (synonym + metric 인식) |
| 🟡 **WebLLM** | 브라우저 내 ~1GB 모델 | ~30초 | 더 좋음 (Llama-3.2-1B 추론) |
| 🛰️ **AI Foundry Live** | Cloudflare Worker (`repolis-taxi`) | 즉시 | 최고 (KB-grounded + references) |

**🛰️ AI Foundry Live**는 [Cloudflare Worker](cloudflare-taxi/)가 Azure AI Search KB를 호출해서 grounded 답변 + 참조 문서를 돌려준다. Worker가 없으면 자동으로 Local로 fallback — silent.

### KB miss / 잡담은 "별빛" 경로

질문이 KB 밖(천문학, 신화, 잡담)이거나 KB가 빈 결과를 주면, Worker가 scholar 인격으로 **Azure OpenAI `gpt-5.4-mini` 직접 호출**로 답한다 (keyless Entra service principal). 브라우저에는 `✦ how I answered` 패널로 표시된다.

### 예시 질문 (모든 모드 작동)

```
"가장 인기있는 repo"          → POLARIS가 다운타운 1번 건물로 픽업
"AI agent 관련 repo"          → POLARIS가 토픽 매칭으로 픽업
"Azure Functions 어떻게 써?"   → VEGA가 MS Docs 인용 + 답변
"Three.js 내부 구조 설명"      → RIGEL이 DeepWiki로 답변
"library"                    → Contribution Library 안내
```

---

## Kronos Council

도시에 사는 별도의 **결정 엔진**. 세 비평가(Olddoc · Livewire · Hearsay)가 토론하고, 의장 **KRONOS**가 `source × recency` 가중으로 판결을 내린다.

- **결정론적** — 같은 입력에 항상 같은 판결
- **수학/정형 케이스**: 정확히 검증된 verdict
- **자유 주제 케이스**: AI 추론 + `⚡ unverified` 배지

```
node council/test.mjs        # → "ALL GREEN — 130 checks passed"
node council/test-live.mjs   # → "56 passed, 0 failed"
node scripts/smoke.mjs       # → index.html 정적 회귀 가드
```

Council의 동작 패턴은 [`COUNCIL_PATTERN.md`](COUNCIL_PATTERN.md), 데이터 모델은 [`docs/domain-model.md`](docs/domain-model.md) §7 참고.

---

## 공유 가능한 도시 (`Shareable towns`)

URL에 `?user=<login>`을 붙이면 **아무나의 public GitHub**로 도시를 짓는다:

```
https://sigco3111.github.io/Repolis/?user=mrdoob
https://sigco3111.github.io/Repolis/?user=torvalds
```

- 캐시는 `localStorage` (stale-fallback 포함)
- Cross-town 택시 운전은 비활성 — "🏠 도시로 돌아가기" 버튼으로 owner 도시 복귀
- 유효하지 않은 username이거나 owner와 같으면 owner 도시 그대로

---

## Contribution Library

`index.html`의 `LIBDATA` (또는 별도 빌드된 [`assets/contribution-library.json`](assets/))로 도시 끝 사거리에 **sigco3111 6 카테고리 × 25 작품**을 전시한다:

| 카테고리 | 작품 수 |
|---|---:|
| 🛠️ 시그니처 OSS | 5 |
| 🎮 AI 게임 / 전략 / RPG | 5 |
| 🤖 AI 자동화 / 에이전트 | 4 |
| 🏘️ 커뮤니티 / 실험 | 3 |
| 🎨 3D / 비주얼 / 게임 에셋 | 5 |
| 📚 학습 / 강의 / 데이터 | 3 |

본인 fork로 갈아끼우려면 `index.html`의 `LIBDATA`만 교체하면 된다.

---

## 자동화 (`Automation`)

### 이중 cron (GitHub Actions 무료 한도 내)

| 워크플로 | 트리거 | 효과 | 월 실행 |
|---|---|---|---:|
| `traffic-refresh.yml` | **4시간마다** | `gh-traffic-monitor` 단독, traffic만 | ~180회 |
| `refresh.yml` | **매일 1회** | 전체 빌드 + Pages 배포 | ~30회 |
| `refresh.yml` workflow_dispatch | 수동 | 즉시 전체 빌드 | 무제한 |

### 수동 트리거 (저장소 추가/삭제 즉시 반영)

```bash
gh workflow run refresh.yml --repo sigco3111/Repolis
# → 1~2분 안에 도시 갱신
```

### 자동 테스트 (배포 전 필수)

```bash
node council/test.mjs        # → "ALL GREEN — 130 checks passed"
node council/test-live.mjs   # → "56 passed, 0 failed"
node scripts/smoke.mjs       # → index.html 정적 회귀 가드
node --check scholars.js
node --check cloudflare-taxi/src/grounded.js
```

UI 검증: 로컬 서버 띄우고 Chrome DevTools에서 콘솔 에러 0개 확인 (모바일 390×844 + 데스크톱).

---

## 알려진 한계 (`Known limits`)

- **첫 24~48시간**: GitHub Traffic API가 visitor를 노출하기까지 시간이 걸려 `uniques=0`이 정상이다.
- **14일 룰**: GitHub이 14일 지난 traffic을 지운다 — **매일 실행이 필수**.
- **WebLLM 모드**: 첫 사용 시 ~1GB 모델 다운로드 (캐시됨). WebGPU 미지원 브라우저는 동작 안 함.
- **🛰️ AI Foundry Live**: Cloudflare Worker가 unconfigured면 Local로 fallback. Worker 설정은 [`cloudflare-taxi/README.md`](cloudflare-taxi/README.md).
- **다국어**: 한국어 / 영어만 지원.

---

## 기술 스택 (`Tech stack`)

| 영역 | 기술 |
|---|---|
| 3D 엔진 | **Three.js r0.160** (단일 `index.html` ~5.2k 줄, CDN import map) |
| 빌드 | 없음 — `python3 -m http.server`만 |
| 데이터 | `repos.json` (생성됨, 손으로 편집 금지) |
| 데이터 백엔드 | **[gh-traffic-monitor](https://github.com/sigco3111/gh-traffic-monitor)** (Python, zero-deps) |
| 빌더 | `scripts/build_repos.py` (stdlib only + gh CLI) |
| LLM grounding | Cloudflare Worker [`cloudflare-taxi/`](cloudflare-taxi/) — Azure AI Search KB + MCP |
| LLM in-persona | Azure OpenAI `gpt-5.4-mini` (keyless Entra SP) |
| LLM on-device | WebLLM (Llama-3.2-1B, WebGPU) |
| 결정 엔진 | `council/` (deterministic debate → verdict, 130+56 checks) |
| 멀티플레이어 | PartyKit (Cloudflare Workers) |
| CI/CD | GitHub Actions (월 ~210회) |
| 호스팅 | GitHub Pages |

---

## 감사와 라이선스

### 🙏 Credits

| 기여 | 출처 |
|---|---|
| **원작 + 도시 엔진 + 3 학자 + Council** | [hyeonsangjeon/Repolis](https://github.com/hyeonsangjeon/Repolis) — 단일 HTML 3D 세계 + LLM 택시 + Kronos Council |
| **데이터 백엔드** | [sigco3111/gh-traffic-monitor](https://github.com/sigco3111/gh-traffic-monitor) — 14일 롤링 한계를 매일 누적으로 해결 |
| **3D 라이브러리** | Three.js 커뮤니티 |
| **CI/CD · 호스팅** | GitHub Actions + Pages |

### 📄 License

**MIT** — 원작 hyeonsangjeon/Repolis도 MIT. [`LICENSE`](LICENSE) 참고.

<p align="center">
  <sub>Built with 🏙️ by sigco3111 · 기반 hyeonsangjeon/Repolis v1.64.0 · 데이터 매일 Actions로 갱신</sub>
</p>