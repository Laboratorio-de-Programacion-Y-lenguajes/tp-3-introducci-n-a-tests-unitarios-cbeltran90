"""Tests para la función sqrt(x) -> float."""

import pytest

from src.calculator import sqrt


# --- EJEMPLO (no borrar) ---
def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Raíz de 0 (resultado: 0.0)
#   - Raíz de un número que no es cuadrado perfecto (resultado decimal)
#   - Raíz de un número negativo → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_sqrt_negativo():
#     with pytest.raises(ValueError):
#         sqrt(-4)

def test_sqrt_cero():
    assert sqrt(0) == 0.0


def test_sqrt_no_cuadrado_perfecto():
    assert sqrt(2) == pytest.approx(1.4142135623730951)
    assert sqrt(3) == pytest.approx(1.7320508075688772)
    assert sqrt(5) == pytest.approx(2.23606797749979)


def test_sqrt_negativo():
    with pytest.raises(ValueError):
        sqrt(-4)
    with pytest.raises(ValueError):
        sqrt(-1)
    with pytest.raises(ValueError):
        sqrt(-100)


@pytest.mark.parametrize("x,expected", [
    (4, 2.0),
    (16, 4.0),
    (25, 5.0),
    (1, 1.0),
    (0.25, 0.5),
    (2, 1.4142135623730951),
    (100, 10.0),
])
def test_sqrt_parametrizado(x, expected):
    assert sqrt(x) == pytest.approx(expected)
