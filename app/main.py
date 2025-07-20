#!python3

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Portfolio(BaseModel):
    owner: str
    holdings: List[str]

@app.get("/")
def read_root():
    return {"message": "Welcome to Market Metrics API"}

@app.get("/metrics/{symbol}")
def get_metrics(symbol: str):
    return {
        "symbol": symbol.upper(),
        "message": f"Basic placeholder metrics for {symbol.upper()}"
    }

@app.post("/portfolio")
def summarize_portfolio(portfolio: Portfolio):
    num_holdings = len(portfolio.holdings)
    return {
        "message": f"Portfolio received for {portfolio.owner}",
        "num_stocks": num_holdings,
        "tickers": portfolio.holdings
    }