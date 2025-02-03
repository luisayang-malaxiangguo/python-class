import pytest
from shape_ex.shape import Circle  # shape package inside shape_ex


def test_circle_creation():
    c = Circle((1.0, 0.0), 2)
    assert c.centre == (1.0, 0.0)
    assert c.radius == 2

def test_contains():
    c = Circle((1.0, 0.0), 2)
    assert (0.5, 0.5) in c  # ✅ Inside the circle
    assert (3.5, 0.5) not in c  # ❌ Outside the circle

def test_invalid_circle():
    with pytest.raises(ValueError):
        Circle((1.0,), 2)  # ❌ Centre is not a tuple of length 2

    with pytest.raises(ValueError):
        Circle((1.0, 0.0), -1)  # ❌ Radius is negative

def test_invalid_point():
    c = Circle((1.0, 0.0), 2)
    with pytest.raises(ValueError):
        (0.5,) in c  # ❌ Point is not a tuple of length 2
