from src.lwe import matrix_vector_multiply


def test_matrix_vector_multiply():
    matrix = [
        [1, 2],
        [3, 4]
    ]

    vector = [2, 3]

    result = matrix_vector_multiply(matrix, vector)

    assert result == [8, 18]


def test_matrix_vector_multiply_modulo():
    matrix = [
        [3328, 2],
        [3, 4]
    ]

    vector = [2, 3]

    result = matrix_vector_multiply(matrix, vector)

    assert result == [4, 18]