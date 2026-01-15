import yfinance as yf
import pandas as pd

def load_multiple_stocks(tickers):
    data = []

    prices = yf.download(
        tickers,
        period="1y",
        group_by="ticker",
        auto_adjust=True,
        threads=True
    )

    for ticker in tickers:
        try:
            if ticker not in prices:
                continue

            close = prices[ticker]["Close"].dropna()
            if close.empty:
                continue

            price = close.iloc[-1]
            returns = close.pct_change().dropna()

            data.append({
                "ticker": ticker,
                "price": price,
                "pe_ratio": None,
                "price_to_book": None,
                "revenue_growth": returns.mean() * 252,
                "dividend_yield": None,
                "sector": "Unknown"
            })
        except Exception:
            continue

    return pd.DataFrame(data)
