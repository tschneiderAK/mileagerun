from csv import DictReader
import mysql.connector
import os.path


def load_earnings(cursor):
    earnings_rates = os.path.join(os.path.dirname(__file__), "../airline-data/earnings_rates.csv")
    with open(earnings_rates, 'r') as f:
        reader = DictReader(f)
        for row in reader:
            values = ", ".join([row.values()])
            sql = "INSERT INTO earning_by_miiles ({columns}) VALUES ({values});".format(columns=", ".join(row.keys()), values=values)
            cursor.execute(sql)

load_earnings()