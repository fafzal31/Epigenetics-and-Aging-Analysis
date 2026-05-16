#!/usr/bin/env bash
# 01_qc.sh — Quality control with Falco
# Run on Galaxy Europe or locally if Falco is installed

set -euo pipefail

INPUT_R1="data/raw/subset_1.fastq"
INPUT_R2="data/raw/subset_2.fastq"
OUTPUT_DIR="results/qc"

mkdir -p "${OUTPUT_DIR}"

echo "Running Falco QC on Read 1..."
falco "${INPUT_R1}" -o "${OUTPUT_DIR}/read1"

echo "Running Falco QC on Read 2..."
falco "${INPUT_R2}" -o "${OUTPUT_DIR}/read2"

echo "QC complete. Results in ${OUTPUT_DIR}/"
