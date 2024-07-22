def memorize(function):
    # todo Здесь нужно написать код
    pass
    my_dict = {}

    def wrapper(*args, **kwargs):
        # if not my_dict.get(args):
        #     my_dict.setdefault(args, function(*args))
        #     return function(*args), my_dict
        # else:
        #     return list(my_dict.values())[-1], my_dict
        my_dict.setdefault(args, function(*args))
        return function(*args), my_dict

    return wrapper


# todo Здесь ничего изменять не нужно!
@memorize
def get_kinetic_energy(weight, speed):
    """Кинетическая энергия
    :param weight: масса
    :param speed: скорость
    :return: кинетическую энергию
    """
    return (weight * speed ** 2) / 2
