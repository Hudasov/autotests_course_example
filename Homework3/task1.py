def modification(lst):
    """Изменение списка
    :param lst: список
    :return: преобразованный список
    """
    # todo Здесь нужно написать код
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst