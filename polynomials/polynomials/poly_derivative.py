from polynomials.polynomials_package import Polynomial

def derivative(poly):
    """Compute the derivative of a Polynomial."""
    if not isinstance(poly, Polynomial):
        raise TypeError("Expected a Polynomial instance")
    return poly.dx()
