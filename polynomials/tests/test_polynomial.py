import pytest
from numbers import Number

from polynomials.polynomials_package import Polynomial
from polynomials.poly_derivative import derivative

def test_print():

    p = Polynomial((2,1,0,3))
    
    assert str(p) == "3x^3 + 1x + 2"

def test_equality():
    assert Polynomial((0, 1)) == Polynomial((0, 1))

@pytest.mark.parametrize(
    "a, b, sum",
    (
        ((0,), (0, 1), (0, 1)),
        ((2, 0, 3), (1, 2), (3, 2, 3)),
        ((4, 2), (10, 2, 4), (14, 4, 4))
    )
)
def test_add(a, b, sum):
    assert Polynomial(a) + Polynomial(b) == Polynomial(sum)

def test_add_scalar():
    assert Polynomial((2, 1)) + 3 == Polynomial((5, 1))

def test_reverse_add_scalar():
    assert 3 + Polynomial((2, 1)) == Polynomial((5, 1))

def test_add_unknown():
    with pytest.raises(TypeError):
        Polynomial(( 1,)) + "frog"

def test_subtraction():
    assert Polynomial((3, 2)) - Polynomial((1, 1)) == Polynomial((2, 1))
    assert Polynomial((3, 2)) - 2 == Polynomial((1, 2))
    assert 5 - Polynomial((3, 2)) == Polynomial((2, -2))

def test_multiplication():
    assert Polynomial((2, 1)) * 3 == Polynomial((6, 3))
    assert 3 * Polynomial((2, 1)) == Polynomial((6, 3))
    assert Polynomial((1, 1)) * Polynomial((1, -1)) == Polynomial((1, 0, -1))

def test_exponentiation():
    assert Polynomial((1, 1)) ** 2 == Polynomial((1, 2, 1))
    assert Polynomial((2,)) ** 3 == Polynomial((8,))

def test_evaluation():
    assert Polynomial((1, 2, 3))(2) == 17  # Evaluating 1 + 2x + 3x^2 at x=2


def test_derivative():
    assert Polynomial((3, 2, 1)).dx() == Polynomial((2, 2))  # (3 + 2x + x^2) -> (2 + 2x)
    assert Polynomial((4,)).dx() == Polynomial((0,))  # Constant derivative is 0
    assert Polynomial((0, 1, 3)).dx() == Polynomial((1, 6))  # (x + 3x^2) -> (1 + 6x)
    assert derivative(Polynomial((5, 0, 2))) == Polynomial((0, 4))  # (5 + 2x^2) -> (4x)