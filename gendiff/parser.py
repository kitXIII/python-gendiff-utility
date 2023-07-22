import json
from yaml import load as yaml_load, Loader


def parse(data, type):
    if type == 'json':
        return json.load(data)

    if type == 'yaml':
        return yaml_load(data, Loader)

    return None
