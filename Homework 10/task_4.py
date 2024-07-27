# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import time
import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

class TestAllDivision:
    @pytest.mark.smoke
    def test_1(self, test_fixture):
        assert all_division(1, 3, 5) == 0.06666666666666667
        time.sleep(2)

    def test_2(self):
        assert all_division(2, 4, 6) == 0.08333333333333333
        time.sleep(2)

    def test_3(self):
        assert all_division(0.1, 0.4, 0.67) == 0.3731343283582089
        time.sleep(2)

    @pytest.mark.acceptance
    def test_4(self):
        with pytest.raises(ZeroDivisionError):
            all_division(10, 12, 0)
        time.sleep(2)

    @pytest.mark.smoke
    def test_5(self, test_fixture):
        assert all_division(-7, -8, -9) == -0.09722222222222222
        time.sleep(2)
