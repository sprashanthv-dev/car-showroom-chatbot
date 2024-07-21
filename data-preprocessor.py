import os

import pandas as pd

from cols_config import *

# Process 1000 rows at a time
CHUNK_SIZE = 1000
MAX_RECORDS = 50000

src = "data/original/used_cars_original.csv"
dest = "data/processed/used_cars_processed.csv"


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


def clean_records(source: str):
    records = pd.DataFrame()

    for chunk in pd.read_csv(source, chunksize=CHUNK_SIZE):
        chunk = chunk.drop(columns=excluded_cols)

        if "transmission" in chunk.columns:
            chunk = format_transmission_text(chunk)

        if "description" in chunk.columns:
            chunk = format_description(chunk)

        records = pd.concat([records, chunk], ignore_index=True)

        if len(records) >= MAX_RECORDS:
            break

    return records


def main():
    if not os.path.exists(dest):
        records = clean_records(src)
        records.to_csv(dest, index=False)

        print(f"Successfully saved {len(records)} records to {dest}")


if __name__ == "__main__":
    main()
