import os

import pandas as pd

from cols_config import excluded_cols, numeric_columns
from col_helpers import *

# Ideal case => Chunk size = 1000, max_records = 10000
CHUNK_SIZE = 1000
MAX_RECORDS = 10000

src = "../data/original/used_cars_original.csv"
dest = "../data/processed/used_cars_processed.csv"


def get_competitors(df: pd.DataFrame) -> pd.DataFrame:
    competitor_info = []

    for index, row in df.iterrows():
        # print(f"Processing row - {index}")
        competitors = get_competitor(df, row)
        competitor_info.append(competitors)

    df['competitors'] = competitor_info

    return df


def clean_records(source: str):
    records = pd.DataFrame()

    for chunk in pd.read_csv(source, chunksize=CHUNK_SIZE):

        chunk = chunk.drop(columns=excluded_cols)
        chunk = insert_default_value(chunk)

        if "transmission" in chunk.columns:
            chunk = format_transmission_text(chunk)

        if "description" in chunk.columns:
            chunk = format_description(chunk)

        if "body_type" in chunk.columns:
            chunk = format_body_type(chunk)

        if "major_options" in chunk.columns:
            chunk = format_major_options(chunk)

        for col in numeric_columns:
            if col in chunk.columns:
                chunk[col] = chunk[col].astype(str).apply(get_numeric_value)

        records = pd.concat([records, chunk], ignore_index=True)

        if len(records) >= MAX_RECORDS:
            break

    return records


def main():
    if not os.path.exists(dest):
        records = clean_records(src)
        records = get_competitors(records)

        records.to_csv(dest, index=False)

        print(f"Successfully saved {len(records)} records to {dest}")


if __name__ == "__main__":
    main()
