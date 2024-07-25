import sqlite3
import csv

from config import *
from helpers import *

sql_transaction = []

PROCESSED_CSV_PATH = "../data/processed/used_cars_processed.csv"
BUFFER_SIZE = 1000

conn = sqlite3.connect(f"{DB_NAME}.db")
c = conn.cursor()


def drop_table_car_specs():
    try:
        query = drop_table_query_for_car_specs()
        # print(f"Dropping table -- {query}")
        c.execute(query)
    except Exception as e:
        print(f"Error in dropping table car_specs: {e}")


def create_table_car_specs():
    try:
        query = get_create_table_query_for_car_specs()
        # print(f"Creating table -- {query}")
        c.execute(query)
    except Exception as e:
        print(f"Error in creating table car_specs: {e}")


def transaction_bldr(sql):
    global sql_transaction
    sql_transaction.append(sql)

    if len(sql_transaction) > BUFFER_SIZE:
        c.execute('BEGIN TRANSACTION')

        for s in sql_transaction:
            try:
                # print(f"Query before execute: {s}")
                # print("------------------------------")
                c.execute(s)
                break
            except Exception as e:
                print(f"Error in executing transaction: {e}")
                print(f"sql: {s}")

        conn.commit()
        sql_transaction = []


def insert_into_car_specs():

    columns = list(col_types.keys())
    query = get_insert_query_for_car_specs()

    counter = 0
    batch = 0

    with open(PROCESSED_CSV_PATH, "r", buffering=BUFFER_SIZE) as f:
        reader = csv.DictReader(f)

        for row in reader:
            values = []

            for col in columns:
                val = row[col]

                if col == "major_options" or col == "main_picture_url":
                    val = val.replace("'", "''")

                values.append(val)

            query_with_values = build_query_with_values(query, values)
            # print('Built Query:', query_with_values)

            transaction_bldr(query_with_values)

            counter += 1

            if counter % 1000 == 0:
                batch += 1
                print(f"Processed {counter} rows for batch #{batch}")


def main():

    # drop_table_car_specs()
    # print(f"Successfully dropped table {TABLE_NAME}")
    #
    # create_table_car_specs()
    # print(f"Successfully created table {TABLE_NAME}")

    insert_into_car_specs()
    print(f"Successfully inserted all records into table {TABLE_NAME}")

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
