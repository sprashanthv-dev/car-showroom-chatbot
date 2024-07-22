import pandas as pd
import re

from cols_config import transmission_types, description_regex


def format_transmission_text(chunk):
    chunk["transmission"] = (chunk["transmission"]
                             .map(transmission_types)
                             .fillna(chunk["transmission"].values[0]).astype(str))

    return chunk


def format_description(chunk):
    chunk["description"] = (chunk["description"]).str.replace(
        description_regex, '', regex=False
    )

    return chunk


def format_body_type(chunk):
    chunk["body_type"] = ((chunk["body_type"]).str.strip()
                          .str.replace('/', '-', regex=False))

    return chunk


def get_numeric_value(value):
    str_value = str(value)
    match = re.search(r'[\d.]+', str_value)
    return float(match.group()) if match else 0.0


def insert_default_value(chunk):
    for col in chunk.columns:
        if chunk[col].dtype == 'float64':
            chunk[col] = chunk[col].fillna(0.0)
        elif chunk[col].dtype == 'int64':
            chunk[col] = chunk[col].fillna(0)
        elif chunk[col].dtype == 'object':
            chunk[col] = chunk[col].fillna("NA")

    return chunk


def get_competitor(df: pd.DataFrame, row: pd.Series):
    competitor_info = df[
        (df['body_type'] == row['body_type']) &
        (row['price'] * 1.2 >= df['price']) &
        (df['price'] >= row['price'] * 0.8) &
        (df['seller_rating'] >= row['seller_rating']) &
        (df['make_name'] != row['make_name'])
        ]

    competitors_info = competitor_info.sort_values(by='daysonmarket')

    return competitors_info
