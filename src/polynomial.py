def add_polynomials(poly_a, poly_b, modulus=3329):
    """
    Add two polynomials coefficient by coefficient.
    Return the result modulo q.
    """

    # Polynomials must have the same number of coefficients.
    if len(poly_a) != len(poly_b):
        raise ValueError("Polynomials must have the same length.")

    result = []

    for i in range(len(poly_a)):
        coefficient = (poly_a[i] + poly_b[i]) % modulus
        result.append(coefficient)

    return result


def multiply_polynomials(poly_a, poly_b, modulus=3329):
    """
    Multiply two polynomials.
    Return the coefficients modulo q.
    """

    # Handle empty polynomials.
    if len(poly_a) == 0 or len(poly_b) == 0:
        return []

    # Create a result list filled with zeros.
    result = [0] * (len(poly_a) + len(poly_b) - 1)

    # Multiply each coefficient.
    for i in range(len(poly_a)):
        for j in range(len(poly_b)):
            result[i + j] += poly_a[i] * poly_b[j]

    # Apply the modulus to every coefficient.
    for i in range(len(result)):
        result[i] = result[i] % modulus

    return result

def reduce_polynomial(poly, modulus=3329, degree=256):
    """
    Reduce a polynomial modulo x^degree + 1.
    Also reduce coefficients modulo q.
    """

    # Create a list with exactly 'degree' coefficients.
    result = [0] * degree

    # Process every coefficient.
    for i in range(len(poly)):

        # Find the position after reduction.
        position = i % degree

        # Determine whether the term changes sign.
        sign = (-1) ** (i // degree)

        # Add the coefficient to the correct position.
        result[position] += sign * poly[i]

    # Apply the coefficient modulus.
    for i in range(degree):
        result[i] = result[i] % modulus

    return result


def multiply_polynomials_in_ring(poly_a, poly_b, modulus=3329, degree=256):
    """
    Multiply two polynomials inside the ring:
    Z_q[x] / (x^degree + 1).
    """

    # First, multiply the polynomials normally.
    product = multiply_polynomials(poly_a, poly_b, modulus)

    # Then reduce the product to the required degree.
    result = reduce_polynomial(product, modulus, degree)

    return result