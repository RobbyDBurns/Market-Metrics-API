# app/etl/plot.py

import matplotlib.pyplot as plt

def plot_indicators(df, symbol):
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