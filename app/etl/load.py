# app/etl/load.py

# A CSV (Comma Separated Values) file is a simple text file format used to store tabular data, 
# like spreadsheets or databases. Each line in a CSV file represents a row, and the values within 
# each row are separated by commas. This makes it a widely compatible format for exchanging data 
# between different applications. 

from pandas import DataFrame
from os import makedirs

def save_to_csv(df: DataFrame, symbol: str) -> str:
    makedirs("data", exist_ok=True)
    path = f"data/{symbol.upper()}_processed.csv"
    df.to_csv(path, index=False)
    return path