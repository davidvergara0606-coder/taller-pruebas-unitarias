import pytest

from src.ejercicio_05 import es_mayor_de_edad


def test_frontera_inferior_17_anios():
    # Arrange
    edad = 17
    esperado = False

    # Act
    resultado = es_mayor_de_edad(edad)

    # Assert
    assert resultado is esperado


def test_frontera_exacta_18_anios():
    # Arrange
    edad = 18
    esperado = True

    # Act
    resultado = es_mayor_de_edad(edad)

    # Assert
    assert resultado is esperado


def test_frontera_superior_19_anios():
    # Arrange
    edad = 19
    esperado = True

    # Act
    resultado = es_mayor_de_edad(edad)

    # Assert
    assert resultado is esperado


def test_edad_menor_a_cero_lanza_value_error():
    # Arrange
    edad = -1

    # Act / Assert
    with pytest.raises(ValueError):
        es_mayor_de_edad(edad)


def test_edad_mayor_a_125_lanza_value_error():
    # Arrange
    edad = 126

    # Act / Assert
    with pytest.raises(ValueError):
        es_mayor_de_edad(edad)