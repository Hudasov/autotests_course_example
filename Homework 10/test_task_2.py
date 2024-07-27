# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.smoke
def test_1():
    assert all_division(1, 3, 5) == 0.06666666666666667

def test_2():
    assert all_division(2, 4, 6) == 0.08333333333333333

def test_3():
    assert all_division(0.1, 0.4, 0.67) == 0.3731343283582089

@pytest.mark.acceptance
def test_4():
    with pytest.raises(ZeroDivisionError):
        all_division(10, 12, 0)

@pytest.mark.smoke
def test_5():
    assert all_division(-7, -8, -9) == -0.09722222222222222



