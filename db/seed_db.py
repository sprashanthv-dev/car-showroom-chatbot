import sqlite3

from config import *
from helpers import get_create_table_query_for_car_specs

sql_transaction = []

conn = sqlite3.connect(f"{DB_NAME}.db")
c = conn.cursor()


def create_table():
    try:
        query = get_create_table_query_for_car_specs()
        c.execute(query)
    except Exception as e:
        print(f"Error in creating table car_specs: {e}")


def main():
    create_table()
    print(f"Successfully created table {DB_NAME}.{TABLE_NAME}")

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
