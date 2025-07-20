# app/etl/transform.py

# A moving average smooths out price data by taking the average closing price over a rolling window of days.

from pandas import DataFrame

def add_moving_average(df: DataFrame, window: int=7) -> DataFrame:
    df["MA"] = df["Close"].rolling(window=window).mean() # average of current window
    return df

def add_volatility(df: DataFrame, window: int=7) -> DataFrame:
    df["Volatility"] = df["Close"].rolling(window=window).std() # standard deviation of window (volatility)
    return df