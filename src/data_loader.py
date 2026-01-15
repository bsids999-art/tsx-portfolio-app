import yfinance as yf
import pandas as pd

def load_multiple_stocks(tickers):
    records = []

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)

            info = stock.info
            hist = stock.history(period="1y")

            if hist.empty:
                continue

            records.append({
                "ticker": ticker,
                "price": hist["Close"].iloc[-1],
                "pe_ratio": info.get("trailingPE"),
                "price_to_book": info.get("priceToBook"),
                "revenue_growth": info.get("revenueGrowth"),
                "dividend_yield": info.get("dividendYield"),
                "sector": info.get("sector", "Unknown")
            })

        except Exception:
            continue

    return pd.DataFrame(records)
