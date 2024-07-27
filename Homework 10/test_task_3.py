# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize("arg1, division", [pytest.param((1,3,5), 0.06666666666666667, marks=pytest.mark.smoke),
                                            pytest.param((2,4,6), 0.08333333333333333, marks=pytest.mark.skip("Ожидаем исправления")),
                                            ((0.1,0.4,0.67), 0.3731343283582089),
                                            ((10,12,0), ZeroDivisionError),
                                            ((-7,-8,-9), -0.09722222222222222)])
def test_all_division(arg1, division):
    if 0 in arg1:
        with pytest.raises(ZeroDivisionError):
            all_division(*arg1)
    else:
        assert all_division(*arg1) == division



