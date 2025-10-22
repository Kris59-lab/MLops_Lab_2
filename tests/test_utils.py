from src.utils import add, subtract, multiply, divide
import pytest


def test_add():
    assert add(1, 2, 3) == 6
    assert add(50, 35, 15) == 100
    assert add(4, 8) == 12


def test_subtract():
    assert subtract(1, 2, 3) == -4
    assert subtract(50, 35, 15) == 0
    assert subtract(7, 2) == 5


def test_multiply():
    assert multiply(-2, -3) == 6
    assert multiply(-5, 5) == -25
    assert multiply(1, 0) == 0


def test_divide():
    assert divide(8, 2) == 4
    assert divide(-100, 5) == -20
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(10, 0)
