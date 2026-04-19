"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Restar un número mayor al primero (resultado negativo)
#   - Restar cero
#   - Restar dos números negativos
#   - Restar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

def test_sub_resultado_negativo():
    assert sub(2, 5) == -3
    assert sub(0, 10) == -10
    assert sub(10, 20) == -10


def test_sub_restar_cero():
    assert sub(10, 0) == 10
    assert sub(-5, 0) == -5
    assert sub(0, 0) == 0


def test_sub_negativos():
    assert sub(-5, -3) == -2
    assert sub(-3, -5) == 2
    assert sub(-10, -2) == -8


def test_sub_decimales():
    assert sub(5.5, 2.3) == pytest.approx(3.2)
    assert sub(2.5, 3.5) == pytest.approx(-1.0)
    assert sub(0.1, 0.2) == pytest.approx(-0.1)


@pytest.mark.parametrize("a,b,expected", [
    (10, 3, 7),
    (3, 10, -7),
    (0, 5, -5),
    (5, 0, 5),
    (-5, -3, -2),
    (-3, -5, 2),
    (-5, 3, -8),
    (5, -3, 8),
    (2.5, 1.5, 1.0),
    (1.5, 2.5, -1.0),
])
def test_sub_parametrizado(a, b, expected):
    assert sub(a, b) == pytest.approx(expected)