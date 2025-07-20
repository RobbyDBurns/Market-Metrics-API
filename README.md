# MarketFlow
A Real-Time Financial ETL (Extract, Transform, Load) Pipeline.<br>
Used to fetch stock/ETF data from the web, computes useful metrics, and exposes clean/documented endpoints.

<h3>🧠 Concept Overview</h3>

* A modular system that:
* Extracts real-world market data (stocks, ETFs, crypto)
* Transforms it (cleansing, aggregating, computing metrics)
* Loads it into a data store (e.g., PostgreSQL or Parquet on S3)
* Serves it via a FastAPI analytics interface
* (Stretch) Streams live updates with Kafka or schedules with Airflow

<h3>🛠️ Tech Stack</h3>

* Python 3.11+<br>
* FastAPI (main web framework)<br>
* pandas, numpy (data wrangling and math)<br>
* yfinance or Alpha Vantage API (data source)<br>
* SQLAlchemy + SQLite or PostgreSQL (for caching/persistence)<br>
* Docker (containerized deployment)<br>
* Pytest (testing)<br>
* Plotly or Matplotlib for visual endpoints<br>

<h3>🛤️ Endpoints</h3>

| Endpoint                                   | Description                                          |
| ------------------------------------------ | ---------------------------------------------------- |
| `GET /health`                              | Health check                                         |
| `GET /metrics/{symbol}`                    | Get key metrics for a given symbol (e.g., AAPL)      |
| `GET /moving-average/{symbol}?window=30`   | Compute and return moving average                    |
| `GET /volatility/{symbol}`                 | Return rolling volatility over time                  |
| `GET /correlation?symbols=AAPL,MSFT,GOOGL` | Compute and return correlation matrix                |
| `GET /sharpe-ratio/{symbol}`               | Sharpe ratio based on last 90 days                   |
| `GET /chart/{symbol}`                      | Return a chart of price + moving averages            |
| `POST /portfolio`                          | Return the Portfolio object in the documented format |

<h3>Important:</h3>

* `http://localhost:8000/docs`
* `source venv/bin/activate`
* `uvicorn app.main:app --reload`
