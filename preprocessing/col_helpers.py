import pandas as pd
import re
import ast

from cols_config import transmission_types, description_regex, MAX_COMPETITORS


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


def format_major_options(chunk):

    formatted_options_list = []

    for option in chunk["major_options"]:
        try:
            options_list = ast.literal_eval(option)
            formatted_option = "#".join(options_list)
        except (ValueError, SyntaxError):
            formatted_option = ""

        formatted_options_list.append(formatted_option)

    chunk["major_options"] = formatted_options_list
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
        ].head(MAX_COMPETITORS)

    competitors_info = competitor_info.sort_values(by='daysonmarket')
    formatted_competitors = []

    for index, row in competitors_info.iterrows():
        formatted_competitors.append(format_competitor(row))

    competitors_str = '$'.join(formatted_competitors)

    return competitors_str


def format_competitor(competitor: pd.Series):

    make = competitor.get('make_name')
    model = competitor.get('model_name')
    price = competitor.get('price')
    seller_rating = competitor.get('seller_rating')
    body_type = competitor.get('body_type')

    return f"{make}#{model}#{body_type}#{price}#{seller_rating}"
