import pandas as pd
import sqlite3


class SQLiteDB:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)

    @staticmethod
    def read_csv(file):
        print(f"Reading file: {file}")
        return pd.read_csv(file, encoding='unicode_escape', low_memory=False)

    def to_sql(self, df, table_name):
        print(f"Storing table into SQLite database")
        df.to_sql(table_name, self.conn, if_exists="replace", index=False)

    def read_sql(self, query):
        return pd.read_sql(query, self.conn)
