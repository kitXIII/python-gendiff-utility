def format_stylish(diff, depth=0):
    result = flatten(map(
        lambda node:
            node_formatters.get(node.get('type'))(node, depth, format_stylish),
        diff
    ))

    final_symbol = '\n' if depth == 0 else ''

    return '\n'.join(['{', *result, indentation(depth) + '}']) + final_symbol


node_formatters = {
    'add': lambda node, nodeDepth, _:
        fmt_node('+', node.get('key'), node.get('value'), nodeDepth),
    'del': lambda node, nodeDepth, _:
        fmt_node('-', node.get('key'), node.get('value'), nodeDepth),
    'eq': lambda node, nodeDepth, _:
        fmt_node(' ', node.get('key'), node.get('value'), nodeDepth),
    'upd': lambda node, nodeDepth, _: [
            fmt_node('-', node.get('key'), node.get('prev_value'), nodeDepth),
            fmt_node('+', node.get('key'), node.get('value'), nodeDepth)
        ],
    'nested': lambda node, nodeDepth, fmt_nested:
        fmt_node(
            ' ',
            node.get('key'),
            fmt_nested(node.get('children'), nodeDepth + 1),
            nodeDepth),
}


def fmt_node(prefix, key, value, nodeDepth=0):
    if type(value) != dict:
        return indentation(nodeDepth) + fmt(prefix, key, value)

    values = [fmt_node(' ', k, v, nodeDepth + 1) for k, v in value.items()]
    nested_value = '\n'.join(['{', *values, indentation(nodeDepth + 1) + '}'])

    return indentation(nodeDepth) + fmt(prefix, key, nested_value)


def fmt(prefix, key, value):
    formatted_value = value
    if value is True:
        formatted_value = 'true'
    elif value is False:
        formatted_value = 'false'
    elif value is None:
        formatted_value = 'null'

    if formatted_value == '':
        return f"  {prefix} {key}:"

    return f"  {prefix} {key}: {formatted_value}"


def indentation(depth):
    return ' ' * depth * 4


def flatten(coll):
    results = []
    for item in coll:
        if type(item) == list:
            results.extend(item)
        else:
            results.append(item)
    return results
