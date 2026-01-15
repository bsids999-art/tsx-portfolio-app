import yfinance as yf
import pandas as pd

def load_multiple_stocks(tickers):
    rows = []

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            rows.append({
                "ticker": ticker,
                "pe_ratio": info.get("trailingPE"),
                "price_to_book": info.get("priceToBook"),
                "revenue_growth": info.get("revenueGrowth"),
                "dividend_yield": info.get("dividendYield"),
            })
        except Exception:
            continue

    return pd.DataFrame(rows)
