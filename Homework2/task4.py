def test_file_path(file_path):
    """Путь до файла
    :param file_path: абсолютный путь до файла
    :return: название файла без расширения, названия диска и корневую папку
    """
    # todo Здесь нужно написать код
    file_name = file_path.split("\\")[-1]
    file_name = file_name.rsplit(".", 1)[0]
    disk_name = file_path[0]
    root_folder = file_path.split("\\")[1]
    return file_name, disk_name, root_folder