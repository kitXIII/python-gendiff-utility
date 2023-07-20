import json
from yaml import load as yaml_load, Loader


types = {
    '.json': 'json',
    '.yml': 'yaml',
    '.yaml': 'yaml',
}


def get_file_type(file_name: str):
    result = None
    for key, val in types.items():
        if file_name.endswith(key):
            result = val
            break

    return result


def parse(data, type):
    if types is None:
        return None

    if type == 'json':
        return json.load(data)

    return yaml_load(data, Loader)
