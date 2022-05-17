import pandas as pd
from sqlalchemy import create_engine


class MySQLDB:
    def __init__(self, conn_url):
        self.engine = create_engine(conn_url)

    @staticmethod
    def read_csv(file):
        print(f"Reading file: {file}")
        return pd.read_csv(file, encoding='unicode_escape', low_memory=False)

    def to_sql(self, df, table_name):
        print(f"Storing table into MySQL database")
        df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
        df.to_sql(table_name, self.engine, if_exists="replace", index=False)

    def read_sql(self, query):
        return pd.read_sql(query, self.engine)
