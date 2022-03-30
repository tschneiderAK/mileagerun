"""Connects to the MySQL database using the info from db_config"""
from csv import DictReader
from sys import argv
from mysql.connector import connect
import os.path


def main(config_file):
    connect_to_db(config_file)

def connect_to_db(config_file):
    config_data = read_config(config_file)
    return connect(**config_data)


def read_config(config_file):
# This should be refactored using another file reading method. DictReader not ideal as we should not need an iterator.
    db_config_path = f'flight-finder/config/{config_file}'
    module_path = os.path.dirname(__file__)
    path = os.path.relpath(db_config_path, module_path)
    with open(path, 'r') as f:
        reader = DictReader(f)
        for row in reader:
            return row


if __name__ == '__main__':
    main(argv[1])