import os


class TYPHOON_TYPE:
    ALL = 'all'
    CURRENT = 'current'
    RETIRED = 'retired'


def get_typhoon_name(type=TYPHOON_TYPE.ALL):
    if type == TYPHOON_TYPE.ALL:
        data_file = os.path.join(os.path.dirname(__file__), 'typhoon-names.json')
