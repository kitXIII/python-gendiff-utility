import os
from gendiff.parser import parse
from gendiff.build_diff import build_diff
from gendiff.render import render


def generate_diff(path1, path2):
    data1 = parse(open(path1), get_file_type(str(path1)))
    data2 = parse(open(path2), get_file_type(str(path2)))

    diff = build_diff(data1, data2)
    return render(diff)


types = {
    '.json': 'json',
    '.yml': 'yaml',
    '.yaml': 'yaml',
}


def get_file_type(file_name):
    _, ext = os.path.splitext(file_name)
    return types.get(ext, None)
