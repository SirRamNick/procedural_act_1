from procedural_act_1 import calculate_sum, calculate_cubic, calculate_square, calculate_exponential, calculate_product
import pytest

@pytest.mark.parametrize("num1, num2, expected_sum",
    [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0)
    ]
    )
def test_calculate_sum(num1, num2, expected_sum):
    assert calculate_sum(num1, num2) == expected_sum

@pytest.mark.parametrize(
    "num1, num2, expected_product",
    [
    (1, 2, 2),
    (0, 0, 0),
    (-1, 1, -1)
    ]
    )
def test_calculate_product(num1, num2, expected_product):
    assert calculate_product(num1, num2) == expected_product

@pytest.mark.parametrize(
    "num, expected_square",
    [(1, 1),
    (0, 0),
    (-1, 1)
    ]
    )
def test_calculate_square(num, expected_square):
    assert calculate_square(num) == expected_square

@pytest.mark.parametrize(
    "num, expected_cubic",
    [
    (1, 1),
    (0, 0),
    (-1, -1)
    ]
    )
def test_calculate_cubic(num, expected_cubic):
    assert calculate_cubic(num) == expected_cubic

@pytest.mark.parametrize("num, expected_exponential",
    [
    (1, 2.718),
    (0, 1),
    (-1, 0.367)
    ]
    )
def test_calculate_exponential(num, expected_exponential):
    assert abs(calculate_exponential(num) - expected_exponential) < 0.001

