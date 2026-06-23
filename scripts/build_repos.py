#!/usr/bin/env python3
"""Repolis data builder (sigco3111 fork — simplified single-layer version).

Aggregates the GitHub traffic history collected by `gh-traffic-monitor`
(stored in ``data/logs/`` and ``data/logs/_cumulative.csv``) with live repo
metadata, and writes ``repos.json`` — the data that powers the Repolis 3D city
(one building per repo).

Differences from the upstream hyeonsangjeon/Repolis builder:
- Single-layer data (gh-traffic-monitor outputs one CSV per day, plus _cumulative.csv)
  instead of three-layer (logs/clones/metadata).
- Designed to consume gh-traffic-monitor's output format directly.
- Forks only included if owner has committed (same as upstream).

Env vars:
  REPO_OWNER  GitHub login (default: sigco3111)
  GTL_DIR    Directory holding _cumulative.csv (default: data/logs)
  OUT         Output path (default: repos.json)
"""
from __future__ import annotations

import csv
import json
import math
import os
import subprocess
import sys
from pathlib import Path

OWNER = os.environ.get("REPO_OWNER", "sigco3111")
GTL_DIR = Path(os.environ.get("GTL_DIR", "data/logs"))
OUT = Path(os.environ.get("OUT", "repos.json"))


def gh_api(path: str) -> list | dict:
    """gh CLI로 GitHub API 호출 (paginated)."""
    out = subprocess.check_output(
        ["gh", "api", "--paginate", path],
        text=True,
        stderr=subprocess.DEVNULL,
    )
    try:
        return json.loads(out) if out.strip() else []
    except json.JSONDecodeError:
        return []


