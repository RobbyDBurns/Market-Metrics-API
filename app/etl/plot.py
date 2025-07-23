# app/etl/plot.py

import matplotlib.pyplot as plt
from pandas import DataFrame

def plot_indicators(df: DataFrame, symbol: str):
    plt.figure(figsize=(12,6))
    plt.plot(df["Date"], df["Close"], label="Close Price")
    plt.plot(df["Date"], df["MA"], label="Moving Average")
    plt.title(f"{symbol} Price vs Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"data/{symbol}_chart.png")
    plt.close()

def plot_rolling_volatility(df: DataFrame, symbol: str, window: int=7, annualized: bool=False):
    file_path = f"data/{symbol.upper()}_volatility_chart.png"

    plt.figure(figsize=(10,5))
    plt.plot(df["Date"], df["Volatility"], label="Rolling Volatility", color="red")
    plt.title(f"{symbol.upper()} Rolling Volatility (Window={window})")
    plt.xlabel("Date")
    if annualized:
        plt.ylabel("Volatility (annualized)")
    else:
        plt.ylabel("Volatility")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(file_path)
    plt.close()
    
    return file_path