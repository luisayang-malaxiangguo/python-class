from numbers import Number
from numbers import Integral  # Import for checking integer type

class Polynomial:

  def __init__(self, coefs):
      self.coefficients = coefs

  def degree(self):
      return len(self.coefficients) - 1
  
  def __str__(self):

    coefs = self.coefficients
    terms = []

    # Degree 0 and 1 terms conventionally have different representation.
    if coefs[0]:
        terms.append(str(coefs[0]))
    if self.degree() > 0 and coefs[1]:
        terms.append(f"{coefs[1]}x")

    # Remaining terms look like cx^d, though factors of 1 are dropped.
    terms += [f"{'' if c == 1 else c}x^{d}"
              for d, c in enumerate(coefs[2:], start=2) if c]

    # Sum polynomial terms from high to low exponent.
    return " + ".join(reversed(terms)) or "0"
  
  def __eq__(self,other):
     return self.coefficients== other.coefficients

#def __repr__(self):
    #return type(self).__name__ + "(" + repr(self.coefficients) + ")"

 #def __repr__(self):
    #return f"{type(self).__name__}({self.coefficients!r})"
  
  def __add__(self, other):
    if isinstance(other, Number):
        return Polynomial((self.coefficients[0] + other,)
                          + self.coefficients[1:])

    elif isinstance(other, Polynomial):
        # Work out how many coefficient places the two polynomials have in
        # common.
        common = min(self.degree(), other.degree()) + 1
        # Sum the common coefficient positions.
        coefs = tuple(a + b for a, b in zip(self.coefficients[:common],
                                            other.coefficients[:common]))

        # Append the high degree coefficients from the higher degree
        # summand.
        coefs += self.coefficients[common:] + other.coefficients[common:]

        return Polynomial(coefs)

    else:
        return NotImplemented
    
  def __radd__(self, other):
    return self + other 
  
  def __sub__(self, other):
    """Subtract another polynomial or a scalar from this polynomial."""
    if isinstance(other, (int, float)):  # If subtracting a number
        return Polynomial((self.coefficients[0] - other, *self.coefficients[1:]))
    elif isinstance(other, Polynomial):  # If subtracting another polynomial
        common = min(len(self.coefficients), len(other.coefficients))
        coefs = tuple(a - b for a, b in zip(self.coefficients[:common], other.coefficients[:common]))
        coefs += self.coefficients[common:] + tuple(-b for b in other.coefficients[common:])
        return Polynomial(coefs)
    return NotImplemented

  def __rsub__(self, other):
    """Reverse subtraction: scalar - Polynomial"""
    if isinstance(other, (int, float)):
        return Polynomial((other,)) - self  # Convert scalar to polynomial and subtract
    return NotImplemented

  def __mul__(self, other):
    """Multiply polynomial by another polynomial or a scalar."""
    if isinstance(other, (int, float)):  # If multiplying by a number
        return Polynomial(tuple(c * other for c in self.coefficients))
    elif isinstance(other, Polynomial):  # If multiplying by another polynomial
        coefs = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                coefs[i + j] += a * b
        return Polynomial(tuple(coefs))
    return NotImplemented

  def __rmul__(self, other):
    """Reverse multiplication: scalar * Polynomial"""
    return self.__mul__(other)  # Just call __mul__ since multiplication is commutative


  def __pow__(self, exponent):
    """Exponentiate the polynomial to a positive integer power."""
    if not isinstance(exponent, Integral) or exponent < 0:
        raise ValueError("Exponent must be a non-negative integer.")
    
    result = Polynomial((1,))  # Start with the polynomial "1"
    for _ in range(exponent):
        result *= self  # Multiply repeatedly
    return result

  def __call__(self, x):
    """Evaluate the polynomial at a given scalar x."""
    return sum(c * (x ** i) for i, c in enumerate(self.coefficients))



  def dx(self):
    """Compute the derivative of the polynomial."""
    if len(self.coefficients) <= 1:
        return Polynomial((0,))  # The derivative of a constant is 0

    # Compute the derivative coefficients
    new_coefs = tuple(i * c for i, c in enumerate(self.coefficients[1:], start=1))
    
    return Polynomial(new_coefs)
