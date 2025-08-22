import pytest
from app.services.math_service import calculate_expression

def test_calculate_expression_basic():
    for expr, expected in [("2+2", 4), ("10-3", 7), ("3*5", 15), ("8/2", 4)]:
        result = calculate_expression(expr)
        assert pytest.approx(float(result)) == float(expected)

def test_calculate_expression_with_functions():
    for expr, expected in [("sqrt(16)", 4), ("pow(2, 3)", 8)]:
        result = calculate_expression(expr)
        assert pytest.approx(float(result)) == float(expected)

def test_calculate_expression_invalid():
    result = calculate_expression("texto_invalido")
    assert isinstance(result, str)
    assert "erro" in result.lower()
