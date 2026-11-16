#!/usr/bin/env python3
"""PKM 볼트에서 '확정 + 공유 표시' 노트를 LLM 위키 raw 기여본으로 내보낸다.

사용: python3 -I tools/pkm_export.py <볼트 경로> --contributor <핸들> [--out raw] [--dry-run]

선별 기준(GOVERNANCE.md 2장):
  1. 노트 tags 에 share/team 이 있다          ← 사람이 고른다
  2. 유형이 concept·guide·decision·observation·analysis
  3. 확정 상태다 (stable · accepted · recorded)
  4. 직무가 정해진다 (tags 의 job/<직무> 우선, 없으면 jobs.json 의 domain 매핑)
  5. 민감정보 패턴에 걸리지 않는다           ← 걸리면 내보내지 않고 위치만 보고
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOLDERS = ["40_Knowledge", "50_Decisions", "70_Insights"]
TYPES = {"concept", "guide", "decision", "observation", "analysis"}
CONFIRMED = {"stable", "accepted", "recorded"}
SHARE_TAG = "share/team"
WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
LEDGER_HEAD = (
    "# PKM 기여 대장\n\n"
    "위키 본문은 `[PKM-<핸들>-<노트ID>-<리비전>]` 으로 출처를 단다. 파일은 불변 — 새 리비전은 새 파일.\n\n"
    "| ID | 파일 | 제목 | 직무 | 기여자 | 내보낸 날 | 상태 | 비고 |\n"
    "|---|---|---|---|---|---|---|---|\n"
)


def as_list(v):
    return v if isinstance(v, list) else ([v] if v else [])


def pick(front: dict, jobmap: dict, test_all: bool = False) -> tuple[str | None, str | None]:
    """(직무, None) 또는 (None, 제외 사유). test_all 은 기준 1·3(사람 판단·확정)을 건너뛴다."""
    tags = as_list(front.get("tags"))
    if SHARE_TAG not in tags and not test_all:
        return None, "공유 표시 없음"
    if front.get("type") not in TYPES:
        return None, f"유형 제외({front.get('type')})"
    if front.get("status") not in CONFIRMED and not test_all:
        return None, f"미확정({front.get('status')})"
    job = next((t[4:] for t in tags if t.startswith("job/")), None) \
        or jobmap["domain_to_job"].get(front.get("domain"))
    if job not in jobmap["jobs"]:
        return None, f"직무 미지정(domain={front.get('domain')})"
    return job, None


def sensitive_hits(text: str, patterns, blocklist) -> list[str]:
    """걸린 패턴 코드와 줄 번호만 낸다. 값은 절대 출력하지 않는다."""
    hits = []
    for n, line in enumerate(text.splitlines(), 1):
        hits += [f"{code}@{n}" for code, rx in patterns if rx.search(line)]
        hits += [f"BLOCKLIST@{n}" for w in blocklist if w in line]
    return hits


def render(lib, front: dict, body: str, job: str, contributor: str, today: str) -> tuple[str, str]:
    # 위키는 Obsidian 위키링크를 금지한다 → 별칭(없으면 ID)만 남긴다. 링크는 인제스트가 다시 건다.
    body = WIKILINK.sub(lambda m: m.group(2) or m.group(1).split()[0], body).strip()
    rev = hashlib.sha256(f"{front['title']}\n{body}".encode()).hexdigest()[:8]
    meta = {
        "pkm_id": front["id"],
        "pkm_type": front["type"],
        "title": front["title"],
        "job": job,
        "domain": front.get("domain") or "",
        "keywords": as_list(front.get("keywords")),
        "contributor": contributor,
        "revision": rev,
        "exported_at": today,
    }
    return rev, lib.dump_front_matter(meta) + f"\n# {front['title']}\n\n{body}\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("vault")
    ap.add_argument("--contributor", required=True, help="소문자·숫자·하이픈 핸들 (예: swj)")
    ap.add_argument("--out", default=str(ROOT / "raw"))
    ap.add_argument("--dry-run", action="store_true")
    # ponytail: 파이프라인 시험용. 실제 기여에는 쓰지 않는다 — 민감정보 검사(기준 5)는 그대로 돈다
    ap.add_argument("--test-all", action="store_true", help="공유 표시·확정 여부를 무시 (테스트 데이터 전용)")
    a = ap.parse_args(argv)
    if not re.fullmatch(r"[a-z0-9-]+", a.contributor):
        ap.error("--contributor 는 소문자·숫자·하이픈만")

    vault, out = Path(a.vault).expanduser(), Path(a.out)
    sys.path.insert(0, str(vault / "_System/Scripts"))  # 머리말 파서는 볼트 하네스 것을 그대로 쓴다
    import pkm_common as lib

    jobmap = json.loads((ROOT / "jobs.json").read_text(encoding="utf-8"))
    schema = json.loads((vault / "_System/Schemas/sensitive-patterns.json").read_text(encoding="utf-8"))
    patterns = [(p["code"], re.compile(p["regex"])) for p in schema["patterns"]]
    bl = ROOT / ".blocklist"  # 사내 도메인·고객 식별어 등. 공개 저장소라 git 제외
    blocklist = [s.strip() for s in bl.read_text(encoding="utf-8").splitlines()
                 if s.strip() and not s.startswith("#")] if bl.exists() else []
    today = datetime.date.today().isoformat()

    report = {"exported": [], "unchanged": [], "skipped": {}, "unshared": 0}
    rows = []
    for folder in FOLDERS:
        for path in sorted((vault / folder).rglob("*.md")):
            parsed = lib.read_front_matter(path.read_text(encoding="utf-8"))
            if not parsed:
                continue
            front, body = parsed
            job, why = pick(front, jobmap, a.test_all)
            if why == "공유 표시 없음":
                report["unshared"] += 1
                continue
            nid = front.get("id", path.stem)
            if not why:
                rev, doc = render(lib, front, body, job, a.contributor, today)
                hits = sensitive_hits(doc, patterns, blocklist)
                why = f"민감정보 의심({', '.join(hits)})" if hits else None
            if why:
                report["skipped"].setdefault(why, []).append(nid)
                continue
            target = out / job / f"{nid}-{rev}.md"
            if target.exists():
                report["unchanged"].append(nid)
                continue
            prev = sorted(str(p.relative_to(out)) for p in out.glob(f"*/{nid}-*.md"))
            report["exported"].append(str(target.relative_to(out)))
            rows.append(f"| PKM-{a.contributor}-{nid}-{rev} | `{job}/{target.name}` | {front['title']} | {job} "
                        f"| {a.contributor} | {today} | 미처리 | {'대체: ' + ', '.join(prev) if prev else ''} |\n")
            if not a.dry_run:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(doc, encoding="utf-8")

    if rows and not a.dry_run:
        ledger = out / "sources.md"
        text = ledger.read_text(encoding="utf-8") if ledger.exists() else LEDGER_HEAD
        ledger.write_text(text + "".join(rows), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
