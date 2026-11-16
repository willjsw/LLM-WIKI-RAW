# LLM-WIKI-RAW

개인 PKM 볼트의 **확정된 지식**을 골라 사내 전사 LLM 위키의 `raw/` 기여본으로 만드는 도구와 규칙.

> ⚠️ 이 저장소는 공개다. 도구와 규칙만 올린다. 내보낸 노트 본문은 `raw/` 에 생기지만 git 에서 제외되며,
> 사내 GitLab MR 로만 옮긴다.

| 파일 | 무엇 |
|---|---|
| [GOVERNANCE.md](GOVERNANCE.md) | 직무 기반 디렉터리, 선별 기준 5개, 역할, MR·인제스트 흐름, 기존 위키에 필요한 변경 |
| [jobs.json](jobs.json) | 직무 어휘 + PKM `domain` → 직무 매핑 (정본) |
| [CODEOWNERS.example](CODEOWNERS.example) | 직무 폴더 ↔ 직무 그룹 소유자 초안 |
| [tools/pkm_export.py](tools/pkm_export.py) | 선별·변환·민감정보 검사 후 `raw/<직무>/<ID>-<rev>.md` 생성 |
| [tools/test_pkm_export.py](tools/test_pkm_export.py) | 자기검사 (가짜 볼트) |

## 사용

```bash
# 1) PKM 노트에서 보낼 것에 태그: tags: [share/team]  (직무를 직접 정하려면 job/개발 등 추가)
# 2) 미리보기
python3 -I tools/pkm_export.py ~/Documents/Obsidian-PKM/PKM-Test --contributor <핸들> --dry-run
# 3) 생성 → raw/<직무>/ 와 raw/sources.md 를 사내 GitLab 으로 MR
python3 -I tools/pkm_export.py ~/Documents/Obsidian-PKM/PKM-Test --contributor <핸들>
# 검사
python3 tools/test_pkm_export.py
```

머리말 파서와 민감정보 패턴은 PKM 볼트의 `_System/` 것을 그대로 쓴다 (따로 두지 않는다).
