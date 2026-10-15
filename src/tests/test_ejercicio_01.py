import pytest

from src.ejercicio_01 import sumar


def test_suma_enteros_positivos():
    # Arrange
    a, b = 2, 3
    esperado = 5

    # Act
    resultado = sumar(a, b)

    # Assert
    assert resultado == esperado


def test_suma_positivo_con_negativo():
    # Arrange
    a, b = 10, -4
    esperado = 6

    # Act
    resultado = sumar(a, b)

    # Assert
    assert resultado == esperado


def test_suma_string_lanza_type_error():
    # Arrange
    a, b = "5", 3

    # Act / Assert
    with pytest.raises(TypeError):
        sumar(a, b)


def test_suma_booleano_lanza_type_error():
    # Arrange
    a, b = True, 3

    # Act / Assert
    with pytest.raises(TypeError):
        sumar(a, b)