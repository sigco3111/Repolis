# Repolis Fork Update — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace sigco3111/Repolis base with hyeonsangjeon/Repolis v1.64.0, then re-apply 5 sigco3111-specific deltas (OWNER, Korean i18n, Library curation, gh-traffic-monitor, dual cron). All 9 verification scenarios must pass.

**Architecture:** Single-file `index.html` Three.js app is preserved. Base swap is mechanical (copy hyeonsangjeon's new files). Deltas are applied as targeted edits to specific files. Verification is via Playwright + bash + grep.

**Tech Stack:** Three.js r0.160, vanilla JS, Cloudflare Workers, GitHub Actions, Python 3 (gh-traffic-monitor).

**Spec:** `docs/superpowers/specs/2026-07-09-repolis-fork-update-design.md`

**Delta sources (saved before worktree creation):**
- `/tmp/sigco-delta-build_repos.py` (8.6 KB)
- `/tmp/sigco-delta-index.html` (174 KB)
- `/tmp/sigco-delta-README.md` (17 KB)
- `/tmp/sigco-delta-README.ko.md` (846 B)
- `/tmp/sigco-delta-github/workflows/{refresh.yml,traffic-refresh.yml}`

---

## File Structure Changes

```
Repolis/                                    [Working dir = worktree]
├── index.html                              [REPLACE base + DELTAS 1,2,3]
├── README.md                                [DELTA 2]
├── README.ko.md                             [DELTA 2]
├── scripts/
│   ├── build_repos.py                       [DELTA 4 — rewrite]
│   └── smoke.mjs                            [NEW from base]
├── .github/workflows/
│   ├── traffic-refresh.yml                  [DELTA 5 — keep]
│   └── refresh.yml                          [DELTA 5 — keep]
├── council/                                 [NEW from base]
│   ├── engine.js
│   └── council.config.json
├── cloudflare-taxi/                         [NEW from base]
│   ├── src/grounded.js
│   └── README.md
├── scholars.js                              [NEW from base]
├── SCHOLARS.md                              [NEW from base]
├── AGENTS.md                                [NEW from base]
├── docs/
│   ├── domain-model.md                      [NEW from base]
│   └── superpowers/                         [already exists]
│       ├── specs/2026-07-09-repolis-fork-update-design.md
│       └── plans/2026-07-09-repolis-fork-update.md (this file)
├── llms.txt                                 [NEW from base]
├── repolis.yaml                             [NEW from base]
└── .env.example                             [NEW from base]
```

---

## Task 0: Prerequisite — Ensure hyeonsangjeon/Repolis is available locally

**Files:**
- Verify: `/tmp/hyeonsangjeon-Repolis/` (already cloned earlier in session)

- [ ] **Step 1: Verify hyeonsangjeon clone exists**

```bash
ls -la /tmp/hyeonsangjeon-Repolis/index.html /tmp/hyeonsangjeon-Repolis/council/engine.js 2>&1
```

Expected: both files exist (clone was created during brainstorming)

- [ ] **Step 2 (fallback): If clone missing, re-clone**

```bash
git clone --depth=1 https://github.com/hyeonsangjeon/Repolis.git /tmp/hyeonsangjeon-Repolis
ls /tmp/hyeonsangjeon-Repolis/index.html
```

Expected: clone created

---

## Task 1: Create isolated worktree

**Files:**
- Create: `../Repolis-update/` (git worktree)

- [ ] **Step 1: Check current git state in Repolis**

Run: `git status --short && git branch --show-current && git log --oneline -3`
Expected: clean working tree on `main`, head at `bfa9258` or similar

- [ ] **Step 2: Create worktree on new branch**

```bash
cd /Users/hjshin/Desktop/project/work/ai-driven-dev/Repolis
git worktree add -b feat/repolis-fork-update ../Repolis-update main
```

Expected: worktree created, new branch `feat/repolis-fork-update`

- [ ] **Step 3: Verify worktree is functional**

Run: `cd ../Repolis-update && git status && git branch --show-current`
Expected: `On branch feat/repolis-fork-update`, clean working tree

- [ ] **Step 4: All subsequent work happens in `../Repolis-update/`**

---

## Task 2: Replace base — copy hyeonsangjeon's new files (additive)

**Files (NEW, all from hyeonsangjeon/Repolis):**
- `council/engine.js`
- `council/council.config.json`
- `cloudflare-taxi/src/grounded.js`
- `cloudflare-taxi/README.md`
- `scholars.js`
- `SCHOLARS.md`
- `AGENTS.md`
- `docs/domain-model.md`
- `scripts/smoke.mjs`
- `llms.txt`
- `repolis.yaml`
- `.env.example`

- [ ] **Step 1: Copy `council/` directory from hyeonsangjeon**

```bash
cd /Users/hjshin/Desktop/project/work/ai-driven-dev/Repolis-update
cp -r /tmp/hyeonsangjeon-Repolis/council/ ./council/
ls council/
```

Expected: `engine.js  council.config.json`

- [ ] **Step 2: Copy `cloudflare-taxi/` directory**

```bash
cp -r /tmp/hyeonsangjeon-Repolis/cloudflare-taxi/ ./cloudflare-taxi/
ls cloudflare-taxi/ cloudflare-taxi/src/
```

Expected: `README.md  src/` and `src/grounded.js`

- [ ] **Step 3: Copy scholar + docs + infra files**

```bash
cp /tmp/hyeonsangjeon-Repolis/scholars.js ./scholars.js
cp /tmp/hyeonsangjeon-Repolis/SCHOLARS.md ./SCHOLARS.md
cp /tmp/hyeonsangjeon-Repolis/AGENTS.md ./AGENTS.md
cp /tmp/hyeonsangjeon-Repolis/docs/domain-model.md ./docs/domain-model.md
cp /tmp/hyeonsangjeon-Repolis/scripts/smoke.mjs ./scripts/smoke.mjs
cp /tmp/hyeonsangjeon-Repolis/llms.txt ./llms.txt
cp /tmp/hyeonsangjeon-Repolis/repolis.yaml ./repolis.yaml
cp /tmp/hyeonsangjeon-Repolis/.env.example ./.env.example
ls scholars.js SCHOLARS.md AGENTS.md docs/domain-model.md scripts/smoke.mjs llms.txt repolis.yaml .env.example
```

Expected: all 8 files present

- [ ] **Step 4: Commit**

```bash
git add council/ cloudflare-taxi/ scholars.js SCHOLARS.md AGENTS.md docs/domain-model.md scripts/smoke.mjs llms.txt repolis.yaml .env.example
git -c user.email=sisyphus@anthropic.local -c user.name=Sisyphus commit -m "feat(base): adopt hyeonsangjeon/Repolis v1.64.0 features

Adds:
- Council system (council/engine.js, council/council.config.json)
- Cloudflare grounded worker (cloudflare-taxi/)
- Scholar NPCs (scholars.js, SCHOLARS.md)
- AGENTS.md project knowledge base
- docs/domain-model.md
- scripts/smoke.mjs regression guards
- llms.txt, repolis.yaml, .env.example"
```

---

## Task 3: Replace `index.html` with hyeonsangjeon's base

**Files:**
- Replace: `index.html` (174 KB → ~190 KB from hyeonsangjeon)

- [ ] **Step 1: Backup current sigco3111 index.html (already saved at `/tmp/sigco-delta-index.html`)**

Verify: `ls -la /tmp/sigco-delta-index.html`
Expected: file exists

- [ ] **Step 2: Replace index.html with hyeonsangjeon's version**

```bash
cd /Users/hjshin/Desktop/project/work/ai-driven-dev/Repolis-update
cp /tmp/hyeonsangjeon-Repolis/index.html ./index.html
wc -l index.html
head -20 index.html
```

Expected: file replaced, ~5000+ lines

- [ ] **Step 3: Verify hyeonsangjeon's content is present**

Run: `grep -c "Three.js r0.160\|Kronos Council\|POLARIS\|scholars" index.html`
Expected: matches > 0

- [ ] **Step 4: Verify sigco3111's old content is gone**

Run: `grep -c "const OWNER = 'sigco3111'" index.html`
Expected: 0 (will be added back in Task 4)

- [ ] **Step 5: Commit**

```bash
git add index.html
git -c user.email=sisyphus@anthropic.local -c user.name=Sisyphus commit -m "feat(base): replace index.html with hyeonsangjeon v1.64.0 base

Adds council UI, scholar UI, sun sprite rendering, course UI, etc.
sigco3111 deltas (OWNER, i18n, LIBDATA) will be re-applied in next tasks."
```

---

## Task 4: Delta 1 — OWNER constant

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Locate current OWNER line in replaced index.html**

Run: `grep -n "const OWNER" index.html | head -5`
Expected: at least one match (likely with default 'hyeonsangjeon' or similar)

- [ ] **Step 2: Replace OWNER constant with sigco3111**

Find the line, e.g.:
```
const OWNER = 'hyeonsangjeon';
```
Replace with:
```
const OWNER = 'sigco3111';
```

Using `edit` tool:
```
oldString: const OWNER = 'hyeonsangjeon';
newString: const OWNER = 'sigco3111';
```

(Adjust oldString if value is different — verify exact value first.)

- [ ] **Step 3: Verify S9 — OWNER constant check**

Run: `grep -c "const OWNER = 'sigco3111'" index.html`
Expected: 1

- [ ] **Step 4: Commit**

```bash
git add index.html
git -c user.email=sisyphus@anthropic.local -c user.name=Sisyphus commit -m "feat(delta): apply Delta 1 — OWNER = 'sigco3111'"
```

---

## Task 5: Delta 2 — Korean description + I18N dict + 🇰🇷 flag

**Files:**
- Modify: `README.md`, `README.ko.md`, `index.html` (I18N dict + 🇰🇷 flag)

- [ ] **Step 1: Find Korean description in current sigco3111 README**

Run: `head -10 /tmp/sigco-delta-README.md`
Expected: Korean title/description (e.g., "🏙️ Repolis — sigco3111의 모든 GitHub repo가 사는 3D 도시")

- [ ] **Step 2: Read current hyeonsangjeon README first 30 lines**

Run: `head -30 README.md`
Expected: English description

- [ ] **Step 3: Add sigco3111's Korean description as secondary subtitle**

In `README.md`, find the line:
```
🏙️ Repolis — the City of Repos
```
Replace with:
```
🏙️ Repolis — the City of Repos
**sigco3111의 모든 GitHub repo가 사는 3D 도시** · 14일 데이터 사라지는 GitHub traffic을 평생 누적으로 보존
```

- [ ] **Step 4: Replace `README.ko.md` with sigco3111's Korean version**

```bash
cp /tmp/sigco-delta-README.ko.md ./README.ko.md
wc -l README.ko.md
```

- [ ] **Step 5: Locate I18N dict in current index.html**

Run: `grep -n "I18N\|const I18N\|const t =" index.html | head -5`
Expected: matches found

- [ ] **Step 6: Locate I18N dict in sigco3111 delta**

Run: `grep -n "I18N\|const I18N\|const t =" /tmp/sigco-delta-index.html | head -5`
Expected: matches found (sigco3111's Korean translations)

- [ ] **Step 7: Extract sigco3111's I18N dict and apply**

Identify the exact `const I18N = {...}` block boundaries in BOTH files. Use `edit` tool to:
- oldString: current I18N block in index.html (hyeonsangjeon's English-only or partial)
- newString: sigco3111's I18N block from `/tmp/sigco-delta-index.html`

Preserve all keys; only change values where sigco3111 has Korean translations.

- [ ] **Step 8: Locate language toggle code**

Run: `grep -n "🇰🇷\|🇺🇸\|lang.*ko\|toggleLang" index.html | head -10`
Expected: matches found

- [ ] **Step 9: Ensure 🇰🇷 flag is present in language toggle**

If `🇰🇷` is missing in current index.html:
- Find the toggle element (e.g., `<span>EN</span>` or `🇺🇸`)
- Replace with Korean flag version: `🇰🇷 / 🇺🇸` toggle

(Check sigco3111 delta for exact format: `grep "🇰🇷" /tmp/sigco-delta-index.html | head -5`)

- [ ] **Step 10: Verify S7 + S8 — README has sigco3111 identity AND Korean i18n**

```bash
grep -c "sigco3111\|gh-traffic-monitor" README.md README.ko.md
grep -c "🇰🇷\|lang.*ko" index.html
```
Expected: matches > 0 in all

- [ ] **Step 11: Commit**

```bash
git add README.md README.ko.md index.html
git -c user.email=sisyphus@anthropic.local -c user.name=Sisyphus commit -m "feat(delta): apply Delta 2 — Korean description + I18N dict + 🇰🇷 flag"
```

---

## Task 6: Delta 3 — Library curation (LIBDATA)

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Locate current LIBDATA in replaced index.html**

Run: `grep -n "const LIBDATA\|const LIBREPO" index.html | head -5`
Expected: matches found

- [ ] **Step 2: Extract sigco3111's LIBDATA block from saved delta**

Run: `grep -n "const LIBDATA\|const LIBREPO" /tmp/sigco-delta-index.html | head -5`
Expected: matches with sigco3111's data

- [ ] **Step 3: Replace LIBDATA + LIBREPO with sigco3111's versions**

Extract the LIBREPO constant + LIBDATA array (lines around 1372 in delta file). Replace same lines in current `index.html`.

Using `edit` tool:
- oldString: lines containing `const LIBREPO=...` and `const LIBDATA=[...]` in current index.html
- newString: lines from `/tmp/sigco-delta-index.html`

(If exact lines differ between bases, manually extract the LIBREPO/LIBDATA block from sigco3111 delta and insert at the matching location.)

- [ ] **Step 4: Verify S2 — Library has 23 items**

Run: `grep -c "items:" <(awk '/const LIBDATA=\[/,/^\];$/' index.html)`
Expected: 6 (categories × items structure)

Manual count check:
```bash
awk '/const LIBDATA=\[/{flag=1;next}/^\];/{flag=0}flag' index.html | grep -c "{"
```
Expected: ~150 lines (6 categories × ~25 entries/items)

- [ ] **Step 5: Commit**

```bash
git add index.html
git -c user.email=sisyphus@anthropic.local -c user.name=Sisyphus commit -m "feat(delta): apply Delta 3 — sigco3111 Library curation (6 cat × 23 works)"
```

---

## Task 7: Delta 4 — gh-traffic-monitor integration

**Files:**
- Replace: `scripts/build_repos.py`

- [ ] **Step 1: Inspect sigco3111's build_repos.py structure**

Run: `head -50 /tmp/sigco-delta-build_repos.py`
Expected: imports `gh_traffic_monitor` package, uses `gh-traffic-monitor` zero-deps

- [ ] **Step 2: Replace build_repos.py with sigco3111's version**

```bash
cd /Users/hjshin/Desktop/project/work/ai-driven-dev/Repolis-update
cp /tmp/sigco-delta-build_repos.py ./scripts/build_repos.py
chmod +x scripts/build_repos.py
head -20 scripts/build_repos.py
```

- [ ] **Step 3: Verify S4 — builder runs without error (dry run if possible)**

Run: `python3 scripts/build_repos.py --help 2>&1 | head -20`
Expected: help text or usage info (or import error if gh_traffic_monitor not installed — that's OK for this session)

- [ ] **Step 4: Verify import**

Run: `python3 -c "import sys; sys.path.insert(0, 'scripts'); import build_repos" 2>&1 | head -5`
Expected: either success or clean ImportError message (no syntax errors)

- [ ] **Step 5: Commit**

```bash
git add scripts/build_repos.py
git -c user.email=sisyphus@anthropic.local -c user.name=Sisyphus commit -m "feat(delta): apply Delta 4 — gh-traffic-monitor integration

Replaces hyeonsangjeon's collect_traffic.py with gh-traffic-monitor (zero-deps).
Preserves sigco3111's preferred data backend."
```

---

## Task 8: Delta 5 — Dual cron (traffic 4h + build daily)

**Files:**
- Verify: `.github/workflows/traffic-refresh.yml` (4-hourly)
- Verify: `.github/workflows/refresh.yml` (daily)
- Copy from: `/tmp/sigco-delta-github/workflows/`

- [ ] **Step 1: Inspect sigco3111's cron files**

Run: `cat /tmp/sigco-delta-github/workflows/traffic-refresh.yml`
Run: `cat /tmp/sigco-delta-github/workflows/refresh.yml`
Expected: cron schedules `0 */4 * * *` and `0 0 * * *`

- [ ] **Step 2: Copy both cron files (sigco3111 originals preserved)**

```bash
cd /Users/hjshin/Desktop/project/work/ai-driven-dev/Repolis-update
cp /tmp/sigco-delta-github/workflows/traffic-refresh.yml ./.github/workflows/traffic-refresh.yml
cp /tmp/sigco-delta-github/workflows/refresh.yml ./.github/workflows/refresh.yml
ls -la .github/workflows/
```

- [ ] **Step 3: Verify cron strings**

Run: `grep -E "cron:|0 \*|0 \*/4" .github/workflows/*.yml`
Expected: matches in both files

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/traffic-refresh.yml .github/workflows/refresh.yml
git -c user.email=sisyphus@anthropic.local -c user.name=Sisyphus commit -m "feat(delta): apply Delta 5 — dual cron (traffic 4h + build daily)"
```

---

## Task 9: Verification — All 9 scenarios

**Tools:** Bash + Playwright (if available) + grep

- [ ] **Step S1: Page loads + city renders**

```bash
cd /Users/hjshin/Desktop/project/work/ai-driven-dev/Repolis-update
python3 -m http.server 8765 &
SERVER_PID=$!
sleep 2
curl -s -o /dev/null -w "%{http_code}" http://localhost:8765/index.html
kill $SERVER_PID
```
Expected: `200`

- [ ] **Step S2: Library shows 23 items (verify via grep)**

```bash
awk '/const LIBDATA=\[/{flag=1;next}/^\];/{flag=0}flag' index.html | grep -oE "\{[^}]*\}" | grep -c "ko:"
```
Expected: ~23 (each entry has one `ko:` field; sigco3111's curation has 23 items)

- [ ] **Step S3a: LLM taxi Local mode (offline fallback)**

This requires browser automation (Playwright). Skip if unavailable:
```bash
grep -c "deterministicIntent\|localIntent" index.html
```
Expected: matches > 0 (fallback code exists)

- [ ] **Step S4: gh-traffic-monitor builder runs**

```bash
python3 scripts/build_repos.py --help 2>&1 | head -10 || \
  python3 -c "import sys; sys.path.insert(0,'scripts'); exec(open('scripts/build_repos.py').read().split(\"if __name__\")[0])" 2>&1 | head -10
```
Expected: no syntax errors (import errors OK if gh_traffic_monitor not installed)

- [ ] **Step S5: Council system files exist**

```bash
ls -la council/ council/engine.js council/council.config.json
head -10 council/engine.js
```
Expected: files exist, header text present

- [ ] **Step S6: Scholar system files exist**

```bash
ls -la scholars.js SCHOLARS.md
head -10 scholars.js
head -10 SCHOLARS.md
```
Expected: files exist, content present

- [ ] **Step S7: README has sigco3111 identity**

```bash
grep -c "sigco3111\|gh-traffic-monitor" README.md
```
Expected: matches > 0

- [ ] **Step S8: Korean i18n toggle code exists**

```bash
grep -c "lang.*ko\|'ko'" index.html | head -1
grep -c "I18N\|i18n" index.html
```
Expected: matches > 0

- [ ] **Step S9: OWNER constant is exactly 'sigco3111'**

```bash
grep -c "const OWNER = 'sigco3111'" index.html
```
Expected: 1

- [ ] **Step ALL: Final summary**

```bash
echo "=== All 9 verification steps ==="
echo "Files added:"
git diff --name-status main..HEAD | grep "^A" | wc -l
echo "Files modified:"
git diff --name-status main..HEAD | grep "^M" | wc -l
echo "Commits:"
git log --oneline main..HEAD
```

Expected: ~10+ commits, mix of adds (council/, cloudflare-taxi/, etc.) and mods (index.html for OWNER/LIBDATA, README for Korean, etc.)

---

## Task 10: Final commit + handoff

- [ ] **Step 1: Verify git log shows all expected commits**

```bash
cd /Users/hjshin/Desktop/project/work/ai-driven-dev/Repolis-update
git log --oneline -15
```

Expected: ~10 commits (base + 5 deltas + intermediate commits)

- [ ] **Step 2: Stage any remaining changes**

```bash
git status
git add -A  # if any untracked
git status  # should be clean
```

- [ ] **Step 3: Update CHANGELOG.md with v0.3.0 entry**

Append to CHANGELOG.md:
```markdown
## [v0.3.0] — 2026-07-09

### 🎉 Fork-based integration with hyeonsangjeon/Repolis v1.64.0
- **Council system**: Deterministic Kronos Council adjudicator + live debate (gpt-5.4-mini SSE).
- **Scholar NPCs**: POLARIS (taxi), VEGA (MS Docs), RIGEL (DeepWiki) — KB-grounded chat.
- **Cloudflare Worker grounded taxi**: Azure AI Search + GitHub MCP integration.
- **Visual improvements**: Sun sprite rendering, Passport/Course/Stamps UI, Contribution Library landmark.
- **Project structure**: AGENTS.md, docs/domain-model.md, llms.txt, repolis.yaml, .env.example.

### Preserved sigco3111 deltas
- OWNER = 'sigco3111'
- Korean description (README.md + README.ko.md)
- Library curation (6 categories × 23 sigco3111 works)
- gh-traffic-monitor backend (zero-deps)
- Dual cron (traffic 4h + build daily)
```

- [ ] **Step 4: Commit CHANGELOG update**

```bash
git add CHANGELOG.md
git -c user.email=sisyphus@anthropic.local -c user.name=Sisyphus commit -m "docs: CHANGELOG v0.3.0 — fork-based integration"
```

- [ ] **Step 5: Final summary report**

Provide:
- Total LOC delta (vs main)
- File counts (added vs modified)
- All 9 verification scenario statuses
- Worktree path (for review/merge)