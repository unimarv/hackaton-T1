import sqlite3
import pandas as pd

na_values = [' ']
requests = pd.read_csv('ds_dirty_fin_202410041147.csv', na_values=na_values)
def load_csv_to_sqlite(csv_file, db_file, table_name):
    conn = sqlite3.connect(db_file)
    df = pd.read_csv(csv_file, na_values=na_values)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Данные из {csv_file} успешно загружены в таблицу {table_name} базы данных {db_file}.")

if __name__ == "__main__":
    csv_file = 'ds_dirty_fin_202410041147.csv'
    db_file = 'gold.db'
    table_name = 'table_name'
    load_csv_to_sqlite(csv_file, db_file, table_name)