def i_committed(full_name: str) -> bool:
    """OWNER가 이 repo에 커밋한 적 있는지."""
    try:
        out = subprocess.check_output(
            ["gh", "api", f"/repos/{full_name}/commits?author={OWNER}&per_page=1"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
        data = json.loads(out)
        return isinstance(data, list) and len(data) > 0
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        return False


def latest_release(full_name: str) -> dict | None:
    """Latest release tag + date."""
    try:
        d = json.loads(subprocess.check_output(
            ["gh", "api", f"/repos/{full_name}/releases/latest"],
            text=True, stderr=subprocess.DEVNULL,
        ))
        return {"tag": d.get("tag_name") or "", "date": (d.get("published_at") or "")[:10]}
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        return None


def load_cumulative_csv(path: Path) -> dict[str, dict]:
    """gh-traffic-monitor _cumulative.csv → {repo_name: {uniques, clones, forks, first_seen}}"""
    if not path.exists():
        return {}
    out: dict[str, dict] = {}
    with path.open("r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            repo_full = row.get("repo", "")
            name = repo_full.split("/", 1)[-1] if "/" in repo_full else repo_full
            out[name] = {
                "uniques": int(row.get("total_uniques", 0) or 0),
                "clones": int(row.get("total_clones", 0) or 0),
                "forks_cum": int(row.get("total_forks", 0) or 0),
                "first_seen": row.get("first_seen", "") or "",
                "last_updated": row.get("last_updated", "") or "",
            }
    return out


def social_map(owner: str) -> dict[str, dict]:
    """repo name → {url, custom} via GraphQL openGraphImageUrl."""
    out: dict[str, dict] = {}
    cursor = None
    query = (
        "query($owner:String!,$cursor:String){"
        " repositoryOwner(login:$owner){"
        " ... on User { repositories(first:50, ownerAffiliations:OWNER,"
        " isFork:false, privacy:PUBLIC, after:$cursor){"
        " nodes{ name usesCustomOpenGraphImage openGraphImageUrl }"
        " pageInfo{ hasNextPage endCursor } } } } }"
    )
    while True:
        cmd = ["gh", "api", "graphql", "-f", "query=" + query, "-F", f"owner={owner}"]
        if cursor:
            cmd += ["-F", f"cursor={cursor}"]
        try:
            data = json.loads(subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL))
        except (subprocess.CalledProcessError, json.JSONDecodeError):
            break
        conn = (((data.get("data") or {}).get("repositoryOwner") or {}).get("repositories")) or {}
        for n in conn.get("nodes") or []:
            out[n["name"]] = {
                "url": n.get("openGraphImageUrl") or "",
                "custom": bool(n.get("usesCustomOpenGraphImage")),
            }
        page = conn.get("pageInfo") or {}
        if page.get("hasNextPage"):
            cursor = page.get("endCursor")
        else:
            break
    return out


def build() -> int:
    """메인 빌드. Returns: 작성된 repo 수."""
    print(f"[1/3] {OWNER}의 public repo 목록 조회 중...", file=sys.stderr)
    repos = gh_api("/user/repos?per_page=100&affiliation=owner&sort=full_name")
    if not isinstance(repos, list):
        print(f"  ⚠️ gh_api 결과가 list가 아님: {type(repos)}", file=sys.stderr)
        return 0
    print(f"      → {len(repos)}개 repo", file=sys.stderr)

    print(f"[2/3] 누적 CSV 로드 중: {GTL_DIR}/_cumulative.csv", file=sys.stderr)
    cumulative = load_cumulative_csv(GTL_DIR / "_cumulative.csv")
    print(f"      → {len(cumulative)}개 repo 트래픽 데이터", file=sys.stderr)

    print(f"[3/3] social preview + repos.json 빌드 중...", file=sys.stderr)
    social = social_map(OWNER)

    out: list[dict] = []
    for r in repos:
        if r.get("private"):
            continue
        # fork는 owner가 커밋한 적 있을 때만 포함
        if r.get("fork") and not i_committed(r.get("full_name") or f"{OWNER}/{r['name']}"):
            continue

        name = r["name"]
        traffic = cumulative.get(name, {})
        visitors = traffic.get("uniques", 0)
        clones = traffic.get("clones", 0)
        forks_cum = traffic.get("forks_cum", 0)

        stars = r.get("stargazers_count", 0) or 0
        forks = r.get("forks_count", 0) or 0
        full = r.get("full_name") or f"{OWNER}/{name}"

        lic = r.get("license") or {}
        lic_name = lic.get("spdx_id") or lic.get("name") or ""
        if lic_name in ("NOASSERTION", "NONE"):
            lic_name = ""

        rel = latest_release(full)

        # 점수 = 트래픽 + 인기도 종합 (log scale로 작은 repo도 0이 안 되게)
        score = (
            math.log1p(visitors) * 1.0
            + math.log1p(clones) * 0.7
            + math.log1p(forks) * 0.6
            + math.log1p(stars) * 0.5
        )

        out.append({
            "repo": name,
            "desc": (r.get("description") or "").strip(),
            "lang": r.get("language") or "Other",
            "topics": r.get("topics") or [],
            "url": r.get("html_url"),
            "home": (r.get("homepage") or "").strip(),
            "stars": stars,
            "forks": forks,
            "fork": bool(r.get("fork")),
            "views": traffic.get("last_updated", "") and 0,  # 누적 views는 _cumulative에 없음
            "visitors": visitors,
            "clones": clones,
            "size": r.get("size", 0) or 0,
            "open_issues": r.get("open_issues_count", 0) or 0,
            "license": lic_name,
            "archived": bool(r.get("archived")),
            "default_branch": r.get("default_branch") or "main",
            "release_tag": (rel or {}).get("tag", ""),
            "release_date": (rel or {}).get("date", ""),
            "created": (r.get("created_at") or "")[:10],
            "pushed": (r.get("pushed_at") or "")[:10],
            "tracked": name in cumulative,
            "first_seen": traffic.get("first_seen", ""),
            "last_tracked": traffic.get("last_updated", ""),
            "social": (social.get(name) or {}).get("url", ""),
            "social_custom": (social.get(name) or {}).get("custom", False),
            "score": round(score, 3),
        })

    # 점수 순 정렬 + rank 부여
    out.sort(key=lambda x: x["score"], reverse=True)
    for i, o in enumerate(out):
        o["rank"] = i

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")

    downtown = sum(1 for o in out if o["rank"] < 14)
    tracked_n = sum(1 for o in out if o["tracked"])
    forks_n = sum(1 for o in out if o.get("fork"))
    print(f"\nwrote {OUT} with {len(out)} public repos ({forks_n} forks I committed to)")
    print(f"  downtown(rank<14)={downtown} hometown={len(out) - downtown} tracked={tracked_n}")

    return len(out)


if __name__ == "__main__":
    sys.exit(0 if build() > 0 else 1)
