def format_stylish(diff):
    result = flatten(map(
        lambda part: parts_formatters[part.get('type')](part), diff))

    return '\n'.join(['{', *result, '}']) + '\n'


parts_formatters = {
    'add': lambda part: fmt_part('+', part.get('key'), part.get('value')),
    'del': lambda part: fmt_part('-', part.get('key'), part.get('value')),
    'eq': lambda part: fmt_part(' ', part.get('key'), part.get('value')),
    'upd': lambda part: [
        fmt_part('-', part.get('key'), part.get('prev_value')),
        fmt_part('+', part.get('key'), part.get('value'))
    ]
}


def fmt_part(prefix, key, value):
    formatted_value = value
    if value is True:
        formatted_value = 'true'
    elif value is False:
        formatted_value = 'false'

    return f"  {prefix} {key}: {formatted_value}"


def flatten(coll):
    results = []
    for item in coll:
        if type(item) == list:
            results.extend(item)
        else:
            results.append(item)
    return results
