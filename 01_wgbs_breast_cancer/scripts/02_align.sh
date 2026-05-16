#!/usr/bin/env bash
# 02_align.sh — Bisulfite-aware alignment with bwameth
# Reference genome: hg38 (must be indexed with bwameth index first)

set -euo pipefail

REFERENCE="data/raw/hg38.fa"
INPUT_R1="data/raw/subset_1.fastq"
INPUT_R2="data/raw/subset_2.fastq"
OUTPUT_BAM="data/processed/aligned.sorted.bam"
THREADS=4

echo "Aligning with bwameth..."
bwameth.py \
    --reference "${REFERENCE}" \
    "${INPUT_R1}" "${INPUT_R2}" \
    | samtools sort -@ "${THREADS}" -o "${OUTPUT_BAM}"

samtools index "${OUTPUT_BAM}"

echo "Alignment complete: ${OUTPUT_BAM}"
