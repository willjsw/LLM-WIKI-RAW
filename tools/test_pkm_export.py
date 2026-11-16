"""pkm_export 자기검사. 실행: PKM_VAULT=<볼트> python3 tools/test_pkm_export.py
볼트의 _System(머리말 파서·민감정보 패턴)만 빌려 가짜 볼트를 만들고 돌린다. 실제 노트는 읽지 않는다."""
import contextlib, io, json, os, shutil, sys, tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import pkm_export

REAL = Path(os.environ.get("PKM_VAULT", "~/Documents/Obsidian-PKM/PKM-Test")).expanduser()


def note(vault, name, **front):
    lines = ["---"] + [f"{k}: {v}" if not isinstance(v, list) else f"{k}:\n" + "\n".join(f"  - {x}" for x in v)
                       for k, v in front.items()] + ["---", "", front.pop("_body", "본문. [[CPT-0002 다른 노트|CPT-0002]] 참고.")]
    p = vault / "40_Knowledge" / f"{name}.md"
    p.write_text("\n".join(l for l in lines if not l.startswith("_body")), encoding="utf-8")


def run(vault, out):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        pkm_export.main([str(vault), "--contributor", "tester", "--out", str(out)])
    return json.loads(buf.getvalue())


with tempfile.TemporaryDirectory() as d:
    vault, out = Path(d) / "v", Path(d) / "raw"
    for sub in ("_System/Scripts", "_System/Schemas"):
        shutil.copytree(REAL / sub, vault / sub, ignore=shutil.ignore_patterns("__pycache__"))
    (vault / "40_Knowledge").mkdir()
    base = dict(schema_version=1, type="concept", origin="authored", status="stable", created_at="2026-11-16")
    note(vault, "CPT-0001 공유됨", **base, id="CPT-0001", title="공유됨", domain="jvm", tags=["share/team"])
    note(vault, "CPT-0003 초안", **{**base, "status": "draft"}, id="CPT-0003", title="초안", domain="jvm", tags=["share/team"])
    note(vault, "CPT-0004 비공유", **base, id="CPT-0004", title="비공유", domain="jvm")
    note(vault, "CPT-0005 IP", **base, id="CPT-0005", title="IP", domain="jvm", tags=["share/team"])
    (vault / "40_Knowledge/CPT-0005 IP.md").write_text(
        (vault / "40_Knowledge/CPT-0005 IP.md").read_text().replace("본문.", "서버 10.1.2.3 에 접속."))
    note(vault, "CPT-0006 미매핑", **base, id="CPT-0006", title="미매핑", domain="unknown-x", tags=["share/team"])
    note(vault, "CPT-0007 태그지정", **base, id="CPT-0007", title="태그지정", domain="unknown-x",
         tags=["share/team", "job/품질-테스트"])

    r = run(vault, out)
    assert r["unshared"] == 1, r
    assert sorted(p.split("/")[0] for p in r["exported"]) == ["개발", "품질-테스트"], r
    reasons = {k.split("(")[0]: v for k, v in r["skipped"].items()}
    assert reasons["미확정"] == ["CPT-0003"] and reasons["직무 미지정"] == ["CPT-0006"], r
    assert reasons["민감정보 의심"] == ["CPT-0005"], r
    assert "10.1.2.3" not in json.dumps(r), "보고에 민감값이 새면 안 된다"
    doc = (out / r["exported"][0]).read_text()
    assert "[[" not in doc and "CPT-0002 참고" in doc, doc
    assert (out / "sources.md").read_text().count("| 미처리 |") == 2

    r2 = run(vault, out)  # 같은 내용이면 다시 쓰지 않는다
    assert r2["exported"] == [] and len(r2["unchanged"]) == 2, r2

    p = vault / "40_Knowledge/CPT-0001 공유됨.md"
    p.write_text(p.read_text().replace("본문.", "고친 본문."))
    r3 = run(vault, out)  # 고치면 새 리비전 파일 + 대체 표시
    assert len(r3["exported"]) == 1 and "대체:" in (out / "sources.md").read_text().splitlines()[-1], r3
print("ok")
