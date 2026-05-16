#!/usr/bin/env python3
"""
download_data.py
Download GSE120307 and GSE41169 methylation data from NCBI GEO using GEOparse.
"""

import os
import GEOparse

DATASETS = {
    "GSE120307": "02_epic_array_aging_clocks/data/GSE120307",
    "GSE41169": "02_epic_array_aging_clocks/data/GSE41169",
}


def download_geo_dataset(accession: str, output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)
    print(f"Downloading {accession}...")
    gse = GEOparse.get_GEO(geo=accession, destdir=output_dir, silent=False)
    print(f"  Samples: {len(gse.gsms)}")
    print(f"  Saved to: {output_dir}")
    return gse


if __name__ == "__main__":
    for accession, output_dir in DATASETS.items():
        try:
            download_geo_dataset(accession, output_dir)
        except Exception as e:
            print(f"Error downloading {accession}: {e}")
    print("\nAll downloads complete.")
