from src.utils import add, subtract


def test_add():
    assert add(1, 2, 3) == 6
    assert add(50, 35, 15) == 100
    assert add(4, 8) == 12


def test_subtract():
    assert subtract(1, 2, 3) == -4
    assert subtract(50, 35, 15) == 0
    assert subtract(7, 2) == 5
