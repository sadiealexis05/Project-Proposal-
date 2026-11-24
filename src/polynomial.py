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