import csv
import json
import os
import sys

from logbook import Logger, StreamHandler

StreamHandler(sys.stdout).push_application()
log = Logger('TyphoonNames')


def typhoon_names_to_json():
    typhoons = []
    current_typhoons = process_current_typhoon_names()
    retired_typhoons = process_retired_typhoon_names()
    typhoons.extend(current_typhoons)
    typhoons.extend(retired_typhoons)

    json_filename_all = os.path.join(os.path.dirname(__file__), "typhoon-names.json")
    json_filename_current = os.path.join(os.path.dirname(__file__), "typhoon-names-current.json")
    json_filename_retired = os.path.join(os.path.dirname(__file__), "typhoon-names-retired.json")

    with open(json_filename_all, 'wb') as f:
        f.write(json.dumps(typhoons).encode('utf-8'))

    with open(json_filename_current, 'wb') as f:
        f.write(json.dumps(current_typhoons).encode('utf-8'))

    with open(json_filename_retired, 'wb') as f:
        f.write(json.dumps(retired_typhoons).encode('utf-8'))

    return True


def process_current_typhoon_names():
    countries = []
    groups = []
    group_names = []
    typhoon_names = []

    with open(os.path.join(os.path.dirname(__file__), "typhoon-names.csv"), "r") as csvfile:
        reader = csv.reader(csvfile)
        countries.extend(next(reader)[1:])

        for row in reader:
            group, *names = row
            groups.append(group)
            group_names.append(names)

            for idx, name in enumerate(names):
                typhoon_names.append(
                    {"name": name, "info": {"country": countries[idx], "group": group, "retired": False}})

    return typhoon_names


def process_retired_typhoon_names():
    header = []
    typhoon_names = []

    with open(os.path.join(os.path.dirname(__file__), "retired-typhoon-names.csv"), "r") as csvfile:
        reader = csv.reader(csvfile)
        header.extend(next(reader))

        for row in reader:
            info = {
                header[i]: v if v else None
                for i, v in enumerate(row)
            }
            info['retired'] = True

            typhoon_names.append({"name": row[0], "info": info})

    return typhoon_names


if __name__ == '__main__':
    typhoon_names_to_json()
