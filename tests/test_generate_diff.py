from pathlib import Path
from gendiff import generate_diff


def get_path(file_name: str) -> str:
    p = Path(__file__)
    current_dir = p.absolute().parent
    return current_dir / 'fixtures' / file_name


def test_gendiff_json():
    diff = generate_diff(get_path('file1.json'), get_path('file2.json'))
    assert diff == open(get_path('plain_result')).read()


def test_gendiff_yaml():
    diff = generate_diff(get_path('file1.yaml'), get_path('file2.yml'))
    assert diff == open(get_path('plain_result')).read()


def test_gendiff_nested_json():
    diff = generate_diff(get_path('nested_file1.json'),
                         get_path('nested_file2.json'))
    assert diff == open(get_path('nested_plain_result')).read()


def test_gendiff_nested_yaml():
    diff = generate_diff(get_path('nested_file1.yaml'),
                         get_path('nested_file2.yml'))
    assert diff == open(get_path('nested_plain_result')).read()
