import csv
import os.path
from connect_to_db import connect_to_db

path = os.path.abspath("C:/Code/flight-finder/airline-data/earnings_rates.csv")
headers = []
new_rows = []
with open(path, "r") as f:
    reader =    csv.DictReader(f)
    for row in reader:
        headers = row.keys()
        codes = [x.strip() for x in row['fare_code'].split(",")]
        for code in codes:
            temp = [row[value] for value in row.keys()]
            temp[3] = code
            new_rows.append(temp)

with open(os.path.abspath("C:/Code/flight-finder/airline-data/new_earnings.csv"), "w", newline='') as f:
    write = csv.writer(f)
    write.writerow(headers)
    write.writerows(new_rows)

cnx = connect_to_db('c:/code/flight-finder/config/db_config.csv')
cursor = cnx.cursor()
sql = "INSERT INTO earning_rates VALUES "
print(new_rows)