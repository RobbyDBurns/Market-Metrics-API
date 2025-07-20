# app/etl/load.py

from pandas import DataFrame
from os import makedirs
from app.etl.database import get_engine
from pyspark.sql import SparkSession

# A CSV (Comma Separated Values) file is a simple text file format used to store tabular data, 
# like spreadsheets or databases. Each line in a CSV file represents a row, and the values within 
# each row are separated by commas. This makes it a widely compatible format for exchanging data 
# between different applications. 
def save_to_csv(df: DataFrame, symbol: str) -> str:
    makedirs("data", exist_ok=True)
    path = f"data/{symbol.upper()}_processed.csv"
    df.to_csv(path, index=False)
    return path

def save_to_db(df: DataFrame, symbol: str):
    engine = get_engine()
    df.to_sql(symbol, con=engine, if_exists="replace", index=False)

# A parquet is an open-source, columnar (column by column) storage file format specifically designed 
# for efficient data storage and retrieval in big data processing and analytics.  
def save_parquet_with_spark(df: DataFrame, filename: str):
    spark = SparkSession.builder.appName("ETL").getOrCreate()
    spark_df = spark.createDataFrame(df)
    spark_df.write.mode("overwrite").parquet(f"data/{filename}.parquet")