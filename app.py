import streamlit as st
from src.data_loader import load_multiple_stocks
from src.scoring_model import calculate_scores

st.set_page_config(page_title="TSX Stock Screener", layout="wide")

st.title("📈 TSX Value & Growth Stock Screener")

tickers = st.text_input(
    "Enter TSX tickers (comma-separated, e.g. SHOP.TO, RY.TO, TD.TO)",
    "SHOP.TO, RY.TO, TD.TO"
)

if st.button("Analyze"):
    ticker_list = [t.strip().upper() for t in tickers.split(",")]

    df_raw = load_multiple_stocks(ticker_list)

    if df_raw.empty:
        st.error("No data returned. Try different TSX tickers.")
    else:
        df_scored = calculate_scores(df_raw)
        st.dataframe(df_scored, use_container_width=True)
