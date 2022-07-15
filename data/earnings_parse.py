import csv
import os.path

path = os.path.abspath("C:/Code/mileagerun/data/ua_earnings_unprocessed.csv")
headers = []
new_rows = []
with open(path, "r") as f:
    reader =    csv.DictReader(f)
    for row in reader:
        headers = row.keys()
        codes = [x.strip() for x in row['fare_code'].split(",")]
        for code in codes:
            temp = [row[value] for value in row.keys()]
            temp[2] = code + temp[5]
            new_rows.append(temp)

with open(os.path.abspath("C:/Code/mileagerun/data/ua_earnings.csv"), "w", newline='') as f:
    write = csv.writer(f)
    write.writerow(headers)
    write.writerows(new_rows)
