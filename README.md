# LLM Wiki — 연구/논문 지식 베이스

Claude가 자동으로 유지·관리하는 개인 연구 위키입니다.

## 구조

```
sources/      # 원본 자료 (논문 PDF, 요약 텍스트 등)
wiki/         # Claude가 생성/관리하는 마크다운 페이지
  papers/     # 논문별 상세 페이지
  topics/     # 주제별 종합 페이지
  authors/    # 저자별 연구 동향
  glossary.md # 핵심 용어 사전
  timeline.md # 연구 흐름 타임라인
  index.md    # 전체 목차
schema/
  CLAUDE.md   # 위키 규칙 정의 (사람이 수정)
```

## 사용 방법

### 논문 추가 (Ingest)
1. `sources/` 폴더에 논문 PDF 또는 요약 텍스트 파일 추가
2. Claude에게 요청:
   ```
   sources/논문파일명을 wiki에 추가해줘
   ```

### 질문 (Query)
```
transformer 기반 논문들의 공통점이 뭐야?
```

### 위키 점검 (Lint)
```
wiki를 점검해줘 — 모순이나 오래된 내용 있으면 알려줘
```
