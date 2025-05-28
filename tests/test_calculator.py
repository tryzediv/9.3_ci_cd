import pytest
from calculator import add, subtract, multiply, divide

# Тесты для функции add
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, -1, -2),
    (0.1, 0.2, pytest.approx(0.3)),
    ("hello", "world", "helloworld")
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# Тесты для функции subtract
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (0, 5, -5),
    (-3, -2, -1),
    (0, 0, 0),
    (0.8, 0.3, pytest.approx(0.5))
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

# Тесты для функции multiply
@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (-2, 5, -10),
    (0, 100, 0),
    (0, 0, 0),
    (0.8, 0.3, pytest.approx(0.24))
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

# Тесты для функции divide
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (-6, 2, -3),
    (5, 2, pytest.approx(2.5)),
    (1, 0.5, 2),
    (-9, -3, 3),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Деление на ноль запрещено"):
        divide(10, 0)
