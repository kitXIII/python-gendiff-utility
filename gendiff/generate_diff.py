import json


def generate_diff(path1, path2) -> str:
    data1 = json.load(
        open(path1), parse_constant=lambda x: str(x).lower())
    data2 = json.load(
        open(path2), parse_constant=lambda x: str(x).lower())

    return build_diff(data1, data2)


handlers = [
    {
        'check': lambda key, dict1, _: key not in dict1,
        'handle': lambda key, _, dict2: f'  + {key}: {dict2.get(key)}'
    },
    {
        'check': lambda key, _, dict2: key not in dict2,
        'handle': lambda key, dict1, _: f'  - {key}: {dict1.get(key)}'
    },
    {
        'check': lambda key, dict1, dict2: dict1.get(key) == dict2.get(key),
        'handle': lambda key, dict1, _: f'    {key}: {dict1.get(key)}'
    },
    {
        'check': lambda key, dict1, dict2: dict1.get(key) != dict2.get(key),
        'handle': lambda key, dict1, dict2: '\n'.join([
            f'  - {key}: {dict1.get(key)}',
            f'  + {key}: {dict2.get(key)}',
        ])
    },
]


def build_diff(data1, data2):
    set_of_keys1 = set(data1.keys())
    set_of_keys2 = set(data2.keys())

    keys = sorted(set_of_keys1 | set_of_keys2)

    results = [
        next(handler['handle'](key, data1, data2)
             for handler in handlers
             if handler['check'](key, data1, data2))
        for key in keys
    ]

    return '\n'.join(['{', *results, '}\n'])
