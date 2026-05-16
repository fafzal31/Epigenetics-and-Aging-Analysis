#!/usr/bin/env python3
"""
plot_results.py
Generate all figures for the epigenetic clock benchmarking analysis.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import squareform

CLOCKS = ["Horvathv1", "Hannum", "PhenoAge", "DunedinPACE", "Lin", "Zhang10", "YingCausAge", "YingDamAge"]
FIGURES_DIR = "figures"


def plot_correlation_matrix(results_df: pd.DataFrame, dataset_name: str) -> None:
    cols = ["age"] + [c for c in CLOCKS if c in results_df.columns]
    corr = results_df[cols].corr()
    
    fig, ax = plt.subplots(figsize=(10, 9))
    sns.heatmap(
        corr, annot=True, fmt=".2f", cmap="RdBu_r",
        vmin=-1, vmax=1, ax=ax, square=True,
        cbar_kws={"label": "Correlation Coefficient"},
    )
    ax.set_title(f"Clock Correlation Matrix — {dataset_name}")
    plt.tight_layout()
    outpath = f"{FIGURES_DIR}/correlation_matrix_{dataset_name}.png"
    plt.savefig(outpath, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {outpath}")


def plot_age_deviation_heatmap(results_df: pd.DataFrame, dataset_name: str) -> None:
    clocks_present = [c for c in CLOCKS if c in results_df.columns]
    deviations = results_df[clocks_present].subtract(results_df["age"], axis=0)
    
    fig, ax = plt.subplots(figsize=(12, max(6, len(deviations) * 0.15)))
    sns.heatmap(
        deviations, annot=True, fmt=".1f", cmap="RdBu_r",
        center=0, ax=ax, cbar_kws={"label": "Deviation (Epigenetic Age − Chronological Age)"},
    )
    ax.set_xlabel("Clocks")
    ax.set_ylabel("Samples (IDs)")
    ax.set_title(f"Age Deviation Heatmap — {dataset_name}")
    plt.tight_layout()
    outpath = f"{FIGURES_DIR}/age_deviation_heatmap_{dataset_name}.png"
    plt.savefig(outpath, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {outpath}")


def plot_predicted_vs_chronological(results_df: pd.DataFrame, dataset_name: str) -> None:
    clocks_present = [c for c in CLOCKS if c in results_df.columns]
    fig, ax = plt.subplots(figsize=(10, 8))
    
    colors = plt.cm.tab10.colors
    for i, clock in enumerate(clocks_present):
        ax.scatter(results_df["age"], results_df[clock], label=clock, alpha=0.7, s=40, color=colors[i])
    
    ax.scatter(results_df["age"], results_df["age"], marker="+", color="red", s=60, label="Age", zorder=5)
    ax.set_xlabel("Chronological Age")
    ax.set_ylabel("Predicted Age")
    ax.set_title(f"Predicted vs Chronological Age — {dataset_name}")
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    outpath = f"{FIGURES_DIR}/predicted_vs_chronological_age_{dataset_name}.png"
    plt.savefig(outpath, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {outpath}")


def plot_mae_comparison(results_gse1: pd.DataFrame, results_gse2: pd.DataFrame,
                        name1: str = "GSE120307", name2: str = "GSE41169") -> None:
    clocks = [c for c in CLOCKS if c in results_gse1.columns and c in results_gse2.columns]
    mae1 = [np.mean(np.abs(results_gse1[c] - results_gse1["age"])) for c in clocks]
    mae2 = [np.mean(np.abs(results_gse2[c] - results_gse2["age"])) for c in clocks]
    
    x = np.arange(len(clocks))
    width = 0.35
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(x - width/2, mae1, width, label=name1, color="#6ecfc3")
    ax.bar(x + width/2, mae2, width, label=name2, color="#b0b0b0")
    ax.set_xticks(x)
    ax.set_xticklabels(clocks, rotation=30, ha="right")
    ax.set_xlabel("Clock")
    ax.set_ylabel("MAE (years)")
    ax.set_title("Mean Absolute Error per Clock across both Datasets")
    ax.legend()
    plt.tight_layout()
    outpath = f"{FIGURES_DIR}/mean_absolute_error_comparison.png"
    plt.savefig(outpath, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {outpath}")


if __name__ == "__main__":
    print("Import this module and call the plot functions with your results DataFrames.")
    print("See the notebook for full usage: notebooks/aging_clock_benchmarking.ipynb")
