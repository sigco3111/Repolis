# Repolis Fork Update — Design Spec

**Date:** 2026-07-09
**Status:** Approved
**Author:** Sisyphus (brainstorming session)
**Target project:** sigco3111/Repolis
**Reference project:** hyeonsangjeon/Repolis (v1.64.0)

---

## Context

`hyeonsangjeon/Repolis` (the upstream) has shipped many feature updates up to v1.64.0 since `sigco3111/Repolis` was forked at v0.2.0. The sigco3111 fork is missing those features but has retained its own identity (Korean description, sigco3111-curated Library, `gh-traffic-monitor` backend, dual-cron automation).

The goal is to bring sigco3111/Repolis back to feature parity with hyeonsangjeon's latest, while preserving sigco3111's specific identity deltas.

## Approach: Fork-Based Integration

Replace the base with `hyeonsangjeon/Repolis` (v1.64.0), then re-apply the 5 sigco3111-specific deltas on top.

**Why fork-based instead of feature-by-feature port:**

| | Fork-based | Feature-by-feature port |
|---|---|---|
| Estimated changes | ~400 LOC | ~3000 LOC |
| Risk of inconsistency | Low (single base) | High (merge conflicts) |
| Time | 1 session | 4–8 sessions |
| Coverage of new features | 100% (all features free) | Selective |

## Sigco3111-Specific Deltas (5)

### Delta 1: OWNER constant
- File: `index.html`
- Change: `const OWNER = 'sigco3111';` (top of file)
- Source: line 165 of `Repolis/README.md` quickstart instructions

### Delta 2: Korean description + i18n enhancements
- Files: `README.md`, `README.ko.md`, `index.html` (I18N dict)
- Changes:
  - Korean description in `README.md` front matter and GitHub repo description
  - Korean translations in `I18N` dict (specific strings)
  - Korean emoji (🇰🇷) flag in language toggle
- Source: `Repolis/README.md` lines 27–82, 195–236

### Delta 3: Library curation (6 categories × 23 sigco3111 works)
- File: `index.html` (LIBDATA array)
- Change: Replace generic LIBDATA with sigco3111's curated entries (papers, awards, OSS projects)
- Source: `Repolis/README.md` lines 78 ("6 카테고리 × 23 항목 (sigco3111 큐레이션)") and lines 180–193

### Delta 4: gh-traffic-monitor integration
- File: `scripts/build_repos.py` (rewrite to use `gh-traffic-monitor`)
- Why: hyeonsangjeon uses their own `collect_traffic.py` (3-layer CSV); sigco3111 uses the dedicated `gh-traffic-monitor` Python package (zero-deps, single layer)
- Source: `Repolis/README.md` line 73, line 159, lines 124–127

### Delta 5: Dual cron (traffic 4h + build daily)
- Files: `.github/workflows/traffic-refresh.yml`, `.github/workflows/refresh.yml`
- Change: 4-hourly traffic refresh + daily build (within GH Actions free tier)
- Source: `Repolis/README.md` lines 78, 250–260

## New features acquired "for free" from hyeonsangjeon v1.64.0

| Feature | File(s) | Description |
|---|---|---|
| Kronos Council (deterministic adjudicator) | `council/engine.js`, `council/council.config.json` | Rule-based verdict engine |
| Live Council debate (LLM-streamed) | `cloudflare-taxi/src/grounded.js` | SSE-based real-time debate via gpt-5.4-mini |
| Named scholar NPCs (POLARIS, VEGA, RIGEL) | `scholars.js`, `SCHOLARS.md` | Persona-grounded chat with KB retrieval |
| Cloudflare Worker grounded taxi | `cloudflare-taxi/src/grounded.js` | Azure AI Search KB + GitHub MCP integration |
| Sun sprite rendering | `index.html` (sun renderer) | Billboard sprites with soft halo |
| Passport / Course / Stamps UI | `index.html` | Visit tracking + daily course |
| Contribution Library landmark | `index.html` (extended) | Library as a city landmark |
| Smoke tests | `scripts/smoke.mjs` | Static regression guards |
| Project knowledge base | `AGENTS.md` | Developer map |
| Domain docs | `docs/domain-model.md` | Data schema docs |

