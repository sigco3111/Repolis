# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2026-07-09

### 🎉 Fork-based integration with hyeonsangjeon/Repolis v1.64.0

Adopts hyeonsangjeon's latest features while preserving sigco3111's identity.

#### Added (from hyeonsangjeon v1.64.0)
- **Kronos Council system** — Deterministic adjudicator (`council/engine.js`) + live debate streaming via Cloudflare Worker (gpt-5.4-mini SSE).
- **Scholar NPCs** — POLARIS (taxi), VEGA (MS Docs engineer), RIGEL (cartographer) with KB grounding.
- **Cloudflare Grounded Worker** — `cloudflare-taxi/src/grounded.js` for Azure AI Search + GitHub MCP integration.
- **Visual improvements** — Sun sprite rendering, Passport/Course/Stamps UI, Contribution Library landmark.
- **Project structure** — `AGENTS.md`, `docs/domain-model.md`, `llms.txt`, `repolis.yaml`, `.env.example`.
- **Smoke tests** — `scripts/smoke.mjs` for static regression guards.

#### Preserved sigco3111 deltas
- `OWNER = 'sigco3111'` (in `index.html`)
- Korean description (`README.md` + `README.ko.md`)
- sigco3111 Library curation (6 categories × 25 works) — sigco3111의 OSS / 게임 / 에이전트 / 커뮤니티 / 3D / 학습 작품
- gh-traffic-monitor backend (`scripts/build_repos.py` — zero-deps, single layer)
- Dual cron (`traffic-refresh.yml` 4h + `refresh.yml` daily)

#### Changed
- README "What's different" section: now documents v0.3.0 status (was v0.2.0 = "last feature version" policy superseded).

## [0.2.1] - 2026-06-23

### Changed
- **README 최종 갱신** — 라이브 데모 임베드, 배지, 시각 자료, 목차, 다층 옵션, 로드맵
- **로드맵 명시**: v0.2.0이 **기능 추가 마지막 버전**. v0.3.0+는 **성능/안정성/관측성/자동화만**
- CHANGELOG: v0.2.1 항목 추가 (README 갱신 마킹)

### Notes
- 이 버전은 **문서만** 변경. 코드/워크플로/도시 데이터 동일.

## [0.2.0] - 2026-06-23

### Added
- **LLM 택시 3가지 모드 전체 활성화**
  - Local mode (default, 키 0, 결정론적 synonym)
  - WebLLM mode (브라우저 내 Llama-3.2-1B, WebGPU, 키 0, ~1GB 다운로드)
  - AI proxy mode (Vercel/Azure endpoint, 최고 품질)
- **Contribution Library 큐레이션** (sigco3111 6 카테고리 × 23 작품)
  - 🛠️ 시그니처 OSS 도구 (5)
  - 🎮 AI 게임 / 전략 / RPG (5)
  - 🤖 AI 자동화 / 에이전트 (4)
  - 🏘️ 커뮤니티 / 실험 (3)
  - 🎨 3D / 비주얼 / 게임 에셋 (5)
  - 📚 학습 / 강의 / 데이터 (3)
- **이중 cron 자동화**
  - `traffic-refresh.yml`: 4시간마다 gh-traffic-monitor만 (저장소 추가/삭제 빠른 반영)
  - `refresh.yml`: 매일 1회 전체 빌드 (GitHub 무료 한도 보호)
- **.nojekyll**: GitHub Pages Jekyll 처리 비활성화 (이미 v0.1.0에 포함)

### Changed
- index.html: hyeonsangjeon → sigco3111 fork로 모든 라이브러리 데이터 교체 (50+ → 23)
- meta tags: sigco3111.github.io/Repolis/ canonical로 통일
- OWNER constant: sigco3111
- 빌더 스크립트: 단일 레이어 (_cumulative.csv) 소비로 단순화
- 자동화 cron: 6시간 → 4시간 + 매일 분리 (반응성 ↑, 한도 보호)

### Removed
- 원작 hyeonsangjeon의 학술 논문 / 수상 / AWS 활동 / Microsoft 발표 항목 (sigco3111 fork에 부적합)

## [0.1.0] - 2026-06-23

### Added
- 초기 릴리즈 (hyeonsangjeon/Repolis fork)
- 155개 public repo 도시 빌드 (점수 = log visitors + log clones + log forks + log stars)
- 다운타운 (rank < 14) + 동네 (141개) 자동 그라데이션
- gh-traffic-monitor v0.1.0을 데이터 백엔드로 통합
- 6시간 cron 자동 갱신
- README 한/영 병기 + 다층 옵션 구조

### Notes
- 첫 24~48시간은 uniques=0 (GitHub Traffic API 지연)
