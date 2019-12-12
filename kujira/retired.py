import csv
import os
import random
import sys

from logbook import Logger, StreamHandler

StreamHandler(sys.stdout).push_application()
log = Logger('TyphoonNames')

header = []
rows = []

with open(os.path.join(os.path.dirname(__file__), "retired-typhoon-names.csv"), "r") as csvfile:
    reader = csv.reader(csvfile)
    header.extend(next(reader))

    for row in reader:
        info = {
            header[i]: v if v else None
            for i, v in enumerate(row)
        }
        rows.append(info)

sample = {'Name': 'Karen', 'Replacement name': None, 'Dates active': 'November 7\xa01 17, 1962',
          'Peak classification': 'Category\xa05 super typhoon', 'Sustained wind speeds': '295\xa0km/h (185\xa0mph)',
          'Pressure': '894\xa0hPa (26.40\xa0inHg)', 'Areas affected': 'Guam', 'Damage\xa0(USD)': '$250\xa0million',
          'Deaths': '11', '': 'Pre - 2000S'}

row = random.choice(rows)

info_data = [
    f'Typhoon name is: {row["name"]}.',
    f'{row["name"]} was active at {row["dates_active"]}, peak classification was {row["peak_classification"]} and sustained wind spped was {row["sustained_wind_speeds"]}'
]
if row['replacement_name']:
    info_data.append(f'That name was replaced to {row["replacement_name"]}.')

log.info(' '.join(info_data))
