import os
import json
import random


class TYPHOON_TYPE:
    ALL = 'all'
    CURRENT = 'current'
    RETIRED = 'retired'


def get_typhoon_name(type=TYPHOON_TYPE.ALL):
    if type == TYPHOON_TYPE.ALL:
        data_file = os.path.join(os.path.dirname(__file__), 'typhoon-names.json')
        with open(data_file, 'r') as f:
            data = json.load(f)

    return random.choice(data)


if __name__ == '__main__':
    print(json.dumps(get_typhoon_name()))