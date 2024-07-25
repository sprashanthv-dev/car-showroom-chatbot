from config import col_types, TABLE_NAME


def escape_value(value):
    escaped_value = value.replace("'", "''")
    return f"'{escaped_value}'"


def build_query_with_values(template, values):
    for value in values:
        formatted_value = repr(value)
        template = template.replace('?', formatted_value, 1)

    return template


def get_create_table_query_for_car_specs():
    columns = ", ".join([f"{col} {dtype}" for col, dtype in col_types.items()])
    query = f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} ({columns});"

    return query


def drop_table_query_for_car_specs():
    query = f"DROP TABLE {TABLE_NAME};"
    return query


def get_insert_query_for_car_specs():
    columns = ", ".join(col_types.keys())
    placeholders = ", ".join("?" * len(col_types))
    query = f"INSERT INTO {TABLE_NAME} ({columns}) VALUES ({placeholders});"
    return query
