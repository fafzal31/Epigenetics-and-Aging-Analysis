#!/usr/bin/env python3
"""
run_clocks.py
Apply epigenetic aging clocks to methylation data using the Biolearn library.
"""

import pandas as pd
from biolearn.model_gallery import ModelGallery

CLOCKS = [
    "Horvathv1",
    "Hannum",
    "PhenoAge",
    "Lin",
    "Zhang10",
    "DunedinPACE",
    "YingCausAge",
    "YingDamAge",
]

gallery = ModelGallery()


def run_all_clocks(methylation_df: pd.DataFrame, metadata_df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all clocks to a methylation beta-value matrix.

    Parameters
    ----------
    methylation_df : pd.DataFrame
        Rows = CpG sites, columns = sample IDs. Values = beta values (0–1).
    metadata_df : pd.DataFrame
        Index = sample IDs. Must contain 'age' column.

    Returns
    -------
    pd.DataFrame
        Columns: sample_id, chronological_age, and one column per clock.
    """
    results = metadata_df[["age"]].copy()

    for clock_name in CLOCKS:
        print(f"Running {clock_name}...")
        try:
            model = gallery.get(clock_name)
            predictions = model.predict(methylation_df, metadata_df)
            results[clock_name] = predictions
        except Exception as e:
            print(f"  Warning: {clock_name} failed — {e}")
            results[clock_name] = float("nan")

    return results


if __name__ == "__main__":
    print("Import this module and call run_all_clocks() with your data.")
    print("See the notebook for full usage: notebooks/aging_clock_benchmarking.ipynb")
