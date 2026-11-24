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