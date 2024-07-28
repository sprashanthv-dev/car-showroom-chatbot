import sqlite3
import json
import pandas as pd

from questions import all_questions
from db.config import DB_NAME

DB_PATH = f"../db/{DB_NAME}.db"
OUTPUT_DIR_PATH = "./output"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Split the questions into training and testing data set
RATIO = 0.7
index = int(len(all_questions) * RATIO)

training_data = all_questions[:index]
test_data = all_questions[index:]


def execute_sql(sql):
    try:
        df = pd.read_sql_query(sql, conn)
        return df.to_json(orient='records')
    except Exception as e:
        print(f"Error occurred while executing sql: {sql}")
        print(e)


def create_train_test_data(file_name: str, data:  list[tuple[str, str]]):
    with (open(f"{OUTPUT_DIR_PATH}/{file_name}.from", "w") as from_file,
          open(f"{OUTPUT_DIR_PATH}/{file_name}.to", "w") as to_file):
        for idx, (question, query) in enumerate(data, start=1):
            result = execute_sql(query)
            from_file.write(json.dumps({"question": question}) + "\n")
            to_file.write(json.dumps({"answer": result}) + "\n")

            if idx % 10 == 0:
                print(f"Processed {idx} out of {len(data)} records")


def main():
    create_train_test_data("train", training_data)
    create_train_test_data("test", test_data)

    conn.close()


if __name__ == "__main__":
    main()
