def square_calculation(a):
    """Вычисление квадрата
    :param a: сторона квадрата
    :return: периметр квадрата, площадь квадрата и диагональ квадрата
    """
    # todo Здесь нужно написать код
    perimeter = round(a * 4, 2)
    square = round(a ** 2, 2)
    diagonal = round(a * 2 ** 0.5, 2)
    return perimeter, square, diagonal