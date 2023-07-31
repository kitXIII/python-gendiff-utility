from gendiff.format_diff.stylish import format_stylish


def format_diff(diff, format):
    if (format == 'stylish'):
        return format_stylish(diff)
    return None


__all__ = (format_diff)
