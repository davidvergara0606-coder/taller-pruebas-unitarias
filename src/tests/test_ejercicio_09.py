import pytest
from src.ejercicio_09 import es_palindromo

def test_es_palindromo_simple():
    assert es_palindromo("radar") is True

def test_es_palindromo_con_espacios_y_mayusculas():
    assert es_palindromo("Anita lava la tina") is True

def test_es_palindromo_falso():
    assert es_palindromo("software") is False

def test_es_palindromo_vacio_o_espacios():
    assert es_palindromo("") is False
    assert es_palindromo("   ") is False

def test_es_palindromo_tipo_invalido_error():
    with pytest.raises(TypeError, match="El parámetro debe ser una cadena de texto"):
        es_palindromo(1001)