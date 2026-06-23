# 🏙️ Repolis — sigco3111의 도시

> **156개의 GitHub repo가 만드는 3D 도시.** 건물은 트래픽이 자라게 하고, LLM 택시가 안내한다.

<a id="english"></a>

**English summary** — Your GitHub repos aren't a list — they're a 3D city you can walk. Every house is a repo, and its height, brightness, ornaments and garden grow from real traffic (visitors · clones · forks · views). Built on [hyeonsangjeon/Repolis](https://github.com/hyeonsangjeon/Repolis), forked and tuned for [sigco3111](https://github.com/sigco3111)'s 156 public repos. Local LLM taxi (no key) included; WebGPU and Cloudflare AI proxy intentionally omitted for simplicity.

---

## ✨ 무엇이 다른가 (`What makes this fork different`)

원작 [hyeonsangjeon/Repolis](https://github.com/hyeonsangjeon/Repolis)와 비교:

| 측면 | 원작 | **sigco3111 fork** |
|---|---|---|
| 데이터 백엔드 | 자체 `collect_traffic.py` (3-layer CSV) | **[gh-traffic-monitor](https://github.com/sigco3111/gh-traffic-monitor)** (단일 레이어) |
| 의존성 | `gh CLI` + 자체 Python | `gh CLI` + **gh-traffic-monitor zero-deps** |
| 도시 데이터 | 60~80개 repo | **155개 repo** |
| LLM 택시 모드 | Local + WebLLM + AI proxy | **Local only** (WebGPU/proxy 생략) |
| Multi-player (PartyKit) | ✅ 있음 | ✅ 그대로 유지 |
| 데이터 갱신 | 매일 1회 cron | **6시간마다** cron (저장소 추가/삭제 4h 내 반영) |

## 🧠 작동 원리 (`How it works`)

```
┌─────────────────────────────────────────────────────────────┐
│ 1. 매 6시간마다 GitHub Actions 트리거                        │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. gh-traffic-monitor: 154개 repo의 트래픽 수집             │
│    - visitors (uniques · views 14-day rolling)              │
│    - clones (14-day rolling)                                │
│    - forks · stars (cumulative)                             │
│    → data/logs/YYYY-MM-DD.csv (일별)                         │
│    → data/logs/_cumulative.csv (평생 누적)                   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. scripts/build_repos.py: gh API로 metadata + social 병합   │
│    - description · language · topics · license              │
│    - openGraphImageUrl (GraphQL)                            │
│    - latest release tag + date                              │
│    - 점수 = log(visitors)·1.0 + log(clones)·0.7 +            │
│            log(forks)·0.6 + log(stars)·0.5                   │
│    → repos.json (155개 항목, score 내림차순)                 │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. GitHub Pages: index.html (Three.js) 자동 배포              │
│    - 155개 건물을 다운타운(상위 14) + 동네(나머지 141)로 배치 │
│    - WASD/joystick로 도보 이동                              │
│    - LLM 택시가 자연어 질문 → repo 안내 → 픽업 → 운전       │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 로컬에서 실행 (`Try it locally`)

### 1. 데이터 수집

```bash
# gh-traffic-monitor 설치
git clone https://github.com/sigco3111/gh-traffic-monitor
cd gh-traffic-monitor
pip install -e .

# 트래픽 수집
mkdir -p ../Repolis/data/logs
python -m gh_traffic_monitor --owner sigco3111 --log-dir ../Repolis/data/logs collect
```

> 첫 실행은 154개 repo × 3 API 호출 = 약 3분 소요.

### 2. repos.json 빌드

```bash
cd ../Repolis
gh auth login  # 또는 GH_TOKEN 환경 변수
REPO_OWNER=sigco3111 python3 scripts/build_repos.py
```

### 3. 정적 서버로 도시 띄우기

```bash
python3 -m http.server 8000
# 브라우저에서 http://localhost:8000 열기
```

> 빌드 단계 없음 — `index.html` 단일 파일이 모든 걸 처리합니다.

## 📊 데이터 형식 (`Data formats`)

### `data/logs/YYYY-MM-DD.csv` (일별 스냅샷)
gh-traffic-monitor가 매일 생성:

```csv
repo,date,uniques,clones,views,forks,stars
sigco3111/opencode-harness-bridge,2026-06-23,0,325,0,1,1
sigco3111/blog-images,2026-06-23,0,737,0,0,0
...
```

### `data/logs/_cumulative.csv` (평생 누적)
빌더가 직접 읽음:

```csv
repo,first_seen,last_updated,total_uniques,total_clones,total_forks
sigco3111/opencode-harness-bridge,2026-06-23,2026-06-23,0,325,1
...
```

### `repos.json` (도시 데이터)
155개 repo × 30 필드. 점수 순 정렬. `index.html`이 직접 fetch.

## 🎮 도시에서 할 수 있는 것 (`What you can do`)

- **걷기** — WASD / 방향키 / on-screen joystick으로 도보 이동
- **차량 호출** — 화면 우상단 🚕 버튼 → 자연어로 질문 → 택시가 픽업 → 운전
- **건물 클릭** — 도시에 있는 집(repo)에 다가가면 카드 자동 오픈
- **야경 보기** — 🌙/☀️ 토글. 밤에는 활발한 repo 창문에서 빛이 남
- **다른 방문자 보기** — 🟢 실시간 멀티플레이어 (PartyKit 서버)

## 🗺️ 우리 도시 통계 (`Our city, as of 2026-06-23`)

| 지표 | 값 |
|---|---|
| 총 public repo | **155개** |
| 다운타운 (rank < 14) | 14개 |
| 동네 (hometown) | 141개 |
| tracked (트래픽 데이터) | 154개 |
| 언어 1위 | **TypeScript (117개)** |
| 언어 2위 | Python (13개) |
| 언어 3위 | JavaScript (9개) |

점수 상위 5개 (2026-06-23):

| Rank | Repo | Score | Clones | Stars |
|---|---|---|---|---|
| 0 | opencode-harness-bridge | 4.81 | 325 | 1 |
| 1 | blog-images | 4.62 | 737 | 0 |
| 2 | icbm2-knowledge-graph | 4.52 | 213 | 0 |
| 3 | opencode-trading | 4.37 | 171 | 0 |
| 4 | icbm2-skills-marketplace | 4.24 | 234 | 0 |

## 🛠️ 자체 호스팅 (`Run your own city`)

### 전제 조건
1. `gh auth login` (또는 `GH_TOKEN`)
2. GitHub Pages 활성화 (Settings → Pages → Source: `main` / `(root)`)
3. (선택) PartyKit 서버 — 멀티플레이어 기능용

### 단계
```bash
# 1. 이 repo를 본인 계정으로 fork
gh repo fork sigco3111/Repolis --clone --remote

# 2. index.html의 OWNER를 본인 GitHub 이름으로 변경
sed -i '' "s/const OWNER = 'sigco3111'/const OWNER = 'YOUR_USERNAME'/" index.html

# 3. (선택) 본인 "Library" repo URL 설정
#    index.html에서 const LIBREPO=null → 'https://github.com/YOU/your-library' 로 변경

# 4. gh-traffic-monitor 데이터 수집
gh repo clone sigco3111/gh-traffic-monitor /tmp/gtm
pip install -e /tmp/gtm
python -m gh_traffic_monitor --owner YOUR_USERNAME --log-dir ./data/logs collect

# 5. repos.json 빌드
REPO_OWNER=YOUR_USERNAME python3 scripts/build_repos.py

# 6. git push → GitHub Actions가 6시간마다 자동 갱신
git add data/ repos.json
git commit -m "feat: initial city"
git push
```

## 📅 자동화 (Cron schedule)

| 트리거 | 주기 | 효과 |
|---|---|---|
| GitHub Actions schedule | **6시간마다** (`0 */6 * * *`) | 신규 repo ≤ 6h 내 도시 반영 |
| GitHub Actions `workflow_dispatch` | 수동 | `gh workflow run refresh.yml` |
| `push` to `main` on `build_repos.py` | 변경 시 | 빌더 수정 즉시 반영 |

## ⚠️ 주의 (`Caveats`)

- **첫 24~48시간**: GitHub Traffic API가 익명 visitor 데이터를 노출하는 데 시간이 걸립니다. 첫 실행 후 `uniques=0`이어도 정상이에요.
- **14일 룰**: 14일 넘은 데이터는 GitHub이 자체 삭제하므로, **반드시 매일 실행**해야 평생 누적이 정확합니다.
- **WebLLM/AI proxy 택시**: 원작에는 3가지 LLM 모드가 있지만, sigco3111 fork는 **Local only** (의존성 최소화 + zero key). 추후 v0.2.0에서 옵션 추가 예정.

## 🙏 감사의 말

- **[hyeonsangjeon/Repolis](https://github.com/hyeonsangjeon/Repolis)** — 이 도시의 원작자. 196개 파일의 정교한 Three.js 세계 + LLM 택시 + 멀티플레이어.
- **[gh-traffic-monitor](https://github.com/sigco3111/gh-traffic-monitor)** — 14일 롤링 윈도우를 매일 누적으로 해결한 데이터 백엔드.
- **Three.js** — 단일 `index.html` 185KB로 만든 놀라운 3D 엔진.

## 📄 라이선스

MIT — 원작 hyeonsangjeon/Repolis도 MIT.
