# Market-Metrics-API

Used to fetch stock/ETF data from the web, computes useful metrics, and exposes clean/documented endpoints.
MarketFlow, A Real-Time Financial ETL Pipeline


Tech Stack:<br>
* Python 3.11+<br>
* FastAPI (main web framework)<br>
* pandas, numpy (data wrangling and math)<br>
* yfinance or Alpha Vantage API (data source)<br>
* SQLAlchemy + SQLite or PostgreSQL (optional for caching/persistence)<br>
* Docker (containerized deployment)<br>
* Pytest (testing)<br>
* Optional: Plotly or Matplotlib for visual endpoints<br>

| Endpoint                                   | Description                                          |
| ------------------------------------------ | ---------------------------------------------------- |
| `GET /health`                              | Health check                                         |
| `GET /metrics/{symbol}`                    | Get key metrics for a given symbol (e.g., AAPL)      |
| `GET /moving-average/{symbol}?window=30`   | Compute and return moving average                    |
| `GET /volatility/{symbol}`                 | Return rolling volatility over time                  |
| `GET /correlation?symbols=AAPL,MSFT,GOOGL` | Compute and return correlation matrix                |
| `GET /sharpe-ratio/{symbol}`               | Sharpe ratio based on last 90 days                   |
| `GET /chart/{symbol}`                      | Return a chart of price + moving averages (optional) |

Important:
* `http://localhost:8000/docs`
