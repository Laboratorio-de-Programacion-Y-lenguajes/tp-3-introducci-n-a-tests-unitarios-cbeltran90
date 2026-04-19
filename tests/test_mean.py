"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Lista con un solo elemento (el resultado debe ser ese mismo elemento)
#   - Lista con números negativos
#   - Lista con números decimales (float)
#   - Lista vacía → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_mean_lista_vacia():
#     with pytest.raises(ValueError):
#         mean([])

def test_mean_un_elemento():
    assert mean([5]) == 5.0
    assert mean([-3]) == -3.0
    assert mean([0]) == 0.0


def test_mean_negativos():
    assert mean([-2, -4, -6]) == -4.0
    assert mean([-10, 0, 10]) == 0.0


def test_mean_decimales():
    assert mean([1.5, 2.5, 3.0]) == pytest.approx(7.0/3)
    assert mean([0.1, 0.2, 0.3]) == pytest.approx(0.2)


def test_mean_lista_vacia():
    with pytest.raises(ValueError):
        mean([])


@pytest.mark.parametrize("values,expected", [
    ([1, 2, 3, 4], 2.5),
    ([10, 20, 30], 20.0),
    ([-5, 5], 0.0),
    ([1, 1, 1, 1], 1.0),
    ([0, 0, 0], 0.0),
])
def test_mean_parametrizado(values, expected):
    assert mean(values) == pytest.approx(expected)