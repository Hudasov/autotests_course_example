def even_sum(lst):
    """Получение суммы элементов списка с четными индексами
    :param lst: список из чисел
    :return: сумму элементов с четными индексами
    """
    # todo Здесь нужно написать код
    strange_sum = sum(lst[::2])
    return strange_sum

a = [1, 2, 3, 4, 5, 6]
print(a)
del a[:]
print(a)
