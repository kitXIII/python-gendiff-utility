from gendiff.format_diff.transform_value import transform_value


def format_stylish(diff, depth=0):
    result = flatten(map(
        lambda node:
            node_formatters.get(node.get('type'))(node, depth, format_stylish),
        diff
    ))

    return '\n'.join(['{', *result, indentation(depth) + '}'])


node_formatters = {
    'added': lambda node, nodeDepth, _:
        fmt_node('+', node.get('key'), node.get('value'), nodeDepth),
    'deleted': lambda node, nodeDepth, _:
        fmt_node('-', node.get('key'), node.get('value'), nodeDepth),
    'unchanged': lambda node, nodeDepth, _:
        fmt_node(' ', node.get('key'), node.get('value'), nodeDepth),
    'updated': lambda node, nodeDepth, _: [
        fmt_node('-', node.get('key'), node.get('prev_value'), nodeDepth),
        fmt_node('+', node.get('key'), node.get('value'), nodeDepth)],
    'nested': lambda node, nodeDepth, fmt_nested:
        fmt_node(
            ' ',
            node.get('key'),
            fmt_nested(node.get('children'), nodeDepth + 1),
            nodeDepth),
}


def fmt_node(prefix, key, value, nodeDepth=0):
    if not isinstance(value, dict):
        return fmt(prefix, key, value, nodeDepth)

    values = [fmt_node(' ', k, v, nodeDepth + 1) for k, v in value.items()]
    nested_value = '\n'.join(['{', *values, indentation(nodeDepth + 1) + '}'])

    return fmt(prefix, key, nested_value, nodeDepth)


def fmt(prefix, key, value, depth=0):
    fmt_value = transform_value(value)

    return f"{indentation(depth)}  {prefix} {key}: {fmt_value}"


def indentation(depth):
    return ' ' * depth * 4


def flatten(coll):
    results = []
    for item in coll:
        if isinstance(item, list):
            results.extend(item)
        else:
            results.append(item)
    return results
