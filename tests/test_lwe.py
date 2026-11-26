from src.lwe import matrix_vector_multiply, add_error_vector, calculate_lwe, module_matrix_vector_multiply, add_polynomial_error_vector, calculate_module_lwe


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
    
    
def test_module_matrix_vector_multiply():
    matrix = [
        [[1, 1], [2]],
        [[0, 1], [1, 1]]
    ]

    vector = [
        [1, 1],
        [2, 1]
    ]

    result = module_matrix_vector_multiply(
        matrix, vector, degree=2
    )

    assert result == [
        [4, 4],
        [0, 4]
    ]
    
    
def test_add_polynomial_error_vector():
    result = [
        [1, 2],
        [3, 4]
    ]

    error = [
        [2, 1],
        [1, 2]
    ]

    final_result = add_polynomial_error_vector(result, error)

    assert final_result == [
        [3, 3],
        [4, 6]
    ]


def test_add_polynomial_error_vector_modulo():
    result = [
        [3328, 10]
    ]

    error = [
        [2, -3]
    ]

    final_result = add_polynomial_error_vector(result, error)

    assert final_result == [
        [1, 7]
    ]


def test_add_polynomial_error_vector_different_lengths():
    result = [[1, 2], [3, 4]]
    error = [[1, 2]]

    try:
        add_polynomial_error_vector(result, error)
        assert False
    except ValueError:
        assert True
        
        
def test_calculate_module_lwe():
    matrix = [
        [[1, 1], [2]],
        [[0, 1], [1, 1]]
    ]

    secret = [
        [1, 1],
        [2, 1]
    ]

    error = [
        [-1, 0],
        [1, -1]
    ]

    result = calculate_module_lwe(
        matrix, secret, error, degree=2
    )

    assert result == [
        [3, 4],
        [1, 3]
    ]
    
    
def test_module_matrix_vector_multiply_invalid_dimensions():
    matrix = [
        [[1, 1], [2]],
        [[0, 1]]
    ]

    vector = [
        [1, 1],
        [2, 1]
    ]

    try:
        module_matrix_vector_multiply(matrix, vector, degree=2)
        assert False
    except ValueError:
        assert True
        
    
    
def test_module_matrix_vector_multiply_polynomial_too_large():
    matrix = [
        [[1, 2, 3]]
    ]

    vector = [
        [1, 2]
    ]

    try:
        module_matrix_vector_multiply(
            matrix, vector, degree=2
        )
        assert False
    except ValueError:
        assert True
        
        
def test_add_polynomial_error_vector_different_polynomial_lengths():
    result = [
        [1, 2],
        [3, 4]
    ]

    error = [
        [1],
        [2, 3]
    ]

    try:
        add_polynomial_error_vector(result, error)
        assert False
    except ValueError:
        assert True