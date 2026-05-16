# Data — WGBS Breast Cancer

Raw data files are **not stored** in this repository due to file size constraints.

## Download Instructions

All raw sequencing data is publicly available via ArrayExpress:

**Accession:** E-MTAB-2014  
**URL:** https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-2014/

### Samples Required

| Sample ID | SRA/ENA Accession | Tissue |
|-----------|-------------------|--------|
| NB1 | See E-MTAB-2014 | Normal breast |
| NB2 | See E-MTAB-2014 | Normal breast |
| BT089 | See E-MTAB-2014 | Invasive ductal carcinoma |
| BT126 | See E-MTAB-2014 | Invasive ductal carcinoma |
| BT198 | See E-MTAB-2014 | Invasive ductal carcinoma |
| MCF7 | See E-MTAB-2014 | Breast cancer cell line |

### Reference Genome

Download hg38 (GRCh38) from UCSC:

```bash
wget https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz
gunzip hg38.fa.gz
# Index for bwameth
bwameth.py index hg38.fa
```

### Galaxy Europe (Recommended)

For Galaxy-based analysis, follow the Galaxy Training Network tutorial which provides pre-loaded data:
https://training.galaxyproject.org/training-material/topics/epigenetics/tutorials/methylation-seq/tutorial.html
