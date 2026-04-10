---
title: "Single-cell spatiotemporal dissection of the human maternal–fetal interface"
authors: Cheng Wang, Yan Zhou, Yuejun Wang, Tuhin Kumar Guha, Zhida Luo, Anxhela Mustafaraj, Tara I. McIntyre, Marisa E. Schwab, Brittany R. Davidson, Gabriella C. Reeder, Ronald J. Wong, Sarah K. England, Juan M. Gonzalez, Robert Blelloch, Alexis J. Combes, Linda C. Giudice, Adrian Erlebacher, Tippi C. MacKenzie, David K. Stevenson, Gary M. Shaw, Michael P. Snyder, Xiaofei Sun, Virginia D. Winn, Susan J. Fisher, Jingjing Li
year: 2026
doi: 10.1038/s41586-026-10316-x
category: reproductive-biology
pdf_path: papers/wang-2026-single-cell-spatiotemporal-dissection.pdf
pdf_filename: wang-2026-single-cell-spatiotemporal-dissection.pdf
source_collection: endnote-library
---

## One-line Summary

임신 초기~만기까지 인간 모체-태아 경계면(MFI)의 대규모 single-nucleus 멀티오믹스 + 서브마이크로미터 공간 전사체 atlas로, 세포 분화 프로그램·공간 구조·임신 합병증 취약 세포 상태를 포괄적으로 해명한 Nature 논문.

## 1. Document Info
- Journal/Conference: Nature
- DOI: 10.1038/s41586-026-10316-x
- Received: 25 September 2024
- Accepted: 23 February 2026
- Published: 2026 (online first)

## 2. Key Contributions
- 인간 MFI 전 임신 기간(GW5~39) 커버하는 snRNA-seq + snATAC-seq 191,735 핵 멀티오믹스 atlas 생성
- STOmics Stereo-seq (0.5 µm 해상도) 공간 전사체 16 샘플로 ~1.1백만 세포 공간 매핑, CODEX 멀티플렉스 단백질 이미징과 통합
- Cytotrophoblast 분화의 "toggle switch" 모델 규명: EVT vs. SCT 운명 결정의 전사 인자 네트워크
- Spiral artery remodelling 중 arterial endothelial state transition(R0→R1→R2) 신규 발견
- ML 모델로 전사체 signature에서 cytotrophoblast 침습성 예측
- Decidual stromal cell 서브타입이 엔도카나비노이드 시그널링을 통해 cytotrophoblast 침습 억제
- GWAS 데이터 통합으로 pre-eclampsia·조산·유산에 취약한 세포 타입 특정

## 3. Methods & Architecture

**데이터 생성:**
- snRNA-seq + snATAC-seq (10x Genomics): 191,735 핵 (paired 191,735), 평균 8,336 핵/샘플
- 공간 전사체: STOmics Stereo-seq (0.5 µm 해상도, 1 cm × 1 cm 칩), 16 second-trimester 바살플레이트 절편, ~1.1백만 세포
- CODEX 멀티플렉스 단백질 이미징 (pan-CK, CD31 등)
- 샘플: GW5~GW39, 정상 임신, decidua basalis + basal plate

**분석 파이프라인:**
- Souporcell: maternal/fetal 기원 구분 (>95% 세포)
- chromVar: ATAC-seq transcription factor motif enrichment
- CellOracle: snATAC + snRNA 통합 GRN 재구성
- Spatial co-occurrence analysis: decidual niche 구조 규명
- GWAS 통합: 세포 타입별 임신 합병증 취약성 분석

**세포 유형 (19종):**
VCT, EVT, SCT, DSC, eS, FB, PV, mVEC, fVEC, LEC, eEpi, Cili, dNK, M, HB, DC, B, T, Ery

## 4. Key Results & Benchmarks

**Toggle switch 모델 (EVT vs. SCT 운명):**
- EVT에서 71개, SCT에서 30개 전사 인자 특이적 상향조절 (FDR ≤ 0.01)
- EVT 전사 인자(ASCL2, FOS, KLF6, STAT1)가 EVT 유전자 활성화 + SCT 유전자 억제
- SCT 전사 인자는 역방향: SCT 프로그램 활성화 + EVT 유전자 억제
- 공유 인자(GCM1)도 cell type별 다른 target gene set 관여

**Spiral artery remodelling:**
- R0(정상 arterial EC) → R1(전환기) → R2(EVT 침습 후)의 3단계 endothelial state 전환 신규 발견
- R2: 세포 증식 억제·세포사 촉진 GO term 강화 (FDR < 10⁻³)

**공간 구조:**
- Decidual niche: DSC-면역세포(dNK) 공간적 co-localization 확인
- EVT 침습 패턴: spiral artery 주변 분포 공간 정량화

**임신 합병증:**
- GWAS 통합으로 pre-eclampsia, 조산, 유산 각각에 취약한 특이적 세포 타입 매핑

## 5. Limitations & Future Work
- 정상 임신 중심 (병리 샘플 제한적)
- Second trimester 공간 프로파일링에 집중 (first/third trimester 공간 데이터 부족)
- Perturbation 실험(functional validation) 없이 관찰적 atlas
- Endocannabinoid 신호 억제 기전의 in vivo 검증 필요

## 6. Related Work
- Vento-Tormo et al. (prior placental atlas; label transfer에 사용)
- CellOracle (GRN 재구성 도구)
- STOmics Stereo-seq (공간 전사체 플랫폼)
- chromVar (ATAC-seq TF motif 분석)
- Souporcell (genotype-based cell demultiplexing)

## 7. Glossary
- **MFI (Maternal-Fetal Interface)**: 태반과 자궁내막이 만나는 반-동종이형 조직 경계
- **EVT (Extravillous Trophoblast)**: 침습성 영양막 세포; spiral artery remodelling 수행
- **SCT (Syncytiotrophoblast)**: 다핵 융합 영양막; 영양소 교환·호르몬 분비
- **VCT (Villous Cytotrophoblast)**: EVT/SCT 분화의 전구세포
- **DSC (Decidual Stromal Cell)**: 자궁내막 기질 세포; 태반 착상 지지
- **GRN (Gene Regulatory Network)**: 전사 인자-표적 유전자 조절 네트워크
- **snATAC-seq**: 단일핵 개방 크로마틴 시퀀싱
- **Stereo-seq**: STOmics 개발 서브마이크로미터 공간 전사체 플랫폼
- **CODEX**: 멀티플렉스 단백질 이미징 기술
- **Toggle switch model**: 두 세포 운명 중 하나를 강화하고 다른 하나를 억제하는 bistable 조절 시스템
- **Spiral artery remodelling**: EVT가 자궁 나선동맥을 저저항 혈관으로 개조하는 과정
