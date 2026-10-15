import pytest
from src.ejercicio_12 import procesar_usuario

def test_procesar_usuario_exitoso():
    # Arrange
    usuario = {"id": 1, "nombre": "Carlos Pérez", "activo": True}
    esperado = {"id": 1, "nombre": "Carlos Pérez", "activo": True, "estado_registro": "VALIDADO"}
    # Act
    resultado = procesar_usuario(usuario)
    # Assert
    assert resultado == esperado

def test_procesar_usuario_clave_faltante():
    usuario = {"id": 1, "nombre": "Carlos Pérez"}
    with pytest.raises(ValueError, match="Faltan campos requeridos"):
        procesar_usuario(usuario)

def test_procesar_usuario_id_invalido():
    usuario = {"id": 0, "nombre": "Carlos", "activo": True}
    with pytest.raises(ValueError, match="El id debe ser un entero positivo"):
        procesar_usuario(usuario)

def test_procesar_usuario_nombre_vacio():
    usuario = {"id": 1, "nombre": "   ", "activo": True}
    with pytest.raises(ValueError, match="El nombre debe ser una cadena no vacía"):
        procesar_usuario(usuario)

def test_procesar_usuario_tipo_no_diccionario():
    with pytest.raises(TypeError, match="El parámetro debe ser un diccionario"):
        procesar_usuario(["id", 1])