import pytest
from src.ejercicio_10 import clasificar_nota

def test_clasificar_nota_excelente_max():
    assert clasificar_nota(5.0) == "Excelente"

def test_clasificar_nota_excelente_borde():
    assert clasificar_nota(4.5) == "Excelente"

def test_clasificar_nota_bueno_borde():
    assert clasificar_nota(4.4) == "Bueno"

def test_clasificar_nota_aceptable_borde():
    assert clasificar_nota(3.0) == "Aceptable"

def test_clasificar_nota_deficiente_borde():
    assert clasificar_nota(2.9) == "Deficiente"

def test_clasificar_nota_minimo_absoluto():
    assert clasificar_nota(0.0) == "Deficiente"

def test_clasificar_nota_fuera_de_escala_inferior():
    with pytest.raises(ValueError, match="Nota fuera de la escala"):
        clasificar_nota(-0.1)

def test_clasificar_nota_fuera_de_escala_superior():
    with pytest.raises(ValueError, match="Nota fuera de la escala"):
        clasificar_nota(5.1)

def test_clasificar_nota_tipo_invalido():
    with pytest.raises(TypeError):
        clasificar_nota("4.5")