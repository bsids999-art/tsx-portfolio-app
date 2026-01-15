import pandas as pd
import numpy as np

def normalize(series):
    series = series.fillna(0)
    if series.max() == series.min():
        return pd.Series(0, index=series.index)
    return (series - series.min()) / (series.max() - series.min())

def calculate_scores(df):
    df = df.copy()

    # Ensure required columns exist
    required = [
        "pe_ratio",
        "price_to_book",
        "revenue_growth",
        "dividend_yield"
    ]

    for col in required:
        if col not in df.columns:
            df[col] = np.nan

    df["pe_ratio"] = df["pe_ratio"].replace(0, np.nan)
    df["price_to_book"] = df["price_to_book"].replace(0, np.nan)

    df["value_score"] = normalize(
        (1 / df["pe_ratio"]) +
        (1 / df["price_to_book"])
    )

    df["growth_score"] = normalize(df["revenue_growth"])
    df["dividend_score"] = normalize(df["dividend_yield"])

    df["total_score"] = (
        0.5 * df["value_score"] +
        0.4 * df["growth_score"] +
        0.1 * df["dividend_score"]
    )

    df["rank"] = df["total_score"].rank(ascending=False)

    return df.sort_values("rank")
