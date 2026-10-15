import pytest

from src.ejercicio_06 import validar_longitud_password


def test_longitud_7_borde_invalido_inferior():
    # Arrange
    password = "a" * 7
    esperado = False

    # Act
    resultado = validar_longitud_password(password)

    # Assert
    assert resultado is esperado


def test_longitud_8_borde_valido_inferior():
    # Arrange
    password = "a" * 8
    esperado = True

    # Act
    resultado = validar_longitud_password(password)

    # Assert
    assert resultado is esperado


def test_longitud_20_borde_valido_superior():
    # Arrange
    password = "a" * 20
    esperado = True

    # Act
    resultado = validar_longitud_password(password)

    # Assert
    assert resultado is esperado


def test_longitud_21_borde_invalido_superior():
    # Arrange
    password = "a" * 21
    esperado = False

    # Act
    resultado = validar_longitud_password(password)

    # Assert
    assert resultado is esperado


def test_password_none_lanza_type_error():
    # Arrange
    password = None

    # Act / Assert
    with pytest.raises(TypeError):
        validar_longitud_password(password)


def test_password_numerico_lanza_type_error():
    # Arrange
    password = 12345678

    # Act / Assert
    with pytest.raises(TypeError):
        validar_longitud_password(password)