import pytest
from src.ejercicio_08 import obtener_mayor

def test_obtener_mayor_positivos():
    # Arrange
    lista = [4, 12, 8, 3]
    esperado = 12
    # Act & Assert
    assert obtener_mayor(lista) == esperado

def test_obtener_mayor_negativos():
    assert obtener_mayor([-15, -3, -8, -20]) == -3

def test_obtener_mayor_un_elemento():
    assert obtener_mayor([42]) == 42

def test_obtener_mayor_lista_vacia_error():
    with pytest.raises(ValueError, match="La lista no puede estar vacía"):
        obtener_mayor([])

def test_obtener_mayor_elementos_invalidos_error():
    with pytest.raises(TypeError, match="Todos los elementos de la lista deben ser números"):
        obtener_mayor([1, 2, "tres"])

def test_obtener_mayor_no_es_lista_error():
    with pytest.raises(TypeError, match="El argumento debe ser una lista"):
        obtener_mayor("no_es_lista")