import pytest
from src.ejercicio_07 import factorial

def test_factorial_cero():
    # Arrange
    n = 0
    esperado = 1
    # Act
    resultado = factorial(n)
    # Assert
    assert resultado == esperado

def test_factorial_uno():
    assert factorial(1) == 1

def test_factorial_cinco():
    assert factorial(5) == 120

def test_factorial_siete():
    assert factorial(7) == 5040

def test_factorial_negativo_error():
    with pytest.raises(ValueError, match="El factorial no está definido para números negativos"):
        factorial(-3)

def test_factorial_tipo_invalido_error():
    with pytest.raises(TypeError, match="El argumento debe ser un número entero"):
        factorial(3.5)