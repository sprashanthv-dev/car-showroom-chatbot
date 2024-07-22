from config import col_types, TABLE_NAME


def get_create_table_query_for_car_specs():
    columns = ", ".join([f"{col} {dtype}" for col, dtype in col_types.items()])
    query = f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} ({columns});"

    return query
