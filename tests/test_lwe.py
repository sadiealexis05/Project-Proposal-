from src.lwe import matrix_vector_multiply, add_error_vector, calculate_lwe


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
    
    
    from src.lwe import add_error_vector


def test_add_error_vector():
    result = [10, 20, 30]
    error = [1, -2, 3]

    final_result = add_error_vector(result, error)

    assert final_result == [11, 18, 33]


def test_add_error_vector_modulo():
    result = [3328, 10]
    error = [2, -3]

    final_result = add_error_vector(result, error)

    assert final_result == [1, 7]


def test_add_error_vector_different_lengths():
    result = [10, 20]
    error = [1, 2, 3]

    try:
        add_error_vector(result, error)
        assert False
    except ValueError:
        assert True
        


def test_calculate_lwe():
    matrix = [
        [1, 2],
        [3, 4]
    ]

    secret = [2, 3]
    error = [1, -2]

    result = calculate_lwe(matrix, secret, error)

    assert result == [9, 16]


def test_calculate_lwe_modulo():
    matrix = [
        [3328, 2]
    ]

    secret = [2, 3]
    error = [2]

    result = calculate_lwe(matrix, secret, error)

    assert result == [6]
    
def test_professor_example():
    matrix = [
        [0, 0, 2418, 23],
        [12, 241, 2415, 23],
        [19, 483, 2413, 23],
        [27, 724, 2410, 22]
    ]

    secret = [0, 1, 1, 1]
    error = [-2, 0, 1, 0]

    result = calculate_lwe(matrix, secret, error)

    assert result == [2439, 2679, 2920, 3156]