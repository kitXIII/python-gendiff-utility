def render(diff):
    result = flatten([
        renderers[part.get('type')](part)
        for part in diff
    ])

    return '\n'.join(['{', *result, '}']) + '\n'


renderers = {
    'add': lambda part: fmt_diff('+', part.get('key'), part.get('value')),
    'del': lambda part: fmt_diff('-', part.get('key'), part.get('value')),
    'eq': lambda part: fmt_diff(' ', part.get('key'), part.get('value')),
    'upd': lambda part: [
        fmt_diff('-', part.get('key'), part.get('prev_value')),
        fmt_diff('+', part.get('key'), part.get('value'))
    ]
}


def fmt_diff(prefix, key, value):
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
