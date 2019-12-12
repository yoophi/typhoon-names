import csv
import json

import tabulate

out = []
with open('typhoon-names2.csv') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    countries = header[1:]

    for row in reader:
        col, *names = row

        for idx, name in enumerate(names):
            out.append([name, countries[idx], col, idx])

# print(tabulate.tabulate(out, headers=['name', 'country', 'col', 'idx']))

print(json.dumps(out))
