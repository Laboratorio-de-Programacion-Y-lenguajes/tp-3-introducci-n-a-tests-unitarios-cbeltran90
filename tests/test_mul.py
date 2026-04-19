"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

def test_mul_por_cero():
    assert mul(10, 0) == 0
    assert mul(0, 10) == 0
    assert mul(0, 0) == 0


def test_mul_negativos():
    assert mul(-3, -4) == 12
    assert mul(-10, -2) == 20


def test_mul_positivo_y_negativo():
    assert mul(-3, 4) == -12
    assert mul(3, -4) == -12


def test_mul_por_uno():
    assert mul(5, 1) == 5
    assert mul(1, 5) == 5
    assert mul(-7, 1) == -7


def test_mul_decimales():
    assert mul(1.5, 2.5) == pytest.approx(3.75)
    assert mul(0.1, 0.2) == pytest.approx(0.02)


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (2, -3, -6),
    (-2, -3, 6),
    (5, 0, 0),
    (5, 1, 5),
    (1.5, 2, 3.0),
    (0.5, 0.5, 0.25),
])
def test_mul_parametrizado(a, b, expected):
    assert mul(a, b) == pytest.approx(expected)
