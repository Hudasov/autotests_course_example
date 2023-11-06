def string_concatenation(str1, str2):
    """Объединение строк
    :param str1: первая строка
    :param str2: вторая строка
    :return: преобразованную строку
    """

    # todo Здесь нужно написать код
    result_string = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]
    return result_string

