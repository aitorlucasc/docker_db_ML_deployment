from sqlite import SQLiteDB


def main():
    try:
        # Create the sqlite engine
        sqlite_db = SQLiteDB(database="lite.db")

        # Read the csv from the created method
        df = sqlite_db.read_csv("online_reatil.csv")

        # Save the table to the database
        sqlite_db.to_sql(df, table_name="retail")

        # df = db.read_sql("select * from retail")

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
