#!/usr/bin/env bash
# 05_dmr_detection.sh — DMR detection with Metilene

set -euo pipefail

# Input: merged CpG methylation file (all samples, tab-separated)
# Format: chr start end NB1 NB2 BT198
INPUT_MERGED="data/processed/merged_cpg_methylation.txt"
OUTPUT_DMR="results/dmrs_normal_vs_cancer.txt"

echo "Running Metilene DMR detection..."
metilene \
    -a g1 -b g2 \
    -m 5 \
    -d 0.1 \
    "${INPUT_MERGED}" \
    > "${OUTPUT_DMR}"

echo "DMR detection complete."
echo "Results saved to ${OUTPUT_DMR}"
echo "Number of DMRs detected: $(wc -l < ${OUTPUT_DMR})"

# Sort by q-value
sort -k7,7g "${OUTPUT_DMR}" > "results/dmrs_sorted_by_qvalue.txt"
echo "Sorted DMRs saved to results/dmrs_sorted_by_qvalue.txt"
