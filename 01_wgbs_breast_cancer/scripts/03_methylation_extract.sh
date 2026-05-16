#!/usr/bin/env bash
# 03_methylation_extract.sh — Methylation extraction and bias assessment with MethylDackel

set -euo pipefail

REFERENCE="data/raw/hg38.fa"
BAM="data/processed/aligned.sorted.bam"
OUTPUT_PREFIX="data/processed/methylation"

echo "Assessing methylation bias..."
MethylDackel mbias \
    "${REFERENCE}" \
    "${BAM}" \
    "${OUTPUT_PREFIX}_mbias"

echo "Extracting CpG methylation (with recommended position trimming)..."
# Adjust --OT and --OB bounds based on mbias output
MethylDackel extract \
    --OT 0,145,6,149 \
    --mergeContext \
    "${REFERENCE}" \
    "${BAM}" \
    -o "${OUTPUT_PREFIX}"

echo "Methylation extraction complete. Output: ${OUTPUT_PREFIX}_CpG.bedGraph"
