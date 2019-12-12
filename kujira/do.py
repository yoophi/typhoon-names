import csv
import os
import random
import sys

from logbook import Logger, StreamHandler

StreamHandler(sys.stdout).push_application()
log = Logger('TyphoonNames')

countries = []
groups = []
group_names = []

with open(os.path.join(os.path.dirname(__file__), "typhoon-names.csv"), "r") as csvfile:
    reader = csv.reader(csvfile)
    countries.extend(next(reader)[1:])

    for row in reader:
        group, *names = row
        groups.append(group)
        group_names.append(names)

country = random.choice(countries)
group = random.choice(groups)
name = group_names[groups.index(group)][countries.index(country)]
log.info(f'Typhoon name is: {name}. The name was suggested by {country} / {group}.')

