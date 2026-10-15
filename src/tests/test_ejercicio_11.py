import pytest
from src.ejercicio_11 import division_segura

def test_division_exacta():
    assert division_segura(10, 2) == 5.0

def test_division_periodica_aproximada():
    # Uso de pytest.approx para precisión decimal flotante
    assert division_segura(10, 3) == pytest.approx(3.333, rel=1e-3)

def test_division_cero_dividendo():
    assert division_segura(0, 5) == 0.0

def test_division_por_cero_error():
    with pytest.raises(ZeroDivisionError, match="No es posible dividir entre cero"):
        division_segura(8, 0)

def test_division_tipo_invalido_error():
    with pytest.raises(TypeError, match="Los operandos deben ser numéricos"):
        division_segura("10", 2)