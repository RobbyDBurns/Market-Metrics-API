# app/etl/extract.py

# Stock ticker is the abbreviation (symbol)

import yfinance as yf
import pandas as pd

def get_historical_data(symbol: str, period: str = "3mo", interval: str = "1d") -> pd.DataFrame:
    # Gets all data related to the associated ticker
    ticker = yf.Ticker(symbol)
    # Fetches historical stock price data and stores it in a pandas.DataFrame
    df = ticker.history(period=period, interval=interval)
    df.reset_index(inplace=True)
    return df
