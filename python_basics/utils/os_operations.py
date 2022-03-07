import os


def get_base_filename(path):
    return os.path.basename(path)


def get_file_name_without_ext(path):
    return os.path.splitext(get_base_filename(path))[0]


def get_filename_ext(path):
    return os.path.splitext(get_base_filename(path))[1]


path = '../python_basics/utils.py'
print(get_filename_ext(path))
