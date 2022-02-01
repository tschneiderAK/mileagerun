from csv import DictReader
from connect_to_db import connect_to_db
import os.path


def main(filename, table):
    file_path = os.path.join(os.path.dirname(__file__), f"../airline-data/{filename}")
    cnx = connect_to_db()
    cursor = cnx.cursor()
    load_data(file_path, table, cursor)

def load_data(file_path, table, cursor):
    with open(file_path, 'r') as f:
        reader = DictReader(f)
        for row in reader:
            values = ", ".join([row.values()])
            sql = "INSERT INTO {table} ({columns}) VALUES ({values});".format(columns=", ".join(row.keys()), values=values)
            cursor.execute(sql)
            

if __name__ == '__main__':
    main()