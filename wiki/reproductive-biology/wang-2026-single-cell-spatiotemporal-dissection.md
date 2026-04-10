---
title: "Single-cell spatiotemporal dissection of the human maternal–fetal interface"
authors: Cheng Wang, Yan Zhou, Yuejun Wang, Susan J. Fisher, Jingjing Li et al.
year: 2026
doi: 10.1038/s41586-026-10316-x
source: wang-2026-single-cell-spatiotemporal-dissection.md
category: reproductive-biology
tags: [maternal-fetal-interface, single-cell, spatial-transcriptomics, cytotrophoblast, decidua, placenta, GWAS, atlas]
---

## Summary

인간 모체-태아 경계면(MFI)의 GW5~39 전 임신 기간을 포괄하는 최대 규모 single-nucleus 멀티오믹스 atlas (191,735 핵)와 서브마이크로미터 공간 전사체 (~1.1백만 세포)를 통합하여, cytotrophoblast 분화·arterial remodelling·decidual niche의 공간·분자 기반을 해명했다. EVT vs. SCT 운명 결정의 "toggle switch" 모델, 신규 endothelial state transition(R0→R1→R2), 엔도카나비노이드 시그널링에 의한 침습 억제를 발견하고, GWAS 통합으로 임신 합병증 취약 세포 타입을 특정했다.

## Key Contributions

- **포괄적 MFI atlas**: snRNA-seq + snATAC-seq (191,735 paired 핵), 19 cell type, GW5~39
- **서브마이크로미터 공간 매핑**: STOmics Stereo-seq 16 second-trimester 샘플, ~1.1백만 세포
- **Toggle switch 모델**: EVT(71 TF) vs. SCT(30 TF) 운명을 상호 강화·억제하는 bistable GRN
- **R0→R1→R2 endothelial state transition**: spiral artery remodelling 중 신규 내피세포 상태 발견
- **ML 침습성 예측 모델**: 전사체 signature에서 cytotrophoblast 침습성 예측
- **엔도카나비노이드 억제 기전**: DSC 서브타입이 엔도카나비노이드 시그널링으로 EVT 침습 억제
- **GWAS 통합**: pre-eclampsia, 조산, 유산 취약 세포 특정

## Methods & Architecture

**데이터 레이어:**
1. snRNA-seq + snATAC-seq (10x Genomics) — paired 191,735 핵, 평균 8,336/샘플
2. STOmics Stereo-seq (0.5 µm) — 16 slices, ~1.1M cells, 1 cm × 1 cm 칩
3. CODEX 멀티플렉스 단백질 이미징 (pan-CK, CD31 등)

**분석:**
- Souporcell: maternal/fetal 기원 구분 (>95% 성공률)
- chromVar: ATAC-seq TF motif enrichment
- CellOracle: snATAC + snRNA 통합 GRN 재구성
- Spatial co-occurrence 분석으로 decidual niche 공간 구조 규명
- GWAS fine-mapping 통합

**Toggle switch GRN:**
- FOS → HLA-G, KRT8, FN1 (EVT 활성화)
- EVT TF → CGA, TFPI2, PLAC4 억제 (SCT 프로그램 억압)
- 공유 TF GCM1: EVT/SCT 모두 필요하나 타겟 유전자 셋 상이

## Results

| 항목 | 결과 |
|------|------|
| 총 핵 (multiomics) | 191,735 (paired snRNA + snATAC) |
| 공간 세포 수 | ~1.1백만 (Stereo-seq, 16 슬라이드) |
| Cell types | 19종 (VCT, EVT, SCT, DSC, mVEC, fVEC, dNK 등) |
| EVT 특이적 TF | 71개 (FDR ≤ 0.01) |
| SCT 특이적 TF | 30개 (FDR ≤ 0.01) |
| Endothelial states | R0, R1, R2 (spiral artery remodelling 단계) |
| Maternal/fetal 구분율 | >95% (Souporcell) |

**Spiral artery remodelling:**
- R2 (EVT-침습 완료): 세포 증식 억제 + 세포사 GO term 강화 (FDR 10⁻³~10⁻⁵)

## Limitations

- 정상 임신 샘플 중심 (병리 직접 비교 없음)
- 공간 프로파일링이 second trimester에 집중
- Functional/perturbation validation 미포함
- Endocannabinoid 억제 기전의 in vivo 검증 필요

## Related Papers

- [[single-cell-dl/]] — scRNA-seq 세포 분류 방법론 관련
- [[gwas/]] — 임신 합병증 GWAS 통합 분석
