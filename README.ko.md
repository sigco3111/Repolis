# 🏙️ Repolis — sigco3111의 도시

> **156개의 GitHub repo가 만드는 3D 도시.** 건물은 트래픽이 자라게 하고, LLM 택시가 안내한다.

이 저장소는 [hyeonsangjeon/Repolis](https://github.com/hyeonsangjeon/Repolis)를 sigco3111에 맞춰 fork한 버전입니다. 자세한 내용은 [README.md](./README.md) 참고.

## 빠른 시작

```bash
git clone https://github.com/sigco3111/Repolis
cd Repolis
gh auth login  # 또는 GH_TOKEN 환경 변수
git clone https://github.com/sigco3111/gh-traffic-monitor /tmp/gtm
pip install -e /tmp/gtm
python -m gh_traffic_monitor --owner sigco3111 --log-dir ./data/logs collect
REPO_OWNER=sigco3111 python3 scripts/build_repos.py
python3 -m http.server 8000  # http://localhost:8000 열기
```

## 라이브 데모

https://sigco3111.github.io/Repolis/

## 라이선스

MIT
