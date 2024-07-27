import time
import pytest

@pytest.fixture(scope="class", autouse=True)
def class_fixture(request):
    print(f"Тестовый класс начинается: {time.strftime('%H:%M:%S')}")
    yield
    print(f"Тестовый класс заканчивается: {time.strftime('%H:%M:%S')}")

@pytest.fixture
def test_fixture():
    print(f"Тест начинается: {time.strftime('%H:%M:%S')}")
    yield
    print(f"Тест заканчивается: {time.strftime('%H:%M:%S')}")


