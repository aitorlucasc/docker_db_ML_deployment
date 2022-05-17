import pandas as pd
import pymongo


class MongoDB:
    def __init__(self, conn_url):
        self.client = pymongo.MongoClient(conn_url)

    @staticmethod
    def read_csv(file):
        print(f"Reading file: {file}")
        return pd.read_csv(file, encoding='unicode_escape', low_memory=False)

    def to_document(self, df, db, table_name):
        df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
        print(f"Storing MongoDB colletion")
        db = self.client[db]
        collection = db[table_name]
        collection.insert_many(df.to_dict('records'))
