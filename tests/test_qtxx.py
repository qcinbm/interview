import os
import pandas as pd
import numpy as np
import pandas.testing as pdt

# Candidates are expected to implement this function in src/normalize_origin_rules.py
# Function signature:
#   normalize_origin_rules(input_excel_path: str, output_csv_path: str) -> None
from src.normalize_origin_rules import normalize_origin_rules  # noqa: F401


def _resolve(path_rel: str, fallback_abs: str) -> str:
    """Prefer the relative path in the repo (./data/...).
    If it is missing, fall back to the absolute path provided in the test environment."""
    return path_rel if os.path.exists(path_rel) else fallback_abs


def _clean_df(df: pd.DataFrame) -> pd.DataFrame:
    """Light normalization to compare outputs fairly:
    - Keep only the required five columns
    - Strip leading and trailing whitespace
    - Replace \n and \t with a single space
    - Collapse repeated whitespace
    - Fill NaN with empty strings
    - Ensure 'HS Code 6 digits' is a six-digit numeric string"""
    required_cols = [
        "Chapter",
        "Heading",
        "HS Code 6 digits",
        "Goods Description",
        "Rule of Origin",
    ]
    # Rename columns if they contain extra whitespace
    df = df.copy()
    df.columns = [str(c).strip() for c in df.columns]
    # Keep only the required columns (in case the candidate adds helper columns)
    df = df[required_cols].copy()

    # Normalize strings
    for col in required_cols:
        if col == "HS Code 6 digits":
            # Force to six-digit numeric strings (in case ints/floats were exported)
            df[col] = df[col].astype(str).str.replace(r"\.0+$", "", regex=True)
            df[col] = df[col].str.replace(r"\D", "", regex=True)
        else:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(r"[\n\r\t]+", " ", regex=True)
                .str.strip()
                .str.replace(r"\s{2,}", " ", regex=True)
            )

    # Fill remaining NaN
    df = df.replace({np.nan: ""})

    # Sort for stable comparison
    df = df.sort_values(required_cols).reset_index(drop=True)
    return df


def test_normalize_origin_rules_end_to_end(tmp_path):
    # Resolve input and expected paths
    input_excel = _resolve("data/QTXX.xlsx", "/mnt/data/QTXX.xlsx")
    expected_csv = _resolve("data/qtxx_expected_output.csv", "/mnt/data/qtxx_co_aanz.csv")
    assert os.path.exists(input_excel), f"Input file not found: {input_excel}"
    assert os.path.exists(expected_csv), f"Expected CSV file not found: {expected_csv}"

    # Temporary output path
    out_csv = tmp_path / "qtxx_output.csv"

    # Call candidate function
    normalize_origin_rules(str(input_excel), str(out_csv))

    # Read data
    got = pd.read_csv(out_csv, dtype=str, keep_default_na=False)
    exp = pd.read_csv(expected_csv, dtype=str, keep_default_na=False)

    # Normalize and compare
    got_clean = _clean_df(got)
    exp_clean = _clean_df(exp)

    # Compare data frames after light normalization
    try:
        pdt.assert_frame_equal(got_clean, exp_clean, check_dtype=False, check_like=False)
    except AssertionError as e:
        # Provide hints when failing
        diff_info = []
        if got_clean.shape != exp_clean.shape:
            diff_info.append(f"Different shapes: got={got_clean.shape}, expected={exp_clean.shape}")
        mismatched_cols = [c for c in exp_clean.columns if not got_clean[c].equals(exp_clean[c])]
        if mismatched_cols:
            diff_info.append("Mismatched columns: " + ", ".join(mismatched_cols[:10]))
        raise AssertionError(
            "Output does not match expected after normalization.\n"
            + "\n".join(diff_info)
            + "\n\nPandas details:\n"
            + str(e)
        )
