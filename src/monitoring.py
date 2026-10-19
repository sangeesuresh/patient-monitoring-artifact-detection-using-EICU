"""Transparent educational flag summaries for ICU vital-sign data.

This module does not provide diagnosis or clinical decision support.
Thresholds are illustrative only and must be reviewed for the specific study.
"""
from __future__ import annotations
import pandas as pd

DEFAULT_RANGES = {
    "HR": (50, 100),       # low if below 50; high if above 100
    "SpO2": (92, 100),     # low if below 92
    "MAP": (60, 120),      # low below 60 or high above 120
    "Temp": (35, 38),      # low below 35 or high above 38
    "RR": (8, 20),         # low below 8 or high above 20
}

def add_rule_flags(data: pd.DataFrame, ranges=None) -> pd.DataFrame:
    """Return a copy with one boolean `<vital>_flag` column per configured vital."""
    ranges = ranges or DEFAULT_RANGES
    result = data.copy()
    for vital, (low, high) in ranges.items():
        if vital not in result.columns:
            continue
        if vital == "SpO2":
            flags = result[vital] < low
        else:
            flags = (result[vital] < low) | (result[vital] > high)
        result[f"{vital}_flag"] = flags.fillna(False).astype(bool)
    return result

def summarize_flags(data: pd.DataFrame, case_col="caseid", ranges=None) -> pd.DataFrame:
    """Summarize flagged observations and affected cases for each available vital."""
    flagged = add_rule_flags(data, ranges=ranges)
    rows = []
    for vital in (ranges or DEFAULT_RANGES):
        flag_col = f"{vital}_flag"
        if flag_col not in flagged:
            continue
        rows.append({
            "Vital": vital,
            "Observations": len(flagged),
            "Flagged observations": int(flagged[flag_col].sum()),
            "Flagged observation percentage": round(float(flagged[flag_col].mean() * 100), 2),
            "Cases with at least one flag": int(flagged.loc[flagged[flag_col], case_col].nunique())
                if case_col in flagged.columns else None,
        })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    print("Import add_rule_flags and summarize_flags from this module and pass a DataFrame.")
    print("This script does not download or process patient data automatically.")
