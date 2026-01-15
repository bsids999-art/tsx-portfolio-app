import streamlit as st
import pandas as pd
import yfinance as yf
from src.data_loader import load_multiple_stocks
from src.scoring_model import calculate_scores

st.set_page_config(page_title="TSX Portfolio App", layout="wide")

st.title("🇨🇦 TSX Value & Growth Portfolio Monitor")
st.caption("Long-term value & growth investing (educational)")

# Sidebar
st.sidebar.header("Configuration")
tickers_input = st.sidebar.text_area(
    "TSX tickers (.TO)",
    value="RY.TO,TD.TO,BNS.TO,BMO.TO,ENB.TO,CNR.TO"
)

# Load data
tickers = [t.strip() for t in tickers_input.split(",")]

@st.cache_data(ttl=3600)
def load_data(tickers):
    return load_multiple_stocks(tickers)

df_raw = load_data(tickers)
df_scored = calculate_scores(df_raw)

st.subheader("📊 Stock Rankings")
st.dataframe(
    df_scored.sort_values("rank")[
        ["ticker", "value_score", "growth_score", "total_score", "rank"]
    ]
)
