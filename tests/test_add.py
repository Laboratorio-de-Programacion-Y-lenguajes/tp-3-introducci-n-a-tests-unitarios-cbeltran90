"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Sumar dos números negativos
#   - Sumar un número positivo y uno negativo
#   - Sumar con cero
#   - Sumar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
#
# Ejemplo de test parametrizado:
#
# @pytest.mark.parametrize("a,b,expected", [
#     (..., ..., ...),
#     (..., ..., ...),
# ])
# def test_add_parametrizado(a, b, expected):
#     assert add(a, b) == expected

def test_add_negativos():
    """Sumar dos números negativos."""
    assert add(-1, -2) == -3
    assert add(-10, -5) == -15


def test_add_positivo_y_negativo():
    """Sumar un número positivo y uno negativo."""
    assert add(5, -3) == 2
    assert add(-7, 4) == -3


def test_add_con_cero():
    """Sumar con cero."""
    assert add(10, 0) == 10
    assert add(0, 10) == 10
    assert add(0, 0) == 0


@pytest.mark.parametrize("a,b,expected", [
    (1.5, 2.5, 4.0),
    (0.1, 0.2, 0.3),
    (1.99, 0.01, 2.0),
    (-1.5, -2.5, -4.0),
    (1.5, -0.5, 1.0),
])
def test_add_decimales(a, b, expected):
    """Sumar números decimales (parametrizado)."""
    assert add(a, b) == pytest.approx(expected)

