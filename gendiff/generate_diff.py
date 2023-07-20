from gendiff.parser import get_file_type, parse


def generate_diff(path1, path2):
    data1 = parse(open(path1), get_file_type(str(path1)))
    data2 = parse(open(path2), get_file_type(str(path2)))

    return build_diff(data1, data2)


handlers = [
    {
        'check': lambda key, dict1, _: key not in dict1,
        'handle': lambda key, _, dict2: fmt_diff(key, dict2.get(key), '+')
    },
    {
        'check': lambda key, _, dict2: key not in dict2,
        'handle': lambda key, dict1, _: fmt_diff(key, dict1.get(key), '-')
    },
    {
        'check': lambda key, dict1, dict2: dict1.get(key) == dict2.get(key),
        'handle': lambda key, dict1, _: fmt_diff(key, dict1.get(key))
    },
    {
        'check': lambda key, dict1, dict2: dict1.get(key) != dict2.get(key),
        'handle': lambda key, dict1, dict2: ''.join([
            fmt_diff(key, dict1.get(key), '-'),
            fmt_diff(key, dict2.get(key), '+')
        ])
    },
]


def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    results = [
        next(handler['handle'](key, data1, data2)
             for handler in handlers
             if handler['check'](key, data1, data2))
        for key in keys
    ]

    return ''.join(['{\n', *results, '}\n'])


def fmt_diff(key, value, sign=' '):
    formatted_value = value
    if value is True:
        formatted_value = 'true'
    elif value is False:
        formatted_value = 'false'

    return f"  {sign} {key}: {formatted_value}\n"
