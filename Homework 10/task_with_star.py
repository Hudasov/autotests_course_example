# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest

@pytest.mark.id_check(1, 2, 3)
def test(request):
    # Здесь пишем код
    pass
    id_check_marker = request.node.get_closest_marker("id_check")
    if id_check_marker is not None:
        print("id_check:", id_check_marker.args)


