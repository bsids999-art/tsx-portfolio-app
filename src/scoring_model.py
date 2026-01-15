import pandas as pd
import numpy as np

def normalize(series):
    if series.max() == series.min():
        return pd.Series(0, index=series.index)
    return (series - series.min()) / (series.max() - series.min())

def calculate_scores(df):
    df = df.copy()

    df["pe_ratio"] = df["pe_ratio"].replace(0, np.nan)
    df["price_to_book"] = df["price_to_book"].replace(0, np.nan)

    df["value_score"] = normalize(
        (1 / df["pe_ratio"]) +
        (1 / df["price_to_book"])
    )

    df["growth_score"] = normalize(df["revenue_growth"].fillna(0))
    df["dividend_score"] = normalize(df["dividend_yield"].fillna(0))

    df["total_score"] = (
        0.5 * df["value_score"] +
        0.4 * df["growth_score"] +
        0.1 * df["dividend_score"]
    )

    df["rank"] = df["total_score"].rank(ascending=False)

    return df.sort_values("rank")
