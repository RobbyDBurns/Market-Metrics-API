# app/etl/transform.py

# A moving average smooths out price data by taking the average closing price over a rolling window of days.

from pandas import DataFrame
import numpy as np

def add_moving_average(df: DataFrame, window: int=7) -> DataFrame:
    df["MA"] = df["Close"].rolling(window=window).mean() # average of current window
    return df

# Computes and adds rolling volatility to the dataframe
def add_volatility(df: DataFrame, window: int=7, annualized: bool=False) -> DataFrame:
    df["LogReturn"] = np.log(df["Close"] / df["Close"].shift(1))
    # if we don't want it annualized volatility
    if not annualized:
        df["Volatility"] = df["LogReturn"].rolling(window=window).std() # standard deviation of window (volatility)
    else:
        df["Volatility"] = df["LogReturn"].rolling(window=window).std() * np.sqrt(252)
    return df