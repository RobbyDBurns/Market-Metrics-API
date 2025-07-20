# app/etl/database.py

from sqlalchemy import create_engine

def get_engine(db_path="sqlite:///data/market_data.db"):
    return create_engine(db_path, echo=False)