import os


def get_file_suffix(filename, has_dot=False):
    """
    获取文件后缀名
    :has_dot: 后缀名是否需要带点
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


def rename_all_files(path, patten, number):
    """
    can only exist files in path, can not exist dir.
    :param path: path
    :param patten: patten
    :param number: start number
    """
    files = os.listdir(path)
    print('These files will be renamed.')
    print(files)
    for file in files:
        suffix = get_file_suffix(file, True)
        os.rename(f'{path}/{file}', f'{path}/{patten}{number}{suffix}')
        number += 1
    print('done')


def example_rename_all_files():
    rename_all_files('C:/Users/13748/Downloads/tmp', 'mea-', 20)


if __name__ == '__main__':
    example_rename_all_files()
