"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Cualquier número elevado a 0 (resultado: 1)
#   - Número elevado a 1 (resultado: el mismo número)
#   - Base negativa con exponente par (resultado positivo)
#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

def test_pow_exponente_cero():
    assert pow_(5, 0) == 1
    assert pow_(-3, 0) == 1
    assert pow_(0, 0) == 1
    assert pow_(100, 0) == 1


def test_pow_exponente_uno():
    assert pow_(5, 1) == 5
    assert pow_(-3, 1) == -3
    assert pow_(0, 1) == 0


def test_pow_base_negativa_exponente_par():
    assert pow_(-2, 2) == 4
    assert pow_(-3, 4) == 81
    assert pow_(-1, 2) == 1


def test_pow_exponente_decimal():
    assert pow_(9, 0.5) == pytest.approx(3.0)
    assert pow_(4, 0.5) == pytest.approx(2.0)
    assert pow_(27, 1/3) == pytest.approx(3.0)


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 8),
    (2, 0, 1),
    (2, 1, 2),
    (-2, 2, 4),
    (9, 0.5, 3.0),
])

def test_pow_parametrizado(a, b, expected):
    assert pow_(a, b) == pytest.approx(expected)
