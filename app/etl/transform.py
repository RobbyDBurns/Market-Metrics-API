# app/etl/transform.py

from pandas import DataFrame

def add_moving_average(df: DataFrame, window: int=7) -> DataFrame:
    df["MA"] = df["Close"].rolling(window=window).mean()
    return df

def add_volatility(df: DataFrame, window: int=7) -> DataFrame:
    df["Volatility"] = df["Close"].rolling(window=window).std()
    return df