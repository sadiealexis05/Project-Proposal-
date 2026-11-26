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

    # Check matrix dimensions and polynomial sizes.
    for row in matrix:

        if len(row) != len(vector):
            raise ValueError("Matrix and vector dimensions do not match.")

        for polynomial in row:
            if len(polynomial) > degree:
                raise ValueError("Polynomial exceeds the allowed degree.")

    # Check secret polynomial sizes.
    for polynomial in vector:
        if len(polynomial) > degree:
            raise ValueError("Polynomial exceeds the allowed degree.")

    # Multiply each row by the polynomial vector.
    for row in matrix:

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


def add_polynomial_error_vector(result, error, modulus=3329):
    """
    Add two vectors containing polynomials.
    Apply the modulus to each coefficient.
    """

    # Both vectors must have the same length.
    if len(result) != len(error):
        raise ValueError("Vectors must have the same length.")

    final_result = []

    # Add corresponding polynomials.
    for i in range(len(result)):

        # Polynomials must have matching lengths.
        if len(result[i]) != len(error[i]):
            raise ValueError("Polynomials must have the same length.")

        polynomial_sum = add_polynomials(
            result[i], error[i], modulus
        )

        final_result.append(polynomial_sum)

    return final_result

def calculate_module_lwe(matrix, secret, error, modulus=3329, degree=256):
    """
    Calculate Module-LWE:
    b = A*s + e (mod q).

    Matrix multiplication and addition happen
    inside the polynomial ring.
    """

    # Multiply the polynomial matrix by the secret vector.
    result = module_matrix_vector_multiply(
        matrix, secret, modulus, degree
    )

    # Add the polynomial error vector.
    final_result = add_polynomial_error_vector(
        result, error, modulus
    )

    return final_result