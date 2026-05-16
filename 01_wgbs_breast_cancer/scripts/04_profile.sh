#!/usr/bin/env bash
# 04_profile.sh — Methylation profiling with deepTools computeMatrix + plotProfile

set -euo pipefail

BIGWIG_DIR="data/processed"
BED_GENES="data/raw/hg38_genes.bed"
OUTPUT_MATRIX="results/methylation_matrix.gz"
OUTPUT_PLOT="figures/05_methylation_profile_all_samples.png"

echo "Computing methylation matrix around TSS..."
computeMatrix reference-point \
    --referencePoint TSS \
    --beforeRegionStartLength 1000 \
    --afterRegionStartLength 1000 \
    --scoreFileName \
        "${BIGWIG_DIR}/NB1_CpG.bw" \
        "${BIGWIG_DIR}/NB2_CpG.bw" \
        "${BIGWIG_DIR}/BT089_CpG.bw" \
        "${BIGWIG_DIR}/BT126_CpG.bw" \
        "${BIGWIG_DIR}/BT198_CpG.meth_ucsc.bw" \
        "${BIGWIG_DIR}/MCF7_CpG.meth_ucsc.bw" \
    --regionsFileName "${BED_GENES}" \
    --outFileName "${OUTPUT_MATRIX}" \
    --skipZeros \
    --numberOfProcessors 4

echo "Plotting methylation profile..."
plotProfile \
    --matrixFile "${OUTPUT_MATRIX}" \
    --outFileName "${OUTPUT_PLOT}" \
    --plotTitle "genes" \
    --samplesLabel NB1_CpG NB2_CpG BT089_CpG BT126_CpG BT198_CpG.meth_ucsc MCF7_CpG.meth_ucsc \
    --colors red yellow green cyan blue darkblue

echo "Profile plot saved to ${OUTPUT_PLOT}"
