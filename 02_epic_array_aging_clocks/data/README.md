# Data — Epigenetic Clock Benchmarking

Raw methylation data is **not stored** in this repository. Download using the provided script:

```bash
python scripts/download_data.py
```

## Datasets

| Dataset | GEO Accession | N | Description |
|---------|---------------|---|-------------|
| GSE120307 | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE120307 | 34 | Whole blood EPIC 850K array |
| GSE41169 | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE41169 | 95 | Whole blood EPIC 850K array |

## Manual Download

If the script fails, download manually from the GEO accession pages above and place the series matrix files in their respective subdirectories here:

```
data/
├── GSE120307/
│   └── GSE120307_series_matrix.txt.gz
└── GSE41169/
    └── GSE41169_series_matrix.txt.gz
```
