from pathlib import Path
from gendiff import generate_diff


def get_path(file_name):
    p = Path(__file__)
    current_dir = p.absolute().parent
    return current_dir / 'fixtures' / file_name


def test_gendiff():
    diff = generate_diff(get_path('file1.json'), get_path('file2.json'))
    assert diff == open(get_path('json_result')).read()
