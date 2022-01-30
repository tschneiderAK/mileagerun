"""Connects to the MySQL database using the info from db_config"""
from csv import DictReader
import os.path
from mysql.connector import connect


def main():
    connect_to_db

def connect_to_db():
    config_data = read_config()
    return connect(**config_data)


def read_config(file_name):
# This should be refactored using another file reading method. DictReader not ideal as we should not need an iterator.
    db_config_path = os.path.join(os.path.dirname(__file__), f"../config/{file_name}")
    with open(db_config_path, 'r') as f:
        reader = DictReader(f)
        for row in reader:
            return row


if __name__ == '__main__':
    main()