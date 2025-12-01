import pandas as pd
import numpy as np
from typing import Tuple, List, Dict, Any
from collections import defaultdict

BANDS: List[str] = ["Delta", "Theta", "Alpha", "Beta", "Gamma"]
REQUIRED: set = {
    "timestamp", "subject_id", "brain_region",
    "signal_amplitude", "frequency_band", "experimental_condition"
}

def load_and_prepare(csv_path: str) -> Tuple[pd.DataFrame, pd.DataFrame, List[str]]:
    """Carga y prepara datos EEG desde CSV"""
    df = pd.read_csv(csv_path)
    

    if not REQUIRED.issubset(set(df.columns)):
        missing = REQUIRED - set(df.columns)
        raise ValueError(f"CSV misses required columns: {missing}")
    

    df["frequency_band"] = df["frequency_band"].astype(str).str.capitalize()
    

    agg: Dict = defaultdict(lambda: {b: [] for b in BANDS})
    
    for _, row in df.iterrows():
        key = (
            str(row["subject_id"]), 
            str(row["brain_region"]), 
            str(row["experimental_condition"])
        )
        band = str(row["frequency_band"]).capitalize()
        amp = float(row["signal_amplitude"])
        
        if band in BANDS: 
            agg[key][band].append(amp)
    

    rows: List[Dict[str, Any]] = []
    for (subject, region, cond), band_dict in agg.items():
        feat = {
            "subject_id": subject, 
            "brain_region": region, 
            "experimental_condition": cond
        }
        
        for band in BANDS:
            arr = np.array(band_dict[band]) if band_dict[band] else np.array([0.0])
            feat[f"{band}_mean"] = float(np.mean(arr))
            feat[f"{band}_std"] = float(np.std(arr)) if len(arr) > 1 else 0.0
            feat[f"{band}_median"] = float(np.median(arr))
            feat[f"{band}_count"] = int(len(arr))
        
        rows.append(feat)
    
    features_df = pd.DataFrame(rows)
    return df, features_df, BANDS