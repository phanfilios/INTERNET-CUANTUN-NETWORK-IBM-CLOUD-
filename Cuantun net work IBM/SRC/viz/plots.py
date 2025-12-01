import os
from typing import Optional
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def basic_boxplot(features_df: pd.DataFrame, outdir: str) -> None:
    """Genera boxplot básico de características por región cerebral"""
    try:
        os.makedirs(outdir, exist_ok=True)
        

        mean_columns = [c for c in features_df.columns if c.endswith("_mean")]
        if not mean_columns:
            print("No mean columns found for boxplot")
            return
        
        melt_mean = features_df.melt(
            id_vars=["subject_id", "brain_region", "experimental_condition"],
            value_vars=mean_columns,
            var_name="band", 
            value_name="mean_amplitude"
        )
        melt_mean["band"] = melt_mean["band"].str.replace("_mean", "", regex=False)
        

        plt.figure(figsize=(12, 6))
        sns.boxplot(data=melt_mean, x="brain_region", y="mean_amplitude", hue="band")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        

        output_path = os.path.join(outdir, "band_mean_by_region.png")
        plt.savefig(output_path, dpi=200)
        plt.close()
        print(f"Saved: {output_path}")
        
    except Exception as e:
        print(f"Error generating boxplot: {e}")