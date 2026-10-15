import pytest

from src.ejercicio_02 import es_par


def test_numero_par_positivo():
    # Arrange
    numero = 8
    esperado = True

    # Act
    resultado = es_par(numero)

    # Assert
    assert resultado is esperado


def test_numero_impar_positivo():
    # Arrange
    numero = 7
    esperado = False

    # Act
    resultado = es_par(numero)

    # Assert
    assert resultado is esperado


def test_cero_es_par():
    # Arrange
    numero = 0
    esperado = True

    # Act
    resultado = es_par(numero)

    # Assert
    assert resultado is esperado


def test_negativo_par():
    # Arrange
    numero = -4
    esperado = True

    # Act
    resultado = es_par(numero)

    # Assert
    assert resultado is esperado


def test_negativo_impar():
    # Arrange
    numero = -9
    esperado = False

    # Act
    resultado = es_par(numero)

    # Assert
    assert resultado is esperado


def test_decimal_lanza_type_error():
    # Arrange
    numero = 4.0

    # Act / Assert
    with pytest.raises(TypeError):
        es_par(numero)