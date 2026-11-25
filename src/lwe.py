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