## Out of scope (intentional)

- Changing hyeonsangjeon's color/visual brand (Three.js scene keeps hyeonsangjeon's palette)
- Replacing `index.html` architecture (single-file design is preserved)
- Changing OWNER to anything other than 'sigco3111'
- Removing any of the 5 sigco3111 deltas

## Verification Scenarios (Contract)

| ID | Scenario | Pass Condition | Tool |
|---|---|---|---|
| S1 | Page loads + city renders | HTTP 200, city geometry visible | `python3 -m http.server` + Playwright |
| S2 | Library shows 23 items | DOM count = 23, each item has Korean + English | Playwright DOM query |
| S3 | LLM taxi Local mode works | Input "가장 인기있는 repo" → result card shows | Playwright interaction |
| S4 | gh-traffic-monitor builder runs | `python3 scripts/build_repos.py --dry-run` exits 0 | Bash |
| S5 | Council system files exist | `ls council/engine.js` + `cat` shows deterministic code | Bash |
| S6 | Scholar system files exist | `ls SCHOLARS.md scholars.js` + `cat` shows persona registry | Bash |
| S7 | README has sigco3111 identity | grep "sigco3111", "gh-traffic-monitor" in README | grep |
| S8 | Korean i18n toggle works | `?lang=ko` → Korean UI visible | Playwright |
| S9 | OWNER constant is exactly `'sigco3111'` | `grep "const OWNER = 'sigco3111'" index.html` returns 1 line | grep |
| S3a | LLM taxi Local mode (offline fallback) | With no `CLOUDFLARE_API_TOKEN`, Local mode still returns top-K results via deterministic intent | Playwright (offline) |

All 9 scenarios must PASS for completion.

## File-by-file change list

```
Repolis/
├── index.html                     [DELTA 1+2+3] OWNER, I18N, LIBDATA
├── README.md                       [DELTA 2]   Korean description + identity section
├── README.ko.md                    [DELTA 2]   Korean translations
├── scripts/
│   └── build_repos.py              [DELTA 4]   gh-traffic-monitor rewrite
├── .github/workflows/
│   ├── traffic-refresh.yml         [DELTA 5]   4-hourly cron
│   └── refresh.yml                 [DELTA 5]   daily cron
├── council/                        [NEW]       from hyeonsangjeon
│   ├── engine.js
│   └── council.config.json
├── cloudflare-taxi/                [NEW]       from hyeonsangjeon
│   ├── src/grounded.js
│   └── README.md
├── scholars.js                     [NEW]       from hyeonsangjeon
├── SCHOLARS.md                     [NEW]       from hyeonsangjeon
├── AGENTS.md                       [NEW]       from hyeonsangjeon
├── docs/                           [NEW]       from hyeonsangjeon
│   └── domain-model.md
├── scripts/
│   └── smoke.mjs                   [NEW]       from hyeonsangjeon
├── .env.example                    [NEW]       from hyeonsangjeon
├── llms.txt                        [NEW]       from hyeonsangjeon
└── repolis.yaml                    [NEW]       from hyeonsangjeon
```

## Risk register

| Risk | Mitigation |
|---|---|
| `index.html` merge conflict (single-file app) | Use sigco3111's existing `index.html` as base, then port specific hyeonsangjeon sections (council UI, scholar UI, sun renderer) by line-range |
| Library entries lost during merge | Preserve sigco3111's exact 23 items verbatim; preserve reference URL pattern |
| Cron config breaks GH Actions | Test workflow YAML with `act` (local GH Actions runner) before push |
| Existing sigco3111 features regress | Add smoke test scenarios S2, S3, S7 to lock behavior |

## Rollback plan

If verification fails after 3 retry attempts:
1. Revert to current sigco3111/Repolis HEAD (shallow clone at commit 398124e)
2. Document failure in CHANGELOG.md as a known issue
3. Re-scope (smaller delta set) and re-brainstorm

## Next phase

After spec approval:
1. Write implementation plan via `writing-plans` skill
2. Create git worktree `../Repolis-update/` for isolation
3. Execute plan with parallel subagents
4. Verify all 8 scenarios
5. Commit + push to sigco3111/Repolis (or new branch)