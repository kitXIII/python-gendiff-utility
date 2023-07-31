from gendiff.format_diff.plain import format_plain
from gendiff.format_diff.stylish import format_stylish


def format_diff(diff, format):
    if (format == 'stylish'):
        return format_stylish(diff)

    if (format == 'plain'):
        return format_plain(diff)

    return None


__all__ = (format_diff)
