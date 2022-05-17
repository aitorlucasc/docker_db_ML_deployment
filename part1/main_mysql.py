from mysql import MySQLDB
import json


def main():
    try:
        # Load credentials
        file = open("credentials/mysql.json")
        credentials = json.load(file)
        file.close()

        # Create the MySQL engine
        url = f"mysql+pymysql://{credentials['username']}:{credentials['password']}@localhost:{credentials['port']}/{credentials['database']}"
        mysql_db = MySQLDB(conn_url=url)

        # Read the csv from the created method
        df = mysql_db.read_csv("online_retail.csv")

        # Save the table to the database
        mysql_db.to_sql(df, table_name="retail")

        # Compute the aggregate monthly price
        query = open('query/agg_month_price.sql', 'r')
        agg_month_price_df = mysql_db.read_sql(query.read())
        print(agg_month_price_df)

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
