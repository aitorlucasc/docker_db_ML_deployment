from mongo import MongoDB


def main():
    try:
        # Create the MySQL engine
        mongo_db = MongoDB(conn_url='mongodb://localhost:27017/')

        # Read the csv from the created method
        df = mongo_db.read_csv("online_retail.csv")

        # Save the table to the database
        mongo_db.to_document(df, db="xxxx-mongo", table_name="retail")
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()

