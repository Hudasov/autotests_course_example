def quadratic(b, c):
    """Решение квадратного уравнения
    :param b: коэффициент b
    :param c: коэффициент c
    :return: корни квадратного уравнения
    """
    # todo Здесь нужно написать код
    a = 1
    discriminant = b ** 2 - 4 * a * c
    x1 = round((-b + discriminant ** 0.5) / (2 * a), 2)
    x2 = round((-b - discriminant ** 0.5) / (2 * a), 2)
    return x1, x2