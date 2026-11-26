from src.polynomial import add_polynomials, multiply_polynomials_in_ring


def matrix_vector_multiply(matrix, vector, modulus=3329):
    """
    Multiply a matrix by a vector.
    Apply the modulus to each result.
    """

    result = []

    # Go through each row of the matrix.
    for row in matrix:

        total = 0

        # Multiply each matrix value by its vector value.
        for i in range(len(vector)):
            total += row[i] * vector[i]

        # Apply the modulus.
        result.append(total % modulus)

    return result


def add_error_vector(result, error, modulus=3329):
    """
    Add an error vector to a result vector.
    Apply the modulus to each value.
    """

    # Both vectors must have the same length.
    if len(result) != len(error):
        raise ValueError("Vectors must have the same length.")

    final_result = []

    # Add corresponding values.
    for i in range(len(result)):
        value = (result[i] + error[i]) % modulus
        final_result.append(value)

    return final_result


def calculate_lwe(matrix, secret, error, modulus=3329):
    """
    Calculate the basic LWE equation:
    b = A*s + e (mod q).
    """

    # Calculate A multiplied by the secret vector.
    result = matrix_vector_multiply(matrix, secret, modulus)

    # Add the error vector.
    final_result = add_error_vector(result, error, modulus)

    return final_result


def module_matrix_vector_multiply(matrix, vector, modulus=3329, degree=256):
    """
    Multiply a matrix of polynomials by a vector of polynomials.
    All polynomial operations happen inside the polynomial ring.
    """

    result = []

    # Go through each row of the matrix.
    for row in matrix:

        # Check that the row and vector have matching lengths.
        if len(row) != len(vector):
            raise ValueError("Matrix and vector dimensions do not match.")

        # Start with a zero polynomial.
        total = [0] * degree

        # Multiply corresponding polynomials.
        for i in range(len(vector)):

            product = multiply_polynomials_in_ring(
                row[i], vector[i], modulus, degree
            )

            # Add the product to the running total.
            total = add_polynomials(total, product, modulus)

        result.append(total)

    return result